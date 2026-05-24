# Bulk visual enrichment for uploader-wide video notes

Use this reference when an uploader/channel-wide video summarization job already has transcript-only notes and must be upgraded with screenshots/key frames and visual analysis.

## Required outcome

For every verified video, produce and verify:

- `*_frames/` with representative screenshots/key frames.
- `*_visual_manifest.json` listing frame paths, timestamps, nearby transcript, and `visual_note` fields.
- `*_visual_analysis.json` or equivalent persisted model output with overall visual summary and per-frame notes.
- Updated `*_final_notes.md` containing:
  - Markdown image embeds for the selected frames.
  - A visual evidence section that combines what is visible in the frame with nearby transcript context.
  - Clear fallback labels if OCR/text-only analysis was used instead of native multimodal vision.
- Regenerated uploader-wide summary/index that includes the visual-enhanced notes, not the old transcript-only files.

## Workflow

1. Inspect the existing notes directory and identify whether visual manifests already exist. Do not assume the first text-only pass satisfied the skill.
2. Extract a small, bounded set of representative frames per video. For short finance videos, three frames around 20%, 50%, and 80% of actual duration usually gives enough evidence without overloading the model.
3. Prefer actual media duration from ffmpeg/ffprobe when extracting frames. Metadata duration can be stale or longer than the downloaded rendition; if ffmpeg reports no frames at a timestamp, retry using actual probed duration.
4. Build a compact contact sheet for each video when analyzing multiple frames. This reduces model calls while preserving per-frame labels. Label each panel with frame index and timestamp.
5. Call the active/native multimodal vision path when available. Ask for strict JSON with:
   - `overall`: video-level visual summary.
   - `frames`: per-frame notes keyed by frame index.
6. Write the parsed visual notes back into the manifest and persist raw/parsed model output in `*_visual_analysis.json` for auditability.
7. Retry only failed visual analyses rather than rerunning the entire batch. Treat timeouts/connection drops as transient and safe to retry.
8. Merge image embeds and visual notes into each final markdown file, then regenerate the channel/uploader summary from the updated final notes. Make the merge idempotent: wrap the inserted visual section in stable HTML comments such as `<!-- VISUAL_ENRICHMENT_START -->` / `<!-- VISUAL_ENRICHMENT_END -->`, strip any previous block before reinserting, and place the section before the existing timeline/summary section so screenshots are visible early in the note.
9. Verify counts before reporting success: verified videos, visual manifests, frame files, visual analyses, final notes with image embeds, and regenerated aggregate files must all match. For a three-frame-per-video pass, assert at least `video_count * 3` Markdown image embeds and `video_count * 3` per-frame visual observations in the regenerated aggregate summary.

## Pitfalls

- Do not stop after extracting frames. The user asked for image content to be analyzed; screenshots alone are incomplete.
- Do not rely on generic browser screenshots for video content. Use actual downloaded video frames with timestamps.
- Do not put raw full transcripts and all images in one model request. Use final notes/chunk summaries plus one contact sheet or one frame at a time.
- Do not hard-code a transient provider failure as a durable limitation. Record the retry/fallback pattern, not the outage.
- Do not claim completion until markdown files and aggregate summary have been rewritten and verified, not merely the intermediate manifests.
- If a bulk visual pass is interrupted after partial vision output, resume from persisted `*_visual_analysis.json` files and retry only missing/failed videos. Do not rerun successful videos unless their frame set or prompt changed.
- Keep an audit artifact for the final merge/verify step (for example `visual_merge_report.json` and `visual_enrichment_verify_report.json`) so the final user report can cite exact counts rather than impressions.
