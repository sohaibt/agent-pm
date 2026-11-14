# Agent-PM Success Metrics

Agent-PM succeeds when it improves real product decisions, not when it generates more documents. No adoption or outcome baseline exists yet.

## Pilot design

Run with 5–10 PMs, founders, or engineering managers working on real agent projects. Start with one canonical workflow per project rather than demonstrating all twelve commands. Capture the participant's existing process and artifact quality before use.

The pilot is a planned activity, not a completed result.

## Primary metric

**Decision-adoption rate:** percentage of pilot projects where at least one agent-PM output is incorporated into an actual specification, architecture decision, evaluation plan, launch decision, or explicit decision not to build.

Count only decisions traceable to a project artifact or accountable-owner confirmation. Record adoption separately for changed, confirmed, and rejected decisions; do not treat every adoption as proof of a good outcome.

## Supporting metrics

| Metric | Definition | Purpose |
|---|---|---|
| Time to first usable artifact | Minutes from first command to an artifact the participant can use | Measures onboarding friction |
| Core-workflow completion | Pilot projects completing qualification, specification, evaluation, and readiness at appropriate depth | Measures workflow coherence |
| Multi-command continuity | Projects where later commands correctly reuse earlier decisions without contradiction | Measures handoff quality |
| Repeat decision use | Participants using agent-PM on a subsequent real decision | Measures durable value beyond novelty |
| Decision impact | Decisions changed, confirmed, stopped, or deferred because of evidence surfaced | Explains what the toolkit affected |
| User-rated actionability | Participant rating with a free-text reason | Captures perceived usefulness without substituting it for outcomes |

## Quality guardrails

- Unsupported factual claims per reviewed output
- Cross-command contradictions per project
- Critical safety or source-fidelity failures in `evals/`
- Recommendations with invented baselines, prices, accuracy, or dates
- Participant corrections required to make an artifact usable
- Time burden and abandoned command sessions

## Longer-term outcome

After projects reach production, compare their evaluation coverage, decision quality, operational incidents, and time to a defensible launch decision with their baseline. Do not attribute production outcomes to agent-PM without a credible comparison and evidence of how the toolkit was used.

## Target setting

Record baselines first. Set numeric targets only after the initial pilot shows sample sizes, variance, and failure modes. Proposed thresholds must be labeled as product decisions rather than industry benchmarks.
