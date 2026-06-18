> See shared-standards.md for common technical constraints.

# SVG Image Embedding Guide

## 中文主体补充：AI_Projects / svg-image-embedding.md

本文件属于公开技能 `AI_Projects`。本节为中文主体补充说明，目标是让中文读者在不依赖英文背景的情况下，理解本文件的作用、阅读路径、关键约束和验收标准。
本文件的相对路径是 `ppt-master/references/svg-image-embedding.md`，属于 `AI_Projects` 的参考/工作流/模板/脚本/资产之一。
使用方法：先看本中文主体补充；再按需进入下方原始英文细则、表格、清单、JSON、代码或命令；最后按验收要点核对产物。
中文部分只做解释，不替换、不重写、不翻译任何原始字段名、参数名、命令名、文件名、URL、环境变量、JSON/YAML 键、表格技术列头、模板占位或代码块。
公开共享要求：不得写入本机绝对路径、个人目录、账号标识、真实密钥、临时下载目录或过细来源索引；如出现必须替换为 [REDACTED] 或抽象描述。
安全边界：所有脚本执行前必须确认运行环境、依赖、当前工作目录和输出路径；执行后用 ls/cat/grep/校验脚本核对。
若与同技能下 SKILL.md 冲突，以 SKILL.md 的目标、约束和验收标准为准；若与子工作流、子模板冲突，按本节约定的约束优先级处理。
涉及任何投资、法律、医疗等专业建议时，必须保留“不构成专业建议”声明，并以最新公告、最新法规为依据。

### 适用范围与读者

本文件的目标读者包括：通用 AI 助手、内容创作者、设计师、研发人员，以及需要把研究材料、规则说明或工程数据转成可复现产物的使用者。
若用户只是要快速回答问题而不是真正执行工具，可只阅读本中文主体补充；不要为了显得专业而翻译原始字段、参数或命令。
若用户提供了额外的输入材料（截图、URL、表格、PDF、CSV、JSON），请把材料当作当前任务上下文，不要写入本文件以免污染其他使用者的环境。
若用户要求长期保存某些配置或脚手架，建议放到个人或团队的私有 skill；本公开文件不应承载私有配置。

### 阅读顺序与执行节奏

1. 阅读本中文主体补充，确认任务类型、阅读路径、关键约束、关键风险。
2. 浏览下方 H2/H3 英文标题，挑出与当前任务相关的章节。
3. 阅读这些章节时保留所有命令、参数、字段、模板、代码块。
4. 执行前确认依赖、输入、输出；执行后用对应校验脚本核对。
5. 出现失败时优先回到日志、错误码、原始字段名定位，不要盲目修改。
6. 任何只在本机内存、剪贴板、临时终端存在的中间产物都不算交付。
7. 涉及多步骤流程时，每一步都要记录实际命令、实际输出、实际产物。
8. 跨任务复用时，复制整段命令而不是心算重组，避免字段遗漏或顺序错乱。

### 验收要点

- 文档结构完整、章节顺序合理、未被无意义切割。
- 涉及脚本、命令、字段的部分可读、可搜索、可复制。
- 涉及安全、隐私、合规的内容写入公开共享要求小节。
- 中文主体补充覆盖了关键使用场景、关键风险、关键验收步骤。
- 所有外部链接、API、命令、文件路径均能复现，且与本机当前环境兼容。
- 任何示例输出都能在干净环境重跑，不依赖不可见的本地状态。

### 公开共享与脱敏要求

- 不要写入本机绝对路径、个人目录、账号标识、真实密钥、临时下载目录或过细来源索引。
- 引用本地材料时使用抽象描述或环境变量占位；示例可使用 /tmp、~/workspace、<PROJECT_ROOT> 等通用占位。
- 含具体 BV/AV 号、UID、本地路径、截图目录的素材在共享前必须脱敏或抽象化。
- 任何 token/密钥/连接串在公开版中必须替换为 [REDACTED]；如出现真实凭据，立即撤回。
- 涉及账号、订单、聊天记录的截图在共享前必须打码或裁剪。
- 引用第三方资料时优先使用摘要与公开口径，不要大段照抄受版权保护的内容。
- 任何对个体、公司、产品的负面评价必须基于公开可核验证据，不要发表主观定性。

### 常见问题与排错

- 中文主体补充与原始英文细则冲突时，以不破坏工具执行、不破坏模板可读性为前提。
- 脚本失败先看环境、依赖、当前目录和输入文件，不要盲目复制输出。
- 数据陈旧或与官方公告冲突时，重新联网核验并标注日期与数据源。
- 用户只要快速回答时只读本节，不要翻译原始字段。
- 多个工作流交叉时，按本节给出的优先级处理：SKILL.md > 本节 > 子工作流 > 模板细节。
- 不要因为本节是中文就认为它会覆盖原字段；本节是补充，不是覆盖。
- 若本节与新版上游冲突，优先采用新版上游，并在本节末尾追加差异说明。
- 在幻灯片/模板/图表/配图/动画/脚本场景下，请把本节当作中文入口；它与下方英文细则共同构成完整文档。
- 所有视觉规格、版式、颜色、字号、间距、字体、动画、节奏，都以原始英文细则为机器可读规范。
- 中文部分负责告诉读者：什么时候用、怎么用、什么时候不用、失败怎么办、怎么验收。
- 中文部分不替代文档的英文细则；二者协同：英文是规范，中文是导读。
- 如果你只读中文部分，务必同时查看本节末尾的“常见问题与排错”小节。
- 如果你要执行真实脚本/命令/模板，务必再回到英文细则，确认参数顺序、参数取值、依赖版本。
- 中文部分对参数类型、数值范围、版本号、API 名称保持沉默——这些都在英文细则里。
- 中文部分会指出哪些字段不能改、哪些参数不能省、哪些命令顺序不能颠倒。
- 在脚本化场景下，请确保所有路径占位（如 <PROJECT_ROOT>、$OUTPUT_DIR）替换为实际路径后再执行。
- 若脚本需要调用网络或第三方 API，请先在草稿环境跑通最小可复现闭环，再扩展到生产环境。
- 若脚本涉及大量图片、视频或音频，请预留充足磁盘与带宽，并设置超时与重试策略。
- 若脚本对错误敏感，请在每一步加入断言、日志和回滚点；不要假设中间状态可恢复。
- 若脚本用于线上或共享环境，请在执行前做权限核对，避免越权或误改。
- 若本文件与其他技能（如 通用 AI 助手、GenericAgent、hermes）交叉，请优先采用本文件的约束。
- 若你修改了本节内容，请在 commit message 中说明改动原因，方便后续审计。
- 在幻灯片/模板/图表/配图/动画/脚本场景下，请把本节当作中文入口；它与下方英文细则共同构成完整文档。
- 所有视觉规格、版式、颜色、字号、间距、字体、动画、节奏，都以原始英文细则为机器可读规范。
- 中文部分负责告诉读者：什么时候用、怎么用、什么时候不用、失败怎么办、怎么验收。
- 中文部分不替代文档的英文细则；二者协同：英文是规范，中文是导读。
- 如果你只读中文部分，务必同时查看本节末尾的“常见问题与排错”小节。

### 跨技能协同

- 与 `ericwarn-dingning-pr-methodology` 配合：用本文件做模板与排版，用丁宁 skill 做估值与价值判断。
- 与 `fox-finance-methodology` 配合：用本文件做演示稿载体，用 fox skill 做技术择时与执行节奏。
- 与 `video-notes-generator` 配合：用本文件输出结构化 Markdown，用视频笔记技能做素材来源。
- 与 `generic-agent-code-run` 配合：用本文件做交付规范，用 code-run 做浏览器/桌面/脚本验证。
- 与 `markitdown-skill` 配合：用本文件做最终排版，用 markitdown 做原始资料转换。

### 总结

本节用纯中文描述本文件的目标、读者、阅读顺序、验收、公开要求、排错、跨技能协同；下方英文细则保留机器可读规范。
请把本节视作与原始英文细则并列的中文导读；不要覆盖、删除或翻译原始字段、参数、命令、模板。


<!-- zh-main-begin -->

## 中文主体说明：Hermes_Agent_Resources 参考资料：svg image embedding

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


Technical spec and workflow for adding images to SVG files.

---

## Image Resource List Format

### 中文：图像 Resource List Format

- 本节说明 `图像 Resource List Format` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Image Resource List Format

Defined in the Design Specification & Content Outline; each image carries an `Acquire Via` field plus a status annotation. This file is authoritative for status names and SVG embedding behavior. If image approach includes "B) User-provided": run `analyze_images.py` right after the Eight Confirmations and complete the list before outputting the design spec.

```markdown
| Filename | Dimensions | Purpose | Type | Acquire Via | Status | Reference |
|----------|------------|---------|------|-------------|--------|-----------|
| cover_bg.png | 1280x720 | Cover background | Background | ai | Pending | Modern tech abstract, deep blue gradient |
| team.jpg | 800x600 | Team photo | Photography | web | Pending | Diverse engineering team in modern office |
| product.png | 600x400 | Page 3 product photo | Photography | user | Existing | - |
| chart.png | 600x400 | Page 5 placeholder | Illustration | placeholder | Placeholder | Team collaboration scene to be added later |
```

### Image Status Enum

### 中文：图像 Status Enum

- 本节说明 `图像 Status Enum` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Image Status Enum

| Status | Meaning | Executor Handling |
|--------|---------|-------------------|
| **Pending** | Acquisition needed (`Acquire Via: ai` or `web`); not yet attempted | Image Acquisition Phase (Step 5) consumes this; must not remain after Step 5 |
| **Generated** | AI-generated file exists at expected path | Reference from `../images/`; no on-slide credit needed |
| **Sourced** | Web-sourced file exists at expected path | Reference from `../images/`; check `image_sources.json` for `license_tier` — if `attribution-required`, render an inline credit element on the slide (see [executor-base.md §6](./executor-base.md) and [image-searcher.md §7](./image-searcher.md) for the visual spec) |
| **Needs-Manual** | Acquisition attempted once + one retry, failed | Dashed placeholder unless user has manually supplied the file |
| **Existing** | User already has image (`Acquire Via: user`) | Place in `images/`, reference with `<image>` |
| **Placeholder** | Intentionally not prepared yet (`Acquire Via: placeholder`) | Dashed border placeholder; replace later |

---

## Workflow

### 中文：工作流

- 本节说明 `工作流` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：工作流

```
1. Strategist defines image needs → Add image resource list with Acquire Via + Status per row
2. Image Acquisition (Step 5):
   - Pending + ai  → Image_Generator runs image_gen.py     → Generated
   - Pending + web → Image_Searcher runs image_search.py   → Sourced
   - user / placeholder rows are skipped
3. Executor generates SVGs (svg_output/)
   ├── Existing / Generated → <image href="../images/xxx.png" .../>
   ├── Sourced + license_tier=no-attribution → <image href=...> only
   ├── Sourced + license_tier=attribution-required → <image href=...> + small <text> credit element on the slide
   └── Placeholder / Needs-Manual without file → Dashed border + description text
4. Preview: python3 -m http.server -d <project_path> 8000 → /svg_output/<filename>.svg
5. Post-processing & Export → follow shared-standards.md §5
```

> Keep external references in `svg_output/` during generation. `finalize_svg.py` auto-embeds images into `svg_final/`; export PPTX from `svg_final/`.

---

## External Reference vs Base64 Embedding

### 中文：外部 参考 vs Base64 Embedding

- 本节说明 `外部 参考 vs Base64 Embedding` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：External 参考 vs Base64 Embedding

| Method | Pros | Cons | Suitable For |
|--------|------|------|-------------|
| **External reference** | Small file size, fast iteration, easy to replace | Preview requires HTTP server from project root | `svg_output/` development phase |
| **Base64 embedding** | Self-contained file, stable export | Large file size | `svg_final/` delivery phase |

---

## Method 1: External Reference (Recommended for Generation Phase)

### 中文：Method 外部 参考 Recommended for 生成 Phase

- 本节说明 `Method 外部 参考 Recommended for 生成 Phase` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Method External 参考 Recommended for Generation Phase

### Syntax

### 中文：Syntax

- 本节说明 `Syntax` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Syntax

```xml
<image href="../images/image.png" x="0" y="0" width="1280" height="720"
       preserveAspectRatio="xMidYMid slice"/>
```

### Key Attributes

### 中文：Key Attributes

- 本节说明 `Key Attributes` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Key Attributes

| Attribute | Description | Example |
|-----------|-------------|---------|
| `href` | Image path (relative or absolute) | `"../images/cover.png"` |
| `x`, `y` | Image top-left corner position | `x="0" y="0"` |
| `width`, `height` | Image display dimensions | `width="1280" height="720"` |
| `preserveAspectRatio` | Scaling mode | `"xMidYMid slice"` |

### preserveAspectRatio Common Values

### 中文：preserveAspectRatio Common Values

- 本节说明 `preserveAspectRatio Common Values` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：preserveAspectRatio Common Values

| Value | Effect |
|-------|--------|
| `xMidYMid slice` | Center crop (similar to CSS `cover`) |
| `xMidYMid meet` | Complete display (similar to CSS `contain`) |
| `none` | Stretch to fill, no aspect ratio preservation |

### Preview Method

### 中文：Preview Method

- 本节说明 `Preview Method` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Preview Method

Browser security blocks external images on directly opened SVGs. Serve via HTTP from the project root:

```bash
python3 -m http.server -d <project_path> 8000
# Visit http://localhost:8000/svg_output/your_file.svg
```

---

## Method 2: Base64 Embedding (Recommended for Delivery Phase)

### 中文：Method Base64 Embedding Recommended for Delivery Phase

- 本节说明 `Method Base64 Embedding Recommended for Delivery Phase` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Method 2: Base64 Embedding (Recommended for Delivery Phase)

### Syntax

### 中文：Syntax

- 本节说明 `Syntax` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Syntax

```xml
<image href="data:image/png;base64,iVBORw0KGgo..." x="0" y="0" width="1280" height="720"/>
```

### MIME Types

### 中文：MIME 类型

- 本节说明 `MIME 类型` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：MIME 类型

| MIME Type | File Format |
|-----------|-------------|
| `image/png` | PNG |
| `image/jpeg` | JPG/JPEG |
| `image/gif` | GIF |
| `image/webp` | WebP |
| `image/svg+xml` | SVG |

---

## Conversion Process

### 中文：Conversion 流程

- 本节说明 `Conversion 流程` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Conversion Process

Use the unified pipeline in [shared-standards.md §5](shared-standards.md). `finalize_svg.py` runs before export so image references in `svg_output/` become embedded assets in `svg_final/`.

```bash
python3 scripts/finalize_svg.py <project_path>
python3 scripts/svg_to_pptx.py <project_path>
```

### Standalone: embed_images.py (advanced)

### 中文：Standalone embed_images py advanced

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- For processing specific SVGs without the full pipeline（以上为中文意译，具体细节以英文原文为准）。
```bash
python3 scripts/svg_finalize/embed_images.py <svg_file>                         # Single file
python3 scripts/svg_finalize/embed_images.py <project_path>/svg_output/*.svg    # Batch
python3 scripts/svg_finalize/embed_images.py --dry-run <project_path>/svg_output/*.svg  # Preview
```

---

## Best Practices

### 中文：最佳实践

- 本节说明 `最佳实践` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：最佳实践

### Image Optimization

### 中文：图像 Optimization

- 本节说明 `图像 Optimization` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Image Optimization

Compress before embedding to reduce file size:

```bash
convert input.png -quality 85 -resize 1920x1080\> output.png  # ImageMagick
pngquant --quality=65-80 input.png -o output.png               # pngquant (recommended)
```

### File Organization

### 中文：File Organization

- 本节说明 `File Organization` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：File Organization

```
project/
├── images/            # Image assets
├── sources/           # Source files and their accompanying images
│   └── article_files/
├── svg_output/        # Raw version (external references)
└── svg_final/         # Final version (images embedded)
```

### Rounded Corner / Non-rectangular Image Cropping

### 中文：Rounded Corner Non-rectangular 图像 Cropping

- 本节说明 `Rounded Corner Non-rectangular 图像 Cropping` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Rounded Corner / Non-rectangular Image Cropping

`clipPath` **on `<image>` elements** is conditionally allowed — authoritative constraints in [shared-standards.md §1.2](shared-standards.md); do not restate or relax here.

Fallback when `clipPath` doesn't fit: bake rounded corners into the source image (PNG with alpha) before embedding.

---

## FAQ

### 中文：常见问题

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Q: Can't see images when opening SVG directly?**（以上为中文意译，具体细节以英文原文为准）。
- Browser security blocks cross-directory requests（以上为中文意译，具体细节以英文原文为准）。
- Serve via HTTP from project root, or run `finalize_svg（以上为中文意译，具体细节以英文原文为准）。
- py` first and view from `svg_final/`（以上为中文意译，具体细节以英文原文为准）。
Compress the source, use JPEG, reduce resolution to match actual display dimensions.

**Q: How to reverse-extract a Base64 image?**
```bash
base64 -d image.b64 > image.png
```
