# 朝の問題ページ（out/dayNNN-am.html）がA4 1枚に収まるかを、Chromium でPDFにしてページ数で確かめる（2枚以上の日を表示）。使い方: bash daily-drill/fit_am.sh
cd "$(dirname "$0")"
S=$(mktemp -d)
for d in $(seq 1 120); do f=out/day$(printf %03d $d)-am.html; /opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --no-sandbox --disable-gpu --print-to-pdf=$S/a.pdf --no-pdf-header-footer file://$PWD/$f 2>/dev/null; n=$(python3 -c "import re;print(len(re.findall(rb'/Type\s*/Page[^s]',open('$S/a.pdf','rb').read())))"); [ "$n" != "1" ] && echo "$f $n"; done; echo done
