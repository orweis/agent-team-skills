# GTM routines (skill-ready procedures)

Rule: run each manually until reliable -> save as a skill -> then schedule as a routine.
Each routine: one owner Bot, one trigger, one skill, one output destination, explicit approvals.

## R1. Daily health check - owner: CRM Steward or you - trigger: every weekday early
1. For each sending inbox/domain: yesterday's sends, bounce %, spam complaints, blocks, replies.
2. Check auth/logins/connectors for every GTM Bot (CRM, email, sequencer, LinkedIn, calendar).
3. Compare to thresholds (`outbound-guardrails.md`).
4. Output: green/amber/red per inbox + per Bot. Red -> pause affected sending and escalate with
   what happened, what's paused, recommended action.

## R2. Signal sweep - owner: Signal Scout - trigger: daily
1. Pull new signals for target accounts from each source.
2. Drop stale, low-weight, and suppressed/owned-and-active accounts.
3. Score (signal weight x fit x recency); keep top N (capacity-matched to what SDR + humans can
   actually work).
4. Output: ranked list with source links -> Researcher.

## R3. Research & draft - owners: Researcher -> Outbound SDR - trigger: new sweep list
1. Researcher: brief per account/contact, sourced.
2. SDR: draft using signal + brief + messaging guide; cite sources in internal note.
3. Checker (you or a checker Bot): rubric gates (fit, accuracy, compliance).
4. Output: approval queue, batched, with recommendation per item.

## R4. Reply triage - owner: Outbound SDR - trigger: new reply
| Reply type | Action |
|---|---|
| Positive / meeting interest | Route to human owner within SLA with full context; propose times if delegated |
| Referral ("talk to X") | Thank; draft to referred person for approval; log relationship |
| Objection (timing/budget/need) | One playbook response or schedule follow-up; never argue twice |
| Not interested / unsubscribe | Suppress everywhere now; polite close only if appropriate |
| Out of office | Pause and resume after return date |
| Angry / legal / sensitive | Suppress, do not reply, escalate to human immediately |
| Question about pricing/security/terms | Route to human |

## R5. Inbound speed-to-lead - owner: Inbound Responder - trigger: form/chat/demo request
1. Enrich + fit check (seconds).
2. Respond within SLA: acknowledge, 1-2 qualifying questions or direct booking link.
3. Route per ownership rules; log in CRM.
4. Non-fit: helpful resources, no hard sell; log.

## R6. Meeting prep - owner: Meeting Prep - trigger: meeting on calendar (e.g. 24h before)
Brief: attendees (role, background), account context, signals, open opportunities/history,
suggested agenda and discovery questions, relevant proof points. Delivered to the human owner.

## R7. Post-meeting follow-up - owner: Meeting Prep - trigger: meeting ends / notes available
Summary, decisions, commitments, next steps + dates -> CRM; follow-up email draft for approval.

## R8. Weekly GTM review - owner: GTM Analyst + you - trigger: weekly
Fill `templates/gtm-weekly-review.md`; sample 10-20 sent messages against the rubric; experiment
readouts; propose next week's experiments and fixes.

## R9. Monthly ICP & signal refresh - owner: GTM Analyst + you
Closed-won/lost analysis -> which segments, personas and signals actually converted -> propose
changes to ICP, signal weights, messaging guide, claims library -> human approves.
