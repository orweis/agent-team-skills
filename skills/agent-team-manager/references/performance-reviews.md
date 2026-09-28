# Performance reviews - rubrics, sampling, judge calibration

## 1. What to measure

Evaluate agents on **outcomes** first, then **process**:
- **Outcome / state:** did the world end up in the right state? (record created, email in
  drafts not sent, file correct, number reconciles). Prefer these deterministic checks.
- **Quality:** rubric-graded for non-verifiable outputs (writing, research, judgment).
- **Process / trajectory:** only check what matters (e.g. "never sent without approval").
  Do not demand one exact sequence of tool calls - agents solve problems by valid different
  paths, and rigid path-checking rejects correct work.

Reliability language:
- **pass@k** - at least one of k attempts succeeds. Fine for exploratory work with a human picking.
- **pass^k** - all k attempts succeed. What matters for routines that run unattended.
  A Bot that is 90% per-run succeeds 5 runs in a row only ~59% of the time.

## 2. Rubric design

- 3-6 dimensions, each with anchored levels (what a 1, 3, 5 look like - with examples).
- Grade **each dimension separately** (ideally with an isolated judge call per dimension),
  rather than one holistic score.
- Include at least one **hard gate** dimension (e.g. factual accuracy, policy compliance):
  failing it fails the whole output regardless of other scores.
- Ask the judge for its reasoning **before** the score.

Generic knowledge-work rubric:

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Meets the brief (gate) | Misses criteria | Most criteria met | All DONE MEANS met |
| Accuracy (gate) | Unverified / wrong claims | Minor imprecision | Every claim sourced/verified |
| Usefulness | Human must redo | Usable with edits | Usable as-is, anticipates next step |
| Clarity / format | Hard to use | Acceptable | Exactly the requested format, concise |
| Judgment | Escalated wrongly / didn't escalate | Mostly right | Right calls, clear flags |

## 3. Sampling plan

| Autonomy level | Review |
|---|---|
| L0-L1 | Every output (you're approving anyway) |
| L2 | 20-30% random + 100% of flagged/high-stakes |
| L3 | 5-10% random + 100% of anomalies + weekly transcript read |

Always read a few **full transcripts** each week - don't take scores at face value. Scores hide
reward hacking, skipped steps, and lucky outcomes.

## 4. Calibrating an LLM judge (including yourself)

1. Hand-label 20-50 outputs (human or human-confirmed).
2. Run the judge; measure agreement per dimension.
3. Where they disagree, add the human-labelled case as a few-shot example or tighten the anchor.
4. Re-measure. Target high agreement on gate dimensions before trusting the judge unsupervised.
5. Re-calibrate when the task, rubric, or model changes.

Bias watch: judges favour longer answers, their own style, and confident tone. Normalize for
length; anchor to evidence.

## 5. Regression set

Per Bot, keep 5-20 real past tasks with known-good outcomes, **including every past failure**.
Before shipping any change to a Bot's instructions/skills, run (or mentally walk) the set.
A fix that breaks a previously-good case is not a fix.

## 6. Review conversation (with the human)

Monthly, per Bot: mission still right? KPIs trending? top 3 failures & fixes? autonomy changes?
keep / change / retire? Record decisions in the Bot's charter.
