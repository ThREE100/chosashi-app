"""独立照合用：問題文だけ（答えを除く）を文字で出す。照合する人は、これだけを読んで解き、その後で dump_answer で答えと比べる。
使い方: python3 daily-drill/evening/dump_exam.py PM-21 [--answer]"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main(pid, answer=False):
    p = json.load(open(os.path.join(HERE, 'problems', pid + '.json'), encoding='utf-8'))
    dump(p, answer)


def dump(p, answer=False):
    pid = p['id']
    if p['kind'] == 'draw':
        return calc(p, answer)          # 作図：条件・表・答えの欄（作図そのものは答案用紙に描く）
    if p['kind'] == 'calc2':
        return calc(p, answer)
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


def calc(p, answer):
    t = p['text']
    print(f"■{p['id']} {p['title']}\n{t['lead']}")
    for k, h in (('conditions', '【条件】'), ('hearing', '【聞き取り結果】'), ('notes', '【注】')):
        print(h)
        for i, x in enumerate(t.get(k, []), 1):
            print(f'{i} {x}')
    for tb in p['tables']:
        print('【' + tb['title'] + '】 ' + ' / '.join(tb['cols']))
        for r in tb['rows']:
            print('  ' + '｜'.join(r))
    f = p.get('fig', {})
    tx = [t['text'] for t in f.get('texts', [])]
    if tx:
        print('【図に書いてある文字・寸法】' + '　'.join(tx))
    if p['text'].get('fig_note'):
        print('【図】' + p['text']['fig_note'])
    print('【解答欄】')
    for a in p['answers']:
        v = a['value']
        print(f"・{a['label']}" + (('：' + ('（' + ', '.join(v) + '）' if isinstance(v, list) else v)) if answer else ''))
    if answer:
        print('【解き方】'); [print('  ' + x) for x in p['steps']]
        print('【つまずき】' + p['trap'])


if __name__ == '__main__':
    a = '--answer' in sys.argv
    for pid in [x for x in sys.argv[1:] if x != '--answer']:
        main(pid, a)
