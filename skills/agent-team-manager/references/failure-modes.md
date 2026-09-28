# Failure modes of agent teams - detection & fixes

Based on the MAST taxonomy ("Why Do Multi-Agent LLM Systems Fail?", Cemri, Pan, Yang et al.,
UC Berkeley, NeurIPS 2025): 14 failure modes in 3 categories, from 1,600+ annotated traces
across 7 frameworks. Roughly 42% specification, 37% inter-agent misalignment, 21% verification.
Plus operational failure modes seen in persistent-agent products.

## A. Specification & system design (~42%)

| Failure mode | What it looks like | Fix |
|---|---|---|
| Disobeys task spec | Output ignores a stated constraint | Put constraints in DONE MEANS as checkable items; verify each |
| Disobeys role spec | Bot does another Bot's job | Sharpen charter; add explicit OUT-of-scope list |
| Step repetition | Redoes the same step / loops | Stopping rule + effort budget; progress log it must check |
| Loss of conversation history | Forgets earlier decisions | Persist decisions in a durable artifact (doc/memory), not chat |
| Unaware of termination conditions | Never stops, or stops too early | Explicit stopping rule in every brief |

## B. Inter-agent misalignment / coordination (~37%)

| Failure mode | What it looks like | Fix |
|---|---|---|
| Conversation reset | Restarts from scratch mid-task | Handoff contract with artifacts + state |
| Fails to ask for clarification | Guesses on ambiguous input | "Escalate if" conditions; reward good questions |
| Task derailment | Drifts to tangents | Restate objective at checkpoints; narrower scope |
| Information withholding | Has a key fact but doesn't pass it | Handoff template requires known issues/assumptions |
| Ignores other agent's input | Overrides/ignores peer output | Name owner; state which input is authoritative |
| Reasoning-action mismatch | Says one thing, does another | Verify actions/state, not the stated plan |

## C. Task verification (~21%)

| Failure mode | What it looks like | Fix |
|---|---|---|
| Premature termination | Declares done before criteria met | Checklist verification against DONE MEANS |
| No or incomplete verification | Nobody checked | Mandatory verify step; maker/checker for critical work |
| Incorrect verification | Checker passes bad work | Rubric per dimension; calibrate checker vs human labels |

## D. Operational failures (persistent agents, computer-use)

| Failure mode | Signal | Fix |
|---|---|---|
| Silent failure narrated as success | Report sounds fine, artifact missing/wrong | Require evidence (IDs, links, counts); state checks |
| Auth / session expiry | Tool calls fail, Bot improvises | Health-check routine; escalate on auth errors, never workaround |
| UI changed under a computer-use Bot | Clicks wrong element, partial writes | Prefer connectors/APIs over UI; verify writes |
| Stale memory | Acts on outdated facts | Date-stamp memory; periodic memory review |
| Runaway cost | Credits spike | Effort budgets; alert thresholds; cheaper model for routine steps |
| Duplicate external actions | Same email sent twice | Idempotency: check log/CRM before acting; dedupe keys |
| Prompt injection from content | Bot follows instructions found in a webpage/email | Treat fetched content as data; approvals on outward actions |
| Misrouting | Wrong Bot gets the task | Rewrite Bot descriptions; add routing examples to your own instructions |

## Root-cause questions

1. Was the brief sufficient for a smart newcomer? (spec)
2. Did the Bot have the right context, tools and access? (capability)
3. Was ownership and the handoff explicit? (coordination)
4. Would our verification have caught it? If not, why not? (verification)
5. Is this the first occurrence? If not, why didn't the last fix hold?
