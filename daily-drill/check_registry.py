"""問題の登録簿（registry.json）と分類（taxonomy.json）の整合を確かめる。
- すべての問題ファイル（morning/problems, evening/problems）が登録簿にあり、登録簿の問題ファイルが実在する
- 型・難度・ひっかけ・分野・出題形式のIDが taxonomy.json にある
- 朝：紛らわしい肢（hard）が問題の肢にあり、1つ以上ある。夜：ひっかけが1つ以上ある
- 新規作成の雛形に残した TODO が問題ファイルにない
使い方: python3 daily-drill/check_registry.py"""
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
tax = json.load(open(os.path.join(HERE, 'taxonomy.json'), encoding='utf-8'))
reg = json.load(open(os.path.join(HERE, 'registry.json'), encoding='utf-8'))
nerr = 0


def err(pid, msg):
    global nerr
    nerr += 1
    print(f'NG {pid}: {msg}')


files = {}
for side, pat in (('morning', 'morning/problems/*.json'), ('evening', 'evening/problems/*.json')):
    for f in glob.glob(os.path.join(HERE, pat)):
        p = json.load(open(f, encoding='utf-8'))
        files[p['id']] = (side, p, open(f, encoding='utf-8').read())
for pid in sorted(set(files) | set(reg)):
    if pid not in reg:
        err(pid, '登録簿にない（registry.json に追加する）')
        continue
    if pid not in files:
        err(pid, '登録簿にあるが問題ファイルがない')
        continue
    side, p, raw = files[pid]
    r = reg[pid]
    if r['side'] != side:
        err(pid, 'side が合わない')
    if 'TODO' in raw:
        err(pid, '雛形の TODO が残っている')
    if not r.get('traps'):
        err(pid, 'ひっかけ（traps）が1つもない')
    if side == 'morning':
        if r['level'] not in tax['levels_morning']:
            err(pid, f'難度 {r["level"]}')
        if r['field'] not in tax['morning_fields']:
            err(pid, f'分野 {r["field"]}')
        if r['style'] not in tax['morning_styles']:
            err(pid, f'出題形式 {r["style"]}')
        for t in r['traps']:
            if t not in tax['traps_morning']:
                err(pid, f'ひっかけID {t}')
        labels = {s['label'] for s in p['statements']}
        if not r.get('hard') or not set(r['hard']) <= labels:
            err(pid, '紛らわしい肢（hard）が肢にない／空')
        if r['level'] == 'L3' and r['style'] == '条文':
            err(pid, 'L3 は事例・規則準則・数量の肢を含むこと（style を見直す）')
    else:
        if r['level'] not in tax['levels_evening']:
            err(pid, f'難度 {r["level"]}')
        for t in r['types']:
            if t not in tax['evening_types']:
                err(pid, f'型ID {t}')
        for t in r['traps']:
            if t not in tax['traps_evening']:
                err(pid, f'ひっかけID {t}')
print(f'{len(files)}問を登録簿と照合。NG {nerr}件')
sys.exit(1 if nerr else 0)
