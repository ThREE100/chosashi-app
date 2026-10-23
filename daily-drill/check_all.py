"""毎日ドリルの全チェック（朝の択一・夜の記述式）と、A4出力の作り直し。
使い方: python3 daily-drill/check_all.py"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
rc = 0
for s in ('check_registry.py', 'check_am.py', 'check_pm.py'):
    rc |= subprocess.call([sys.executable, os.path.join(HERE, s)])
if rc == 0:
    subprocess.call([sys.executable, os.path.join(HERE, 'coverage.py')])
    subprocess.call([sys.executable, os.path.join(HERE, 'build.py')])
sys.exit(rc)
