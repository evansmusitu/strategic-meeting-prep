#!/usr/bin/env python3
"""Unit tests for the scorer using SYNTHETIC labels, never actual agent evidence."""
from __future__ import annotations
from pathlib import Path
import importlib.util
import json
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('score_behavior',ROOT/'scripts/score_behavior.py')
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

class TestScorer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases=ROOT/'tests/eval-cases.json'; cls.policy=ROOT/'tests/benchmark-policy.json'
        cls.corpus=json.loads(cls.cases.read_text())
    def run_case(self,data):
        with tempfile.TemporaryDirectory(prefix='meeting-grade-unit-') as tmp:
            fn=Path(tmp)/'synthetic.json'; fn.write_text(json.dumps({'runs':data}))
            return mod.score(self.cases,self.policy,fn)
    def ideal_runs(self):
        rows=[]
        for repeat in (1,2,3):
            for r in self.corpus['routing']:
                rows.append({'case_id':r['id'],'repeat':repeat,'triggered':r['should_trigger'],'evidence':'synthetic unit-test trace'})
            for r in self.corpus['behavior']:
                rows.append({'case_id':r['id'],'repeat':repeat,'observed':r['must_observe'],'violations':[],'evidence':'synthetic unit-test trace'})
        return rows
    def test_no_evidence_inconclusive(self):
        self.assertEqual(self.run_case([])['verdict'],'INCONCLUSIVE')
    def test_ideal_synthetic_never_full_certified(self):
        x=self.run_case(self.ideal_runs())
        self.assertEqual(x['verdict'],'CANDIDATE CHECK PASS - FULL CERTIFICATION PENDING')
        self.assertEqual(x['routing_precision'],1.0)
        self.assertEqual(x['behavior_criteria_rate'],1.0)
    def test_critical_violation_vetoes(self):
        runs=self.ideal_runs()
        for r in runs:
            if r['case_id']=='BH-14':r['violations']=['external_send']; break
        self.assertEqual(self.run_case(runs)['verdict'],'FAIL')
    def test_false_trigger_regression_fails(self):
        runs=self.ideal_runs()
        for r in runs:
            if r['case_id']=='RT-N-01':r['triggered']=True
        self.assertEqual(self.run_case(runs)['verdict'],'FAIL')
    def test_no_trace_evidence_is_inconclusive(self):
        runs=self.ideal_runs(); runs[0]['evidence']=''
        self.assertEqual(self.run_case(runs)['verdict'],'INCONCLUSIVE')

if __name__=='__main__':unittest.main(verbosity=2)
