"""毎日ドリルの全チェック（朝の択一・夜の記述式）と、A4出力の作り直し。
使い方: python3 daily-drill/check_all.py"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
rc = 0
for s in ('check_registry.py', 'check_am.py', 'check_pm.py'):
    rc |= subprocess.call([sys.executable, os.path.join(HERE, s)])
rc |= subprocess.call([sys.executable, os.path.join(HERE, 'saturday', 'check_sat.py')])   # 土曜の20問模擬
rc |= subprocess.call([sys.executable, os.path.join(HERE, 'sougou', 'build_sougou.py')])   # 本番形式の統合問題（検査して出力）
rc |= subprocess.call([sys.executable, os.path.join(HERE, 'kiroku.py'), 'check'])   # 誤答の記録の形（log/）
if rc == 0:
    subprocess.call([sys.executable, os.path.join(HERE, 'coverage.py')])
    subprocess.call([sys.executable, os.path.join(HERE, 'build.py')])
    subprocess.call([sys.executable, os.path.join(HERE, 'saturday', 'build_sat.py')])
    subprocess.call([sys.executable, os.path.join(HERE, 'kiroku.py'), 'report'])
    rc |= subprocess.call([sys.executable, os.path.join(HERE, 'check_public.py')])   # 公開用ページに内部の要素がないか
    rc |= subprocess.call([sys.executable, os.path.join(HERE, 'check_choices.py')])   # 正解の組合せが選択肢にちょうど1つあるか（問題・独立の判定・印刷ページ）
sys.exit(rc)
