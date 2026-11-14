# Illustrative End-to-End Example: Billing Support Draft Assistant

This is a handcrafted example of the intended artifact flow, not a captured model run or evidence that the commands passed an evaluation.

The fictional input describes a five-person support team handling 400 billing tickets per week. Support agents currently search help-center articles and draft replies manually; the reported current average is eight minutes per ticket. A human sends every reply. The agent cannot issue refunds or modify customer accounts. The team has no quality baseline or selected model.

All facts above are **user-provided within the fictional brief**. All targets and design choices are **proposed** or **assumptions**, not observed results.

Artifact flow:

1. `01-qualification.md` rejects unnecessary autonomy.
2. `02-architecture.md` chooses a routing and prompt-chaining workflow.
3. `agent-spec.md` summarizes the product decision and links specialist work.
4. `eval-plan.md` defines an initial outcome and judge-alignment plan.
5. `cost-model.md` shows what remains unknown without model prices and observed tokens.
6. `production-readiness.md` blocks launch until evidence exists.
