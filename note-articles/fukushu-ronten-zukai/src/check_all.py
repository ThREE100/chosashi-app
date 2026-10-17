#!/usr/bin/env python3
"""論点別 復習用 図解プロンプト40枚の機械チェック（標準ライブラリのみ）。NG 0件が条件。
使い方: python3 note-articles/fukushu-ronten-zukai/src/check_all.py"""
import re, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
D = HERE.parent
LAWS = D.parent / "laws"
sys.path.insert(0, str(HERE))
from specs import TOPICS, SPECS
ng = []
def NG(m): ng.append(m); print("NG  ", m)
def OK(m): print("OK  ", m)

files = sorted(D.glob("T*/prompt_infographic_T*.md"))
assert len(files) == len(TOPICS), "論点ごとのファイル数が合わない"
blocks = []
for f in files:
    t = f.read_text(encoding="utf8")
    for b in re.findall(r"```text\n(.*?)\n```", t, flags=re.S):
        blocks.append((f.name, b))
if len(blocks) != len(SPECS): NG(f"プロンプト数 {len(blocks)} が設計データ {len(SPECS)} と違う")
else: OK(f"プロンプト {len(blocks)} 本（設計データと一致）")

# 1. 個人の演習結果・問題番号・図番・樹形図の語が入っていない
bad = ["誤答", "★", "のべ", "履歴", "回間違", "正答率", "未習得", "誤解"]
idp = re.compile(r"\bD\d{4}\b|[HR]\d{1,2}-Q\d+|第\d+問|問\d+|答練|模試")
tree = re.compile(r"決定木|判定木|ツリー")
for n, b in blocks:
    for w in bad:
        if w in b: NG(f"{n}: 個人の演習結果らしい語「{w}」")
    m = idp.search(b)
    if m: NG(f"{n}: 問題番号・教材名らしい文字列「{m.group(0)}」")
    if tree.search(b): NG(f"{n}: 樹形図の意味の『木』『ツリー』")
    body = b.split("--- HEADER ---")[1] if "--- HEADER ---" in b else b
    if re.search(r"図\s*\d|Figure", body): NG(f"{n}: 画像の中に図番らしい文字")
OK("個人の演習結果・問題番号・図番・禁止語の確認")

# 2. 表・カード・ステップの数の宣言と実データが合う／最終確認の漢字が本文にある
for n, b in blocks:
    body = b.split("--- FOOTER ---")[0]
    m = re.search(r"Exactly (\d+) columns and exactly (\d+) data rows", body)
    if m:
        rows = re.findall(r"^Row \d+: (.*)$", body, flags=re.M)
        if len(rows) != int(m.group(2)): NG(f"{n}: 行数 {m.group(2)} と実際 {len(rows)} が違う")
        for r in rows:
            if len(re.findall(r"」 \| 「", r)) + 1 != int(m.group(1)): NG(f"{n}: 列数が違う行がある：{r[:30]}")
    m = re.search(r"paying special attention to the kanji ([^;]+);", b)
    if m:
        for k in re.findall(r"[一-鿿]", m.group(1)):
            if k not in body: NG(f"{n}: 最終確認の漢字「{k}」が本文にない")
OK("表の行数・列数、最終確認の漢字")

# 3. 画像に入る文字（「」の中）に、許可した文字以外が入っていない（全角英字・記号・矢印・丸数字など）
allowed = re.compile(r"^[぀-ヿ一-鿿0-9０-９「」（）・：／、。ー 々]+$")
for n, b in blocks:
    body = b.split("--- FOOTER ---")[0]
    for s in re.findall(r"「([^」]*)」", body):
        if s and not allowed.match(s):
            odd = sorted({c for c in s if not allowed.match(c)})
            NG(f"{n}: 許可外の文字 {odd} を含む文字列：{s[:30]}")
OK("画像に入る文字の字種")

# 4. 主な根拠の語が、法令DBの原文にある（番号の取り違え防止の抜き取り）
chk = [
 ("fudousan-touki-hou.md", ["共用部分である旨の登記", "団地共用部分である旨の登記", "地図を作成するため必要があると認めるとき"]),
 ("fudousan-touki-kisoku-1.md", ["法定相続情報番号"]),
 ("kubunshoyuu-hou.md", ["分離して処分することができない", "建物の敷地と定められたものとみなす"]),
 ("touroku-menkyozei-hou.md", ["別表第一"]),
 ("chousashi-hou.md", ["成立の日から二週間以内に"]),
]
for fn, ws in chk:
    p = LAWS / fn
    if not p.exists(): NG(f"法令DBがない：{fn}"); continue
    t = p.read_text(encoding="utf8")
    for w in ws:
        if w not in t: print("WARN", f"{fn} に「{w}」が見つからない（表記ゆれの可能性。目視で確認）")
OK("法令DBの抜き取り確認（WARNは目視）")

print("\nNG", len(ng), "件")
sys.exit(1 if ng else 0)
