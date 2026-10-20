#!/usr/bin/env bash
# 音声合成（Open JTalk）の声データを voices/ に取得する。1回だけ実行すればよい。
#   トリ先生: nitech_jp_atr503_m001（名古屋工業大学、修正BSDライセンス）
#   藍子    : tohoku-f01（東北大学 伊藤・能勢研究室、CC BY 4.0 → 動画の概要欄にクレジットを書く）
set -euo pipefail
cd "$(dirname "$0")/voices"
pip install --break-system-packages -q pyopenjtalk pyworld numpy pillow playwright==1.56.0 2>/dev/null || pip install -q pyopenjtalk pyworld numpy pillow playwright==1.56.0
if [ ! -d hts_voice_nitech_jp_atr503_m001-1.05 ]; then
  curl -sSL -o m001.tgz "https://downloads.sourceforge.net/project/open-jtalk/HTS%20voice/hts_voice_nitech_jp_atr503_m001-1.05/hts_voice_nitech_jp_atr503_m001-1.05.tar.gz"
  tar xzf m001.tgz && rm m001.tgz
fi
[ -d htsvoice-tohoku-f01 ] || git clone -q --depth 1 https://github.com/icn-lab/htsvoice-tohoku-f01.git
ls
