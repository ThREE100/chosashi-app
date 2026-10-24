"""作図だけを練習する夜の問題（15〜20分）を、evening/draw_specs/pmNNN.py の DRAW から作る。
DRAW は本番形式の統合問題の第3部（sougou/sNN/draw.py）と同じ形（draw・title・text・tables・answers・spec・rubric・steps・trap・keys）に、
'verify'（答えの欄ごとに、座標から計算し直す式）と、REG（registry の型・難度・ひっかけ・条文）を足したもの。
  verify = {'areas': [[答えの欄の名前, [[X, Y], …], 'floor'], …],   … 多角形の面積（座標法、分数で計算）。'floor' は小数第2位未満を切り捨て
            'lens':  [[答えの欄の名前, [X, Y], [X, Y]], …]}         … 2点間の距離（小数第2位に四捨五入）
check_pm.py が、答えの欄の値と、キー列（F-789SG）の表示を、計算し直して確かめる（check_draw_module）。
使い方: python3 daily-drill/evening/gen_draw.py [PM-115 …] [--json-only]（--json-only は registry.json を書き換えない）"""
import glob
import importlib.util
import json
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def load(fp):
    importlib.invalidate_caches()
    sp = importlib.util.spec_from_file_location(os.path.basename(fp)[:-3], fp)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m.DRAW, m.REG


def main(only, json_only=False):
    reg = json.load(open(os.path.join(ROOT, 'registry.json'), encoding='utf-8'))
    n = 0
    for fp in sorted(glob.glob(os.path.join(HERE, 'draw_specs', 'pm*.py'))):
        pid = 'PM-' + os.path.basename(fp)[2:-3]
        if only and pid not in only:
            continue
        D, R = load(fp)
        p = {'id': pid, 'day': int(pid[3:]), 'kind': 'draw'}
        p.update({k: v for k, v in D.items() if k != 'verify'})
        p['verify'] = dict(D['verify'], type='module')
        json.dump(p, open(os.path.join(HERE, 'problems', pid + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        reg[pid] = {'side': 'evening', 'types': R['types'], 'level': R['level'], 'traps': R['traps'], 'articles': R.get('articles', []), 'minutes': D.get('minutes', 15)}
        print(pid, [(a['label'], a['value']) for a in p['answers']])
        n += 1
    if not json_only:
        json.dump(reg, open(os.path.join(ROOT, 'registry.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{n}問を書き出し')


if __name__ == '__main__':
    main(set(a for a in sys.argv[1:] if a != '--json-only'), '--json-only' in sys.argv)
