"""独立照合用：問題文だけ（答えを除く）を文字で出す。照合する人は、これだけを読んで解き、その後で dump_answer で答えと比べる。
使い方: python3 daily-drill/evening/dump_exam.py PM-21 [--answer]"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main(pid, answer=False):
    p = json.load(open(os.path.join(HERE, 'problems', pid + '.json'), encoding='utf-8'))
    e = p['exam']
    print(f"■{pid} {p['title']}\n{e['lead']}\n【事実関係】")
    for i, f in enumerate(e['facts'], 1):
        print(f'{i} {f}')
    print(f"【{e.get('register_title', '登記記録')}】")
    for r in e['register']:
        print('◇' + r['name'])
        for row in r['rows']:
            print('  ' + '｜'.join(row))
    if p.get('coords'):
        pts = p['calc']['points']
        print('【座標】' + '　'.join(f"{k}（{pts[k][0]:.2f}, {pts[k][1]:.2f}）" for k in p['coords']))
    if e.get('fig_note'):
        print('【図】' + e['fig_note'])
    print('【注】')
    for i, n in enumerate(e['notes'], 1):
        print(f'{i} {n}')
    print('【答案用紙】' + p['form']['title'])
    for it in p['form']['items']:
        if it['kind'] == 'field':
            print(f"・{it['label']}" + (f"：{it['answer']}" if answer or it.get('copy') else ''))
            if answer and it.get('note'):
                print(f"    （解説）{it['note']}")
        else:
            print(f"・表「{it['label']}」 列：{' / '.join(it['cols'])}")
            for r in it['rows']:
                print(f"    行 {r['name']}" + (('：' + ' / '.join(c.replace(chr(10), '　') for c in r['cells'])) if answer else ''))
            if answer and it.get('note'):
                print(f"    （解説）{it['note']}")


if __name__ == '__main__':
    a = '--answer' in sys.argv
    for pid in [x for x in sys.argv[1:] if x != '--answer']:
        main(pid, a)
