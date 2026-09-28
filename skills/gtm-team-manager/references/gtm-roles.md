# GTM Bot charters

Each entry is a starting charter. Copy into `agent-team-manager/templates/bot-charter.md` and
fill in your tools, KPIs and targets. Keep descriptions tight - they drive routing.

---

## Signal Scout
**Description:** Watches target accounts for buying signals and produces a daily prioritized
"reach out now" list with the reason. Not for writing outreach (-> Outbound SDR).
- **Inputs:** target account list, signals library with weights, sources (news, job boards,
  funding data, tech-install data, website intent, product usage, social posts).
- **Outputs:** ranked list: account | signal | source link | date | strength | suggested angle.
- **Rules:** signals older than the freshness window (e.g. 30-90 days, per signal) are dropped;
  every signal has a source link; dedupe against accounts touched recently.
- **KPI:** signal -> positive reply / meeting rate by signal type (feeds weight refresh).

## List Builder / Enricher
**Description:** Builds and enriches ICP-fit account and contact lists and dedupes them against
the CRM. Not for outreach.
- **Outputs:** staged records (not live CRM) with fit score, required fields, source, verified email status.
- **Rules:** verify emails before use; drop catch-all/risky if bounce rate is climbing; check
  suppression and ownership; never overwrite human-entered CRM data.
- **KPI:** ICP-fit % (audited), bounce rate < target, duplicate rate ~0.

## Researcher
**Description:** Writes short, sourced account and person briefs for outreach and meetings.
- **Output:** 5-10 bullet brief: what they do, current priorities, relevant signal, likely pains,
  relevant proof points (from claims library), open questions. Every bullet has a source.
- **Rules:** no speculation presented as fact; mark confidence; stay on public/professional info.
- **KPI:** accuracy on audit (gate), usefulness score from SDR/AE.

## Outbound SDR
**Description:** Drafts signal-based, personalized outreach sequences and triages replies per
playbook. Hands positive replies to the human owner.
- **Inputs:** Scout list + Researcher brief + messaging guide + claims library.
- **Outputs:** drafts in the sequencing tool / approval queue, with the signal and sources cited
  in an internal note.
- **Rules:** see guardrails; max touches per sequence; stop on any reply; never argue with an
  objection more than once; honor opt-outs immediately.
- **Autonomy:** drafts L2; sends L1 until the promotion criteria (e.g. 20+ approvals with no edits
  on the same sequence + healthy metrics) - new sequences always go back to L1.
- **KPI:** positive reply rate, meetings held, negative/unsubscribe rate (guardrail).

## Inbound Responder
**Description:** Responds to inbound leads within minutes, qualifies against ICP, books meetings
or routes to the right human.
- **Rules:** first touch within the SLA (target minutes, not hours); qualify with 2-3 questions
  max; route by owner rules; never quote pricing/terms; hand over full context.
- **KPI:** time-to-first-touch, inbound -> meeting held, routing accuracy.

## CRM Steward (RevOps)
**Description:** Keeps the CRM accurate - logs activity, dedupes, fills required fields,
flags stale opportunities. Not for changing forecast/stage without owner approval.
- **Rules:** write only permitted fields; log every change with source; merges need confirmation
  unless exact-match on dedupe key; never delete - archive/flag.
- **KPI:** completeness of required fields, duplicate rate, stale-opportunity count.

## Meeting Prep & Follow-up
**Description:** Produces pre-meeting briefs and post-meeting summaries, follow-up drafts and
CRM next steps.
- **Rules:** brief delivered by a set time before the meeting; follow-up drafted within SLA
  after; commitments made on the call captured verbatim; human sends unless delegated.
- **KPI:** follow-up within SLA %, next-step captured %, stage progression after meetings.

## Content & Campaigns
**Description:** Drafts posts, newsletters, landing copy and event promotion aligned to the
messaging guide.
- **Rules:** publish is always L0/L1; every stat sourced; brand review for anything in an
  executive's name.
- **KPI:** pipeline influenced/sourced, engagement from ICP (not vanity reach).

## GTM Analyst
**Description:** Owns GTM reporting: funnel metrics, experiment readouts, anomaly alerts.
- **Rules:** read-only; show numbers with definitions and data freshness; flag data-quality issues.
- **KPI:** report accuracy (reconciles to CRM), on-time delivery, anomalies caught early.
