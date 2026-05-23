---
name: video-notes-generator
description: "Use when user wants to summarize, analyze, or generate notes from a video URL. Converts video content into structured Markdown notes with timestamps, extracted visual frames, native multimodal image observations, and AI summaries. Supports Bilibili, YouTube, Douyin, Kuaishou, and local files."
version: 1.0.0
author: Diana (extracted from BiliNote v2.2.1 by JefferyHcool)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [video, notes, bilibili, youtube, transcription, summarization]
    related_skills: [youtube-content, gif-search]
---

# Video Notes Generator

> Based on [BiliNote v2.2.1](https://github.com/JefferyHcool/BiliNote) by JefferyHcool.
> No external LLM / API Key required. The Agent itself acts as the LLM for note generation.

Converts video content from URLs or local files into structured, readable Markdown notes using AI. Supports multiple video platforms, transcription engines, note styles, and optional visual frame extraction for native multimodal image understanding.

Extracted from **BiliNote v2.2.1** by JefferyHcool.

## When to Use

Trigger when the user says any of:
- "视频笔记", "视频总结", "视频转笔记"
- "video notes", "summarize video", "video to notes"
- "generate notes from video", "video summary"
- Shares a Bilibili/YouTube/Douyin/Kuaishou URL and asks for notes/summary
- Asks to transcribe or summarize a local video file

## Quick Start

```bash
# Summarize a Bilibili video
python ~/.hermes/skills/media/video-notes-generator/scripts/video_to_notes.py \
  --url "https://www.bilibili.com/video/BV1xxxxx"

# Summarize a YouTube video with detailed style
python ~/.hermes/skills/media/video-notes-generator/scripts/video_to_notes.py \
  --url "https://www.youtube.com/watch?v=xxxxx" --style detailed

# Process a local file with screenshots and AI summary
python ~/.hermes/skills/media/video-notes-generator/scripts/video_to_notes.py \
  --file /path/to/video.mp4 --format link,screenshot,summary
```

## Configuration

### Environment Variables (.env or export)

| Variable | Required | Default | Description |
|---|---|---|---|
| `OPENAI_API_KEY` | Yes | — | API key for LLM (OpenAI-compatible) |
| `OPENAI_BASE_URL` | No | `https://api.openai.com/v1` | LLM API base URL |
| `TRANSCRIBER_TYPE` | No | `fast-whisper` | Engine: `fast-whisper`, `groq`, `bcut`, `kuaishou`, `mlx-whisper` |
| `WHISPER_MODEL_SIZE` | No | `base` | Whisper model: `tiny`, `base`, `small`, `medium`, `large-v3` |
| `GROQ_API_KEY` | No | — | Required if using groq transcriber |
| `GROQ_TRANSCRIBER_MODEL` | No | `whisper-large-v3-turbo` | Groq whisper model |
| `NOTE_OUTPUT_DIR` | No | `./note_results` | Output directory for generated notes |

### CLI Arguments

| Arg | Description |
|---|---|
| `--url` | Video URL (Bilibili, YouTube, Douyin, Kuaishou) |
| `--file` | Path to local video file |
| `--style` | Note style (see below) |
| `--format` | Comma-separated: `toc`, `link`, `screenshot`, `summary` |
| `--quality` | Download quality: `fast`, `normal`, `high` |
| `--frames` | Extract video frames and emit a visual manifest for native multimodal image analysis |
| `--frame-interval` | Seconds between extracted frames; default `30` |
| `--max-frames` | Maximum extracted frames; default `8` |

## Style Reference

| Value | Label | Description |
|---|---|---|
| `minimal` | 精简 | Concise, key points only |
| `detailed` | 详细 | Comprehensive with full discussion |
| `academic` | 学术 | Formal, structured for academic use |
| `tutorial` | 教程 | Step-by-step with key conclusions |
| `xiaohongshu` | 小红书 | Social media style with emojis and hooks |
| `life_journal` | 生活向 | Personal, emotional expression |
| `task_oriented` | 任务导向 | Goals, tasks, action items |
| `business` | 商业风格 | Formal business report style |
| `meeting_minutes` | 会议纪要 | Meeting minutes format |

## Format Options

| Value | Description |
|---|---|
| `toc` | Auto-generate table of contents from `##` headings |
| `link` | Add `*Content-[mm:ss]` timestamp markers to headings |
| `screenshot` | Extract real image frames when `--frames` is used; otherwise insert `*Screenshot-[mm:ss]` markers |
| `summary` | Append an AI-generated summary at the end |

## Platform Support

| Platform | Subtitles | Download | Cookies | Notes |
|---|---|---|---|---|
| Bilibili | ✅ Priority | yt-dlp | Recommended | Subtitle-first; falls back to whisper |
| YouTube | ✅ Priority | yt-dlp | Optional | Prefers existing subtitles |
| Douyin | ❌ | yt-dlp + ABogus | Not needed | Anti-bot bypass built-in |
| Kuaishou | ✅ | yt-dlp + helper | Not needed | Custom downloader |
| Local | N/A | Direct file | N/A | Any format FFmpeg supports |

## Native Multimodal Visual Workflow

When the user asks for image-aware video analysis and the active model supports images:

1. Run the script with `--frames`, plus `--frame-interval` / `--max-frames` as needed.
2. If the active model supports native image input, open each `image_path` directly and analyze the actual frame visually.
3. Fill the summary with visual observations such as scene changes, UI operations, gestures, objects, diagrams, and slide structure.
4. If the active model does **not** support image input, use OCR only as a fallback and clearly mark those notes as OCR-derived rather than native visual understanding.
5. Combine visual observations with `nearby_transcript` and timestamps; do not invent details that are not visible or audible.

The script writes `*_notes.md` as the integrated user-facing note. It keeps `visual_note` blank in JSON on purpose; the agent/model should inspect the actual image files when native multimodal input is available, or use OCR fallback only when image input is unavailable.

## Context-Safe Workflow

The script is designed to avoid Claude Code context overflow:

1. Read `*_final_notes.md` first for the user-facing result.
2. Read `*_chunk_summaries.md` before opening `*_transcript.json`.
3. Do not read the full transcript JSON unless the user explicitly asks for raw transcript details.
4. If more detail is needed, inspect one transcript chunk or one timestamp range at a time.
5. Treat `*_visual_manifest.json` as a compact frame index. Do not open images by default.
6. If visual evidence is required, open at most one frame per model request, summarize it, then continue. Never send multiple images plus transcript together.
7. If a model/API returns a context-window error, retry from `*_chunk_summaries.md` and `*_final_notes.md`; do not resend raw transcript, OCR, and frames together.

The full transcript remains available in `*_transcript.json`, but it is an archive artifact, not the default prompt input.
The CLI prints a short JSON summary by default. Do not use `--print-full-json` inside Claude Code unless the user explicitly asks for raw JSON output.

## Common Pitfalls

1. **Missing OPENAI_API_KEY**: Set it in `.env` or `export` before running. The LLM call will fail without it.
2. **No ffmpeg**: Required system dependency. Install via `apt install ffmpeg` / `brew install ffmpeg` / `choco install ffmpeg`.
3. **Bilibili download fails**: Set Bilibili cookies in config for restricted videos.
4. **YouTube subtitle missing**: Falls back to Whisper transcription — may be slow for long videos.
5. **GPU not detected**: Whisper defaults to CUDA. Set device to `cpu` if no GPU available.
6. **Long video (>2h)**: Automatically chunked and merged, but may take significant time.
7. **Chinese output only**: The prompt is designed for Chinese notes. English output requires prompt customization.
8. **Style not applied**: Ensure `--style` value matches exactly (e.g., `xiaohongshu`, not `xhs`).

## Verification Checklist

After running, verify:
- [ ] Output `.md` integrated notes file exists in `NOTE_OUTPUT_DIR`
- [ ] Output `.json` transcript file exists for programmatic reuse
- [ ] Output `*_chunk_summaries.md` exists and is read before full transcript JSON
- [ ] Output `*_final_notes.md` exists for user-facing notes
- [ ] Markdown renders correctly (no broken formatting)
- [ ] Timestamps (`*Content-[mm:ss]`) are present if `link` format was selected
- [ ] Frames directory contains images if `--frames` / `screenshot` format was selected
- [ ] `*_visual_manifest.json` points to existing image files when frames were extracted
- [ ] No more than one frame is passed into any single model request unless the user explicitly asks for deeper visual inspection
- [ ] Native multimodal visual notes are used when image input is supported; OCR fallback is marked if used
- [ ] AI summary section exists if `summary` format was selected
- [ ] No error messages in terminal output
