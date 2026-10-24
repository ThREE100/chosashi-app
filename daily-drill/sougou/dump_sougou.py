"""本番形式の統合問題を、問題文だけ（答えなし）で文字に出す。独立に解く人はこれだけを読んで解く。
使い方: python3 daily-drill/sougou/dump_sougou.py s01 [--answer]"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'evening'))
import build_sougou as BS  # noqa: E402
import dump_exam as DE  # noqa: E402

sid = sys.argv[1]
ans = '--answer' in sys.argv
meta, ps = BS.parts(sid)
print('■本番形式の統合問題 ' + meta['title'] + '（目安' + str(meta.get('minutes', 60)) + '分）')
for x in meta['lead']:
    print(x)
for k in ('calc', 'form', 'draw'):
    print('\n' + '=' * 30)
    DE.dump(ps[k], ans)
    if k == 'draw' and ans:
        print('【自己採点の項目】')
        for t, b in ps[k]['rubric']:
            print(f'  □ {t}（{b}）')
