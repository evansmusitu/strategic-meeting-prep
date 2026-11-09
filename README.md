# Strategic Meeting Prep — Agent Skill

**Version:** 1.1.0 · **Status:** [Public GitHub release](https://github.com/evansmusitu/strategic-meeting-prep/releases/tag/v1.1.0) · **Behavioral certification:** pending.

Strategic Meeting Prep is a reusable Agent Skill for evidence-grounded meeting briefs, stakeholder intelligence, decision strategy, interview and negotiation rehearsal, difficult questions, and accountable follow-up. It supports flash, standard and high-stakes preparation.

## Get the installable skill

**[Download Strategic Meeting Prep v1.1.0 ZIP](https://github.com/evansmusitu/strategic-meeting-prep/releases/download/v1.1.0/strategic-meeting-prep-v1.1.0.zip)**

The exact 26-file archive is available on the [GitHub Releases page](https://github.com/evansmusitu/strategic-meeting-prep/releases/tag/v1.1.0). GitHub's reported digest and local SHA-256 both equal:

`742ec8009110e7e918ff7990eb51dd7325564456f7c7d57b3110c23f56c89e33`

Download, extract and install its `strategic-meeting-prep/` directory using an Agent Skills-compatible host. A ZIP download alone does not activate the skill.

## Example usage

> Prepare me for tomorrow's steering committee. I need approval for a two-week pilot. Give me evidence-backed talking points, likely objections and a 60-second brief.

> Rehearse the hardest questions for my admissions interview, using only qualifications I actually have.

> My supplier call starts in five minutes. What's my most important question and closing ask?

For more, read [the skill instructions](strategic-meeting-prep/SKILL.md), [installation guidance](dist/INSTALL_AND_ROLLBACK.md), and [release notes](dist/RELEASE_NOTES_v1.1.0.md).

## Testing and certification

The frozen release passed **29/29 structural**, **15/15 evaluation-corpus**, **5/5 mutation** and **5/5 unit tests**, plus ZIP integrity and source parity checks. These results verify packaging and evaluation readiness only. **No live agent behavior, customer outcomes or revenue performance have been certified.** See the [benchmark certificate](dist/BENCHMARK_CERTIFICATE_v1.1.0.md) and [release status](RELEASE_STATUS.md).

To rerun deterministic checks from the repository:

```bash
python strategic-meeting-prep/scripts/run_checks.py
```

## Ownership and safety

**No public reuse license is currently granted.** Public access does not constitute open-source licensing. See [license status](LICENSE_STATUS.md).

The skill does not automatically access Gmail, calendars, files, or external accounts, nor may it commit or send on the user's behalf without authorization. GitHub publication is not Agensi marketplace onboarding.

