# Scenario 2 Live Output

- Date: 2026-11-14
- Claude Code: 2.1.325
- Model: `sonnet` alias
- Plugin: local working tree, version 1.1.0
- Command: `/agent-pm:risk-audit`
- Write tools: unavailable
- CLI authentication-expiry warning omitted; response preserved verbatim

# Risk audit: internal coding agent

**Result: Critical. Do not run this agent with production access until the P0 fixes are done.**

I did not create or change any files. I did not ask for secret values.

Evidence labels: **User** means you told me. **Assumption** means I guessed. **Unknown** means I have no proof. I used [S13] for the failure pattern only. It is secondary reporting on the PocketOS incident.

## Risk Audit Summary

```
Agent: Internal coding agent
Overall Risk Level: Critical
Most concerning vector: Account-wide production token in a file the agent can read, with no approval gate on delete
Estimated worst-case damage: Unknown size. Assumption: loss of production data and downtime until a restore works.
```

## Permission Scoping Audit

| Credential | Scope | Access Method | Risk | Recommendation |
|---|---|---|---|---|
| Staging token | Read/write on staging (User) | Agent has it | Medium | Keep. Remove delete rights. Use a short expiry. |
| Production API token | Account-wide (User) | Config file the agent can read (User) | **High** | Remove it from the agent's reach now. Rotate it. Replace it with a project-scoped, read-only token. |
| Backup account credentials | Unknown | Agent cannot access (User, not verified) | Unknown | Check that no token or login the agent can reach opens this account. |

## Environment Separation Audit

| Check | Status | Finding | Required Action |
|---|---|---|---|
| Runtime env verification | ✗ Unknown | No evidence the agent can tell staging from production. | Add a check that blocks any call when the target is not the expected environment. |
| Credential isolation | ✗ | A staging session can reach production through the config-file token (User). | Put production credentials where the agent cannot read them. |
| Infrastructure separation | Unknown | Not stated. | Confirm staging and production are separate projects or accounts. |
| Data isolation | Unknown | Not stated. | Confirm staging holds no real user data. |

## Destructive Action Inventory

| Action | Reversible? | Approval Gate? | Max Blast Radius | Recommendation |
|---|---|---|---|---|
| Delete production resources | N, unless a restore works (Unknown) | **N** (User) | Assumption: whole production database or volume | Human approval for every delete. Remove the capability from the agent. |
| Other production writes through the account-wide token | Unknown | N (assumption) | Whole account | Do not give write rights. |
| Staging deletes | Likely Y (Assumption) | Unknown | Staging only | Allow only if staging holds no real data. |

## Backup & Recovery Status

```
Backup location: Separate Railway account (User)
Backup-to-agent isolation: Pass (User, not verified)
Most recent backup: Unknown
Last recovery test: Never (User)
Estimated recovery time: Unknown
```

Isolation is good. It is the main thing that failed in [S13]. But a backup that was never restored is only a hope. Treat it as unproven.

## Top Risks

1. **Over-permissioned token in a readable file**
   - Likelihood: High. The agent only needs to read the file.
   - Impact: Any action on the whole production account.
   - Mitigation: Move it out of reach. Rotate it. Issue a narrow, read-only token.
   - Priority: **P0**
2. **No approval on production delete**
   - Likelihood: Medium to High. One wrong tool call is enough.
   - Impact: Production data gone in seconds.
   - Mitigation: Require a human to approve each delete, with the exact target shown.
   - Priority: **P0**
3. **Test and production mix-up**
   - Likelihood: Medium. One agent can reach both.
   - Impact: A staging task hits production.
   - Mitigation: Separate credentials per environment. Add an environment check before every call.
   - Priority: **P0**
4. **Recovery never tested**
   - Likelihood: Unknown.
   - Impact: Isolated backups may not restore, or may be too old.
   - Mitigation: Run a full restore into a clean environment. Time it. Record the age of the data.
   - Priority: **P0.** This is a launch blocker under the contract rule for unknown critical recovery paths.
5. **No kill switch or logs described**
   - Likelihood: Unknown.
   - Impact: Slow detection and unclear cause.
   - Mitigation: Add a way to halt the agent at once. Send logs to storage the agent cannot edit.
   - Priority: P1

## The SmarterX Test

YES means unsafe.

- [x] Could the agent find an over-permissioned credential in a readable file? **YES → P0**
- [x] Could the agent delete production data without human approval? **YES → P0**
- [x] Could a destructive action take effect in under 30 seconds with no intervention? **YES → P0.** Basis: no gate (User). Assumption: the API acts at once. [S13] reports 9 seconds.
- [ ] Could the agent reach or delete the backups needed to recover? **No** (User, not verified). Whether those backups are good enough is **Unknown**.
- [x] Could the agent act on the wrong environment? **YES → P0**

Four checks are YES. The agent should not run in production.

## Recommendations By Priority

**P0 — Block launch:**
- Take the production token away from the agent. Rotate it, because the agent could already have read it.
- Replace it with a narrow, read-only token, or no production access at all.
- Require human approval for every production delete.
- Add a runtime environment check.
- Restore a backup in a clean environment. Record how long it took and how old the data was.

**P1 — Within 30 days:**
- Add a kill switch.
- Send logs to storage the agent cannot edit.
- Check that backup-account credentials are out of the agent's reach.

**P2 — Monitor:**
- Rotate tokens on a schedule.
- Repeat the restore test every 90 days.
- Re-run this audit when the agent gets a new tool or credential.

## Audit & Observability Recommendations

- Log each tool call: time, tool, target environment, target resource, approver. Do not log secret values.
- Store logs somewhere the agent cannot write or delete.
- Alert on any production call from this agent and on any delete.
- Keep logs long enough to cover the time it takes you to notice an incident. Period: Unknown, you must set it.

## Pressure-Test Questions

- If the agent did its worst action today, would you know in 1 minute? In 1 hour? In 1 day?
- If the isolated backup is 6 months old, can the business live with that?
- Who is the named owner who accepts the risk if you keep production access?

## Questions I need answered (max 3)

1. Which service does the production token control: Railway only, or other services too?
2. How old is the newest backup, and how often is it taken?
3. Can you halt the agent at once today, and where do its logs go?

### Artifact handoff
Suggested path: .agent-pm/internal-coding-agent/risk-audit.md
Upstream artifacts used: None
Decisions to carry forward: Production token leaves the agent's reach and gets rotated. Every production delete needs human approval. Agent cannot reach production credentials. Restore test is a launch blocker.
Assumptions / Unknowns: Delete takes effect at once. Blast radius is the full production database. Backup age, restore time, staging data type, kill switch, and log storage are unknown. Backup isolation is user-provided and not verified.
Recommended next command: /agent-pm:guardrails-plan
