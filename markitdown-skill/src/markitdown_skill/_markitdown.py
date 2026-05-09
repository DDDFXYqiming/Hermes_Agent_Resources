import mimetypes
import os
import re
import sys
import shutil
import io
from dataclasses import dataclass
from typing import Any, List, Dict, Optional, Union, BinaryIO
from pathlib import Path
from urllib.parse import urlparse
import requests
import magika
import charset_normalizer
import codecs

from ._stream_info import StreamInfo
from ._uri_utils import parse_data_uri, file_uri_to_path

from .converters import (
    PlainTextConverter,
    HtmlConverter,
    RssConverter,
    WikipediaConverter,
    YouTubeConverter,
    IpynbConverter,
    BingSerpConverter,
    PdfConverter,
    DocxConverter,
    XlsxConverter,
    XlsConverter,
    PptxConverter,
    ImageConverter,
    AudioConverter,
    OutlookMsgConverter,
    ZipConverter,
    EpubConverter,
    CsvConverter,
)

from ._base_converter import DocumentConverter, DocumentConverterResult

from ._exceptions import (
    FileConversionException,
    UnsupportedFormatException,
    FailedConversionAttempt,
)


# Lower priority values are tried first.
PRIORITY_SPECIFIC_FILE_FORMAT = 0.0   # e.g., .docx, .pdf, .xlsx, Or specific pages
PRIORITY_GENERIC_FILE_FORMAT = 10.0   # Near catch-all converters for mimetypes like text/*, etc.


@dataclass(kw_only=True, frozen=True)
class ConverterRegistration:
    """A registration of a converter with its priority and other metadata."""

    converter: DocumentConverter
    priority: float


class MarkItDown:
    """Self-contained document-to-Markdown converter for DeepSeek Agent Skill.
    No external LLM / API key required. Image descriptions are delegated to the agent.
    """

    def __init__(
        self,
        *,
        requests_session: Optional[requests.Session] = None,
        exiftool_path: Optional[str] = None,
    ):
        requests_session = requests_session or requests.Session()
        requests_session.headers.update({
            "Accept": "text/markdown, text/html;q=0.9, text/plain;q=0.8, */*;q=0.1"
        })
        self._requests_session = requests_session

        self._magika = magika.Magika()

        # Exiftool path resolution
        self._exiftool_path: Union[str, None] = exiftool_path
        if self._exiftool_path is None:
            self._exiftool_path = os.getenv("EXIFTOOL_PATH")
        if self._exiftool_path is None:
            candidate = shutil.which("exiftool")
            if candidate:
                candidate = os.path.abspath(candidate)
                if any(
                    d == os.path.dirname(candidate)
                    for d in [
                        "/usr/bin", "/usr/local/bin", "/opt", "/opt/bin",
                        "/opt/local/bin", "/opt/homebrew/bin",
                        "C:\\Windows\\System32", "C:\\Program Files",
                        "C:\\Program Files (x86)",
                    ]
                ):
                    self._exiftool_path = candidate

        # Converter registry
        self._converters: List[ConverterRegistration] = []
        self._enable_builtins()

    def _enable_builtins(self) -> None:
        """Register all built-in converters."""

        # Register converters. Later registrations are tried first (higher priority).
        # Most specific converters should appear below the most generic converters.
        self.register_converter(PlainTextConverter(), priority=PRIORITY_GENERIC_FILE_FORMAT)
        self.register_converter(ZipConverter(markitdown=self), priority=PRIORITY_GENERIC_FILE_FORMAT)
        self.register_converter(HtmlConverter(), priority=PRIORITY_GENERIC_FILE_FORMAT)
        self.register_converter(RssConverter())
        self.register_converter(WikipediaConverter())
        self.register_converter(YouTubeConverter())
        self.register_converter(BingSerpConverter())
        self.register_converter(DocxConverter())
        self.register_converter(XlsxConverter())
        self.register_converter(XlsConverter())
        self.register_converter(PptxConverter())
        self.register_converter(AudioConverter())
        self.register_converter(ImageConverter())
        self.register_converter(IpynbConverter())
        self.register_converter(PdfConverter())
        self.register_converter(OutlookMsgConverter())
        self.register_converter(EpubConverter())
        self.register_converter(CsvConverter())

    def convert(
        self,
        source: Union[str, requests.Response, Path, BinaryIO],
        *,
        stream_info: Optional[StreamInfo] = None,
        **kwargs: Any,
    ) -> DocumentConverterResult:
        """
        Args:
            - source: can be a path (str or Path), url, or a requests.response object
            - stream_info: optional stream info to use for the conversion. If None, infer from source
            - kwargs: additional arguments to pass to the converter
        """

        if isinstance(source, str):
            if (
                source.startswith("http:")
                or source.startswith("https:")
                or source.startswith("file:")
                or source.startswith("data:")
            ):
                _kwargs = {k: v for k, v in kwargs.items()}
                if "url" in _kwargs:
                    _kwargs["mock_url"] = _kwargs["url"]
                    del _kwargs["url"]
                return self.convert_uri(source, stream_info=stream_info, **_kwargs)
            else:
                return self.convert_local(source, stream_info=stream_info, **kwargs)
        elif isinstance(source, Path):
            return self.convert_local(source, stream_info=stream_info, **kwargs)
        elif isinstance(source, requests.Response):
            return self.convert_response(source, stream_info=stream_info, **kwargs)
        elif (
            hasattr(source, "read")
            and callable(source.read)
            and not isinstance(source, io.TextIOBase)
        ):
            return self.convert_stream(source, stream_info=stream_info, **kwargs)
        else:
            raise TypeError(
                f"Invalid source type: {type(source)}. Expected str, requests.Response, BinaryIO."
            )

    def convert_local(
        self,
        path: Union[str, Path],
        *,
        stream_info: Optional[StreamInfo] = None,
        file_extension: Optional[str] = None,
        url: Optional[str] = None,
        **kwargs: Any,
    ) -> DocumentConverterResult:
        if isinstance(path, Path):
            path = str(path)

        base_guess = StreamInfo(
            local_path=path,
            extension=os.path.splitext(path)[1],
            filename=os.path.basename(path),
        )

        if stream_info is not None:
            base_guess = base_guess.copy_and_update(stream_info)
        if file_extension is not None:
            base_guess = base_guess.copy_and_update(extension=file_extension)
        if url is not None:
            base_guess = base_guess.copy_and_update(url=url)

        with open(path, "rb") as fh:
            guesses = self._get_stream_info_guesses(file_stream=fh, base_guess=base_guess)
            return self._convert(file_stream=fh, stream_info_guesses=guesses, **kwargs)

    def convert_stream(
        self,
        stream: BinaryIO,
        *,
        stream_info: Optional[StreamInfo] = None,
        file_extension: Optional[str] = None,
        url: Optional[str] = None,
        **kwargs: Any,
    ) -> DocumentConverterResult:
        guesses: List[StreamInfo] = []

        base_guess = None
        if stream_info is not None or file_extension is not None or url is not None:
            if stream_info is None:
                base_guess = StreamInfo()
            else:
                base_guess = stream_info
            if file_extension is not None:
                assert base_guess is not None
                base_guess = base_guess.copy_and_update(extension=file_extension)
            if url is not None:
                assert base_guess is not None
                base_guess = base_guess.copy_and_update(url=url)

        if not stream.seekable():
            buffer = io.BytesIO()
            while True:
                chunk = stream.read(4096)
                if not chunk:
                    break
                buffer.write(chunk)
            buffer.seek(0)
            stream = buffer

        guesses = self._get_stream_info_guesses(
            file_stream=stream, base_guess=base_guess or StreamInfo()
        )
        return self._convert(file_stream=stream, stream_info_guesses=guesses, **kwargs)

    def convert_url(
        self,
        url: str,
        *,
        stream_info: Optional[StreamInfo] = None,
        file_extension: Optional[str] = None,
        mock_url: Optional[str] = None,
        **kwargs: Any,
    ) -> DocumentConverterResult:
        """Alias for convert_uri()"""
        return self.convert_uri(
            url,
            stream_info=stream_info,
            file_extension=file_extension,
            mock_url=mock_url,
            **kwargs,
        )

    def convert_uri(
        self,
        uri: str,
        *,
        stream_info: Optional[StreamInfo] = None,
        file_extension: Optional[str] = None,
        mock_url: Optional[str] = None,
        **kwargs: Any,
    ) -> DocumentConverterResult:
        uri = uri.strip()

        if uri.startswith("file:"):
            netloc, path = file_uri_to_path(uri)
            if netloc and netloc != "localhost":
                raise ValueError(
                    f"Unsupported file URI: {uri}. Netloc must be empty or localhost."
                )
            return self.convert_local(
                path,
                stream_info=stream_info,
                file_extension=file_extension,
                url=mock_url,
                **kwargs,
            )
        elif uri.startswith("data:"):
            mimetype, attributes, data = parse_data_uri(uri)
            base_guess = StreamInfo(
                mimetype=mimetype,
                charset=attributes.get("charset"),
            )
            if stream_info is not None:
                base_guess = base_guess.copy_and_update(stream_info)
            return self.convert_stream(
                io.BytesIO(data),
                stream_info=base_guess,
                file_extension=file_extension,
                url=mock_url,
                **kwargs,
            )
        elif uri.startswith("http:") or uri.startswith("https:"):
            response = self._requests_session.get(uri, stream=True)
            response.raise_for_status()
            return self.convert_response(
                response,
                stream_info=stream_info,
                file_extension=file_extension,
                url=mock_url,
                **kwargs,
            )
        else:
            raise ValueError(
                f"Unsupported URI scheme: {uri.split(':')[0]}. Supported schemes are: file:, data:, http:, https:"
            )

    def convert_response(
        self,
        response: requests.Response,
        *,
        stream_info: Optional[StreamInfo] = None,
        file_extension: Optional[str] = None,
        url: Optional[str] = None,
        **kwargs: Any,
    ) -> DocumentConverterResult:
        mimetype: Optional[str] = None
        charset: Optional[str] = None

        if "content-type" in response.headers:
            parts = response.headers["content-type"].split(";")
            mimetype = parts.pop(0).strip()
            for part in parts:
                if part.strip().startswith("charset="):
                    _charset = part.split("=")[1].strip()
                    if len(_charset) > 0:
                        charset = _charset

        filename: Optional[str] = None
        extension: Optional[str] = None
        if "content-disposition" in response.headers:
            m = re.search(r"filename=([^;]+)", response.headers["content-disposition"])
            if m:
                filename = m.group(1).strip("\"'")
                _, _extension = os.path.splitext(filename)
                if len(_extension) > 0:
                    extension = _extension

        if filename is None:
            parsed_url = urlparse(response.url)
            _, _extension = os.path.splitext(parsed_url.path)
            if len(_extension) > 0:
                filename = os.path.basename(parsed_url.path)
                extension = _extension

        base_guess = StreamInfo(
            mimetype=mimetype,
            charset=charset,
            filename=filename,
            extension=extension,
            url=response.url,
        )

        if stream_info is not None:
            base_guess = base_guess.copy_and_update(stream_info)
        if file_extension is not None:
            base_guess = base_guess.copy_and_update(extension=file_extension)
        if url is not None:
            base_guess = base_guess.copy_and_update(url=url)

        buffer = io.BytesIO()
        for chunk in response.iter_content(chunk_size=512):
            buffer.write(chunk)
        buffer.seek(0)

        guesses = self._get_stream_info_guesses(file_stream=buffer, base_guess=base_guess)
        return self._convert(file_stream=buffer, stream_info_guesses=guesses, **kwargs)

    def _convert(
        self, *, file_stream: BinaryIO, stream_info_guesses: List[StreamInfo], **kwargs
    ) -> DocumentConverterResult:
        res: Union[None, DocumentConverterResult] = None
        failed_attempts: List[FailedConversionAttempt] = []

        sorted_registrations = sorted(self._converters, key=lambda x: x.priority)
        cur_pos = file_stream.tell()

        for stream_info in stream_info_guesses + [StreamInfo()]:
            for converter_registration in sorted_registrations:
                converter = converter_registration.converter
                assert cur_pos == file_stream.tell(), \
                    "File stream position should NOT change between guess iterations"

                _kwargs = {k: v for k, v in kwargs.items()}

                # Always pass exiftool_path if configured
                if "exiftool_path" not in _kwargs and self._exiftool_path is not None:
                    _kwargs["exiftool_path"] = self._exiftool_path

                # Add parent converters for nested processing (e.g., ZIP)
                _kwargs["_parent_converters"] = self._converters

                # Legacy kwargs
                if stream_info is not None:
                    if stream_info.extension is not None:
                        _kwargs["file_extension"] = stream_info.extension
                    if stream_info.url is not None:
                        _kwargs["url"] = stream_info.url

                _accepts = False
                try:
                    _accepts = converter.accepts(file_stream, stream_info, **_kwargs)
                except NotImplementedError:
                    pass

                assert cur_pos == file_stream.tell(), \
                    f"{type(converter).__name__}.accept() should NOT change the file_stream position"

                if _accepts:
                    try:
                        res = converter.convert(file_stream, stream_info, **_kwargs)
                    except Exception:
                        failed_attempts.append(
                            FailedConversionAttempt(
                                converter=converter, exc_info=sys.exc_info()
                            )
                        )
                    finally:
                        file_stream.seek(cur_pos)

                if res is not None:
                    res.text_content = "\n".join(
                        [line.rstrip() for line in re.split(r"\r?\n", res.text_content)]
                    )
                    res.text_content = re.sub(r"\n{3,}", "\n\n", res.text_content)
                    return res

        if len(failed_attempts) > 0:
            raise FileConversionException(attempts=failed_attempts)

        raise UnsupportedFormatException(
            "Could not convert stream to Markdown. No converter attempted a conversion, "
            "suggesting that the filetype is simply not supported."
        )

    def register_converter(
        self,
        converter: DocumentConverter,
        *,
        priority: float = PRIORITY_SPECIFIC_FILE_FORMAT,
    ) -> None:
        """
        Register a DocumentConverter with a given priority.

        Priorities work as follows: By default, most converters get priority
        PRIORITY_SPECIFIC_FILE_FORMAT (== 0). The exception is the
        PlainTextConverter, HtmlConverter, and ZipConverter, which get
        priority PRIORITY_GENERIC_FILE_FORMAT (== 10), with lower values
        being tried first (i.e., higher priority).

        Just prior to conversion, the converters are sorted by priority, using
        a stable sort. This means that converters with the same priority will
        remain in the same order, with the most recently registered converters
        appearing first.
        """
        self._converters.insert(
            0, ConverterRegistration(converter=converter, priority=priority)
        )

    def _get_stream_info_guesses(
        self, file_stream: BinaryIO, base_guess: StreamInfo
    ) -> List[StreamInfo]:
        """
        Given a base guess, attempt to guess or expand on the stream info
        using the stream content (via magika).
        """
        guesses: List[StreamInfo] = []

        enhanced_guess = base_guess.copy_and_update()

        if base_guess.mimetype is None and base_guess.extension is not None:
            _m, _ = mimetypes.guess_type("placeholder" + base_guess.extension, strict=False)
            if _m is not None:
                enhanced_guess = enhanced_guess.copy_and_update(mimetype=_m)

        if base_guess.mimetype is not None and base_guess.extension is None:
            _e = mimetypes.guess_all_extensions(base_guess.mimetype, strict=False)
            if len(_e) > 0:
                enhanced_guess = enhanced_guess.copy_and_update(extension=_e[0])

        cur_pos = file_stream.tell()
        try:
            result = self._magika.identify_stream(file_stream)
            if result.status == "ok" and result.prediction.output.label != "unknown":
                charset = None
                if result.prediction.output.is_text:
                    file_stream.seek(cur_pos)
                    stream_page = file_stream.read(4096)
                    charset_result = charset_normalizer.from_bytes(stream_page).best()
                    if charset_result is not None:
                        charset = self._normalize_charset(charset_result.encoding)

                guessed_extension = None
                if len(result.prediction.output.extensions) > 0:
                    guessed_extension = "." + result.prediction.output.extensions[0]

                compatible = True
                if (
                    base_guess.mimetype is not None
                    and base_guess.mimetype != result.prediction.output.mime_type
                ):
                    compatible = False
                if (
                    base_guess.extension is not None
                    and base_guess.extension.lstrip(".")
                    not in result.prediction.output.extensions
                ):
                    compatible = False
                if (
                    base_guess.charset is not None
                    and self._normalize_charset(base_guess.charset) != charset
                ):
                    compatible = False

                if compatible:
                    guesses.append(
                        StreamInfo(
                            mimetype=base_guess.mimetype or result.prediction.output.mime_type,
                            extension=base_guess.extension or guessed_extension,
                            charset=base_guess.charset or charset,
                            filename=base_guess.filename,
                            local_path=base_guess.local_path,
                            url=base_guess.url,
                        )
                    )
                else:
                    guesses.append(enhanced_guess)
                    guesses.append(
                        StreamInfo(
                            mimetype=result.prediction.output.mime_type,
                            extension=guessed_extension,
                            charset=charset,
                            filename=base_guess.filename,
                            local_path=base_guess.local_path,
                            url=base_guess.url,
                        )
                    )
            else:
                guesses.append(enhanced_guess)
        finally:
            file_stream.seek(cur_pos)

        return guesses

    def _normalize_charset(self, charset: str | None) -> str | None:
        if charset is None:
            return None
        try:
            return codecs.lookup(charset).name
        except LookupError:
            return charset
