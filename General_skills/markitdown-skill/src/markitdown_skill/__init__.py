# SPDX-FileCopyrightText: 2024-present Adam Fourney <adamfo@microsoft.com>
# SPDX-FileCopyrightText: 2025 MarkItDown Skill — self-contained variant for DeepSeek Agent
#   (no external LLM, no Azure, no plugins)
#
# SPDX-License-Identifier: MIT

from .__about__ import __version__
from ._markitdown import (
    MarkItDown,
    PRIORITY_SPECIFIC_FILE_FORMAT,
    PRIORITY_GENERIC_FILE_FORMAT,
)
from ._base_converter import DocumentConverterResult, DocumentConverter
from ._stream_info import StreamInfo
from ._exceptions import (
    MarkItDownException,
    MissingDependencyException,
    FailedConversionAttempt,
    FileConversionException,
    UnsupportedFormatException,
)

__all__ = [
    "__version__",
    "MarkItDown",
    "DocumentConverter",
    "DocumentConverterResult",
    "MarkItDownException",
    "MissingDependencyException",
    "FailedConversionAttempt",
    "FileConversionException",
    "UnsupportedFormatException",
    "StreamInfo",
    "PRIORITY_SPECIFIC_FILE_FORMAT",
    "PRIORITY_GENERIC_FILE_FORMAT",
]
