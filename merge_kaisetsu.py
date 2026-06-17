#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成されたkaisetsuファイルをkaisetsu_plus.jsonにマージする"""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

GENERATED_FILES = [
    'kaisetsu_H17_H25.json',
    'kaisetsu_H21.json',
    'kaisetsu_H22.json',
    'kaisetsu_H23.json',
]

with open('src/data/kaisetsu_plus.json', encoding='utf-8') as f:
    kp = json.load(f)

before_count = len(kp['entries'])
print('Before:', before_count, 'entries')

added = 0
for fname in GENERATED_FILES:
    with open(fname, encoding='utf-8') as f:
        new_entries = json.load(f)
    for entry_id, entry in new_entries.items():
        if entry_id not in kp['entries']:
            kp['entries'][entry_id] = entry
            added += 1
            print('  Added:', entry_id)
        else:
            print('  SKIP (already exists):', entry_id)

print('\nAdded:', added, 'entries')
print('After:', len(kp['entries']), 'entries')

with open('src/data/kaisetsu_plus.json', 'w', encoding='utf-8') as f:
    json.dump(kp, f, ensure_ascii=False, indent=2)
print('Written to src/data/kaisetsu_plus.json')
