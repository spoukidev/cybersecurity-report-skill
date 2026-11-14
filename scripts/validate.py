#!/usr/bin/env python3
"""Validate the skill package: SKILL.md frontmatter, referenced files and eval JSON.

Usage: python3 scripts/validate.py   (exits non-zero on any problem)
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        errors.append("SKILL.md: missing YAML frontmatter block")
        return {}
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')
    return fields


skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
meta = frontmatter(skill_text)
name = meta.get("name", "")
if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
    errors.append(f"SKILL.md: name {name!r} must be lowercase kebab-case")
description = meta.get("description", "")
if not description:
    errors.append("SKILL.md: description is required")
elif len(description) > 1024:
    errors.append(f"SKILL.md: description is {len(description)} chars (max 1024)")

for ref in sorted(set(re.findall(r"`((?:references|evals)/[^`]+)`", skill_text))):
    if not (ROOT / ref).is_file():
        errors.append(f"SKILL.md references missing file: {ref}")

for eval_file, required in (
    ("evals/evals.json", ("name", "input", "assertions")),
    ("evals/triggers.json", ("input", "should_trigger")),
):
    try:
        data = json.loads((ROOT / eval_file).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{eval_file}: {exc}")
        continue
    if data.get("skill") != name:
        errors.append(f"{eval_file}: skill {data.get('skill')!r} does not match SKILL.md name {name!r}")
    cases = data.get("test_cases")
    if not isinstance(cases, list) or not cases:
        errors.append(f"{eval_file}: test_cases must be a non-empty list")
        continue
    for index, case in enumerate(cases):
        missing = [key for key in required if key not in case]
        if missing:
            errors.append(f"{eval_file}: test_cases[{index}] missing {', '.join(missing)}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: skill {name!r} is valid")
