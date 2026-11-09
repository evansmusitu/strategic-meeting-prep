# Strategic Meeting Prep — Agent Skill

**Version:** 1.1.0 · **Status:** GitHub source staging; frozen release ZIP upload pending; behavioral certification not yet measured.

Strategic Meeting Prep is a reusable Agent Skill for evidence-grounded meeting briefs, decision strategies, stakeholder intelligence, difficult questions, interview and negotiation rehearsal, and accountable follow-up.

## Publication status

The GitHub repository contains the principal skill instructions, documentation, certification report and an automated release workflow. **The complete 26-file installable ZIP is not yet uploaded, and the GitHub Release is not yet public.** For current status, inspect [Releases](../../releases) rather than treating documentation as publication proof.

### Complete v1.1.0 publication

1. Download the frozen `strategic-meeting-prep-v1.1.0.zip` from the ChatGPT release conversation.
2. [Upload it to the `dist/` directory on `main`](https://github.com/evansmusitu/strategic-meeting-prep/upload/main/dist), preserving its filename.
3. The [finalization workflow](.github/workflows/complete-release.yml) verifies its fixed SHA-256, extracts the complete source, runs the deterministic checks, and attempts to publish the immutable `v1.1.0` GitHub Release.
4. Verify the [public release](../../releases/tag/v1.1.0) actually exists and contains the ZIP and notes. An Actions run alone is not proof of release.

Expected SHA-256:

`742ec8009110e7e918ff7990eb51dd7325564456f7c7d57b3110c23f56c89e33`

## Example usage

> Prepare me for tomorrow's steering committee. I need approval for a two-week pilot. Give me evidence-backed talking points, likely objections, and a 60-second brief.

> Rehearse the hardest questions for my admissions interview, using only qualifications I actually have.

> My supplier call starts in five minutes. What's the most important question and closing ask?

See [skill instructions](strategic-meeting-prep/SKILL.md), [skill README](strategic-meeting-prep/README.md), and [publishing guide](PUBLISHING.md).

## Test evidence

The frozen local candidate passed **29/29 structural**, **15/15 evaluation-corpus**, **5/5 mutation**, and **5/5 evaluator unit tests**, plus ZIP integrity and source parity checks. These are deterministic package checks, **not** evidence of production agent performance. Live behavioral certification remains **inconclusive**.

Details: [benchmark certificate](dist/BENCHMARK_CERTIFICATE_v1.1.0.md).

## License

No public reuse license has been selected. Public visibility alone does not authorize third-party modification or redistribution. See [license status](LICENSE_STATUS.md).

The skill does not automatically gain access to any calendar, email, account or connector; all external actions remain subject to user authorization.