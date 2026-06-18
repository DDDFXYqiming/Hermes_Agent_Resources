# Type: scene

## 中文长概览：skill / scene.md

本文件属于公开技能 `skill` 下的 `scene.md` 文档，目标是把幻灯片、模板、图表、配图、动画或脚本相关的全部规格统一收纳，便于复用与扩展。
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

## 中文主体说明：Hermes_Agent_Resources 参考资料：scene

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


Atmospheric environment with narrative — a moment, a place, a situation rendered as a small story. Used for case studies, brand storytelling, lifestyle pages, personal narrative slides.

> **What scene means inside a PPT block**: the image internally is **a moment in a place** — environment, figures (if any), atmosphere, mood. Unlike `hero` (single dominant subject), scene has **context and narrative**. Unlike `background` (no subject), scene has **inhabitants**.

## 1. Composition skeleton

### 中文：Composition skeleton

- 本节说明 `Composition skeleton` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：构图 skeleton

```
   ┌────────────────────────────────────┐
   │  sky / atmosphere (foreground      │
   │                    or upper area)  │
   │                                     │
   │    figure / subject in environment  │
   │           ↑ foreground              │
   │  ────────────────────────────       │
   │   middle ground (context, objects)  │
   │  ────────────────────────────       │
   │   background (atmospheric depth)    │
   └────────────────────────────────────┘
```

| LAYOUT | Three-layer composition: foreground (subject + immediate context), middle ground (supporting environment), background (atmospheric depth). The viewer reads the scene like a small story |
| ELEMENTS | One or more figures (simplified silhouettes unless `corporate-photo`) in an environment. Environmental elements (sun, lamp, tree, desk) support the narrative |
| NEGATIVE SPACE | Atmospheric perspective creates breathing room — background paler than foreground |
| ATMOSPHERE | Lighting direction, color temperature, and mood are deliberate (golden-hour, evening light, morning haze, etc.) |

---

## 2. Container sizing for local PPT inserts

### 中文：容器 sizing for local PPT inserts

- 本节说明 `容器 sizing for local PPT inserts` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：2. Container sizing for local PPT inserts

| Use | Canvas | Aspect | Padding |
|---|---|---|---|
| Hero scene banner | 1200×600 | 2:1 | 10% (scenes fill the frame) |
| Half-page narrative | 600×800 | 3:4 | 10% |
| Wide scenic | 1200×500 | 2.4:1 | 10% |
| Square scene | 700×700 | 1:1 | 10% |

---

## 3. Text-policy variants

### 中文：Text-policy variants

- 本节说明 `Text-policy variants` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：3. Text-policy variants

### `text_policy: none` (essentially always)

### 中文：text_policy none essentially always

- 本节说明 `text_policy none essentially always` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：`text_policy: none` (essentially always)

Scenes are visual narratives — text would interrupt. Use `text_policy: none`.

### `text_policy: embedded` (very rare)

### 中文：text_policy embedded very rare

- 本节说明 `text_policy embedded very rare` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：`text_policy: embedded` (very rare)

Only when the scene includes a tiny diegetic text (a sign in the scene, a label on a book) — these often fail to render correctly. Usually better as `text_policy: none`.

---

## 4. Fewshot prompt snippets

### 中文：Fewshot 提示词 snippets

- 本节说明 `Fewshot 提示词 snippets` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Fewshot 提示词 snippets

**Snippet A — warm-scene + warm-earth personal story, text_policy: none, 1200×600**

> Atmospheric scene illustration with golden-hour cinematic lighting. The composition is a three-layer narrative: foreground left — a softly rendered simplified figure silhouette walking along a path with warm long shadows cast toward the right; middle ground — the warm path winds into a stylized hillside with a few suggested trees; background — atmospheric perspective creates pale warm distance, sky transitioning from amber `#D97706` at the horizon to soft cream `#FEF3C7` at the top. Lighting is warm golden-hour from the upper right. Foreground in deeper warm primary `#9A3412`; small accent gold `#D4AF37` highlights on sunlit surfaces. No hard outlines — forms emerge from light and shadow. Subtle film grain at 8% opacity. Composed as a 1200×600 hero scene with 10% inner padding. Simplified silhouette figure only — no realistic face. NO text or labels. Color values are rendering guidance only.

**Snippet B — corporate-photo + warm-earth team scene, text_policy: none, 1200×600**

> Editorial photography of a small modern team collaborating around a workspace. Foreground: three diverse, professionally attired adults engaged in genuine conversation over a laptop and notebooks on a wooden desk. Middle ground: a colleague visible in the background, slightly out of focus, working on their own laptop. Background: large window with soft natural light streaming in, contemporary office context. Soft window light from the left creates warm-amber highlights on subjects' faces and equipment; deeper warm shadows in the desk area. Color grading warm-editorial — primary terracotta `#9A3412` in shadow tones, secondary cream `#FEF3C7` in highlights, accent gold `#D4AF37` on wood and a small warm desk-lamp glow. Shallow depth of field — foreground subjects sharp, middle/background gently blurred. Composed as a 1200×600 hero scene with 10% inner padding. Diverse, professionally attired subjects rendered photorealistically. NO text. Color values are rendering guidance only.

---

## 5. Common failure modes

### 中文：Common failure 模式

- 本节说明 `Common failure 模式` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：5. Common failure modes

| Symptom | Cause | Fix |
|---|---|---|
| No foreground/midground/background depth | Layer rule omitted | "Three-layer composition: foreground, middle ground, background — atmospheric perspective creates depth" |
| Realistic faces in non-photo rendering | §5.2 omitted | Reaffirm "simplified silhouette figures only, no realistic faces" (exception: corporate-photo rendering) |
| Too many subjects competing | Narrative focus weak | "Clear narrative focus — one primary scene moment, supporting elements contextual not competing" |
| Mood inconsistent | Lighting direction not specified | "Single deliberate light source — direction explicit (e.g. upper right, warm golden-hour)" |
| Cluttered with detail | Scene too busy | "Atmospheric — scenes suggest rather than describe; restrained detail" |

---

## 6. When to switch away from scene

### 中文：When to switch away from 场景

- 本节说明 `When to switch away from 场景` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：When to switch away from 场景

- If pure atmosphere with no subject → `background`
- If single dominant subject without environment → `hero`
- If structured information with zones → `infographic`
- If conceptual relationships → `framework`
- If chronological progression → `timeline`
