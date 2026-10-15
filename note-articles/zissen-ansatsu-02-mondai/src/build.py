#!/usr/bin/env python3
"""body/qNN.md（手書きの本文）と specs.py（問題文・正解・図解・見出し画像の指定）から ../qNN-xxx.md を作る。

使い方：  python3 build.py            （全20問）
          python3 build.py 3 7        （第3問・第7問だけ）
記事の本文を直すときは body/qNN.md を直してから、このスクリプトを実行する。
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import quote_block, quote_block_dialogue, infographic_prompt, midashi_prompt  # noqa: E402
from specs import SPECS  # noqa: E402

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "tools"))
from split_paragraphs import process as split_long_paragraphs  # noqa: E402

OUT = os.path.dirname(HERE)


def build(n):
    s = SPECS[n]
    body = open(os.path.join(HERE, "body", "q%02d.md" % n), encoding="utf-8").read().strip("\n")
    qb = quote_block_dialogue(s) if s.get("dialogue") else quote_block(s)
    if s["ask"] == "count":
        # 個数問題でも、見出し行は同じ形にする
        pass
    out = []
    out.append("## 【土地家屋調査士受験生向け】実践答練第2回 第%d問〜%s〜" % (n, s["title"]))
    out.append("")
    out.append("**出題年度：実践答練　第2回　択一式　第%d問**" % n)
    out.append("")
    out.append(qb)
    out.append("")
    out.append("---")
    out.append("")
    out.append(body)
    out.append("")
    out.append("---")
    out.append("")
    out.append("## 見出し画像 プロンプト")
    out.append("")
    out.append(s["midashi"]["note"])
    out.append("")
    out.append("```")
    out.append(midashi_prompt(s))
    out.append("```")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## インフォグラフィック プロンプト（問題全体）")
    out.append("")
    out.append(s["info"]["desc"])
    out.append("")
    out.append("```")
    out.append(infographic_prompt(s))
    out.append("```")
    out.append("")
    path = os.path.join(OUT, "q%02d-%s.md" % (n, s["slug"]))
    final = "\n".join(out)
    # 解説文の1段落が長すぎるとき（format-templateの「1段落は4行以内」）は、文の区切りで分ける
    final, _changed = split_long_paragraphs(final)
    open(path, "w", encoding="utf-8").write(final)
    return path


if __name__ == "__main__":
    ns = [int(a) for a in sys.argv[1:]] or sorted(SPECS)
    for n in ns:
        if not os.path.exists(os.path.join(HERE, "body", "q%02d.md" % n)):
            print("skip (no body):", n)
            continue
        print("built", build(n))
