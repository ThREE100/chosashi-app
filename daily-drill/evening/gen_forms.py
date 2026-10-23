"""書式ひな形ドリル（evening/forms/pmNN.py）を読み込み、evening/problems/PM-NN.json に書き出す。
registry.json と forms_made.json も更新する（各問の REGISTRY を使う）。
使い方: python3 daily-drill/evening/gen_forms.py [PM-NN ...]"""
import glob
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'forms'))
ROOT = os.path.dirname(HERE)
PLAN = {p['pid']: p for p in json.load(open(os.path.join(ROOT, 'forms_plan.json'), encoding='utf-8'))}


def load(fp):
    spec = importlib.util.spec_from_file_location(os.path.basename(fp)[:-3], fp)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main(only=None, json_only=False):
    reg = json.load(open(os.path.join(ROOT, 'registry.json'), encoding='utf-8'))
    made = json.load(open(os.path.join(ROOT, 'forms_made.json'), encoding='utf-8'))
    n = 0
    for fp in sorted(glob.glob(os.path.join(HERE, 'forms', 'pm[0-9][0-9].py'))):
        pid = 'PM-' + os.path.basename(fp)[2:4]
        if only and pid not in only:
            continue
        m = load(fp)
        pl = PLAN[pid]
        p = dict(m.PROBLEM)
        p.update({'id': pid, 'day': pl['day'], 'kind': 'shinsei2', 'module': True, 'forms_no': pl['no']})
        p.setdefault('layout', 'generic' if p.get('fig') else 'none')
        json.dump(p, open(os.path.join(HERE, 'problems', pid + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        r = dict(m.REGISTRY)
        r.update({'side': 'evening', 'forms_no': pl['no']})
        r.setdefault('minutes', 15)
        reg[pid] = r
        made[str(pl['no'])] = pid
        n += 1
    if json_only:          # 並行して作るときは JSON だけ書き、registry.json・forms_made.json は最後にまとめて更新する
        print(n, '問を書き出し（registry は更新しない）')
        return
    json.dump(reg, open(os.path.join(ROOT, 'registry.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(made, open(os.path.join(ROOT, 'forms_made.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(n, '問を書き出し')


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if a != '--json-only']
    main(set(args) or None, '--json-only' in sys.argv)   # 例: python3 gen_forms.py PM-21 PM-28（指定した問だけ書き出す）
