"""令和8年度の各問の見出し画像のInstagram用プロンプト（4:5・1080x1350）を、note-unei/instagram/prompts/header-R08.md に書き出す。
note用の見出し画像プロンプトは各記事（q01〜q20）の「見出し画像プロンプト」にある。文字は同じで、大きさと余白だけ違う。
年度と問の番号は算用数字（2026-11-05 ユーザー指示。共通ルール）。
使い方：python3 note-articles/r8-mondai/src/make_ig_header.py
"""
import glob
import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lib  # noqa: E402

REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
OUT = os.path.join(REPO, "note-unei", "instagram", "prompts", "header-R08.md")

DATA = {}
for p in sorted(glob.glob(os.path.join(HERE, "d[0-9][0-9]*.py"))):
    DATA.update(importlib.import_module(os.path.basename(p)[:-3]).DATA)

L = ["# 令和8年度 各問の見出し画像（Instagram用・4:5・1080×1350）のプロンプト", "",
     "2026-11-05 作成（`note-articles/r8-mondai/src/make_ig_header.py` で作る。手で直さない）。note用（1280×670）は各記事の「見出し画像プロンプト」にある。",
     "女性のMCキャラクター1人だけを描く（トリ先生・藍子は入れない）。ChatGPTに、`キャラクターシート_MC-01〜MC-04` の4枚を添付してから貼る。",
     "副題の「令和8年度」「第N問」は**算用数字**（漢数字にしない。共通ルール）。画像の中の数字は、この副題の数字だけ。",
     "画像の中に、アカウント名・URL・ハッシュタグ・「noteへ」などの案内は入れない。左右54px・上下68pxの余白の内側に、文字と主要な絵を置く。",
     "画像の生成と目視確認は未実施。", "", "| 問 | 副題 |", "|---|---|"]
for n in range(1, 21):
    L.append("| 第%d問 | 令和8年度　午後の部　第%d問　%s |" % (n, n, DATA[n]["h_sub_topic"]))
L.append("")
for n in range(1, 21):
    L += ["## 第%d問" % n, "", "```text", lib.header_prompt_ig(n, DATA[n]), "```", ""]
open(OUT, "w", encoding="utf-8").write("\n".join(L))
print("wrote", OUT)
