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
    bv_count = len(set(re.findall(r"BV[0-9A-Za-z]+", evidence)))
    assert bv_count >= 25, f"expected broad BV evidence coverage, got {bv_count}"

    source = (ROOT / "references" / "source-videos.md").read_text(encoding="utf-8")
    row_count = sum(1 for line in source.splitlines() if line.startswith("| ") and "`BV" in line)
    assert row_count == 40, f"source video index should contain 40 rows, got {row_count}"

    timestamped = (ROOT / "references" / "timestamped-evidence.md").read_text(encoding="utf-8")
    timestamp_rows = len(re.findall(r"BV[0-9A-Za-z]+.*\d{1,2}:\d{2}", timestamped))
    assert timestamp_rows >= 80, f"expected broad timestamped evidence coverage, got {timestamp_rows}"


    text_files = [p for p in ROOT.rglob("*") if p.is_file() and p.suffix.lower() in {".md", ".py", ".txt", ".yaml", ".yml", ".json"}]
    combined_text = "\n".join(p.read_text(encoding="utf-8") for p in text_files)
    searchable = combined_text.replace("fox-finance-methodology", "")
    bad_terms = ["fo" + "x", "狐" + "狸"]
    for term in bad_terms:
        idx = searchable.lower().find(term.lower())
        assert idx == -1, f"disallowed brand term remains near: {searchable[max(0, idx-40):idx+40] if idx >= 0 else ''}"
    rel_paths = "\n".join(str(p.relative_to(ROOT)) for p in ROOT.rglob("*"))
    rel_paths = rel_paths.replace("fox-finance-methodology", "")
    for term in bad_terms:
        idx = rel_paths.lower().find(term.lower())
        assert idx == -1, f"disallowed brand term remains in path near: {rel_paths[max(0, idx-40):idx+80] if idx >= 0 else ''}"

    print("ok skill validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
