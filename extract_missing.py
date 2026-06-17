#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/kaisetsu_plus.json', encoding='utf-8') as f:
    kp = json.load(f)
with open('src/data/takuitsu.json', encoding='utf-8') as f:
    tq = json.load(f)

existing_ids = set(kp['entries'].keys())
missing = []
for q in tq['questions']:
    qid = 'chosashi_' + q['yearCode'] + '_q' + str(q['questionNo']).zfill(2)
    if qid not in existing_ids:
        missing.append({
            'id': qid,
            'yearCode': q['yearCode'],
            'questionNo': q['questionNo'],
            'subject': q.get('subject', ''),
            'stem': q.get('stem', ''),
            'alts': q.get('alts', []),
            'combos': q.get('combos', []),
            'correctAnswer': q.get('correctAnswer', 0)
        })

by_year = defaultdict(list)
for q in missing:
    by_year[q['yearCode']].append(q)

for yr, qs in sorted(by_year.items()):
    nos = [q['questionNo'] for q in qs]
    print(yr + ': ' + str(len(qs)) + ' questions - Q' + str(nos))

with open('missing_questions.json', 'w', encoding='utf-8') as f:
    json.dump(missing, f, ensure_ascii=False, indent=2)
print('\nSaved ' + str(len(missing)) + ' missing questions to missing_questions.json')
