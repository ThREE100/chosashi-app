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
"""
import re
import sys

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
