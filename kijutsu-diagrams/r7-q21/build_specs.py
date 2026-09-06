#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
令和7年度 第21問（土地）の座標仕様書(spec JSON)を生成するスクリプト。

座標・境界標の種類は src/data/kijutsu.json の chosashi_R07_q21（問題文・自作模範解答）
および法務省が公表した問題冊子（public/kijutsu/R07-tochi/q1.png〜q4.png）の
〔調査図素図〕〔合成図〕〔遺産分割協議書添付図〕と突き合わせて確認済み。
D点・K点は座標計算（トラバース計算・等積分割）でこのリポジトリのセッション内で
独立検算し、模範解答と一致することを確認した。

実行すると同じフォルダに spec_00〜03.json を書き出す。SVGの生成は
traverse_tool.py 側で行う（このスクリプトはJSON仕様書の組み立てのみ）。
"""
import json
import os

POINTS = {
    "A": (184.31, 99.33, "concrete"),
    "B": (219.57, 99.33, "concrete"),
    "C": (219.57, 117.56, "concrete"),
    "D": (201.71, 114.41, "concrete"),   # 発見されたコンクリート杭（トラバース計算で検算済み）
    "E": (184.31, 114.41, "concrete"),
    "F": (184.31, 130.08, "concrete"),
    "G": (193.50, 131.88, "kinzoku"),
    "H": (217.00, 131.88, "concrete"),
    "K": (199.98, 131.88, "kinzoku"),     # 等積分割点（このセッションで再計算し一致確認）
    "I": (216.07, 99.33, "none"),         # B-A線上、幾何条件のみで定まる点（境界標の記載なし）
    "J": (216.07, 116.94, "none"),        # C-D線上、同上
    "M": (205.30, 115.04, "concrete"),
    "L": (203.64, 131.88, "kinzoku"),
    "T1": (185.31, 135.37, "takakuten"),
    "T2": (188.60, 92.18, "takakuten"),
}

BASE_META = {
    "chiban_ward": "S市N町三丁目／S市T町一丁目",
    "surveyor": "民事秋子",
    "scale_label": "1:250",
    "coord_system_no": "（問題文に明記なし）",
}


def points_block(names):
    out = []
    for n in names:
        x, y, mark = POINTS[n]
        out.append({"name": n, "x": x, "y": y, "mark": mark})
    return out


def write_spec(filename, meta_extra, points_names, parcels, ref_lines=None):
    spec = {
        "meta": {**BASE_META, **meta_extra},
        "points": points_block(points_names),
        "parcels": parcels,
        "reference_lines": ref_lines or [],
    }
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(spec, f, ensure_ascii=False, indent=2)
    print("wrote", path)


ALL_POINTS = list(POINTS.keys())

# --- 00: 調査図素図（原始状態） ---
write_spec(
    "spec_00_overview.json",
    {"title": "調査図素図（令和7年度 第21問・土地）", "case": "現況（登記申請前）", "chiban": "206番／10番"},
    ALL_POINTS,
    parcels=[
        {"label": "206番（甲土地・畑）", "boundary": ["A", "B", "C", "D", "E"], "kind": "land", "fill": "existing", "chimoku": "畑"},
        {"label": "10番（乙土地・宅地・全体）", "boundary": ["D", "C", "H", "G", "F", "E"], "kind": "land", "fill": "new", "chimoku": "宅地"},
    ],
    ref_lines=[
        {"from": "T2", "to": "T1", "label": "基準点間"},
        {"from": "T2", "to": "D", "label": "観測"},
    ],
)

# --- 01: 乙土地の地積更正＋分筆（D-K線で等積分割） ---
write_spec(
    "spec_01_bunkatsu.json",
    {"title": "乙土地：地積更正・分筆（令和7年8月15日申請）", "case": "地積更正登記＋分筆登記", "chiban": "10番 → 10番1・10番2"},
    ["A", "B", "C", "D", "E", "F", "G", "H", "K"],
    parcels=[
        {"label": "206番（甲土地・参考）", "boundary": ["A", "B", "C", "D", "E"], "kind": "land", "fill": "#EEEEEE", "chimoku": "畑"},
        {"label": "10番1（北側・一郎取得）", "boundary": ["D", "C", "H", "K"], "kind": "land", "fill": "existing", "chimoku": "宅地"},
        {"label": "10番2（南側・二郎取得）", "boundary": ["D", "K", "G", "F", "E"], "kind": "land", "fill": "new", "chimoku": "宅地"},
    ],
)

# --- 02: 甲土地⇔丙土地（10番1）の等積交換（B-C-J-I ⇔ M-L-K-D） ---
write_spec(
    "spec_02_koukan.json",
    {"title": "甲土地・丙土地の交換（等積分割の応用）", "case": "交換合意に基づく分合筆（登記自体は206番・10番1それぞれ別途）", "chiban": "206番 ⇔ 10番1"},
    ["A", "B", "C", "D", "E", "H", "K", "I", "J", "M", "L"],
    parcels=[
        {"label": "206番（甲土地・畑）", "boundary": ["A", "B", "C", "D", "E"], "kind": "land", "fill": "#EEEEEE", "chimoku": "畑"},
        {"label": "10番1（丙土地・分割直後）", "boundary": ["D", "C", "H", "K"], "kind": "land", "fill": "#EAF3EA", "chimoku": "宅地"},
        {"label": "甲→丙 交換分（B-C-J-I）", "boundary": ["B", "C", "J", "I"], "kind": "land", "fill": "new", "chimoku": "宅地"},
        {"label": "丙→甲 交換分（M-L-K-D）", "boundary": ["M", "L", "K", "D"], "kind": "land", "fill": "existing", "chimoku": "宅地"},
    ],
)

# --- 03: 丙土地（10番1）の分筆（令和7年10月30日申請、10番1・10番3） ---
write_spec(
    "spec_03_final.json",
    {"title": "丙土地：分筆登記（令和7年10月30日申請）", "case": "分筆登記", "chiban": "10番1 → 10番1（残地）・10番3"},
    ["D", "C", "H", "K", "M", "L"],
    parcels=[
        {"label": "10番1（残地・二郎交換分）", "boundary": ["C", "H", "L", "M"], "kind": "land", "fill": "existing", "chimoku": "宅地"},
        {"label": "10番3（新設・花子へ譲渡予定）", "boundary": ["M", "L", "K", "D"], "kind": "land", "fill": "new", "chimoku": "宅地"},
    ],
)
