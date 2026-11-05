#!/usr/bin/env python3
"""個別テーマ記事の本文で、1文が4行以上(34字/行 × 3行 = 102字超)になっている文を拾う。
使い方: python3 note-articles/topics/check_linelen.py [ファイル...]   (省略時は K*.md 全部)
対象: 通常の段落だけ。箇条書き・表・見出し・コードブロック・引用は対象外。「## 見出し画像プロンプト」以降(プロンプト部)も対象外。
1行の目安: note をPCで見ると約34字(±1)。34字は「が同一の登記所の管轄区域内にある場合であっても、甲土地の分筆の登記と」の字数。
"""
import re, sys, glob, os
PER, LIM = 34, 34 * 3
H = os.path.dirname(os.path.abspath(__file__))
files = sys.argv[1:] or sorted(glob.glob(os.path.join(H, 'K*_*.md')))
total = 0
for p in files:
    inb = False
    for n, line in enumerate(open(p, encoding='utf-8').read().split('\n'), 1):
        if line.startswith('## 見出し画像プロンプト') or line.startswith('## インフォグラフィック'): break
        if line.startswith('```'): inb = not inb; continue
        if inb or not line.strip() or re.match(r'\s*([-*>|#]|\d+\.)', line): continue
        t = re.sub(r'\*\*|`|\[([^\]]*)\]\([^)]*\)', lambda m: m.group(1) or '', line.rstrip())
        # ハードブレーク(行末2スペース)で区切られた行ごとに文を数える
        for sent in re.findall(r'[^。]+。?', t):
            if len(sent) > LIM:
                total += 1
                print(f'{os.path.basename(p)}:{n} {len(sent)}字 {sent[:30]}…')
print('NG', total)
