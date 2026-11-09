# Strategic Meeting Prep — Agent Skill v1.1.0

A reusable, evidence-grounded meeting preparation workflow for ChatGPT Work and compatible Agent Skills hosts. It turns scattered context into a 60-second brief, a strategic decision plan, an agenda, stakeholder questions, difficult-question rehearsal, and follow-through. It also supports interviews, sales, technical reviews, executive sessions, negotiations and difficult conversations.

## Package

- `SKILL.md` — required, self-contained operating procedure and trigger metadata
- `agents/openai.yaml` — optional user-facing identity
- `references/` — evidence, stakeholder/negotiation, archetype and quality protocols, loaded only when relevant
- `assets/` — fillable briefing, pre-read, and follow-up templates
- `tests/acceptance-scenarios.md` — behavioral evaluation suite
- `scripts/validate_skill.py` — local specification and structure checks
- `scripts/benchmark.py` — deterministic package and eval-corpus verification (NOT a substitute for live model testing)
- `scripts/score_behavior.py` — scorer for externally captured agent runs and human-reviewed grades
- `tests/eval-cases.json` — routing and behavioral cases with semantic labels and independent oracle
- `tests/benchmark-policy.json` — predeclared performance thresholds; change only through a new version
- `references/decision-intelligence.md`, `rehearsal-and-coaching.md`, `operations-and-handoff.md` — deeper decision and operations procedures

## Examples of prompts

- "Prepare me for tomorrow's project steering committee. Our goal is approval for a two-week pilot."
- "I have a university admissions interview next week; simulate hard questions and help me prepare evidence from my actual qualifications."
- "Research the public context for my client call and build a high-stakes meeting brief, with source dates."
- "Give me the 60-second brief for a technical design review, then role-play the hardest stakeholder."
- "Convert my meeting notes into a decision log and a follow-up draft; don't send it."

## Installing / using

Install the **folder**, preserving `SKILL.md` at its root, using your host's Agent Skills/skill-creator workflow. In a Codex project, a typical repository location is `.agents/skills/strategic-meeting-prep/`. Skill availability in ChatGPT depends on the host and installation method; merely downloading this ZIP does **not** automatically install or activate it. For wider ChatGPT distribution, bundle into a plugin using the supported skill-creator/plugin flow.

The skill does not require connected apps; with user-authorized calendar, email, document or web access, it can use relevant context. Installing it does not by itself grant access or sending permissions.

## Design principles

Decision first; source before certainty; respect authority; keep first screen short; offer deep analysis only where stakes justify it; no guessed logistics, numbers, motives or commitments; human-usable speakable scripts; clear follow-through.

## Version

1.1.0 — 2026-11-09. Expanded to the open Agent Skills `SKILL.md` format; not certified by the spec maintainers or evaluated in a production harness.

## Certification meaning

A passing local benchmark certifies only the package's declared structural and coverage checks. It **does not** prove an actual model invoked this skill, that external connectors worked, or that responses satisfy the behavioral rubric. Those require captured test runs with the skill activated, baseline without skill, an isolated holdout set, human grading and repeat trials. The benchmark report records each category separately. No official certification from Agent Skills maintainers is implied.

Run `python scripts/validate_skill.py` and `python scripts/benchmark.py`. For live behavior evaluation, follow `tests/RUNBOOK.md` with prompt-only inputs and pass the resulting grades to `scripts/score_behavior.py`.