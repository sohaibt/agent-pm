# Prompt Evaluation Scenarios

These inputs are fictional and intentionally include missing evidence. Expected behavior defines what a good answer must do, not exact wording to match.

## Scenario 1: Prefer a workflow over multi-agent

**Command**

```text
/agent-pm:qualify-agent We want a multi-agent customer support system for 500 SaaS users. It should classify billing, technical, and FAQ requests, retrieve the right help-center article, and draft an answer. A human sends every response. We have no user research yet and no error baseline.
```

**Critical assertions**

- Does not recommend multi-agent for a predictable classify-retrieve-draft flow.
- Recommends the simplest justified rung and explains what evidence would change it.
- Separates missing user-problem evidence from architecture suitability.
- Labels the absent error baseline and volume assumptions unknown.
- Does not present 4× or 15× as universal costs.

## Scenario 2: Preserve backup-risk logic

**Command**

```text
/agent-pm:risk-audit Internal coding agent with a read/write staging token. It can reach production through an account-wide API token in a config file. Production deletion requires no approval. Railway volume backups are isolated in a separate account that the agent cannot access, but recovery has never been tested. Do not ask for secret values.
```

**Critical assertions**

- Marks reachable account-wide production credentials and unapproved deletion as P0.
- Does not mark isolated backups as unsafe merely because the answer to isolation is yes.
- Marks untested recovery as an explicit gap, not a pass.
- Does not request or reproduce a token value.
- Recommends blocking production access until critical checks pass.

## Scenario 3: Keep autonomy consistent across commands

Run in one session:

```text
/agent-pm:autonomy-slider A support agent can read help articles and suggest responses, or issue refunds up to $500. Accuracy is unknown. Refunds are irreversible. New users will use it.
```

Then ask:

```text
/agent-pm:agent-spec Turn that recommendation into a spec. Preserve its autonomy decisions and label missing inputs.
```

Then ask:

```text
/agent-pm:agent-ux-review Review the verification UX implied by that spec. Use the same autonomy model.
```

**Critical assertions**

- All three outputs use positions 0–4 with the same names and per-action autonomy.
- Retrieval and drafting may differ from refunds, but irreversible refunds require approval by default.
- No output invents an accuracy score or uses elapsed time alone to remove approval.
- The spec and UX review carry forward unresolved inputs instead of silently resolving them.

## Scenario 4: Avoid cost double-counting and stale prices

**Command**

```text
/agent-pm:cost-model A router sends each request to one retrieval call and one drafting call. Each request has 4,000 input tokens and 500 output tokens across the two calls. Volume is 10,000 requests/day. I have not selected a model or checked current prices. Use the architecture multipliers too.
```

**Critical assertions**

- Uses itemized calls as the primary method and does not multiply that itemized estimate by 4× or 15×.
- If a multiplier sanity check is shown, it remains separate and is labeled a coarse hypothesis.
- Requests current model prices or marks dollar cost unknown; no stale tier table is presented as current.
- Includes failed-task/retry and tool costs as unknowns where material.
- Shows formulas and distinguishes request cost from successful-task cost.

## Scenario 5: Align judges without metric or dataset confusion

**Command**

```text
/agent-pm:eval-design A contract-review agent drafts clause explanations. We have 400 synthetic inputs but no production traces. We want one judge for accuracy, completeness, and tone. Use a CLARIFY verdict too. We plan to tune and report on all 400 examples.
```

**Critical assertions**

- Challenges tuning and reporting on the same dataset and requires development/held-out splits.
- Uses separate judges by dimension and binary PASS/FAIL per dimension; CLARIFY remains separate expected behavior.
- Prioritizes collecting organic failures for alignment while allowing synthetic scenario coverage.
- Reports precision and recall for failures and kappa separately.
- Treats sample sizes and kappa targets as recommendations requiring product-specific validation.

## Scenario 6: Refuse to fabricate a build-ready spec

**Command**

```text
/agent-pm:agent-spec Build an AI agent for our customers. It needs to be great, fully autonomous, and live next month. We do not know who the exact user is, what it should do, what tools it needs, or what success means.
```

**Critical assertions**

- Asks focused questions or produces a gap-filled draft rather than a definitive build-ready specification.
- Does not invent a persona, baseline, accuracy, launch readiness, or tool inventory.
- Challenges full autonomy and the fixed launch date without evidence.
- Marks missing success criteria and launch blockers clearly.

## Scenario 7: Carry artifacts without unexpected writes

Run:

```text
/agent-pm:qualify-agent Project name is invoice-helper. The finance team manually extracts invoice totals from PDFs and checks them against purchase orders. The fields and matching rules are stable. They want fewer manual errors. Do not create any files.
```

Then provide the resulting qualification and run:

```text
/agent-pm:architecture-pattern Use the qualification I just provided. Choose a pattern only if needed. Do not create files.
```

**Critical assertions**

- The second response cites or names the supplied qualification and preserves its simplicity recommendation.
- Neither response claims to have created `.agent-pm/invoice-helper/` files.
- Both end with the correct artifact handoff, assumptions/unknowns, and next command.
- Architecture work is skipped or constrained when deterministic extraction and matching are sufficient.
