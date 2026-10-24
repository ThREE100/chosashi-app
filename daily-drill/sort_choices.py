"""択一の選択肢を、アイウエオ順（組合せの1つ目の肢、同じなら2つ目の肢の順）に並べ替える。
並べ替えで正解の番号が変わるので、独立に解いた結果（morning/review・saturday/review）の版（hash）と、土曜の選んだ番号（choice）を、同じ組合せの新しい番号に付け替える（肢の判定は変えない）。
土曜の模擬は、並べ替えた後の正解の番号の偏り（1つの番号が7問以上、または1問以下）を、正解でない組合せを1つ差し替えて直す。
使い方: python3 daily-drill/sort_choices.py"""
import glob
import itertools
import json
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, 'saturday'))
import check_am as CA  # noqa: E402
import check_sat as CS  # noqa: E402

L = 'アイウエオ'
key = lambda c: [L.index(x) for x in c]


def ans_of(p):
    want = p['mode'] == '正しい'
    return {s['label'] for s in p['statements'] if s['truth'] == want}


def sort_one(p):
    p['choices'] = sorted([sorted(c, key=L.index) for c in p['choices']], key=key)
    return [i + 1 for i, c in enumerate(p['choices']) if set(c) == ans_of(p)][0]


def shift(p, want_lower):
    """正解の番号を1つ下げる（want_lower）または上げるよう、正解でない組合せを1つ差し替える"""
    a = ans_of(p)
    chs = [tuple(c) for c in p['choices']]
    pos = [i for i, c in enumerate(chs) if set(c) == a][0]
    akey = key(sorted(a, key=L.index))
    cands = [c for c in itertools.combinations(L, 2) if c not in chs and set(c) != a and len(set(c) & a) == 1]
    if want_lower:          # 正解より前の組合せを1つ減らし、後ろに足す
        out = [c for c in chs if key(c) < akey and set(c) != a]
        inn = [c for c in cands if key(c) > akey]
    else:
        out = [c for c in chs if key(c) > akey]
        inn = [c for c in cands if key(c) < akey]
    if not out or not inn:
        return False
    chs.remove(out[-1] if want_lower else out[0])
    chs.append(inn[0])
    p['choices'] = [list(c) for c in sorted(chs, key=key)]
    return True


def main():
    # 朝
    for fp in sorted(glob.glob(os.path.join(HERE, 'morning', 'problems', 'AM-*.json'))):
        p = json.load(open(fp, encoding='utf-8'))
        sort_one(p)
        json.dump(p, open(fp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        rp = os.path.join(HERE, 'morning', 'review', p['id'] + '.json')
        if os.path.exists(rp):
            r = json.load(open(rp, encoding='utf-8'))
            r['hash'] = CA.content_hash(p)
            json.dump(r, open(rp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    # 土曜
    for rp in sorted(glob.glob(os.path.join(HERE, 'saturday', 'review', 'SAT*.json'))):
        sid = os.path.basename(rp)[:-5]
        rv = json.load(open(rp, encoding='utf-8'))
        qs = []
        for fp in sorted(glob.glob(os.path.join(HERE, 'saturday', 'q', sid + '-Q*.json'))):
            q = json.load(open(fp, encoding='utf-8'))
            pid = os.path.basename(fp)[:-5]
            r = rv.get(pid, {})
            old = q['choices'][r['choice'] - 1] if r.get('choice') else None
            sort_one(q)
            qs.append((fp, pid, q, old))
        for _ in range(40):                      # 正解の番号の偏りを直す
            nos = Counter(sort_one(q) for _, _, q, _ in qs)
            hi = [k for k, v in nos.items() if v > 6]
            lo = [k for k in range(1, 6) if nos.get(k, 0) < 2]
            if not hi and not lo:
                break
            moved = False
            for fp, pid, q, old in qs:
                n = sort_one(q)
                if hi and n == hi[0]:
                    moved = shift(q, want_lower=(lo and lo[0] < n) or n > 3)
                elif lo and n in (lo[0] - 1, lo[0] + 1):
                    moved = shift(q, want_lower=lo[0] < n)
                if moved:
                    break
            if not moved:
                break
        for fp, pid, q, old in qs:
            json.dump({k: v for k, v in q.items() if k != 'id'}, open(fp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
            q['id'] = pid
            if pid in rv:
                rv[pid]['hash'] = CS.content_hash(q)
                if old is not None:
                    hit = [i + 1 for i, c in enumerate(q['choices']) if set(c) == set(old)]
                    rv[pid]['choice'] = hit[0] if hit else [i + 1 for i, c in enumerate(q['choices']) if set(c) == ans_of(q)][0]
        json.dump(rv, open(rp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(sid, dict(sorted(Counter(sort_one(q) for _, _, q, _ in qs).items())))


if __name__ == '__main__':
    main()
