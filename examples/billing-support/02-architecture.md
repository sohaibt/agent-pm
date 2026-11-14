# Architecture: Billing Support Draft Assistant

## Recommended pattern

Primary pattern: Routing plus prompt chaining  
System level: Workflow, not an agent  
Confidence: Medium

```text
Billing ticket
  ↓
[Deterministic validation and policy checks]
  ↓
[Router: billing category or clarify]
  ↓
[Deterministic retrieval from approved help center]
  ↓
[Draft call: ticket + selected articles + category policy]
  ↓
[Deterministic citation and response checks]
  ↓
Human reviews, edits, and sends
```

## Why this fits

Categories may require different policy context, while retrieval and drafting have a fixed sequence. The model does not need to choose its own process or tools. The architecture preserves human authority and keeps retrieval and account permissions outside model control.

## Alternatives considered

- **Single retrieval-augmented call:** Preferred first prototype if category-specific behavior is unnecessary.
- **Agent:** Rejected because the steps are predictable and no dynamic investigation is specified.
- **Multi-agent:** Rejected because there are no independent workstreams or context-scale requirements.

## Implementation decisions

| Decision | Recommendation | Evidence status |
|---|---|---|
| Router | Start with deterministic categories; add a model router only if needed | Assumption |
| Models | Unknown; compare candidates on the same eval set | Unknown |
| Context | Pass only selected article excerpts and required ticket fields | Proposed |
| Stopping | One classification and one drafting call per prototype; no agent loop | Proposed |
| Errors | Return a clarification or unsupported-article state; never invent policy | Proposed |
| Logging | Store structured outcome and trace metadata with sensitive content excluded by policy | Proposed |

## Failure modes

| Failure | Early signal | Mitigation |
|---|---|---|
| Wrong category | Category disagreement in sampled traces | Fallback category plus human correction |
| Unsupported draft | Citation assertion or judge failure | Draft only from retrieved policy; abstain when absent |
| Sensitive data exposure | Privacy test failure or log inspection | Input minimization, access control, redaction, retention limits |

## Cost profile

Use one router only when evaluation justifies it, plus one drafting call. Measure actual input and output tokens. Do not add the generic 4× or 15× multipliers to this itemized design [S03].

### Artifact handoff
Suggested path: `.agent-pm/billing-support/02-architecture.md`  
Upstream artifacts used: `.agent-pm/billing-support/01-qualification.md`  
Decisions to carry forward: Fixed routing-retrieval-drafting workflow; deterministic permissions; human sends; agent and multi-agent rejected.  
Assumptions / Unknowns: Whether a separate router improves quality is untested; models and latency are unknown.  
Recommended next command: `/agent-pm:agent-spec`
