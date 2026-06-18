# Anthropic Style Template - Design Specification

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


> Suitable for AI/LLM tech talks, developer conferences, technical training, product launches, and similar scenarios.

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
| **Template Name** | anthropic (Anthropic Style Template)                |
| **Use Cases**  | AI tech talks, developer conferences, technical training, product launches |
| **Design Tone** | Tech-forward, professional, modern, conclusion-first |
| **Theme Mode** | Mixed theme (dark cover/chapter + light content pages) |

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
| **Safe Margins** | 60px (left/right), 50px (top/bottom) |
| **Content Area** | x: 60-1220, y: 100-670     |
| **Title Area** | y: 50-100                     |
| **Grid Base**  | 40px                          |

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

| Role             | Value       | Notes                            |
| ---------------- | ----------- | -------------------------------- |
| **Anthropic Orange** | `#D97757` | Brand identity, title emphasis, key data |
| **Deep Space Gray** | `#1A1A2E` | Cover background, body text, chart base |
| **Tech Blue**    | `#4A90D9`   | Flowcharts, links, interactive elements |
| **Mint Green**   | `#10B981`   | Recommended options, positive indicators, success states |
| **Coral Red**    | `#EF4444`   | Risks, cautions, warnings        |

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
| **Cloud White** | `#F8FAFC`  | Card background        |
| **Border Gray** | `#E2E8F0`  | Card borders, dividers |
| **Slate Gray** | `#64748B`   | Secondary text, chart labels |
| **Pure White** | `#FFFFFF`   | Page background        |

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

**Font Stack**: `Arial, "Helvetica Neue", "Segoe UI", sans-serif`

### Font Size Hierarchy

### 中文：Font Size Hierarchy

- 本节说明 `Font Size Hierarchy` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：字体 Size Hierarchy

| Level    | Usage            | Size   | Weight  |
| -------- | ---------------- | ------ | ------- |
| H1       | Cover main title | 56px   | Bold    |
| H2       | Page title       | 32-36px| Bold    |
| H3       | Subtitle/section | 24-28px| Semibold|
| H4       | Card title       | 20-22px| Bold    |
| P        | Body content     | 16-18px| Regular |
| Data     | Highlighted data | 40-48px| Bold    |
| Label    | Label text       | 14px   | 500     |
| Sub      | Chart labels/footnotes | 12-14px | Regular |

---

## V. Core Design Principles

### 中文：Core 设计 原则

- 本节说明 `Core 设计 原则` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：核心 设计 原则

### Top-Tier Consulting Style

### 中文：Top-Tier Consulting 风格

- 本节说明 `Top-Tier Consulting 风格` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Top-Tier Consulting 风格

1. **Conclusion First (Pyramid Principle)**: Each page title is the core takeaway
2. **Data Contextualization**: Comparisons, trends, benchmarks — never present data in isolation
3. **SCQA Framework**: Situation → Complication → Question → Answer
4. **MECE Principle**: Mutually Exclusive, Collectively Exhaustive
5. **Professional Whitespace**: Content ratio < 65%, let information "breathe"

---

## VI. Page Structure

### 中文：VI Page 结构

- 本节说明 `VI Page 结构` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：VI 页面 结构

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
| **Top**        | y=0, h=6-8px    | Anthropic Orange decorative bar        |
| **Label**      | y=50-70         | Page type label (uppercase, orange)    |
| **Title Area** | y=80-140        | Page title (core takeaway)             |
| **Content Area** | y=160-620     | Main content area                      |
| **Footer**     | y=680           | Page number (centered)                 |

### Decorative Elements

### 中文：Decorative Elements

- 本节说明 `Decorative Elements` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Decorative Elements

- **Top Orange Bar**: Anthropic Orange (`#D97757`), height 6px
- **Left Gradient Bar**: Orange gradient (`#D97757` → `#E8956F`)
- **Card Border**: Light gray (`#E2E8F0`)
- **Card Shadow**: Soft shadow effect
- **Grid Decoration Lines**: White low-opacity grid on dark covers

---

## VII. Page Types

### 中文：VII Page 类型

- 本节说明 `VII Page 类型` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：VII 页面 类型

### 1. Cover Page (01_cover.svg)

### 中文：Cover Page cover svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Dark gradient background (`#1A1A2E` → `#16213E` → `#0F0F1A`)（以上为中文意译，具体细节以英文原文为准）。
- Grid decoration lines (white, 3% opacity)（以上为中文意译，具体细节以英文原文为准）。
- Orange and blue glow effects（以上为中文意译，具体细节以英文原文为准）。
- Neural network-style connection lines and nodes（以上为中文意译，具体细节以英文原文为准）。
- Neural network-style connection lines and nodes
- Centered main title (white) + subtitle
- Orange decorative short line
- Bottom date and source info

### 2. Table of Contents Page (02_toc.svg)

### 中文：表格 of Contents Page toc svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- White background（以上为中文意译，具体细节以英文原文为准）。
- Left orange gradient decorative bar (8px)（以上为中文意译，具体细节以英文原文为准）。
- Orange circular numbers + chapter titles（以上为中文意译，具体细节以英文原文为准）。
- Right-side complexity progression illustration（以上为中文意译，具体细节以英文原文为准）。
- Right-side complexity progression illustration

### 3. Chapter Page (02_chapter.svg)

### 中文：Chapter Page chapter svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Dark gradient background（以上为中文意译，具体细节以英文原文为准）。
- Grid decoration（以上为中文意译，具体细节以英文原文为准）。
- Centered large chapter title（以上为中文意译，具体细节以英文原文为准）。
- Orange decorative line（以上为中文意译，具体细节以英文原文为准）。
- Orange decorative line

### 4. Content Page (03_content.svg)

### 中文：内容 Page 内容 svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- White background（以上为中文意译，具体细节以英文原文为准）。
- Top orange decorative bar（以上为中文意译，具体细节以英文原文为准）。
- Page type label (orange uppercase)（以上为中文意译，具体细节以英文原文为准）。
- Title as core takeaway（以上为中文意译，具体细节以英文原文为准）。
- Title as core takeaway
- Three-column card layout (colored top borders)
- Footer with centered page number

### 5. Ending Page (04_ending.svg)

### 中文：Ending Page ending svg

- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。
- Dark gradient background（以上为中文意译，具体细节以英文原文为准）。
- Neural network decoration（以上为中文意译，具体细节以英文原文为准）。
- Centered thank-you message（以上为中文意译，具体细节以英文原文为准）。
- Contact information（以上为中文意译，具体细节以英文原文为准）。
- Contact information

---

## VIII. Common Components

### 中文：VIII Common 组件

- 本节说明 `VIII Common 组件` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：VIII Common 组件

### Card Style

### 中文：Card 风格

- 本节说明 `Card 风格` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Card 风格

```xml
<!-- Card with shadow -->
<g filter="url(#cardShadow)">
    <path fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"
          d="M72,180 H408 A12,12 0 0 1 420,192 V588 A12,12 0 0 1 408,600 H72 A12,12 0 0 1 60,588 V192 A12,12 0 0 1 72,180 Z"/>
</g>
<!-- Top colored decorative bar -->
<rect x="60" y="180" width="360" height="6" fill="#10B981"/>
```

### Circular Number

### 中文：Circular Number

- 本节说明 `Circular Number` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Circular Number

```xml
<circle cx="90" cy="200" r="24" fill="#D97757"/>
<text x="90" y="207" font-size="18" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1</text>
```

### Icon Background Circle

### 中文：图标 背景 Circle

- 本节说明 `图标 背景 Circle` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：图标 背景 Circle

```xml
<circle cx="130" cy="250" r="35" fill="#10B981" fill-opacity="0.1"/>
```

---

## IX. Spacing Guidelines

### 中文：IX Spacing 指南

- 本节说明 `IX Spacing 指南` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：IX 间距 指南

| Element          | Value  |
| ---------------- | ------ |
| Safe margin      | 60px   |
| Card gap         | 30-40px|
| Card border radius | 8-12px |
| Card padding     | 30px   |
| Grid base        | 40px   |

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
3. Use `<tspan>` for text wrapping (**strictly no** `<foreignObject>`)
4. Use `fill-opacity` / `stroke-opacity` for transparency
5. Prohibited: `mask`, `<style>`, `class`, `foreignObject`. `clipPath` is allowed only on `<image>` under `shared-standards.md` §1.2
6. Prohibited: `textPath`, `animate*`, `script`
7. Define gradients using `<defs>`

### PPT Compatibility Rules

### 中文：PPT Compatibility 规则

- 本节说明 `PPT Compatibility 规则` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：PPT Compatibility 规则

- No `<g opacity="...">` (group opacity)
- Inline styles only

---

## XI. Placeholder Specification

### 中文：XI Placeholder 规范

- 本节说明 `XI Placeholder 规范` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：XI Placeholder 规范

| Placeholder        | Description        |
| ------------------ | ------------------ |
| `{{TITLE}}`        | Main title         |
| `{{SUBTITLE}}`     | Subtitle           |
| `{{COVER_QUOTE}}`  | Cover quote        |
| `{{SOURCE}}`       | Source info        |
| `{{DATE}}`         | Date               |
| `{{PAGE_TITLE}}`   | Page title (core takeaway) |
| `{{PAGE_LABEL}}`   | Page type label    |
| `{{CONTENT_AREA}}` | Flexible content anchor |
| `{{CHAPTER_NUM}}`  | Chapter number     |
| `{{CHAPTER_TITLE}}`| Chapter title      |
| `{{PAGE_NUM}}`     | Page number        |
| `{{TOTAL_PAGES}}`  | Total pages        |
| `{{TOC_ITEM_N_TITLE}}` | TOC item title |
| `{{TOC_ITEM_N_DESC}}`  | TOC item description |
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

1. Copy the template to the project directory
2. Select the appropriate page template based on content needs
3. **Title is the core takeaway** — ensure each page has a clear conclusion
4. Use three accent colors to differentiate content types (green = recommended, blue = process, orange = emphasis)
5. Generate the final SVG through the Executor role
