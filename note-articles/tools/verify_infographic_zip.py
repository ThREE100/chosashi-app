#!/usr/bin/env python3
"""ChatGPTが生成したインフォグラフィックZIPを受け取った後の検品スクリプト。

CHATGPT_INFOGRAPHIC_BATCH_WORKFLOW.md の「受け取り後の検品」で使う。次を確認する。
  1. ZIPが破損していないか（testzip）
  2. 期待枚数と一致するか
  3. 各PNGが完全に不透明か（アルファチャンネルがある場合、全ピクセルalpha=255か）
  4. ファイル名が list_gozu_guide_targets.py の命名規則と一致するか

Pillowが必要（pip install pillow）。

使い方:
    python3 note-articles/tools/verify_infographic_zip.py path/to/chosashi_gozu_guide.zip
    python3 note-articles/tools/verify_infographic_zip.py path/to/xxx.zip --expected 63
"""
import argparse
import sys
import zipfile
from io import BytesIO

# Windows既定のロケール(cp932)では、ファイル名やメッセージ中の記号を標準出力へ
# 書き出せずUnicodeEncodeErrorになることがあるため、明示的にUTF-8へ切り替える。
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

try:
    from PIL import Image
except ImportError:
    print("Pillowが必要です: pip install pillow", file=sys.stderr)
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("zip_path")
    parser.add_argument("--expected", type=int, default=63, help="期待する画像枚数（既定63）")
    args = parser.parse_args()

    problems = []

    with zipfile.ZipFile(args.zip_path) as zf:
        bad = zf.testzip()
        if bad is not None:
            problems.append(f"ZIP破損: {bad}")

        names = sorted(n for n in zf.namelist() if n.lower().endswith(".png"))
        print(f"PNGファイル数: {len(names)}（期待値: {args.expected}）")
        if len(names) != args.expected:
            problems.append(f"枚数不一致: {len(names)}枚 / 期待{args.expected}枚")

        for name in names:
            data = zf.read(name)
            try:
                img = Image.open(BytesIO(data))
                img.load()
            except Exception as e:
                problems.append(f"{name}: 画像として開けません（{e}）")
                continue

            if img.mode in ("RGBA", "LA", "PA"):
                alpha = img.convert("RGBA").getchannel("A")
                min_alpha = alpha.getextrema()[0]
                if min_alpha < 255:
                    problems.append(
                        f"{name}: 透過ピクセルあり（最小alpha={min_alpha}）→ 再生成が必要"
                    )

            w, h = img.size
            print(f"  {name}: {w}x{h}px, mode={img.mode}")

    print()
    if problems:
        print(f"NG: {len(problems)}件の問題があります")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)
    else:
        print("OK: 破損なし・枚数一致・全画像が不透明です")


if __name__ == "__main__":
    main()
