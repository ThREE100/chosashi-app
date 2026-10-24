"""夜の記述式デイリー（計算の連鎖）を、evening/chain_specs/pmNN.py の SPEC から作る。
答え（方法A）・F-789SGのキー列・問題と解答の JSON（evening/problems/PM-NN.json）を書き出し、registry.json に登録する。
答えが一つに決まらない設計（四捨五入・切捨ての境目、ほぼ平行な2直線、辺の外の点、解のない面積の条件）は止める。
使い方: python3 daily-drill/evening/gen_chain.py [PM-85 …] [--json-only]"""
import glob
import importlib.util
import json
import os
import sys

sys.dont_write_bytecode = True    # SPEC を秒単位で書き直したとき、古い __pycache__ を読まないように
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import chain  # noqa: E402


def load(fp):
    importlib.invalidate_caches()
    spec = importlib.util.spec_from_file_location(os.path.basename(fp)[:-3], fp)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.SPEC


def main(only, json_only):
    reg = json.load(open(os.path.join(ROOT, 'registry.json'), encoding='utf-8'))
    n, bad = 0, 0
    for fp in sorted(glob.glob(os.path.join(HERE, 'chain_specs', 'pm*.py'))):
        pid = 'PM-' + os.path.basename(fp)[2:-3]
        if only and pid not in only:
            continue
        S = load(fp)
        S['pid'] = pid
        try:
            p, got, out = chain.build_problem(S, int(pid[3:]))
        except chain.SpecError as e:
            print(f'NG {pid}: {e}')
            bad += 1
            continue
        errs = chain.verify_problem(p)
        for e in errs:
            print(f'NG {pid}: {e}')
        bad += bool(errs)
        json.dump(p, open(os.path.join(HERE, 'problems', pid + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        reg[pid] = {'side': 'evening', 'types': S['types'], 'level': S['level'], 'traps': S['traps'], 'articles': S.get('articles', []), 'minutes': S.get('minutes', 15)}
        print(pid, [(a['label'], a['value']) for a in p['answers']])
        n += 1
    if not json_only:
        json.dump(reg, open(os.path.join(ROOT, 'registry.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{n}問を書き出し、NG {bad}問')
    return bad


if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if x != '--json-only']
    sys.exit(1 if main(set(a), '--json-only' in sys.argv) else 0)
