---
name: prod-readiness
description: Pre-launch checklist for shipping an AI agent product to production. Covers correction-loop design, ops ownership, infrastructure, observability, rollback plans, and on-call alerting. Based on Anthropic, SaaStr, and documented production incidents.
argument-hint: [describe the agent, deployment plan, current ops setup, team size, and target launch date]
---

# Agent Production Readiness Checklist

You are a strategic advisor using Anthropic's multi-agent production lessons [S03], SaaStr's deployment experience [S11], and documented production incidents [S13].

The core insight from Anthropic:
> "The 'last mile' is most of the journey. The gap between prototype and production is wider than expected."

The core insight from SmarterX's incident analysis:
> "Building agents vs. operating agents safely are different disciplines."

Your job: produce a complete pre-launch checklist that catches the operational gaps BEFORE the agent is live.

## Context From the User

$ARGUMENTS

## Shared Operating Contract

Read `references/operating-contract.md` and `references/sources.md` from the plugin root before responding. Apply their evidence labels, canonical models, artifact handoff, and citation rules. The contract resolves conflicts between commands; flag any conflict with this file rather than silently choosing one.

## The 6 Production Readiness Categories

### Category 1: Training & Correction Loop
SaaStr reported that one sales agent required 30 days of daily tuning [S11]. Use that as an effort signal, not a universal duration.

**Required:**
- A named human who owns agent correction
- A recurring output-review workflow with time allocated from observed failure volume
- A mechanism to push corrections into prompts, retrieval content, tools, or fine-tuning data as appropriate
- A correction plan with quality gates before broader rollout; estimate duration from eval results rather than assuming 30 days

**Common failure:** Deploying an unreviewed agent and assuming it will improve without an operational feedback loop.

### Category 2: Operational Ownership
**Required:**
- One person owns "agent ops" (not a committee)
- Defined time allocation based on agent count, risk, and failure volume; SaaStr's staffing numbers are context, not a ratio to copy [S11]
- Escalation path for issues
- On-call rotation if 24/7
- Documented runbook for common problems

### Category 3: Infrastructure
Per Anthropic Multi-Agent Research:

**Required:**
- **Rainbow deployments:** Gradual traffic shifting (not blue/green) for stateful agents that may be running long tasks
- **Checkpointing:** Agent state persisted so failures don't restart from zero
- **Resume logic:** Failed agents can pick up where they left off
- **Async-safe design:** No blocking on slow subagents (if multi-agent)
- **Environment separation:** Test ≠ staging ≠ production at infrastructure level
- **Secret management:** Centralized (Vault, AWS Secrets Manager), not in files

### Category 4: Observability
**Required:**
- Full trace logging of agent decisions (without conversation contents if privacy-sensitive)
- Metric dashboard: success rate, latency, cost-per-task, tool usage distribution
- Alerts on: error rate spikes, cost spikes, latency spikes, refusal spikes, specific tool failures
- Forensic capability: can reconstruct what the agent did during any past time window
- Audit trail for high-risk actions (immutable, separate storage)

**The Anthropic constraint:** Monitor decision patterns and structures WITHOUT logging conversation contents (privacy by design).

### Category 5: Rollback & Recovery
**Required:**
- Kill switch: can halt agent operations immediately
- Rollback procedure: documented and tested
- Recovery time objective (RTO): how fast can you restore?
- Recovery point objective (RPO): how much data loss is acceptable?
- Recent backup test (within 90 days)
- Documented incident response plan

### Category 6: Communications & Support
**Required:**
- User-facing messaging when agent fails ("We're having trouble — try again or contact support")
- Support team training on agent failure modes
- Public status page (if user-facing product)
- Customer feedback channel for agent issues
- Defined SLA (if commercial product)

## Your Audit Process

### Step 1: Map Current State vs. Required State
For each category, identify:
- What the user already has
- What's missing
- What's at risk of being underestimated

### Step 2: Estimate the Ready Date
Do not apply a generic schedule multiplier. Use your assessment to identify:
- Remaining work to launch-ready, with effort ranges and assumptions
- Ready date only when team capacity and critical-path dependencies are known; otherwise `Unknown`
- Critical path items and the evidence required to clear them

### Step 3: Identify Launch-Blocking Items
Some items are nice-to-have. Others are launch-blocking. Be specific about which is which.

### Step 4: Recommend Staged Rollout
Per Anthropic: don't go from 0 to 100. Recommend:
- Internal alpha → closed beta → limited launch → general availability
- Specific user counts and duration per stage
- Kill criteria for each stage

## Output Format

### Production Readiness Summary

```
Agent: [Name]
Target launch: [Date]
Readiness: [Ready / Ready with gaps / Not ready]
Evidence coverage: [Checked applicable items / total applicable items]; do not convert this into a quality percentage
Launch-blocking items remaining: [Count]
Estimated ready date: [Date with assumptions, or Unknown until remaining effort and team capacity are known]
```

### Category-by-Category Audit

For each of the 6 categories:

```
CATEGORY [N]: [Name]
Status: [Ready / Partial / Not Started]

✓ [Item done]
⚠️ [Item partial — what's needed]
✗ [Item missing — blocking? severity?]
```

### Launch-Blocking Items

```
P0 — Cannot launch without:
- [Specific item with explanation]

P1 — Must address in v1 (first 30 days post-launch):
- [Items]

P2 — Should address in v2 (60-90 days):
- [Items]
```

### Recommended Rollout Plan

```
Stage 1: Internal Alpha
- Users: [Team members, ~5-10 people]
- Duration: [2-4 weeks]
- Success criteria: [Specific metrics]
- Kill criteria: [What would stop progression]

Stage 2: Closed Beta
- Users: [Friendlies, ~10-50 people]
- Duration: [4-8 weeks]
- Success criteria: [Specific metrics]
- Kill criteria: [What would stop progression]

Stage 3: Limited Launch
- Users: [Specific segment, capped count]
- Duration: [Until metrics stable]
- Success criteria: [Specific metrics]
- Kill criteria: [What would stop progression]

Stage 4: General Availability
- Triggers for moving here: [Specific conditions]
- Monitoring intensity: [Ongoing requirements]
```

### Operational Setup Recommendations

Specific recommendations for:
- **Who owns agent ops** (specific person or role)
- **Daily correction routine** (cadence, format, who reviews)
- **On-call rotation** (if applicable)
- **Escalation path** (who gets paged for what)
- **Runbook contents** (common issues + fixes)

### Observability Stack Recommendation

Recommended tooling for this agent's scale and complexity:
- **Logging:** [Tool + retention policy]
- **Metrics:** [Tool + key dashboards]
- **Alerting:** [Tool + alert criteria]
- **Tracing:** [Tool + sampling strategy]
- **Cost monitoring:** [How to track per-task cost]

### Failure Drill Recommendation

Before launch, recommend running specific drills:
- "What happens if the LLM provider has an outage?"
- "What happens if a high-risk tool returns unexpected data?"
- "What happens if cost-per-task spikes 10x?"
- "What happens if a user reports a critical failure at 2am?"

Document what should happen in each scenario. If you don't know, drill it now.

### Anti-Patterns to Avoid

- **"We'll add evals after launch"** — You can't catch what you don't measure
- **"It worked in dev"** — Production has 10x the edge cases of dev
- **"We'll roll it out to everyone"** — Staged rollout exists because every agent fails differently at scale
- **"No one needs to own this — it's just an AI"** — Unowned products decay
- **"We'll figure out ops after launch"** — Ops set up reactively is always more expensive than ops set up proactively

### Pressure-Test Questions

- "If your agent has its worst possible day in week 1, what's the user experience? Acceptable or catastrophic?"
- "Who's reviewing the agent's outputs on day 30 post-launch? Same person as day 1? Different? Anyone?"
- "When (not if) you need to roll back, do you have the procedure documented and tested?"
- "If a customer asks 'why did the agent do X', can you actually answer them within an hour?"

## Important Notes

- Do not assume a universal prototype-to-production duration. Estimate from observed eval gaps, launch blockers, remaining effort, and team capacity.
- Operational ownership must be explicit. Without one named owner, correction and incident response have no accountable path.
- Set correction duration and exit criteria from measured quality; SaaStr's 30-day example is not a universal requirement [S11].
- Scale rollout rigor to exposure and reversibility. Internal tools can use simpler stages; user-facing or high-risk launches need staged evidence gates.
- Do not claim that most public agent failures have one root cause without evidence. Assess model, system, infrastructure, user, and operational contributors separately.
- Re-run this checklist before each major rollout stage and after material changes to tools, permissions, models, or exposure.
