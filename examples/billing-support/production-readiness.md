# Production Readiness: Billing Support Draft Assistant

Readiness: Not ready  
Evidence coverage: 6/6 categories assessed; assessment does not mean passed  
Launch-blocking items remaining: 6  
Estimated ready date: Unknown until owners, remaining effort, and team capacity are known

## Category assessment

| Category | Status | Evidence and gap |
|---|---|---|
| Correction loop | Not started | No owner, reviewed traces, correction cadence, or quality gate exists |
| Operational ownership | Not started | No named agent-ops owner, escalation path, or runbook exists |
| Infrastructure | Partial in design | Read-only architecture is specified; deployment, checkpoint needs, environment separation, and secret controls are unverified |
| Observability | Partial in design | Metrics are named; dashboards, privacy review, traces, and alerts are unimplemented |
| Rollback and recovery | Not started | Disable path, recovery drill, RTO/RPO, and support fallback are unverified |
| Communications and support | Not started | Support training, failure messaging, and feedback ownership are missing |

## Launch blockers

1. Validate the user problem and current handling-time baseline.
2. Pass held-out groundedness, scope, privacy, and failure-behavior evaluations.
3. Assign operational and policy-content owners.
4. Implement privacy-approved traces, metrics, alerts, and correction workflow.
5. Test immediate disablement and manual support fallback.
6. Establish acceptable handling-time, reviewer-burden, privacy, and fully loaded cost outcomes in internal alpha.

## Recommended rollout

- **Offline evaluation:** Historical or synthetic tickets only; exit when critical deterministic checks pass and human rubrics are stable.
- **Internal alpha:** A small support-agent group reviews every draft; exit only after predefined quality and handling-time gates pass.
- **Expanded pilot:** Increase exposure gradually while monitoring unsupported drafts, correction burden, privacy, and cost.
- **General availability:** Unknown until operational evidence and owner sign-off exist.

## Failure drills

- Retrieval outage produces an unsupported state without fabricated policy.
- Stale policy content is detected and blocked or flagged.
- Sensitive ticket content follows the approved logging and retention policy.
- The disable path restores the manual workflow without losing tickets.
- An unsupported-draft alert reaches a named owner with a reproducible trace.

### Artifact handoff
Suggested path: `.agent-pm/billing-support/production-readiness.md`  
Upstream artifacts used: `.agent-pm/billing-support/agent-spec.md`, `.agent-pm/billing-support/eval-plan.md`, `.agent-pm/billing-support/cost-model.md`  
Decisions to carry forward: Not ready; no customer exposure until quality, operational, privacy, recovery, and outcome gates pass.  
Assumptions / Unknowns: All operational implementation evidence and a capacity-based ready date remain unknown.  
Recommended next command: `/agent-pm:risk-audit` if credentials or deployment access are introduced
