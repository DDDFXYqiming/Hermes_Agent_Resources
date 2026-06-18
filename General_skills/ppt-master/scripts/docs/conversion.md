# Conversion Tools

## 中文长概览：skill / conversion.md

本文件属于公开技能 `skill` 下的 `conversion.md` 文档，目标是把幻灯片、模板、图表、配图、动画或脚本相关的全部规格统一收纳，便于复用与扩展。
读者对象：通用 AI 助手、内容创作者、设计师，以及需要把研究材料转成演示稿的研发人员。
使用方法：先阅读本中文长概览，确认任务类型与适用场景；再翻到下方对应 H2/H3 英文细则，按保留的命令、参数、字段、模板与代码进行执行；最后按验收要点逐条核对产物。
本文件作为公开共享资源，禁止写入本机绝对路径、个人目录、真实账号、真实密钥、临时下载目录或过细来源索引；如出现必须替换为 [REDACTED] 或抽象描述。
涉及任何投资、法律、医疗等专业建议时，必须保留“不构成专业建议”声明，并以最新公告、最新法规为依据。
下方原始内容是机器可读规范：代码块、表格、JSON/YAML、SVG、HTML、命令、URL、参数名、字段名、模板占位、文件名都按原样保留，不翻译。
- 建议把本文件视作参考手册：先用目录或本概览定位主题，再按主题读对应章节，最后按章节给出的命令、字段、模板执行。
- 执行任何命令或脚本前，请确认运行环境、依赖、当前工作目录和输出路径；执行后用 ls/cat/grep/校验脚本等手段核对产物。
- 若本文件与同一技能下的 SKILL.md 冲突，以 SKILL.md 的目标、约束和验收标准为准。
- 若本文件与同一技能下的子工作流、子模板冲突，以本概览下方的“约束优先级”段为准。
- 如果用户只是要快速回答问题而不是真正执行工具，可以只看本中文长概览；不要为了显得专业而翻译原始字段、参数或命令。
- 本文件不会包含任何具体 UID、AV/BV 号、本地路径或下载链接；所有可识别来源均已抽象为公司公告、监管披露、官方资料、可靠行情源等口径。
- 本文件的执行结果应当可复现、可验证、可分享；任何只存在于本机内存、剪贴板、临时终端的中间产物都不算交付。
- 若某个章节长时间未更新，请先怀疑它可能已过时，再回到原始上游或官方资料核对；不要凭印象执行。
- 若某个工具或服务在当前环境不可用，优先使用本文件中给出的降级方案；不要擅自调用未列入清单的外部接口。
- 若用户提供了额外的输入材料（截图、URL、表格、PDF），请把材料当作当前任务上下文，不要写入本文件以免污染其他使用者的环境。
- 建议把本文件视作参考手册：先用目录或本概览定位主题，再按主题读对应章节，最后按章节给出的命令、字段、模板执行。
- 执行任何命令或脚本前，请确认运行环境、依赖、当前工作目录和输出路径；执行后用 ls/cat/grep/校验脚本等手段核对产物。
- 若本文件与同一技能下的 SKILL.md 冲突，以 SKILL.md 的目标、约束和验收标准为准。
- 若本文件与同一技能下的子工作流、子模板冲突，以本概览下方的“约束优先级”段为准。
- 如果用户只是要快速回答问题而不是真正执行工具，可以只看本中文长概览；不要为了显得专业而翻译原始字段、参数或命令。
- 本文件不会包含任何具体 UID、AV/BV 号、本地路径或下载链接；所有可识别来源均已抽象为公司公告、监管披露、官方资料、可靠行情源等口径。
- 本文件的执行结果应当可复现、可验证、可分享；任何只存在于本机内存、剪贴板、临时终端的中间产物都不算交付。
- 若某个章节长时间未更新，请先怀疑它可能已过时，再回到原始上游或官方资料核对；不要凭印象执行。
- 若某个工具或服务在当前环境不可用，优先使用本文件中给出的降级方案；不要擅自调用未列入清单的外部接口。
- 若用户提供了额外的输入材料（截图、URL、表格、PDF），请把材料当作当前任务上下文，不要写入本文件以免污染其他使用者的环境。
- 建议把本文件视作参考手册：先用目录或本概览定位主题，再按主题读对应章节，最后按章节给出的命令、字段、模板执行。
- 执行任何命令或脚本前，请确认运行环境、依赖、当前工作目录和输出路径；执行后用 ls/cat/grep/校验脚本等手段核对产物。
- 若本文件与同一技能下的 SKILL.md 冲突，以 SKILL.md 的目标、约束和验收标准为准。
- 若本文件与同一技能下的子工作流、子模板冲突，以本概览下方的“约束优先级”段为准。
- 如果用户只是要快速回答问题而不是真正执行工具，可以只看本中文长概览；不要为了显得专业而翻译原始字段、参数或命令。
- 本文件不会包含任何具体 UID、AV/BV 号、本地路径或下载链接；所有可识别来源均已抽象为公司公告、监管披露、官方资料、可靠行情源等口径。
- 本文件的执行结果应当可复现、可验证、可分享；任何只存在于本机内存、剪贴板、临时终端的中间产物都不算交付。
- 若某个章节长时间未更新，请先怀疑它可能已过时，再回到原始上游或官方资料核对；不要凭印象执行。
- 若某个工具或服务在当前环境不可用，优先使用本文件中给出的降级方案；不要擅自调用未列入清单的外部接口。
- 若用户提供了额外的输入材料（截图、URL、表格、PDF），请把材料当作当前任务上下文，不要写入本文件以免污染其他使用者的环境。

### 阅读顺序

1. 阅读本中文长概览，确认任务类型、阅读路径、关键约束。
2. 浏览下方 H2/H3 标题，挑出与当前任务相关的章节。
3. 阅读这些章节，保留所有命令、参数、字段、模板、代码块。
4. 执行前确认依赖、输入、输出；执行后用对应校验脚本核对。

### 验收要点

- 文档结构完整、章节顺序合理、未被无意义切割。
- 涉及脚本、命令、字段的部分可读、可搜索、可复制。
- 涉及安全、隐私、合规的内容写入公开共享要求小节。
- 中文长概览覆盖了关键使用场景、关键风险、关键验收步骤。

### 公开共享要求

- 不要写入本机绝对路径、个人目录、账号标识、真实密钥、临时下载目录或过细来源索引。
- 引用本地材料时使用抽象描述或环境变量占位。
- 含具体 BV/AV 号、UID、本地路径的素材在共享前必须脱敏。
- 任何 token/密钥/连接串在公开版中必须替换为 [REDACTED]。

### 常见问题与排错

- 中文长概览与原始英文细则冲突时，以不破坏工具执行为前提。
- 脚本失败先看环境、依赖、当前目录和输入文件，不要盲目复制输出。
- 数据陈旧或与公告冲突时，重新联网核验并标注日期。
- 用户只要快速回答时只读本概览，不要翻译原始字段。


<!-- zh-main-begin -->

## 中文主体说明：Hermes_Agent_Resources 文档：conversion

- 本文档是通用技能资料。中文部分说明用途、输入、输出、执行步骤、验证标准和注意事项；保留必要英文标识以保证工具可运行。
- 阅读顺序建议：先看本中文说明，确认任务类型和验收标准；再阅读下方原始细则、模板或命令；最后按当前任务补充必要上下文并执行。
- 公开共享要求：不要写入本机绝对路径、个人目录、账号标识、真实密钥、临时下载目录或过细来源索引。若需要引用本地材料，用抽象描述或环境变量占位。

### 中文使用要点

- 先确认用户目标、输入材料、输出格式和验收标准，再选择本文档中的对应流程。
- 所有脚本、命令、字段名、模型名、平台名、文件名和示例代码保持原样，避免破坏可执行性。
- 面向用户的解释、报告、检查清单、风险提示和交付说明应使用中文。
- 遇到英文原文与中文说明冲突时，以不破坏工具执行为前提，优先遵循中文说明中的安全边界和验收要求。
- 完成后必须运行相关验证：语法检查、文件存在性检查、导出结果检查、截图或日志核对、敏感信息扫描。

<!-- zh-main-end -->


> Architecture rationale (why native-Python first with pandoc fallback, why curl_cffi for TLS impersonation): see [docs/technical-design.md "Source Content Conversion"](../../../../docs/technical-design.md#source-content-conversion).

Source conversion tools turn PDFs, documents, slide decks, and web pages into Markdown before project creation.

## `source_to_md/pdf_to_md.py`

### 中文：source_to_md pdf_to_md py

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Recommended first choice for native PDFs（以上为中文意译，具体细节以英文原文为准）。
```bash
python3 scripts/source_to_md/pdf_to_md.py book.pdf
python3 scripts/source_to_md/pdf_to_md.py book.pdf -o output.md
python3 scripts/source_to_md/pdf_to_md.py ./pdfs
python3 scripts/source_to_md/pdf_to_md.py ./pdfs -o ./markdown

# Image extraction control (default: filtered)
python3 scripts/source_to_md/pdf_to_md.py book.pdf --images filtered  # size/quality filters applied
python3 scripts/source_to_md/pdf_to_md.py book.pdf --images all       # extract all images, no filtering
python3 scripts/source_to_md/pdf_to_md.py book.pdf --images none      # skip all images (text only)
```

Use cases:
- Native PDFs exported from Word, PowerPoint, LaTeX, or similar tools
- Privacy-sensitive documents that should stay local
- Fast first-pass extraction before falling back to OCR-heavy tools

Prefer MinerU or another OCR/layout tool when:
- The PDF is scanned or image-based
- Multi-column layout parsing is poor
- Encoding is garbled

Dependency:

```bash
pip install PyMuPDF
```

## `source_to_md/doc_to_md.py`

### 中文：source_to_md doc_to_md py

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Hybrid converter: pure-Python for the common formats, pandoc fallback for the rest（以上为中文意译，具体细节以英文原文为准）。
- Native path (no external binary required)（以上为中文意译，具体细节以英文原文为准）。
- `（以上为中文意译，具体细节以英文原文为准）。
- docx` — via `mammoth`（以上为中文意译，具体细节以英文原文为准）。
- `.html` / `.htm` — via `markdownify` + `beautifulsoup4`
- `.epub` — via `ebooklib` + `markdownify`
- `.ipynb` — via `nbconvert`

Pandoc fallback (only if you need these):
- `.doc`, `.odt`, `.rtf`, `.tex`/`.latex`, `.rst`, `.org`, `.typ`

```bash
python3 scripts/source_to_md/doc_to_md.py lecture.docx
python3 scripts/source_to_md/doc_to_md.py lecture.docx -o output.md
python3 scripts/source_to_md/doc_to_md.py notes.epub
python3 scripts/source_to_md/doc_to_md.py paper.tex -o paper.md  # uses pandoc
```

Dependencies:

```bash
# Native path — always required
pip install mammoth markdownify ebooklib nbconvert beautifulsoup4

# Fallback path — only for .doc/.odt/.rtf/.tex/.rst/.org/.typ
# macOS:   brew install pandoc
# Ubuntu:  sudo apt install pandoc
# Windows: https://pandoc.org/installing.html
```

All paths produce the same output convention: `<input>.md` plus a sibling `<input>_files/` directory containing extracted images with relative references.

## `source_to_md/excel_to_md.py`

### 中文：source_to_md excel_to_md py

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Excel workbook converter for presentation source intake（以上为中文意译，具体细节以英文原文为准）。
- Supported formats（以上为中文意译，具体细节以英文原文为准）。
- `（以上为中文意译，具体细节以英文原文为准）。
- xlsx`（以上为中文意译，具体细节以英文原文为准）。
- `.xlsm`

Unsupported by default:
- `.xls` — resave as `.xlsx` first

```bash
python3 scripts/source_to_md/excel_to_md.py report.xlsx
python3 scripts/source_to_md/excel_to_md.py report.xlsx -o output.md
python3 scripts/source_to_md/excel_to_md.py report.xlsm --max-rows 200 --max-cols 40
```

Behavior:
- preserves workbook and sheet structure in Markdown
- exports visible sheets only
- trims empty outer rows and columns
- propagates merged-cell labels for readable Markdown tables
- exports formula cells as cached values; it does not recalculate formulas

Dependency:

```bash
pip install openpyxl
```

CSV/TSV files are already plain-text table sources and do not require this converter.

## `source_to_md/ppt_to_md.py`

### 中文：source_to_md ppt_to_md py

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Structured PowerPoint-to-Markdown converter for Open XML slide decks（以上为中文意译，具体细节以英文原文为准）。
- Supported formats include（以上为中文意译，具体细节以英文原文为准）。
- `（以上为中文意译，具体细节以英文原文为准）。
- pptx`, `（以上为中文意译，具体细节以英文原文为准）。
- `.ppsx`, `.ppsm`
- `.potx`, `.potm`

```bash
python3 scripts/source_to_md/ppt_to_md.py sales_deck.pptx
python3 scripts/source_to_md/ppt_to_md.py sales_deck.pptx -o output.md
python3 scripts/source_to_md/ppt_to_md.py ./decks
python3 scripts/source_to_md/ppt_to_md.py ./decks -o ./markdown
python3 scripts/source_to_md/ppt_to_md.py template.ppsx -o notes/template.md
```

Behavior:
- extracts slide text in reading order
- converts PowerPoint tables to Markdown tables
- exports embedded pictures to a sibling `_files/` directory
- appends speaker notes when present

Dependency:

```bash
pip install python-pptx
```

Legacy `.ppt` is not parsed directly. Resave it as `.pptx` or export it to PDF first.

## `source_to_md/web_to_md.py`

### 中文：source_to_md web_to_md py

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Convert web pages to Markdown and download images locally（以上为中文意译，具体细节以英文原文为准）。
```bash
python3 scripts/source_to_md/web_to_md.py https://example.com/article
python3 scripts/source_to_md/web_to_md.py https://url1.com https://url2.com
python3 scripts/source_to_md/web_to_md.py -f urls.txt
python3 scripts/source_to_md/web_to_md.py https://example.com -o output.md
```

When `curl_cffi` is installed (included in `requirements.txt`), this script
automatically impersonates a modern Chrome TLS fingerprint, which lets it
fetch WeChat Official Accounts (`mp.weixin.qq.com`) and other sites that
block Python's default TLS fingerprint. No extra flags needed. If
`curl_cffi` is not available, it falls back to plain `requests`.


## `rotate_images.py`

### 中文：rotate_images py

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Fix image EXIF orientation in downloaded or imported assets（以上为中文意译，具体细节以英文原文为准）。
```bash
python3 scripts/rotate_images.py auto projects/xxx_files
python3 scripts/rotate_images.py gen projects/xxx_files
python3 scripts/rotate_images.py fix fixes.json
```

Use this when extracted photos appear sideways after conversion or import.
