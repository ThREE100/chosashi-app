"""土曜の模擬を、問題文だけ（正誤・解説・根拠なし）で文字に出す。独立に解く人はこれだけを読んで解く。
使い方: python3 daily-drill/saturday/dump_sat.py SAT01 [Q01-Q10]   （範囲を省くと20問）
        python3 daily-drill/saturday/dump_sat.py SAT01 --answer       （正解・解説つき。解き終えてから見る）"""
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
NUM = '①②③④⑤'


def main():
    sid = sys.argv[1]
    ans = '--answer' in sys.argv
    rng = [a for a in sys.argv[2:] if a.startswith('Q')]
    lo, hi = (1, 20)
    if rng:
        a, b = rng[0].split('-')
        lo, hi = int(a[1:]), int(b[1:])
    for fp in sorted(glob.glob(os.path.join(HERE, 'q', f'{sid}-Q*.json'))):
        q = json.load(open(fp, encoding='utf-8'))
        if not lo <= q['no'] <= hi:
            continue
        print(f"\n【第{q['no']}問】{q['stem']}")
        if q['format'] == '会話':
            for t in q['dialogue']:
                print(f"  {t['speaker']}：" + (f"（{t['label']}）" if t.get('label') else '') + t['text'])
        else:
            for s in q['statements']:
                print(f"  {s['label']}　{s['text']}")
        print('  ' + '　'.join(f'{NUM[i]} {"".join(c)}' for i, c in enumerate(q['choices'])))
        if ans:
            want = q['mode'] == '正しい'
            right = sorted(s['label'] for s in q['statements'] if s['truth'] == want)
            no = [i for i, c in enumerate(q['choices']) if set(c) == set(right)]
            print(f"  ＝正解 {NUM[no[0]] if no else '（なし）'}")
            for s in q['statements']:
                print(f"    {s['label']} {'○' if s['truth'] else '×'} {s['note']}")


if __name__ == '__main__':
    main()
