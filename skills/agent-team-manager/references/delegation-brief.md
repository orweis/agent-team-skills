# Delegation Brief - template & examples

A good brief lets a capable newcomer do the task without asking a single question.
Anthropic found that lead agents given short, vague task descriptions produced sub-agents that
duplicated each other's work, left gaps, or chased tangents. The fix was teaching the lead to
specify objective, output format, tool guidance and boundaries for every sub-task.

## Template

```
TO: <Bot>                     OWNER: <Bot accountable for the outcome>
DUE: <date/time + timezone>   PRIORITY: <P0 now / P1 today / P2 this week>

OBJECTIVE
<One sentence. The outcome, not the activity. "Produce X so that Y" >

WHY
<The bigger goal and the decision this informs. Lets the Bot make good judgment calls.>

CONTEXT
- <Facts it needs>
- <Links / records / files>
- <What has already been tried and what happened>
- <What other Bots are doing in parallel - so it doesn't overlap>

DONE MEANS (acceptance criteria - each must be checkable)
1. <...>
2. <...>

OUTPUT FORMAT
<Exact structure, fields, length, file type, destination (doc / CRM field / thread).>

SCOPE
IN:  <...>
OUT: <... explicitly excluded>

TOOLS & SOURCES (name connectors/accounts only; never paste credentials)
Use: <...>   Avoid: <...>   Source quality bar: <e.g. primary sources, < 12 months old>

EFFORT BUDGET / STOPPING RULE
<e.g. "max ~15 tool calls", "stop once 3 independent sources agree", "time-box 30 min">

APPROVAL GATES
<Actions that need my / the human's sign-off before execution. Default: anything external,
irreversible, or spending money.>

ESCALATE IF
<e.g. missing access, conflicting data, cost > $X, scope turns out 2x bigger, legal/PR risk>

REPORT BACK
<Format: status line, deliverable link, evidence, open questions, confidence level.>
```

## Bad vs good

**Bad:** "Research competitors for the pricing page."

**Good:**
```
OBJECTIVE: Produce a table of how 5 named competitors price their team tier, so the human can
decide our Q4 team-tier price.
CONTEXT: Competitors = A, B, C, D, E. Research Bot is separately covering feature comparison -
do NOT cover features.
DONE MEANS: (1) all 5 rows filled, (2) every price has a source URL captured within the last
30 days, (3) monthly and annual prices both listed or marked "not public", (4) note any usage
caps that change effective price.
OUTPUT FORMAT: Markdown table: vendor | tier | monthly | annual | caps | source | date checked.
Then 3 bullets of notable patterns. Max 200 words beyond the table.
TOOLS: public pricing pages, docs, archived pages. Avoid: third-party review sites for prices.
EFFORT: ~3 tool calls per vendor. If price is "contact sales", record it and move on.
APPROVAL GATES: none (read-only).
ESCALATE IF: a vendor's site blocks access or pricing looks region-specific.
REPORT BACK: table + patterns + confidence (high/med/low) per row.
```

## Parallel fan-out checklist

- [ ] Slices are mutually exclusive and collectively cover the goal
- [ ] Each Bot knows what the others cover
- [ ] Output formats are identical so you can merge them mechanically
- [ ] Each has its own stopping rule
- [ ] One Bot (or you) owns integration

## Handoff contract between Bots (pipelines / group chats)

When Bot A hands off to Bot B, A must pass:
1. The artifact (link/ID), not a paraphrase of it
2. What was done and what was not
3. Known issues / assumptions
4. What B is expected to produce and by when
5. Who owns the outcome from now on (explicit ownership transfer)
