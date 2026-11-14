# Source Map

Sources were checked on 2026-11-14. Publication dates are included when the publisher exposes them. These sources inform frameworks; they do not make every agent-PM recommendation a sourced fact.

## Architecture and qualification

### [S01] Anthropic — Building effective agents

- URL: https://www.anthropic.com/engineering/building-effective-agents
- Published: 2024-12-19
- Used by: `qualify-agent`, `architecture-pattern`, `agent-spec`
- Supports: workflow versus agent distinction, simplicity bias, prompt chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizer
- Limits: patterns are composable examples, not a requirement to adopt agentic complexity

### [S02] OpenAI — A practical guide to building agents

- Landing page: https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- PDF: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- Used by: `qualify-agent`, `architecture-pattern`, `tool-design-review`, `guardrails-plan`
- Supports: agent use-case triggers, manager and decentralized orchestration, tool design, layered guardrails, and escalation for failures and high-risk actions
- Limits: approval exceptions in agent-PM are product policy, not an OpenAI promise of safe autonomy

### [S03] Anthropic — How we built our multi-agent research system

- URL: https://www.anthropic.com/engineering/multi-agent-research-system
- Published: 2025-06-13
- Used by: `qualify-agent`, `architecture-pattern`, `tool-design-review`, `cost-model`, `eval-design`, `prod-readiness`, `failure-mode-map`
- Supports: parallel research use cases, orchestrator-workers, delegation, evaluation, tracing, checkpointing, resume behavior, and rainbow deployments
- Observed in that system: agents used about 4× chat tokens and multi-agent about 15×; token usage explained 80% of BrowseComp performance variance; tool-testing agents reduced future task completion time by 40%
- Limits: these are deployment-specific observations, not universal multipliers, quality gains, or staffing ratios

### [S04] Barry Zhang, Anthropic — How We Build Effective Agents

- Video: https://www.youtube.com/watch?v=D7_ipDqhtwk
- Used by: `qualify-agent`, `cost-model`
- Supports: practical simplicity, evaluation, and thinking from the agent's perspective
- Limits: do not attribute later talks or unsolved-problem claims to this video without checking its transcript

## Evaluation

### [S05] Hamel Husain — Your AI Product Needs Evals

- URL: https://hamel.dev/blog/posts/evals/index.html
- Published: 2024-03-29
- Used by: `eval-design`, `agent-spec`
- Supports: iterative evaluation, trace inspection, domain-specific assertions, and evaluation as product infrastructure

### [S06] Eugene Yan — Product Evals in Three Simple Steps

- URL: https://eugeneyan.com/writing/product-evals/
- Published: 2025-11
- Used by: `eval-design`
- Supports: binary labels, organic failures, development and held-out test splits, one evaluator per dimension, precision/recall, and Cohen's kappa
- Observed guidance: 50–100 failures among 200+ examples is a starting recommendation, not a universal sample-size requirement

## Autonomy and UX

### [S07] Andrej Karpathy — Software Is Changing (Again)

- Overview: https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again
- Talk date: 2025-06-17
- Used by: `autonomy-slider`, `agent-ux-review`, `agent-spec`
- Supports: partial autonomy, human verification, generation-verification loops, and the Iron Man suit analogy
- Limits: agent-PM's five numbered positions and accuracy bands are product constructs, not thresholds from the talk

### [S08] Linus Lee — Generative Interfaces Beyond Chat

- Video: https://home.mlops.community/public/videos/generative-interfaces-beyond-chat
- Published: 2023-04
- Used by: `agent-ux-review`
- Supports: using application context, selections, structured outputs, and guided interactions beyond a blank chat box
- Limits: the five category names in the command are an operational synthesis of the talk, not a standardized industry taxonomy

## Tool design

### [S09] Anthropic — Writing effective tools for agents, with agents

- URL: https://www.anthropic.com/engineering/writing-tools-for-agents
- Published: 2025-09-17
- Used by: `tool-design-review`, `agent-spec`
- Supports: clear tool contracts, token-efficient outputs, namespaces, evaluation, and iterative tool improvement

### [S10] Anthropic — Tool use with Claude

- URL: https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview
- Used by: `tool-design-review`, `cost-model`
- Supports: tool definitions and tool-use request/response mechanics
- Limits: token overhead changes with API and model versions; measure current requests instead of treating legacy counts as fixed

## Production operations and economics

### [S11] SaaStr — Dear SaaStr: Should I Run 20+ AI Agents the Way SaaStr Does?

- URL: https://www.saastr.com/dear-saastr-should-i-run-20-ai-agents-the-way-saastr-does/
- Published: 2026-03-05
- Used by: `prod-readiness`, `failure-mode-map`
- Supports: dedicated operational ownership, sustained review, knowledge freshness, and substantial correction effort
- Deployment-specific observations: one sales agent took 30 days of daily tuning; their Chief AI Officer spent 30% of her time on agent management; they budgeted 30–60 minutes daily per two or three agents
- Limits: self-reported results from one organization do not establish a mandatory 30-day period or a general staffing formula

### [S12] Vantage — Cursor Pricing Explained

- URL: https://www.vantage.sh/blog/cursor-pricing-explained
- Published: 2026-03-04
- Used by: `cost-model`
- Supports: an example of usage-based agent-product pricing and cost analysis
- Limits: secondary market analysis, not provider pricing documentation

### [S13] SmarterX — An AI Agent Deleted a Production Database in 9 Seconds

- URL: https://smarterx.ai/smarterxblog/ai-agent-database-deletion
- Published: 2026-05-05
- Used by: `risk-audit`, `guardrails-plan`, `failure-mode-map`, `prod-readiness`
- Supports: a secondary case analysis of the PocketOS incident, including credential scope, environment confusion, destructive action without confirmation, and volume-level backup loss
- Limits: this is secondary reporting about a founder postmortem, not a primary incident report; avoid expanding its claims beyond the article

## Current pricing references

Use these instead of hardcoded model-tier prices:

- [S14] Anthropic pricing: https://www.anthropic.com/pricing
- [S15] OpenAI API pricing: https://openai.com/api/pricing/

Record the exact model, provider, price components, and access date in every cost model. A cached price table in a prompt is not current evidence.
