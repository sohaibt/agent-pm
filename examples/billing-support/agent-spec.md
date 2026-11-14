# Agent Product Spec: Billing Support Draft Assistant

Status: Illustrative draft with unresolved launch inputs  
Date: 2026-11-14

## 1. Agent identity

Agent name: Billing Support Draft Assistant  
One-line description: Drafts policy-grounded billing replies for support agents to review and send.  
Target user: SaaS support agents handling billing tickets  
Replaces / augments: Augments manual article search and drafting; does not replace the sender

## 2. User job

When I handle a billing question, I want a draft grounded in current policy, so I can respond accurately with less manual searching.

- **Painful current state:** Agents search articles and compose each response manually.
- **Desired future state:** Agents review a cited draft and correct unsupported content before sending.
- **Aha moment:** The first draft contains the correct policy citation and requires only minor edits.
- **Evidence gap:** Validate that search and drafting are meaningful sources of ticket effort.

## 3. Success criteria

All baselines are unknown; targets below are proposed pilot gates.

| Level | Metric | Proposed target | Rationale |
|---|---|---|---|
| Task success | Drafts with correct policy and citation on held-out cases | Set after baseline pilot; block on any fabricated policy | Measures correctness rather than acceptance alone |
| User experience | Median active handling time | Improve on observed manual baseline without increasing correction burden | Measures actual time saved |
| Business | Fully loaded cost per successfully resolved ticket | Below validated value of time saved | Prevents usage growth from hiding poor economics |

Kill criteria: fabricated policy, material privacy breach, no handling-time improvement, or reviewers routinely needing to rewrite drafts.

## 4. Scope and boundaries

In scope: billing-question classification, approved-article retrieval, cited drafting, and clarification when policy is missing.

Out of scope: refunds, account changes, sending replies, non-billing technical support, and policy invention.

Edge cases: ambiguous ticket, no article, conflicting articles, stale policy, sensitive customer data, and retrieval failure.

## 5. Behavior specification

1. Trigger: support agent opens the assistant on a billing ticket.
2. Inputs: minimum necessary ticket text and approved help-center content.
3. Processing: validate, classify, retrieve, draft, and run deterministic checks.
4. Tool calls: retrieval only; model cannot choose account or messaging tools.
5. Output: draft, citations, and any unsupported-question warning.
6. State: trace metadata and reviewer correction persist according to the approved privacy policy.

## 6. Tool definitions

| Tool | Purpose | Inputs | Outputs | Risk | Execution |
|---|---|---|---|---|---|
| `retrieve_billing_policy` | Returns approved passages for a category and query | Category, query, locale, maximum results | Passages with document ID, revision, and URL | Low | Server-side read-only |

No send, refund, customer-write, or shell tools exist in this design.

## 7. Model selection

Model is Unknown. Compare candidates on groundedness, citation correctness, reviewer edit burden, latency, and fully loaded cost. Do not infer suitability from model tier.

## 8. Autonomy and human review

Position 1: Suggestion. The support agent decides, edits if needed, and sends. There are no autonomous external actions.

Escalate when policy is absent or conflicting, the request is out of scope, sensitive data requires special handling, or deterministic checks fail.

## 9. Stopping conditions

Stop after a draft with valid citations, a clarification request, an unsupported-policy state, or a failed safety check. No iterative agent loop is present.

## 10. Eval plan

See `eval-plan.md` for scenario assertions and judge alignment. Production metrics include handling time, correction burden, unsupported-draft rate, and cost per resolved ticket.

## 11. Failure modes

| Failure | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Unsupported policy statement | Unknown | Incorrect customer guidance | Approved retrieval, citation checks, abstention |
| Wrong classification | Unknown | Wrong policy context | Fallback and reviewer correction |
| Stale article | Unknown | Outdated guidance | Revision metadata and content freshness owner |
| Sensitive data leakage | Unknown | Privacy harm | Minimization, access control, retention policy |

## 12. Cost and performance budget

Targets remain Unknown until baseline handling time, model choice, and observed tokens are available. See `cost-model.md` for formulas and missing inputs. Measure p50/p95 latency during pilot rather than inventing a budget.

## 13. Rollout plan

- **v0:** Offline historical-ticket evaluation; no customer exposure.
- **Internal alpha:** Small group of support agents; every draft reviewed; collect corrections and timing.
- **Expanded pilot:** Increase only if quality, privacy, handling-time, and cost gates pass.
- **General availability:** Requires operational readiness and documented rollback.

## 14. Open questions

1. Does retrieval and drafting account for enough manual effort to justify the feature?
2. Which approved content is authoritative when policies conflict?
3. What quality and correction-burden gates do support leads require?
4. What ticket and trace data may legally be retained?
5. Which model meets the same held-out quality gate at the lowest fully loaded cost?

### Artifact handoff
Suggested path: `.agent-pm/billing-support/agent-spec.md`  
Upstream artifacts used: `.agent-pm/billing-support/01-qualification.md`, `.agent-pm/billing-support/02-architecture.md`  
Decisions to carry forward: Read-only workflow, Position 1 autonomy, no sends or writes, held-out quality and handling-time outcomes.  
Assumptions / Unknowns: Baselines, model, prices, privacy constraints, and launch gates require owners and evidence.  
Recommended next command: `/agent-pm:eval-design`
