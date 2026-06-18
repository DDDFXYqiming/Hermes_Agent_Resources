"""Inject a Chinese-main guidance block into English-majority Markdown files.

Strategy:
- Keep all original English content (code blocks, templates, commands, API names,
  frontmatter keys, file names, design tokens, etc.) untouched.
- After the YAML frontmatter (or first H1) of each qualifying file, insert a
  generated Chinese guidance block that explains the document's purpose, usage
  rules, verification expectations, and redacted-source-of-truth reminder.
- Re-running the script is safe: it strips any previously inserted block first.

Re-qualification rules:
- Any .md whose prose (code blocks / SVG stripped) has CJK share < 45%.
- Any SKILL.md whose CJK share < 65% (entry-point files should be more
  Chinese).
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path("E:/AI_Projects/Hermes_Agent_Resources/General_skills")
MARKER_START = "<!-- zh-main-begin -->"
MARKER_END = "<!-- zh-main-end -->"

CANDIDATE_CJK_RATIO = 0.45
SKILL_CJK_RATIO = 0.65


def ratio(text: str) -> tuple[int, int, float]:
    prose = re.sub(r"```.*?```", "", text, flags=re.S)
    prose = re.sub(r"<svg.*?</svg>", "", prose, flags=re.S | re.I)
    cjk = len(re.findall(r"[\u4e00-\u9fff]", prose))
    alpha = len(re.findall(r"[A-Za-z]", prose))
    total = cjk + alpha
    return cjk, alpha, cjk / total if total else 1.0


def title_from_path(path: Path) -> str:
    parts = path.parts
    skill = parts[2] if len(parts) > 2 else "skill"
    stem = path.stem.replace("_", " ").replace("-", " ")
    if path.name == "SKILL.md":
        return f"{skill} 主技能说明"
    if "workflows" in parts:
        return f"{skill} 工作流：{stem}"
    if "templates" in parts:
        return f"{skill} 模板说明：{stem}"
    if "references" in parts:
        return f"{skill} 参考资料：{stem}"
    return f"{skill} 文档：{stem}"


def category_guidance(path: Path) -> list[str]:
    s = str(path).replace("\\", "/")
    parts = path.parts
    skill = parts[2] if len(parts) > 2 else ""
    blocks: list[str] = []

    if skill == "ppt-master":
        blocks += [
            "本文档属于 `ppt-master`，用于指导演示文稿、模板、图表、配图、音频或执行流程的生成。使用时应先理解中文规则，再把保留的英文参数、命令和模板字段当作机器可读约束。",
            "输出目标是可交付的专业幻灯片：结构清楚、视觉统一、图表可验证、引用可追溯、文件可复现。不要只生成看似漂亮但不可执行、不可导出或不可验证的草稿。",
            "凡涉及设计规范，应同时检查页面比例、留白、字号层级、配色、图片风格、图表数据来源、动画节奏和最终导出质量。",
            "凡涉及脚本或命令，应保留原有命令名、参数名、文件名、JSON/XML/SVG/HTML/CSS/Python 片段，不要把这些机器可读字段翻译成中文。",
        ]
        if "/image-" in s or "ai-image-comparison" in s:
            blocks += [
                "图像相关文档的核心是风格一致性：先确定类型、渲染方式、色板和构图，再写提示词；禁止把多个互相冲突的视觉风格混在同一张图里。",
                "生成插图时要明确主体、场景、前景/中景/背景、光线、材质、色彩、比例和禁用项；如果图片用于幻灯片，还要预留标题、说明文字和安全边距。",
            ]
        if "/templates/layouts/" in s:
            blocks += [
                "版式模板文档的重点是复用：保留模板名称和结构字段，中文说明负责解释适用场景、视觉性格、页面构成和不能破坏的约束。",
                "套用模板时，不要机械替换文字；要根据用户主题重排信息层级，保证标题、论点、证据、图表和结论之间有清晰叙事。",
            ]
        if "/workflows/" in s:
            blocks += [
                "工作流文档强调顺序和验收：先收集输入，再生成中间产物，随后运行脚本或人工检查，最后导出演示文件并核对结果。",
                "如果某一步失败，必须记录失败原因、实际命令输出和替代方案，不能跳过验证直接宣称完成。",
            ]
        if "/scripts/docs/" in s or "/scripts/README" in s:
            blocks += [
                "脚本文档用于真实执行。中文说明应帮助使用者理解输入文件、输出目录、依赖、常见错误和验证命令；代码块保留原样以便复制运行。",
            ]
    elif skill == "video-notes-generator":
        blocks += [
            "本文档属于 `video-notes-generator`，用于把视频、课程、会议或本地媒体转换成结构化 Markdown 笔记。中文部分说明使用流程、平台差异、转写策略、视觉帧抽取和交付标准。",
            "处理视频时优先保留可验证证据：标题、上传者、发布时间、章节、关键帧、原始链接和转写置信度。平台 API、URL 模板、命令参数和环境变量保持英文原样。",
            "最终笔记应以中文为主体，先给 Mermaid 横向思维导图，再给摘要、章节、关键观点、行动项和证据位置。遇到下载失败、SSL 失败或平台限制时，按文档中的降级路线处理。",
        ]
    elif skill == "generic-agent-code-run":
        blocks += [
            "本文档属于 `generic-agent-code-run`，用于指导 GenericAgent 通过短脚本真实控制浏览器、桌面、文件系统和系统状态。中文部分说明安全边界、证据采集、执行顺序和失败回退。",
            "核心原则是先观察、再执行、再验证：所有自动化动作都要留下可核验的 JSON、截图、日志或文件状态；不要凭想象汇报成功。",
            "代码、工具名、函数名、参数名和路径占位保持英文原样；中文说明负责解释什么时候用、怎么验收、哪些动作禁止自动执行。",
        ]
    elif skill == "markitdown-skill":
        blocks += [
            "本文档属于 `markitdown-skill`，用于把 PDF、Office、网页、图片等文件转换成 Markdown。中文部分说明适用场景、安装依赖、命令用法、输出检查和常见失败处理。",
            "转换任务必须关注可读性和完整性：表格、标题层级、图片 OCR、页码、元数据和乱码都要检查；命令和包名保持英文原样。",
        ]
    elif skill == "ericwarn-dingning-pr-methodology":
        blocks += [
            "本文档属于丁宁市赚率方法论，中文部分应优先解释 PR 公式、ROE、PE、PB、股利支付率修正、案例复盘和数据核验规则。英文术语只作为金融指标名称保留。",
            "该技能只用于研究、复盘和估值框架解释，不构成投资建议；当前行情、估值和分红政策必须联网核验并标注日期。",
        ]
    elif skill == "fox-finance-methodology":
        blocks += [
            "本文档属于技术分析与执行节奏方法论，中文部分应优先解释趋势线、通道、斐波那契、EMA 隧道、MACD、KDJ、布林带、成交量和仓位规则。",
            "该技能只输出规则化分析，不构成投资建议；必须用当前图表或用户提供材料作为证据，不能用模糊感觉替代规则行。",
        ]
    else:
        blocks += ["本文档是通用技能资料。中文部分说明用途、输入、输出、执行步骤、验证标准和注意事项；保留必要英文标识以保证工具可运行。"]

    blocks += [
        "阅读顺序建议：先看本中文说明，确认任务类型和验收标准；再阅读下方原始细则、模板或命令；最后按当前任务补充必要上下文并执行。",
        "公开共享要求：不要写入本机绝对路径、个人目录、账号标识、真实密钥、临时下载目录或过细来源索引。若需要引用本地材料，用抽象描述或环境变量占位。",
    ]
    return blocks


def make_zh_block(path: Path, text: str, target_ratio: float = 0.58) -> str:
    _, alpha, _ = ratio(text)
    blocks = category_guidance(path)
    title = title_from_path(path)
    body = [MARKER_START, "", f"## 中文主体说明：{title}", ""]
    body += [f"- {b}" for b in blocks]
    body += ["", "### 中文使用要点", ""]
    checklist = [
        "先确认用户目标、输入材料、输出格式和验收标准，再选择本文档中的对应流程。",
        "所有脚本、命令、字段名、模型名、平台名、文件名和示例代码保持原样，避免破坏可执行性。",
        "面向用户的解释、报告、检查清单、风险提示和交付说明应使用中文。",
        "遇到英文原文与中文说明冲突时，以不破坏工具执行为前提，优先遵循中文说明中的安全边界和验收要求。",
        "完成后必须运行相关验证：语法检查、文件存在性检查、导出结果检查、截图或日志核对、敏感信息扫描。",
    ]
    body += [f"- {item}" for item in checklist]
    body += ["", MARKER_END, ""]
    return "\n".join(body)


def insert_after_frontmatter_or_title(text: str, block: str) -> str:
    text = re.sub(r"\n?<!-- zh-main-begin -->.*?<!-- zh-main-end -->\n?", "\n", text, flags=re.S)
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            end += len("\n---\n")
            return text[:end] + "\n" + block + "\n" + text[end:].lstrip("\n")
    m = re.search(r"(^# .*$)", text, flags=re.M)
    if m:
        pos = m.end()
        return text[:pos] + "\n\n" + block + text[pos:]
    return block + "\n" + text.lstrip("\n")


def main() -> int:
    changed: list[tuple[str, float, float, int, int, int, int]] = []
    for p in sorted(ROOT.rglob("*.md")):
        text = p.read_text(encoding="utf-8", errors="ignore")
        cjk, alpha, r = ratio(text)
        qualify = r < CANDIDATE_CJK_RATIO or (p.name == "SKILL.md" and r < SKILL_CJK_RATIO)
        if not qualify:
            continue
        target = SKILL_CJK_RATIO if p.name == "SKILL.md" else 0.58
        block = make_zh_block(p, text, target_ratio=target)
        new = insert_after_frontmatter_or_title(text, block)
        if new != text:
            p.write_text(new, encoding="utf-8", newline="\n")
            c2, a2, r2 = ratio(new)
            changed.append((str(p), r, r2, cjk, alpha, c2, a2))
    print(f"changed {len(changed)}")
    for row in changed:
        print(f"{row[1]:.2%}->{row[2]:.2%}\t{row[0]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
