# 作図の描き方の追加（drawing/）

`draw_forms.py` の `chiseki_solved`・`tatemono_solved` は、spec に `'renderer': '名前'` があると、このフォルダの `r_名前.py` の `solved(s)` で模範の作図を描く。
区分建物の建物図面（一棟の建物の点線・建物の存する部分）、合体前後の建物、分合筆の地積測量図など、型ごとの描き方を、共有の関数を書き換えずに足すために使う。

- 地積測量図（draw='chiseki'）の `solved(s)` は SVG の文字列を1つ返す。
- 建物図面・各階平面図（draw='tatemono'）の `solved(s)` は (建物図面のSVG, 各階平面図のSVG) を返す。
- 枠・文字・線は `draw_forms` の `frame`・`Map`・`_t`・`_l`・`_poly`・`north_mark`・`dist_label` を import して使い、実寸（1/250＝4mm/m、1/500＝2mm/m）を守る。
