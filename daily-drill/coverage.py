"""登録簿から、網羅の状況（型・ひっかけ・難度・分野・出題形式）を coverage/coverage.md に書き出す。
使い方: python3 daily-drill/coverage.py"""
import json
import os
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
tax = json.load(open(os.path.join(HERE, 'taxonomy.json'), encoding='utf-8'))
reg = json.load(open(os.path.join(HERE, 'registry.json'), encoding='utf-8'))
day = lambda pid: int(pid.split('-')[1])
ev = {k: v for k, v in reg.items() if v['side'] == 'evening'}
mo = {k: v for k, v in reg.items() if v['side'] == 'morning'}
L = ['# 網羅の状況（自動生成。`python3 daily-drill/coverage.py`）', '', f'登録済み：朝 {len(mo)} 問、夜 {len(ev)} 問。', '']
L += ['## 夜：型の網羅（優先度順）', '', '| 型 | 内容 | 優先 | 状態 | 出題日 |', '|---|---|---|---|---|']
by = defaultdict(list)
for k, v in ev.items():
    for t in v['types']:
        by[t].append(day(k))
for t, d in sorted(tax['evening_types'].items(), key=lambda x: (x[1]['priority'], x[0])):
    L.append(f'| {t} | {d["name"]} | {d["priority"]} | {d["status"]} | {"・".join(f"{x}日" for x in sorted(by[t])) or "—"} |')
unc = [t for t, d in tax['evening_types'].items() if not by[t]]
L += ['', f'**未出題の型：{", ".join(unc) or "なし"}**（優先度1から作る）', '']
L += ['## 夜：ひっかけの網羅', '', '| ID | 内容 | 回数 |', '|---|---|---|']
tc = Counter(t for v in ev.values() for t in v['traps'])
for t, n in tax['traps_evening'].items():
    L.append(f'| {t} | {n} | {tc[t] or "—"} |')
L += ['', f'**未使用のひっかけ：{", ".join(t for t in tax["traps_evening"] if not tc[t]) or "なし"}**', '']
lc = Counter(v['level'] for v in ev.values())
L += ['## 夜：難度', '', '| 難度 | 内容 | 問数 |', '|---|---|---|'] + [f'| {k} | {d} | {lc[k]} |' for k, d in tax['levels_evening'].items()]
L += ['', '## 朝：分野・出題形式・難度（直近7日の目安と比べる）', '']
q = tax['morning_quota_per_week']
fc, sc, mc = Counter(v['field'] for v in mo.values()), Counter(v['style'] for v in mo.values()), Counter(v['level'] for v in mo.values())
L += ['| 区分 | 現状 | 7日あたりの目安 |', '|---|---|---|']
for f in ('不登法', '民法', '調査士法'):
    L.append(f'| 分野：{f} | {fc[f]} | {q[f]} |')
for s, n in q['style'].items():
    L.append(f'| 形式：{s} | {sc[s]} | {n} |')
for s, n in q['level'].items():
    L.append(f'| 難度：{s} | {mc[s]} | {n} |')
mt = Counter(t for v in mo.values() for t in v['traps'])
L += ['', '| ひっかけ | 内容 | 回数 |', '|---|---|---|'] + [f'| {t} | {n} | {mt[t] or "—"} |' for t, n in tax['traps_morning'].items()]
L += ['', '## 朝：扱った条文', '']
arts = defaultdict(list)
for k, v in mo.items():
    for a in v['articles']:
        arts[a].append(day(k))
L += [f'- {a}（{"・".join(f"{x}日" for x in sorted(d))}）' for a, d in sorted(arts.items())]
os.makedirs(os.path.join(HERE, 'coverage'), exist_ok=True)
open(os.path.join(HERE, 'coverage', 'coverage.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('coverage/coverage.md を書き出し。未出題の型:', unc)
