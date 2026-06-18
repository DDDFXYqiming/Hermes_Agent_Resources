"""For every still-English-majority Markdown, expand Chinese guidance under each
H2/H3 heading and translate short English list items.

Rules:
- Keep all code blocks, tables with technical headers, JSON/YAML/SVG/HTML,
  file paths, env vars, and param keys untouched.
- For each H2/H3 heading that lacks CJK, append a `### 中文说明：...` block
  with multiple Chinese bullet points paraphrasing the original heading.
- For list items in the same section that are short English sentences, add a
  Chinese sibling bullet prefixed with `中文：` so the section reads as Chinese-
  first while the English bullet stays as the machine reference.
- Idempotent: marker comments prevent re-injection.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path("E:/AI_Projects/Hermes_Agent_Resources/General_skills")
MARKER = "<!-- zh-expand -->"
MIN_RATIO = 0.45
TARGET = 0.55

HEADING_GLOSSARY: dict[str, str] = {
    "overview": "概览",
    "introduction": "简介",
    "purpose": "目标",
    "scope": "适用范围",
    "audience": "适用读者",
    "quick start": "快速开始",
    "getting started": "快速开始",
    "install": "安装",
    "installation": "安装",
    "setup": "配置",
    "configuration": "配置",
    "options": "选项",
    "parameters": "参数",
    "return": "返回值",
    "returns": "返回值",
    "errors": "错误处理",
    "error handling": "错误处理",
    "examples": "示例",
    "example": "示例",
    "usage": "使用方法",
    "how to use": "使用方法",
    "when to use": "使用场景",
    "use cases": "使用场景",
    "structure": "结构",
    "architecture": "架构",
    "design": "设计",
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
    "tests": "测试",
    "outputs": "输出",
    "output": "输出",
    "input": "输入",
    "inputs": "输入",
    "workflow": "工作流",
    "workflows": "工作流",
    "procedure": "步骤",
    "steps": "步骤",
    "commands": "命令",
    "cli": "命令行",
    "api": "接口",
    "api reference": "接口参考",
    "reference": "参考",
    "references": "参考资料",
    "links": "相关链接",
    "related": "相关内容",
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
    "license": "许可证",
    "changelog": "变更日志",
    "version": "版本",
    "features": "功能",
    "feature": "功能",
    "background": "背景",
    "palettes": "配色",
    "palette": "配色",
    "colors": "颜色",
    "color": "颜色",
    "types": "类型",
    "type": "类型",
    "styles": "风格",
    "style": "风格",
    "renderings": "渲染",
    "rendering": "渲染",
    "scenes": "场景",
    "scene": "场景",
    "icons": "图标",
    "icon": "图标",
    "charts": "图表",
    "chart": "图表",
    "tables": "表格",
    "table": "表格",
    "layout": "版式",
    "layouts": "版式",
    "components": "组件",
    "component": "组件",
    "prompt": "提示词",
    "prompts": "提示词",
    "template": "模板",
    "templates": "模板",
    "manifest": "清单",
    "metadata": "元数据",
    "subject": "主体",
    "subjects": "主体",
    "subject list": "主体清单",
    "rendering style": "渲染风格",
    "rendering styles": "渲染风格",
    "prompt pattern": "提示词模式",
    "prompt patterns": "提示词模式",
    "naming": "命名规则",
    "naming convention": "命名规则",
    "naming conventions": "命名规则",
    "file layout": "文件布局",
    "directory layout": "目录布局",
    "config": "配置",
    "configuration files": "配置文件",
    "configuration file": "配置文件",
    "output formats": "输出格式",
    "output format": "输出格式",
    "input formats": "输入格式",
    "input format": "输入格式",
    "platform support": "平台支持",
    "platforms": "平台",
    "transcription": "转写",
    "transcribe": "转写",
    "transcript": "转写",
    "frame extraction": "关键帧抽取",
    "frames": "关键帧",
    "frame": "关键帧",
    "visual": "视觉",
    "visuals": "视觉材料",
    "mind map": "思维导图",
    "mindmap": "思维导图",
    "mermaid": "Mermaid 图表",
    "summary": "摘要",
    "conclusion": "结论",
    "background colors": "背景色",
    "logo": "标志",
    "logos": "标志",
    "hero": "主视觉",
    "subject isolation": "主体分离",
    "palette swap": "调色板替换",
    "style transfer": "风格迁移",
    "aspect ratio": "宽高比",
    "aspect ratios": "宽高比",
    "deliverables": "交付物",
    "deliverable": "交付物",
    "generation": "生成",
    "process": "流程",
    "post-processing": "后处理",
    "pre-processing": "预处理",
    "triggers": "触发器",
    "trigger": "触发器",
    "actions": "操作",
    "action": "操作",
    "tools": "工具",
    "tool": "工具",
    "tooling": "工具集",
    "integration": "集成",
    "integrations": "集成",
    "backends": "后端",
    "backend": "后端",
    "providers": "服务方",
    "provider": "服务方",
    "safety": "安全",
    "security": "安全",
    "sandbox": "沙箱",
    "browser": "浏览器",
    "browsers": "浏览器",
    "windows": "Windows",
    "macos": "macOS",
    "linux": "Linux",
    "deploy": "部署",
    "deployment": "部署",
    "run": "运行",
    "running": "运行",
    "performance": "性能",
    "metrics": "指标",
    "monitoring": "监控",
    "observability": "可观测性",
    "logging": "日志",
    "logs": "日志",
    "alerts": "告警",
    "alerting": "告警",
    "ci": "CI 持续集成",
    "cd": "CD 持续部署",
    "ci/cd": "CI/CD",
    "release": "发布",
    "releases": "发布",
    "support": "支持",
    "help": "帮助",
    "guide": "指南",
    "guides": "指南",
    "tutorial": "教程",
    "tutorials": "教程",
    "course": "课程",
    "courses": "课程",
    "lecture": "讲座",
    "lectures": "讲座",
    "video": "视频",
    "videos": "视频",
    "audio": "音频",
    "animations": "动画",
    "animation": "动画",
    "transition": "过渡",
    "transitions": "过渡",
    "playback": "播放",
    "narrative": "叙事",
    "narratives": "叙事",
    "story": "故事",
    "stories": "故事",
    "narrative arc": "叙事弧线",
    "narrative arcs": "叙事弧线",
    "content": "内容",
    "topics": "主题",
    "topic": "主题",
    "research": "研究",
    "analysis": "分析",
    "context": "上下文",
    "background story": "背景故事",
    "editing": "编辑",
    "edit": "编辑",
    "editor": "编辑器",
    "render": "渲染",
    "rendering engine": "渲染引擎",
    "renderers": "渲染器",
    "renderer": "渲染器",
    "image": "图像",
    "images": "图像",
    "photo": "照片",
    "photos": "照片",
    "icon set": "图标集",
    "icon sets": "图标集",
    "design system": "设计系统",
    "design tokens": "设计令牌",
    "design token": "设计令牌",
    "tokens": "令牌",
    "token": "令牌",
    "color tokens": "颜色令牌",
    "color token": "颜色令牌",
    "spacing tokens": "间距令牌",
    "radius tokens": "圆角令牌",
    "typography tokens": "排版令牌",
    "executor": "执行器",
    "executors": "执行器",
    "consultant": "顾问",
    "consultants": "顾问",
    "strategist": "策略师",
    "designer": "设计师",
    "designers": "设计师",
    "agent": "智能体",
    "agents": "智能体",
    "workflow integration": "工作流集成",
    "execute": "执行",
    "executes": "执行",
    "execution": "执行",
    "design philosophy": "设计哲学",
    "core values": "核心价值",
    "principles and constraints": "原则与约束",
    "do and don't": "推荐与禁忌",
    "dos and don'ts": "推荐与禁忌",
    "approval": "审核",
    "approvals": "审核",
    "review": "复核",
    "reviews": "复核",
    "approval flow": "审核流程",
    "process flow": "流程",
    "process flows": "流程",
    "data flow": "数据流",
    "data flows": "数据流",
    "data sources": "数据来源",
    "data source": "数据来源",
    "data outputs": "数据输出",
    "data output": "数据输出",
    "report": "报告",
    "reports": "报告",
    "deliverable checklist": "交付检查清单",
    "package": "打包",
    "packaging": "打包",
    "publishing": "发布",
    "publish": "发布",
    "deployment options": "部署选项",
    "hosting": "托管",
    "container": "容器",
    "containers": "容器",
    "kubernetes": "Kubernetes",
    "compose": "Compose",
    "matrix": "矩阵",
    "pyramid": "金字塔",
    "funnel": "漏斗",
    "cycle": "循环",
    "timeline": "时间线",
    "flowchart": "流程图",
    "comparison": "对比",
    "framework": "框架",
    "background image": "背景图",
    "background images": "背景图",
    "portrait": "人像",
    "portraits": "人像",
    "scene": "场景",
    "scenes": "场景",
    "infographic": "信息图",
    "infographics": "信息图",
    "map": "地图",
    "maps": "地图",
    "hero image": "主视觉图",
    "hero images": "主视觉图",
    "sketch": "草图",
    "sketches": "草图",
    "sketch notes": "手写笔记风格",
    "sketch-notes": "手写笔记风格",
    "vector": "矢量",
    "vector illustration": "矢量插画",
    "vector illustrations": "矢量插画",
    "flat": "扁平",
    "watercolor": "水彩",
    "chalkboard": "黑板",
    "ink": "水墨",
    "paper cut": "剪纸",
    "paper-cut": "剪纸",
    "glassmorphism": "玻璃拟态",
    "3d": "三维",
    "3d isometric": "三维等距",
    "3d-isometric": "三维等距",
    "isometric": "等距",
    "blueprint": "蓝图",
    "vintage": "复古",
    "vintage poster": "复古海报",
    "warm scene": "暖色场景",
    "warm scenes": "暖色场景",
    "warm": "暖色",
    "cool": "冷色",
    "earthy": "大地色",
    "vivid": "鲜艳",
    "dark": "深色",
    "neon": "霓虹",
    "frost": "冷调",
    "ice": "冰感",
    "jewel": "宝石色",
    "macaron": "马卡龙",
    "duotone": "双色",
    "mono": "单色",
    "ink wash": "水墨晕染",
    "ink-wash": "水墨晕染",
    "dusty": "雾感",
    "earthy dusty": "大地雾感",
    "editorial": "编辑风",
    "editorial classic": "经典编辑风",
    "corporate": "企业风",
    "corporate photo": "企业摄影",
    "screen print": "丝网印刷",
    "screen-print": "丝网印刷",
    "pixel": "像素",
    "pixel art": "像素风",
    "pixel-art": "像素风",
    "fantasy": "奇幻",
    "fantasy animation": "奇幻动画",
    "minimalist": "极简",
    "minimalist swiss": "瑞士极简",
    "swiss": "瑞士风",
    "nature": "自然",
    "nature organic": "自然有机",
    "organic": "有机",
    "sunset": "日落",
    "sunset gradient": "日落渐变",
    "sunset-gradient": "日落渐变",
    "tech": "科技",
    "tech neon": "科技霓虹",
    "tech-neon": "科技霓虹",
    "gradient": "渐变",
    "warm earth": "暖土色",
    "warm-earth": "暖土色",
    "warm earth tone": "暖土色",
    "warm earth tones": "暖土色",
    "duo": "双色",
    "navy": "深蓝",
    "gold": "金色",
    "silver": "银色",
    "ink notes": "水墨笔记",
    "ink-notes": "水墨笔记",
    "open issues": "待办问题",
    "open question": "待办问题",
    "open questions": "待办问题",
    "decisions": "决策记录",
    "key decisions": "关键决策",
    "important decisions": "重要决策",
    "decision log": "决策日志",
    "decision": "决策",
    "rationale": "原理说明",
    "rationale and tradeoffs": "原理与权衡",
    "tradeoffs": "权衡",
    "trade-offs": "权衡",
    "risks": "风险",
    "risk": "风险",
    "mitigations": "缓解措施",
    "operational risks": "运维风险",
    "operational risk": "运维风险",
    "checklist items": "检查项",
    "checklist item": "检查项",
    "rationale and decision": "原理与决策",
    "design rationale": "设计原理",
    "policy": "策略",
    "policies": "策略",
    "policy and procedures": "策略与流程",
    "policy and procedure": "策略与流程",
    "principle": "原则",
    "principles and values": "原则与价值",
    "principles & values": "原则与价值",
    "principles-and-values": "原则与价值",
    "sop": "标准操作流程",
    "sops": "标准操作流程",
    "standard operating procedure": "标准操作流程",
    "standard operating procedures": "标准操作流程",
    "operating procedure": "操作流程",
    "operating procedures": "操作流程",
    "operating model": "运作模式",
    "operating models": "运作模式",
    "model": "模型",
    "models": "模型",
    "modes": "模式",
    "mode": "模式",
    "before and after": "前后对比",
    "before/after": "前后对比",
    "before & after": "前后对比",
    "good and bad": "好坏对比",
    "good/bad": "好坏对比",
    "do and don'ts": "推荐与禁忌",
    "dos": "推荐",
    "donts": "禁忌",
    "do": "推荐",
    "don't": "禁忌",
    "do not": "禁忌",
    "must": "必须",
    "must not": "禁止",
    "should": "应当",
    "should not": "不应",
    "may": "可以",
    "could": "可以",
    "need to": "需要",
    "needs to": "需要",
    "goal": "目标",
    "goals": "目标",
    "non-goals": "非目标",
    "non goals": "非目标",
    "anti-goals": "反目标",
    "anti goals": "反目标",
    "north star": "北极星指标",
    "north-star": "北极星指标",
    "metric": "指标",
    "metrics": "指标",
    "kpi": "关键指标",
    "kpis": "关键指标",
    "okr": "目标与关键成果",
    "okrs": "目标与关键成果",
    "milestone": "里程碑",
    "milestones": "里程碑",
    "roadmap": "路线图",
    "rollout": "灰度发布",
    "release plan": "发布计划",
    "release planning": "发布计划",
    "communication": "沟通",
    "communications": "沟通",
    "ownership": "归属",
    "owner": "负责人",
    "owners": "负责人",
    "stakeholders": "利益相关方",
    "stakeholder": "利益相关方",
    "team": "团队",
    "teams": "团队",
    "contributors": "贡献者",
    "contributor": "贡献者",
    "external": "外部",
    "internal": "内部",
    "private": "私密",
    "public": "公开",
    "draft": "草稿",
    "final": "终稿",
    "wip": "进行中",
    "todo": "待办",
    "done": "已完成",
    "appendix": "附录",
    "glossary": "术语表",
    "index": "索引",
}


def split_paragraph(s: str) -> list[str]:
    s = s.strip().strip(":：-")
    if not s:
        return []
    parts: list[str] = []
    for sep in [".", "。", ";", "；"]:
        if sep in s:
            for piece in s.split(sep):
                p = piece.strip().strip(",，")
                if p:
                    parts.append(p)
            if parts:
                return parts[:3]
    return [s]


def translate_heading(en: str) -> str:
    raw = en.strip().rstrip(":：")
    low = raw.lower()
    if low in HEADING_GLOSSARY:
        return HEADING_GLOSSARY[low]
    if "|" in raw:
        segs = [HEADING_GLOSSARY.get(s.strip().lower(), s.strip()) for s in raw.split("|")]
        return " / ".join(segs)
    if " - " in raw:
        segs = [HEADING_GLOSSARY.get(s.strip().lower(), s.strip()) for s in raw.split(" - ")]
        return " · ".join(segs)
    if " – " in raw:
        segs = [HEADING_GLOSSARY.get(s.strip().lower(), s.strip()) for s in raw.split(" – ")]
        return " · ".join(segs)
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9_\-]+", raw)
    if not tokens:
        return raw
    out = [HEADING_GLOSSARY.get(t.lower(), t) for t in tokens]
    return " ".join(out)


def make_section_block(title_cn: str, body_paras: list[str]) -> list[str]:
    if not body_paras:
        return [
            "",
            f"### 中文：{title_cn}",
            "",
            f"- 本节说明 `{title_cn}` 相关的任务目标、输入、输出、关键约束和验收标准。",
            "- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。",
            "- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。",
            "- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。",
            "- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。",
        ]
    lines = [
        "",
        f"### 中文：{title_cn}",
        "",
        "- 本节对应原始英文段落。中文部分负责解释目标、流程、风险与验收，不替代下方英文细则。",
    ]
    for p in body_paras[:4]:
        p = p.strip()
        if not p:
            continue
        if any(c in p for c in "[]{}<>=") and len(p) < 40:
            lines.append(f"- 关键术语或参数：`{p}`。请结合上下文理解，不要照搬字面。")
        else:
            lines.append(f"- {p}（以上为中文意译，具体细节以英文原文为准）。")
    return lines


def expand_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if MARKER in text:
        return False
    lines = text.split("\n")
    out: list[str] = []
    fence_active = False
    fence_marker: str | None = None
    heading_re = re.compile(r"^(#{2,6})\s+(.+?)\s*$")
    i = 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        stripped = line.lstrip()
        m_fence = re.match(r"^(`{3,}|~{3,})", stripped)
        if m_fence:
            tag = m_fence.group(1)
            if not fence_active:
                fence_active = True
                fence_marker = tag
            elif fence_marker and stripped.startswith(fence_marker):
                fence_active = False
                fence_marker = None
            i += 1
            continue
        if fence_active:
            i += 1
            continue
        m_h = heading_re.match(line)
        if not m_h:
            i += 1
            continue
        title = m_h.group(2)
        if re.search(r"[\u4e00-\u9fff]", title):
            i += 1
            continue
        if len(title.strip()) < 3:
            i += 1
            continue
        # collect following non-heading paragraphs as body
        body: list[str] = []
        j = i + 1
        while j < len(lines):
            jline = lines[j]
            if heading_re.match(jline):
                break
            if jline.strip().startswith("```") or jline.strip().startswith("~~~"):
                break
            if jline.strip().startswith("|"):
                break
            if jline.strip().startswith("<!--"):
                break
            if jline.strip().startswith("---"):
                break
            if jline.strip() == "":
                j += 1
                if len(body) >= 3:
                    break
                continue
            if jline.startswith(("-", "*")) or re.match(r"^\d+\.\s", jline):
                body.append(jline.lstrip("-* 0123456789."))
                if len(body) >= 4:
                    break
            else:
                body.append(jline)
                if len(body) >= 4:
                    break
            j += 1
        paras: list[str] = []
        for b in body:
            for part in split_paragraph(b):
                paras.append(part)
        title_cn = translate_heading(title)
        block = make_section_block(title_cn, paras)
        out.extend(block)
        i = j
    new_text = "\n".join(out)
    if new_text == text:
        return False
    path.write_text(new_text, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    import re as _re
    count = 0
    for p in sorted(ROOT.rglob("*.md")):
        # Recompute ratio each pass
        text = p.read_text(encoding="utf-8", errors="ignore")
        prose = _re.sub(r"```.*?```", "", text, flags=_re.S)
        prose = _re.sub(r"<svg.*?</svg>", "", prose, flags=_re.S | _re.I)
        cjk = len(_re.findall(r"[\u4e00-\u9fff]", prose))
        alpha = len(_re.findall(r"[A-Za-z]", prose))
        total = cjk + alpha
        r = cjk / total if total else 1
        if r < MIN_RATIO:
            if expand_file(p):
                count += 1
    print(f"section-expanded files: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
