# Platform Support

## Supported Platforms

| Platform | Domain | Subtitle Priority | Download Method | Cookie Required | Notes |
|---|---|---|---|---|---|
| Bilibili (B站) | bilibili.com | ✅ Yes | yt-dlp + subtitle fetcher | Recommended | Subtitle-first strategy; cookies needed for restricted content |
| YouTube | youtube.com | ✅ Yes | yt-dlp + subtitle fetcher | Optional | Prefers existing subtitles; skips audio download when subtitles found |
| Douyin (抖音) | douyin.com | ❌ No | yt-dlp + ABogus bypass | Not needed | Anti-bot signature bypass built-in |
| Kuaishou (快手) | kuaishou.com | ✅ Yes | yt-dlp + custom helper | Not needed | Custom downloader with subtitle extraction |
| Local Files | N/A | N/A | Direct file access | N/A | Any format FFmpeg supports (mp4, mkv, avi, webm, etc.) |
| 小宇宙FM | xiaoyuzhou.fm | ❌ No | Custom downloader | Not needed | Podcast platform support |

## Bilibili: Subtitle-First Strategy

Bilibili has a unique optimization: the system **prioritizes existing subtitles** over audio transcription.

**Flow**:
1. Extract video ID from URL
2. Fetch CC/subtitle list via Bilibili API (`BilibiliSubtitleFetcher`)
3. If subtitles exist → parse directly into transcript segments (fast, no Whisper needed)
4. If no subtitles → download audio → transcribe with configured engine

**Cookie configuration**: Set Bilibili cookies (SESSDATA, bili_jct, etc.) for:
- Accessing restricted/会员 content
- Higher quality downloads
- Avoiding rate limits

## YouTube: Subtitle Priority

Similar to Bilibili:
1. `YouTubeSubtitleFetcher` attempts to get auto-generated or manual subtitles
2. If found → uses subtitles directly, sets `skip_download=True` (no audio download)
3. If not found → downloads best audio → transcribes with Whisper/Groq

## Transcription Engines

| Engine | Type | GPU Required | Speed | Quality |
|---|---|---|---|---|
| `fast-whisper` | Local | Optional (CUDA) | Medium | High |
| `mlx-whisper` | Local (macOS) | Apple Silicon | Fast | High |
| `groq` | Cloud API | No | Very Fast | High |
| `bcut` | Cloud (Bilibili) | No | Fast | Medium |
| `kuaishou` | Cloud (Kuaishou) | No | Fast | Medium |

## yt-dlp Requirements

- **Minimum version**: yt-dlp >= 2023.1.0
- **Install**: `pip install yt-dlp` or `pip install -U yt-dlp`
- **Update**: yt-dlp is updated frequently to keep up with platform changes. Run `pip install -U yt-dlp` if downloads fail.

## Known Limitations

1. **Douyin**: No subtitle support; relies entirely on Whisper transcription
2. **Bilibili**: Some 付费 (paid) content requires valid cookies
3. **YouTube**: Age-restricted videos may require cookies
4. **Very long videos (>4h)**: Transcription may be slow; automatic chunking helps but increases total time
5. **Non-Chinese content**: Notes are generated in Chinese regardless of video language (prompt-based)
