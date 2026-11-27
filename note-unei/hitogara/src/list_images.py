"""記事フォルダに要る画像の一覧を出す（make_zip.sh から使う）。
使い方：python3 list_images.py <記事フォルダ>
出力：1行に「ファイル名<TAB>幅<TAB>高さ<TAB>種類」。
 - 見出し画像：header-prompts.md の「ファイル名：`…png`」。直前の見出し「## note用（W×H）」の寸法。
 - 本文の図：article.md に出てくる `…png`（見出し画像以外）。寸法は Instagram用（_ig）だけ 1080×1440 を確かめる（確かめないものは「-」）。
"""
import sys, re, os
d = sys.argv[1]
out = {}
hp = os.path.join(d, "header-prompts.md")
if os.path.exists(hp):
    w = h = "-"
    for line in open(hp, encoding="utf-8"):
        m = re.match(r"^##\s.*?（(\d+)×(\d+)）", line)
        if m: w, h = m.group(1), m.group(2)
        m = re.search(r"ファイル名：`([^`]+\.png)`", line)
        if m: out[m.group(1)] = (w, h, "見出し画像（Codexで生成）")
art = open(os.path.join(d, "article.md"), encoding="utf-8").read()
for name in re.findall(r"`([A-Za-z0-9_\-]+\.png)`", art):
    if name in out: continue
    wh = ("1080", "1440") if name.endswith("_ig.png") else ("-", "-")
    out[name] = (*wh, "本文の図（作成済み）")
for k, (w, h, kind) in out.items():
    print(f"{k}\t{w}\t{h}\t{kind}")
