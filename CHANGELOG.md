# Changelog

## 1.1.0 - 2026-11-14

### Fixed

- Corrected the risk audit so backup isolation cannot be interpreted as a launch blocker when isolation exists.
- Standardized the five-position autonomy model and high-risk approval policy across commands.
- Classified orchestrator-workers consistently as multi-agent and removed cost-multiplier double counting.
- Corrected Anthropic's tool-design result to a 40% decrease in task completion time in its research system, not a universal task-completion improvement.
- Replaced universal SaaStr staffing and correction-duration claims with deployment-specific context.
- Separated organic judge-alignment data from synthetic coverage and development data from held-out test data.
- Replaced unsupported readiness percentages and ready dates with evidence coverage and explicit assumptions.

### Added

- A shared operating contract for evidence labels, canonical policies, calculations, and artifact handoffs.
- A claim-level source map with URLs, dates, usage limits, and current pricing references.
- Canonical `.agent-pm/<project-slug>/` artifact ownership and command skip conditions.
- Prompt evaluation scenarios, an output rubric, a results template, and repository regression checks.
- A handcrafted end-to-end billing-support example with explicit assumptions and unknowns.
- Pilot success metrics and a scorecard for measuring real decision adoption.

### Changed

- Commands now reuse upstream decisions and recommend only applicable next commands instead of implying all twelve are mandatory.
- Cost models use current provider prices and itemized calls rather than a hardcoded model-tier price table.
- Contributor requirements now include source mapping and relevant evaluations.
