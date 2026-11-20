#!/usr/bin/env python3
"""Validate the skills in this repo: frontmatter, relative links, referenced paths.

Stdlib only. Usage: python3 scripts/validate.py [repo_root]
Exit code 0 when clean, 1 when problems are found.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_DESC = 1024
MAX_NAME = 64
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
REF_RE = re.compile(r"`((?:[a-z0-9-]+/)?(?:references|templates)/[A-Za-z0-9_./-]+\.md)`")
FENCE_RE = re.compile(r"^(```|~~~)")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str | None]:
    """Return (fields, error). Handles `key: value` scalars, quotes and indented continuations."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, "missing opening '---' frontmatter delimiter"
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            fields: dict[str, str] = {}
            key = None
            for line in lines[1:i]:
                if not line.strip():
                    continue
                if line[0] in " \t" and key:  # indented continuation of previous value
                    fields[key] = (fields[key] + " " + line.strip()).strip()
                    continue
                if ":" not in line:
                    return {}, f"malformed frontmatter line: {line!r}"
                k, v = line.split(":", 1)
                key, v = k.strip(), v.strip()
                if v in (">", "|", ">-", "|-", ">+", "|+"):
                    v = ""  # block scalar: value follows on indented lines
                elif len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                    v = v[1:-1]
                fields[key] = v
            return fields, None
    return {}, "missing closing '---' frontmatter delimiter"


def strip_code(text: str) -> str:
    """Drop fenced code blocks and inline code so links in examples are ignored."""
    out, in_fence = [], False
    for line in text.splitlines():
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append(re.sub(r"`[^`]*`", "", line))
    return "\n".join(out)


def check_links(md: Path, root: Path) -> list[str]:
    errs = []
    for target in LINK_RE.findall(strip_code(md.read_text(encoding="utf-8"))):
        if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("#"):
            continue
        path = target.split("#", 1)[0]
        if not path:
            continue
        resolved = (md.parent / path).resolve()
        if not resolved.is_relative_to(root.resolve()):
            errs.append(f"{md}: link escapes repo: {target}")
        elif not resolved.exists():
            errs.append(f"{md}: broken link: {target}")
    return errs


def check_skill(skill_dir: Path, root: Path) -> list[str]:
    errs = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return [f"{skill_dir}: missing SKILL.md"]
    text = skill_md.read_text(encoding="utf-8")
    fields, err = parse_frontmatter(text)
    if err:
        return [f"{skill_md}: {err}"]
    name, desc = fields.get("name", ""), fields.get("description", "")
    if not name:
        errs.append(f"{skill_md}: missing 'name'")
    else:
        if name != skill_dir.name:
            errs.append(f"{skill_md}: name {name!r} != directory {skill_dir.name!r}")
        if len(name) > MAX_NAME or not NAME_RE.match(name):
            errs.append(f"{skill_md}: invalid name {name!r}")
    if not desc:
        errs.append(f"{skill_md}: missing 'description'")
    elif len(desc) > MAX_DESC:
        errs.append(f"{skill_md}: description is {len(desc)} chars (max {MAX_DESC})")
    for md in sorted(skill_dir.rglob("*.md")):
        for ref in sorted(set(REF_RE.findall(md.read_text(encoding="utf-8")))):
            # `<skill>/references/x.md` resolves against skills/; bare paths against this skill.
            first = ref.split("/", 1)[0]
            base = root / "skills" if first not in ("references", "templates") else skill_dir
            if not (base / ref).is_file():
                errs.append(f"{md}: referenced file not found: {ref}")
        errs.extend(check_links(md, root))
    return errs


def validate(root: Path) -> list[str]:
    skills_dir = root / "skills"
    if not skills_dir.is_dir():
        return [f"{root}: no skills/ directory"]
    dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir())
    if not dirs:
        return [f"{skills_dir}: no skills found"]
    errs = []
    for d in dirs:
        errs.extend(check_skill(d, root))
    for md in (root / "README.md", root / "SOURCES.md", root / "CHANGELOG.md"):
        if md.is_file():
            errs.extend(check_links(md, root))
    return errs


def main(argv: list[str]) -> int:
    root = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parent.parent
    errs = validate(root)
    for e in errs:
        print(e, file=sys.stderr)
    print(f"{len(errs)} problem(s)" if errs else "OK")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
