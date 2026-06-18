---
description: Verify chart coordinates against the design spec using svg_position_calculator.py
---

## 中文主体补充：AI_Projects / verify-charts.md

本文件属于公开技能 `AI_Projects`。本节为中文主体补充说明，目标是让中文读者在不依赖英文背景的情况下，理解本文件的作用、阅读路径、关键约束和验收标准。
本文件的相对路径是 `ppt-master/workflows/verify-charts.md`，属于 `AI_Projects` 的参考/工作流/模板/脚本/资产之一。
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
## 中文长概览：skill / verify-charts.md

本文件属于公开技能 `skill` 下的 `verify-charts.md` 文档，目标是把幻灯片、模板、图表、配图、动画或脚本相关的全部规格统一收纳，便于复用与扩展。
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

## 中文主体说明：Hermes_Agent_Resources 工作流：verify charts

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

# Verify Charts Workflow

> Standalone post-generation step. Run after a deck containing data charts has finished SVG generation, before post-processing & export. Catches the 10–50 px coordinate errors AI models routinely introduce when mapping data to pixel positions.

This workflow is **independent**: it reads `design_spec.md` and the generated SVGs, then runs the calculator script — no upstream conversation context required. Safe to invoke in a fresh session.

## When to Run

### 中文：When to 运行

- 本节说明 `When to 运行` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：When to Run

- The deck contains one or more data visualization charts of types supported by a **single** `svg_position_calculator.py calc` invocation. The supported set is fixed by the calculator's CLI subcommands (`bar`, `line`, `pie`, `radar`) and their single-series model — see Step 1 for the exact `charts_index.json` keys.
- SVGs are generated to `<project_path>/svg_output/` and `svg_quality_checker.py` has passed.
- Post-processing (`finalize_svg.py`, `svg_to_pptx.py`) has **not yet** run.

Composite/derived chart types (multi-series, stacked, signed-delta, mirrored, dual-axis, cumulative-overlay) cannot be calibrated by one calc call and are out of scope. Same for non-XY visualizations (treemap / gauge / funnel / heatmap / matrix / bubble / box plot) and infographics / diagrams / frameworks / maps.

---

## Step 1: Build the page list from the design spec

### 中文：Step Build the page list from the 设计 规范

- 本节说明 `Step Build the page list from the 设计 规范` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：步骤 Build the 页面 list from the 设计 规范

Read `<project_path>/design_spec.md` §VII Visualization Reference List (authoritative deck plan; cross-check against §IX page outline) and **filter strictly to the calculator-supported set below**. Anything outside this set is out of scope — do NOT include it in the list, even if §VII labels it as a chart.

| Calculator subcommand | In-scope `charts_index.json` keys | Notes |
|-----------------------|-----------------------------------|-------|
| `calc bar`   | `bar_chart`, `horizontal_bar_chart` | Use `--horizontal` for the latter. Single series only. |
| `calc line`  | `line_chart`, `area_chart`, `scatter_chart` | Area uses line output as the top boundary, then closes to `y_max`. |
| `calc pie`   | `pie_chart`, `donut_chart` | Donut: pass `--inner-radius`. |
| `calc radar` | `radar_chart` | Separate subcommand — not under `calc pie`. |

**Verifiable via repeated calls + cumulative precompute** (see [Stacked recipe](#stacked-recipe) below):

- `stacked_bar_chart`, `stacked_area_chart` — include in the Step 1 list, mark `type=stacked-bar` / `type=stacked-area`, and verify per the recipe.

**Out of scope** (no single-call model and no clean repeat-call recipe — skip silently):

- Multi-series / signed / paired / dual-axis bar & line: `grouped_bar_chart`, `butterfly_chart`, `waterfall_chart`, `bullet_chart`, `dumbbell_chart`, `pareto_chart`, `dual_axis_line_chart`
- Non-XY data visualizations: `treemap_chart`, `gauge_chart`, `progress_bar_chart`, `funnel_chart`, `matrix_2x2`, `bubble_chart`, `heatmap_chart`, `box_plot_chart`, `kpi_cards`
- Everything in the `process` / `strategy` / `architecture` / `infographic` / `table` categories of `charts_index.json`

Resulting list:

```
P03 03_market_share.svg  type=bar
P07 07_growth.svg        type=line
P11 11_share_split.svg   type=pie
```

If §VII is absent (legacy project / free-structure deck), skip this workflow and report: "design_spec.md has no §VII — chart pages cannot be enumerated authoritatively, verify-charts skipped". Do NOT fall back to guessing from SVG content; that reintroduces the silent-skip failure this workflow was built to eliminate.

If the filtered list is empty, output `verify-charts: spec declares no calculator-supported chart pages, nothing to verify` and stop.

---

## Step 2: Per page — read SVG, run calculator, compare, update

### 中文：Step Per page read SVG 运行 calculator compare update

- 本节说明 `Step Per page read SVG 运行 calculator compare update` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：步骤 Per 页面 read SVG run calculator compare update

For each page in the Step 1 list:

1. Read `<project_path>/svg_output/<page>.svg`.
2. Locate the plot-area definition:
   - Preferred: `<!-- chart-plot-area: ... -->` marker placed by Executor (see [executor-base.md §3.1](../references/executor-base.md)). Read coordinates directly.
   - If missing: derive the plot area from the SVG's axis lines (rectangular charts) or center/radius elements (radial charts). Then **add the marker back to the SVG** so future runs are not paying this cost again.
3. Read the data series from the SVG's `<text>` label/value elements.
4. **Read axis tick labels (bar charts only).** Locate the `<text>` elements along the value axis — these are the X-axis labels for horizontal bars, or Y-axis labels for vertical bars. Extract the first and last tick values to determine the axis range (e.g. `0%` to `120%` → range `0,120`). Pass this range as `--value-range "0,120"` to the calculator. If the SVG has no explicit tick labels (data labels only, no grid), omit `--value-range` and let the calculator auto-normalize — but flag the receipt as `scale=auto (no ticks)`.
5. Run the matching calculator command:

   ```bash
   # bar_chart / horizontal_bar_chart (add --horizontal for the latter)
   # IMPORTANT: always pass --value-range from axis tick labels (step 4)
   python3 skills/ppt-master/scripts/svg_position_calculator.py calc bar \
     --data "Label1:Value1,Label2:Value2" --area "x_min,y_min,x_max,y_max" \
     --bar-width 120 --value-range "0,axis_max"

   # line_chart / area_chart / scatter_chart — area uses line output as the top boundary, then closes to y_max
   python3 skills/ppt-master/scripts/svg_position_calculator.py calc line \
     --data "x1:y1,x2:y2,..." --area "x_min,y_min,x_max,y_max" --y-range "0,max"

   # pie_chart
   python3 skills/ppt-master/scripts/svg_position_calculator.py calc pie \
     --data "Slice1:Value1,Slice2:Value2" --center "cx,cy" --radius 200

   # donut_chart (pie with inner-radius)
   python3 skills/ppt-master/scripts/svg_position_calculator.py calc pie \
     --data "Slice1:Value1,Slice2:Value2" --center "cx,cy" --radius 200 --inner-radius 120

   # radar_chart (separate subcommand)
   python3 skills/ppt-master/scripts/svg_position_calculator.py calc radar \
     --data "Dim1:Value1,Dim2:Value2,Dim3:Value3" --center "cx,cy" --radius 200
   ```

   Area chart fill path closes to the bottom edge of the plot area:

   ```svg
   M first_x,first_y ... L last_x,last_y L last_x,y_max L first_x,y_max Z
   ```

6. **Scale-aware comparison.** Compare calculator output against the SVG's existing coordinates. Before declaring a mismatch, verify that the calculator output header shows `Value scale: axis ticks (...)` matching the SVG's drawn axis. If it shows `auto (max*1.1)` for a chart that has explicit axis ticks, the calculator was invoked without `--value-range` — go back to step 4 and re-run with the correct range. **Do NOT update the SVG with mismatched-scale output.** Only update SVG attributes when the scale is confirmed to match and coordinates genuinely differ. Update by hand (do NOT use regex / bulk replacement — coordinates are positional and easy to swap incorrectly).

After updating any page, re-run the quality checker on the project to confirm nothing broke:

```bash
python3 skills/ppt-master/scripts/svg_quality_checker.py <project_path>
```

---

## Stacked recipe

### 中文：Stacked recipe

- 本节说明 `Stacked recipe` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Stacked recipe

`stacked_bar_chart` and `stacked_area_chart` are not single-call but reduce cleanly to repeated calls on existing primitives. The operator already had to compute cumulative values to draw the SVG — verify-charts reuses them.

**Stacked bar** — for N stacked series on the same x categories, run `calc bar` N times. Pass each segment's **height** as the data value, and shift `--area`'s `y_max` down by the sum of all lower segments for that category. Compare each segment's `(x, y, width, height)` against the SVG.

```bash
# Example: two-series stack at category "Q1" with bottom=30, top=20, plot area y from 100 to 500
# Run 1 — bottom segment (origin = baseline)
python3 skills/ppt-master/scripts/svg_position_calculator.py calc bar \
  --data "Q1:30,Q2:..." --area "x_min,100,x_max,500" \
  --bar-width 80 --value-range "0,axis_max"
# Run 2 — top segment (origin shifted up by bottom segment's height in pixels)
python3 skills/ppt-master/scripts/svg_position_calculator.py calc bar \
  --data "Q1:20,Q2:..." --area "x_min,100,x_max,<500 - bottom_height_px>" \
  --bar-width 80 --value-range "0,axis_max"
```

**Stacked area** — for N stacked series, run `calc line` N times on **cumulative** y-values (series 1 raw; series 2 = series1+series2; …). Each call yields the top boundary of one band. Each band's SVG path closes to the **previous** band's top boundary (not to `y_max`).

If a stack page's segment positions don't reduce to this recipe (e.g., negative segments, percent-stacked with non-100 totals), mark it `manual-verify` in the receipt and inspect by hand — do not silently pass.

---

## Step 3: Per-page receipt

### 中文：Step Per-page receipt

- 本节说明 `Step Per-page receipt` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：步骤 Per-page receipt

Output one line per page from the Step 1 list. Receipt count MUST equal Step 1 list length — that is the gate-closing artifact.

```
verify-charts: 03_market_share.svg | type=bar          | scale=0-100 (from ticks) | calc=ran | svg=updated
verify-charts: 07_growth.svg       | type=line         | scale=N/A                | calc=ran | svg=unchanged (already accurate)
verify-charts: 11_share_split.svg  | type=pie          | scale=N/A                | calc=ran | svg=updated | marker=added (was missing)
verify-charts: 14_revenue_mix.svg  | type=stacked-bar  | scale=0-200 (from ticks) | calc=ran×3 | svg=updated (per Stacked recipe)
verify-charts: 15_unit_economics.svg | type=stacked-area | scale=N/A | manual-verify | reason=percent-stacked, recipe does not apply
```

---

## After verification

### 中文：After 校验

- 本节说明 `After 校验` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：After 校验

Continue with post-processing & export ([SKILL.md Step 7](../SKILL.md)):

```bash
python3 skills/ppt-master/scripts/total_md_split.py <project_path>
python3 skills/ppt-master/scripts/finalize_svg.py <project_path>
python3 skills/ppt-master/scripts/svg_to_pptx.py <project_path>
```
