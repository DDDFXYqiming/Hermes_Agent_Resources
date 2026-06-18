#!/usr/bin/env python3
"""Validate ericwarn-dingning-pr-methodology skill package."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "SKILL.md",
    "references/rulebook.md",
    "references/evidence-map.md",
    "references/data-verification.md",
    "templates/pr-valuation-card.md",
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print("Missing files:", ", ".join(missing))
    sys.exit(1)

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
if not skill.startswith("---\n") or "\n---\n" not in skill[4:]:
    print("SKILL.md frontmatter missing or malformed")
    sys.exit(1)

m = re.search(r"description:\s*\"(.*?)\"", skill, re.S)
if not m:
    print("description not found")
    sys.exit(1)
if len(m.group(1)) > 1024:
    print("description too long")
    sys.exit(1)

for term in ["市赚率", "PR", "ROE", "股利支付率", "not investment advice"]:
    if term not in skill:
        print(f"SKILL.md missing term: {term}")
        sys.exit(1)

rulebook = (ROOT / "references/rulebook.md").read_text(encoding="utf-8")
for term in ["PR-01", "PR-02", "PR-03", "PR-04", "fox-finance-methodology"]:
    if term not in rulebook:
        print(f"rulebook missing term: {term}")
        sys.exit(1)

print("OK: ericwarn-dingning-pr-methodology skill package validated")
