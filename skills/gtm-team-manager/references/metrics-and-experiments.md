# Metrics & experiments

## 1. Funnel math (work backwards from the target)

```
Revenue target
 / win rate                      -> opportunities needed
 / meeting->opportunity rate      -> meetings held needed
 / show rate                      -> meetings booked needed
 / positive-reply->meeting rate   -> positive replies needed
 / positive reply rate            -> contacts to reach
 / contacts per account           -> accounts to work
```
Use your own trailing 90-day rates. This tells you whether the plan is a volume problem
(need more accounts/signals) or a conversion problem (need better targeting/messaging) - and
most of the time it's conversion.

## 2. Definitions (write them down; Bots must use the same ones)

- **Positive reply:** expresses interest, asks for info/meeting, or refers to the right person.
  Excludes OOO, unsubscribes, "not interested".
- **Meeting held:** occurred with an ICP-fit decision-maker or influencer (not just booked).
- **Qualified opportunity:** meets your qualification framework and is accepted by an AE.
- **Sourced vs influenced pipeline:** decide attribution rules once; don't let Bots invent them.

## 3. Directional benchmarks (2026, vendor-reported - high variance)

| Metric | Typical | Strong |
|---|---|---|
| Cold email reply rate (all replies) | ~3-4% | ~5-6%+ |
| Positive reply rate, B2B tech | ~2-3.5% | ~4-6% |
| Intent/signal-triggered sequences | | high single to low double digits after tuning |
| Inbound first touch | hours (common) | minutes (target) |

Known pattern: AI-sourced meetings have tended to convert to opportunities less often than
human-sourced ones - track meeting -> opportunity per source and fix targeting/qualification,
don't just add volume. Treat all external benchmarks as sanity checks; your baseline is the bar.

## 4. Experiment design

- **One variable per test.** Candidates, roughly in order of typical impact: targeting/segment
  -> signal/trigger used -> angle/problem framed -> CTA -> length -> subject line -> timing.
- **Randomize** assignment at the contact (or account) level; keep inbox/domain mix equal.
- **Sample size:** at a ~3% positive reply rate (95% confidence, 80% power), detecting a lift to
  5% needs ~1,500 sends per arm; detecting a doubling to 6% needs ~750 per arm. If you can't reach that, test bolder changes, pool across weeks, or read replies
  qualitatively and label them "directional".
- **Pre-register** hypothesis, metric, sample size and stop date. No early stopping on a
  lucky day.
- **Success metric:** positive replies -> meetings held -> opportunities. Watch guardrail metrics
  (unsubscribe, complaints, negative replies) - a "win" that raises complaints is a loss.
- **Record everything** in an experiment log:
  `id | hypothesis | variable | arms | segment | n per arm | dates | result | decision | skill updated?`

## 5. Diagnosing a drop

| Symptom | Check first |
|---|---|
| Replies fell everywhere | Deliverability (placement, blocklists, auth), sending pattern changes |
| Replies fell in one segment | List quality, signal freshness, message-market fit |
| Replies OK, meetings low | CTA, reply-handling speed, handoff to humans |
| Meetings OK, opportunities low | ICP fit, qualification, who is attending |
| Bounces up | Enrichment source, email verification step |
| Negative replies up | Targeting, frequency, tone, relevance - pause and audit samples |
