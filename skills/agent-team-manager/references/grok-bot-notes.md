# Grok Bot mapping

Grok Bot (xAI, launched Aug 2026) is a system of persistent, named Bots. Each Bot has its own
cloud computer, memory, tools, skills and routines, keeps working when your device is off, and
signs into apps the way a person does. This file maps the manager skill to its concepts.

> Product details change fast. Treat this as a guide and confirm current behaviour in the
> official docs (docs.x.ai/grok-bot) before relying on a specific limit or setting.

| Manager concept | Grok Bot concept | How to use it |
|---|---|---|
| You (manager) | The pinned "Chief of Staff" Bot | Single entry point. Human messages you a goal; you route, verify, report. |
| Team member | A Bot | One narrow job per Bot. Its **description** drives delegation routing - write it as "what it owns + when to hand it work". |
| Brief / handoff | Chat message / @-mention | Hand off with a full Delegation Brief. @-mention to bring a Bot into a thread. |
| Visible collaboration | Group chat (2-6 Bots) | Use when the handoff itself needs to be visible. Name the owner in the first message. |
| Method | Skill (SKILL.md: name + description + instructions) | Save from a completed, successful task: sources, sequence, decision rules, validation, output format, approval points. |
| Recurring work | Routine (schedule or event trigger, e.g. Slack/GitHub/Teams message) | Only after the skill is reliable. One routine = one Bot + one skill + one trigger. |
| Autonomy levels | Approvals ("Ask first", Auto-review rules) | L0/L1 = Ask first; L2+ = Auto-review with rules. Enterprise team rules are inherited and "Ask first" wins conflicts. |
| Tools | Connectors, plugins, MCP servers, the Bot's computer | Prefer connectors/APIs over UI clicking for reliability and verifiability. |
| Evidence | Artifacts (docs, code, files) + activity view | Require artifact links in every report. |
| Audit | Activity history; Enterprise audit logs | Weekly transcript sampling; watch for silent failures. |

## Setup pattern

1. Start with **one** pinned Bot (you). Do real work together for a few days.
2. Brain-dump from the human: who they are, their work, recurring chores, tools, approval
   preferences. Propose a roster plan; get approval.
3. Create specialists one at a time, only per the "when to create a Bot" rules. Each gets a
   charter (`templates/bot-charter.md`) and one proven skill.
4. Add routines last.
5. Keep yourself as the only Bot the human needs to talk to day-to-day.

## Tips

- The main Grok Bot screen is a roster, designed for delegation over supervision - respect that:
  surface only what needs the human (approvals, decisions, blockers) and summarize the rest.
- When a Bot needs a human to take over its computer (login, CAPTCHA, 2FA), batch those
  requests and say exactly what to do.
- Credentials and sessions expire: add a lightweight daily health-check routine that verifies
  each critical connector/login and reports failures instead of letting Bots improvise.
- Portable: SKILL.md files also work in Grok Build (`.grok/skills/`, `~/.grok/skills/`,
  `.agents/skills/`) and other SKILL.md-compatible agents; Grok also accepts `.md`, `.zip` and
  `.skill` uploads.
