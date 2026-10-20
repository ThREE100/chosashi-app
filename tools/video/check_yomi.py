#!/usr/bin/env python3
"""台本の読みを、音声を聞かずに一覧で確かめる（Open JTalk の読みを表示する）。

    python3 check_yomi.py episodes/R7_Q21_ep01.json            # 場面ごとの読み（カタカナ）と間を表示
    python3 check_yomi.py episodes/R7_Q21_ep01.json --words    # 台本に出てくる漢字の語と読みの一覧（重複なし）
    python3 check_yomi.py episodes/R7_Q21_ep01.json --md out.md  # 同じ内容をMarkdownに書き出す

読み違いを見つけたら:
  - その場面だけ直す → 台本の beat に "yomi": {"表記": "よみ"}
  - 全部の台本で直す → yomi_dict.json に "表記": "よみ"
"""
import argparse
import json
import re

import pyopenjtalk

import tts
from render import split_pages

KANJI = re.compile(r"[一-龥々]")


def kana(s: str) -> str:
    return pyopenjtalk.g2p(s, kana=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("--words", action="store_true")
    ap.add_argument("--md")
    a = ap.parse_args()
    sc = json.load(open(a.script, encoding="utf-8"))
    names = {k: c["name"] for k, c in sc["characters"].items()}
    lines, words = [], {}
    n = 0
    for ch in sc["chapters"]:
        lines.append(f"\n## {ch['title']}")
        for beat in ch["beats"]:
            if "speaker" not in beat:
                continue
            for page in split_pages(beat["text"]):
                n += 1
                reading = tts.to_reading(page, beat.get("yomi"))
                segs = tts.segments(reading)
                lines.append(f"\n[{n}] {names[beat['speaker']]}：{page.replace('|', '')}")
                lines.append("    " + " ".join(f"{kana(t)}" + (f" ⏸{sec:.2f}" if sec else "") for t, sec in segs))
                for t, _ in segs:
                    for node in pyopenjtalk.run_frontend(t):
                        if KANJI.search(node["string"]):
                            words.setdefault(node["string"], node["pron"].replace("’", ""))
    if a.words:
        out = ["| 表記 | 読み（Open JTalk） |", "|---|---|"] + [f"| {w} | {p} |" for w, p in sorted(words.items())]
    else:
        out = lines
    text = "\n".join(out)
    print(text)
    if a.md:
        open(a.md, "w", encoding="utf-8").write(text + "\n")


if __name__ == "__main__":
    main()
