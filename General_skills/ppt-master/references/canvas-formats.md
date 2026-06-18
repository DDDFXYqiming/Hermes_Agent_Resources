# Canvas Format Specification

<!-- zh-main-begin -->

## 中文主体说明：Hermes_Agent_Resources 参考资料：canvas formats

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


> See shared-standards.md for SVG basic rules.

## Format Quick Reference

### 中文：Format Quick 参考

- 本节说明 `Format Quick 参考` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Format Quick 参考

| Format | viewBox | Ratio | Use Case |
|--------|---------|-------|----------|
| PPT 16:9 | `0 0 1280 720` | 16:9 | Business presentations, meetings |
| PPT 4:3 | `0 0 1024 768` | 4:3 | Traditional projectors, academic talks |
| Xiaohongshu (RED) | `0 0 1242 1660` | 3:4 | Image-text sharing, knowledge posts |
| WeChat Moments / IG | `0 0 1080 1080` | 1:1 | Square posters, brand showcases |
| Story / TikTok | `0 0 1080 1920` | 9:16 | Vertical stories, short video covers |
| WeChat Article Header | `0 0 900 383` | 2.35:1 | WeChat article cover images |
| Landscape Banner | `0 0 1920 1080` | 16:9 | Web banners, digital screens |
| Portrait Poster | `0 0 1080 1920` | 9:16 | Phone screens, elevator ads |
| A4 Print | `0 0 1240 1754` | 1:sqrt(2) | Print posters, flyers |

## Format Selection Decision Tree

### 中文：Format Selection 决策 Tree

- 本节说明 `Format Selection 决策 Tree` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Format Selection Decision Tree

```
Content purpose?
├── Presentation
│   ├── Modern devices → PPT 16:9 (1280x720)
│   └── Traditional devices → PPT 4:3 (1024x768)
├── Social sharing
│   ├── Xiaohongshu (RED) → 1242x1660
│   ├── WeChat Moments / IG → 1080x1080
│   └── Story / TikTok → 1080x1920
└── Marketing materials
    ├── WeChat Article Header → 900x383
    ├── Banner → 1920x1080
    └── Print → 1240x1754
```

## Layout Principles

### 中文：版式 原则

- 本节说明 `版式 原则` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：版式 原则

### Landscape (16:9, 4:3, 2.35:1)

### 中文：Landscape

- 本节说明 `Landscape` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Landscape (16:9, 4:3, 2.35:1)
- Visual flow: Z-pattern, left to right
- Margins: 40-80px
- Layouts: multi-column, left-right split, grid
- Card dimensions (16:9): single-row 530-600px, double-row 265-295px

### Portrait (3:4, 9:16)

### 中文：人像

- 本节说明 `人像` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Portrait (3:4, 9:16)
- Visual flow: top to bottom
- Margins: 60-120px
- Layouts: single-column, top-bottom split, card stacking
- Card dimensions (3:4): height 400-600px, gap 40-60px

### Square (1:1)

### 中文：Square

- 本节说明 `Square` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Square (1:1)
- Visual flow: center-radiating
- Margins: 60-100px
- Core area: ~800x800px

## Format-specific Design

### 中文：Format-specific 设计

- 本节说明 `Format-specific 设计` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Format-specific 设计

| Format | Title Area | Content Area | Special Notes |
|--------|-----------|--------------|---------------|
| PPT | 80-100px | Full width utilization | Page number bottom-right |
| Xiaohongshu (RED) | 180-240px (bold) | Generous top/bottom whitespace | Brand area at bottom 120-160px |
| WeChat Moments | 200-280px | Center 500-600px | QR code area at bottom 150-200px |
| Story | — | Middle 1500px | Top safe zone 120px, bottom 180px |
| WeChat Article Header | Center/left-aligned 48-72px | — | Image on right or as background |

## ViewBox Examples

### 中文：ViewBox 示例

- 本节说明 `ViewBox 示例` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：ViewBox 示例

```xml
<svg width="1280" height="720" viewBox="0 0 1280 720">   <!-- PPT 16:9 -->
<svg width="1242" height="1660" viewBox="0 0 1242 1660"> <!-- Xiaohongshu -->
<svg width="1080" height="1080" viewBox="0 0 1080 1080"> <!-- WeChat Moments -->
<svg width="1080" height="1920" viewBox="0 0 1080 1920"> <!-- Story -->
<svg width="900" height="383" viewBox="0 0 900 383">     <!-- WeChat Article Header -->
```
