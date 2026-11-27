#!/usr/bin/env bash
# 記事フォルダの画像（見出し画像＋本文の図）を1つのzipにまとめる。
# 使い方：bash note-unei/hitogara/make_zip.sh [記事フォルダ ...]
#   フォルダを省くと hitogara/ の下の NN-* をすべて処理する。
#   zip は note-unei/hitogara/zip/<フォルダ名>.zip にできる（git には入れない）。
# 足りない画像・寸法の違う画像があれば一覧を出し、そのフォルダの zip は作らない（終了コード1）。
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
OUTDIR="$HERE/zip"
mkdir -p "$OUTDIR"
if [ $# -eq 0 ]; then set -- "$HERE"/[0-9][0-9]-*/; fi
status=0
for dir in "$@"; do
  dir="${dir%/}"; name="$(basename "$dir")"
  echo "== $name"
  missing=0; files=()
  while IFS=$'\t' read -r f w h kind; do
    p="$dir/$f"
    if [ ! -f "$p" ]; then
      echo "  足りない：$f（$kind$([ "$w" != "-" ] && echo "、${w}×${h}")）"; missing=1; continue
    fi
    if [ "$w" != "-" ]; then
      size="$(python3 -c 'import struct,sys
b=open(sys.argv[1],"rb").read(24)
print("%dx%d"%struct.unpack(">II",b[16:24]) if b[:8]==b"\x89PNG\r\n\x1a\n" else "PNGではない")' "$p")"
      if [ "$size" != "${w}x${h}" ]; then
        echo "  寸法が違う：$f（${size}。期待は ${w}×${h}）"; missing=1; continue
      fi
    fi
    echo "  OK：$f"; files+=("$f")
  done < <(python3 "$HERE/src/list_images.py" "$dir")
  if [ $missing -ne 0 ]; then
    echo "  → zip は作りませんでした。上の画像をそろえてから、もう一度実行してください。"; status=1; continue
  fi
  rm -f "$OUTDIR/$name.zip"
  (cd "$dir" && zip -q -X "$OUTDIR/$name.zip" "${files[@]}")
  echo "  → 作成：$OUTDIR/$name.zip（${#files[@]}枚）"
done
exit $status
