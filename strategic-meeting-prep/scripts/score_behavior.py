#!/usr/bin/env python3
"""Score independently reviewed trace observations, without pretending to run or grade an LLM.
Usage: python scripts/score_behavior.py CASES POLICY OBSERVATIONS
"""
from __future__ import annotations
from pathlib import Path
from collections import defaultdict
import json
import sys


def score(casesfile,policyfile,observationsfile):
    cases=json.loads(Path(casesfile).read_text()); policy=json.loads(Path(policyfile).read_text()); observations=json.loads(Path(observationsfile).read_text())
    routing={c['id']:c for c in cases['routing']}; behavior={c['id']:c for c in cases['behavior']}
    results=defaultdict(list); errors=[]
    for r in observations.get('runs',[]):
        cid=r.get('case_id'); repeat=r.get('repeat'); key=(cid,repeat)
        if cid not in routing and cid not in behavior: errors.append(f'Unknown ID {cid}'); continue
        if not isinstance(repeat,int) or repeat<1: errors.append(f'Invalid repeat for {cid}'); continue
        if any(z.get('repeat')==repeat for z in results[cid]): errors.append(f'Duplicate {key}'); continue
        if not r.get('evidence'):errors.append(f'Missing trace evidence for {key}')
        if cid in routing and not isinstance(r.get('triggered'),bool):errors.append(f'Missing observed activation for {key}')
        if cid in behavior:
            if not isinstance(r.get('observed'),list) or not isinstance(r.get('violations'),list):errors.append(f'Missing graded criterion lists for {key}')
            if set(r.get('observed',[]))-set(behavior[cid]['must_observe']):errors.append(f'Unknown observed criterion for {key}')
            if set(r.get('violations',[]))-set(behavior[cid]['must_not_observe']):errors.append(f'Unknown forbidden criterion for {key}')
        results[cid].append(r)
    N=policy['behavior']['min_repeats']
    expected=set(routing)|set(behavior)
    missing=[cid for cid in sorted(expected) if len(results[cid])<N]
    if errors or missing:
        return {'verdict':'INCONCLUSIVE','errors':errors,'missing_or_underrepeated':missing,'message':'No model pass claim without complete, independently observed traces.'}
    tp=fp=fn=0
    for cid,c in routing.items():
        for r in results[cid][:N]:
            if r['triggered'] and c['should_trigger']:tp+=1
            elif r['triggered'] and not c['should_trigger']:fp+=1
            elif not r['triggered'] and c['should_trigger']:fn+=1
    precision=tp/(tp+fp) if tp+fp else 0
    recall=tp/(tp+fn) if tp+fn else 0
    observed=total=0
    violations=[]; slice_num=defaultdict(int);slice_den=defaultdict(int)
    for cid,c in behavior.items():
        for r in results[cid][:N]:
            num=len(set(r['observed']))
            observed+=num*c['weight']; total+=len(c['must_observe'])*c['weight']
            slice_num[c['family']]+=num; slice_den[c['family']]+=len(c['must_observe'])
            if r['violations']:violations.append({'case_id':cid,'repeat':r['repeat'],'violations':r['violations']})
    score=observed/total if total else 0
    slices={k:v/slice_den[k] for k,v in slice_num.items()}
    passed=(precision>=policy['routing']['precision_min'] and recall>=policy['routing']['recall_min'] and fp<=policy['routing']['false_positive_max'] and score>=policy['behavior']['observed_criteria_min'] and all(x>=policy['behavior']['family_pass_min'] for x in slices.values()) and not violations)
    # This assesses candidate only. Baseline and blind holdout must still be separately evidenced.
    return {'verdict':'CANDIDATE CHECK PASS - FULL CERTIFICATION PENDING' if passed else 'FAIL','routing_precision':precision,'routing_recall':recall,'routing_false_positives':fp,'behavior_criteria_rate':score,'family_rates':slices,'forbidden_violations':violations,'baseline_comparison':'REQUIRES SEPARATE RUN','independent_blind_holdout':'REQUIRES SEPARATE RUN'}

if __name__=='__main__':
    if len(sys.argv)!=4:raise SystemExit('Usage: score_behavior.py CASES POLICY OBSERVATIONS')
    print(json.dumps(score(*sys.argv[1:]),indent=2))
