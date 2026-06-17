#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/kijutsu.json', encoding='utf-8') as f:
    kj = json.load(f)

with open('kijutsu_text_land.json', encoding='utf-8') as f:
    land = json.load(f)
with open('kijutsu_text_building.json', encoding='utf-8') as f:
    building = json.load(f)

new_texts = {**land, **building}

updated = 0
for p in kj['problems']:
    if p['id'] in new_texts and not p.get('modelAnswerText', '').strip():
        p['modelAnswerText'] = new_texts[p['id']]
        updated += 1
        print('Updated:', p['id'])

print('\nUpdated', updated, 'entries')

with open('src/data/kijutsu.json', 'w', encoding='utf-8') as f:
    json.dump(kj, f, ensure_ascii=False, indent=2)
print('Written to src/data/kijutsu.json')
