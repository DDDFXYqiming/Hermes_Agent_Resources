#!/usr/bin/env python3
"""Validate this skill package."""
from __future__ import annotations

import pathlib
import re
import sys

try:
    import yaml
except Exception as exc:  # pragma: no cover
    print(f"Missing PyYAML: {exc}", file=sys.stderr)
    sys.exit(2)

ROOT = pathlib.Path(__file__).resolve().parents[1]
REQUIRED = [
    ROOT / "SKILL.md",
    ROOT / "references" / "rulebook.md",
    ROOT / "references" / "evidence-map.md",
    ROOT / "references" / "source-videos.md",
    ROOT / "references" / "timestamped-evidence.md",
    ROOT / "templates" / "signal-card.md",
]
SENSITIVE_PATTERNS = [
    r"[A-Za-z]:\\",
    r"[A-Za-z]:/",
    r"/(?:c|d|e)/",
    r"Users[\\/]\d+",
    r"Desktop[\\/]books",
    r"BV[0-9A-Za-z]{6,}",
]


def main() -> int:
    missing = [str(p) for p in REQUIRED if not p.exists()]
    if missing:
        print("missing files:", missing, file=sys.stderr)
        return 1

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    assert skill.startswith("---"), "SKILL.md must start with frontmatter"
    m = re.search(r"\n---\s*\n", skill[3:])
    assert m, "frontmatter closing marker missing"
    fm = yaml.safe_load(skill[3 : m.start() + 3])
    assert fm["name"] == "fox-finance-methodology"
    assert "description" in fm and len(fm["description"]) <= 1024
    assert "not investment advice" in fm["description"].lower()

    rulebook = (ROOT / "references" / "rulebook.md").read_text(encoding="utf-8")
    for token in ["EMA144", "EMA288", "KDJ", "0.618", "成交量", "成交额", "回避/风险优先"]:
        assert token in rulebook, f"rulebook missing {token}"

    evidence = (ROOT / "references" / "evidence-map.md").read_text(encoding="utf-8")
    for token in ["趋势线", "斐波那契", "EMA", "KDJ", "成交量", "仓位"]:
        assert token in evidence, f"evidence map missing rule family: {token}"

    source = (ROOT / "references" / "source-videos.md").read_text(encoding="utf-8")
    assert "公开版不保存具体视频编号" in source

    timestamped = (ROOT / "references" / "timestamped-evidence.md").read_text(encoding="utf-8")
    for token in ["结构类规则", "指标类规则", "斐波那契", "输出要求"]:
        assert token in timestamped, f"rule evidence summary missing {token}"

    text_files = [
        p
        for p in ROOT.rglob("*")
        if p.is_file()
        and p.name != "validate_skill.py"
        and p.suffix.lower() in {".md", ".txt", ".yaml", ".yml", ".json"}
    ]
    combined_text = "\n".join(p.read_text(encoding="utf-8") for p in text_files)
    searchable = combined_text.replace("fox-finance-methodology", "")
    bad_terms = ["fo" + "x", "狐" + "狸"]
    for term in bad_terms:
        idx = searchable.lower().find(term.lower())
        assert idx == -1, f"disallowed brand term remains near: {searchable[max(0, idx-40):idx+40] if idx >= 0 else ''}"

    for pattern in SENSITIVE_PATTERNS:
        match = re.search(pattern, combined_text)
        assert not match, f"sensitive or over-detailed source pattern remains: {pattern}"

    print("ok skill validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
