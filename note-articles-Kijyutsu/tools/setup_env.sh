#!/bin/bash
# 記述式の作図・画像の書き出し・答案用紙PDFの実測に要る環境を、新しいコンテナで一度に整える（2026-10-26、R2/Q21）。
# 何度流しても同じ結果になる（すでに入っているものは入れ直さない）。
# 使い方：  bash note-articles-Kijyutsu/tools/setup_env.sh
#
# 直すもの（照らし直しのたびにつまずいた順）：
#  1. 日本語フォント Noto Sans CJK JP … `apt-get install` の前に `apt-get update` が要る（要らないと「Unable to locate package」）
#  2. Python の matplotlib・pymupdf・playwright・numpy・pillow
#  3. システムの古い PIL（/usr/lib/python3/dist-packages）が先に読まれて `cannot import name '_imaging'` になるとき、
#     pip の pillow を /usr/local/lib/python3.x/dist-packages へ入れ直す（素の `pip` は別の Python に入るので `python3 -m pip`）
#  4. Chromium のフォルダ名が環境で違う（chrome-linux と chrome-linux64）。古い作成スクリプト（26本）は
#     `/opt/pw-browsers/chromium-*/chrome-linux/chrome` で探すので、chrome-linux64 しかない環境では chrome-linux という名前の
#     シンボリックリンクを作って見つかるようにする（作成スクリプトを1本ずつ直さずに済む）
set -u

echo "== 1. 日本語フォント"
if [ "$(fc-list 2>/dev/null | grep -c 'Noto Sans CJK')" = "0" ]; then
  apt-get update -qq >/dev/null 2>&1
  apt-get install -y -qq fonts-noto-cjk >/dev/null 2>&1
  rm -rf ~/.cache/matplotlib
fi
echo "   Noto Sans CJK のフォント数: $(fc-list 2>/dev/null | grep -c 'Noto Sans CJK')（0なら失敗）"

echo "== 2. Python のライブラリ"
python3 -c "import matplotlib, pymupdf, playwright, numpy" 2>/dev/null || python3 -m pip install -q matplotlib pymupdf playwright numpy pillow 2>&1 | tail -1
rm -rf ~/.cache/matplotlib

echo "== 3. PIL"
if ! python3 -c "from PIL import Image" 2>/dev/null; then
  DST="$(python3 -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')"
  python3 -m pip install -q --ignore-installed --target "$DST" pillow 2>&1 | tail -1
fi
python3 -c "from PIL import Image; print('   PIL OK')" 2>&1 | tail -1

echo "== 4. Chromium（playwright）"
for d in /opt/pw-browsers/chromium-*; do
  [ -d "$d" ] || continue
  if [ -x "$d/chrome-linux64/chrome" ] && [ ! -e "$d/chrome-linux" ]; then ln -s chrome-linux64 "$d/chrome-linux"; fi
done
ls /opt/pw-browsers/chromium-*/chrome-linux*/chrome 2>/dev/null | sed 's/^/   /' || true
python3 - <<'EOF'
import glob
exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux*/chrome'))
print('   Chromium:', exe[-1] if exe else '見つからない（/opt/pw-browsers を確かめる）')
EOF
echo "== 完了"
