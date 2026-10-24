"""PM-120 の模範の作図。描き方は r_pm118.py の render（数筆の敷地・附属建物の数・各階平面図の区画の数を spec で指定する）と同じ。"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r_pm118 import render  # noqa: E402

solved = render
