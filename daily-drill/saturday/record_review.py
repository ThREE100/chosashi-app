"""独立に解いた結果を saturday/review/SATnn.json に記録する（今の問題文の版の hash をつける）。
入力は解いた人が書いた JSON：{"Q01": {"choice": 3, "verdicts": {"ア": true, …}, "issues": "…"}, …}
使い方: python3 daily-drill/saturday/record_review.py SAT01 解いた結果.json [解いた結果2.json …]"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from check_sat import load, content_hash  # noqa: E402

sid = sys.argv[1]
qs = {q['id']: q for q in load(sid)}
rp = os.path.join(HERE, 'review', sid + '.json')
rv = json.load(open(rp, encoding='utf-8')) if os.path.exists(rp) else {}
for fp in sys.argv[2:]:
    for k, r in json.load(open(fp, encoding='utf-8')).items():
        pid = f'{sid}-{k}'
        if pid not in qs:
            sys.exit(f'{pid} がない')
        rv[pid] = {'hash': content_hash(qs[pid]), 'reviewer': '問題文だけ（正誤・解説・根拠なし）を渡した独立のエージェントが解いた結果',
                   'choice': r['choice'], 'verdicts': r['verdicts'], 'issues': r.get('issues', '')}
json.dump(rv, open(rp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{len(rv)}問分を {rp} に記録')
