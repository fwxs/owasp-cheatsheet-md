#!/usr/bin/env python3
"""Validate structural integrity of the owasp-cheatsheet-md skill collection.

Checks (stdlib only):
  1. Every SKILL.md (root + each category) has valid frontmatter: name
     (lowercase/hyphen, <=64 chars, no reserved words) and a non-empty
     description <=1024 chars.
  2. Every category directory listed in the root SKILL.md's category table
     has its own SKILL.md and a resources/ folder.
  3. Every `resources/*.md` path listed in a category's SKILL.md exists on
     disk, and every file physically present in that category's resources/
     is listed in its SKILL.md (drift is caught in both directions).
  4. All Python scripts compile.

Exit code 0 = pass, 1 = failure. Intended for CI and pre-commit use.
"""
import glob
import py_compile
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []


def check(cond, msg):
    if not cond:
        errors.append(msg)


def parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    check(fm is not None, f"{path.relative_to(ROOT)}: missing YAML frontmatter")
    if not fm:
        return
    name = re.search(r"^name:\s*(.+)$", fm.group(1), re.M)
    desc = re.search(r"^description:\s*(.+)$", fm.group(1), re.M)
    check(name is not None, f"{path.relative_to(ROOT)}: missing name")
    check(desc is not None, f"{path.relative_to(ROOT)}: missing description")
    if name:
        n = name.group(1).strip()
        check(re.fullmatch(r"[a-z0-9-]{1,64}", n) is not None,
              f"{path.relative_to(ROOT)}: name '{n}' must be lowercase/hyphen, <=64 chars")
        check("claude" not in n and "anthropic" not in n,
              f"{path.relative_to(ROOT)}: name contains a reserved word")
    if desc:
        d = desc.group(1).strip()
        check(0 < len(d) <= 1024,
              f"{path.relative_to(ROOT)}: description length {len(d)} not in 1..1024")


# 1. Root SKILL.md frontmatter
root_skill_path = ROOT / "SKILL.md"
check(root_skill_path.exists(), "missing root SKILL.md")
if root_skill_path.exists():
    parse_frontmatter(root_skill_path)
    root_skill = root_skill_path.read_text(encoding="utf-8")

    # 2. Category directories referenced in the root routing table
    categories = sorted(set(re.findall(r"\[(\w[\w]*)\]\(\1/SKILL\.md\)", root_skill)))
    check(len(categories) > 0, "root SKILL.md: no category links found in routing table")

    for cat in categories:
        cat_dir = ROOT / cat
        cat_skill = cat_dir / "SKILL.md"
        cat_resources = cat_dir / "resources"
        check(cat_skill.exists(), f"{cat}: missing SKILL.md")
        check(cat_resources.is_dir(), f"{cat}: missing resources/ directory")
        if not cat_skill.exists() or not cat_resources.is_dir():
            continue

        # 3. Category SKILL.md frontmatter
        parse_frontmatter(cat_skill)

        # 4. Resources listed vs. resources present, both directions
        cat_skill_text = cat_skill.read_text(encoding="utf-8")
        listed = set(re.findall(r"resources/([\w.\-]+\.md)", cat_skill_text))
        present = {p.name for p in cat_resources.glob("*.md")}

        check(listed == present,
              f"{cat}: SKILL.md resources list does not match resources/ contents "
              f"(listed but missing on disk: {sorted(listed - present)}; "
              f"on disk but not listed: {sorted(present - listed)})")

# 5. Scripts compile
for s in glob.glob(str(ROOT / "scripts" / "*.py")):
    try:
        py_compile.compile(s, doraise=True)
    except py_compile.PyCompileError as e:
        errors.append(f"script does not compile: {Path(s).name}: {e}")

if errors:
    print("VALIDATION FAILED:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print(f"OK: {len(categories)} category skills validated, frontmatter valid, "
      "resources match, scripts compile.")
sys.exit(0)
