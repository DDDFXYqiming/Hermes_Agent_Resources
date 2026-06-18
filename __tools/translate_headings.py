"""Add a Chinese heading translation to English-only H2/H3/H4 headings in Markdown.

Heuristics (deliberately conservative):
- Only touch headings where the heading text has no CJK characters at all.
- Skip headings that are inside code fences.
- Skip headings shorter than 4 characters (likely codes/symbols).
- Skip headings that look like a path, URL, BVID, image name, or all-uppercase token.

Result: a new H2 sub-heading immediately after the original, prefixed with "中文：".
The original heading stays so anchors, templates, and code references still work.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path("E:/AI_Projects/Hermes_Agent_Resources/General_skills")
MARKER = "中文："

SKIP_FILE_PARTS = {
    "code_run_header.py",
    "design_spec",
}


def is_pathy(s: str) -> bool:
    if s.startswith("/") or s.startswith("./") or s.startswith("../"):
        return True
    if re.match(r"^[A-Za-z]:[\\/]", s):
        return True
    if re.search(r"\.(md|py|json|yaml|yml|svg|png|jpg|jpeg|txt|css|html|sh|bat)\b", s):
        return True
    if re.match(r"^BV[0-9A-Za-z]{6,}$", s):
        return True
    return False


def looks_pure_token(s: str) -> bool:
    s = s.strip()
    if not s:
        return True
    if is_pathy(s):
        return True
    # mostly underscores / pipes / colons => not a normal prose heading
    alnum = sum(ch.isalnum() for ch in s)
    if alnum / max(len(s), 1) < 0.5:
        return True
    return False


def split_paragraph(s: str) -> list[str]:
    s = s.strip()
    if not s:
        return []
    parts: list[str] = [p.strip(" :-|•") for p in re.split(r"[\.;]", s) if p.strip()]
    return parts[:3] or [s]


def has_cjk(s: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", s))


def translate_phrase(en: str) -> str:
    """Lightweight deterministic translation for common heading tokens.

    Not a full MT — it just maps frequent vocab so each heading gets a usable
    Chinese title. Anything not in the table gets a clean Chinese framing using
    the heading words verbatim.
    """
    vocab = {
        "overview": "概览",
        "introduction": "简介",
        "background": "背景",
        "purpose": "目标",
        "goals": "目标",
        "scope": "范围",
        "audience": "目标读者",
        "quick start": "快速开始",
        "quickstart": "快速开始",
        "getting started": "快速开始",
        "install": "安装",
        "installation": "安装",
        "setup": "安装配置",
        "configuration": "配置",
        "configure": "配置",
        "config": "配置",
        "options": "选项",
        "parameters": "参数",
        "arguments": "参数",
        "return": "返回值",
        "returns": "返回值",
        "errors": "错误处理",
        "error handling": "错误处理",
        "examples": "示例",
        "example": "示例",
        "usage": "使用方法",
        "how to use": "使用方法",
        "when to use": "使用场景",
        "usage scenarios": "使用场景",
        "use cases": "使用场景",
        "structure": "结构",
        "architecture": "架构",
        "design": "设计",
        "design spec": "设计规范",
        "spec": "规范",
        "specs": "规范",
        "specification": "规范",
        "specifications": "规范",
        "rules": "规则",
        "principles": "原则",
        "guidelines": "指南",
        "best practices": "最佳实践",
        "checklist": "检查清单",
        "checklists": "检查清单",
        "validation": "校验",
        "verify": "校验",
        "verification": "校验",
        "testing": "测试",
        "test": "测试",
        "tests": "测试",
        "outputs": "输出",
        "output": "输出",
        "input": "输入",
        "inputs": "输入",
        "inputs/outputs": "输入与输出",
        "workflow": "工作流",
        "workflows": "工作流",
        "procedure": "步骤",
        "steps": "步骤",
        "step": "步骤",
        "commands": "命令",
        "cli": "命令行",
        "cli usage": "命令行用法",
        "api": "接口",
        "api reference": "接口参考",
        "reference": "参考",
        "references": "参考资料",
        "links": "相关链接",
        "related": "相关内容",
        "see also": "相关参考",
        "notes": "说明",
        "note": "说明",
        "tips": "提示",
        "caveats": "注意事项",
        "pitfalls": "常见陷阱",
        "common pitfalls": "常见陷阱",
        "limitations": "局限性",
        "constraints": "限制",
        "requirements": "依赖与要求",
        "prerequisites": "前置条件",
        "dependencies": "依赖",
        "troubleshooting": "故障排查",
        "faq": "常见问题",
        "frequently asked questions": "常见问题",
        "license": "许可证",
        "changelog": "变更日志",
        "version": "版本",
        "versions": "版本",
        "todos": "待办",
        "contributing": "贡献",
        "roadmap": "路线图",
        "feature": "功能",
        "features": "功能",
        "background colors": "背景色",
        "palette": "配色",
        "palettes": "配色",
        "color": "颜色",
        "colors": "颜色",
        "colour": "颜色",
        "colours": "颜色",
        "type": "类型",
        "types": "类型",
        "style": "风格",
        "styles": "风格",
        "rendering": "渲染",
        "renderings": "渲染",
        "scene": "场景",
        "scenes": "场景",
        "icon": "图标",
        "icons": "图标",
        "chart": "图表",
        "charts": "图表",
        "table": "表格",
        "tables": "表格",
        "section": "段落",
        "sections": "段落",
        "page": "页面",
        "pages": "页面",
        "layout": "版式",
        "layouts": "版式",
        "component": "组件",
        "components": "组件",
        "shape": "形状",
        "shapes": "形状",
        "gradient": "渐变",
        "gradients": "渐变",
        "shadow": "阴影",
        "shadows": "阴影",
        "font": "字体",
        "fonts": "字体",
        "typography": "排版",
        "spacing": "间距",
        "margin": "外边距",
        "margins": "外边距",
        "padding": "内边距",
        "radius": "圆角",
        "corners": "圆角",
        "border": "边框",
        "borders": "边框",
        "stroke": "描边",
        "strokes": "描边",
        "logo": "标志",
        "logos": "标志",
        "hero": "主视觉",
        "background": "背景",
        "subject": "主体",
        "subjects": "主体",
        "foreground": "前景",
        "middle ground": "中景",
        "midground": "中景",
        "composition": "构图",
        "lighting": "光线",
        "highlight": "高光",
        "highlights": "高光",
        "focus": "焦点",
        "texture": "材质",
        "textures": "材质",
        "prompt": "提示词",
        "prompts": "提示词",
        "template": "模板",
        "templates": "模板",
        "manifest": "清单",
        "metadata": "元数据",
        "ascii": "ASCII 字符",
        "emoji": "Emoji 表情",
        "unicode": "Unicode 字符",
        "kaios": "字号",
        "web": "Web",
        "desktop": "桌面",
        "mobile": "移动端",
        "tablet": "平板",
        "widescreen": "宽屏",
        "promotional": "宣传",
        "executive": "高管",
        "starter": "入门",
        "intermediate": "中级",
        "advanced": "高级",
        "beginner": "初级",
        "core": "核心",
        "foundation": "基础",
        "essentials": "要点",
        "misc": "杂项",
        "miscellaneous": "杂项",
        "appendix": "附录",
        "glossary": "术语表",
        "summary": "摘要",
        "conclusion": "结论",
        "context": "上下文",
        "prerequisites": "前置依赖",
    }

    raw = en.strip()
    low = raw.lower()
    # direct lookup
    if low in vocab:
        return vocab[low]
    # try to translate pipe-joined segments
    if "|" in raw:
        segs = [vocab.get(s.strip().lower(), s.strip()) for s in raw.split("|")]
        return " | ".join(segs)
    # split dash
    if " - " in raw:
        segs = [vocab.get(s.strip().lower(), s.strip()) for s in raw.split(" - ")]
        return " - ".join(segs)
    if " – " in raw:
        segs = [vocab.get(s.strip().lower(), s.strip()) for s in raw.split(" – ")]
        return " - ".join(segs)
    # tokenize words
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9_\-]+", raw)
    if tokens:
        out: list[str] = []
        for t in tokens:
            out.append(vocab.get(t.lower(), t))
        if all(t == vocab.get(t.lower(), t) for t in tokens):
            return f"中文标题：{raw}"
        return "中文标题：" + " ".join(out)
    return f"中文标题：{raw}"


def in_code_fence(lines: list[str], idx: int) -> bool:
    inside = False
    fence = None
    for i in range(idx):
        line = lines[i].lstrip()
        m = re.match(r"^(`{3,}|~{3,})", line)
        if m:
            tag = m.group(1)
            if not inside:
                inside = True
                fence = tag
            elif fence and line.startswith(fence):
                inside = False
                fence = None
    return inside


def add_translation(path: Path) -> bool:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if MARKER in text:
        return False
    lines = text.split("\n")
    new_lines: list[str] = []
    changed = False
    fence_active = False
    fence_marker: str | None = None
    for idx, line in enumerate(lines):
        new_lines.append(line)
        stripped = line.lstrip()
        m = re.match(r"^(`{3,}|~{3,})", stripped)
        if m:
            tag = m.group(1)
            if not fence_active:
                fence_active = True
                fence_marker = tag
            elif fence_marker and stripped.startswith(fence_marker):
                fence_active = False
                fence_marker = None
            continue
        if fence_active:
            continue
        hm = re.match(r"^(#{2,6})\s+(.+?)\s*$", line)
        if not hm:
            continue
        head = hm.group(2)
        if has_cjk(head):
            continue
        if looks_pure_token(head):
            continue
        if len(head.strip()) < 4:
            continue
        trans = translate_phrase(head)
        if not trans:
            continue
        indent = line[: len(line) - len(line.lstrip())]
        new_lines.append(f"{indent}### {MARKER}{trans}")
        changed = True
    if not changed:
        return False
    path.write_text("\n".join(new_lines), encoding="utf-8", newline="\n")
    return True


def main() -> int:
    count = 0
    for p in sorted(ROOT.rglob("*.md")):
        if any(part in SKIP_FILE_PARTS for part in p.parts):
            continue
        if add_translation(p):
            count += 1
    print(f"heading-translated files: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
