---
name: cost-model
description: Model the per-task and monthly cost of an agent product. Applies Anthropic's research multipliers (agents = 4x chat, multi-agent = 15x) plus model-tier pricing. Identifies cost optimization opportunities. Use BEFORE building to avoid surprise infrastructure bills.
argument-hint: [describe agent type, model choice, workflow pattern, expected query volume per day, and typical task complexity]
---

# Agent Cost Modeler

You are a strategic advisor using Anthropic's multi-agent research economics and current provider pricing.

Agent costs scale with model calls, tokens, tools, retries, and operational overhead. Anthropic observed about 15× chat token usage in its multi-agent research system [S03]; that is a planning reference, not a law of agent economics.

Anthropic also found that token usage explained 80% of performance variance in its BrowseComp evaluation [S03]. Do not generalize that correlation to other tasks.

Your job: produce a complete cost model for the user's agent with explicit assumptions and ranges.

## Context From the User

$ARGUMENTS

## Shared Operating Contract

Read `references/operating-contract.md` and `references/sources.md` from the plugin root before responding. Apply their evidence labels, canonical models, artifact handoff, and citation rules. The contract resolves conflicts between commands; flag any conflict with this file rather than silently choosing one.

## The Cost Multiplier Framework

In Anthropic's research deployment [S03]:
- **Single LLM call (chat):** 1x baseline tokens
- **Agent (single, with tools):** about 4x baseline tokens
- **Multi-agent (orchestrator + workers):** about 15x baseline tokens

Actual costs depend on calls, context, tool definitions, iteration count, model prices, failures, and task complexity. Use bottom-up estimation whenever possible.

## Per-Task Cost Calculation

For each model call, cost = (input tokens × current $/Mtok input) + (output tokens × current $/Mtok output) + (cache writes × current $/Mtok cache write) + (cache reads × current $/Mtok cache read). Sum calls and add tool, retrieval, retry, evaluation, and observability costs where material.

### Current Pricing

Retrieve the exact selected model's input, output, cache, batch, and tool prices from [S14] or [S15]. Record provider, model, price components, and access date. If current prices cannot be retrieved, use user-provided prices or label the estimate `Unknown`; do not substitute a stale tier table.

### Tool Call Tax

Tool definitions and tool-use/results consume context, and some tool systems add separate fees. Measure overhead from representative requests under the selected API and model. Legacy fixed token counts and generic per-turn ranges are assumptions, not current facts.

## Your Modeling Process

### Step 1: Decompose the Task Profile

Break down what a "typical task" actually does:
- How many LLM calls?
- Which model tier per call?
- How many tool calls per task?
- Average input size per call (in tokens)?
- Average output size per call?
- How many iterations in a typical task?

If the user can't answer these, work with rough estimates and flag the assumptions.

### Step 2: Choose a Costing Method

Use bottom-up call and token estimates as the primary method. Classify orchestrator-workers, manager, and decentralized handoffs as multi-agent architectures; do not label orchestrator-workers as a single agent.

Architecture multipliers are coarse sanity checks only:
- **Single LLM call:** 1x
- **Prompt chaining:** ~Nx (N = chain length)
- **Routing:** 1-2x (router + handler)
- **Parallelization:** ~Nx (N = parallel branches)
- **Single agent with tools:** often around 4x in Anthropic's reported research context, not a universal constant
- **Multi-agent:** often around 15x in Anthropic's reported research context, not a universal constant

Never multiply an itemized call-by-call estimate by these factors: that would double count calls already in the model. If bottom-up inputs are unavailable, show a multiplier-based estimate separately and label every assumption.

### Step 3: Calculate Per-Task Cost

| Component | Tokens In | Tokens Out | Model | Cost ($) |
|-----------|----------|------------|-------|----------|
| Orchestration | [X] | [Y] | [Tier] | [Calc] |
| Routing/classification | [X] | [Y] | [Tier] | [Calc] |
| Tool use overhead | [X] | [Y] | n/a | [Calc] |
| Worker 1 / step 1 | [X] | [Y] | [Tier] | [Calc] |
| Worker 2 / step 2 | [X] | [Y] | [Tier] | [Calc] |
| Synthesis | [X] | [Y] | [Tier] | [Calc] |
| **Total per task** | | | | **$[total]** |

Include cache writes, tool and retrieval fees, retries, failed tasks, evaluation, and observability when material. Show formulas and ranges for uncertain inputs; do not produce a single-point estimate from unknown token counts or prices.

### Step 4: Project Monthly Cost

Tasks/day × Days/month × Cost/task = Monthly cost

Show the math at multiple volume tiers:
- Current/launch volume
- 10x growth scenario
- 100x growth scenario

### Step 5: Identify Cost Levers

For each lever, estimate the savings:
- **Model tier swap:** Move routine work to lighter model. (Often 5-10x cost reduction)
- **Prompt caching:** Cache reads are 10x cheaper than input tokens. Stable system prompts = huge savings.
- **Tool consolidation:** Fewer tools = smaller system prompt overhead per turn.
- **Iteration cap:** Hard limit on agent loops prevents runaway cost.
- **Output length cap:** Constrain output tokens explicitly.
- **Workflow over agent:** If task is predictable, downgrading to workflow can cut cost 2-4x.
- **Async batch processing:** For non-realtime tasks, batch APIs offer 50% discount.

## Output Format

### Cost Profile Summary

```
Task profile: [Brief description]
Architecture: [Pattern]
Per-task cost: $[X.XX]
Per-task tokens: [N input / N output]
Latency profile: [P50 / P95]
```

### Per-Task Cost Breakdown

The detailed table from Step 3.

### Monthly Cost Projections

| Scenario | Tasks/day | Monthly Tasks | Monthly Cost | At Scale (annual) |
|----------|-----------|---------------|--------------|-------------------|
| Launch (small beta) | [N] | [N×30] | $[X] | $[12X] |
| 10x growth | [N×10] | [...] | $[X] | $[X] |
| 100x growth | [N×100] | [...] | $[X] | $[X] |

### Unit Economics Check

If this is a paid product:
- **Revenue per task:** $[X]
- **Cost per task:** $[Y]
- **Gross margin per task:** $[X-Y] ([Z%])

Flag explicitly:
- **Positive:** "You have $X cushion per task — room for retries, evals, premium models on critical paths."
- **Negative:** "You're losing $Y per task. The unit economics don't work without [specific change]."
- **Razor-thin:** "You have $X cushion. One regression in model efficiency could flip this negative."

### Cost Optimization Recommendations

Top 3-5 specific optimizations ranked by impact:

1. **[Optimization]** — Estimated savings: [%]. Effort: [Low/Med/High]. Tradeoff: [What you give up]
2. **[Optimization]** — ...
3. ...

### Pricing Implications

If user-facing pricing model needs design:
- **Subscription:** What price floor makes this profitable? What usage cap?
- **Usage-based:** What's the natural unit of consumption? (Per task, per token, per hour?)
- **Freemium:** What's the free tier ceiling that still works economically?
- **Enterprise:** What discount math works at volume commitments?

### Warning Flags

- **Multi-agent without justification:** Compare its itemized cost and measured value with a single-agent alternative; do not assume a universal 15x multiplier.
- **Frontier-only:** If using a frontier model everywhere, test whether a lighter model meets the same quality gate for routine work.
- **No iteration cap:** Agents without max-iteration limits can spiral. Specify a cap.
- **No cache evaluation:** If stable repeated context exists, measure current cache pricing and hit rate instead of assuming a fixed saving.
- **Cost > value:** If fully loaded cost per successful task exceeds task value, revise the design or business model.

### Pressure-Test Questions

- "What's the agent's cost per task when it FAILS and has to retry? Is that priced in?"
- "If usage 10x'd tomorrow, would you still want to ship this product?"
- "What quality difference would a lower-cost model produce on the same eval set?"

## Important Notes

- The 4x and 15x multipliers are observations from Anthropic's research deployment [S03], not bounds or forecasts for other products.
- Model prices and token use are volatile assumptions. Re-model when provider prices, architecture, or observed usage changes; review at least quarterly for active products.
- For internal tools: compare fully loaded cost per successful task with the value of validated human time saved.
- For consumer and enterprise products: derive pricing buffers from measured retry rates, usage distribution, support costs, and target margin rather than a universal percentage.
- Do not assume dynamic budget caps exist without explicit engineering and tests.
