#!/usr/bin/env python3
"""Print one version's section of CHANGELOG.md, for a GitHub release.

Usage: python3 scripts/release-notes.py 0.3.0
"""
import re
import sys
from pathlib import Path

if len(sys.argv) != 2:
    sys.exit(__doc__)
version = sys.argv[1].lstrip("v")
text = (Path(__file__).resolve().parent.parent / "CHANGELOG.md").read_text(encoding="utf-8")
match = re.search(rf"^## {re.escape(version)}\b[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
if not match:
    sys.exit(f"No CHANGELOG.md section for {version}")
print(match.group(1).strip())
