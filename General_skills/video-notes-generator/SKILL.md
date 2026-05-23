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
  "https://www.bilibili.com/video/BV1xxxxx"

# Summarize a YouTube video and write outputs to a custom directory
python ~/.hermes/skills/media/video-notes-generator/scripts/video_to_notes.py \
  "https://www.youtube.com/watch?v=xxxxx" -o ./my_notes

# Process a local file with extracted frames for native multimodal analysis
python ~/.hermes/skills/media/video-notes-generator/scripts/video_to_notes.py \
  "/path/to/video.mp4" --frames --frame-interval 30 --max-frames 3
```

## Configuration

### Environment Variables (.env or export)

| Variable | Required | Default | Description |
|---|---|---|---|
| `VIDEO_NOTES_RUNTIME_DIR` | No | `E:\AI_Projects\video-notes-generator-runtime` | Runtime directory for optional `.env`, bins, and downloaded helper assets |
| `VIDEO_NOTES_ENV` | No | `<VIDEO_NOTES_RUNTIME_DIR>/.env` | Optional env file loaded before running |
| `YTDLP` | No | auto-detected `yt-dlp` | Path to yt-dlp executable |
| `FFMPEG` | No | auto-detected `ffmpeg` | Path to ffmpeg executable |
| `TRANSCRIBER_TYPE` | No | `faster-whisper` | Engine selection used by the script when subtitles are unavailable |
| `WHISPER_CPP` | No | auto-detected | Optional whisper.cpp binary path |
| `WHISPER_MODEL` | No | `base` | whisper.cpp model name when using `--transcribe` / whisper.cpp |
| `VIDEO_NOTES_TRANSCRIPT_CHUNK_CHARS` | No | `3200` | Character budget per compact transcript chunk |
| `VIDEO_NOTES_TRANSCRIPT_PREVIEW_CHARS` | No | `1200` | Transcript preview length in final notes |
| `VIDEO_NOTES_MAX_AGENT_FRAMES` | No | `3` | Default maximum extracted frames for agent-safe multimodal analysis |
| `VIDEO_NOTES_FRAME_MAX_WIDTH` | No | `640` | Maximum frame image width after resizing |

### CLI Arguments

| Arg | Description |
|---|---|
| `url` | Required positional argument: video URL (Bilibili, YouTube, Douyin, Kuaishou) or local video file path |
| `-o`, `--output` | Output directory; default `./notes` |
| `--no-subtitle` | Skip subtitle fetching and download/transcribe audio directly |
| `--transcribe` | Force whisper.cpp transcription instead of subtitle-first behavior |
| `--model` | whisper.cpp model name; defaults to `WHISPER_MODEL` or `base` |
| `--frames` | Extract video frames and emit `*_visual_manifest.json` for native multimodal image analysis |
| `--frame-interval` | Seconds between extracted frames; default `30` |
| `--max-frames` | Maximum extracted frames; default `VIDEO_NOTES_MAX_AGENT_FRAMES` (`3` unless overridden) |
| `--print-full-json` | Print full structured JSON to stdout; avoid in Claude Code unless raw JSON is explicitly requested |

Unsupported in this script version: `--url`, `--file`, `--style`, `--format`, and `--quality`. Use the positional `url` argument and let the agent synthesize the final note style from `*_final_notes.md`, `*_chunk_summaries.md`, and optional frames.

## Note Style

This script does not accept a `--style` flag. It produces compact source artifacts (`*_final_notes.md`, `*_chunk_summaries.md`, `*_transcript.json`, and optionally `*_visual_manifest.json`). The agent should transform those artifacts into the user-requested style in the conversation or by editing the generated Markdown.

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

1. **No ffmpeg**: Required system dependency. Install via `apt install ffmpeg` / `brew install ffmpeg` / `choco install ffmpeg`.
2. **No yt-dlp**: Required for URL downloads. Install yt-dlp and optionally set `YTDLP` if it is not on PATH.
3. **Bilibili download fails**: Set Bilibili cookies for restricted videos or videos that require login.
4. **YouTube subtitle missing**: Falls back to audio transcription, which may be slow for long videos.
5. **Frames missing**: Frames are extracted only when `--frames` is passed.
6. **Long video (>2h)**: Automatically chunked and merged, but may take significant time.
7. **Chinese output only**: The generated artifacts are Chinese-oriented; transform the final response manually if the user asks for another language/style.
8. **Old parameters fail**: This script version does not support `--url`, `--file`, `--style`, `--format`, or `--quality`; pass the URL/local file as the positional `url` argument.

## Verification Checklist

After running, verify:
- [ ] Output `.md` integrated notes file exists in the selected output directory
- [ ] Output `.json` transcript file exists for programmatic reuse
- [ ] Output `*_chunk_summaries.md` exists and is read before full transcript JSON
- [ ] Output `*_final_notes.md` exists for user-facing notes
- [ ] Markdown renders correctly (no broken formatting)
- [ ] Frame timestamp sections are present when `--frames` is used
- [ ] Frames directory contains images if `--frames` is used
- [ ] `*_visual_manifest.json` points to existing image files when frames were extracted
- [ ] No more than one frame is passed into any single model request unless the user explicitly asks for deeper visual inspection
- [ ] Native multimodal visual notes are used when image input is supported; OCR fallback is marked if used
- [ ] No error messages in terminal output
