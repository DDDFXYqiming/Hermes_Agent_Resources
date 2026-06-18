# CATARC (中汽研) Modern Template - Design Specification (v3.0 Future Tech)

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


> Suitable for CATARC high-end launches, forward-looking technology presentations, international exchanges, and similar scenarios.
> **v3.0 Update**: Introduces a "Future Tech" design language with deep blue + neon cyan palette, emphasizing spatial depth and flowing light effects.

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
| **Template Name** | 中汽研_现代 (CATARC_Modern_Tech)                       |
| **Use Cases**  | Forward-looking technology showcases, strategic releases, high-end business reporting |
| **Design Tone** | **Futuristic, tech-forward, deep & refined**              |
| **Theme Mode** | Immersive dark cover/transition pages + clean light-gray content pages |

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
| **viewBox**    | `0 0 1280 720`               |
| **Page Margins** | Left/Right 80px, Top 100px, Bottom 60px |
| **Safe Area**  | x: 80-1200, y: 100-660       |

---

## III. Color Scheme

### 中文：III 颜色 Scheme

- 本节说明 `III 颜色 Scheme` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：III 颜色 Scheme

### Core Palette (Future Tech Palette)

### 中文：Core 配色 Future 科技 配色

- 本节说明 `Core 配色 Future 科技 配色` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：核心 配色 Future Tech 配色

| Role           | Color Value | Gradient (SVG defs)            | Notes                            |
| -------------- | ----------- | ------------------------------ | -------------------------------- |
| **Deep Night Sky** | `#001529` | `#001529` -> `#002B52`        | Cover/transition page main background |
| **Tech Blue**  | `#1890FF`  | `#1890FF` -> `#096DD9`         | Primary visual accent            |
| **Neon Cyan**  | `#00E5FF`  | `#00E5FF` -> `#00B5D8`         | Ultra-bright accent for highlights/data |
| **Polar Gray** | `#F7F9FC`  | N/A                            | Content page background (not pure white, easier on eyes) |
| **Dark Night** | `#1F2937`  | N/A                            | Body text                        |

### Text Colors

### 中文：Text 颜色

- 本节说明 `Text 颜色` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Text 颜色

| Role           | Color Value | Usage                  |
| -------------- | ----------- | ---------------------- |
| **Heading (Dark BG)** | `#FFFFFF` | Main title on dark backgrounds |
| **Heading (Light BG)** | `#001529` | Main title on light backgrounds |
| **Body Text**  | `#374151`  | Content page body text  |
| **Secondary Text** | `#6B7280` | Auxiliary descriptions  |
| **Decorative Text** | `#E5E7EB` | Very light watermark text |

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

**Primary Font Stack**: `Arial, "Microsoft YaHei", sans-serif`
*Use Arial for English and numbers by default. Roboto or DIN may be used only when the font is explicitly installed or embedded for the target environment.*

### Font Size Hierarchy

### 中文：Font Size Hierarchy

- 本节说明 `Font Size Hierarchy` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：字体 Size Hierarchy

| Level | Usage              | Size  | Weight  | Color      |
| ----- | ------------------ | ----- | ------- | ---------- |
| H1    | Cover main title   | 64px  | Bold    | #FFFFFF    |
| H2    | Page heading       | 36px  | Bold    | #001529    |
| H3    | Section title      | 24px  | Bold    | #1890FF    |
| P     | Body content       | 18px  | Regular | #374151    |
| Deco  | Decorative large numbers | 120px | Bold | Opacity 5% |

---

## V. Page Structure (Asymmetric Tech Layout)

### 中文：Page 结构 Asymmetric 科技 版式

- 本节说明 `Page 结构 Asymmetric 科技 版式` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：页面 结构 Asymmetric Tech 版式

### Common Navigation Bar (y=0 to 100)

### 中文：Common Navigation Bar to

- 本节说明 `Common Navigation Bar to` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Common Navigation Bar (y=0 to 100)

- **Asymmetric Design**: Title left-aligned with a geometric decorative bar on the left.
- **Logo**: Floating in the upper-right corner with a subtle glow effect.
- **Decoration**: Top area retains only a splash of bright color line on the right side, breaking visual balance.

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
- Visual Focus**: **Deep spatial depth**（以上为中文意译，具体细节以英文原文为准）。
- Background uses a deep blue radial gradient（以上为中文意译，具体细节以英文原文为准）。
- Hero Element**: Right side features abstract **"Luminous Flow"** or **"Digital Matrix"** graphics（以上为中文意译，具体细节以英文原文为准）。
- Title**: Bottom-left aligned, emphasizing bold typography with a neon-colored underline（以上为中文意译，具体细节以英文原文为准）。
### 2. Table of Contents (02_toc.svg)

### 中文：表格 of Contents toc svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Layout**: **Split Screen (left dark, right light)**（以上为中文意译，具体细节以英文原文为准）。
- Left Side**: Dark area containing "CONTENTS" and Logo（以上为中文意译，具体细节以英文原文为准）。
- Right Side**: Light area with TOC items（以上为中文意译，具体细节以英文原文为准）。
- Replaces cards with **"Timeline"** or **"Floating List"** style（以上为中文意译，具体细节以英文原文为准）。
- **Numbers**: Highlighted in neon cyan (`#00E5FF`).

### 3. Chapter Page (02_chapter.svg)

### 中文：Chapter Page chapter svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Background**: Dark background（以上为中文意译，具体细节以英文原文为准）。
- Special Effect**: Large outlined numbers in the background (Stroke Text)（以上为中文意译，具体细节以英文原文为准）。
- Dynamism**: Added tilted decorative lines to simulate a sense of speed（以上为中文意译，具体细节以英文原文为准）。
### 4. Content Page (03_content.svg)

### 中文：内容 Page 内容 svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Background**: Very light gray `#F7F9FC`（以上为中文意译，具体细节以英文原文为准）。
- Header**: Floating title bar for enhanced hierarchy（以上为中文意译，具体细节以英文原文为准）。
- Watermark**: Tech-styled geometric watermark in the lower-right corner（以上为中文意译，具体细节以英文原文为准）。
### 5. Ending Page (04_ending.svg)

### 中文：Ending Page ending svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Background**: Echoes the cover（以上为中文意译，具体细节以英文原文为准）。
- Center**: Minimalist "Thank You" with surrounding halo ring decoration（以上为中文意译，具体细节以英文原文为准）。
---

## VII. Layout Patterns (Recommended)

### 中文：VII 版式 Patterns Recommended

- 本节说明 `VII 版式 Patterns Recommended` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：VII 版式 Patterns Recommended

### 1. Floating Timeline

### 中文：Floating 时间线

- 本节说明 `Floating 时间线` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：1. Floating Timeline
- Uses right-side space for time or process display.
- Nodes feature a neon glowing effect.

### 2. HUD Display

### 中文：HUD Display

- 本节说明 `HUD Display` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：2. HUD Display
- Simulates a heads-up display style using thin wireframes and highlighted numbers for key KPIs.

### 3. Asymmetric Contrast

### 中文：Asymmetric Contrast

- 本节说明 `Asymmetric Contrast` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：3. Asymmetric Contrast
- Leverages the page's asymmetric structure to create dynamic image-text layouts.

---

## VIII. Spacing Guidelines

### 中文：VIII Spacing 指南

- 本节说明 `VIII Spacing 指南` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：VIII 间距 指南

| Property       | Value | Description              |
| -------------- | ----- | ------------------------ |
| **Base Unit**  | 8px   | Tech designs typically use an 8px grid |
| **Module Gap** | 48px  | Extra spacious for a modern feel |
| **Line Height** | 1.6  | Increased line height for readability |

---

## IX. SVG Technical Constraints

### 中文：IX SVG Technical 限制

- 本节说明 `IX SVG Technical 限制` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：IX SVG Technical 限制

### Mandatory Rules

### 中文：Mandatory 规则

- 本节说明 `Mandatory 规则` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Mandatory 规则

1. **Blend Modes**: Avoid `mix-blend-mode` wherever possible; use `opacity` as a substitute.
2. **Gradients**: Leverage angled `linearGradient` (e.g., `x1="0%" y1="0%" x2="100%" y2="50%"`) to create light and shadow effects.
3. **Strokes**: Use thin `stroke-width="1"` with low transparency `stroke-opacity="0.2"` to simulate glass edges.

---

## X. Placeholder Specification

### 中文：Placeholder 规范

- 本节说明 `Placeholder 规范` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Placeholder 规范

| Placeholder        | Description           |
| ------------------ | --------------------- |
| `{{TITLE}}`        | Presentation main title |
| `{{SUBTITLE}}`     | Subtitle              |
| `{{AUTHOR}}`       | Presenting organization |
| `{{PRESENTER}}`    | Presenter             |
| `{{DATE}}`         | Date                  |
| `{{CHAPTER_NUM}}`  | Chapter number (01, 02) |
| `{{PAGE_TITLE}}`   | Content page title    |
| `{{STAT_1}}`       | Statistical data 1    |
| `{{TOC_ITEM_N_TITLE}}` | TOC item title    |
| `{{TOC_ITEM_N_DESC}}`  | TOC item description |
| `{{THANK_YOU}}`    | Thank-you message     |
| `{{CONTACT_INFO}}` | Contact information   |

---

## XI. Usage Notes (Recommended)

### 中文：XI 使用方法 说明 Recommended

- 本节说明 `XI 使用方法 说明 Recommended` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：XI 使用方法 说明 Recommended

1. **Light & Shadow Effects**: All light and shadow effects are achieved via SVG gradients, with no dependency on external images.
2. **Fonts**: Use Arial for numbers by default. Roboto or DIN may be used only with an explicit font-install or font-embedding requirement.
3. **Backgrounds**: Dark backgrounds look excellent on projectors, but ensure the ambient lighting is as dim as possible.
