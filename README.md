# Agent Team Skills

Two [Agent Skills](https://agentskills.io) (SKILL.md format) for an AI agent that **manages
other AI agents**. Built primarily for **Grok Bot** (a "Chief of Staff" Bot running a roster of
specialist Bots), and portable to any SKILL.md-compatible runtime (Grok Build, Claude Code,
Codex, Cursor, and others).

| Skill | What it does |
|---|---|
| [`agent-team-manager`](skills/agent-team-manager/SKILL.md) | Manage any team of agents: roster design, delegation briefs, monitoring, verification, graduated autonomy, scorecards, failure analysis, and a continuous improvement loop that upgrades each agent's instructions, skills and routines. |
| [`gtm-team-manager`](skills/gtm-team-manager/SKILL.md) | Manage a go-to-market agent team (signal scouting, research, list building, outbound SDR, inbound speed-to-lead, CRM hygiene, meeting prep, content, analytics) with GTM foundations, guardrails, metrics, experiments and operating cadence. Builds on `agent-team-manager`. |

## Layout

```
skills/
  agent-team-manager/
    SKILL.md
    references/  delegation-brief.md, failure-modes.md, performance-reviews.md, grok-bot-notes.md
    templates/   bot-charter.md, weekly-team-review.md
  gtm-team-manager/
    SKILL.md
    references/  gtm-roles.md, gtm-routines.md, outbound-guardrails.md, metrics-and-experiments.md
    templates/   gtm-foundation-brief.md, gtm-weekly-review.md
```

## Install

**Grok Bot:** zip each skill folder (e.g. `agent-team-manager/`) and upload it to your manager
Bot's skills (Grok accepts `.zip`, `.skill`, and `.md`). Give the GTM skill to the same manager
Bot. Specialist Bots get their own narrow skills (see `gtm-team-manager/references/gtm-roles.md`).

**Grok Build:** copy the folders into `.grok/skills/` (project) or `~/.grok/skills/` (global).
Grok also scans `.agents/skills/`.

**Claude Code / others:** copy into `.claude/skills/` (or the runtime's skills directory).

```bash
# Read the SKILL.md files before installing: skills are instructions your agent will follow,
# so treat updates like code. Optionally pin to a commit (git checkout <sha>) once reviewed.
git clone --depth 1 https://github.com/orweis/agent-team-skills
mkdir -p ~/.grok/skills
cp -r agent-team-skills/skills/* ~/.grok/skills/   # fresh install; overwrites same-named files
```

To upgrade, remove the old copy of each skill first so no stale files linger
(`rm -rf ~/.grok/skills/agent-team-manager ~/.grok/skills/gtm-team-manager`), then copy again.

For Claude Code use `~/.claude/skills/` (or `.claude/skills/` in a project) instead.

## Development and tests

No dependencies are needed to validate the skills (Python 3.10+ standard library):

```bash
python3 scripts/validate.py      # frontmatter, name/description limits, links, referenced files
python3 -m pip install pytest && python3 -m pytest -q   # test suite for the validator
```

CI runs both on every push and pull request. See [CONTRIBUTING.md](CONTRIBUTING.md) and
[SECURITY.md](SECURITY.md). Version history: [CHANGELOG.md](CHANGELOG.md).

## Getting started (Grok Bot)

1. Install both skills on one pinned Bot - your Chief of Staff.
2. Tell it about you, your work, your tools and your approval preferences; ask it to propose a
   roster using `agent-team-manager`. Approve the plan.
3. For GTM: fill in `templates/gtm-foundation-brief.md` with it (ICP, personas, signals,
   approved claims, voice, routing, CRM rules, sending policy) before any outbound Bot sends.
4. Start with 2-3 specialist Bots at low autonomy; promote on track record.
5. Ask for the weekly review every week. The improvement loop is where the value compounds.

## Design principles (from the research)

- Most multi-agent failures are **specification (~42%), coordination (~37%) and verification
  (~21%)** problems, not model problems -> precise briefs, explicit ownership, mandatory checks.
- A lead agent should **delegate like a PM**: objective, output format, tools, boundaries,
  stopping rule.
- **Trust artifacts, not narratives**; read transcripts, don't just trust scores.
- **Bounded autonomy**: permissions per action, approvals, audit, human escalation paths.
- **Do it once -> make it reliable -> save as a skill -> then automate as a routine.**
- In GTM: **signal-based, context-aware** outreach that knows when *not* to reach out beats volume.

Full source list: [SOURCES.md](SOURCES.md).

Note: product-specific details (Grok Bot features, outbound-email thresholds, legal summaries) change
over time; treat them as dated guidance and confirm against current vendor docs and counsel.

## License

MIT
