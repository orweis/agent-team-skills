import importlib.util
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("validate", ROOT / "scripts" / "validate.py")
v = importlib.util.module_from_spec(spec)
sys.modules["validate"] = v
spec.loader.exec_module(v)


def make_skill(root: Path, name="demo", fm=None, body="# Demo\n"):
    d = root / "skills" / name
    d.mkdir(parents=True)
    fm = fm if fm is not None else f"---\nname: {name}\ndescription: A demo.\n---\n"
    (d / "SKILL.md").write_text(fm + body, encoding="utf-8")
    return d


def test_real_repo_is_clean():
    assert v.validate(ROOT) == []


def test_real_skills_present():
    names = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
    assert {"agent-team-manager", "gtm-team-manager"} <= names


def test_valid_minimal(tmp_path):
    make_skill(tmp_path)
    assert v.validate(tmp_path) == []


@pytest.mark.parametrize("fm,msg", [
    ("name: demo\n", "missing opening"),
    ("---\nname: demo\ndescription: x\n", "missing closing"),
    ("---\nname: demo\nbad line\n---\n", "malformed"),
    ("---\ndescription: x\n---\n", "missing 'name'"),
    ("---\nname: demo\n---\n", "missing 'description'"),
    ("---\nname: other\ndescription: x\n---\n", "!= directory"),
    ("---\nname: demo\ndescription: " + "x" * 1025 + "\n---\n", "max 1024"),
])
def test_frontmatter_errors(tmp_path, fm, msg):
    make_skill(tmp_path, fm=fm)
    assert any(msg in e for e in v.validate(tmp_path))


def test_description_at_limit_ok(tmp_path):
    make_skill(tmp_path, fm="---\nname: demo\ndescription: " + "x" * 1024 + "\n---\n")
    assert v.validate(tmp_path) == []


def test_invalid_name_chars(tmp_path):
    make_skill(tmp_path, name="Bad_Name", fm="---\nname: Bad_Name\ndescription: x\n---\n")
    assert any("invalid name" in e for e in v.validate(tmp_path))


def test_missing_skill_md(tmp_path):
    (tmp_path / "skills" / "empty").mkdir(parents=True)
    assert any("missing SKILL.md" in e for e in v.validate(tmp_path))


def test_no_skills_dir(tmp_path):
    assert v.validate(tmp_path)


def test_missing_reference_file(tmp_path):
    make_skill(tmp_path, body="See `references/nope.md`.\n")
    assert any("referenced file not found" in e for e in v.validate(tmp_path))


def test_reference_present(tmp_path):
    d = make_skill(tmp_path, body="See `references/a.md`.\n")
    (d / "references").mkdir()
    (d / "references" / "a.md").write_text("hi")
    assert v.validate(tmp_path) == []


def test_broken_relative_link(tmp_path):
    make_skill(tmp_path, body="[x](missing.md)\n")
    assert any("broken link" in e for e in v.validate(tmp_path))


def test_links_ignored_cases(tmp_path):
    body = "[a](https://example.com) [b](#anchor) [c](mailto:a@b.c)\n`[d](nope.md)`\n```\n[e](nope.md)\n```\n"
    make_skill(tmp_path, body=body)
    assert v.validate(tmp_path) == []


def test_link_with_anchor_resolves(tmp_path):
    d = make_skill(tmp_path, body="[x](other.md#sec)\n")
    (d / "other.md").write_text("# s")
    assert v.validate(tmp_path) == []


def test_link_escaping_repo(tmp_path):
    root = tmp_path / "repo"
    make_skill(root, body="[x](../../../outside.md)\n")
    (tmp_path / "outside.md").write_text("x")
    assert any("escapes repo" in e for e in v.validate(root))


def test_main_exit_codes(tmp_path, capsys):
    assert v.main(["validate", str(ROOT)]) == 0
    make_skill(tmp_path, body="[x](missing.md)\n")
    assert v.main(["validate", str(tmp_path)]) == 1


def test_bot_names_consistent_in_gtm_files():
    # Every routine owner must be a Bot in the SKILL.md roster table.
    gtm = ROOT / "skills" / "gtm-team-manager"
    skill = (gtm / "SKILL.md").read_text()
    roster = set(re.findall(r"^\| \*\*(.+?)\*\* \|", skill, re.M))
    assert roster
    text = (gtm / "references" / "gtm-routines.md").read_text()
    owners = re.findall(r"owner: (.+?) - trigger", text)
    assert owners
    for owner in owners:
        for name in re.split(r" or | \+ ", owner):
            name = name.strip()
            if name != "you":
                assert name in roster or any(r.startswith(name) for r in roster), name


def test_folded_and_quoted_frontmatter(tmp_path):
    make_skill(tmp_path)
    md = tmp_path / "skills" / "demo" / "SKILL.md"
    md.write_text('---\nname: demo\ndescription: >\n  line one\n  line two\n---\nbody\n')
    assert v.validate(tmp_path) == []
    md.write_text('---\nname: "demo"\ndescription: "quoted"\n---\nbody\n')
    assert v.validate(tmp_path) == []


def test_broken_ref_in_references_file_and_cross_skill(tmp_path):
    make_skill(tmp_path)
    ref = tmp_path / "skills" / "demo" / "references"
    ref.mkdir()
    (ref / "a.md").write_text("see `templates/nope.md`\n")
    assert any("nope.md" in e for e in v.validate(tmp_path))
    (ref / "a.md").write_text("see `other/templates/nope.md`\n")
    assert any("other/templates/nope.md" in e for e in v.validate(tmp_path))
