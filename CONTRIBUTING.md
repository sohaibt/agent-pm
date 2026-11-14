# Contributing to agent-pm

Thanks for your interest in contributing! agent-pm is an open source Claude Code plugin that encodes the agent product lifecycle into structured slash commands.

## Ways to contribute

### Add a new slash command

Have an agent PM framework that should be a command? Open an issue with:
- The command name and what it does
- What inputs it needs from the user
- What the output should look like
- The primary source it's grounded in (blog post, paper, talk, post-mortem)

We strongly prefer commands grounded in **primary sources** from credible practitioners — Anthropic, OpenAI, named engineers/PMs at shipping companies, peer-reviewed papers. If the framework is just "best practices," it doesn't belong here.

Label: `new-command`

### Add a research source

Found a transcript, paper, or post-mortem that surfaces new agent PM patterns? Open an issue or PR with:
- The source (URL, transcript, or summary)
- What new practices or principles it adds
- Which existing commands it could strengthen

Label: `research`

### Improve an existing command

If a command gives shallow analysis, misses nuance, or doesn't match the source material:
- Better scoring frameworks
- More specific source references and quotes
- Sharper pressure-test questions
- Edge case handling (different agent types, sizes, deployment contexts)

Label: `enhancement`

### Fix bad advice

If a command gives advice that's wrong, misleading, or would lead to bad agent products — that's a bug. agent-pm commands should be opinionated but grounded.

Label: `bug`

## How the plugin works

Each slash command is a `SKILL.md` file in the `skills/` directory. The file contains:
1. **YAML frontmatter** — name, description, argument hint
2. **Framework instructions** — the structured analysis Claude follows
3. **Output format** — what the response should look like
4. **Important notes** — edge cases and guardrails

There's no code to run. The "logic" is the framework itself — encoded as expert instructions that Claude follows when the user invokes the command.

## Adding a new command

1. **Create a directory** in `skills/` with your command name (lowercase, hyphens):
   ```
   skills/your-command-name/SKILL.md
   ```

2. **Write the SKILL.md** following this structure:
   ```yaml
   ---
   name: your-command-name
   description: One sentence explaining when to use this command.
   argument-hint: [what the user should provide]
   ---

   # Command Title

   You are a strategic advisor trained on [SPECIFIC PRIMARY SOURCE].

   The core principle: [QUOTE OR THESIS FROM SOURCE]

   ## Context From the User

   $ARGUMENTS

   ## Your Analysis Framework

   [The structured framework Claude follows]

   ## Output Format

   [What the response should look like]

   ## Important Notes

   [Edge cases, guardrails, when NOT to use this]
   ```

3. **Every command must include:**
   - A source ID mapped in `references/sources.md`, with deployment-specific limits preserved
   - The shared rules in `references/operating-contract.md`
   - A structured scoring or assessment framework
   - Actionable next steps and an outcome check
   - Pressure-test questions that challenge the analysis
   - Honest acknowledgment of unknowns and when the framework doesn't apply
   - The canonical artifact handoff and applicable skip conditions

4. **Test it locally:**
   ```bash
   claude --plugin-dir ./agent-pm
   /agent-pm:your-command-name [test input]
   ```

5. **Run relevant evaluations:**
   ```bash
   python3 -m unittest discover -s evals -p 'test_*.py'
   ```
   Add or update a scenario in `evals/prompt-scenarios.md` for behavior changes. Record actual command outputs and rubric results; a prompt inspection is not a model-run pass.

6. **Submit a PR** with:
   - The changed files and source mapping
   - A brief description of the source material and its limits
   - An actual example output or a clear statement that model evaluation was not run
   - Repository and prompt evaluation results

## Quality standards

- **Traceable.** Link the exact source and distinguish primary material, secondary analysis, sourced observations, and agent-PM product judgments.
- **Opinionated but honest.** Do not invent evidence, baselines, prices, thresholds, dates, or universal rules. Use `Unknown` and `N/A` where appropriate.
- **Consistent.** Preserve the shared architecture, autonomy, high-risk approval, evaluation, cost, and readiness policies.
- **Connected.** Reuse upstream artifacts and keep detailed specialist matrices in their owning artifacts rather than creating competing copies.
- **Structured and actionable.** Provide specific analysis, outcome checks, and next steps rather than essays or generic advice.
- **Pressure-tested.** Challenge assumptions and evaluate actual outputs before claiming quality improvements.
- **Context-aware.** What works for a five-user internal tool differs from a consumer product at scale.

## Pull request guidelines

- Open an issue first for new commands so we can discuss the approach
- Keep PRs focused and update the shared contract rather than duplicating conflicting policy
- Include exact source references and access dates for volatile claims
- Run repository checks and relevant real-command evaluations
- Show an example output and disclose any evaluation that was not run

## What we don't want

- Generic AI product advice not grounded in named sources
- Commands that are just "ask Claude to do X" without a structured framework
- Frameworks that apply to all software (not specific to AI agents)
- Low-confidence recommendations without acknowledging uncertainty

## Questions?

Open an issue or reach out to [Sohaib Thiab](https://sohaibthiab.me).
