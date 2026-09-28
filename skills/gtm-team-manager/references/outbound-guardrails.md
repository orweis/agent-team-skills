# Outbound guardrails

These protect the company's domains, reputation and legal standing. Bots never waive them;
only a human can change them, in writing.

## 1. Deliverability

Conservative defaults (tune with your deliverability provider; industry guidance as of 2026):

| Control | Default |
|---|---|
| Sending domains | Use secondary domains for cold outbound; never the primary corporate domain |
| Authentication | SPF, DKIM, DMARC set and passing on every sending domain |
| Warm-up | New inboxes warmed for several weeks before cold volume; ramp gradually |
| Cold sends per inbox per day | Start ~30-50; well-warmed, healthy inboxes may go higher (~80-100 is widely cited as a ceiling); spread across inboxes/domains instead of pushing one |
| Bounce rate | Keep < ~2%; pause the list/inbox above it and fix data |
| Spam complaint rate | Aim < 0.1%; never approach 0.3% (major mailbox-provider bulk-sender threshold) |
| One-click unsubscribe / opt-out | Present and honored promptly as required |
| Sending pattern | Business hours in recipient timezone; randomized intervals; no sudden volume spikes |
| Content | Plain text-ish, few links, no attachments on first touch, no link shorteners |

Automatic pause triggers: bounce or complaint above threshold, blocklist hit, sudden drop in
reply/placement, auth failure. Pausing is always allowed without approval; resuming needs you.

## 2. Targeting

- Only contacts that pass ICP fit and have a reason-to-reach-now (signal).
- Suppression list checked at draft time **and** at send time.
- Account-level coordination: max N people per account at a time; no touching an account with an
  open opportunity or active conversation without the owner's approval.
- Cool-down between sequences to the same person (e.g. 90+ days).

## 3. Content integrity

- Claims only from the approved claims library, with sources.
- Personalization only from sourced facts; no invented familiarity or fake "re:"/"fwd:" tricks.
- No misleading subject lines, no fake urgency, no impersonation.
- AI disclosure: follow company policy and applicable law.

## 4. Compliance (not legal advice - confirm with counsel)

- **US (CAN-SPAM):** accurate headers/subject, identify as ad where applicable, physical address,
  working opt-out honored promptly.
- **EU/UK (GDPR, PECR):** lawful basis (commonly legitimate interest for B2B, with an assessment);
  transparency about data source on request; honor objections and erasure requests; mind stricter
  rules for sole traders / personal addresses in some countries.
- **Canada (CASL):** consent requirements are stricter; treat as opt-in unless an exemption clearly applies.
- **Platforms:** respect LinkedIn and other platforms' terms and rate limits; account restrictions are
  a red flag to stop, not a puzzle to work around.
- Data retention: don't keep enrichment data longer than needed; log sources.

## 5. Approval matrix (default)

| Action | Level |
|---|---|
| Research, briefs, list staging, drafts | L2 |
| First send of a new sequence / segment / persona / claim / sender | L1 (Ask first) - always |
| Sends of a proven sequence to a proven segment | L1 -> L2 after promotion criteria |
| Replies to positive responses | L1 (or route to human) |
| Anything to existing customers, execs of strategic accounts, press, partners | Human |
| CRM writes to permitted fields | L2 |
| CRM merges/deletes, stage/forecast changes | L1 |
| Publishing content in a person's or company's name | L1 |
| Spend (tools, data, ads) | Human |
