# Qualification: Billing Support Draft Assistant

## Recommended rung

Recommendation: Rung 2 — Workflow  
Confidence: Medium because the task shape is clear, but quality and volume evidence is unvalidated

## Problem evidence

- **User-provided:** Support agents handle billing tickets and manually search articles and draft replies.
- **User-provided:** The fictional brief reports 400 tickets/week and eight minutes/ticket.
- **Unknown:** Whether retrieval and drafting are the main source of delay or dissatisfaction; validate through ticket observation before building.
- **Unknown:** Current response quality, escalation rate, and error cost.

## Rationale

The steps are predictable: classify the request, retrieve an approved article, and draft a reply. Deterministic routing or a single classification call plus retrieval and drafting can handle that flow. Dynamic tool selection, independent subagents, and autonomous execution are unnecessary for the stated scope.

A single LLM call could be the first prototype if one prompt can classify, retrieve through deterministic code, and draft reliably. A workflow is appropriate only if separate classification and drafting improve measured quality or operational control.

## Simpler alternative

Prototype a single retrieval-augmented drafting call with human review. Add a separate router only if evaluation shows materially different prompts or retrieval paths are needed.

## Upgrade triggers

- Add routing if distinct billing categories need different policies and a combined prompt fails representative tests.
- Consider an agent only if tasks require unpredictable multi-system investigation that predefined code cannot handle.
- Do not consider multi-agent until independent workstreams and value justify its measured cost.

## Practical implications

- **Build effort:** Unknown until the retrieval source, integration, and evaluation scope are known.
- **Token cost:** Unknown until the model, context size, and call count are measured; no universal multiplier is applied.
- **Evaluation:** Test routing, grounded drafting, refusal, missing articles, and unsafe account actions.
- **Autonomy:** Position 1, Suggestion; a human sends every response.
- **Kill criterion:** Do not launch if grounded-draft quality or review time fails to improve on the current manual workflow.

### Artifact handoff
Suggested path: `.agent-pm/billing-support/01-qualification.md`  
Upstream artifacts used: None  
Decisions to carry forward: Start with a single-call or simple workflow prototype; human sends every reply; no account writes.  
Assumptions / Unknowns: User pain frequency and eight-minute baseline are fictional input; quality, error cost, and model economics are unknown.  
Recommended next command: `/agent-pm:architecture-pattern`
