"""新しい問題の雛形を作り、登録簿（registry.json）に仮登録する。
  朝：python3 daily-drill/new_problem.py morning AM-008 --day 8 --field 不登法 --style 事例 --level L3
  夜（申請書・判断）：python3 daily-drill/new_problem.py evening PM-08 --day 8 --types B3 --level L3
  夜（計算）：python3 daily-drill/new_problem.py evening-calc PM-09 --day 9 --types T5 --level L3
雛形の TODO は check_registry.py が検出する（TODO が残っていると NG）。作り方は daily-drill/RULES.md。"""
import argparse
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument('kind', choices=['morning', 'evening', 'evening-calc'])
ap.add_argument('pid')
ap.add_argument('--day', type=int, required=True)
ap.add_argument('--field', default='不登法')
ap.add_argument('--style', default='条文')
ap.add_argument('--types', default='')
ap.add_argument('--level', default='L2')
a = ap.parse_args()
reg = json.load(open(os.path.join(HERE, 'registry.json'), encoding='utf-8'))
tax = json.load(open(os.path.join(HERE, 'taxonomy.json'), encoding='utf-8'))
if a.pid in reg:
    sys.exit(f'{a.pid} は登録済み')
if a.kind == 'morning':
    if a.field not in tax['morning_fields'] or a.style not in tax['morning_styles'] or a.level not in tax['levels_morning']:
        sys.exit('分野・形式・難度が taxonomy.json にない')
    s = open(os.path.join(HERE, 'templates', 'morning_TEMPLATE.json'), encoding='utf-8').read().replace('AM-TODO', a.pid).replace('"day": 0', f'"day": {a.day}')
    open(os.path.join(HERE, 'morning', 'problems', a.pid + '.json'), 'w', encoding='utf-8').write(s)
    reg[a.pid] = {'side': 'morning', 'field': a.field, 'style': a.style, 'level': a.level, 'traps': ['TODO'], 'hard': ['TODO'], 'articles': ['TODO']}
else:
    ts = [t for t in a.types.split(',') if t]
    if not ts or any(t not in tax['evening_types'] for t in ts) or a.level not in tax['levels_evening']:
        sys.exit('型・難度が taxonomy.json にない')
    if a.kind == 'evening-calc':
        shutil.copy(os.path.join(HERE, 'templates', 'evening_calc_TEMPLATE.py'), os.path.join(HERE, 'evening', f'build_{a.pid}.py'))
        print(f'evening/build_{a.pid}.py を作成。TODO を埋めて実行する')
    else:
        print('申請書・判断の問題は evening/gen_shinsei.py に辞書を足す（land2 / bld2 が見本）。PMの id・day を設定する')
    reg[a.pid] = {'side': 'evening', 'types': ts, 'level': a.level, 'traps': [], 'articles': [], 'minutes': 15}
json.dump(reg, open(os.path.join(HERE, 'registry.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{a.pid} を登録簿に仮登録（traps・articles を埋める）')
