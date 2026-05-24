# Bilibili uploader video discovery and verification

Use this when the user asks to summarize all videos from a Bilibili UP/uploader, not just one explicit URL.

## Durable workflow

1. Treat the uploader space URL and `mid` as an identity hint, not as proof that every search result belongs to that uploader.
2. Try the normal uploader archive/list route first (space upload page, `yt-dlp --flat-playlist`, or Bilibili archive APIs when available). For Bilibili web space, the most precise non-login route is usually `https://api.bilibili.com/x/space/wbi/arc/search` with fresh `buvid3`/`buvid4` from `/x/frontend/finger/spi`, WBI keys from `/x/web-interface/nav`, signed params, and conservative pagination. If `ps=30,pn=1` is blocked, retry small pages such as `ps=10,pn=2..4`, `ps=15,pn=2`, `ps=20,pn=2`, and tiny first-page requests (`ps=1..4,pn=1`) with long backoff. Merge successful pages until the unique count matches the API `page.count`.
3. If the archive route is rate-limited or anti-bot challenged, switch to candidate discovery:
   - retry Bilibili `x/space/wbi/arc/search` with warmed browser-like session, `buvid3`/`buvid4` from `x/frontend/finger/spi`, WBI signing from `x/web-interface/nav`, smaller `ps` values, alternate `pn`, and category `tid` values from `tlist`;
   - use Bilibili `search_type=video` as a site-native index source, filtered by `author`/`mid`, then verify each BV;
   - only then use broader candidate discovery: search the uploader name, UID/mid, distinctive channel phrases, and titles/tags from already verified seed videos;
   - use search-engine snippets only as candidate sources, never as final evidence;
   - collect BV IDs into a candidate set.
4. Verify every candidate video with `yt-dlp --skip-download --write-info-json` and accept it only when the metadata uploader identity matches the requested uploader:
   - `uploader_id` equals the requested `mid`, or
   - another reliable owner field in the info JSON proves the same account.
5. Save rejected candidates with their observed uploader/uploader_id so they are not retried or accidentally summarized.
6. Only after a verified list exists should batch-run `video_to_notes.py` over the videos. If the complete list is blocked, clearly report the verified count and optionally proceed on the verified subset while continuing discovery separately.

## Pitfalls

- Bilibili search snippets often match words like “财”, “狐狸”, or finance terms and can return unrelated videos. Do not trust title/query relevance.
- User-card search results may show an uploader’s total video count while only embedding a few sample videos; do not treat the sample list as complete.
- Mobile space SSR can render an empty archive even when search shows videos exist. That is a retrieval limitation, not proof the uploader has no videos.
- WBI signatures may be necessary but not sufficient; anti-bot responses such as HTTP 412, `code:-352`, or `code:-799` require exact fallbacks (fresh session, buvid cookies, smaller pages, alternate pages/categories) before broader candidate discovery. Do not fabricate completeness.
- Generic web search / AnySearch is broad candidate discovery, not an exact uploader archive source; do not present it as the source of “all videos”.
- If multiple verifier scripts run concurrently, avoid shared writes to the same accepted-list JSON. Prefer source-specific files and a final merge from verified yt-dlp `*.info.json` files.
- Known good verification signal from yt-dlp: info JSON fields like `uploader`, `uploader_id`, `title`, `timestamp`, and `duration`.

## Reporting standard

For “all videos from this uploader” tasks, final or checkpoint reports must include:

- requested uploader name and mid/UID;
- number of videos claimed by source pages/search cards, if known;
- number of verified BV IDs actually accepted;
- number of rejected candidates and why;
- the exact output directory containing metadata/notes;
- a truthful blocker statement if anti-bot/rate limits prevented a complete list.
