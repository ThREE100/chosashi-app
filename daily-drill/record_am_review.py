"""朝の問題を独立に照合した結果を morning/review/AM-NNN.json に記録する（今の問題文の版の hash つき）。
入力は照合者が書いた JSON：{"AM-009": {"verdicts": {"ア": true, …}, "ambiguous": {"イ": "理由"}}, …}
使い方: python3 daily-drill/record_am_review.py 照合結果.json"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from check_am import content_hash  # noqa: E402

for pid, r in json.load(open(sys.argv[1], encoding='utf-8')).items():
    p = json.load(open(os.path.join(HERE, 'morning', 'problems', pid + '.json'), encoding='utf-8'))
    out = {'hash': content_hash(p), 'reviewer': '資料（問題文・肢・条文原文・過去問の解説の記載）だけを渡した独立のエージェント',
           'verdicts': r['verdicts'], 'ambiguous': r.get('ambiguous', {})}
    json.dump(out, open(os.path.join(HERE, 'morning', 'review', pid + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('記録', pid)
