# Agent-PM Evaluations

Agent-PM has two evaluation layers:

1. **Repository checks** validate command registration, shared references, source IDs, canonical policies, and known regressions.
2. **Prompt evaluations** run the real slash commands against `prompt-scenarios.md` and grade their actual outputs with `output-rubric.md`.

Live results are in `results/`. Scenario 1 initially exposed source-fidelity and unsupported-number failures, then passed after prompt correction; Scenario 2 passed its safety assertions. The other scenarios have not been run. These limited runs are not full release coverage or proof of consistency across models. A scenario or illustrative example alone is not evidence that a command passed.

## Run repository checks

```bash
python3 -m unittest discover -s evals -p 'test_*.py'
```

## Run prompt evaluations

Run each scenario in a fresh local plugin session:

```bash
claude --plugin-dir ./agent-pm
```

Then invoke the commands exactly as written in the scenario. For cross-command scenarios, keep the same session and provide the specified upstream artifact. Record the model, date, command, full input, and unedited output in a copy of `results-template.md`.

Do not paste real credentials, customer conversations, or sensitive production data into an evaluation.

## Proposed release gate

A release candidate passes when:

- Repository checks pass.
- Every critical scenario assertion passes.
- No output contains an unsupported factual claim presented as evidence.
- Cross-command scenarios use the same architecture, autonomy, approval, evaluation, and readiness policies.
- Any failure is recorded with a minimal reproduction before the prompt is changed.

This is agent-PM's proposed quality gate, not a sourced industry threshold. Establish baseline pass rates before setting numeric improvement targets.
