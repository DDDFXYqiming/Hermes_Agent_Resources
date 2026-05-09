# MarkItDown Skill

**DeepSeek Agent 自包含 Skill** — 将各类文件格式转换为 Markdown，供智能体消费。

> 基于 Microsoft [MarkItDown](https://github.com/microsoft/markitdown) 重写。
> 不依赖任何外部 LLM / API Key。图片描述由 DeepSeek Agent 自身的多模态能力处理。

---

## 激活条件

**当用户要求读取/分析/转换以下内容时，使用本 Skill：**

- 本地文件：`.pdf` `.docx` `.pptx` `.xlsx` `.xls` `.csv` `.html` `.epub` `.msg` `.ipynb` `.zip` `.jpg` `.png` `.wav` `.mp3`
- 远程 URL：YouTube 视频、Wikipedia 页面、RSS 订阅、网页
- 二进制流：从 HTTP 响应或 stdin 传入的任意支持格式

**不应使用本 Skill 的场景：**
- 用户要求直接输出原始文本（不需要转换）— 直接用 `read_file`
- 文件格式不在支持列表中 — 先告知用户，再尝试 `read_file` 读取原文

---

## 调用方式

### 模式 1：命令行（推荐，最可靠）

```bash
cd markitdown-skill && source .venv/bin/activate && python -m markitdown_skill <文件路径>
```

输出直接写到 stdout，智能体读取 stdout 即可获得 Markdown 文本。

### 模式 2：Python API（需要程序化控制时）

```python
from markitdown_skill import MarkItDown

md = MarkItDown()
result = md.convert("<文件路径>")
print(result.markdown)  # 纯 Markdown 文本
```

### 初始化（仅首次）

```bash
cd markitdown-skill && bash install.sh
```

安装后 `.venv/` 目录即持久存在，后续调用无需重复初始化。

---

## 输出格式约定

转换结果写入 stdout，**Agent 应将其视为完整文档直接阅读或二次处理**。

**特殊标记：**
- `<!-- embedded_image: data:image/...;base64,... -->` — 图片的 base64 编码。Agent 可调用自身多模态能力分析此图片，无需外部 API。

---

## 支持的格式

| 格式 | 扩展名 | 转换方式 |
|------|--------|---------|
| PDF | `.pdf` | pdfminer + pdfplumber 文本提取 |
| Word | `.docx` | mammoth 转换（含 OMML 数学公式→LaTeX） |
| PowerPoint | `.pptx` | python-pptx 解析形状/文字/图表/表格 |
| Excel | `.xlsx`, `.xls` | pandas + openpyxl / xlrd |
| 图片 | `.jpg`, `.jpeg`, `.png` | EXIF 元数据 + base64 嵌入标记 |
| 音频 | `.wav`, `.mp3`, `.m4a`, `.mp4` | EXIF 元数据 + SpeechRecognition 转录 |
| HTML | `.html`, `.htm` | markdownify 转换 |
| CSV | `.csv` | pandas 读取→Markdown 表格 |
| EPUB | `.epub` | ebooklib 解析 |
| Outlook | `.msg` | olefile 解析 |
| Jupyter | `.ipynb` | JSON 解析→Markdown |
| ZIP | `.zip` | 递归遍历内容 |
| YouTube | URL | youtube-transcript-api 抓字幕 |
| Wikipedia | URL | API 提取 |
| RSS | URL / `.xml` | feedparser 解析 |
| Bing SERP | URL | HTML 解析 |
| 纯文本 | `.txt`, `.json`, `.xml`, `.md` 等 | 直接输出 |

---

## 安装

### 一键安装（推荐）

```bash
cd markitdown-skill
bash install.sh
```

安装脚本会自动：
1. 检测 Python 3.10+
2. 创建虚拟环境 `.venv`
3. 安装所有核心依赖
4. 检测 `exiftool`（可选）
5. 验证安装成功

### 手动安装

```bash
cd markitdown-skill
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 使用

### 命令行

```bash
source .venv/bin/activate
python -m markitdown_skill document.pdf              # 输出到 stdout
python -m markitdown_skill document.pdf -o out.md    # 输出到文件
cat document.pdf | python -m markitdown_skill         # 管道输入
python -m markitdown_skill -x .docx < input.bin       # 指定扩展名
```

### Python API

```python
from markitdown_skill import MarkItDown

md = MarkItDown()

# 本地文件
result = md.convert("report.pdf")
print(result.markdown)

# URL
result = md.convert("https://example.com/doc.docx")

# 二进制流
with open("data.bin", "rb") as f:
    result = md.convert_stream(f, stream_info=StreamInfo(extension=".xlsx"))
```

### API 方法

| 方法 | 说明 |
|------|------|
| `md.convert(source)` | 智能入口：自动判断路径/URL/流/Response |
| `md.convert_local(path)` | 本地文件路径 |
| `md.convert_stream(binary_io)` | 二进制流 |
| `md.convert_uri(uri)` | file:/http:/https:/data: URI |
| `md.convert_response(requests.Response)` | HTTP 响应对象 |

返回值 `DocumentConverterResult`：
- `.markdown` — 转换后的 Markdown 文本
- `.title` — 文档标题（可选）
- `str(result)` — 等价于 `.markdown`

---

## 与原始 MarkItDown 的关键差异

| 维度 | 原始 | Skill 版 |
|------|------|---------|
| **LLM 依赖** | 需要 `openai` + API Key | **不需要** |
| **图片处理** | 调 GPT-4o Vision | EXIF 元数据 + base64 标记，由 Agent 自行分析 |
| **PPTX 图片** | 调 GPT-4o Vision | 保留 alt text，Agent 自主处理 |
| **Azure Doc Intel** | 支持 | 移除 |
| **插件系统** | 支持 3rd-party entry_points | 移除（Skill 内聚） |
| **安装** | `pip install markitdown[all]` | `bash install.sh` 一键 |
| **配置** | `OPENAI_API_KEY` | **零配置** |

---

## 图片处理机制

对于 JPG/PNG 图片和 PPTX 内嵌图片，Skill 不再调用外部 LLM：

- **EXIF 元数据**：如果安装了 `exiftool`，提取 ImageSize / DateTimeOriginal / GPSPosition 等
- **Base64 嵌入标记**：输出中包含 `<!-- embedded_image: data:image/...;base64,... -->`
- **Agent 自主处理**：DeepSeek Agent 发现该标记后，使用自身的多模态能力分析图片内容

示例输出：

```markdown
ImageSize: 1920x1080
DateTimeOriginal: 2025:01:15 14:30:00

<!-- embedded_image: data:image/jpeg;base64,/9j/4AAQSkZJRg... -->
```

---

## 可选依赖

核心依赖（6 个）自动安装。以下为按需安装：

| 功能 | 额外依赖 |
|------|---------|
| PDF 解析 | `pdfminer.six`, `pdfplumber` |
| Word 解析 | `mammoth`, `lxml` |
| Excel 解析 | `pandas`, `openpyxl`, `xlrd` |
| PowerPoint 解析 | `python-pptx` |
| 音频转录 | `pydub`, `SpeechRecognition` |
| YouTube 字幕 | `youtube-transcript-api` |
| EPUB 解析 | `ebooklib` |
| EXIF 元数据 | `exiftool`（系统级工具） |

---已安装的依赖不会报错，缺少时转换器会静默跳过。

---

## 安全

MarkItDown 以当前进程权限执行 I/O。在不受信任的环境中：
- 使用最窄的 API（`convert_local()`, `convert_stream()`）
- 不要向 `convert()` 传入不可信 URL

---

## 许可

MIT License — 基于 [microsoft/markitdown](https://github.com/microsoft/markitdown)
