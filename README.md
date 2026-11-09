# Strategic Meeting Prep — Agent Skill

**Version:** 1.1.0  ·  **Release:** 2026-11-09  ·  **Status:** Locally verified; live behavior certification pending.

Strategic Meeting Prep is an Agent Skill that turns scattered meeting context into an evidence-grounded 60-second brief, stakeholder questions, decision strategy, rehearsal, and action-oriented follow-up. It supports urgent, routine, and high-stakes preparations for interviews, executive reviews, sales calls, negotiations, technical design meetings, and difficult conversations.

## Get the skill

Download the installable skill from this repository’s **Releases → v1.1.0** page **after** the GitHub release workflow completes. The identical, locally validated archive is checked in as [`dist/strategic-meeting-prep-v1.1.0.zip`](dist/strategic-meeting-prep-v1.1.0.zip). Extract the ZIP and import its `strategic-meeting-prep/` directory through the supported Agent Skills workflow on your host. A download does **not** activate the skill automatically.

## Usage

> Prepare me for tomorrow's steering committee. I need approval for a two-week pilot. Give me evidence-backed talking points, likely objections, and a 60-second brief.

> Rehearse the hardest questions for my admissions interview, using only qualifications I actually have.

> My supplier call starts in five minutes. What's the most important question and closing ask?

See [`strategic-meeting-prep/README.md`](strategic-meeting-prep/README.md) for full usage and [`dist/INSTALL_AND_ROLLBACK.md`](dist/INSTALL_AND_ROLLBACK.md) for installation and rollback.

## Quality and certification

Local checks: **29/29** structural, **15/15** evaluation-corpus checks, **5/5** mutation, **5/5** scorer unit tests, and ZIP integrity: **passed**. This is **not** live-model performance evidence. Behavioral certification remains **inconclusive** pending baseline/candidate runs, independent grading, and fresh blind holdouts. See [`dist/BENCHMARK_CERTIFICATE_v1.1.0.md`](dist/BENCHMARK_CERTIFICATE_v1.1.0.md).

To rerun locally:

```bash
python strategic-meeting-prep/scripts/run_checks.py
cd dist && sha256sum -c SHA256SUMS.txt
```

## Repository layout

- `strategic-meeting-prep/` — installable Agent Skill source, tests and support docs.
- `dist/` — frozen v1.1.0 release archive, notes, hashes and certification.
- `.github/workflows/` — continuous checks and tag-triggered GitHub Release creation.
- `publish-github.sh` — safe publisher for a new public repository under your authenticated account.

## License and support

**No public reuse license has been granted.** The files are publicly inspectable if this repository is made public, but that does not make them open-source licensed. The owner must explicitly select a license before downstream redistribution/modification is permitted. Contributions should not be submitted until a contribution license is chosen.

The skill does not grant connector access or permission to send messages or change calendars. It must respect user authorization. No official certification by Agent Skills maintainers is implied.