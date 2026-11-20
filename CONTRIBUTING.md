# Contributing

1. Edit skills under `skills/<name>/`. Each needs a `SKILL.md` with `name` (equal to the directory
   name, lowercase-hyphen) and `description` (at most 1024 characters) frontmatter.
2. Run `python3 scripts/validate.py` and `python3 -m pytest -q`; both must pass.
3. Add a CHANGELOG entry. Renaming or removing referenced files is a breaking change (major bump
   and migration note).
4. Never include credentials, personal data, or unverifiable numbers without a source in
   `SOURCES.md`. Date time-sensitive claims.
