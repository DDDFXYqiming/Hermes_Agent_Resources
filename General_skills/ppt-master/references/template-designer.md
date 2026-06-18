> See shared-standards.md for common technical constraints.

# Template Designer — Template Design Role

## 中文主体补充：AI_Projects / template-designer.md

本文件属于公开技能 `AI_Projects`。本节为中文主体补充说明，目标是让中文读者在不依赖英文背景的情况下，理解本文件的作用、阅读路径、关键约束和验收标准。
本文件的相对路径是 `ppt-master/references/template-designer.md`，属于 `AI_Projects` 的参考/工作流/模板/脚本/资产之一。
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


## 中文主体补充：AI_Projects / template-designer.md

本文件属于公开技能 `AI_Projects`。本节为中文主体补充说明，目标是让中文读者在不依赖英文背景的情况下，理解本文件的作用、阅读路径、关键约束和验收标准。
本文件的相对路径是 `ppt-master/references/template-designer.md`，属于 `AI_Projects` 的参考/工作流/模板/脚本/资产之一。
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

### 跨技能协同

- 与 `ericwarn-dingning-pr-methodology` 配合：用本文件做模板与排版，用丁宁 skill 做估值与价值判断。
- 与 `fox-finance-methodology` 配合：用本文件做演示稿载体，用 fox skill 做技术择时与执行节奏。
- 与 `video-notes-generator` 配合：用本文件输出结构化 Markdown，用视频笔记技能做素材来源。
- 与 `generic-agent-code-run` 配合：用本文件做交付规范，用 code-run 做浏览器/桌面/脚本验证。
- 与 `markitdown-skill` 配合：用本文件做最终排版，用 markitdown 做原始资料转换。

### 总结

本节用纯中文描述本文件的目标、读者、阅读顺序、验收、公开要求、排错、跨技能协同；下方英文细则保留机器可读规范。
请把本节视作与原始英文细则并列的中文导读；不要覆盖、删除或翻译原始字段、参数、命令、模板。


## 中文长概览：skill / template-designer.md

本文件属于公开技能 `skill` 下的 `template-designer.md` 文档，目标是把幻灯片、模板、图表、配图、动画或脚本相关的全部规格统一收纳，便于复用与扩展。
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

## 中文主体说明：Hermes_Agent_Resources 参考资料：template designer

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


## Core Mission

### 中文：Core Mission

- 本节说明 `Core Mission` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：核心 Mission

Generate reusable page templates for the **global template library** based on a finalized template brief.

> This is a standalone role: only triggered via the `/create-template` workflow. It is **not** the project-level template selection/customization step in the main PPT generation pipeline.

## Usage

### 中文：使用方法

- 本节说明 `使用方法` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：使用方法

- **Trigger**: `/create-template` workflow
- **Output location**: `templates/layouts/<template_name>/`
- **Input**: finalized template brief (template ID, display name, category, applicable scenarios, tone, theme mode, canvas format, optional reference assets)

When the workflow provides a PPTX reference source, the effective input package comes from the unified `pptx_template_import.py` preparation workspace and becomes:

- finalized template brief
- `manifest.json` — single source of truth (slide size, theme, per-master themes, assets, asset map, placeholders, layouts, masters, slides, SVG file paths, page-type candidates)
- `summary.md` — short orientation digest derived from manifest.json
- exported `assets/`
- `svg/master_*.svg` / `svg/layout_*.svg` — every master / layout in the deck rendered once as standalone SVG, including ones no sample slide references (template packages often ship more design surfaces than the embedded samples exercise)
- `svg/slide_NN.svg` — each slide's own shapes and slide-local background only; master / layout decoration and backgrounds are **not** inlined here
- `svg/inheritance.json` — which layout / master each slide consumes
- `svg-flat/slide_NN.svg` — companion view; each slide is self-contained so you can preview or screenshot a single page without losing the surrounding chrome. Use it as a sanity check for "what would PowerPoint actually show", not as an authoring source — the master/layout chrome will be duplicated across every flat slide.
- optional screenshots for visual cross-checking

PPTX import interpretation:

- Placeholder guides in master / layout SVGs are layout signals. Use `manifest.json` placeholder records for type / index / geometry / base style; do not copy dashed guide boxes into final templates unless the visual design truly uses dashed boxes.
- Charts, SmartArt, diagrams, and OLE objects may appear as typed placeholders in layered SVGs. In flat SVGs they may show preview images. Treat them as source intent markers, not reusable decorative assets.
- The asset filenames referenced by SVGs are governed by the manifest asset map. Prefer those references over inventing duplicate asset names.

Input priority for PPTX-backed template creation:

1. `manifest.json` for all factual metadata (theme, assets, unique layout/master structure, slide reuse, page-type guidance)
2. `svg/master_*.svg` + `svg/layout_*.svg` — the **primary source for the deck's shared visual language**: backgrounds, page chrome, decorative bars, recurring brand motifs. These are what the new template's fixed structure should adopt or reinterpret. Read these before any slide SVG.
3. `svg/inheritance.json` for confirming which slide uses which layout / master
4. exported `assets/` for reusable visual resources
5. `svg/slide_NN.svg` — each slide's unique content, useful for judging composition rhythm and content density (not for fixed structure)
6. `summary.md` only as a fast scan; never as the canonical fact source
7. screenshots / original PPTX only for style verification

---

## Page Roster

### 中文：Page Roster

- 本节说明 `Page Roster` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：页面 Roster

The output page set is determined by **replication mode**, declared in the finalized template brief:

| Mode | When to use | Roster |
|------|-------------|--------|
| `standard` (default) | Most templates — clean, reusable, balanced coverage | `01_cover`, `02_chapter`, `03_content`, `04_ending`, optional `02_toc` |
| `fidelity` | User explicitly wants strict replication of a source PPTX, but still wants the AI to clean / cluster / cap variants | Standard roster + one variant per distinct layout cluster found in `manifest.json` |
| `mirror` | User wants every source slide preserved 1:1 as a reference page (someone else's polished deck used as a library template). Verbatim copy, no abstraction, no placeholders | One SVG per source slide, named `<NNN>_<page_type>.svg` by source order |

### Standard mode

### 中文：Standard 模式

- 本节说明 `Standard 模式` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Standard mode

| # | Filename | Purpose | Description |
|---|----------|---------|-------------|
| 01 | `01_cover.svg` | Cover | Fixed structure: title, subtitle, date, organization |
| 02 | `02_chapter.svg` | Chapter page | Fixed structure: chapter number, chapter title |
| 03 | `03_content.svg` | Content page | Flexible structure: only defines header/footer; content area freely laid out by AI |
| 04 | `04_ending.svg` | Ending page | Fixed structure: thank-you message, contact info |
| -- | `02_toc.svg` | Table of contents | Optional: TOC title, chapter list (number + title) |

**Design philosophy**: Templates define visual consistency and structural pages; content pages maintain maximum flexibility.

**Naming note**: TOC page keeps `02_toc.svg` naming for template library compatibility and sort order.

### Fidelity mode

### 中文：Fidelity 模式

- 本节说明 `Fidelity 模式` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Fidelity mode

When the brief sets `Replication mode: fidelity`, derive the page roster from `manifest.json` page-type clusters and emit one SVG per distinct visual cluster.

**Variant naming**: append a lowercase letter suffix to the parent type's index, preserving sort order:

| Parent type | Example variants |
|-------------|------------------|
| Chapter | `02a_chapter_full.svg`, `02b_chapter_minimal.svg` |
| Content | `03a_content_two_col.svg`, `03b_content_data_card.svg`, `03c_content_quote.svg` |
| Ending | `04a_ending_thanks.svg`, `04b_ending_contact.svg` |

Extension page types beyond the canonical four (transition / appendix / disclaimer / divider) take the next free index: `05_section_break.svg`, `06_appendix.svg`, `07_disclaimer.svg`.

**Roster decision**:

- Cluster slides from `manifest.json` by `pageType` + visual structure (column count, hero-image vs. icon-grid vs. quote, etc.)
- One SVG per cluster — do **not** emit a variant for a cluster represented by a single source slide unless that slide is structurally distinct from existing variants
- One variant per visually distinct cluster — let the source's structural diversity drive the count. Collapse only **near-duplicates** (same column count, same hero element, same content density); do not collapse genuine structural differences just to keep the variant count down. If you find yourself wanting one variant per source slide, that is the signal the user should be in `mirror` mode, not `fidelity`
- Record every emitted page in `design_spec.md §V Page Roster` and in the `pages` field of the `layouts_index.json` entry (auto-collected by `register_template.py`)

> Variants reuse the parent type's placeholder set — see §4 (Placeholder Reference) below.

### Mirror mode

### 中文：Mirror 模式

- 本节说明 `Mirror 模式` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Mirror mode

When the brief sets `Replication mode: mirror`, the role does **not** abstract or reconstruct. Each source slide becomes one template page **byte-for-byte**:

- Source: `<import_workspace>/svg-flat/slide_NN.svg` (the self-contained "what PowerPoint shows" view). Do **not** read or use `svg/master_*.svg`, `svg/layout_*.svg`, or `svg/inheritance.json` — chrome / content separation is irrelevant because mirror does not insert placeholders.
- Output: `templates/layouts/<template_id>/<NNN>_<page_type>.svg`, where `<NNN>` is the zero-padded source slide index (3 digits) and `<page_type>` is derived from `manifest.json` `pageTypeCandidates` — `cover` / `toc` / `chapter` / `content` / `ending`. When the page-type heuristic is ambiguous, fall back to `content`. Preserve source slide order via the numeric prefix.
- Modifications allowed: **only** rewriting `<image href="...">` paths to point at the local `assets/` copy, and renaming asset files to semantic names. Everything else — geometry, decoration, sprite-sheet wrappers, original example text, chart placeholders, embedded fonts — is copied as-is.
- Modifications forbidden: inserting `{{TITLE}}` / `{{CONTENT_AREA}}` / any other placeholder; "cleaning up" decorative complexity; merging similar slides; dropping master/layout chrome (it's already baked into the flat SVG, leave it).
- `design_spec.md` §V Page Roster lists every emitted file with **a one-line description** of what the page contains and what content slot it suits — Strategist selects mirror pages purely from these descriptions, since the SVG itself carries no placeholder contract.

**Why mirror has no placeholders**: it is consumed as a **visual reference** rather than a templated form. Executor's mirror path (see [executor-base.md](executor-base.md) §1.1) copies the chosen mirror page into the project and edits text elements in place against the project content — no `{{}}` substitution happens. This keeps the library asset 100% verbatim and lets the user re-discover the source deck by browsing `templates/layouts/<template_id>/` directly.

**What mirror is not**: a pixel-perfect re-rendering pipeline test. Charts, SmartArt, OLE objects, and EMF / WMF media that fail to round-trip in `pptx_template_import.py` will fail the same way in mirror. If the import workspace has missing media or unsupported objects, mirror inherits those gaps — the user should be told before generation begins.

---

## Template Design Specifications

### 中文：模板 设计 规范

- 本节说明 `模板 设计 规范` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：模板 设计 规范

### 1. Must Generate design_spec.md

### 中文：必须 Generate design_spec md

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Scope rule — personality only（以上为中文意译，具体细节以英文原文为准）。
- ** A template `design_spec（以上为中文意译，具体细节以英文原文为准）。
- md` describes **what makes this template recognizable**: brand colors, signature decorative motifs, page-by-page visual character, bundled assets（以上为中文意译，具体细节以英文原文为准）。
- SVG technical constraints, PPT compatibility rules → [`shared-standards（以上为中文意译，具体细节以英文原文为准）。
- Canonical placeholder vocabulary → §4 below
- Content methodology (pyramid / SCQA / MECE) → [`strategist.md`](strategist.md)

Re-declaring any of these in a template `design_spec.md` is noise — Strategist already has them in context, and duplication forces every relaxation to sweep N templates instead of one source. **If a rule is generic, omit it. If this template breaks a generic rule, write only the deviation.**

**Required skeleton:**

```markdown
---
template_id: <id>
category: brand | general | scenario | government | special
summary: <one-line tone & use case>
keywords: [tag1, tag2, tag3]
primary_color: "#......"
canvas_format: ppt169
replication_mode: standard | fidelity | mirror
# Optional — only when this template overrides canonical placeholder vocabulary.
# Omit entirely for `mirror` mode (mirror has no placeholders).
# placeholders:
#   01_cover: ["{{TITLE}}", "{{SUBTITLE}}", "{{BRAND_LOGO}}"]
#   03_content: ["{{KEY_MESSAGE}}", "{{CONTENT_AREA}}"]
---

# [Template Name] — Design Specification

## I. Template Overview
- Use cases, design tone, theme mode (light / dark / mixed)
- One paragraph: what visually identifies this template at a glance

## II. Color Scheme
- HEX values with role labels (primary / accent / background / text / etc.)
- Brand-specific application rules when present (e.g. "KPI cards rotate blue→green→red→yellow")

## III. Typography (omit when using the default `Arial, "Microsoft YaHei", sans-serif` stack)
- Per-role font stacks ONLY when the template intentionally diverges (display serif title, brand typeface, etc.)
- Font-install or embedding requirement when a non-preinstalled font leads any stack
- Body baseline px (informational; `spec_lock.md` owns the actual values per project)

## IV. Signature Design Elements
- Decorative motifs that ARE this template — top bar, gradient underline, logo treatment, brand emblem placement
- Optional XML snippet for any reusable component unique to this template

## V. Page Roster
One row per emitted SVG describing what this template's version of cover / chapter / content / ending looks like (background treatment, decorative anchors, layout rhythm). For `fidelity` mode, also note the cluster source and visual differentiator. For `mirror` mode the roster is the **load-bearing artifact** — Strategist picks mirror pages purely from these descriptions, so each row must include enough detail to distinguish it from siblings (column count, hero element, content density, what kind of content slot it fits — "three-column KPI grid with large numbers, suits quarterly summary"). Roster entries must match the actual SVG files on disk.

## VI. Assets (omit when none)
Logos, cover backgrounds, brand textures bundled with the template package — file name, dimensions, intended usage.

## VII. Placeholder Overrides (omit when none)
Reference the `placeholders:` frontmatter declaration and explain the rationale (e.g. "consulting decks lead with `{{KEY_MESSAGE}}` instead of `{{PAGE_TITLE}}`").
```

Sections to **omit** from template `design_spec.md` (sourced elsewhere — listing them here is noise):

| Don't write | Source |
|---|---|
| SVG technical constraints / Mandatory rules / Prohibited elements | `shared-standards.md` §1 |
| PPT compatibility rules (`<g opacity>`, inline-styles-only, etc.) | `shared-standards.md` |
| Generic layout pattern library (centered card / 三栏 / timeline / …) | `design_spec_reference.md` §V |
| Generic spacing bands (margin 40-60px, card gap 20-32px, etc.) | `design_spec_reference.md` §V |
| Generic font-size hierarchy (cover 2.5-5x body, page title 1.5-2x, …) | `design_spec_reference.md` §IV |
| Canonical placeholder table (`{{TITLE}}`, `{{PAGE_NUM}}`, …) | §4 below |
| Content methodology (pyramid / SCQA / MECE / 金字塔) | `strategist.md` |
| "Usage Instructions" boilerplate (copy template / select page / …) | `create-template.md` |
| Created Date / Page Count rows | not a library-level field |

When rewriting an existing template that contains the omitted sections, delete them — do not leave a "see XXX" pointer behind. The pointer is what this scope rule replaces.

### 2. Inherit Design Specification

### 中文：Inherit 设计 规范

- 本节说明 `Inherit 设计 规范` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Inherit 设计 规范

Templates must strictly follow the finalized template brief and the generated `design_spec.md`:
- **Canvas dimensions**: viewBox matches the design spec
- **Color scheme**: Uses primary, secondary, and accent colors from the spec
- **Font plan**: Uses the per-role font families declared in the spec
- **Layout principles**: Margins and spacing conform to the spec

If PPTX import output exists:
- Prefer imported theme colors and fonts over visually guessed values
- Reuse exported `assets/` images directly — `<image>` references in `svg/` already point at canonical files
- Treat page-type candidates from `manifest.pageTypeCandidates` as hints, not guarantees

**Precondition**:

- When PPTX import output is provided, do not generate any template SVG or `design_spec.md` until every file under `<import_workspace>/svg/` has been read — including `master_*.svg`, `layout_*.svg`, and every `slide_*.svg`
- Before template generation begins, explicitly report the read slide indexes

### 2.1 PPTX Import Simplification Rule

### 中文：PPTX Import Simplification Rule

- 本节说明 `PPTX Import Simplification Rule` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：2.1 PPTX Import Simplification Rule

The imported PPTX is a **reference source**, not a direct conversion target.

Do:
- preserve brand assets, recurring backgrounds, and stable structural motifs
- rebuild the layout into a clean SVG structure aligned with PPT Master constraints
- simplify repeated decorative fragments into a smaller number of maintainable SVG elements
- use a background image asset when the original decorative layer is too complex to recreate cleanly
- use cleaned slide SVG references to inspect composition, spacing, text hierarchy, and fixed decorative structure only after factual metadata has been anchored
- read every reference SVG under `svg/` — `master_*.svg`, `layout_*.svg`, and every `slide_*.svg` regardless of slide count. Master / layout files describe the deck's shared visual language (read first); slide files describe per-page content (read after). Partial coverage drops template fidelity.
- rename adopted assets to semantic names (`cover_bg.png`, `brand_emblem.png`) rather than carrying raw `image3.png` into the final template

Do not:
- attempt 1:1 translation of every PowerPoint shape, group, shadow, or decorative fragment
- mirror PPT-specific complexity when it makes the resulting SVG brittle or hard to edit
- introduce dense low-value vector detail that does not materially improve template reuse

### 3. Placeholder Markers

### 中文：Placeholder Markers

- 本节说明 `Placeholder Markers` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：3. Placeholder Markers

> **Mirror mode skips this section entirely.** Mirror SVGs are verbatim copies of the source flat slides — they carry no `{{}}` markers. Executor reads them as visual references and edits text in place (see [executor-base.md](executor-base.md) §1.1). The rest of this section applies to `standard` and `fidelity` only.

Use clear placeholder markers for replaceable content:

```xml
<!-- Text placeholder -->
<text x="80" y="320" fill="#FFFFFF" font-size="48" font-weight="bold">
  {{TITLE}}
</text>

<!-- Content area placeholder (content page only) -->
<rect x="40" y="90" width="1200" height="550" fill="#FFFFFF" rx="8"/>
<text x="640" y="365" text-anchor="middle" fill="#CBD5E1" font-size="16">
  {{CONTENT_AREA}}
</text>
```

### 4. Placeholder Reference (canonical convention, overridable per template)

### 中文：Placeholder 参考 canonical convention overridable per 模板

- 本节说明 `Placeholder 参考 canonical convention overridable per 模板` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Placeholder 参考 canonical convention overridable per 模板

This is the **default vocabulary** used across the library. Newly created templates SHOULD prefer these names so projects that consume the library find familiar slots; designers MAY substitute or extend them when a style genuinely needs different vocabulary (e.g. consulting decks lead with `{{KEY_MESSAGE}}` instead of `{{PAGE_TITLE}}`; a brand cover may need `{{BRAND_LOGO}}`).

`svg_quality_checker.py --template-mode` emits **advisory warnings** when a page lacks the conventional placeholder for its type. To silence those warnings — and document the template's actual contract — declare a `placeholders:` map in `design_spec.md` frontmatter:

```yaml
placeholders:
  01_cover: ["{{TITLE}}", "{{SUBTITLE}}", "{{BRAND_LOGO}}"]
  03_content: ["{{KEY_MESSAGE}}", "{{CONTENT_AREA}}"]
  03a_content_dual_col: []   # explicitly assert "no required placeholders"
```

| Placeholder | Purpose | Applicable page | Convention role |
|------------|---------|-------------------|--------|
| `{{TITLE}}` | Main title | Cover | Default |
| `{{SUBTITLE}}` | Subtitle | Cover | Default |
| `{{DATE}}` | Date | Cover | Default |
| `{{AUTHOR}}` | Author / Organization | Cover | Default |
| `{{CHAPTER_NUM}}` | Chapter number | Chapter page | Default |
| `{{CHAPTER_TITLE}}` | Chapter title | Chapter page | Default |
| `{{CHAPTER_DESC}}` | Chapter description | Chapter page | Optional |
| `{{PAGE_TITLE}}` | Page title | Content page | Default |
| `{{CONTENT_AREA}}` | Content area | Content page | Default |
| `{{PAGE_NUM}}` | Page number | Content page, ending page | Default |
| `{{KEY_MESSAGE}}` | Key takeaway | Content page (consulting style) | Style-specific |
| `{{SECTION_NAME}}` | Section name | Content page footer | Optional |
| `{{SOURCE}}` | Data source | Content page footer | Optional |
| `{{THANK_YOU}}` | Thank-you message | Ending page | Default |
| `{{CONTACT_INFO}}` | Contact info | Ending page | Default |
| `{{ENDING_SUBTITLE}}` | Ending subtitle | Ending page | Optional |
| `{{CLOSING_MESSAGE}}` | Closing message | Ending page | Style-specific |
| `{{COPYRIGHT}}` | Copyright | Ending page | Optional |

For TOC pages in **newly created library templates**, use indexed placeholders:

- `{{TOC_ITEM_1_TITLE}}`, `{{TOC_ITEM_1_DESC}}`
- `{{TOC_ITEM_2_TITLE}}`, `{{TOC_ITEM_2_DESC}}`
- ...

Do **not** create new TOC placeholder families such as `{{CHAPTER_01_TITLE}}` for new templates. Existing templates may contain legacy placeholder variants, but new library assets should converge on the indexed TOC contract.

Variants reuse their parent type's placeholder set by default: every `03*_content*.svg` shares the content placeholder list above, unless the spec frontmatter declares an override for that specific stem.

When rebuilding from imported PPTX references, placeholder insertion takes priority over visual mimicry. If the original layout leaves insufficient room for canonical placeholders, adjust the layout instead of inventing one-off placeholder families — or, if the deviation is intentional and meaningful, declare it in frontmatter.

---

## Output Requirements

### 中文：输出 依赖与要求

- 本节说明 `输出 依赖与要求` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：输出 依赖与要求

### File Save Location

### 中文：File Save Location

- 本节说明 `File Save Location` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：File Save Location

Standard mode (default):

```
templates/layouts/<template_name>/
├── design_spec.md     # Design specification (required)
├── 01_cover.svg
├── 02_chapter.svg
├── 02_toc.svg          # Optional
├── 03_content.svg
├── 04_ending.svg
└── *.png / *.jpg       # Image assets (if any)
```

Fidelity mode adds variants and extension pages, e.g.:

```
templates/layouts/<template_name>/
├── design_spec.md
├── 01_cover.svg
├── 02a_chapter_full.svg
├── 02b_chapter_minimal.svg
├── 02_toc.svg
├── 03a_content_two_col.svg
├── 03b_content_data_card.svg
├── 03c_content_quote.svg
├── 04_ending.svg
├── 05_section_break.svg
└── *.png / *.jpg
```

Mirror mode emits one SVG per source slide, named by source order:

```
templates/layouts/<template_name>/
├── design_spec.md
├── 001_cover.svg
├── 002_toc.svg
├── 003_content.svg
├── 004_content.svg
├── 005_chapter.svg
├── 006_content.svg
├── ...
├── 049_content.svg
├── 050_ending.svg
└── *.png / *.jpg
```

Filenames preserve the source slide order via the 3-digit prefix; `<page_type>` is derived from `manifest.json` `pageTypeCandidates`. No `{{}}` placeholders appear in any mirror SVG.

### Template Preview

### 中文：模板 Preview

- 本节说明 `模板 Preview` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：模板 Preview

After each template is generated, provide a brief summary table listing each template's status.

If the template is based on PPTX import output, briefly note:
- which extracted assets were reused directly
- which complex original decorations were intentionally simplified
- whether any page-type mapping required judgment beyond the import heuristic

---

## Using Pre-built Template Library (Optional)

### 中文：Using Pre-built 模板 Library Optional

- 本节说明 `Using Pre-built 模板 Library Optional` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Using Pre-built 模板 Library Optional

If suitable template resources already exist, use them directly instead of generating new ones:

1. **Copy template**: Copy template files to the project's `templates/` directory
2. **Adjust colors**: Modify colors per the project design spec
3. **Customize**: Make project-specific adjustments

This section describes downstream reuse. The `Template_Designer` role itself is responsible for creating or normalizing the reusable library asset first.

**Example library structure** (query `templates/layouts/layouts_index.json`):

```
templates/layouts/
├── google_style/      # Google Material Design style
├── academic_defense/  # Academic defense style
└── 招商银行/          # China Merchants Bank brand style
```

---

## Phase Completion Checkpoint

### 中文：Phase Completion Checkpoint

- 本节说明 `Phase Completion Checkpoint` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Phase Completion Checkpoint

```markdown
## Template_Designer Phase Complete

- [x] Read `references/template-designer.md`
- [x] Replication mode confirmed: `standard` | `fidelity` | `mirror`
- [x] Every page listed in `design_spec.md §V Page Roster` saved to `templates/layouts/<template_name>/`
- [x] Naming convention applied (standard / fidelity: letter-suffix variants; mirror: `<NNN>_<page_type>.svg`)
- [x] Templates follow design spec (colors, fonts, layout)
- [x] Placeholder markers are clear and standardized (standard / fidelity); mirror SVGs contain **no** `{{}}` markers
- [ ] **Next step**: Validate assets and register the template in `layouts_index.json` (include `pages` field)
```
