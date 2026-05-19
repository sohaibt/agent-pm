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
   - A specific primary source reference
   - A structured scoring or assessment framework
   - Actionable next steps (not generic advice)
   - Pressure-test questions that challenge the analysis
   - Honest acknowledgment of when the framework doesn't apply

4. **Test it locally:**
   ```bash
   claude --plugin-dir ./agent-pm
   /agent-pm:your-command-name [test input]
   ```

5. **Submit a PR** with:
   - The SKILL.md file
   - A brief description of the source material
   - An example of what the output looks like

## Quality standards

- **Grounded in primary sources.** Every recommendation should trace back to a specific practice from a credible practitioner. No generic AI advice.
- **Opinionated but honest.** Frameworks have failure modes. Every command should acknowledge when its approach doesn't apply.
- **Structured output.** Scoring tables, clear frameworks, specific next steps. Not essays.
- **Pressure-test questions.** Every command should challenge the user's assumptions, not just validate them.
- **Context-aware.** What works for a 5-user internal tool ≠ a consumer product at scale. Commands should adapt to context.

## Pull request guidelines

- Open an issue first for new commands so we can discuss the approach
- Keep PRs focused — one command per PR
- Include the primary source reference
- Test the command locally before submitting
- Show an example output in the PR description

## What we don't want

- Generic AI product advice not grounded in named sources
- Commands that are just "ask Claude to do X" without a structured framework
- Frameworks that apply to all software (not specific to AI agents)
- Low-confidence recommendations without acknowledging uncertainty

## Questions?

Open an issue or reach out to [Sohaib Thiab](https://sohaibthiab.me).
