# Academic Defense Template - Design Specification

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


> Suitable for academic thesis defense, research presentations, graduation project showcases, and similar scenarios.

---

## I. Template Overview

### 中文：模板 概览

- 本节说明 `模板 概览` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：模板 概览

| Property       | Description                                            |
| -------------- | ------------------------------------------------------ |
| **Template Name** | academic_defense                                    |
| **Use Cases**  | Thesis defense, academic presentations, research progress reports, grant applications |
| **Design Tone** | Professional, rigorous, research-oriented, clear hierarchy |
| **Theme Mode** | Light theme (white background + dark blue title bar)   |

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
| **Page Margins** | Left/Right 40px, Top 0px, Bottom 35px |
| **Safe Area**  | x: 40-1240, y: 70-665        |

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

| Role           | Value       | Notes                            |
| -------------- | ----------- | -------------------------------- |
| **Primary Dark Blue** | `#003366` | Header background, section titles, main headings |
| **Accent Blue** | `#0066CC` | Card borders, icons, secondary decorations |
| **Accent Red** | `#CC0000`  | Key highlights, keyword emphasis, left decorative bar |
| **Light Blue-Gray** | `#E8F4FC` | Key message bar background, card inner sections |
| **Background White** | `#FFFFFF` | Page main background           |

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
| **White Text** | `#FFFFFF`   | Text on dark backgrounds |
| **Primary Text** | `#333333` | Body content           |
| **Secondary Text** | `#666666` | Descriptions, annotations |
| **Muted Gray** | `#999999`  | Footer, auxiliary info |

### Neutral Colors

### 中文：Neutral 颜色

- 本节说明 `Neutral 颜色` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Neutral 颜色

| Role           | Value       | Usage                  |
| -------------- | ----------- | ---------------------- |
| **Card Gray**  | `#F5F7FA`   | Card inner background, info blocks |
| **Border Gray** | `#D0D7E0`  | Card borders, dividers |

### Functional Colors

### 中文：Functional 颜色

- 本节说明 `Functional 颜色` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Functional 颜色

| Usage      | Value       | Description    |
| ---------- | ----------- | -------------- |
| **Success** | `#28A745`  | Positive indicators |
| **Warning** | `#FFA500`  | Alerts         |
| **Info**   | `#17A2B8`   | Information tips |

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

**Font Stack**: `"Microsoft YaHei", "微软雅黑", Arial, sans-serif`

### Font Size Hierarchy

### 中文：Font Size Hierarchy

- 本节说明 `Font Size Hierarchy` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：字体 Size Hierarchy

| Level | Usage            | Size | Weight  |
| ----- | ---------------- | ---- | ------- |
| H1    | Cover main title | 56px | Bold    |
| H2    | Page title       | 28px | Bold    |
| H3    | Section title    | 56px | Bold    |
| H4    | Card title       | 24px | Bold    |
| P     | Body content     | 18px | Regular |
| High  | Highlighted data | 36px | Bold    |
| Sub   | Notes/sources    | 14px | Regular |
| XS    | Page number/copyright | 12px | Regular |

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

| Area           | Position/Height | Description                            |
| -------------- | --------------- | -------------------------------------- |
| **Header**     | y=0, h=70px     | Dark blue background + red left bar + page title |
| **Key Message Bar** | y=70, h=50px | Core message/summary area (light blue-gray background) |
| **Content Area** | y=135, h=515px | Main content area                    |
| **Footer**     | y=665, h=55px   | Data source, section name, page number |

### Decorative Elements

### 中文：Decorative Elements

- 本节说明 `Decorative Elements` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Decorative Elements

- **Left Red Bar**: Red (`#CC0000`), width 6px, used for header and card decoration
- **Blue Border**: Accent blue (`#0066CC`), used for card borders
- **Decorative Divider**: Blue (`#0066CC`), paired with decorative dots

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
- White background（以上为中文意译，具体细节以英文原文为准）。
- Dark blue top bar + red left vertical bar decoration（以上为中文意译，具体细节以英文原文为准）。
- Top-right Logo placeholder area（以上为中文意译，具体细节以英文原文为准）。
- Centered main title + subtitle（以上为中文意译，具体细节以英文原文为准）。
- Centered main title + subtitle
- Decorative divider line (blue + dots)
- Presenter info area (name, advisor, institution)
- Bottom gray info area (date)

### 2. Table of Contents Page (02_toc.svg)

### 中文：表格 of Contents Page toc svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- White background（以上为中文意译，具体细节以英文原文为准）。
- Standard header (dark blue + red vertical bar)（以上为中文意译，具体细节以英文原文为准）。
- Card-style TOC item layout (2 columns)（以上为中文意译，具体细节以英文原文为准）。
- Light blue-gray background cards + left colored vertical bar（以上为中文意译，具体细节以英文原文为准）。
- Light blue-gray background cards + left colored vertical bar
- Optional items use dashed borders

### 3. Chapter Page (02_chapter.svg)

### 中文：Chapter Page chapter svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Dark blue full-screen background (`#003366`)（以上为中文意译，具体细节以英文原文为准）。
- Right-side geometric decorations（以上为中文意译，具体细节以英文原文为准）。
- Left red vertical bar decoration（以上为中文意译，具体细节以英文原文为准）。
- Large semi-transparent background number（以上为中文意译，具体细节以英文原文为准）。
- Large semi-transparent background number
- Prominent white chapter title
- Light blue-gray chapter description
- Red decorative horizontal line

### 4. Content Page (03_content.svg)

### 中文：内容 Page 内容 svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- White background（以上为中文意译，具体细节以英文原文为准）。
- Standard header (dark blue + red vertical bar)（以上为中文意译，具体细节以英文原文为准）。
- Key message bar (light blue-gray background + blue left vertical bar)（以上为中文意译，具体细节以英文原文为准）。
- Flexible content area（以上为中文意译，具体细节以英文原文为准）。
- Flexible content area
- Footer: data source, section name, page number

### 5. Ending Page (04_ending.svg)

### 中文：Ending Page ending svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- White background（以上为中文意译，具体细节以英文原文为准）。
- Dark blue top bar（以上为中文意译，具体细节以英文原文为准）。
- Centered thank-you message（以上为中文意译，具体细节以英文原文为准）。
- Tagline（以上为中文意译，具体细节以英文原文为准）。
- Tagline
- Decorative divider line
- Contact info card (gray background)
- Bottom gray area (copyright, page number)

---

## VII. Layout Patterns

### 中文：VII 版式 Patterns

- 本节说明 `VII 版式 Patterns` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：VII 版式 Patterns

| Pattern            | Use Cases                      |
| ------------------ | ------------------------------ |
| **Single Column Centered** | Cover, ending, key points |
| **Two-Column Cards** | Table of contents            |
| **Left-Right Split (5:5)** | Comparison display      |
| **Left-Right Split (4:6)** | Image-text mixed layout |
| **Card Grid**      | Research content list           |
| **Timeline**       | Research progress               |
| **Table**          | Data comparison, experiment results |

---

## VIII. Spacing Guidelines

### 中文：VIII Spacing 指南

- 本节说明 `VIII Spacing 指南` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：VIII 间距 指南

| Element            | Value  |
| ------------------ | ------ |
| Card gap           | 20px   |
| Content block gap  | 24px   |
| Card padding       | 20px   |
| Card border radius | 8px    |
| Icon-to-text gap   | 12px   |

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

1. viewBox: `0 0 1280 720`
2. Use `<rect>` elements for backgrounds
3. Use `<tspan>` for text wrapping (no `<foreignObject>`)
4. Use `fill-opacity` / `stroke-opacity` for transparency; no `rgba()`
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
- Use overlay layers for image transparency
- Inline styles only; no external CSS or `@font-face`

---

## X. Placeholder Specification

### 中文：Placeholder 规范

- 本节说明 `Placeholder 规范` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Placeholder 规范

Templates use `{{PLACEHOLDER}}` format placeholders. Common placeholders:

| Placeholder        | Description        |
| ------------------ | ------------------ |
| `{{TITLE}}`        | Thesis/project main title |
| `{{SUBTITLE}}`     | Subtitle           |
| `{{AUTHOR}}`       | Presenter name     |
| `{{ADVISOR}}`      | Advisor            |
| `{{INSTITUTION}}`  | University/institution |
| `{{DATE}}`         | Defense date       |
| `{{PAGE_TITLE}}`   | Page title         |
| `{{SECTION_NUM}}`  | Section number     |
| `{{CHAPTER_NUM}}`  | Chapter number (large) |
| `{{CHAPTER_TITLE}}`| Chapter title      |
| `{{CHAPTER_DESC}}` | Chapter description |
| `{{KEY_MESSAGE}}`  | Key message        |
| `{{PAGE_NUM}}`     | Page number        |
| `{{SOURCE}}`       | Data source        |
| `{{SECTION_NAME}}` | Section name (footer) |
| `{{TOC_ITEM_N_TITLE}}` | TOC item title (N=1..n) |
| `{{TOC_ITEM_N_DESC}}` | TOC item description (N=1..n) |
| `{{THANK_YOU}}`    | Thank-you message  |
| `{{ENDING_SUBTITLE}}` | Ending subtitle/tagline |
| `{{CONTACT_INFO}}` | Contact information |
| `{{EMAIL}}`        | Email address      |
| `{{COPYRIGHT}}`    | Copyright info     |
| `{{LOGO}}`         | Logo text          |

---

## XI. Component Specifications

### 中文：XI 组件 规范

- 本节说明 `XI 组件 规范` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：XI 组件 规范

### 1. Tag

### 中文：Tag

- 本节说明 `Tag` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：1. Tag

```xml
<!-- Blue background white text tag -->
<rect x="40" y="150" width="80" height="28" fill="#0066CC" rx="4"/>
<text x="80" y="170" text-anchor="middle" fill="#FFFFFF" font-size="14" font-weight="bold">内容详解</text>

<!-- Red background white text tag (emphasis) -->
<rect x="40" y="150" width="80" height="28" fill="#CC0000" rx="4"/>
<text x="80" y="170" text-anchor="middle" fill="#FFFFFF" font-size="14" font-weight="bold">核心目标</text>
```

### 2. Flow Arrow

### 中文：Flow Arrow

- 本节说明 `Flow Arrow` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：2. Flow Arrow

```xml
<!-- Horizontal flow arrow -->
<line x1="200" y1="300" x2="350" y2="300" stroke="#0066CC" stroke-width="2"/>
<polygon points="350,295 360,300 350,305" fill="#0066CC"/>
```

### 3. Data Highlight Box

### 中文：Data Highlight Box

- 本节说明 `Data Highlight Box` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Data 高光 Box

```xml
<!-- Key data block -->
<rect x="40" y="400" width="200" height="80" fill="#FFFFFF" stroke="#CC0000" stroke-width="2" rx="8"/>
<text x="140" y="445" text-anchor="middle" fill="#CC0000" font-size="24" font-weight="bold">30%</text>
<text x="140" y="470" text-anchor="middle" fill="#666666" font-size="12">关键指标</text>
```

---

## XII. Usage Instructions

### 中文：XII 使用方法 Instructions

- 本节说明 `XII 使用方法 Instructions` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：XII 使用方法 Instructions

1. Copy the template to the project directory
2. Select the appropriate page template based on defense content needs
3. Use placeholders to mark content that needs replacement
4. Ensure presenter info and advisor info are complete
5. Generate the final SVG through the Executor role
