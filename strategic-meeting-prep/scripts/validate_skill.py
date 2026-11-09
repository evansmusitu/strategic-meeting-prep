#!/usr/bin/env python3
"""Validate Agent Skills package conformance; requires PyYAML for correct YAML parsing.
Usage: python scripts/validate_skill.py [--root DIR] [--json]
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path


def check(root: Path):
    errors, warnings, checks = [], [], []
    root = root.resolve()
    skill = root/'SKILL.md'
    def test(label, condition, detail=''):
        (checks if condition else errors).append(label if condition else f'{label}: {detail}')
    test('Required SKILL.md exists', skill.is_file(), 'missing SKILL.md')
    if not skill.is_file():
        return errors, warnings, checks
    txt = skill.read_text(encoding='utf8')
    front = re.match(r'\A---\s*\n(.*?)\n---\s*\n', txt, re.S)
    test('YAML frontmatter delimited', bool(front), 'expected two --- markers')
    if not front:
        return errors, warnings, checks
    try:
        import yaml
    except ImportError:
        errors.append('PyYAML unavailable: install pyyaml to validate complex YAML safely')
        return errors, warnings, checks
    try:
        fm = yaml.safe_load(front.group(1))
    except yaml.YAMLError as e:
        errors.append(f'YAML not parseable: {e}')
        return errors, warnings, checks
    test('Frontmatter is mapping', isinstance(fm,dict), 'must be mapping')
    if not isinstance(fm,dict):
        return errors, warnings, checks
    supported={'name','description','license','compatibility','metadata','allowed-tools'}
    test('Valid frontmatter fields', set(fm) <= supported, f'unsupported keys {sorted(set(fm)-supported)}')
    name=fm.get('name')
    test('Conformant name',isinstance(name,str) and bool(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name)) and len(name)<=64,'invalid characters/length/hyphens')
    test('Name matches folder',name == root.name,f'{name} != {root.name}')
    desc=fm.get('description')
    test('Description length and type',isinstance(desc,str) and 1<=len(desc)<=1024,'must be nonempty string <= 1024 chars')
    if isinstance(desc,str):
        test('Activation conditions in description',bool(re.search(r'\buse\s+(?:when|for)\b',desc,re.I)), 'state when to use')
        test('Negative routing described',bool(re.search(r'\bdo not use\b',desc,re.I)), 'state nearby non-trigger cases')
    compatibility=fm.get('compatibility','')
    test('Compatibility length',isinstance(compatibility,str) and len(compatibility)<=500,'max 500 characters')
    metadata=fm.get('metadata',{})
    test('Metadata values are strings',isinstance(metadata,dict) and all(isinstance(k,str) and isinstance(v,str) for k,v in metadata.items()),'values must be strings')
    if isinstance(metadata,dict):
        ver=metadata.get('version')
        test('Semantic version',isinstance(ver,str) and bool(re.fullmatch(r'\d+\.\d+\.\d+',ver)),'metadata.version must be X.Y.Z')
    test('Body is nonempty',bool(txt[front.end():].strip()),'body missing')
    test('Progressive disclosure line budget',len(txt.splitlines())<=500,f'{len(txt.splitlines())} > 500')
    # Less than 5k tokens is guidance rather than a strict spec requirement.
    if len(re.findall(r'\b\w+\b',txt))>5500:
        warnings.append('SKILL.md appears long relative to the ~5k-token recommended body target')
    for dirname in ['references','assets','tests','scripts']:
        test(f'{dirname} exists',(root/dirname).is_dir(),f'missing {dirname}')
    # Internal links include markdown target paths and code spans; constrain to known prefixes and no traversal.
    refs=set(re.findall(r'(?<![\w/])((?:references|assets|agents|tests|scripts)/[A-Za-z0-9_.\-/]+(?:\.md|\.json|\.py|\.yaml))',txt))
    for ref in sorted(refs):
        target = (root/ref).resolve()
        test(f'Local resource {ref}',target.is_relative_to(root) and target.is_file(), 'missing or unsafe reference')
    if len(refs)<5:
        warnings.append('SKILL.md references fewer than five progressive resources')
    for p in root.rglob('*'):
        if p.is_symlink():
            errors.append(f'Symlink not allowed in distributable package: {p.relative_to(root)}')
    if (root/'agents/openai.yaml').is_file():
        try:
            agent=yaml.safe_load((root/'agents/openai.yaml').read_text(encoding='utf8'))
            test('Agent profile YAML',isinstance(agent,dict) and isinstance(agent.get('interface'),dict),'invalid agent profile')
        except Exception as e:
            errors.append(f'Agent profile YAML: {e}')
    return errors,warnings,checks


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]); parser.add_argument('--json',action='store_true')
    args=parser.parse_args()
    errors,warnings,checks=check(args.root)
    report={'status':'PASS' if not errors else 'FAIL','check_count':len(checks)+len(errors),'passed_checks':len(checks),'errors':errors,'warnings':warnings}
    if args.json: print(json.dumps(report,indent=2))
    else:
        print(f"{report['status']}: {report['passed_checks']}/{report['check_count']} Agent Skills structural checks")
        for msg in errors: print('FAIL:',msg)
        for msg in warnings: print('WARN:',msg)
    return 1 if errors else 0

if __name__=='__main__': raise SystemExit(main())
