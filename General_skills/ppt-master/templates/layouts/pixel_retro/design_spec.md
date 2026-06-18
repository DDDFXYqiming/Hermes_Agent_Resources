# Pixel Retro Style Template - Design Specification

## 中文主体补充：AI_Projects / design_spec.md

本文件属于公开技能 `AI_Projects`。本节为中文主体补充说明，目标是让中文读者在不依赖英文背景的情况下，理解本文件的作用、阅读路径、关键约束和验收标准。
本文件的相对路径是 `ppt-master/templates/layouts/pixel_retro/design_spec.md`，属于 `AI_Projects` 的参考/工作流/模板/脚本/资产之一。
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

## 中文主体说明：Hermes_Agent_Resources 模板说明：design spec

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


> Suitable for tech talks, programming tutorials, game-related presentations, geek-style content showcases, and similar scenarios.

---

## I. Template Overview

### 中文：模板 概览

- 本节说明 `模板 概览` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：模板 概览

| Property       | Description                                                |
| -------------- | ---------------------------------------------------------- |
| **Template Name** | pixel_retro (Pixel Retro Template)                      |
| **Use Cases**  | Tech talks, programming tutorials, game introductions, geek-style showcases |
| **Design Tone** | Retro gaming, neon cyberpunk, geek tech, 8-bit style      |
| **Theme Mode** | Dark theme (deep space black background + neon accents)    |

---

## II. Canvas Specification

### 中文：II Canvas 规范

- 本节说明 `II Canvas 规范` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：II Canvas 规范

| Property       | Value                         |
| -------------- | ----------------------------- |
| **Format**     | Standard 16:9                 |
| **Dimensions** | 1280 × 720 px                |
| **viewBox**    | `0 0 1280 720`                |
| **Page Margins** | Left/Right 60px, Top 50px, Bottom 40px |
| **Safe Area**  | x: 60-1220, y: 50-680         |

---

## III. Color Scheme

### 中文：III 颜色 Scheme

- 本节说明 `III 颜色 Scheme` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：III 颜色 Scheme

### Background Colors

### 中文：背景色

- 本节说明 `背景色` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：背景色

| Role           | Value       | Notes                            |
| -------------- | ----------- | -------------------------------- |
| **Deep Space Black** | `#0D1117` | Main background color          |
| **Starry Night Blue** | `#161B22` | Card/block background         |
| **Dark Border** | `#30363D`  | Borders/dividers                 |

### Accent Colors (Neon Series)

### 中文：Accent 颜色 霓虹 Series

- 本节说明 `Accent 颜色 霓虹 Series` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Accent 颜色 Neon Series

| Role           | Value       | Usage                            |
| -------------- | ----------- | -------------------------------- |
| **Neon Green** | `#39FF14`   | Primary accent, success, save points, Git |
| **Cyber Pink** | `#FF2E97`   | Secondary accent, warnings, contrast, GitHub |
| **Electric Blue** | `#00D4FF` | Tertiary accent, links, info, flows |
| **Gold Yellow** | `#FFD700`  | Quaternary accent, history, timelines, highlights |

### Auxiliary Colors

### 中文：Auxiliary 颜色

- 本节说明 `Auxiliary 颜色` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Auxiliary 颜色

| Role           | Value       | Usage                            |
| -------------- | ----------- | -------------------------------- |
| **Dark Green** | `#238636`   | Muted version of success state   |
| **Dark Pink**  | `#8B2252`   | Muted pink                       |
| **Dark Blue**  | `#1F6FEB`   | Muted blue                       |

### Text Colors

### 中文：Text 颜色

- 本节说明 `Text 颜色` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Text 颜色

| Role           | Value       | Usage                  |
| -------------- | ----------- | ---------------------- |
| **Moonlight White** | `#E6EDF3` | Primary text         |
| **Mist Gray**  | `#8B949E`   | Secondary descriptive text |
| **Pure White** | `#FFFFFF`   | Emphasized titles      |

---

## IV. Typography System

### 中文：IV Typography System

- 本节说明 `IV Typography System` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：IV 排版 System

### Font Stack

### 中文：Font Stack

- 本节说明 `Font Stack` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：字体 Stack

**Title Font**: `"Consolas", "Monaco", "Courier New", monospace` - Pixel/code aesthetic

**Body Font**: `-apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft YaHei", sans-serif`

**Code Font**: `"Cascadia Code", "Fira Code", "Consolas", monospace`

### Font Size Hierarchy

### 中文：Font Size Hierarchy

- 本节说明 `Font Size Hierarchy` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：字体 Size Hierarchy

| Level | Usage              | Size | Weight  |
| ----- | ------------------ | ---- | ------- |
| H1    | Cover main title   | 52px | Bold    |
| H2    | Page heading       | 36px | Bold    |
| H3    | Section title/Subtitle | 22px | 600  |
| P     | Body content       | 18px | Regular |
| High  | Highlighted data   | 48px | Bold    |
| Sub   | Supplementary text | 14px | Regular |
| Code  | Code text          | 16px | Regular |

---

## V. Page Structure

### 中文：Page 结构

- 本节说明 `Page 结构` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：页面 结构

### General Layout

### 中文：General 版式

- 本节说明 `General 版式` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：General 版式

| Area       | Position/Height | Description                            |
| ---------- | --------------- | -------------------------------------- |
| **Top**    | y=0, h=4-6px    | Neon green decoration line (dual-line effect) |
| **Title Area** | y=50, h=70px | Page title + English subtitle         |
| **Content Area** | y=130, h=510px | Main content area                  |
| **Footer** | y=680, h=40px   | Page number, decoration line, progress indicator |

### Decorative Elements

### 中文：Decorative Elements

- 本节说明 `Decorative Elements` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Decorative Elements

- **Top Decoration Line**: Neon green dual lines (main line 4px + auxiliary line 2px)
- **Bottom Decoration Line**: Neon green dual lines (auxiliary line 4px + main line 4px)
- **Pixel Blocks**: Corner decorations with decreasing opacity (100% → 60% → 30%)
- **Scanline Grid**: Optional low-opacity background grid lines

---

## VI. Page Types

### 中文：VI Page 类型

- 本节说明 `VI Page 类型` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：VI 页面 类型

### 1. Cover Page (01_cover.svg)

### 中文：Cover Page cover svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Deep space black background（以上为中文意译，具体细节以英文原文为准）。
- Top/bottom neon decoration lines（以上为中文意译，具体细节以英文原文为准）。
- Pixel-style console graphic (optional)（以上为中文意译，具体细节以英文原文为准）。
- Main title (neon green glow effect)（以上为中文意译，具体细节以英文原文为准）。
- Main title (neon green glow effect)
- Subtitle (moonlight white)
- Function button group (horizontal layout)
- Bottom prompt text (e.g., "PRESS START")

### 2. Table of Contents (02_toc.svg)

### 中文：表格 of Contents toc svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Deep space black background（以上为中文意译，具体细节以英文原文为准）。
- Standard top decoration（以上为中文意译，具体细节以英文原文为准）。
- Chapter list (with importance labels)（以上为中文意译，具体细节以英文原文为准）。
- Red: Essential / Must-learn（以上为中文意译，具体细节以英文原文为准）。
  - Red: Essential / Must-learn
  - Yellow: Recommended
  - Green: Optional
- Pixel-style list design

### 3. Chapter Page (02_chapter.svg)

### 中文：Chapter Page chapter svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Deep space black background（以上为中文意译，具体细节以英文原文为准）。
- Full-screen neon effect（以上为中文意译，具体细节以英文原文为准）。
- Large chapter number (glow effect)（以上为中文意译，具体细节以英文原文为准）。
- Chapter title + English subtitle（以上为中文意译，具体细节以英文原文为准）。
- Chapter title + English subtitle
- Pixel-style decorative frame

### 4. Content Page (03_content.svg)

### 中文：内容 Page 内容 svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Deep space black background（以上为中文意译，具体细节以英文原文为准）。
- Standard top decoration（以上为中文意译，具体细节以英文原文为准）。
- Page title (neon green + glow)（以上为中文意译，具体细节以英文原文为准）。
- English subtitle (mist gray)（以上为中文意译，具体细节以英文原文为准）。
- English subtitle (mist gray)
- **Fully open content area** (y=140 to y=670, width 1160px)
- Bottom page number

> **Design Principle**: The content page template only provides the page frame (title area + footer). The content area is freely designed by the Executor based on actual content. Available layouts include but are not limited to: cards, progress bars, tables, timelines, comparison charts, etc.

### 5. Ending Page (04_ending.svg)

### 中文：Ending Page ending svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Deep space black background（以上为中文意译，具体细节以英文原文为准）。
- Neon glow main title（以上为中文意译，具体细节以英文原文为准）。
- Summary card group（以上为中文意译，具体细节以英文原文为准）。
- "GAME SAVED" visual effect（以上为中文意译，具体细节以英文原文为准）。
- "GAME SAVED" visual effect
- Progress button group

---

## VII. Layout Modes

### 中文：VII 版式 模式

- 本节说明 `VII 版式 模式` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：VII 版式 Modes

| Mode               | Use Cases                      |
| ------------------ | ------------------------------ |
| **Single Column Centered** | Cover, closing, key points |
| **Two Columns (5:5)** | Comparative display (e.g., Git vs GitHub) |
| **Dual-Column Cards** | Feature lists, trait comparisons |
| **Three-Column Cards** | Key takeaways, project lists |
| **Progress Bar Display** | Data statistics, usage rates |
| **Timeline**       | History, processes, workflows  |

---

## VIII. Spacing Guidelines

### 中文：VIII Spacing 指南

- 本节说明 `VIII Spacing 指南` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：VIII 间距 指南

| Element          | Value  |
| ---------------- | ------ |
| Card spacing     | 20-30px |
| Content block spacing | 30px |
| Card padding     | 20-24px |
| Card border radius | 0px (blocky feel) or 4px |
| Border width     | 2-3px  |
| Icon-to-text gap | 12px   |

---

## IX. Visual Effects

### 中文：IX 视觉 Effects

- 本节说明 `IX 视觉 Effects` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：IX. Visual Effects

### Pixel Style Characteristics

### 中文：像素 风格 Characteristics

- 本节说明 `像素 风格 Characteristics` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Pixel 风格 Characteristics

- Blocky icons and decorations
- Use block characters such as: full block, dark shade, light shade, upper half, lower half, small black/white squares for decoration
- Progress bars filled with blocks
- Borders use double lines or dotted patterns
- Card corners with pixel decoration blocks

### Neon Glow Effect

### 中文：霓虹 Glow Effect

- 本节说明 `霓虹 Glow Effect` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Neon Glow Effect

Apply glow filters to key text/elements:

```xml
<defs>
  <filter id="glowGreen" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="3-4" result="blur" />
    <feMerge>
      <feMergeNode in="blur" />
      <feMergeNode in="SourceGraphic" />
    </feMerge>
  </filter>
</defs>

<!-- Usage -->
<text filter="url(#glowGreen)" fill="#39FF14">Glowing Text</text>
```

> **Note**: `filter` effects are typically ignored in PPT, but render well in SVG-compatible viewers.

### Emoji Usage

### 中文：Emoji 使用方法

- 本节说明 `Emoji 使用方法` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Emoji 表情 使用方法

- 🎮 Game/Save
- 💾 Save
- 🔀 Branch/Merge
- 📁 Folder
- 📝 Document
- 🚀 Release
- ⏪ Revert
- 👾 Developer
- 🌐 Network/Cloud
- ✅ Confirm/Success
- 🎯 Target/Key Point
- 🤔 Question/Thinking

---

## X. SVG Technical Constraints

### 中文：SVG Technical 限制

- 本节说明 `SVG Technical 限制` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：SVG Technical 限制

### Mandatory Rules

### 中文：Mandatory 规则

- 本节说明 `Mandatory 规则` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Mandatory 规则

1. viewBox: `0 0 1280 720`
2. Use `<rect>` elements for backgrounds
3. Use `<tspan>` for text wrapping (no `<foreignObject>`)
4. Use `fill-opacity` / `stroke-opacity` for transparency; `rgba()` is prohibited
5. Prohibited: `mask`, `<style>`, `class`, `foreignObject`. `clipPath` is allowed only on `<image>` under `shared-standards.md` §1.2
6. Prohibited: `textPath`, `animate*`, `script`
7. `marker-start` / `marker-end` conditionally allowed (marker in `<defs>`, `orient="auto"`, shape = triangle/diamond/oval) — see shared-standards.md §1.1

### PPT Compatibility Rules

### 中文：PPT Compatibility 规则

- 本节说明 `PPT Compatibility 规则` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：PPT Compatibility 规则

- No `<g opacity="...">` (group opacity); set opacity on each child element individually
- Use overlay layers instead of image opacity
- Use inline styles only; external CSS and `@font-face` are prohibited
- `filter` effects serve as enhancements (allowed) and do not affect baseline display

---

## XI. Placeholder Specification

### 中文：XI Placeholder 规范

- 本节说明 `XI Placeholder 规范` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：XI Placeholder 规范

Templates use `{{PLACEHOLDER}}` format placeholders. Common placeholders:

| Placeholder        | Description        |
| ------------------ | ------------------ |
| `{{TITLE}}`        | Main title         |
| `{{SUBTITLE}}`     | Subtitle           |
| `{{AUTHOR}}`       | Author/Organization |
| `{{PAGE_TITLE}}`   | Page title         |
| `{{PAGE_TITLE_EN}}`| Page title (English) |
| `{{CONTENT_AREA}}` | Flexible content area |
| `{{CHAPTER_NUM}}`  | Chapter number     |
| `{{PAGE_NUM}}`     | Page number        |
| `{{TOTAL_PAGES}}`  | Total page count   |
| `{{VERSION}}`      | Version number     |
| `{{TOC_ITEM_N_TITLE}}` | TOC item title |
| `{{THANK_YOU}}`    | Thank-you message  |
| `{{CONTACT_INFO}}` | Primary contact info |

---

## XII. Usage Instructions

### 中文：XII 使用方法 Instructions

- 本节说明 `XII 使用方法 Instructions` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：XII 使用方法 Instructions

1. Copy the template to the project `templates/` directory
2. Select the appropriate page template based on content requirements
3. Mark content to be replaced using placeholders
4. Generate the final SVG through the Executor role
5. Define glow effects using `filter` (within `<defs>`)
6. Maintain consistency of the neon color scheme

---

## XIII. Color Quick Reference

### 中文：XIII 颜色 Quick 参考

- 本节说明 `XIII 颜色 Quick 参考` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：XIII 颜色 Quick 参考

```
Background Layer:
  Main background    #0D1117  Deep Space Black
  Card background    #161B22  Starry Night Blue
  Borders            #30363D  Dark Border

Accent Colors (use in order):
  Primary accent     #39FF14  Neon Green
  Secondary accent   #FF2E97  Cyber Pink
  Tertiary accent    #00D4FF  Electric Blue
  Quaternary accent  #FFD700  Gold Yellow

Text:
  Primary text       #E6EDF3  Moonlight White
  Secondary text     #8B949E  Mist Gray
  Emphasis text      #FFFFFF  Pure White
```
