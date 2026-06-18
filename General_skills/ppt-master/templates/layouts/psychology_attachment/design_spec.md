# Psychology Healing Template (Psychology Attachment Style) - Design Specification

## 中文主体补充：AI_Projects / design_spec.md

本文件属于公开技能 `AI_Projects`。本节为中文主体补充说明，目标是让中文读者在不依赖英文背景的情况下，理解本文件的作用、阅读路径、关键约束和验收标准。
本文件的相对路径是 `ppt-master/templates/layouts/psychology_attachment/design_spec.md`，属于 `AI_Projects` 的参考/工作流/模板/脚本/资产之一。
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


> Suitable for psychology, psychotherapy, counseling training, and academic sharing in professional settings.

---

## I. Template Overview

### 中文：模板 概览

- 本节说明 `模板 概览` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：模板 概览

| Property         | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| **Template Name**| psychology_attachment (Psychology Healing Template)           |
| **Use Cases**    | Psychotherapy training, academic lectures, counseling case analysis, professional sharing |
| **Design Tone**  | Professional, warm, healing, trustworthy                     |
| **Theme Mode**   | Light theme (cloud white background + blue-green gradient accent + multi-color semantic colors) |

### Core Visual Metaphor

### 中文：Core 视觉 Metaphor

- 本节说明 `Core 视觉 Metaphor` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：核心 Visual Metaphor

The design adopts "**Secure Base**" as the core visual metaphor:

- **Structural Stability**: Page layout resembles a secure attachment relationship with clear boundaries and predictable patterns
- **Clear Hierarchy**: Information levels mirror the organization of the attachment system — from biological instinct to higher-order reflection
- **Warm Professionalism**: Colors convey both professional authority and healing warmth

---

## II. Canvas Specification

### 中文：II Canvas 规范

- 本节说明 `II Canvas 规范` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：II Canvas 规范

| Property           | Value                           |
| ------------------ | ------------------------------- |
| **Format**         | Standard 16:9                   |
| **Dimensions**     | 1280 × 720 px                  |
| **viewBox**        | `0 0 1280 720`                 |
| **Page Margins**   | Left/right 40px, top 60px, bottom 40px |
| **Content Safe Area** | x: 40-1240, y: 60-680       |

### Page Zones

### 中文：Page Zones

- 本节说明 `Page Zones` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：页面 Zones

| Zone             | Y-Range   | Height | Usage                      |
| ---------------- | --------- | ------ | -------------------------- |
| Top Title Area   | 60-120    | 60px   | Page title, chapter labels |
| Main Content     | 130-640   | 510px  | Core content display       |
| Bottom Info Area | 650-680   | 30px   | Page number, chapter nav   |

---

## III. Color Scheme

### 中文：III 颜色 Scheme

- 本节说明 `III 颜色 Scheme` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：III 颜色 Scheme

### Primary Colors

### 中文：Primary 颜色

- 本节说明 `Primary 颜色` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Primary 颜色

| Semantic Role     | Color Name    | HEX       | RGB         | Usage                              |
| ----------------- | ------------- | --------- | ----------- | ---------------------------------- |
| **Dominant**      | Secure Blue   | `#2E5C8E` | 46,92,142   | Titles, key frameworks, secure attachment |
| **Background**    | Cloud White   | `#F8FAFC` | 248,250,252 | Page background                    |
| **Accent A**      | Warm Orange   | `#E07843` | 224,120,67  | Activation, emotion, anxious type  |
| **Accent B**      | Healing Green | `#3D8B7A` | 61,139,122  | Growth, integration, secure type   |
| **Accent C**      | Cool Gray-Blue| `#64748B` | 100,116,139 | Avoidant type, dismissive type     |
| **Warning**       | Trauma Red    | `#B54545` | 181,69,69   | Disorganized type, unresolved trauma |

### Attachment Type Color Assignments

### 中文：Attachment 类型 颜色 Assignments

- 本节说明 `Attachment 类型 颜色 Assignments` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Attachment 类型 颜色 Assignments

| Attachment Type              | Primary   | Secondary | Symbolism              |
| ---------------------------- | --------- | --------- | ---------------------- |
| Secure / Autonomous          | `#3D8B7A` | `#D4EDDA` | Growth, coherence      |
| Avoidant / Dismissive        | `#64748B` | `#E2E8F0` | Detachment, suppression |
| Anxious-Ambivalent / Preoccupied | `#E07843` | `#FED7AA` | Anxiety, amplification |
| Disorganized / Unresolved    | `#B54545` | `#FECACA` | Trauma, fragmentation  |

### Text Colors

### 中文：Text 颜色

- 本节说明 `Text 颜色` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Text 颜色

| Role              | Value     | Usage                              |
| ----------------- | --------- | ---------------------------------- |
| **Main Title**    | `#1E293B` | Dark ink blue, cover/page titles   |
| **Subtitle**      | `#2E5C8E` | Secure blue, emphasized subtitles  |
| **Body Text**     | `#374151` | Dark gray, body content            |
| **Helper Text**   | `#6B7280` | Medium gray, annotations           |
| **Secondary Text**| `#64748B` | Gray-blue, page numbers etc.       |
| **White Text**    | `#FFFFFF` | Text on dark backgrounds           |
| **Light Text**    | `#E5E7EB` | Secondary text on dark backgrounds |
| **English Gray**  | `#94A3B8` | English subtitles                  |

### Gradients

### 中文：Gradients

- 本节说明 `Gradients` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：渐变

| Name             | Start     | Middle    | End       | Usage                  |
| ---------------- | --------- | --------- | --------- | ---------------------- |
| Cover Gradient   | `#1E3A5F` | `#2E5C8E` | `#3D8B7A` | Cover/chapter page BG  |
| Ending Gradient  | `#1E3A5F` | `#2E5C8E` | `#3D8B7A` | Ending page background |

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

**Chinese Font Stack**: `"Microsoft YaHei", "PingFang SC", sans-serif`

**English Font Stack**: `Arial, sans-serif`

### Font Size Hierarchy

### 中文：Font Size Hierarchy

- 本节说明 `Font Size Hierarchy` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：字体 Size Hierarchy

| Level | Usage            | Size | Weight   | Line Height |
| ----- | ---------------- | ---- | -------- | ----------- |
| H1    | Cover main title | 52px | Bold     | 1.2         |
| H2    | Page main title  | 32px | Bold     | 1.3         |
| H3    | Section subtitle | 24px | SemiBold | 1.3         |
| H4    | Card title       | 20px | SemiBold | 1.4         |
| Body  | Body content     | 18px | Regular  | 1.5         |
| Small | Annotations      | 14px | Regular  | 1.4         |

### Spacing System

### 中文：Spacing System

- 本节说明 `Spacing System` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：间距 System

| Usage              | Value                     |
| ------------------ | ------------------------- |
| Base unit          | 8px                       |
| Element spacing    | 16px / 24px / 32px / 48px |
| Paragraph spacing  | 24px                      |
| List item spacing  | 12px                      |
| Card inner padding | 24px                      |

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

| Area              | Position/Height | Description                          |
| ----------------- | --------------- | ------------------------------------ |
| **Left Accent**   | x=0, w=8px      | Dominant color vertical bar (content pages) |
| **Top**           | y=60-120        | Page title + English subtitle        |
| **Divider**       | y=125-130       | Decorative divider line              |
| **Content Area**  | y=130-640       | Main content area (510px height)     |
| **Footer**        | y=650-700       | Page number, chapter info            |

### Decorative Design

### 中文：Decorative 设计

- 本节说明 `Decorative 设计` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Decorative 设计

- **Left Accent Bar**: Dominant color (`#2E5C8E`), width 8px, spanning the full page height
- **Divider Line**: Light gray (`#E5E7EB`), width 1-2px
- **Circle Decorations**: Low-opacity circles for chapter page/cover backgrounds

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
- Background**: Blue-green gradient (`#1E3A5F` → `#2E5C8E` → `#3D8B7A`)（以上为中文意译，具体细节以英文原文为准）。
- Decoration**: Optional background image (opacity=0（以上为中文意译，具体细节以英文原文为准）。
- 25)（以上为中文意译，具体细节以英文原文为准）。
- Title Area**: Centered, main title 52px + subtitle 28px（以上为中文意译，具体细节以英文原文为准）。
- **English Title**: Light gray, 24px
- **Decorative Line**: Warm orange thin line, 200px wide
- **Bottom**: Quote card (semi-transparent background + healing green left border)
- **Tags**: Keyword tags (semi-transparent capsules)
- **Page Number**: Bottom-right, 14px

### 2. Table of Contents (02_toc.svg)

### 中文：表格 of Contents toc svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Background**: Cloud white (`#F8FAFC`)（以上为中文意译，具体细节以英文原文为准）。
- Left Accent**: Dominant color 8px vertical bar（以上为中文意译，具体细节以英文原文为准）。
- Title**: "Contents Overview"（以上为中文意译，具体细节以英文原文为准）。
- Left Side**: Five-chapter list (colored number blocks + title + description)（以上为中文意译，具体细节以英文原文为准）。
- **Left Side**: Five-chapter list (colored number blocks + title + description)
  - Chapter 1: Dominant blue `#2E5C8E`
  - Chapter 2: Healing green `#3D8B7A`
  - Chapter 3: Warm orange `#E07843`
  - Chapter 4: Cool gray-blue `#64748B`
  - Chapter 5: Trauma red `#B54545`
- **Right Side**: Learning objectives card
- **Center**: Dashed divider

### 3. Chapter Page (02_chapter.svg)

### 中文：Chapter Page chapter svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Background**: Blue-green gradient（以上为中文意译，具体细节以英文原文为准）。
- Decoration**: Multiple low-opacity concentric circles, diagonal line accents（以上为中文意译，具体细节以英文原文为准）。
- Large Number**: 120px, semi-transparent white, centered（以上为中文意译，具体细节以英文原文为准）。
- Chapter Label**: Capsule shape "CHAPTER X"（以上为中文意译，具体细节以英文原文为准）。
- **Chapter Label**: Capsule shape "CHAPTER X"
- **Title**: 48px white bold
- **Subtitle**: 24px light gray English
- **Decorative Line**: Warm orange thin line, 200px
- **Quote**: Semi-transparent quote card
- **Keywords**: Bottom tag group
- **Page Number**: Bottom-right

### 4. Content Page (03_content.svg)

### 中文：内容 Page 内容 svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Background**: Cloud white（以上为中文意译，具体细节以英文原文为准）。
- Left Accent**: Dominant blue 8px vertical bar（以上为中文意译，具体细节以英文原文为准）。
- Title Area**: Main title 28px + English subtitle 16px（以上为中文意译，具体细节以英文原文为准）。
- Divider**: Decorative line below title（以上为中文意译，具体细节以英文原文为准）。
- **Divider**: Decorative line below title
- **Content Area**: Flexible layout (three-column / left-right split / single column)
- **Card Styles**:
  - White background + light gray border
  - Border radius 12-16px
  - Colored top bar / colored left border
- **Bottom Tip**: Light gray background tip bar (optional)
- **Page Number**: Bottom-right

### 5. Ending Page (04_ending.svg)

### 中文：Ending Page ending svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Background**: Blue-green gradient（以上为中文意译，具体细节以英文原文为准）。
- Decoration**: Network connection graph (dots + lines)（以上为中文意译，具体细节以英文原文为准）。
- Title**: Main title 56px + subtitle 28px（以上为中文意译，具体细节以英文原文为准）。
- English**: Light gray English title（以上为中文意译，具体细节以英文原文为准）。
- **English**: Light gray English title
- **Decorative Line**: Warm orange thin line, 300px
- **Info Area**: Semi-transparent info card
- **Bottom**: Copyright information

---

## VII. Layout Patterns

### 中文：VII 版式 Patterns

- 本节说明 `VII 版式 Patterns` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：VII 版式 Patterns

### 7.1 Three-Column Side-by-Side (Comparison/Findings)

### 中文：Three-Column Side-by-Side 对比 Findings

- 本节说明 `Three-Column Side-by-Side 对比 Findings` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：7.1 Three-Column Side-by-Side (Comparison/Findings)

```
[Card 1: 360px] [Gap: 40px] [Card 2: 360px] [Gap: 40px] [Card 3: 360px]
```

- Each card: Colored top bar + icon + number + title + content + bottom tag
- Suitable for: Three findings, three-type comparisons

### 7.2 Left-Right Split

### 中文：Left-Right Split

- 本节说明 `Left-Right Split` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：7.2 Left-Right Split

```
[Left Column: 560px] [Gap: 60px] [Right Column: 580px]
```

- Left side: Concepts/theory
- Right side: Application/practice
- Suitable for: Concept explanations, therapeutic relationships

### 7.3 Vertical Stack (Hierarchical Structure)

### 中文：Vertical Stack Hierarchical 结构

- 本节说明 `Vertical Stack Hierarchical 结构` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Vertical Stack Hierarchical 结构

```
┌─────────────────────────────────┐
│       Top Layer: Metacognition   │
├─────────────────────────────────┤
│       Representation Layer       │
├─────────────────────────────────┤
│       Affective Layer            │
├─────────────────────────────────┤
│       Somatic Layer              │
└─────────────────────────────────┘
```

- Suitable for: Self-development hierarchy, theoretical frameworks

### 7.4 Attachment Type Quadrant

### 中文：Attachment 类型 Quadrant

- 本节说明 `Attachment 类型 Quadrant` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Attachment 类型 Quadrant

| Secure (Green) | Avoidant (Gray-Blue) |
| Anxious-Ambivalent (Orange) | Disorganized (Red) |

- Each card uses the corresponding attachment type color scheme

---

## VIII. Visual Element Specifications

### 中文：VIII 视觉 Element 规范

- 本节说明 `VIII 视觉 Element 规范` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：VIII Visual Element 规范

### 8.1 Card Styles

### 中文：Card 风格

- 本节说明 `Card 风格` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Card 风格

```xml
<!-- Standard info card -->
<rect rx="12" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1"/>

<!-- Emphasis card (with left border) -->
<rect rx="12" fill="#FFFFFF"/>
<rect x="0" width="4" fill="#2E5C8E" rx="2"/>

<!-- Colored top card -->
<rect rx="16" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1"/>
<rect rx="16" width="100%" height="80" fill="#2E5C8E"/>  <!-- Top color block -->
```

### 8.2 Number Blocks

### 中文：Number Blocks

- 本节说明 `Number Blocks` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：8.2 Number Blocks

```xml
<path fill="#2E5C8E" d="M8,0 H42 A8,8 0 0 1 50,8 V42 A8,8 0 0 1 42,50 H8 A8,8 0 0 1 0,42 V8 A8,8 0 0 1 8,0 Z"/>
<text x="25" y="33" font-size="20" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1</text>
```

### 8.3 Tag Styles

### 中文：Tag 风格

- 本节说明 `Tag 风格` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Tag 风格

```xml
<!-- Capsule tag -->
<path fill="#E0F2FE" d="M33,0 H107 A13,13 0 0 1 120,13 V13 A13,13 0 0 1 107,26 H33 A13,13 0 0 1 20,13 V13 A13,13 0 0 1 33,0 Z"/>
<text x="70" y="18" font-size="13" fill="#2E5C8E" text-anchor="middle">Tag Text</text>
```

### 8.4 Quote Cards

### 中文：Quote Cards

- 本节说明 `Quote Cards` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：8.4 Quote Cards

```xml
<!-- Semi-transparent quote card -->
<path fill="#FFFFFF" fill-opacity="0.1" d="..."/>
<path fill="#3D8B7A" d="..." rx="2"/>  <!-- Left accent bar -->
<text font-style="italic" fill="#E5E7EB">Quote content</text>
```

### 8.5 Divider Lines

### 中文：Divider Lines

- 本节说明 `Divider Lines` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：8.5 Divider Lines

```xml
<line x1="60" y1="Y" x2="1240" y2="Y" stroke="#E5E7EB" stroke-width="2"/>
```

---

## IX. Icon Usage

### 中文：IX 图标 使用方法

- 本节说明 `IX 图标 使用方法` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：IX 图标 使用方法

Use `tabler-outline` as the stylistic icon library for this template. It matches the professional, warm, low-noise psychology tone and avoids heavy filled symbols.

### Placeholder Format

### 中文：Placeholder Format

- 本节说明 `Placeholder Format` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Placeholder Format

```xml
<use data-icon="tabler-outline/icon-name" x="X" y="Y" width="32" height="32" fill="COLOR"/>
```

### Common Icon Mappings

### 中文：Common 图标 Mappings

- 本节说明 `Common 图标 Mappings` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Common 图标 Mappings

| Concept              | Icons                     |
| -------------------- | ------------------------- |
| Attachment/Bonding   | `tabler-outline/heart`, `tabler-outline/link` |
| Secure Base          | `tabler-outline/home`, `tabler-outline/shield-check` |
| Mentalization        | `tabler-outline/brain`, `tabler-outline/bulb` |
| Affect Regulation    | `tabler-outline/activity`, `tabler-outline/adjustments-horizontal` |
| Awareness            | `tabler-outline/eye`, `tabler-outline/compass` |
| Trauma               | `tabler-outline/alert-triangle`, `tabler-outline/bolt` |
| Repair               | `tabler-outline/refresh`, `tabler-outline/tool` |
| Development          | `tabler-outline/trending-up`, `tabler-outline/layers-linked` |

---

## X. SVG Technical Constraints

### 中文：SVG Technical 限制

- 本节说明 `SVG Technical 限制` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：SVG Technical 限制

### viewBox Specification

### 中文：viewBox 规范

- 本节说明 `viewBox 规范` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：viewBox 规范

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
```

### Prohibited Features (Blocklist)

### 中文：Prohibited 功能 Blocklist

- 本节说明 `Prohibited 功能 Blocklist` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Prohibited 功能 Blocklist

| Category           | Prohibited Items                        |
| ------------------ | --------------------------------------- |
| **Clipping/Masking** | `mask` is forbidden; `clipPath` is allowed only on `<image>` under `shared-standards.md` §1.2 |
| **Style System**   | `<style>`, `class` (`id` inside `<defs>` is allowed) |
| **Structure/Nesting** | `<foreignObject>`                   |
| **Text/Font**      | `textPath`, `@font-face`               |
| **Animation/Interaction** | `<animate*>`, `<set>`, `on*`    |

> `marker-start` / `marker-end` are conditionally allowed — see `shared-standards.md` §1.1 (marker must be in `<defs>`, `orient="auto"`, shape = triangle / diamond / oval).

### PPT Compatibility Rules

### 中文：PPT Compatibility 规则

- 本节说明 `PPT Compatibility 规则` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：PPT Compatibility 规则

| Prohibited                         | Correct Alternative                                    |
| ---------------------------------- | ------------------------------------------------------ |
| `fill="rgba(255,255,255,0.1)"`     | `fill="#FFFFFF" fill-opacity="0.1"`                    |
| `stroke="rgba(0,0,0,0.5)"`        | `stroke="#000000" stroke-opacity="0.5"`                |
| `<g opacity="0.2">...</g>`        | Set `opacity` / `fill-opacity` on each child element individually |

---

## XI. Placeholder Specification

### 中文：XI Placeholder 规范

- 本节说明 `XI Placeholder 规范` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：XI Placeholder 规范

| Placeholder          | Usage                |
| -------------------- | -------------------- |
| `{{TITLE}}`          | Main title           |
| `{{SUBTITLE}}`       | Subtitle             |
| `{{TITLE_EN}}`       | English title        |
| `{{PAGE_TITLE}}`     | Content page title   |
| `{{CONTENT_AREA}}`   | Flexible content area |
| `{{CHAPTER_NUM}}`    | Chapter number       |
| `{{CHAPTER_TITLE}}`  | Chapter title        |
| `{{CHAPTER_EN}}`     | Chapter English title |
| `{{QUOTE}}`          | Quote content        |
| `{{QUOTE_AUTHOR}}`   | Quote author         |
| `{{PAGE_NUM}}`       | Page number          |
| `{{COVER_BG_IMAGE}}` | Cover background image path |
| `{{TOC_ITEM_N_TITLE}}` | TOC item title     |
| `{{TOC_ITEM_N_DESC}}`  | TOC item description |
| `{{THANK_YOU}}`      | Thank-you message    |
| `{{CONTACT_INFO}}`   | Primary contact info |

---

## XII. Usage Notes

### 中文：XII 使用方法 说明

- 本节说明 `XII 使用方法 说明` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：XII 使用方法 说明

### Template Usage Steps

### 中文：模板 使用方法 步骤

- 本节说明 `模板 使用方法 步骤` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：模板 使用方法 步骤

1. **Copy Template**: Copy template files to the project `templates/` directory
2. **Replace Placeholders**: Replace `{{}}` placeholders with actual content
3. **Adjust Colors**: Fine-tune the color scheme based on the theme
4. **Generate Content**: Use the Executor role to generate specific pages
5. **Post-process**: Run `finalize_svg.py` to complete image embedding

### Applicable Topics

### 中文：Applicable 主题

- 本节说明 `Applicable 主题` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Applicable Topics

- Psychotherapy and counseling
- Attachment theory research
- Developmental psychology
- Clinical case analysis
- Academic training lectures
- Psychology course instruction
