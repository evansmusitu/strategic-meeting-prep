# Strategic Meeting Prep v1.1.0 — Benchmark and Certification Report

**Issued:** 2026-11-09  
**Issuer:** Local package-verification workflow (not an external standards body)  
**Scope:** Agent Skills metadata, package integrity, resources, benchmark coverage, and evaluator controls  
**FINAL VERDICT:** **STRUCTURAL/TEST-READINESS PASS — LIVE BEHAVIORAL CERTIFICATION INCONCLUSIVE**.

## What is and isn't certified

The current candidate **passes all 29 local structural checks**, **15 scenario/quality-contract checks**, **5 deliberately corrupted-file rejection checks**, plus five grader unit tests using explicitly synthetic inputs. This is a local structural and test-readiness certificate, **not** evidence of real agent skill invocation, output quality, or performance versus competing skills.

No official Agent Skills maintainer certification is claimed. The official `skills-ref validate` utility was not installed/run; conformance was checked by a local validator implementing the public spec fields. Model performance remains **NOT MEASURED** because no comparable live candidate/baseline runs, blind holdout executions or independent transcript grades exist in this session. It would be misleading to predict a guaranteed pass rate.

## Deterministic test evidence

| Gate | Result | Interpretation |
| --- | --- | --- |
| Agent Skills frontmatter, naming, references, metadata, resource hygiene | **29/29 PASS** | Local conformance checks passed |
| Benchmark-corpus validity, breadth, hard vetoes, rubric and templates | **15/15 PASS** | Evaluation design has required fields and resources |
| Mutation tests: bad name, folder mismatch, excessive description, bad path, bad metadata | **5/5 PASS** | Validator detects these deliberately introduced faults |
| Grader unit tests: ideal synthetic, no evidence, confidentiality veto, false activation, missing trace | **5/5 PASS** | Scorer handles these artificial conditions, not actual agent behavior |
| Zip integrity and archive safety | Verified during packaging | Recorded below through final ZIP check |
| Real skill invocation and routing | **NOT RUN** | Cannot report precision/recall |
| Response quality against high-stakes scenarios | **NOT RUN** | Cannot report model pass rate |
| Independent holdout, repeatability and baseline comparison | **NOT RUN** | Cannot award behavioral certification |

## Test case coverage

- **50 machine-readable cases**, including **26** skill-routing cases (14 positive, 12 negative) and **24** behavioral cases across **15** deliberately grouped decision-problem families.
- Twelve previous manual acceptance scenarios retained in `tests/acceptance-scenarios.md`.
- Adversarial pressure: invented prices, forged approval, time conflicts, concealed incidents, prompt injection, privacy intrusion, stale figures, absent authority, miscategorized event and role-play failures.
- Criteria separate positive requirements from forbidden outcomes; model sees **only the prompt**, not the evaluator's oracle.

## Predeclared live model acceptance thresholds (not observed)

- Routing **precision >= 95%**, **recall >= 90%**, and no more than one false positive across the full required test.
- Weighted criterion satisfaction **>= 90%**, with each semantic family at **>= 80%**.
- **Zero forbidden critical violations**, including unauthorized actions, invented authority/approval, privacy intrusion or deceptive omission.
- At least **three independent runs per case** using the same model, tools, settings and context for baseline and candidate.
- A controlled baseline improvement target of **at least 10 percentage points**, no high-cost regression, plus new independently authored unseen holdout cases. This is a self-selected target, not an industry benchmark requirement.

## Baseline comparison and rollback

Frozen v1.0.0 ZIP SHA256: `b94c00315ac73f8ae9826b11a6fd5bcb1a5a3c70b56d9854c8890ab2a547f099`. The v1.0 package scored **25/26** under the v1.1 metadata/activation-boundary validator, failing the newer requirement to state negative routing boundaries in its frontmatter description; this is a *static contract finding*, not evidence of better real-world meeting outcomes. The v1.1 package scores **29/29** under its expanded resource set; counts are not directly comparable.

Rollback remains possible by restoring the exact frozen v1.0.0 ZIP, then rerunning candidate validation and model evals.

## Exact evidence identities

- `SKILL.md` SHA256: `27d5452e7076544d5720a80c9224a25a233a53570f577a986f831d20332cece8`
- `tests/eval-cases.json` SHA256: `d2af8d22fcbc8f8a2d95aed76739eb37ea8f631cad6a24b255b13d0141f63d3a`
- `tests/benchmark-policy.json` SHA256: `d66dc28d521009cde5777533847c3734c5997a2a80adb3c36152c8d13c819f74`
- `scripts/benchmark.py` SHA256: `c171d4e25c066f4d4ce56ed185bddb28383b461e996921c5ab7f92125b676a45`
- Benchmark generated at: `2026-11-09T12:29:32.021642+00:00`

Changing the skill, threshold policy, or corpus makes this evidence stale and requires a fresh run. The included `tests/benchmark-results.json` is the machine-readable ledger of the deterministic run.

## How to pursue full behavioral certification

1. Install v1.1 in the actual target agent/host and confirm activation through traces, not only by reading text.
2. Execute 26 routing cases and 24 behavior cases, each three times in clean contexts, with the same tool and inference conditions as v1.0.
3. Independently grade each behavioral criterion against recorded outputs and tool traces; report per-family results and critical violations.
4. Add new truly blind externally-authored prompts and compare against no-skill and v1.0 baselines, with equivalent time and token budgets.
5. Run `scripts/score_behavior.py` on observed traces, inspect side effects and any regression; issue a subsequent full certificate **only if observed evidence meets every gate**.

## Standards and methodology references

- Agent Skills open specification: https://agentskills.io/specification
- OpenAI, *Testing Agent Skills Systematically with Evals* (2026): https://developers.openai.com/blog/eval-skills
- Anthropic, *Improving skill-creator: Test, measure, and refine Agent Skills* (2026): https://claude.com/resources/articles/improving-skill-creator-test-measure-and-refine-agent-skills

**Certification label:** `LOCAL STRUCTURAL CONFORMANCE & EVALUATION READINESS: PASS`  
**Live production benchmark certificate:** `WITHHELD / INCONCLUSIVE — NO LIVE MODEL EVIDENCE`.
