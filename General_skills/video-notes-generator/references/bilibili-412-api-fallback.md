# Bilibili HTTP 412 API fallback

Use this when `yt-dlp` fails on a Bilibili BV URL with `HTTP Error 412: Precondition Failed`, but the public Bilibili metadata API is still reachable. As of skill version 1.2.0, `scripts/video_to_notes.py` performs this fallback automatically for public Bilibili videos.

## Automatic script behavior

1. `get_video_info()` first tries `yt-dlp --dump-json`.
2. If that fails for a Bilibili URL, it fetches `https://api.bilibili.com/x/web-interface/view?bvid=<BV...>` with browser-like `User-Agent` and `Referer`, preserving title, uploader, duration, description, view count, like count, and `cid`.
3. If audio/video download via `yt-dlp` fails, `download_bilibili_via_api()` fetches `x/player/playurl?bvid=<BV...>&cid=<cid>&qn=32&fnval=16&fourk=0`.
4. It selects a small video DASH stream plus the best audio DASH stream, downloads them with `curl -L -k --retry 3` and browser-like headers, then muxes them with `ffmpeg -c copy` into `<output>/<bvid>_bilibili_api/<bvid>_merged.mp4`.
5. The merged MP4 is reused for both transcription and frame extraction, avoiding a second network download.

## Manual fallback pattern

If the automatic path breaks, repeat the same logic manually:

```bash
OUT='temp/bilibili_manual_download'
BVID='BV1xxxxx'
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36'
REF="https://www.bilibili.com/video/$BVID/"
# 1. fetch view metadata and cid with Python urllib
# 2. fetch x/player/playurl and save selected DASH URLs
# 3. curl -L -k --retry 3 -A "$UA" -e "$REF" "$VIDEO_URL" -o "$OUT/video.m4s"
# 4. curl -L -k --retry 3 -A "$UA" -e "$REF" "$AUDIO_URL" -o "$OUT/audio.m4s"
# 5. ffmpeg -y -i "$OUT/video.m4s" -i "$OUT/audio.m4s" -c copy "$OUT/merged.mp4"
```

Then run the skill on `merged.mp4` as a local file if needed.

## Reporting requirement

When this fallback is used, report it transparently: direct `yt-dlp` processing hit Bilibili 412, so the run used Bilibili public APIs plus local muxing, then processed the resulting MP4 through the same skill pipeline. Do not claim the direct `yt-dlp` URL path succeeded.
