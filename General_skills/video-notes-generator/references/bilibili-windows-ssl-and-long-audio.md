# Bilibili on Windows: SSL fallback and long-audio transcription

Use this reference when `video_to_notes.py` or yt-dlp has trouble downloading/transcribing a long Bilibili video on Windows, especially when the user still needs a Markdown summary delivered in the current Feishu chat.

## Durable workflow pattern

1. Resolve the Bilibili short link to the canonical BV URL and fetch metadata with yt-dlp.
2. If the standard script hits transient Bilibili SSL EOF/certificate failures, treat that as a fallback path, not a default: retry with the native `yt-dlp.exe --no-check-certificate` rather than a `.cmd` wrapper when Python subprocesses also pass Unicode output paths.
3. Prefer subtitles if available; otherwise download audio only.
4. For long audio or memory-sensitive hosts, do not force a single full-audio Whisper pass. Split audio into bounded chunks, e.g. 10 minutes each, transcribe one chunk at a time, add each chunk's time offset to segment timestamps, and append results to a partial transcript artifact after every chunk.
5. Keep three artifacts:
   - `<BV>_transcript.json` — segment archive with global timestamps.
   - `<BV>_full_text.txt` — readable raw transcript for summarization.
   - `<BV>_chunk_summaries.md` — compact timestamped chunk digests for context-safe note generation.
6. Verify completion before summarizing:
   - Transcript exists and has non-zero segments.
   - `last_end` is close to video duration.
   - Full text has enough characters for the expected duration.
   - Chunk count covers every split audio file.
7. Generate a polished Markdown note from chunk summaries and selected transcript ranges; do not paste the whole raw transcript into the final answer.
8. In Feishu chat, if the user asked to receive the Markdown document, the normal final response can include `MEDIA:/absolute/path/to/file.md` so the gateway sends it as an attachment. Do not call `send_message` during ordinary chat turns.

## Why chunking matters

A full faster-whisper pass over an ~80-minute Bilibili audio file can require large contiguous NumPy allocations and fail on Windows. Chunking reduces peak memory and makes progress recoverable: if one chunk fails, previous chunks are already written and can be verified.

## Verification snippet shape

Future scripts should print or inspect at least:

```json
{
  "segments": 3034,
  "first_start": 1.26,
  "last_end": 4880.71,
  "duration": 4884.5,
  "full_text_chars": 22335
}
```

The exact values vary by video; the check is that `last_end` approximately reaches `duration` and the text length is plausible.
