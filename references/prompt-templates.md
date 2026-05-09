# Prompt Templates

The video-notes-generator uses several prompt templates to instruct the LLM. These are injected into the final prompt based on user-selected format options.

## BASE_PROMPT

**Purpose**: The main summarization prompt sent to the LLM for every note generation request.

**Structure**:
- System role: Professional note assistant
- Language rules: Chinese output, English for proper nouns/technical terms
- Injected variables: `{video_title}`, `{tags}`, `{segment_text}`
- Output rules: Markdown only, no code blocks, escaped numbered headings
- Core tasks: Complete info, remove filler, preserve key details, readable layout, preserve LaTeX formulas

**Template** (Chinese):
```
你是一个专业的笔记助手，擅长将视频转录内容整理成清晰、有条理且信息丰富的笔记。

语言要求：
- 笔记必须使用 **中文** 撰写。
- 专有名词、技术术语、品牌名称和人名应适当保留 **英文**。

视频标题：
{video_title}

视频标签：
{tags}

输出说明：
- 仅返回最终的 **Markdown 内容**。
- **不要**将输出包裹在代码块中。

视频分段（格式：开始时间 - 内容）：
---
{segment_text}
---

你的任务：
根据上面的分段转录内容，生成结构化的笔记，遵循以下原则：

1. **完整信息**：记录尽可能多的相关细节。
2. **去除无关内容**：省略广告、填充词、问候语。
3. **保留关键细节**：保留重要事实、示例、结论和建议。
4. **可读布局**：使用项目符号，保持段落简短。
5. 视频中提及的数学公式必须以 LaTeX 语法呈现。

额外重要的任务如下(每一个都必须严格完成):
```

**When used**: Always — this is the base of every prompt.

---

## LINK

**Purpose**: Instructs the LLM to add timestamp markers to section headings.

**Template**:
```
9. **Add time markers**: THIS IS IMPORTANT For every main heading (`##`),
   append the starting time of that segment using the format,
   start with *Content, eg: `*Content-[mm:ss]`.
```

**When used**: When `link` is included in format options.

**Output example**:
```markdown
## AI的发展历史 *Content-[02:15]
```

---

## AI_SUM

**Purpose**: Instructs the LLM to append a professional AI summary at the end.

**Template**:
```
🧠 Final Touch:
At the end of the notes, add a professional **AI Summary** in Chinese –
a brief conclusion summarizing the whole video.
```

**When used**: When `summary` is included in format options.

**Output example**:
```markdown
## AI 总结
本视频介绍了AI的发展历程，从早期规则系统到现代大语言模型...
```

---

## SCREENSHOT

**Purpose**: Instructs the LLM to insert screenshot placeholder markers for visual content.

**Template**:
```
8. **Screenshot placeholders**: If a section involves **visual demonstrations,
   code walkthroughs, UI interactions**, or any content where visuals aid
   understanding, insert a screenshot cue at the end of that section:
   - Format: `*Screenshot-[mm:ss]`
   - Only use it when truly helpful.
```

**When used**: When `screenshot` is included in format options.

**Output example**:
```markdown
这段代码展示了如何配置环境变量 *Screenshot-[05:30]
```

---

## MERGE_PROMPT

**Purpose**: Used to merge multiple chunked note segments into a single coherent document. When a video is very long, the transcript is split into chunks, each processed separately, then merged.

**Template**:
```
你将收到多个来自同一视频的 Markdown 笔记片段，请合并成一份完整笔记：
- 只做合并与去重，不要发明新内容
- 保持原有标题层级与 Markdown 结构
- 保留所有 *Content-[mm:ss] 与 *Screenshot-[mm:ss] 标记
- 保持中文输出，专有名词保留英文
- 不要使用代码块包裹输出
```

**When used**: Automatically when the transcript exceeds the LLM context window and needs to be chunked.

---

## Prompt Assembly Order

The final prompt is assembled in this order:

1. `BASE_PROMPT` (always)
2. Format options appended in order: `LINK`, `SCREENSHOT`, `AI_SUM` (based on selection)
3. Style description appended (from style map)
4. Any user-provided extra instructions appended last
