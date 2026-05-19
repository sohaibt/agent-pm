# agent-pm

**The PM playbook for building AI agent products.**

A Claude Code plugin with 12 slash commands covering the full agent product lifecycle — from "should this even be an agent?" through eval design to production safety. Grounded in primary sources from Anthropic, OpenAI, Karpathy, Hamel Husain, Linus Lee, and real production deployments.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-orange)](https://claude.ai/code)

---

## Why this exists

Building an AI agent product is a different job than building traditional software.

You need to decide if it should even be an agent. Pick from 5 workflow patterns. Design tool descriptions that are actually UX surfaces. Build eval infrastructure before you ship. Model token costs at 4x or 15x baseline. Stack 7 guardrail layers. Audit permissions to prevent the SmarterX-class disaster. Position your feature on the autonomy spectrum. Run a 30-day correction loop in production.

All of this knowledge exists — scattered across blog posts, conference talks, papers, and failure post-mortems. There's no operationalized PM toolkit for "I want to ship an agent product."

agent-pm changes that. Every command encodes a specific framework from a specific primary source. Not generic AI advice. Not vibe-coded prompts. Structured analysis grounded in what Anthropic, OpenAI, Karpathy, Hamel, and others actually recommend.

> "Building agents vs. operating agents safely are different disciplines."
> — SmarterX post-mortem

---

## The 12 Commands

### Phase 1: Should I Build This?

| Command | What it does |
|---------|-------------|
| `/agent-pm:qualify-agent` | Determine whether a feature should be deterministic code, a single LLM call, a workflow, an agent, or multi-agent. Applies Anthropic's "bias toward simplicity" and OpenAI's three agent triggers. |
| `/agent-pm:architecture-pattern` | Recommend the right pattern from Anthropic's 5 (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer) plus OpenAI's multi-agent patterns. |
| `/agent-pm:agent-spec` | Generate a complete PM spec (PRD-style) for an agent product — user job, success criteria, tools, autonomy level, eval criteria, failure modes. |
| `/agent-pm:tool-design-review` | Review a tool definition for Agent-Computer Interface (ACI) quality. Based on Anthropic's "invest in ACI as much as HCI." Rewrites mistake-prone tools. |

### Phase 2: How Do I Build It?

| Command | What it does |
|---------|-------------|
| `/agent-pm:eval-design` | Design a complete eval plan (Feature × Scenario × Assertion matrix, LLM-as-judge alignment, golden datasets). Based on Hamel Husain and Eugene Yan. |
| `/agent-pm:cost-model` | Model per-task and monthly costs. Applies the 4x agent / 15x multi-agent multipliers. Identifies cost optimization opportunities. |
| `/agent-pm:guardrails-plan` | Design a layered guardrail stack using OpenAI's 7 layers + mandatory human-in-the-loop triggers. |
| `/agent-pm:risk-audit` | Audit for the specific failure modes that caused real production disasters — permission scoping, environment separation, destructive action gates, backup isolation. Prevents the SmarterX-class failure. |

### Phase 3: How Do I Ship & Run It?

| Command | What it does |
|---------|-------------|
| `/agent-pm:agent-ux-review` | Review UX against Linus Lee's 5 paradigms beyond chat. Surfaces chat-as-default anti-patterns. Designs the verification loop. |
| `/agent-pm:autonomy-slider` | Position a feature on the autonomy spectrum (suggestion → execution → full autonomy) and design the verification UX. Based on Karpathy's autonomy slider. |
| `/agent-pm:prod-readiness` | Pre-launch checklist covering training loops, ops ownership, infrastructure, observability, rollback plans, and on-call alerting. |
| `/agent-pm:failure-mode-map` | Catalog the failure modes specific to this agent type and design mitigations for each — model, system, infrastructure, user, and operational categories. |

Every command returns:
- **Structured analysis** with scoring and frameworks
- **Specific next steps** grounded in primary sources
- **Pressure-test questions** to challenge assumptions
- **Honest assessment** including when the recommended approach won't work

---

## Install

### Claude Code

```bash
claude plugin install agent-pm
```

### Test locally (development)

```bash
git clone https://github.com/sohaibt/agent-pm.git
claude --plugin-dir ./agent-pm
```

Then try:

```
/agent-pm:qualify-agent We're building a customer support AI for our SaaS product. Users will ask billing questions, technical questions, and general FAQs. Currently handled by a human team of 5. We want to deploy in 6 weeks.
```

---

## Example: Qualify Agent

**Ask:**

> /agent-pm:qualify-agent We want to build an AI that automates expense report approval. It needs to read receipts, check against policy, approve or escalate.

**What you get:**

A recommendation against the simplicity ladder (deterministic / single LLM / workflow / agent / multi-agent), assessment against OpenAI's three agent triggers, hidden cost surfacing (eval infrastructure, observability, latency multipliers), red flags detected in your framing, and 3 pressure-test questions to challenge the recommendation.

---

## Example: Eval Design

**Ask:**

> /agent-pm:eval-design Our agent answers technical questions about our API. We have 200 historical Q&A pairs. Team of 2 engineers and 1 PM. Want to ship in 4 weeks.

**What you get:**

A complete eval plan: Feature × Scenario × Assertion matrix (Level 1 unit tests), synthetic test case generator prompt customized to your domain, human label dataset structure (200 examples, oversample failures), trace viewer spec (build in 1 day), LLM-as-judge prompts per dimension, the human-LLM alignment workflow with Cohen's Kappa target, and tracking infrastructure recommendations.

---

## The Research Behind It

This plugin is grounded in 12 primary sources, not generic AI advice:

1. **Anthropic — "Building Effective Agents"** — The 5 workflow patterns
2. **Anthropic — "How we built our multi-agent research system"** — Production lessons
3. **Anthropic — "Tool Use" docs** — ACI design principles
4. **Barry Zhang (Anthropic) — AI Engineer Summit talk** — "Don't build agents for everything"
5. **OpenAI — "A Practical Guide to Building Agents"** — Manager/decentralized patterns, 7-layer guardrails
6. **Andrej Karpathy — "Software is Changing Again"** — Software 3.0, autonomy slider, partial autonomy
7. **Hamel Husain — "Your AI Product Needs Evals"** — The foundational eval framework
8. **Eugene Yan — "Product Evals in 3 Steps"** — LLM-as-judge alignment
9. **Linus Lee — "Generative Interfaces Beyond Chat"** — UX paradigms beyond chat
10. **Lenny's Podcast — "20 AI Agents Sales Team"** — Real production deployment lessons
11. **Vantage — "Cursor Pricing Explained"** — Agent product economics
12. **SmarterX — "AI Agent Database Deletion"** — Production failure case study

Every recommendation in the plugin traces back to a specific framework, quote, or principle from these sources.

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
