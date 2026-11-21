#!/usr/bin/env python3
"""Offline integrity checks for this published dataset release (stdlib only)."""
from pathlib import Path
import json,csv,hashlib,collections
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'
read=lambda name: json.loads((DATA/name).read_text(encoding='utf-8'))
names={'clean_dev_970':970,'model_selection_30':30,'final_test_250':250,'reserve_50':50,'all_experimental_1250':1250}
tables={name:read(name+'.json') for name in names}
for n,expect in names.items():
    arr=tables[n]; assert len(arr)==expect,(n,len(arr),expect)
    assert len({r['question_id'] for r in arr})==expect,(n,'duplicate')
ids={name:{r['question_id'] for r in arr} for name,arr in tables.items()}
assert len(set.union(*(ids[name] for name in names if name!='all_experimental_1250')))==1300
parts=['clean_dev_970','model_selection_30','final_test_250','reserve_50']
for i,a in enumerate(parts):
    for b in parts[i+1:]:assert not (ids[a]&ids[b]),f'{a} overlaps {b}'
assert ids['all_experimental_1250']==ids['clean_dev_970']|ids['model_selection_30']|ids['final_test_250']
with (DATA/'source_register_1300.csv').open(encoding='utf-8-sig',newline='') as f:source=list(csv.DictReader(f))
assert len(source)==1300
ref={r['question_id']:r for r in source}
assert len(ref)==1300
for n,arr in tables.items():
    for r in arr:
        x=ref[r['question_id']]
        for field in ['question','reference_answer','source_name','source_reference','verification_status','answer_type','category']:
            assert str(r[field])==str(x[field]),(r['question_id'],field)
        assert r['accepted_aliases']==x['accepted_aliases'].split(' | ')
        assert x['dataset_split'] in (n,'clean_dev_970','model_selection_30','final_test_250','reserve_50')
        assert r['source_reference'].startswith('https://')
manifest=read('release_manifest.json')
# Prevent publishing new or changed files without regenerating the release manifest.
from refresh_manifest import compute_checksums
observed_hashes = compute_checksums()
expected_hashes = manifest['output_sha256']
assert set(observed_hashes) == set(expected_hashes), (
    "Manifest file list is stale. Run: python scripts/refresh_manifest.py",
    "missing_entries=" + str(sorted(set(observed_hashes) - set(expected_hashes))),
    "missing_files=" + str(sorted(set(expected_hashes) - set(observed_hashes)))
)
for rel,recorded in manifest['output_sha256'].items():
    h=hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()
    assert h==recorded,(rel,'SHA mismatch')
print('PASS — 970 Clean-Dev, 30 model selection, 250 final test, 50 reserve, 1300 linked sources; checksums verified.')
