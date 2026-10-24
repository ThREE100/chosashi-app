"""独立に解いた答え（JSON）と、問題の想定の答えを欄ごとに突き合わせる。
入力：{"PM-86": {"answers": {"ラベル": "値" or [X, Y]}, "issues": "…"}, …}
使い方: python3 daily-drill/evening/compare_solved.py 解いた結果.json [...]
結果は evening/review/chain_solved.json に記録する（今の答えの版つき）"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def norm(v):
    if isinstance(v, list):
        return [f'{float(x):.2f}' for x in v]
    s = str(v).strip().replace('㎡', '').replace('m', '').replace(',', '')
    try:
        return f'{float(s):.2f}' if '.' in s else str(int(float(s)))
    except ValueError:
        return s


def ver(p):
    return hashlib.sha256(json.dumps([p['text'], p['tables'], p['answers']], ensure_ascii=False).encode()).hexdigest()[:16]


rp = os.path.join(HERE, 'review', 'chain_solved.json')
rec = json.load(open(rp, encoding='utf-8')) if os.path.exists(rp) else {}
ng = 0
for fp in sys.argv[1:]:
    for pid, r in json.load(open(fp, encoding='utf-8')).items():
        p = json.load(open(os.path.join(HERE, 'problems', pid + '.json'), encoding='utf-8'))
        bad = []
        for a in p['answers']:
            got = r['answers'].get(a['label'])
            if got is None:
                bad.append(f"{a['label']}：解いた答えがない")
            elif norm(got) != norm(a['value']):
                bad.append(f"{a['label']}：想定 {a['value']} ／ 解いた答え {got}")
        ng += len(bad)
        rec[pid] = {'version': ver(p), 'match': not bad, 'diff': bad, 'issues': r.get('issues', '')}
        print(('OK ' if not bad else 'NG ') + pid + ('' if not bad else '：' + ' ／ '.join(bad)) + (f"　［問題の作りの指摘］{r['issues']}" if r.get('issues') else ''))
os.makedirs(os.path.dirname(rp), exist_ok=True)
json.dump(rec, open(rp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'食い違い {ng}件')
