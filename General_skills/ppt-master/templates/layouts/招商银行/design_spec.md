# China Merchants Bank Transaction Banking - Design Specification

## 中文主体补充：AI_Projects / design_spec.md

本文件属于公开技能 `AI_Projects`。本节为中文主体补充说明，目标是让中文读者在不依赖英文背景的情况下，理解本文件的作用、阅读路径、关键约束和验收标准。
本文件的相对路径是 `ppt-master/templates/layouts/招商银行/design_spec.md`，属于 `AI_Projects` 的参考/工作流/模板/脚本/资产之一。
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


## I. Template Overview

### 中文：模板 概览

- 本节说明 `模板 概览` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：模板 概览

| Property | Description |
| --- | --- |
| **Template Name** | 招商银行 |
| **Display Name** | China Merchants Bank Transaction Banking Template |
| **Use Cases** | 交易银行产品介绍、销售收款方案汇报、客户案例拆解、分行培训材料 |
| **Design Tone** | Brand-consistent, structured, product-focused, refined finance |
| **Theme Mode** | Hybrid theme (brand-red cover/chapter/ending + light content pages) |

Reference slides read before generation: `1, 2, 3, 4, 6, 9, 11, 13, 16, 18`.

## II. Canvas Specification

### 中文：II Canvas 规范

- 本节说明 `II Canvas 规范` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：II Canvas 规范

| Property | Value |
| --- | --- |
| **Format** | Standard 16:9 |
| **Dimensions** | 1280 × 720 px |
| **viewBox** | `0 0 1280 720` |
| **Safe Margins** | 56px left/right, 48px top, 40px bottom |
| **Primary Content Area** | x: 72-1216, y: 140-640 |

## III. Color Scheme

### 中文：III 颜色 Scheme

- 本节说明 `III 颜色 Scheme` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：III 颜色 Scheme

| Role | Color Value | Usage |
| --- | --- | --- |
| **Brand Red** | `#C8152D` | Header strips, emphasis, chapter anchor |
| **Deep Red** | `#8F0F1B` | Dark-page overlay and structural depth |
| **Signal Red** | `#E26A74` | Fine divider accents on cover |
| **Finance Blue** | `#2175D9` | Case-study secondary emphasis |
| **Dark Text** | `#1F1F1F` | Main titles and core copy |
| **Medium Gray** | `#666666` | Secondary copy |
| **Light Gray** | `#E9E9E9` | Dividers and boundary hints |
| **White** | `#FFFFFF` | Background and reverse text |

## IV. Typography System

### 中文：IV Typography System

- 本节说明 `IV Typography System` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：IV 排版 System

| Level | Usage | Size | Weight |
| --- | --- | --- | --- |
| **H1** | Cover title | 54px | Bold |
| **H2** | Chapter title | 46px | Bold |
| **H3** | Content title | 26px | Bold |
| **H4** | TOC / card title | 20px | Bold |
| **Body** | Paragraph text | 16px | Regular |
| **Caption** | Metadata / footer | 12px | Regular |
| **Display Number** | Chapter numeral | 220px | Bold |

**Font Stack**: `"Microsoft YaHei", "PingFang SC", Arial, sans-serif`

## V. Page Structure

### 中文：Page 结构

- 本节说明 `Page 结构` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：页面 结构

### Common Layout

### 中文：Common 版式

- 本节说明 `Common 版式` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Common 版式

| Area | Description |
| --- | --- |
| **Header Strip** | Red brand strip with logo, used on light pages |
| **Title Zone** | Left-aligned title and short key message |
| **Content Body** | Open layout with only light boundary hints |
| **Footer** | Thin divider, section/source/page number |

### Design DNA

### 中文：设计 DNA

- 本节说明 `设计 DNA` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：设计 DNA

1. Reuse the PPT's bank-red brand language, but simplify heavy PPT export artifacts into clean vector geometry.
2. Keep cover / chapter / ending pages visually strong and brand-led.
3. Keep content pages bright and practical for data, process, and case-study layouts.
4. Preserve a secondary finance-blue accent to support comparison and case storytelling.
5. Maintain content coverage ≤ 60%, ensuring visual "breathing room" on data-heavy pages.
6. Use structured layouts (cards, grids, process flows) to organize financial data clearly.

## VI. Page Types

### 中文：VI Page 类型

- 本节说明 `VI Page 类型` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：VI 页面 类型

### 1. Cover Page (`01_cover.svg`)

### 中文：Cover Page cover svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Uses the imported cover background asset `cover_bg（以上为中文意译，具体细节以英文原文为准）。
- png`（以上为中文意译，具体细节以英文原文为准）。
- Centered white typography with restrained divider lines（以上为中文意译，具体细节以英文原文为准）。
- Suitable for title, subtitle, presenter, and date（以上为中文意译，具体细节以英文原文为准）。
### 2. Table of Contents (`02_toc.svg`)

### 中文：表格 of Contents toc svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Light page with red top strip and logo（以上为中文意译，具体细节以英文原文为准）。
- Two-column indexed list for up to four agenda items（以上为中文意译，具体细节以英文原文为准）。
- Red numerals + dark text for fast scanning（以上为中文意译，具体细节以英文原文为准）。
### 3. Chapter Page (`02_chapter.svg`)

### 中文：Chapter Page chapter svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Full-brand dark red background（以上为中文意译，具体细节以英文原文为准）。
- Large translucent chapter numeral in the background（以上为中文意译，具体细节以英文原文为准）。
- Left-aligned title and short chapter description（以上为中文意译，具体细节以英文原文为准）。
### 4. Content Page (`03_content.svg`)

### 中文：内容 Page 内容 svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Light page with a narrow red header strip and right-aligned white logo（以上为中文意译，具体细节以英文原文为准）。
- Page title, section label, key message line, and open body region（以上为中文意译，具体细节以英文原文为准）。
- Footer includes section name, source, and page number（以上为中文意译，具体细节以英文原文为准）。
### 5. Ending Page (`04_ending.svg`)

### 中文：Ending Page ending svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Reuses the cover background asset（以上为中文意译，具体细节以英文原文为准）。
- Centered closing message and compact contact card（以上为中文意译，具体细节以英文原文为准）。
- Suitable for formal client-facing endings（以上为中文意译，具体细节以英文原文为准）。
## VII. Layout Modes

### 中文：VII 版式 模式

- 本节说明 `VII 版式 模式` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：VII 版式 Modes

| Mode | Recommendation |
| --- | --- |
| **Process / Flow** | Use full-width body area with 3-6 horizontal stages |
| **Case Study** | Use split columns or a left-right evidence / solution structure |
| **Product Feature** | Use a short key message on top and modular cards below |
| **Agenda / Sectioning** | Use TOC or chapter page instead of improvising layout headers |

## VIII. Spacing Specification

### 中文：VIII Spacing 规范

- 本节说明 `VIII Spacing 规范` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：VIII 间距 规范

| Property | Value |
| --- | --- |
| **Base Unit** | 8px |
| **Module Gap** | 24px |
| **Card Gap** | 20px |
| **Title to Body** | 44px |
| **Footer Offset** | 32px from bottom |

## IX. SVG Technical Constraints

### 中文：IX SVG Technical 限制

- 本节说明 `IX SVG Technical 限制` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：IX SVG Technical 限制

1. `viewBox` must stay `0 0 1280 720`
2. No `mask`, `<style>`, `class`, `foreignObject`, `textPath`, or animation tags. `clipPath` is allowed only on `<image>` under `shared-standards.md` §1.2
3. Use plain hex colors with `fill-opacity` / `stroke-opacity`
4. Keep image assets semantic and minimal
5. Prefer vector reconstruction over embedding PPT-export fragments

## X. Placeholder Specification

### 中文：Placeholder 规范

- 本节说明 `Placeholder 规范` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Placeholder 规范

| Placeholder | Description |
| --- | --- |
| `{{TITLE}}` | Cover main title |
| `{{SUBTITLE}}` | Cover subtitle |
| `{{DATE}}` | Cover date |
| `{{AUTHOR}}` | Cover presenter / organization |
| `{{TAGLINE}}` | Cover tagline (e.g. product/service line) |
| `{{BRAND_LINE}}` | Cover bottom brand attribution line |
| `{{CHAPTER_NUM}}` | Chapter number |
| `{{CHAPTER_TITLE}}` | Chapter title |
| `{{CHAPTER_DESC}}` | Chapter description |
| `{{PAGE_TITLE}}` | Content page title |
| `{{KEY_MESSAGE}}` | Content page key message |
| `{{CONTENT_AREA}}` | Content page body placeholder |
| `{{SECTION_NAME}}` | Section label / footer section |
| `{{SOURCE}}` | Source text |
| `{{PAGE_NUM}}` | Page number |
| `{{TOC_ITEM_1_TITLE}}` | TOC item 1 title |
| `{{TOC_ITEM_1_DESC}}` | TOC item 1 description |
| `{{TOC_ITEM_2_TITLE}}` | TOC item 2 title |
| `{{TOC_ITEM_2_DESC}}` | TOC item 2 description |
| `{{TOC_ITEM_3_TITLE}}` | TOC item 3 title |
| `{{TOC_ITEM_3_DESC}}` | TOC item 3 description |
| `{{TOC_ITEM_4_TITLE}}` | TOC item 4 title |
| `{{TOC_ITEM_4_DESC}}` | TOC item 4 description |
| `{{TOC_FOOTER}}` | TOC page footer description |
| `{{THANK_YOU}}` | Ending main message |
| `{{ENDING_SUBTITLE}}` | Ending subtitle |
| `{{CLOSING_MESSAGE}}` | Ending supporting sentence |
| `{{CONTACT_NAME}}` | Ending contact person name |
| `{{DEPARTMENT}}` | Ending department name |
| `{{CONTACT_EMAIL}}` | Ending email address |
| `{{CONTACT_PHONE}}` | Ending phone number |

## XI. Asset Specification

### 中文：XI Asset 规范

- 本节说明 `XI Asset 规范` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：XI Asset 规范

### Core Assets

### 中文：Core Assets

- 本节说明 `Core Assets` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：核心 Assets

| Asset | Purpose |
| --- | --- |
| `cover_bg.png` | Cover / ending brand background (dark pages) |
| `logo_white.png` | White brand logo for red and dark pages |
| `logo_dark.png` | 「招商银行 \| 公司金融」dark logo for light page headers |

### Optional Assets

### 中文：Optional Assets

- 本节说明 `Optional Assets` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Optional Assets

| Asset | Purpose |
| --- | --- |
| `page_header_bg.png` | Full-page header background reference (red accent + logo) |
| `logo_crm_banner.png` | 「招商银行 \| CRM 4.0」red banner (product-specific, use when applicable) |
| `ref_content_bg.png` | Content page reference layout (with building illustration, for design reference only) |

### Usage Rule

### 中文：使用方法 Rule

- 本节说明 `使用方法 Rule` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：使用方法 Rule

Core assets are wired into SVG templates. `logo_dark.png` is used on light pages (TOC, content); `logo_white.png` and `cover_bg.png` on dark pages (cover, chapter, ending). Optional assets are available for project-specific customization.

## XII. Chart Specifications

### 中文：XII 图表 规范

- 本节说明 `XII 图表 规范` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：XII 图表 规范

### Recommended Chart Dimensions

### 中文：Recommended 图表 Dimensions

- 本节说明 `Recommended 图表 Dimensions` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Recommended 图表 Dimensions

| Chart Type | Recommended Size |
| --- | --- |
| Bar chart | 500-700 × 400px |
| Pie chart | 300-400px diameter |
| Data card | 160 × 120px |
| Process flow | Full width, 100-140px height |
| Comparison table | 1100 × 300-400px |

### Chart Color Palette

### 中文：图表 颜色 配色

- 本节说明 `图表 颜色 配色` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：图表 颜色 配色

| Usage | Colors |
| --- | --- |
| Primary series | `#C8152D`, `#E26A74`, `#8F0F1B` |
| Secondary series | `#2175D9`, `#5A9FE6` |
| Positive indicator | `#27AE60` |
| Negative indicator | `#E74C3C` |
| Neutral | `#666666` |

## XIII. Usage Instructions

### 中文：XIII 使用方法 Instructions

- 本节说明 `XIII 使用方法 Instructions` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：XIII 使用方法 Instructions

1. Copy the template directory to the project `templates/` folder
2. Read this design specification to understand the visual system
3. Select the appropriate page template for each slide
4. Replace `company_finance_header.png` if the project is not CRM-specific
5. Mark content to be replaced using `{{PLACEHOLDER}}` format
6. Prioritize data charts and structured layouts; keep text concise
7. Generate final SVGs through the Executor role
