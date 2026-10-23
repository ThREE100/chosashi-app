"""第1週の夜の記述式ドリルのうち、計算の問題を evening/problems/ に書き出す。
計算の問題はシード固定で再現できる（check_pm.py が作り直して一致を確かめる）。
使い方: python3 daily-drill/evening/gen_week1.py"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import calc_types as ct  # noqa: E402

OUT = os.path.join(HERE, 'problems')
HO, KI, REI, TOUMEN = '不動産登記法', '不動産登記規則', '不動産登記令別表', '登録免許税法'


def B(law, art, quote):
    return {'law': law, 'article': art, 'quote': quote}


def F(q, answer, basis, note, calc=False):
    return {'q': q, 'answer': answer, 'basis': basis, 'note': note, 'calc': calc}


CALC_DAYS = {1: ('radial', 101), 2: ('intersection', 202), 4: ('foot', 404), 5: ('parallel', 505), 6: ('area', 606)}

problems = []
for day, (typ, seed) in CALC_DAYS.items():
    p = ct.GEN[typ](seed)
    p.update({'id': f'PM-{day:02d}', 'day': day, 'kind': 'calc', 'seed': seed})
    problems.append(p)

# 申請書ドリル（PM-03・PM-07）は gen_shinsei.py で作る

os.makedirs(OUT, exist_ok=True)
for p in problems:
    with open(os.path.join(OUT, p['id'] + '.json'), 'w', encoding='utf-8') as f:
        json.dump(p, f, ensure_ascii=False, indent=1)
print(len(problems), 'written')
