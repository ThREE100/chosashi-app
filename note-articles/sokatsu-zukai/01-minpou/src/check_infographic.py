#!/usr/bin/env python3
"""民法編の図解インフォグラフィック・見出し画像プロンプトの機械チェック（NG 0件が条件）。
使い方: python3 note-articles/sokatsu-zukai/01-minpou/src/check_infographic.py
- 個人の演習結果・問題番号・図番・禁止語（決定木・判定木・ツリー）が画像の中の文言に入っていない
- 表の行数の宣言とデータ行が合う／最終確認の漢字が本文にある
- 論点M1-1〜M3-6の全部に図解のファイルがある／各章の全体図（M?-0）がある
- 記事（sokatsu-01-minpou-ch1〜3.md）の論点の見出しと、README の対応表の論点が一致する"""
import re, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
D = HERE.parent
ROOT = HERE.parents[3]
COL = ROOT / "note-articles" / "column"
ng = []
def NG(m): ng.append(m); print("NG  ", m)
def OK(m): print("OK  ", m)

bad_words = ["誤答", "★", "のべ", "履歴", "回間違", "正答率"]
id_pat = re.compile(r"\bD\d{4}\b|[HR]\d{1,2}-Q\d+")
tree_words = ["決定木", "判定木", "ツリー"]
files = sorted((D / "infographic").glob("prompt_infographic_*.md")) + sorted(D.glob("prompt_midashi_*.md"))
n_img = 0
for f in files:
    t = f.read_text(encoding="utf8")
    blocks = re.findall(r"```text\n(.*?)\n```", t, flags=re.S)
    txt = "\n".join(blocks) if blocks else t
    for w in bad_words:
        if w in txt: NG(f"{f.name}: 個人の演習結果らしい語「{w}」がある")
    if id_pat.search(txt): NG(f"{f.name}: 問題番号らしい文字列「{id_pat.search(txt).group(0)}」がある")
    for w in tree_words:
        if w in t: NG(f"{f.name}: 禁止語「{w}」がある")
    for blk in blocks:
        n_img += 1
        body = blk.split("--- FOOTER ---")[0]
        m = re.search(r"exactly (\d+) data rows", body)
        if m:
            rows = len(re.findall(r"^Data row \d+|^Row \d+:", body, flags=re.M))
            if rows and rows != int(m.group(1)): NG(f"{f.name}: 表の行数の宣言 {m.group(1)} とデータ行 {rows} が違う")
        m = re.search(r"paying special attention to the kanji ([^;]+);", blk)
        if m:
            for k in re.findall(r"[一-鿿]", m.group(1)):
                if k not in body: NG(f"{f.name}: 最終確認の漢字「{k}」が本文にない")
        head = body.split("--- HEADER ---")[1] if "--- HEADER ---" in body else ""
        if re.search(r"図\s*\d|Figure", head): NG(f"{f.name}: 画像の中に図番らしい文字がある")
OK(f"図解・見出し画像 {len(files)} ファイル／プロンプト {n_img} 本を検査（上にNGがなければ）")

# 論点との対応
topics = []
for n in (1, 2, 3):
    art = (COL / f"sokatsu-01-minpou-ch{n}.md").read_text(encoding="utf8")
    topics += re.findall(r"^### 【(M\d-\d+)】", art, flags=re.M)
for tp in topics:
    if not list((D / "infographic").glob(f"prompt_infographic_{tp}.md")): NG(f"{tp}: 図解のファイルがない")
for n in (1, 2, 3):
    if not list((D / "infographic").glob(f"prompt_infographic_M{n}-0_zentai*.md")): NG(f"第{n}章の全体図（M{n}-0_zentai）がない")
OK(f"論点 {len(topics)} 個の図解の有無・各章の全体図を確認（上にNGがなければ）")
print(f"\n結果: NG {len(ng)}件")
sys.exit(1 if ng else 0)
