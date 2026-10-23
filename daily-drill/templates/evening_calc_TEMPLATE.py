"""夜の計算問題（calc2）の雛形。このファイルを evening/build_PM-NN.py にコピーし、TODO を埋める。
流れ：①点の座標を設計（四捨五入の境目を避ける） ②観測値・距離を逆算して丸める ③答えを複素数で出す（方法A）
      ④text（lead・conditions・hearing・notes）・tables（地積測量図などの参照元の題に作成年）・fig を作る
      ⑤ python3 daily-drill/evening/build_PM-NN.py → evening/problems/PM-NN.json
      ⑥ calc_keys.py に F-789SG のキー列の関数を足す → check_pm.py に別の方法（方法B）の検算を足す → registry.json に登録
ひっかけ（taxonomy.json の traps_evening）を1つ以上、聞き取り結果か条件に入れる。答えを本文に漏らさない。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from calc_exam import P, r2, shoelace, floor2, inter, dms, dms_rad, fmt, pt_row, pack  # noqa: E402,F401
import json  # noqa: E402


def build():
    # TODO 1. 点（P(X, Y)）を設計する
    # TODO 2. text = {'lead': ..., 'conditions': [...], 'hearing': [...], 'notes': [...]}
    # TODO 3. tables = [{'title': '○番の地積測量図（平成○年作成）に記載された座標値', 'cols': [...], 'rows': [pt_row(...)]}]
    # TODO 4. fig = {'points': {名: {'xy': P(..), 'kind': 'given|ref|unknown', 'dx': .., 'dy': ..}}, 'polys': [...], 'lines': [...], 'texts': [...]}
    # TODO 5. ans = [{'label': '点P', 'kind': 'xy', 'value': fmt(z)}, ...]、steps（解き方）、traps（つまずき）、verify（検算の入力）
    raise NotImplementedError('TODO')


if __name__ == '__main__':
    text, tables, fig, ans, steps, traps, verify = build()
    p = pack('PM-NN', 0, 'TODO（題）', lambda: (text, tables, fig, ans, steps, traps, verify))
    json.dump(p, open(os.path.join(HERE, 'problems', 'PM-NN.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
