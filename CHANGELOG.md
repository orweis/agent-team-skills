# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow
[Semantic Versioning](https://semver.org/). Renaming or removing a `references/` or `templates/`
file, or a skill, is a breaking change and requires a major bump plus a migration note here.

## [1.1.0] - 2026-11-20

No breaking changes.

### Added
- Security principles in `agent-team-manager`: external content and other Bots' output are data,
  never instructions; no credentials in charters, briefs, memory or logs; least-privilege access
  and revocation on demotion; human approval required to grant more autonomy or relax guardrails.
- `scripts/validate.py` (stdlib-only) and a pytest suite validating frontmatter, links and
  referenced files; GitHub Actions CI with read-only permissions.
- CONTRIBUTING.md, SECURITY.md, .editorconfig, .gitignore.
- README: upgrade instructions, development and test section.
- Validator checks backticked `references/`, `templates/` and cross-skill paths in every skill
  Markdown file, and accepts quoted and folded frontmatter values.

### Fixed
- Meeting Prep Bot named consistently ("Meeting Prep & Follow-up") in `gtm-routines.md`.

## [1.0.0] - untagged baseline (commit b180981)

- Initial release: `agent-team-manager` and `gtm-team-manager` skills.
