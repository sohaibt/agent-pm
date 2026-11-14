# Scenario 1 Initial Live Output

- Date: 2026-11-14
- Claude Code: 2.1.325
- Model: CLI default; exact model not captured
- Plugin: local working tree, version 1.1.0
- Command: `/agent-pm:qualify-agent`
- Write tools: unavailable
- CLI authentication-expiry warning omitted; response preserved verbatim

**Recommendation:** Rung 1 — Single LLM call with retrieval
**Confidence:** Medium

I did not create or change any files. I read `references/operating-contract.md` and `references/sources.md`.

## Rationale

**The short answer: you do not need many agents. You need one good model call.**

Your job has three steps. These steps are classify, find the article, and draft the reply. They always run in the same order. When the order is fixed, plain code can run the steps. You do not need an agent to choose the order. [S01]

Here is how it works:
1. Code searches the help center with the customer's message. This step does not need a model.
2. One model call gets the message and the top articles. It returns three things: the category, the best article, and a draft reply.
3. A human reads the draft and sends it.

**The OpenAI triggers** [S02]:
- **Complex decisions:** No. A human makes every send decision. *(User-provided: "A human sends every response.")*
- **Rules that are hard to keep up:** No. You did not tell us about an old rule system that is breaking.
- **Messy text:** Yes. Customers write in free text. This is a reason to use an LLM. It is not a reason to use an agent.

**The multi-agent triggers** [S03]: none apply. One ticket fits in one context window (the amount of text a model can read at once). The steps depend on each other, so they cannot run in parallel. 500 users is not a high-value, high-volume case that can pay for about 15× the tokens. *(The 15× number is from Anthropic's own research system. Use it only as a rough guess.)*

**Could a lower rung work? (Rung 0, no AI)** Maybe. Your help desk may already have article suggestions and saved replies (macros). For 500 users, the ticket count may be small. That count is **Unknown**. Measure the count before you build.

**What could push this up to Rung 2 (workflow):** billing questions often need account data, such as the plan or the last invoice. If they do, add one fixed code step that gets the data before the model call. That is still not an agent.

## What This Means in Practice

| Item | Estimate | Label |
|---|---|---|
| Build effort | Days to about 2 weeks for a prototype | Assumption |
| Token cost | 1 search call + 1 model call per ticket. Total cost is unknown until you know ticket volume and the model you pick. | Unknown |
| Eval complexity | Low. Use 50–100 real past tickets. Mark PASS/FAIL for each check: correct category, correct article, and a draft with no made-up facts. | Assumption [S06] |
| Failure modes | About 5: wrong category, wrong or missing article, made-up answer, old article, and a missed escalation (for example an angry customer or a refund fight) | Assumption |
| Time to production | Unknown. It depends on when you have a labeled ticket set. | Unknown |

**Autonomy:** Position 1, Suggestion. AI drafts and the human decides. This is correct for v1. Keep it there.

## If You Were Tempted to Build Higher

Multi-agent sounds good because there are three kinds of request. It is easy to think "one agent per kind."

But the three kinds use the same tool: help-center search. They also give the same output: a draft. A router agent plus three worker agents gives you 4× the prompts and evals. It also adds hand-offs that can fail. You get no new ability for that cost.

**Upgrade path:** after about 3 months of real traces, move to Rung 2 or 3 only if both of these are true:
- Drafts often fail because they need data the model cannot get in one fixed step.
- Those steps are different from ticket to ticket.

## Red Flags Detected

- **Architecture before problem.** "Multi-agent" was picked before anyone said what the pain is. *(User-provided: "no user research yet.")*
- **No baseline.** You cannot show improvement without a "before" number. *(User-provided: "no error baseline.")* This is the "we'll add evals later" pattern.
- **No success criterion.** "Draft an answer" is not a metric. Pick one, for example: the share of drafts sent with small edits, or the time to first reply.
- **Demand is not checked.** We do not know if support load is a real problem at 500 users.

## Pressure-Test Questions

1. How many tickets do you get each week? How long does one reply take now? If it is 20 tickets a week, help-desk macros may beat any AI build.
2. Do billing replies need account data (plan, invoice, refund status)? If yes, the design changes to Rung 2.
3. Say a draft gives a wrong refund policy and the agent sends it without a check. What does that cost you? Your answer tells you how strict the review screen must be.

## What you do now

Pull 50–100 past tickets. Count them by type. Time how long the human replies take. That gives you the baseline and the eval set in one step.

### Artifact handoff
Suggested path: `.agent-pm/saas-support-drafting/01-qualification.md`
Upstream artifacts used: None
Decisions to carry forward: Rung 1 (deterministic search + one LLM call). Autonomy at position 1 (human sends all). No multi-agent.
Assumptions / Unknowns: ticket volume, pain cost, whether billing needs account data, error baseline, model and price, help-center freshness
Recommended next command: `eval-design` (after you pull the past tickets). Skip `architecture-pattern` unless billing needs account lookups.
