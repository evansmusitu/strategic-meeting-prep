#!/usr/bin/env python3
"""Repeatable deterministic package / corpus benchmark; NOT a live agent benchmark."""
from __future__ import annotations
from collections import Counter
from datetime import datetime,timezone
from hashlib import sha256
from pathlib import Path
import argparse
import json
import re
import subprocess
import sys
import tempfile
import shutil

ROOT=Path(__file__).resolve().parents[1]

def hashfile(path): return sha256(path.read_bytes()).hexdigest()

def run_check(root):
    p=subprocess.run([sys.executable,str(ROOT/'scripts/validate_skill.py'),'--root',str(root),'--json'],capture_output=True,text=True)
    if not p.stdout.strip(): return {'status':'FAIL','errors':[p.stderr]}
    return json.loads(p.stdout)

def mutation_suite():
    variants={
        'reject-invalid-name':lambda s:s.replace('name: strategic-meeting-prep','name: Strategic--Meeting-Prep',1),
        'reject-mismatched-folder-name':lambda s:s.replace('name: strategic-meeting-prep','name: another-skill',1),
        'reject-overlong-description':lambda s:re.sub(r'^description: .+$','description: '+('x'*1100),s,count=1,flags=re.M),
        'reject-bad-reference':lambda s:s+'\nSee `references/does-not-exist.md` for critical instructions.\n',
        'reject-invalid-metadata':lambda s:s.replace('version: "1.1.0"','version: 1.1',1),
    }
    original=(ROOT/'SKILL.md').read_text(encoding='utf8')
    outcomes={}
    with tempfile.TemporaryDirectory(prefix='meeting-skill-mutations-') as tmp:
        temp=Path(tmp)/ROOT.name
        shutil.copytree(ROOT,temp)
        for label,mutator in variants.items():
            (temp/'SKILL.md').write_text(mutator(original),encoding='utf8')
            result=run_check(temp)
            outcomes[label]='PASS' if result['status']=='FAIL' else 'FAIL'
    return outcomes

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--output',type=Path,default=ROOT/'tests/benchmark-results.json')
    args=parser.parse_args()
    structural=run_check(ROOT)
    corpus=json.loads((ROOT/'tests/eval-cases.json').read_text())
    policy=json.loads((ROOT/'tests/benchmark-policy.json').read_text())
    cases=corpus['routing']+corpus['behavior']
    ids=[c['id'] for c in cases]
    families=Counter(c['family'] for c in corpus['behavior'])
    checks={
      'valid_corpus_metadata':corpus['version']==policy['version']=='1.1.0',
      'unique_case_ids':len(ids)==len(set(ids)),
      'routing_positive_and_negative':sum(x['should_trigger'] for x in corpus['routing'])>=10 and sum(not x['should_trigger'] for x in corpus['routing'])>=10,
      'semantic_family_breadth':len(families)>=policy['behavior']['min_distinct_families'],
      'behavioral_oracle_fields':all(x.get('must_observe') and x.get('must_not_observe') and isinstance(x.get('weight'),int) for x in corpus['behavior']),
      'all_prompts_present':all(len(x.get('prompt','').strip())>=30 for x in cases),
      'at_least_20_behavior_cases':len(corpus['behavior'])>=20,
      'strict_critical_veto':policy['behavior']['critical_forbidden_violations_max']==0,
      'multiple_runs_required':policy['behavior']['min_repeats']>=3,
      'pass_thresholds_declared':policy['behavior']['observed_criteria_min']>=0.90 and policy['routing']['precision_min']>=0.95,
      'runbook_exists':(ROOT/'tests/RUNBOOK.md').is_file(),
      'decision_guidance_substantive':(ROOT/'references/decision-intelligence.md').stat().st_size>=1000,
      'rehearsal_guidance_substantive':(ROOT/'references/rehearsal-and-coaching.md').stat().st_size>=1000,
      'tool_handoff_guidance_substantive':(ROOT/'references/operations-and-handoff.md').stat().st_size>=1000,
      'quick_and_decision_templates':all((ROOT/'assets'/p).is_file() for p in ['flash-card-template.md','decision-memo-template.md']),
    }
    mutations=mutation_suite() if structural['status']=='PASS' else {}
    static_pass=structural['status']=='PASS' and all(checks.values()) and all(x=='PASS' for x in mutations.values())
    report={
      'benchmark':'Strategic Meeting Prep deterministic package and corpus benchmark',
      'test_executed_at':datetime.now(timezone.utc).isoformat(),
      'candidate':'1.1.0',
      'baseline':'1.0.0 (frozen ZIP; controlled live comparison NOT performed)',
      'code_hash_sha256':hashfile(ROOT/'scripts/benchmark.py'),
      'skill_hash_sha256':hashfile(ROOT/'SKILL.md'),
      'corpus_hash_sha256':hashfile(ROOT/'tests/eval-cases.json'),
      'policy_hash_sha256':hashfile(ROOT/'tests/benchmark-policy.json'),
      'structural':structural,
      'corpus':{'total':len(cases),'routing':len(corpus['routing']),'routing_positive':sum(c['should_trigger'] for c in corpus['routing']),'routing_negative':sum(not c['should_trigger'] for c in corpus['routing']),'behavior':len(corpus['behavior']),'distinct_behavior_families':len(families),'case_distribution':dict(families)},
      'contract_coverage_checks':checks,
      'mutation_checks':mutations,
      'static_verdict':'PASS' if static_pass else 'FAIL',
      'live_model_execution':'NOT RUN',
      'model_trigger_precision':'NOT MEASURED',
      'model_trigger_recall':'NOT MEASURED',
      'behavior_pass_rate':'NOT MEASURED',
      'baseline_model_comparison':'NOT RUN',
      'independent_blind_holdout':'NOT RUN',
      'overall_certification':'INCONCLUSIVE - structural/coverage only' if static_pass else 'FAIL - deterministic gate',
      'limitations':'Static checks inspect package and rubric coverage, not agent activation or resulting quality. A fully passing certificate requires captured baseline and candidate model runs, three repeats, blind held-out cases and trace review.'
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print(f"{report['static_verdict']}: static package checks {structural['passed_checks']}/{structural['check_count']}; corpus checks {sum(checks.values())}/{len(checks)}; mutation checks {sum(x=='PASS' for x in mutations.values())}/{len(mutations)}")
    print(f"Corpus: {len(cases)} total, {len(corpus['routing'])} routing, {len(corpus['behavior'])} behavioral, {len(families)} semantic families")
    print('Behavioral certificate:',report['overall_certification'])
    print('Evidence:',args.output)
    return 0 if static_pass else 1

if __name__=='__main__':raise SystemExit(main())
