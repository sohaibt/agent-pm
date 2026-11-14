# Cost Model: Billing Support Draft Assistant

Status: Inputs incomplete; dollar cost is Unknown

## Task profile

Architecture: One optional routing call plus one drafting call, with deterministic retrieval  
Volume input: 400 tickets/week in the fictional brief  
Model and current prices: Unknown  
Observed tokens, retries, cache behavior, and tool fees: Unknown

The optional router is included only if evaluation shows it is necessary. No agent or multi-agent multiplier is applied to itemized calls.

## Formula

For each call:

```text
call cost = input tokens × current input price
          + output tokens × current output price
          + cache writes × current cache-write price
          + cache reads × current cache-read price
```

For the product:

```text
cost per attempted draft = router cost, if used
                         + drafting cost
                         + retrieval/tool cost
                         + allocated evaluation and observability cost

cost per successful resolution = total period cost / successfully resolved tickets
```

Report monthly ranges from attempted tickets, not only accepted drafts. Include failed drafts, retries, reviewer time, and support overhead where material.

## Required inputs

- Exact model candidates and current prices from [S14] or [S15], with access date
- Representative input/output token distributions for router and drafting calls
- Router usage rate
- Retrieval and infrastructure fees
- Draft failure and retry rates
- Evaluation, observability, and human review cost
- Successfully resolved ticket count and validated value of time saved

## Unit economics

Gross cost and margin are Unknown. Do not claim savings from the fictional eight-minute average until the baseline is observed and reviewer time is included.

### Artifact handoff
Suggested path: `.agent-pm/billing-support/cost-model.md`  
Upstream artifacts used: `.agent-pm/billing-support/02-architecture.md`, `.agent-pm/billing-support/eval-plan.md`  
Decisions to carry forward: Bottom-up costs only; cost per successful resolution; human review included.  
Assumptions / Unknowns: Model, prices, tokens, failures, operational costs, and realized value are unknown.  
Recommended next command: `/agent-pm:prod-readiness`
