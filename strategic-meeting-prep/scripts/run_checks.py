#!/usr/bin/env python3
"""One-command local verification of skill and benchmark tooling."""
import subprocess
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
for p in [ROOT/'scripts/validate_skill.py',ROOT/'scripts/benchmark.py',ROOT/'tests/test_score_behavior.py']:
    print(f'\n>>> {p.relative_to(ROOT)}',flush=True)
    result=subprocess.run([sys.executable,str(p)],cwd=ROOT)
    if result.returncode:
        print(f'FAIL: {p.name} exit={result.returncode}',flush=True)
        raise SystemExit(result.returncode)
print('\nALL LOCAL DETERMINISTIC CHECKS PASSED. LIVE MODEL BENCHMARK NOT RUN.',flush=True)
