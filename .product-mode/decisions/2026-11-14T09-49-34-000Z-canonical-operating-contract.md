## Decision: Canonical operating contract and artifact workflow
Date: 2026-11-14
Context: The product review found contradictory autonomy, approval, cost, evaluation, and readiness guidance across twelve independent commands, with no shared artifact handoff or claim-level source map. The user approved fixing the P0 issues and then the remaining review recommendations.
Options considered: [Keep independent command-specific frameworks, Duplicate one corrected framework in every command, Use a shared operating contract with canonical artifacts]
Choice: Use a shared operating contract with canonical artifacts, because it centralizes safety and evidence policies while preserving each command's specialist analysis and avoiding twelve copies that can drift.
Reversibility: two-way door
Revisit trigger: Revisit after the first 5-10 real-project pilots, any contradictory command output, or a source change that invalidates a canonical policy.

Implementation consequences:
- Command names and specialist output formats remain intact.
- `references/operating-contract.md` is canonical for taxonomy, autonomy, high-risk approval, cost, evaluation, readiness, and artifact handoffs.
- `references/sources.md` distinguishes sourced observations from agent-PM product judgments.
- Commands do not write project artifacts unless the user asks.
- Public behavior changes should be released with a changelog and evaluated against `evals/`.

---
*Recorded during agent-PM product-review remediation*
