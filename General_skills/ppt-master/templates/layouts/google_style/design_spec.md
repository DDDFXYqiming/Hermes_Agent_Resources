# Google Style Template - Design Specification

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


> Suitable for tech company annual reports, work summaries, technical sharing, data presentations, and similar scenarios.

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
| **Template Name** | google_style (Google Style Template)                    |
| **Use Cases**  | Annual work reports, technical sharing, project showcases, data-driven presentations |
| **Design Tone** | Professional, modern, clean and restrained, data-driven, generous whitespace |
| **Theme Mode** | Light theme (white/light gray background + Google brand color accents) |

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
| **Page Margins** | Left/Right 60px, Top 50px, Bottom 50px |
| **Safe Area**  | x: 60-1220, y: 50-670        |

---

## III. Color Scheme

### 中文：III 颜色 Scheme

- 本节说明 `III 颜色 Scheme` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：III 颜色 Scheme

### Google Brand Colors

### 中文：Google Brand 颜色

- 本节说明 `Google Brand 颜色` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Google Brand 颜色

| Role             | Value       | Notes                                |
| ---------------- | ----------- | ------------------------------------ |
| **Google Blue**  | `#4285F4`   | Primary titles, key data, main buttons |
| **Google Red**   | `#EA4335`   | Important emphasis, warning info     |
| **Google Yellow**| `#FBBC04`   | Auxiliary icons, secondary emphasis   |
| **Google Green** | `#34A853`   | Success indicators, positive data    |

### Professional Colors

### 中文：Professional 颜色

- 本节说明 `Professional 颜色` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Professional 颜色

| Role           | Value       | Usage                                |
| -------------- | ----------- | ------------------------------------ |
| **Deep Blue**  | `#1A237E`   | Titles, core text, dark emphasis     |
| **Deep Blue Gradient Start** | `#1A73E8` | Gradient title start point  |
| **Deep Blue Gradient End** | `#0D47A1` | Gradient title end point      |
| **Main Background White** | `#FFFFFF` | Page main background           |
| **Light Gray Background** | `#F8F9FA` | Card inner background, auxiliary areas |
| **Light Gray Border** | `#E8EAED` | Dividers, borders, grid lines     |

### Text Colors

### 中文：Text 颜色

- 本节说明 `Text 颜色` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Text 颜色

| Role           | Value       | Usage                                |
| -------------- | ----------- | ------------------------------------ |
| **Primary Text** | `#1A237E` | Titles, important text               |
| **Body Text**  | `#5F6368`   | Body content, descriptions           |
| **Secondary Text** | `#9AA0A6` | Annotations, page numbers, tips    |
| **White Text** | `#FFFFFF`   | Text on dark backgrounds             |

### Chart Colors (use in order)

### 中文：图表 颜色 use in order

- 本节说明 `图表 颜色 use in order` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：图表 颜色 use in order

| Order | Value       | Notes          |
| ----- | ----------- | -------------- |
| 1     | `#4285F4`   | Google Blue    |
| 2     | `#34A853`   | Google Green   |
| 3     | `#FBBC04`   | Google Yellow  |
| 4     | `#EA4335`   | Google Red     |

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

**Font Stack**: `Arial, "Microsoft YaHei", sans-serif`

> Uses PowerPoint-safe cross-platform fonts by default. Roboto may be used only when the target environment explicitly installs or embeds it.

### Font Size Hierarchy

### 中文：Font Size Hierarchy

- 本节说明 `Font Size Hierarchy` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：字体 Size Hierarchy

| Level  | Usage                | Size   | Weight      |
| ------ | -------------------- | ------ | ----------- |
| H1     | Cover main title     | 52px   | 700 (Bold)  |
| H2     | Page main title      | 46px   | 700 (Bold)  |
| H3     | Module/section title | 28px   | 600         |
| H4     | Card title/subtitle  | 24px   | 600         |
| P      | Body content         | 20px   | 400         |
| Data   | Large data numbers   | 56px   | 700 (Bold)  |
| Label  | Data labels/descriptions | 16px | 500        |
| Sub    | Auxiliary text/page number | 14px | 400       |

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

| Area               | Position/Height | Description                            |
| ------------------ | --------------- | -------------------------------------- |
| **Top Decorative Bar** | y=0, h=6px  | Four-color gradient bar, spanning full width |
| **Title Area**     | y=50, h=60px    | Page title + title underline           |
| **Content Area**   | y=130, h=500px  | Main content area                      |
| **Footer**         | y=660, h=60px   | Four-color dot decoration + optional page number |

### Signature Design Elements

### 中文：Signature 设计 Elements

- 本节说明 `Signature 设计 Elements` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Signature 设计 Elements

#### 1. Four-Color Gradient Top Bar

### 中文：Four-Color 渐变 Top Bar

- 本节说明 `Four-Color 渐变 Top Bar` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Four-Color 渐变 Top Bar
```
linearGradient: #4285F4 → #EA4335 → #FBBC04 → #34A853
height: 6px, width: 100%
```

#### 2. Title Underline (Four-Color Segments)

### 中文：Title Underline Four-Color Segments

- 本节说明 `Title Underline Four-Color Segments` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：2. Title Underline (Four-Color Segments)
```
Blue: 150px → Red: 70px → Yellow: 70px → Green: 170px
stroke-width: 4px, y: 20px below title
```

#### 3. KPI Data Card

### 中文：关键指标 Data Card

- 本节说明 `关键指标 Data Card` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：3. KPI Data Card
```
Size: 280×140px
Border radius: 16px
Border: 3px, using corresponding brand color
Shadow: Subtle shadow for depth
```

#### 4. Four-Color Dot Decoration

### 中文：Four-Color Dot Decoration

- 本节说明 `Four-Color Dot Decoration` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：4. Four-Color Dot Decoration
```
Used in footer or as dividers
radius: 6-14px (varies)
spacing: 30-50px
```

#### 5. Left Four-Color Vertical Bar

### 中文：Left Four-Color Vertical Bar

- 本节说明 `Left Four-Color Vertical Bar` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：5. Left Four-Color Vertical Bar
```
Cover page exclusive
width: 10px, 4 segments, 180px each
Color order: Blue → Red → Yellow → Green
```

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
- Light gradient background (white to light blue/light green)（以上为中文意译，具体细节以英文原文为准）。
- Left four-color vertical bar decoration（以上为中文意译，具体细节以英文原文为准）。
- Centered rounded white content card (with subtle shadow)（以上为中文意译，具体细节以英文原文为准）。
- Gradient main title + subtitle（以上为中文意译，具体细节以英文原文为准）。
- Gradient main title + subtitle
- Four-color segmented divider line
- Speaker info (name, title, date)
- Bottom four-color dot decoration

### 2. Table of Contents Page (02_toc.svg)

### 中文：表格 of Contents Page toc svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- White background + top four-color gradient bar（以上为中文意译，具体细节以英文原文为准）。
- Page title + blue underline（以上为中文意译，具体细节以英文原文为准）。
- Chapter list (left brand-color dots + numbers + titles)（以上为中文意译，具体细节以英文原文为准）。
- Optional: right-side decorative graphics or data stats（以上为中文意译，具体细节以英文原文为准）。
- Optional: right-side decorative graphics or data stats

### 3. Chapter Page (02_chapter.svg)

### 中文：Chapter Page chapter svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Dark gradient background (deep blue to darker blue)（以上为中文意译，具体细节以英文原文为准）。
- Large chapter number (gradient or white)（以上为中文意译，具体细节以英文原文为准）。
- Chapter title (white, large font)（以上为中文意译，具体细节以英文原文为准）。
- English subtitle (white, semi-transparent)（以上为中文意译，具体细节以英文原文为准）。
- English subtitle (white, semi-transparent)
- Four-color decorative elements

### 4. Content Page (03_content.svg)

### 中文：内容 Page 内容 svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- White background（以上为中文意译，具体细节以英文原文为准）。
- Top four-color gradient bar（以上为中文意译，具体细节以英文原文为准）。
- Page title + blue underline（以上为中文意译，具体细节以英文原文为准）。
- Flexible content area (supports multiple layouts)（以上为中文意译，具体细节以英文原文为准）。
- Flexible content area (supports multiple layouts)
- Bottom four-color dot decoration

### 5. Ending Page (04_ending.svg)

### 中文：Ending Page ending svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Light gradient background（以上为中文意译，具体细节以英文原文为准）。
- Centered rounded white content card（以上为中文意译，具体细节以英文原文为准）。
- Gradient "Thank You!" title（以上为中文意译，具体细节以英文原文为准）。
- Four-color divider line（以上为中文意译，具体细节以英文原文为准）。
- Four-color divider line
- Acknowledgment list (brand-color dots + names/items)
- Closing remarks + bottom four-color dots

---

## VII. Layout Patterns

### 中文：VII 版式 Patterns

- 本节说明 `VII 版式 Patterns` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：VII 版式 Patterns

| Pattern                | Use Cases                          |
| ---------------------- | ---------------------------------- |
| **Centered Card**      | Cover, ending, key points          |
| **Left Text Right Image** | Text description + chart/KPI area |
| **KPI Grid (2×2/2×3)** | Data overview, key metrics display |
| **Three-Column Cards** | Project lists, feature introductions |
| **Four Quadrants**     | Category display, SWOT analysis    |
| **Top-Bottom Split**   | Two related topics side by side    |
| **Timeline**           | Development history, roadmap       |
| **Dashboard Style**    | Multi-metric data dashboard        |

---

## VIII. Spacing Guidelines

### 中文：VIII Spacing 指南

- 本节说明 `VIII Spacing 指南` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：VIII 间距 指南

| Element              | Value    |
| -------------------- | -------- |
| Page margins         | 60px     |
| Title-to-content gap | 30-40px  |
| Module gap           | 60-80px  |
| Card gap             | 20-24px  |
| Card padding         | 20px     |
| Card border radius   | 16px     |
| Icon-to-text gap     | 15px     |

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
4. Use `fill-opacity` / `stroke-opacity` for transparency
5. Define gradients using `<linearGradient>` within `<defs>`

### Prohibited Elements

### 中文：Prohibited Elements

- 本节说明 `Prohibited Elements` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Prohibited Elements

The following SVG features are prohibited (not PPT-compatible):

- `mask`; `clipPath` is allowed only on `<image>` under `shared-standards.md` §1.2
- `<style>` tag, `class` attribute
- `foreignObject`
- `textPath`
- `animate*` animation elements
- `script`
- `rgba()` color format (use HEX + opacity instead)

> `marker-start` / `marker-end` are conditionally allowed — see `shared-standards.md` §1.1 (marker must be in `<defs>`, `orient="auto"`, shape = triangle / diamond / oval). The converter maps them to native DrawingML arrow heads.

### Shadow Implementation

### 中文：Shadow Implementation

- 本节说明 `Shadow Implementation` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：阴影 Implementation

Since `filter` may affect PPT compatibility:
- Use subtle border color variations to simulate shadows
- Or accept that `filter` may be ignored in older PPT versions, though it works well in newer versions

---

## X. Placeholder Specification

### 中文：Placeholder 规范

- 本节说明 `Placeholder 规范` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Placeholder 规范

Templates use `{{PLACEHOLDER}}` format placeholders:

| Placeholder            | Description              |
| ---------------------- | ------------------------ |
| `{{TITLE}}`            | Main title               |
| `{{SUBTITLE}}`         | Subtitle/department info |
| `{{SPEAKER_NAME}}`     | Speaker name             |
| `{{SPEAKER_TITLE}}`    | Speaker title/position   |
| `{{DATE}}`             | Date                     |
| `{{PAGE_TITLE}}`       | Page title               |
| `{{CHAPTER_NUM}}`      | Chapter number           |
| `{{CHAPTER_TITLE}}`    | Chapter title            |
| `{{CHAPTER_TITLE_EN}}` | Chapter English subtitle |
| `{{PAGE_NUM}}`         | Page number              |
| `{{CONTENT_AREA}}`     | Content area placeholder |
| `{{TOC_ITEM_N_TITLE}}` | TOC item title           |
| `{{THANK_YOU}}`        | Thank-you message        |
| `{{CONTACT_INFO}}`     | Primary contact info     |
| `{{ENDING_SUBTITLE}}`  | Ending subtitle          |

---

## XI. Color Application Examples

### 中文：XI 颜色 Application 示例

- 本节说明 `XI 颜色 Application 示例` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：XI 颜色 Application 示例

### KPI Card Color Rules

### 中文：关键指标 Card 颜色 规则

- 本节说明 `关键指标 Card 颜色 规则` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：KPI Card 颜色 规则

| Card Order | Border Color | Number Color | Applicable Content |
| ---------- | ------------ | ------------ | ------------------ |
| 1st        | `#4285F4`    | `#4285F4`    | Core projects/main metrics |
| 2nd        | `#34A853`    | `#34A853`    | Cost/efficiency metrics |
| 3rd        | `#EA4335`    | `#EA4335`    | Reliability/risk   |
| 4th        | `#FBBC04`    | `#FBBC04`    | Performance/growth |

### List Item Colors

### 中文：List Item 颜色

- 本节说明 `List Item 颜色` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：List Item 颜色

- Use the four brand colors in rotation for list bullet colors
- Keep text in a consistent deep blue `#1A237E`

---

## XII. Usage Instructions

### 中文：XII 使用方法 Instructions

- 本节说明 `XII 使用方法 Instructions` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：XII 使用方法 Instructions

1. Copy the template to the project directory `templates/`
2. Select the appropriate page type based on content needs
3. Use placeholders to mark content that needs replacement
4. Strictly follow the Google brand four-color scheme
5. Maintain generous whitespace to highlight key information
6. Data-driven: use large numbers + small labels to display KPIs

---

_This specification is based on Google Material Design principles, adapted for PPT Master project requirements_
