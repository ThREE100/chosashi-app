"""noteで公開する out/ のHTMLに、自分だけが知っておけばよい内部の要素（資料のパス・ファイル名、照合や検査の記録、作成の道具の名前）が入っていないかを確かめる。
使い方: python3 daily-drill/check_public.py"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BAN = re.compile(r'note-articles|laws/|照合済み|原文で照合|独立照合|\.md\b|\.py\b|\.json\b|daily-drill|registry|kiroku|check_|独立に解|機械で作図|過去問の解説|エージェント|AI|スクリプト')
ng = 0
for fp in sorted(glob.glob(os.path.join(HERE, 'out', '*.html'))):
    t = re.sub(r'<style>.*?</style>', '', open(fp, encoding='utf-8').read(), flags=re.S)
    t = re.sub(r'<[^>]+>', ' ', t)
    for m in BAN.finditer(t):
        print(f'NG {os.path.basename(fp)}: 公開用のページに内部の要素「{m.group(0)}」…{t[max(0, m.start() - 20):m.end() + 20].strip()}')
        ng += 1
print(f'公開用ページの検査：{len(glob.glob(os.path.join(HERE, "out", "*.html")))}ファイル、NG {ng}件')
sys.exit(1 if ng else 0)
