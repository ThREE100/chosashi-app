#!/usr/bin/env python3
"""
note-articles配下の記事ファイルにある「### まとめ表」のMarkdownテーブルを、
noteの本文エディタでも表示できる箇条書き形式に一括変換するスクリプト。

変換前:
    ### まとめ表

    | 肢 | 判定 | ポイント |
    |---|---|---|
    | ア | 誤 | ... |

変換後:
    ### まとめ

    - **ア（誤）**　...

使い方:
    python table_to_bullets.py <対象フォルダ1> [<対象フォルダ2> ...]

例:
    python table_to_bullets.py ../r6-mondai ../r7-mondai
"""

import sys
import re
import glob
import os


def convert_file(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()

    m = re.search(
        r"^### まとめ表\s*\n\n((?:\|.*\|\n?)+)",
        text,
        re.M,
    )
    if not m:
        return None  # 変換対象なし(既に箇条書き、または表がない)

    table_block = m.group(1)
    rows = []
    for line in table_block.strip().splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3:
            continue
        if all(re.fullmatch(r"-+", c) for c in cells):
            continue
        if cells[0] == "肢":
            continue
        rows.append(cells)

    if not rows:
        return None

    bullets = "\n".join(
        f"- **{label}（{verdict}）**　{point}" for label, verdict, point in rows
    )
    replacement = f"### まとめ\n\n{bullets}"

    new_text = text[: m.start()] + replacement + text[m.end():]
    if new_text == text:
        return None

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    return len(rows)


def main():
    if len(sys.argv) < 2:
        print("使い方: python table_to_bullets.py <フォルダ1> [<フォルダ2> ...]")
        sys.exit(1)

    total_converted = 0
    total_skipped = 0
    for folder in sys.argv[1:]:
        md_files = sorted(glob.glob(os.path.join(folder, "*.md")))
        for path in md_files:
            result = convert_file(path)
            if result is not None:
                print(f"OK: {path} ({result}行を箇条書き化)")
                total_converted += 1
            else:
                print(f"SKIP: {path} (対象のまとめ表なし)")
                total_skipped += 1

    print(f"\n変換: {total_converted}件, スキップ: {total_skipped}件")


if __name__ == "__main__":
    main()
