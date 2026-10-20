#!/usr/bin/env python3
"""会話形式のnote記事（トリ先生・藍子）から、KaisetsuScript の下書きを作る。

    python3 article2script.py ../../note-articles-Kijyutsu/R7/Q21/note_R7_dai21mon_tochi_kaiwa_kaisetsu.md \
        --id R7_Q21_full --chapters 1-2 > episodes/R7_Q21_draft.json

下書きは記事のセリフをそのまま並べただけ。動画にする前に、Claude Code に次の仕上げをさせる（README の手順4）。
- 画像挿入マーカー（image_hint）に合う zu/ のPNGを image に書く
- 電卓のキー列・長い式は読み上げても伝わらないので、bullets や図に回してセリフを詰める
- 数字・記号の読み（yomi）を足す
"""
import argparse
import json
import os
import re
import sys

SPEAKERS = {"トリ先生": "tori", "藍子": "aiko"}


def parse(md: str):
    chapters, cur, speaker = [], None, None
    lines = md.splitlines()
    i = 0
    in_code = False
    while i < len(lines):
        ln = lines[i].rstrip()
        if ln.startswith("```"):
            in_code = not in_code
            i += 1
            continue
        if in_code:
            i += 1
            continue
        m = re.match(r"^## (?:第\d+章[：:])?\s*(.+)$", ln)
        if m:
            cur = {"title": m.group(1).strip(), "beats": []}
            chapters.append(cur)
            speaker = None
        elif cur is not None:
            m = re.match(r"^\*\*(トリ先生|藍子)\*\*", ln)
            if m:
                speaker = SPEAKERS[m.group(1)]
            elif ln.startswith("「") and speaker:
                text = ln.strip()
                while not text.endswith("」") and i + 1 < len(lines) and lines[i + 1].strip():
                    i += 1
                    text += lines[i].strip()
                cur["beats"].append({"speaker": speaker, "text": text.strip("「」")})
            elif ln.startswith("> 【画像挿入】"):
                cur["beats"].append({"image_hint": ln.replace("> 【画像挿入】", "").strip(), "image": "TODO"})
            elif re.match(r"^- \*\*", ln) or re.match(r"^- ", ln):
                items = []
                while i < len(lines) and lines[i].startswith("- "):
                    items.append(re.sub(r"\*\*", "", lines[i][2:]).strip())
                    i += 1
                cur["beats"].append({"bullets": {"heading": "", "items": items}, "_memo": "話者のセリフに付けるか、削る"})
                continue
        i += 1
    return chapters


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("article")
    ap.add_argument("--id", required=True)
    ap.add_argument("--chapters", help="例: 1-2（記事の章の番号。省略時は全部）")
    a = ap.parse_args()
    md = open(a.article, encoding="utf-8").read()
    title = md.splitlines()[0].lstrip("# ").strip()
    chs = parse(md)
    chs = [c for c in chs if c["beats"]]
    if a.chapters:
        s, _, e = a.chapters.partition("-")
        chs = chs[int(s) - 1:int(e or s)]
    zu = os.path.join(os.path.dirname(os.path.abspath(a.article)), "zu")
    out = {
        "format": "kaisetsuscript/1",
        "id": a.id,
        "source": os.path.relpath(a.article, os.path.join(os.path.dirname(__file__), "..", "..")),
        "series": "",
        "base_dir": os.path.relpath(zu, os.path.join(os.path.dirname(os.path.abspath(__file__)), "episodes")),
        "tts": "openjtalk",
        "characters": {
            "aiko": {"name": "藍子", "side": "left", "voice": "aiko", "cls": ""},
            "tori": {"name": "トリ先生", "side": "right", "voice": "tori", "cls": "tori"},
        },
        "intro": {"jingle": "opening", "top": "トリ先生と藍子の 記述式ゼミ", "title": title, "bottom": ""},
        "chapters": chs,
        "outro": {"jingle": "ending", "seconds": 5, "top": "次回", "title": "", "bottom": "記事の全文と解説図は note で公開中"},
        "youtube": {"title": "", "description": "", "credits": [], "tags": []},
        "_candidates": sorted(f for f in os.listdir(zu) if f.endswith(".png")) if os.path.isdir(zu) else [],
    }
    json.dump(out, sys.stdout, ensure_ascii=False, indent=2)
    print()


if __name__ == "__main__":
    main()
