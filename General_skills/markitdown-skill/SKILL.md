# MarkItDown Skill

**Self-contained DeepSeek Agent Skill** — Convert various file formats to Markdown for agent consumption.

> Based on Microsoft [MarkItDown](https://github.com/microsoft/markitdown).
> No external LLM / API Key required. Image descriptions are handled by the DeepSeek Agent's own multimodal capabilities.

---

## When to Use

**Use this skill when the user asks to read / analyze / convert:**

- Local files: `.pdf` `.docx` `.pptx` `.xlsx` `.xls` `.csv` `.html` `.epub` `.msg` `.ipynb` `.zip` `.jpg` `.png` `.wav` `.mp3`
- Remote URLs: YouTube videos, Wikipedia pages, RSS feeds, web pages
- Binary streams: any supported format from HTTP responses or stdin

**Do NOT use this skill when:**
- The user asks for raw file content (just use `read_file` directly)
- The file format is not in the supported list — inform the user, then try `read_file` for plain text

---

## How to Invoke

### Mode 1: CLI (recommended, most reliable)

```bash
cd markitdown-skill && source .venv/bin/activate && python -m markitdown_skill <file_path>
```

Output goes directly to stdout. The agent reads stdout to get the Markdown text.

### Mode 2: Python API (for programmatic control)

```python
from markitdown_skill import MarkItDown

md = MarkItDown()
result = md.convert("<file_path>")
print(result.markdown)
```

### Initial Setup (first time only)

```bash
cd markitdown-skill && bash install.sh
```

After installation, `.venv/` persists — subsequent calls skip setup.

---

## Output Conventions

Conversion results are written to stdout. **The agent should treat the output as the full document for reading or downstream processing.**

**Special markers:**
- `<!-- embedded_image: data:image/...;base64,... -->` — base64-encoded image data. The agent can analyze this image using its own multimodal capabilities, no external API needed.

---

## Supported Formats

| Format | Extension | Conversion Method |
|--------|-----------|-------------------|
| PDF | `.pdf` | pdfminer + pdfplumber text extraction |
| Word | `.docx` | mammoth (with OMML math → LaTeX) |
| PowerPoint | `.pptx` | python-pptx (shapes, text, charts, tables) |
| Excel | `.xlsx`, `.xls` | pandas + openpyxl / xlrd |
| Images | `.jpg`, `.jpeg`, `.png` | EXIF metadata + base64 embedded marker |
| Audio | `.wav`, `.mp3`, `.m4a`, `.mp4` | EXIF metadata + SpeechRecognition transcription |
| HTML | `.html`, `.htm` | markdownify conversion |
| CSV | `.csv` | pandas → Markdown table |
| EPUB | `.epub` | ebooklib parsing |
| Outlook | `.msg` | olefile parsing |
| Jupyter | `.ipynb` | JSON → Markdown |
| ZIP | `.zip` | recursive traversal |
| YouTube | URL | youtube-transcript-api |
| Wikipedia | URL | API extraction |
| RSS | URL / `.xml` | feedparser |
| Bing SERP | URL | HTML parsing |
| Plain text | `.txt`, `.json`, `.xml`, `.md` etc. | direct pass-through |

---

## Installation

### One-Click (recommended)

```bash
cd markitdown-skill
bash install.sh
```

The script will:
1. Detect Python 3.10+
2. Create a virtual environment `.venv`
3. Install all core dependencies
4. Detect `exiftool` (optional)
5. Verify the installation

### Manual

```bash
cd markitdown-skill
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Usage

### Command Line

```bash
source .venv/bin/activate
python -m markitdown_skill document.pdf              # stdout output
python -m markitdown_skill document.pdf -o out.md    # save to file
cat document.pdf | python -m markitdown_skill         # pipe input
python -m markitdown_skill -x .docx < input.bin       # specify extension
```

### Python API

```python
from markitdown_skill import MarkItDown

md = MarkItDown()

# Local file
result = md.convert("report.pdf")
print(result.markdown)

# URL
result = md.convert("https://example.com/doc.docx")

# Binary stream
with open("data.bin", "rb") as f:
    result = md.convert_stream(f, stream_info=StreamInfo(extension=".xlsx"))
```

### API Methods

| Method | Description |
|--------|-------------|
| `md.convert(source)` | Smart dispatch: auto-detects path/URL/stream/Response |
| `md.convert_local(path)` | Local file path |
| `md.convert_stream(binary_io)` | Binary stream |
| `md.convert_uri(uri)` | file:/http:/https:/data: URIs |
| `md.convert_response(requests.Response)` | HTTP response object |

Return value `DocumentConverterResult`:
- `.markdown` — the converted Markdown text
- `.title` — document title (optional)
- `str(result)` — equivalent to `.markdown`

---

## Differences from Upstream MarkItDown

| Aspect | Upstream | Skill Version |
|--------|----------|---------------|
| **LLM dependency** | requires `openai` + API Key | **none** |
| **Image handling** | GPT-4o Vision API | EXIF + base64 marker, agent handles |
| **PPTX images** | GPT-4o Vision API | alt text preserved, agent handles |
| **Azure Doc Intel** | supported | removed |
| **Plugin system** | 3rd-party entry_points | removed (self-contained) |
| **Install** | `pip install markitdown[all]` | `bash install.sh` one-click |
| **Config** | `OPENAI_API_KEY` required | **zero config** |

---

## Image Handling

For JPG/PNG images and PPTX embedded images, the skill no longer calls an external LLM:

- **EXIF metadata**: if `exiftool` is installed, extracts ImageSize / DateTimeOriginal / GPSPosition etc.
- **Base64 embedded marker**: output includes `<!-- embedded_image: data:image/...;base64,... -->`
- **Agent self-processing**: the DeepSeek Agent discovers this marker and analyzes the image using its own multimodal capabilities

Example output:

```markdown
ImageSize: 1920x1080
DateTimeOriginal: 2025:01:15 14:30:00

<!-- embedded_image: data:image/jpeg;base64,/9j/4AAQSkZJRg... -->
```

---

## Optional Dependencies

6 core dependencies are auto-installed. The following are optional:

| Feature | Extra Dependencies |
|---------|-------------------|
| PDF | `pdfminer.six`, `pdfplumber` |
| Word | `mammoth`, `lxml` |
| Excel | `pandas`, `openpyxl`, `xlrd` |
| PowerPoint | `python-pptx` |
| Audio transcription | `pydub`, `SpeechRecognition` |
| YouTube captions | `youtube-transcript-api` |
| EPUB | `ebooklib` |
| EXIF metadata | `exiftool` (system tool) |

Missing optional dependencies will not cause errors — converters silently skip unavailable functionality.

---

## Security

MarkItDown performs I/O with the privileges of the current process. In untrusted environments:
- Use the narrowest API (`convert_local()`, `convert_stream()`)
- Do NOT pass untrusted URLs to `convert()`

---

## License

MIT License — based on [microsoft/markitdown](https://github.com/microsoft/markitdown)
