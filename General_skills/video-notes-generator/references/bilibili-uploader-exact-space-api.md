# Bilibili uploader exact space API playbook

Use this reference when a user asks for **all videos from a specific Bilibili UP/uploader**. General web search is only a candidate source; the primary path should be Bilibili-native data plus per-video owner verification.

## Exact-source priority

1. Parse the uploader `mid` from the space URL.
2. Try Bilibili-native uploader sources before generic search:
   - `yt-dlp --flat-playlist` on the space upload URL;
   - `https://api.bilibili.com/x/space/wbi/arc/search` with WBI signing;
   - Bilibili `search_type=video` only as a Bilibili index source, then filter by `author`/`mid` and verify with yt-dlp.
3. Treat AnySearch/general search as candidate discovery only. It is not an exact source for an uploader's complete video list.
4. Verify every BV with `yt-dlp --skip-download --write-info-json` and accept only if `uploader_id` equals the requested `mid`.

## WBI + buvid pattern for `x/space/wbi/arc/search`

A plain WBI signature may still be banned. A more reliable sequence is:

1. Create a fresh HTTP session with normal browser headers.
2. Warm up first-party pages:
   - `https://www.bilibili.com/`
   - `https://space.bilibili.com/<mid>/upload/video`
3. Fetch `https://api.bilibili.com/x/frontend/finger/spi` and set returned `b_3`/`b_4` as `buvid3`/`buvid4` cookies in the session.
4. Fetch `https://api.bilibili.com/x/web-interface/nav`, extract `wbi_img.img_url` and `wbi_img.sub_url`, compute the mixin key with Bilibili's `mixinKeyEncTab`, then sign request params with `wts` + `w_rid`.
5. Request:
   `https://api.bilibili.com/x/space/wbi/arc/search?mid=<mid>&ps=<ps>&pn=<pn>&tid=0&order=pubdate&platform=web&web_location=1550101&order_avoided=true&...signature...`

Successful responses include `data.page.count` and `data.list.vlist`. Preserve raw successful JSON under metadata for auditability.

## Anti-bot fallback that preserves precision

If `pn=1` or large pages return `-352`, `-412`, or `-799`, do not switch to unverified web search as ground truth. Instead:

- retry later with a fresh session and buvid cookies;
- request smaller pages such as `ps=10`, `ps=5`, `ps=3`, or `ps=1`;
- try different `pn` values because later pages may succeed even when page 1 is banned;
- try category `tid` values reported in a successful response's `tlist`;
- merge all successful `vlist` rows by BV ID;
- verify merged BVs with yt-dlp before summarization.

A useful pattern is that page 2/3/4 with small `ps` may reveal most of the archive while page 1 remains highly protected. If `ps=1` or `ps=3` succeeds for page 1, continue tiny-page retrieval rather than making a large page-1 request.

## Concurrency pitfall

Do not let multiple verifier scripts write the same `verified_all_videos.json` concurrently. A stale broad-candidate verifier can overwrite newer exact-source results. Prefer one of these patterns:

- write each discovery source to a separate file, then run a final merge by scanning all accepted yt-dlp `*.info.json` files;
- or serialize verification and writes through a single script.

The final accepted list should be reconstructable from yt-dlp info JSON files, not only from an incrementally updated JSON file.

## Reporting standard

Report exactness honestly:

- source-reported total count, if known;
- count obtained from exact Bilibili space/index sources;
- count accepted after yt-dlp uploader verification;
- count summarized successfully;
- remaining count and the current blocker, if anti-bot protection prevents full completion.
