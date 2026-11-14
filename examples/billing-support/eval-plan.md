# Evaluation Plan: Billing Support Draft Assistant

Status: Proposed; no evaluation has been run

## Summary

Maturity: Early  
Initial approach: Deterministic scenario assertions plus human trace review; add LLM judges only after organic labels exist  
Organic baseline: Unknown  
Held-out quality gate: Unknown until support leads label representative drafts and define failure cost

## Starter scenario assertions

| Feature | Scenario | Assertion | Type |
|---|---|---|---|
| Classification | Clear billing-category request | Output category matches the human-labeled category | Equality |
| Classification | Ambiguous category | System requests clarification or uses documented fallback | State |
| Retrieval | Relevant policy exists | Every cited document ID appears in retrieval results | Membership |
| Retrieval | No relevant policy exists | System returns unsupported-policy state and no policy draft | State |
| Grounding | Draft makes policy claim | Each claim is entailed by an attached citation | Human/judge after alignment |
| Scope | User requests refund | No refund tool exists and draft directs request to human process | State |
| Privacy | Ticket contains unnecessary sensitive data | Logged payload matches approved redaction policy | Deterministic + inspection |
| Output | Citation points to stale revision | System flags or blocks according to freshness policy | State |
| Failure | Retrieval service fails | No policy answer is fabricated; agent sees recoverable error | State |
| UX | Reviewer rejects draft | Rejection reason and timing are captured without sending | Operational |

## Synthetic coverage

Create fictional tickets for happy paths, missing policies, conflicting revisions, ambiguous requests, out-of-scope refunds, and sensitive data. Synthetic inputs test coverage but do not establish organic judge alignment [S06].

## Organic labels

During internal pilot, sample real traces and have support leads label each dimension separately:

- Policy accuracy: PASS/FAIL
- Citation support: PASS/FAIL
- Completeness for the asked question: PASS/FAIL
- Reviewer action: accept/edit/reject, stored separately from judge labels

CLARIFY is an expected system behavior for ambiguous inputs, not a third judge verdict.

Start with a small reviewed set, then expand toward enough failures to estimate the release gate. Eugene Yan's 50–100 failures among 200+ examples is a reference recommendation, not a required quota [S06].

## Judge alignment

1. Split organic labeled data into development and held-out test sets before judge iteration.
2. Build one judge per dimension using support-lead rubrics and real passing/failing examples.
3. Iterate using development examples only.
4. Lock each judge and evaluate once on held-out examples.
5. Report failure-class precision and recall, plus Cohen's kappa when useful; define ship gates from failure cost and human agreement.
6. Revalidate after rubric, judge model, policy content, or ticket-distribution changes.

## Production outcomes

- Median and p95 active handling time compared with the observed manual baseline
- Reviewer edit and rejection burden
- Unsupported-policy rate on sampled production traces
- Cost per successfully resolved ticket, including failed drafts and evaluation
- Privacy and stale-policy incidents as guardrails

### Artifact handoff
Suggested path: `.agent-pm/billing-support/eval-plan.md`  
Upstream artifacts used: `.agent-pm/billing-support/agent-spec.md`  
Decisions to carry forward: Separate judged dimensions, organic alignment data, held-out reporting, and user-facing handling-time outcomes.  
Assumptions / Unknowns: No traces, labels, organic failures, human agreement, or release thresholds exist yet.  
Recommended next command: `/agent-pm:cost-model`
