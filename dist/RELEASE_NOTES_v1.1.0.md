# Strategic Meeting Prep — v1.1.0 Release Notes

**Release date:** 2026-11-09  
**Type:** Distributable Agent Skill package  
**Release status:** Locally verified; live behavioral certification pending  
**Skill ID:** `strategic-meeting-prep`

## What ships

A reusable evidence-grounded preparation agent for interviews, project reviews, negotiations, executive sessions, client calls, and technical discussions. Supports Flash, Standard, and High-Stakes meeting preparation, with decision strategy, stakeholder mapping, evidence freshness gates, realistic objections, speaking scripts, and follow-through plans.

## Improvements over v1.0.0

- Explicit activation and non-trigger routing boundaries for scheduling-only and past-minutes tasks.
- Separates evidence, hypotheses, decisions and proposals; introduces material-fact freshness checks and permission controls.
- Better guidance for counterparty objections, decision memos, multi-party negotiations and adversarial role-play.
- Advanced high-stakes decision paths and failure-recovery playbooks.
- New templates, substantive references and machine-readable benchmark cases.
- Deterministic validator, mutation tests, scored evaluation framework and rollback baseline.

## Fresh release verification

- Agent Skills local structural validation: **29/29 PASS**.
- Eval corpus and quality-contract checks: **15/15 PASS**.
- Deliberate validation mutation checks: **5/5 PASS**.
- Synthetic scorer unit tests: **5/5 PASS**.
- ZIP CRC, archive path safety and source-file byte equality: **PASS**.
- Test corpus: 50 scenarios (26 routing; 24 behavioral, across 15 families).
- Evidence timestamp: `2026-11-09T12:33:15.451515+00:00` (UTC).

**Important:** These are deterministic checks of the skill package and evaluation apparatus, **not** measurements of live agent quality. The skill has not passed the predeclared live behavior thresholds because its required live baseline/candidate tests have not been executed. No external agency or official Agent Skills certification is implied.

## Release limitations

- Distribution and installation depend on the target agent host; ZIP download alone does not activate the skill.
- The package does not include a public reuse license. Obtain a license choice from its owner before labeling it open source or publishing with a license.
- Connectors, messages, calendar edits and external actions require the host to provide access and the user's authorization; none are automatically enabled.

## Contents

- `strategic-meeting-prep-v1.1.0.zip` — installable skill folder archive.
- `BENCHMARK_CERTIFICATE_v1.1.0.md` — scoped local verification report.
- `INSTALL_AND_ROLLBACK.md` — host-agnostic installation, smoke tests and rollback steps.
- `SHA256SUMS.txt` — integrity hashes for released files.
- `RELEASE_MANIFEST.json` — release file identities and benchmark status.

## Next certification milestone

Execute the 50-case baseline/candidate eval protocol with repeat trials, independent grading, tool traces and new unseen holdouts. Publish a separate live-behavior certificate only when all thresholds are met. See `tests/RUNBOOK.md` inside the skill archive.