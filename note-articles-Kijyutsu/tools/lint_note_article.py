"""記述式note記事の表記ルールを機械的にチェックする。

使い方:
    python3 note-articles-Kijyutsu/tools/lint_note_article.py note-articles-Kijyutsu/R6/Q21/note_R6_*.md

チェック内容（qa-checklist-kijutsu.md の G 項に対応）:
    - Markdown表（| で始まる行）が残っていないか
    - 見出しが ### までに収まっているか
    - LaTeX（$ や \\frac など）を使っていないか
    - 絵文字を使っていないか
    - 「式（点名）」「電卓操作」の組がそろっているか（数の比較）
    - 「表示：」の行の一覧（値の照合は calc_helpers.py で行う）
    - 「…」の付いていない4桁小数の表示値（切り捨て・「…」付け忘れの候補）
    - 電卓操作のコードブロックで、[ALPHA] の後に使われている変数の一覧（変数の割り当てと照合する）
    - 会話形式の長すぎるセリフ（2026-10-02追加）：noteの本文の1行を全角44字（半角は0.5字）とみなし、
      260字（約6行。目安は5行＝220字）を超える段落と、3段落を超える1つのセリフを違反として出す
      （執筆プロンプトの「セリフの長さ」。セリフの続きの段落は空行のあとに話者名なしで続き、最後の段落が」で閉じる）
    - 会話形式の同じ話者の連続（2026-10-02追加）：話者名の行が同じ話者で続くもの。画像挿入マーカーとセリフの続きの段落は
      読み飛ばし、箇条書き・表・コードブロック・計算の結果の行（**▶ 〜**、表示：）・見出し・区切り線をはさむものは数えない
      （年度ごとの照合スクリプトで判定がまちまちで、マーカーをはさむ連続の見逃しが多かったため、全記事で共通に確かめる）
"""
import re
import sys
import unicodedata

LINE_W = 44          # noteの本文の1行（全角の字数）
TARGET = LINE_W * 5  # 1段落の目安（5行＝220字）
MAX_PARA = 260       # 1段落の上限（ユーザーの見本の長いほうの段落）
MAX_PARAS = 3        # 1つのセリフの段落の数の上限


def width(s):
    """全角を1、半角を0.5として数える。"""
    return sum(0.5 if unicodedata.east_asian_width(c) in ('H', 'Na', 'N') else 1 for c in s)


def long_lines(lines):
    """話者名の行（**トリ先生**  ／**藍子**  ）に続くセリフを段落ごとに調べ、長すぎるものを (行番号, 内容) で返す。
    セリフは「で始まり、」で終わる段落まで（途中の段落は空行で区切られ、話者名がない）。"""
    out = []
    for i, line in enumerate(lines):
        if line.rstrip() not in ('**トリ先生**', '**藍子**') or i + 1 >= len(lines) or not lines[i + 1].startswith('「'):
            continue
        paras, cur, j = [], [], i + 1
        while j < len(lines):
            t = lines[j].rstrip()
            if not cur and j > i + 1 and t.startswith(('**', '> ', '#', '---', '- ', '```')):
                break                          # 」で閉じないまま次の要素が来たら、そこで打ち切る
            if t.strip():
                cur.append((j, t))
            elif cur:
                paras.append(cur)
                if cur[-1][1].endswith('」'):
                    cur = []
                    break
                cur = []
            j += 1
        if cur:
            paras.append(cur)
        for p in paras:
            w = width(''.join(t for _, t in p))
            if w > MAX_PARA:
                out.append((p[0][0] + 1, f'1段落が約{w / LINE_W:.1f}行（全角換算{w:g}字。目安{TARGET}字・上限{MAX_PARA}字）'))
        if len(paras) > MAX_PARAS:
            out.append((i + 2, f'1つのセリフが{len(paras)}段落（上限{MAX_PARAS}段落）'))
    return out

SPEAKERS = ('**トリ先生**', '**藍子**')


def same_speaker(lines):
    """同じ話者が続く話者名の行を (行番号, 話者) で返す。"""
    out, prev, broken = [], None, False
    for i, line in enumerate(lines, 1):
        t = line.rstrip()
        if t in SPEAKERS:
            if t == prev and not broken:
                out.append((i, t.strip('*')))
            prev, broken = t, False
        elif t.startswith(('#', '---')):
            prev = None
        elif re.match(r'^(\s*[-*] |\s*\d+\. |\||```|\*\*▶|表示：)', t):
            broken = True
    return out


EMOJI = re.compile('[\U0001F300-\U0001FAFF☀-➿]')


def lint(path):
    text = open(path, encoding='utf-8').read()
    lines = text.splitlines()
    problems = []
    in_code = False
    code_vars = set()
    for i, line in enumerate(lines, 1):
        if line.startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            code_vars.update(re.findall(r'\[ALPHA\] \[([A-FXYM])\]', line))
            continue
        if line.lstrip().startswith('|'):
            problems.append(f'{i}: Markdown表が残っています')
        if re.match(r'^#{4,} ', line):
            problems.append(f'{i}: 見出しが4階層以上です')
        if '$' in line or '\\frac' in line:
            problems.append(f'{i}: LaTeXらしき記法があります')
        if EMOJI.search(line):
            problems.append(f'{i}: 絵文字があります')
    for n, msg in long_lines(lines):
        problems.append(f'{n}: セリフが長すぎます（{msg}）。相手の短い受け答えをはさむ・箇条書きに出す・「。」の後ろで改行する')
    for n, who in same_speaker(lines):
        problems.append(f'{n}: 同じ話者（{who}）のセリフが続いています。相手の短い受け答えをはさむか、1つのセリフにまとめる')
    n_shiki = text.count('式（点名）')
    n_dentaku = len(re.findall(r'^電卓操作', text, re.M))
    print(f'== {path}')
    print(f'式（点名）: {n_shiki} 個 / 電卓操作: {n_dentaku} 個（差が大きい場合は3点セットの欠けを確認）')
    print('== 表示の行（calc_helpers.py で1つずつ照合すること）')
    for i, line in enumerate(lines, 1):
        if line.startswith('表示：'):
            flag = ''
            # 小数第4位まで書いてあり「…」がない値は、割り切れる値か要確認
            for m in re.finditer(r'\d+\.\d{4}(?!…|\d)', line):
                flag = '  ← 「…」なし4桁。割り切れる値か確認'
            print(f'{i}: {line}{flag}')
    print('== 電卓操作で使っている変数:', ', '.join(sorted(code_vars)))
    if problems:
        print('== 表記ルール違反')
        for p in problems:
            print(p)
    else:
        print('== 表記ルール違反: なし')


if __name__ == '__main__':
    for p in sys.argv[1:]:
        lint(p)
