import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED_COMMANDS = {
    "qualify-agent",
    "architecture-pattern",
    "agent-spec",
    "tool-design-review",
    "eval-design",
    "cost-model",
    "guardrails-plan",
    "risk-audit",
    "agent-ux-review",
    "autonomy-slider",
    "prod-readiness",
    "failure-mode-map",
}


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def skill(name):
    return read(f"skills/{name}/SKILL.md")


class RepositoryTests(unittest.TestCase):
    def test_expected_command_set(self):
        actual = {path.parent.name for path in SKILLS.glob("*/SKILL.md")}
        self.assertEqual(actual, EXPECTED_COMMANDS)
        stray = [path for path in SKILLS.glob("*/SKILL.md") if path.parent.name not in EXPECTED_COMMANDS]
        self.assertEqual(stray, [])

    def test_frontmatter_names_match_directories(self):
        for name in EXPECTED_COMMANDS:
            with self.subTest(command=name):
                text = skill(name)
                self.assertTrue(text.startswith("---\n"))
                self.assertRegex(text, rf"(?m)^name: {re.escape(name)}$")
                self.assertIn("description:", text.split("---", 2)[1])
                self.assertIn("argument-hint:", text.split("---", 2)[1])

    def test_every_command_uses_shared_contract(self):
        for name in EXPECTED_COMMANDS:
            with self.subTest(command=name):
                text = skill(name)
                self.assertIn("$ARGUMENTS", text)
                self.assertIn("references/operating-contract.md", text)
                self.assertIn("references/sources.md", text)

    def test_artifact_owners_cover_every_command(self):
        contract = read("references/operating-contract.md")
        rows = re.findall(r"^\| `[^`]+` \| `([^`]+)` \|$", contract, re.MULTILINE)
        self.assertEqual(set(rows), EXPECTED_COMMANDS)
        self.assertEqual(len(rows), len(EXPECTED_COMMANDS))
        self.assertIn(".agent-pm/<project-slug>/", contract)
        self.assertIn("Do not create or modify artifacts unless the user asks", contract)

    def test_source_ids_are_defined(self):
        sources = read("references/sources.md")
        defined = set(re.findall(r"(?m)^(?:### | - |)\[(S\d{2})\]", sources))
        defined.update(re.findall(r"(?m)^- \[(S\d{2})\]", sources))
        for source_id in ("S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08", "S09", "S10", "S11", "S12", "S13", "S14", "S15"):
            self.assertIn(source_id, defined)
        for name in EXPECTED_COMMANDS:
            with self.subTest(command=name):
                used = set(re.findall(r"\[(S\d{2})\]", skill(name)))
                self.assertTrue(used <= defined)

    def test_known_source_corruptions_stay_removed(self):
        combined = "\n".join(skill(name) for name in EXPECTED_COMMANDS)
        forbidden = (
            "40% task completion improvement",
            "40% improvement came from rewriting",
            "20% of one FTE",
            "30-day correction loop is non-negotiable",
            "Readiness: [%]",
            "Single agent (orchestrator-workers)",
            "Most \"AI agent launches\" that fail in public failed at operations",
        )
        for phrase in forbidden:
            with self.subTest(phrase=phrase):
                self.assertNotIn(phrase, combined)

    def test_risk_audit_uses_consistent_unsafe_yes_checks(self):
        text = skill("risk-audit")
        section = text.split("### The SmarterX Test", 1)[1].split("### Recommendations By Priority", 1)[0]
        self.assertIn("YES means unsafe", section)
        self.assertIn("Could the agent reach or delete the backups", section)
        self.assertNotIn("Are backups isolated from the agent's blast radius?", section)
        self.assertIn("Mark a check `Unknown`, not `No`", section)

    def test_autonomy_model_is_shared(self):
        for name in ("autonomy-slider", "agent-spec", "agent-ux-review"):
            with self.subTest(command=name):
                text = skill(name)
                for position in ("0: Manual", "1: Suggestion", "2: Single-action", "3: Task-level", "4: Full autonomy"):
                    self.assertIn(position, text)

    def test_high_risk_policy_is_shared(self):
        for name in ("autonomy-slider", "tool-design-review", "guardrails-plan", "risk-audit", "failure-mode-map"):
            with self.subTest(command=name):
                self.assertIn("explicit risk acceptance", skill(name))

    def test_cost_model_avoids_stale_prices_and_double_counting(self):
        text = skill("cost-model")
        self.assertIn("Never multiply an itemized call-by-call estimate", text)
        self.assertIn("do not substitute a stale tier table", text)
        self.assertNotIn("GPT-3.5 class", text)
        self.assertNotIn("$75", text)

    def test_eval_design_separates_data_and_metrics(self):
        text = skill("eval-design")
        self.assertIn("held-out test", text)
        self.assertIn("development data only", text)
        self.assertIn("synthetic cases may supplement scenario coverage", text)
        self.assertIn("do not substitute one for another", text)

    def test_example_has_complete_core_handoffs(self):
        expected = {
            "01-qualification.md",
            "02-architecture.md",
            "agent-spec.md",
            "eval-plan.md",
            "cost-model.md",
            "production-readiness.md",
        }
        for filename in expected:
            with self.subTest(example=filename):
                text = read(f"examples/billing-support/{filename}")
                self.assertIn("### Artifact handoff", text)
                self.assertIn("Assumptions / Unknowns:", text)

    def test_local_markdown_links_exist(self):
        for filename in ("README.md", "CONTRIBUTING.md", "evals/README.md", "examples/billing-support/README.md"):
            with self.subTest(document=filename):
                text = read(filename)
                for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
                    if re.match(r"^[a-z]+://", target) or target.startswith("#"):
                        continue
                    clean = target.split("#", 1)[0]
                    self.assertTrue((ROOT / filename).parent.joinpath(clean).exists(), target)

    def test_manifest_and_changelog_versions_match(self):
        manifest = json.loads(read(".claude-plugin/plugin.json"))
        self.assertEqual(manifest["name"], "agent-pm")
        self.assertIn(f"## {manifest['version']} ", read("CHANGELOG.md"))


if __name__ == "__main__":
    unittest.main()
