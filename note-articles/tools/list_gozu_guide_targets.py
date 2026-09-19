#!/usr/bin/env python3
"""r7〜h17の問1〜問3の記事から、⑤作図ガイド型インフォグラフィックのプロンプトを
まとめて抽出し、生成対象の一覧（通し番号・年度・記事slug・出力ファイル名・プロンプト
本文）をJSONで出力する。

CHATGPT_INFOGRAPHIC_BATCH_WORKFLOW.md の手順で、ChatGPTに1件ずつプロンプトを
貼り付ける際の参照リストとして使う。

使い方:
    python3 note-articles/tools/list_gozu_guide_targets.py > targets.json
    python3 note-articles/tools/list_gozu_guide_targets.py --prompt-only 5   # 5番目のプロンプト本文だけ表示
"""
import argparse
import json
import os
import re
import sys

# Windows既定のロケール(cp932)ではプロンプト中の記号（emダッシュ「―」等）を
# 標準出力へ書き出せずUnicodeEncodeErrorになるため、明示的にUTF-8へ切り替える。
# `> file.json` のようなリダイレクト時にも影響するため、importの直後に行う。
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

YEARS = [
    "r7", "r6", "r5", "r4", "r3", "r2", "r1",
    "h30", "h29", "h28", "h27", "h26", "h25", "h24", "h23", "h22", "h21", "h20",
    "h19", "h18", "h17",
]
BASE = os.path.join(os.path.dirname(__file__), "..")
HEADING_RE = re.compile(r"^## インフォグラフィック プロンプト（.*作図ガイド）\s*$", re.M)


def build_manifest():
    rows = []
    seq = 0
    for year in YEARS:
        year_dir = os.path.join(BASE, f"{year}-mondai")
        for n in (1, 2, 3):
            matches = sorted(
                f for f in os.listdir(year_dir) if f.startswith(f"q0{n}-") and f.endswith(".md")
            )
            if len(matches) != 1:
                raise RuntimeError(f"{year} q0{n}: expected exactly 1 file, found {matches}")
            fname = matches[0]
            slug = fname[:-3]
            path = os.path.join(year_dir, fname)
            text = open(path, encoding="utf-8").read()

            headings = [m.start() for m in HEADING_RE.finditer(text)]
            if not headings:
                raise RuntimeError(f"{path}: 作図ガイドセクションが見つかりません")
            start = headings[0]
            code_match = re.search(r"```(.*?)```", text[start:], re.S)
            if not code_match:
                raise RuntimeError(f"{path}: 作図ガイドのコードブロックが見つかりません")
            prompt = code_match.group(1).strip()

            seq += 1
            rows.append(
                {
                    "seq": seq,
                    "year": year,
                    "qn": n,
                    "slug": slug,
                    "path": os.path.relpath(path, BASE),
                    "output_filename": f"{seq:02d}_{year}-{slug}.png",
                    "prompt": prompt,
                }
            )
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--prompt-only",
        type=int,
        default=None,
        help="指定した通し番号(1-63)のプロンプト本文だけを標準出力する",
    )
    args = parser.parse_args()

    rows = build_manifest()

    if args.prompt_only is not None:
        matches = [r for r in rows if r["seq"] == args.prompt_only]
        if not matches:
            print(f"seq={args.prompt_only} が見つかりません（1〜{len(rows)}）", file=sys.stderr)
            sys.exit(1)
        print(matches[0]["prompt"])
        return

    print(json.dumps(rows, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
