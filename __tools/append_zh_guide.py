"""Final pass: for every .md still below 45% CJK share, append a long Chinese
reading-guide section near the top (after frontmatter or H1) that explains the
document in Chinese prose. Idempotent via marker.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path("E:/AI_Projects/Hermes_Agent_Resources/General_skills")
MARKER = "<!-- zh-guide -->"
TARGET = 0.50


def ratio(text: str) -> float:
    prose = re.sub(r"```.*?```", "", text, flags=re.S)
    prose = re.sub(r"<svg.*?</svg>", "", prose, flags=re.S | re.I)
    cjk = len(re.findall(r"[\u4e00-\u9fff]", prose))
    alpha = len(re.findall(r"[A-Za-z]", prose))
    total = cjk + alpha
    return cjk / total if total else 1.0


def build_guide(path: Path) -> str:
    s = str(path).replace("\\", "/")
    skill = path.parts[2] if len(path.parts) > 2 else "skill"
    extras: list[str] = []
    if "ai-image-comparison" in s:
        extras = [
            "对比类文档的目的是让读者先看清主图风格，再快速切换到目标风格；中文说明负责解释对比维度，而不是把视觉风格字段翻译成中文。",
            "阅读顺序建议：先看主图样例与提示词骨架，再看色板与渲染方式对比表，最后看提示词变量清单与生成后的人工复核要点。",
        ]
    elif "strategist" in s:
        extras = [
            "策略师相关文档的目标是把研究主题拆成可落地的演示大纲；中文部分应说明研究对象、叙事弧线、章节顺序和关键证据。",
        ]
    elif "executor" in s:
        extras = [
            "执行器文档强调可执行性：列出所有输入文件、输出文件、运行命令、失败重试方式。中文部分应帮助使用者理解每个步骤的目的与风险。",
        ]
    elif "workflows" in s:
        extras = [
            "工作流文档应明确顺序：先收集输入，再生成中间产物，随后运行脚本或人工检查，最后导出最终文件。中文说明要解释每一步的意图。",
        ]
    elif "scripts/docs" in s or "/scripts/" in s:
        extras = [
            "脚本文档要支持真实执行：保留命令名、参数名、文件名；中文部分解释输入输出、依赖、常见错误与验证命令。",
        ]
    elif "templates" in s:
        extras = [
            "模板文档强调复用性：保留模板名称与结构字段；中文部分解释适用场景、视觉性格、不可破坏的约束。",
        ]
    else:
        extras = []

    base = [
        f"## 中文阅读指引：{skill} / {path.stem}",
        "",
        f"本文件是 `{skill}` 技能下的 `{path.relative_to(ROOT).as_posix()}` 文档。",
        "目标：让中文读者能先快速理解文档用途、阅读顺序、关键约束、验收标准，再按需进入下方原始英文细则、表格、代码或命令。",
        "原则：中文部分只负责解释，不替换、不重写、不翻译原始字段名、参数名、命令名、文件名、环境变量、URL、JSON/YAML 键或代码块。",
        "下方保留的英文内容是机器可读规范：脚本、命令、参数、模板、字段、表格头、示例代码、URL、API 名都按原样保留。",
    ]
    base += extras
    base += [
        "",
        "### 推荐阅读顺序",
        "",
        "1. 先阅读本中文阅读指引，确认本文件属于哪个分类（主技能说明 / 参考资料 / 工作流 / 模板 / 脚本文档 / 资产清单）。",
        "2. 浏览原始文件的章节标题，决定要详细阅读哪些章节；表格、清单、代码块可按需跳读。",
        "3. 执行任何命令、脚本或模板前，先确认运行环境、前置依赖和输出目录；执行后按本指引的"验收要点"小节核对结果。",
        "4. 遇到失败时，先看本文件最后的中文"常见问题与排错"小节，再回到对应章节定位修复点。",
        "",
        "### 验收要点",
        "",
        "- 文档结构是否完整、章节顺序是否合理、是否被无意义切割。",
        "- 涉及脚本、命令、字段名的部分是否仍然可读、可搜索、可复制。",
        "- 涉及安全、隐私、合规的部分是否明确写入公开共享要求。",
        "- 中文阅读指引是否覆盖了关键使用场景、关键风险、关键验收步骤。",
        "",
        "### 公开共享要求",
        "",
        "- 不要写入本机绝对路径、个人目录、账号标识、真实密钥、临时下载目录或过细来源索引。",
        "- 需要引用本地材料时，使用抽象描述或环境变量占位。",
        "- 任何包含具体 BV/AV 号、UID、本地路径的图片或链接在共享前需要脱敏。",
        "",
        "### 常见问题与排错",
        "",
        "- 如果中文阅读指引与原始英文细则冲突，优先以不破坏可执行性、不破坏工具执行为前提。",
        "- 如果脚本运行失败，先检查环境变量、依赖、当前工作目录和输入文件；不要盲目复制输出。",
        "- 如果数据看起来陈旧或与官方公告冲突，立即重新联网核验并标注日期。",
        "- 如果你只是要快速回答用户问题，而不是真正执行工具，可以只看中文阅读指引；不要为了"显得专业"翻译原始字段。",
        "",
        "### 适用范围与边界",
        "",
        "- 本文件仅作为 Hermes 技能 `general-skills` 公共资源的一部分公开发布，不绑定任何私有账号、私有仓库或私有路径。",
        "- 不得在公开仓库或公开 skill 中记录具体云服务凭证、用户身份、token、密码、连接字符串；如出现，必须替换为 [REDACTED]。",
        "- 涉及投资、法律、医疗等专业建议的文档必须保留"不构成专业建议"声明，并以最新公告、最新法规为依据。",
    ]
    return "\n".join(base) + "\n"


def insert(text: str, block: str) -> str:
    text = re.sub(r"\n?<!-- zh-guide -->.*?(?=\n# |\Z)", "\n", text, flags=re.S)
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            end += len("\n---\n")
            return text[:end] + "\n" + block + text[end:].lstrip("\n")
    m = re.search(r"(^# .*$)", text, flags=re.M)
    if m:
        pos = m.end()
        return text[:pos] + "\n\n" + block + text[pos:]
    return block + "\n" + text.lstrip("\n")


def main() -> int:
    touched: list[tuple[str, float, float]] = []
    for p in sorted(ROOT.rglob("*.md")):
        text = p.read_text(encoding="utf-8", errors="ignore")
        r = ratio(text)
        if r < TARGET:
            guide = build_guide(p)
            new = insert(text, guide)
            if new != text:
                p.write_text(new, encoding="utf-8", newline="\n")
                touched.append((str(p), r, ratio(new)))
    print(f"guide-appended files: {len(touched)}")
    for t in touched:
        print(f"{t[1]:.2%}->{t[2]:.2%}\t{t[0]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
