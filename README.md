# agent-pm

**The PM playbook for building AI agent products.**

A Claude Code plugin with 12 slash commands covering agent qualification, architecture, specification, evaluation, economics, UX, safety, and production readiness. Commands share explicit evidence labels, canonical product policies, linked practitioner sources, and artifact handoffs.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-orange)](https://claude.ai/code)

---

## Why this exists

Building an AI agent product is a different job than building traditional software.

You need to decide if it should even be an agent, choose a proportionate architecture, design tools and verification UX, evaluate outcomes, model current costs, control permissions and destructive actions, and assign operational ownership. This knowledge is scattered across engineering guides, talks, evaluations, and incident analyses.

agent-pm turns those sources into structured product workflows. It distinguishes sourced observations from assumptions and unknowns, reuses earlier decisions across commands, and recommends simpler alternatives when agentic complexity is unjustified.

> "Building agents vs. operating agents safely are different disciplines."
> — SmarterX analysis of the PocketOS incident

---

## The 12 Commands

### Phase 1: Should I Build This?

| Command | What it does |
|---------|-------------|
| `/agent-pm:qualify-agent` | Determines whether the feature should be deterministic code, a single LLM call, a workflow, an agent, or multi-agent, while separating problem evidence from architecture suitability. |
| `/agent-pm:architecture-pattern` | Recommends a proportionate workflow or multi-agent pattern using task dependencies, latency, reliability, and cost tradeoffs. |
| `/agent-pm:agent-spec` | Generates the central product specification and indexes specialist artifacts for evaluation, cost, autonomy, UX, and safety. |
| `/agent-pm:tool-design-review` | Reviews tool contracts and rewrites unclear definitions without inventing toolkit boundaries when sibling tools are unavailable. |

### Phase 2: How Do I Build It?

| Command | What it does |
|---------|-------------|
| `/agent-pm:eval-design` | Designs scenario assertions, organic human labels, judge alignment, held-out evaluation, and production outcomes. |
| `/agent-pm:cost-model` | Builds bottom-up per-task and monthly cost ranges using current provider prices without double-counting architecture multipliers. |
| `/agent-pm:guardrails-plan` | Designs applicable guardrail layers, default approval for high-risk actions, and infrastructure controls. |
| `/agent-pm:risk-audit` | Audits permission scope, environment separation, destructive-action gates, backup isolation, and recovery evidence without requesting secret values. |

### Phase 3: How Do I Ship & Run It?

| Command | What it does |
|---------|-------------|
| `/agent-pm:agent-ux-review` | Reviews interaction and verification UX using the same per-action autonomy model as the specification. |
| `/agent-pm:autonomy-slider` | Assigns positions 0–4 per action and defines evidence-based transitions and rollback triggers. |
| `/agent-pm:prod-readiness` | Assesses correction loops, ownership, infrastructure, observability, recovery, support, and launch blockers without false readiness percentages. |
| `/agent-pm:failure-mode-map` | Prioritizes model, system, infrastructure, user, and operational failures with drills and residual risk. |

Every command returns:
- Structured analysis with source IDs and explicit assumptions or unknowns
- Specific next steps and an operational or user-facing outcome check
- Pressure-test questions to challenge assumptions
- An artifact handoff that preserves earlier decisions

You do **not** need to run all twelve commands for every project.

---

## Install

### Claude Code marketplace

If `agent-pm` is listed in your configured marketplace:

```bash
claude plugin install agent-pm
```

### Local development

```bash
git clone https://github.com/sohaibt/agent-pm.git
claude --plugin-dir ./agent-pm
```

## Ten-minute quickstart

Start with the problem and current alternative, not a preferred architecture:

```text
/agent-pm:qualify-agent Our five-person support team handles billing questions by searching help-center articles and drafting replies manually. We are considering an agent that classifies questions, retrieves policy, and drafts a response. A human sends every response. We have no quality baseline yet.
```

Then follow only the recommended path:

```text
/agent-pm:architecture-pattern Use the previous qualification. Choose a pattern only if the task needs one.
/agent-pm:agent-spec Use the previous decisions and label missing inputs.
/agent-pm:eval-design Build the smallest useful evaluation for this spec.
/agent-pm:prod-readiness Assess readiness using the spec and eval plan; do not invent operational evidence.
```

Each response ends with an artifact handoff. Commands do not write files unless you ask; to persist a response, say `Save the artifact handoff for project billing-support`.

See [the complete illustrative workflow](examples/billing-support/README.md) for qualification, architecture, specification, evaluation, cost, and readiness artifacts.

---

## Shared Rules and Sources

- [Operating contract](references/operating-contract.md): canonical architecture, autonomy, high-risk approval, evaluation, cost, readiness, and artifact-handoff rules
- [Source map](references/sources.md): exact links, publication and access dates, claim mappings, and limitations for primary material and secondary case analyses
- [Changelog](CHANGELOG.md): behavior changes and corrections

Source-backed observations are not universal promises. Current model names, prices, limits, and APIs must be checked against provider documentation.

## Quality and Product Success

- [Evaluation guide](evals/README.md): repository checks and real-command prompt evaluations
- [Prompt scenarios](evals/prompt-scenarios.md): over-engineering, destructive risk, cross-command consistency, cost, evaluation alignment, vague input, and artifact handoffs
- [Output rubric](evals/output-rubric.md): source fidelity, safety, uncertainty, consistency, specificity, and outcomes
- [Success metrics](references/success-metrics.md): decision adoption, workflow continuity, repeat use, and quality guardrails
- [Pilot scorecard](evals/pilot-scorecard.md): evidence collection for real-project pilots

The repository includes an evaluation process, not a claim that all model-run evaluations or real-user pilots have passed.

---

## Who this is for

- **PMs building AI agent products** who need a structured framework for the decisions you're making blind
- **Founders shipping AI features** who want to avoid the "demo works, production doesn't" trap
- **Engineering managers** scoping agent projects who need PM frameworks engineering can build to
- **Anyone moving from prototype to production** with an AI agent

This is NOT for:
- Building chatbots that don't need agentic capability (use a simpler approach)
- Pure ML/research work (this is product-focused)
- Generic AI product strategy (use [strategy-mcp](https://github.com/sohaibt/strategy-mcp) for that)

---

## Contributing

Contributions welcome. Some ways to help:

- **Add a new command** — open an issue with the framework and source material
- **Add research sources** — transcripts, articles, papers that surface new agent PM patterns
- **Improve existing commands** — sharper analysis, deeper source references, better pressure-test questions
- **Report bad advice** — if a command gives shallow or wrong analysis, that's a bug

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## License

MIT — use it however you want.

---

## Built by

[Sohaib Thiab](https://sohaibthiab.me) — Former CPO, now building AI products in public.

- [strategy-mcp](https://github.com/sohaibt/strategy-mcp) — 12 product strategy frameworks as MCP tools
- [founder-mode](https://github.com/sohaibt/founder-mode) — Brian Chesky's founder mode operating system as a Claude Code plugin
- [Mastering Product HQ](https://masteringproducthq.com) — Weekly writing on product leadership

**Want connected strategy execution?** [GetVelocity.ai](https://getvelocity.ai) takes these frameworks further — connecting your OKRs to Jira, Linear, and ClickUp with AI-powered monitoring and real-time velocity tracking.

---

> "Invest in ACI as much as HCI." — Anthropic
