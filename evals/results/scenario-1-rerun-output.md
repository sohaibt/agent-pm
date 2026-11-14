# Scenario 1 Rerun Live Output

- Date: 2026-11-14
- Claude Code: 2.1.325
- Model: `sonnet` alias
- Plugin: local working tree, version 1.1.0
- Command: `/agent-pm:qualify-agent`
- Write tools: unavailable
- CLI authentication-expiry warning omitted; response preserved verbatim

## Recommended Rung

```
Recommendation: Rung 1 — Single LLM call with retrieval (RAG)
Confidence: Medium
```

I did not create or change any files. I read `references/operating-contract.md` and `references/sources.md`.

## Rationale

**Triggers.** Trigger 3 applies: heavy unstructured data, because customers write free text [S02]. That trigger justifies a model. It does not justify an agent. Triggers 1 and 2 do not apply. Nothing you wrote shows hard judgment calls or a brittle rule tree. (Unknown: you gave me no ticket examples.)

**Why not multi-agent.** None of the Rung 4 triggers apply [S01, S03]:
- The task fits in one context window.
- The three steps depend on each other, so they cannot run in parallel.
- The steps do not need different tools.

Classify, retrieve, draft is a fixed sequence. One call can return a category label plus a draft, using the retrieved article.

**Why Rung 1, not Rung 2.** Move to a workflow only if one prompt cannot handle all three types. For example, billing may need its own prompt and an account lookup. You have no evidence of that yet.

**Evidence status.**
- User-provided: 500 SaaS users, three request types, a human sends every response.
- Unknown: user research, error baseline, ticket volume, current handling time, and who the 500 users are (customers or staff).
- Assumption: the help center has good articles.

You gave me a solution. You did not give me a problem I can check.

## What This Means in Practice

- **Build effort:** Unknown. It depends on your help-center format, your ticketing tool, and team capacity.
- **Token cost:** About one model call per ticket, plus one retrieval step. Dollar cost is Unknown. I need current prices [S14, S15] and real ticket volume.
- **Eval complexity:** Check three things:
  - Is the category correct?
  - Is the right article retrieved?
  - Is the draft faithful to the article?

  Use `eval-design` for dataset design.
- **Failure modes:**
  - Wrong category.
  - Wrong or stale article.
  - Draft invents policy or prices.
  - Billing answers that expose or misstate account data.
  - Reviewers approve drafts too fast without reading.
- **Time to production:** Unknown until you have a baseline and team capacity.

## If You Were Tempted to Build Higher

It is tempting to build multi-agent because there are three request types. That looks like three specialist agents. But categories are not parallel work. They are labels. One call can sort them.

Anthropic saw about 4× tokens for agents and 15× for multi-agent in its research system [S03]. Treat that only as a coarse sanity check, not as a forecast for your system.

Upgrade path:
- If one prompt fails on billing, evaluate Rung 2 with a separate billing path.
- If tickets need live account lookups with unpredictable steps, evaluate Rung 3.
- Elapsed time alone is not a trigger.

## Red Flags Detected

- **No success criterion.** "Good answer" is not a metric.
- **No baseline.** You cannot tell whether the AI helps.
- **No user research.** Pain and frequency are unknown.
- **Architecture before problem.** "Multi-agent" came before the problem evidence.
- **Human review is not a free safety net.** If reviewers rubber-stamp, errors still reach customers.

## Pressure-Test Questions

1. What is the smallest manual or rule-based baseline you can measure first? For example, time 50 past tickets from read to send.
2. If 1 in 20 billing drafts is wrong and a reviewer misses it, what happens to that customer?
3. Is the real problem slow replies, or hard-to-find help articles? If it is findability, better search (Rung 0) might fix it.

## What I Need From You

I can answer more firmly with three facts:
1. How many tickets arrive per week, and what share is each type?
2. How long does a human take per ticket today?
3. Are the help-center articles current and complete?

**Decision:** Gather those three facts first (my pick), or build a Rung 1 prototype on 50 real past tickets. I would gather facts first. It is cheap and it gives you the baseline.

### Artifact handoff
Suggested path: .agent-pm/customer-support-agent/01-qualification.md
Upstream artifacts used: None
Decisions to carry forward: Rung 1 (single LLM call with RAG). No agent trigger applies. No multi-agent trigger applies. Human sends every response (autonomy position 1, Suggestion).
Assumptions / Unknowns: Ticket volume, error baseline, user research, article quality, whether billing needs account data, cost, effort, timeline.
Recommended next command: None until the baseline evidence exists. Then `agent-spec`.
