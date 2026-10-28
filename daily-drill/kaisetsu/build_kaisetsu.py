#!/usr/bin/env python3
"""解説記事の組み立て。 python3 build_kaisetsu.py 1 2 3  （src/dayNNN.py のデータから dayNNN-am-kaisetsu.md を作る）
day004 は手書きの見本なので、このスクリプトでは作り直さない。"""
import importlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'src'))
import tpl  # noqa: E402


def quote(p):
    lines = ['> ' + p['stem'] + '  ', '>　  ']
    for s in p['statements']:
        lines += [f"> {s['label']}　{s['text']}  ", '>　  ']
    ch = '　　'.join(f"{i + 1}　{''.join(c)}" for i, c in enumerate(p['choices']))
    lines.append('> ' + ch)
    return '\n'.join(lines)


def answer(p):
    wrong = [s['label'] for s in p['statements'] if not s['truth']]
    idx = [i for i, c in enumerate(p['choices']) if list(c) == wrong]
    assert len(idx) == 1, (wrong, p['choices'])
    return '・'.join(wrong), idx[0] + 1


def build(n):
    d = importlib.import_module(f'day{n:03d}').D
    p = json.load(open(os.path.join(HERE, '..', 'morning', 'problems', f'AM-{n:03d}.json'), encoding='utf-8'))
    w, num = answer(p)
    o = [f"## 【土地家屋調査士受験生向け】毎朝ドリル_Day{n:03d}_択一解説～{d['catch']}～", '',
         f'**出題：毎日ドリル　第{n}日（朝）　択一**', '', quote(p), '', '---', '', d['intro'], '']
    for lab in 'アイウエオ':
        h, body = d['sections'][lab]
        o += [f'### {lab}：{h}', '', body, '']
    o += ['---', '', '### まとめ', '']
    for lab, tf, t in d['summary']:
        o.append(f'- **{lab}（{tf}）** {t}')
    o += ['', d['summary_tail'], '', f'**正解：{w}の組合せ（選択肢{num}番）**', '']
    for s in d['supplements']:
        o += ['---', '', s, '']
    o += ['---', '', '**このまま使える点／使う前に確認したい点**', '']
    o += [f'- {x}' for x in d['notes']]
    o += ['', '---', '', '## 見出し画像用フレーズ', '']
    o += [f'- {x}' for x in d['phrases']]
    h = d['header']
    o += ['', '---', '', '## 見出し画像プロンプト', '',
          'noteの見出し画像（アイキャッチ、1280x670px）用です。見出し画像は、女性のMCキャラクター1人だけを使います（トリ先生・藍子は入れません）。ChatGPTに、基準画像（キャラクターシート_MC-01〜MC-04の4枚）を添付し、下のコードブロックを貼ります。画像は生成していません。',
          '', '```text', tpl.header(n, h['t1'], h['t2'], h['topic'], h['left'], h['right'], h['kanji'].split('・')), '```', '',
          '---', '', '## インフォグラフィック プロンプト（問題全体）', '', d['poster_intro'], '', '```text']
    q = d['poster']
    o += [tpl.poster(q['title'], q['sub'], q['col_a'], q['col_b'], q['cards'], q['kanji'], q['n_a']), '```', '']
    if d['notebooks']:
        o += ['---', '', f"## インフォグラフィック プロンプト（{d['nb_label']}・間違いノート）", '', d['nb_intro'], '']
        for i, nb in enumerate(d['notebooks'], 1):
            o += [f"### 画像{i}：{nb['name']}", '', '```text', tpl.notebook(**nb['args']), '```', '']
    open(os.path.join(HERE, f'day{n:03d}-am-kaisetsu.md'), 'w', encoding='utf-8').write('\n'.join(o).rstrip('\n') + '\n')
    print('wrote', n)


if __name__ == '__main__':
    for a in sys.argv[1:]:
        build(int(a))
