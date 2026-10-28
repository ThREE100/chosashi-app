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
    # mode が「誤り」なら誤っている肢、「正しい」なら正しい肢の組合せが正解
    want = p.get('mode') != '正しい'
    sel = [s['label'] for s in p['statements'] if s['truth'] != want]
    idx = [i for i, c in enumerate(p['choices']) if list(c) == sel]
    assert len(idx) == 1, (sel, p['choices'])
    return '・'.join(sel), idx[0] + 1


def tables_to_bullets(text):
    """noteはMarkdownの表を表示できないので、コードブロックの外の表を箇条書きに直す。
    行頭の列を見出しにして「- 行名：列名は…、列名は…。」の形にする。"""
    out, block, table = [], False, []

    def flush():
        if not table:
            return
        rows = [[c.strip() for c in r.strip().strip('|').split('|')] for r in table]
        rows = [r for r in rows if not all(set(c) <= set('-: ') for c in r)]
        head, body = rows[0], rows[1:]
        for r in body:
            parts = [f'（{head[i]}）{r[i].rstrip("。")}。' for i in range(1, len(r)) if r[i]]
            out.append(f'- {r[0]}：' + ''.join(parts))
        table.clear()

    for line in text.split('\n'):
        if line.startswith('```'):
            flush()
            block = not block
            out.append(line)
        elif not block and line.lstrip().startswith('|'):
            table.append(line)
        else:
            flush()
            out.append(line)
    flush()
    return '\n'.join(out)


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
          '', '```text', tpl.header(n, h['t1'], h['t2'], h['topic'], h.get('left'), h.get('right'), h['kanji'].split('・'), h.get('pose')), '```', '',
          '---', '', '## インフォグラフィック プロンプト（問題全体）', '', d['poster_intro'], '', '```text']
    q = d['poster']
    o += [tpl.poster(q['title'], q['sub'], q['col_a'], q['col_b'], q['cards'], q['kanji'], q['n_a']), '```', '']
    if d['notebooks']:
        o += ['---', '', f"## インフォグラフィック プロンプト（{d['nb_label']}・間違いノート）", '', d['nb_intro'], '']
        for i, nb in enumerate(d['notebooks'], 1):
            o += [f"### 画像{i}：{nb['name']}", '', '```text', tpl.notebook(**nb['args']), '```', '']
    out_dir = HERE
    open(os.path.join(out_dir, f'day{n:03d}-am-kaisetsu.md'), 'w', encoding='utf-8').write(tables_to_bullets('\n'.join(o)).rstrip('\n') + '\n')
    print('wrote', n)


if __name__ == '__main__':
    for a in sys.argv[1:]:
        build(int(a))
