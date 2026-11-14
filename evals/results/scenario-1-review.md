# Scenario 1 Live Evaluation

- Run date: 2026-11-14
- Claude Code: 2.1.325
- Model: CLI default; exact model not captured
- Initial unedited output: `scenario-1-initial-output.md`
- Scenario: `../prompt-scenarios.md` → Scenario 1

## Core assertions

| Assertion | Status | Evidence |
|---|---|---|
| Reject unnecessary multi-agent | PASS | Recommended Rung 1, deterministic retrieval plus one LLM call |
| Explain simpler alternative and upgrade evidence | PASS | Single call first; fixed account-data lookup could justify Rung 2 |
| Separate problem evidence from architecture | PASS | Named architecture-before-problem and unchecked demand |
| Preserve unknown baseline and volume | PASS | Marked ticket count, baseline, model, and price unknown |
| Avoid universal 4×/15× claims | PASS | Called 15× a rough guess from Anthropic's research system |

Core scenario assertions: 5/5 passed.

## Additional findings

| Finding | Severity | Evidence | Required correction |
|---|---|---|---|
| Misapplied source sample size | Critical | Recommended 50–100 total past tickets with `[S06]`; S06 recommends 50–100 failures among 200+ total for judge alignment, not this qualification sample | Defer dataset sizing to `eval-design` |
| Invented comparison ratio | Critical | Claimed a router plus three workers gives “4× the prompts and evals” without a calculation or evidence | Prohibit unsupported narrative ratios |
| Arbitrary elapsed-time upgrade trigger | Major | Proposed “after about 3 months” without evidence | Use observed decision triggers only |
| Unsupported value inference | Major | Inferred that 500 users cannot justify multi-agent economics | Do not infer task value or ticket volume from account count |
| Core workflow skipped | Major | Recommended `eval-design` before `agent-spec` | Recommend `agent-spec` when proceeding to build, or no command while gathering evidence |

Initial release gate: **Fail** despite all five scenario assertions passing, because the output rubric treats fabricated numbers and source misrepresentation as critical.

## Re-run

- Model: `sonnet` alias
- Unedited output: `scenario-1-rerun-output.md`
- Core scenario assertions: 5/5 passed
- Initial critical findings resolved: dataset sizing deferred to `eval-design`; no unsupported comparison ratio
- Initial major findings resolved: no elapsed-time trigger, no affordability inference from user count, and no command recommended until evidence exists, followed by `agent-spec`
- Additional critical findings: None identified
- Re-run release gate for this scenario: **Pass**

The rerun used an explicit `sonnet` alias while the initial run's model was not captured. This confirms the revised prompt passed on that model, but it is not a controlled before/after comparison or proof of consistency across models.
