#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
traverse_tool.py — 座標データから地積測量図・建物図面を「正確に」描画するツール

## これは何か

学習漫画パイプライン（アーティファクト「学習漫画制作パイプライン」参照）が前提としていた、
「地積測量図・建物図面のような技術的に正確でなければならない図は、生成AIに絵として
描かせず、座標ベースのスクリプトで生成する」という役割分担を実現するための実装。

入力は座標・筆界点・境界標などを記述したJSON仕様書（下記フォーマット参照）。
出力はSVG（拡大縮小しても劣化しない・そのまま学習漫画のコマに合成できる）。
外部ライブラリに依存せず、Python標準ライブラリのみで動く。

画像生成AI（Gemini/ChatGPT）が担当するのは、このSVGに重ねる「小さいキャラクター」と
「吹き出し」だけであり、座標・辺長・面積計算はすべてこのツールが機械的に検算する。

## 使い方

    python3 traverse_tool.py spec.json -o out.svg
    python3 traverse_tool.py --example > example_spec.json   # サンプル仕様書を出力

## 仕様書（spec JSON）のフォーマット

{
  "meta": {
    "title": "地積測量図",                 // 図面種別（省略時は自動判定）
    "chiban_ward": "S市N町三丁目",         // 地番区域の名称（規則77条1項1号）
    "chiban": "206番1",                    // 地番（規則77条1項4号）
    "adjacent_chiban": ["206番2", "205番"],// 隣接地の地番（同号）
    "case": "分筆登記",                     // 事件（表示のみ、任意）
    "surveyor": "民事秋子",                 // 作成者（規則73条2項）
    "date": "令和7年10月1日",               // 作成年月日（同項）
    "scale_label": "1:250",                // 縮尺の表示（規則77条4項：原則1/250）
    "coord_system_no": "第Ⅷ系",            // 平面直角座標系の番号（規則77条1項7号）
    "chimoku": "宅地"                       // 地目（規則100条の地積端数処理に使用）
  },
  "points": [
    {"name": "A", "x": 105.62, "y": 88.40, "mark": "kinzoku"},
    {"name": "B", "x": 112.10, "y": 95.30, "mark": "concrete"}
  ],
  "parcels": [
    {"label": "206番1", "boundary": ["A", "B", "C", "D"], "kind": "land", "fill": "existing"},
    {"label": "206番2", "boundary": ["D", "C", "E", "F"], "kind": "land", "fill": "new"}
  ],
  "reference_lines": [
    {"from": "T1", "to": "A"}
  ],
  "characters": [
    {"id": "akiko", "anchor": "K", "dx": 40, "dy": -90, "size": 72,
     "image": null, "label": "秋子", "color": "#F5B942"}
  ],
  "speech_bubbles": [
    {"text": "差は公差の範囲を\n超えています", "character": "akiko",
     "dx": 0, "dy": -70, "width": 200}
  ]
}

- points の x = 北方向の座標値、y = 東方向の座標値（Survey.tsx と同じ座標系の約束：
  X=北, Y=東, 方向角は北から時計回り）。
- points[].mark は境界標の種類。MARK_SYMBOLSのキー（下記）を使う。省略可（無印）。
- parcels[].kind は "land"（土地・座標法で求積）または "building"（建物・床面積は
  丸め規則が別のため参考値として面積のみ表示し、登記用丸めは行わない）。
- parcels[].fill は "existing"（分筆前・現況）/ "new"（分筆後・新設）/ 任意の色名。
- parcels[].chimoku は当該筆の地目（省略時は meta.chimoku、それも省略時は"宅地"）。
  1つの図面に地目の異なる筆（畑・宅地等）が混在する場合に、規則100条の端数処理を
  筆ごとに正しく適用するために使う。
- characters[] は学習漫画のコマに乗せる小さいキャラクター。anchor（points内の
  点名）を基準に dx/dy（px）だけずらした位置に配置する。image（PNG等のファイル
  パス）を指定すればそれをそのまま埋め込み、省略すればプレースホルダー（丸顔
  アイコン）を描く。座標・図形の正確さはこのツールが担保する部分であり、
  キャラクターの絵そのもの（image未指定時のプレースホルダーを含む）は対象外。
- speech_bubbles[] は吹き出し。character（characters[].id）を指定すればそのキャラの
  上に、anchor（points内の点名）を指定すればその点を基準に配置する。text内の
  "\n"で改行、それ以外は width から自動で折り返す。文字はこのツール自身が組版
  するため、AIが生成した画像内の文字化け・誤字のリスクを避けられる。

## 法的根拠（このツールが機械的に担保する内容）

- 地積測量図の記録事項（地番区域の名称・方位・縮尺・地番・地積及びその求積方法・
  筆界点間の距離・平面直角座標系の番号・座標値・境界標の種類）：不動産登記規則第77条1項
- 縮尺は原則250分の1：同条4項
- 地積の端数処理（宅地・鉱泉地以外で10㎡超は1㎡未満切り捨て、それ以外は
  1㎡の100分の1未満切り捨て）：不動産登記規則第100条
  （条文原文は note-articles/laws/fudousan-touki-kisoku-1.md で確認済み）
- 面積計算式（座標法）：2A = Σ Xi(Y[i+1] − Y[i−1])。src/components/Survey.tsx の
  座標求積ロジックと同じ式・同じ座標系の約束に統一している。

条文の解釈が問題そのものの前提条件と食い違う場合（縮尺の例外事由がある等）は、
meta.scale_label で表示だけ上書きし、実際の描画スケールは常に自動フィット
（縦横比を保ち、角度・比率が歪まないことを優先）にしている。印刷用に正確な
1/250物理スケールが必要な場合は --px-per-meter で明示的に指定すること。
"""
from __future__ import annotations

import argparse
import base64
import json
import math
import mimetypes
import sys
from dataclasses import dataclass, field
from typing import Optional

# ---------------------------------------------------------------------------
# 境界標の種類（不動産登記規則77条1項9号・3項：符号＋種類を記録）
# ---------------------------------------------------------------------------
MARK_SYMBOLS = {
    "kinzoku": ("●", "金属標"),
    "concrete": ("□", "コンクリート杭"),
    "plastic": ("○", "プラスチック杭"),
    "kariguoi": ("×", "仮杭"),
    "inshoten": ("▲", "引照点"),
    "takakuten": ("◎", "多角点（基準点）"),
    "none": ("・", "境界標なし（推定点）"),
}
DEFAULT_MARK = "none"

FILL_COLORS = {
    "existing": "#F1EEE3",
    "new": "#E4ECF3",
}


@dataclass
class Point:
    name: str
    x: float  # 北方向
    y: float  # 東方向
    mark: str = DEFAULT_MARK


@dataclass
class Parcel:
    label: str
    boundary: list[str]
    kind: str = "land"
    fill: str = "existing"
    chimoku: Optional[str] = None  # 未指定時は meta.chimoku（既定"宅地"）を使う


@dataclass
class RefLine:
    frm: str
    to: str
    label: str = ""


@dataclass
class Character:
    """学習漫画のコマに合成する小さいキャラクター。

    座標・図形の正確さはこのツールが担保するが、キャラクターの絵そのものは
    このツールの担当外。image を指定しなければ簡易プレースホルダー（顔アイコン）
    を描画するので、位置決め・吹き出しとの組版だけを先に固められる。
    image に画像生成AI（Gemini/ChatGPT等）が作成したPNG等のパスを指定すれば、
    そのまま座標位置に埋め込まれる。
    """

    id: str
    anchor: str  # points内の点名。この点を基準に配置する
    dx: float = 0.0
    dy: float = -90.0
    size: float = 72.0
    image: Optional[str] = None
    label: str = "？"
    color: str = "#F5B942"


@dataclass
class SpeechBubble:
    text: str
    character: Optional[str] = None  # characters[].id。指定した場合はそのキャラの上に表示
    anchor: Optional[str] = None  # character未指定時、points内の点を直接指定
    dx: float = 0.0
    dy: float = -60.0
    width: float = 220.0


@dataclass
class Spec:
    meta: dict
    points: dict[str, Point]
    parcels: list[Parcel]
    ref_lines: list[RefLine] = field(default_factory=list)
    characters: list[Character] = field(default_factory=list)
    speech_bubbles: list[SpeechBubble] = field(default_factory=list)


# ---------------------------------------------------------------------------
# 仕様書の読み込み
# ---------------------------------------------------------------------------
def load_spec(path: str) -> Spec:
    with open(path, encoding="utf-8") as f:
        raw = json.load(f)
    points = {}
    for p in raw["points"]:
        mark = p.get("mark", DEFAULT_MARK)
        if mark not in MARK_SYMBOLS:
            raise ValueError(f"未知の境界標種別です: {mark!r}（点 {p['name']}）")
        points[p["name"]] = Point(p["name"], float(p["x"]), float(p["y"]), mark)
    parcels = []
    for pc in raw.get("parcels", []):
        for name in pc["boundary"]:
            if name not in points:
                raise ValueError(f"筆界点 {name!r} が points に定義されていません（parcel {pc['label']!r}）")
        parcels.append(Parcel(pc["label"], pc["boundary"], pc.get("kind", "land"), pc.get("fill", "existing"), pc.get("chimoku")))
    ref_lines = []
    for rl in raw.get("reference_lines", []):
        ref_lines.append(RefLine(rl["from"], rl["to"], rl.get("label", "")))
    characters = []
    for c in raw.get("characters", []):
        if c["anchor"] not in points:
            raise ValueError(f"characters[].anchor が points に見つかりません: {c['anchor']!r}")
        characters.append(Character(
            id=c["id"], anchor=c["anchor"], dx=c.get("dx", 0.0), dy=c.get("dy", -90.0),
            size=c.get("size", 72.0), image=c.get("image"), label=c.get("label", "？"),
            color=c.get("color", "#F5B942"),
        ))
    char_ids = {c.id for c in characters}
    speech_bubbles = []
    for sb in raw.get("speech_bubbles", []):
        character = sb.get("character")
        anchor = sb.get("anchor")
        if character is None and anchor is None:
            raise ValueError("speech_bubbles[] には character または anchor のいずれかが必要です")
        if character is not None and character not in char_ids:
            raise ValueError(f"speech_bubbles[].character が characters に見つかりません: {character!r}")
        if anchor is not None and anchor not in points:
            raise ValueError(f"speech_bubbles[].anchor が points に見つかりません: {anchor!r}")
        speech_bubbles.append(SpeechBubble(
            text=sb["text"], character=character, anchor=anchor,
            dx=sb.get("dx", 0.0), dy=sb.get("dy", -60.0), width=sb.get("width", 220.0),
        ))
    return Spec(
        meta=raw.get("meta", {}), points=points, parcels=parcels, ref_lines=ref_lines,
        characters=characters, speech_bubbles=speech_bubbles,
    )


# ---------------------------------------------------------------------------
# 幾何計算（Survey.tsx と同じ座標系の約束：X=北, Y=東, 方向角は北から時計回り）
# ---------------------------------------------------------------------------
def distance(p1: Point, p2: Point) -> float:
    return math.hypot(p2.x - p1.x, p2.y - p1.y)


def azimuth_deg(p1: Point, p2: Point) -> float:
    """北を0度とし時計回りの方向角（度）。"""
    dx = p2.x - p1.x  # 北方向成分
    dy = p2.y - p1.y  # 東方向成分
    deg = math.degrees(math.atan2(dy, dx))
    return deg % 360


def polygon_double_area(pts: list[Point]) -> float:
    """座標法：2A = Σ Xi(Y[i+1] − Y[i−1])。符号付きの値を返す（絶対値は呼び出し側で取る）。"""
    n = len(pts)
    total = 0.0
    for i in range(n):
        x_i = pts[i].x
        y_next = pts[(i + 1) % n].y
        y_prev = pts[(i - 1) % n].y
        total += x_i * (y_next - y_prev)
    return total


def round_chiseki(area_sqm: float, chimoku: str = "宅地") -> tuple[float, str]:
    """
    不動産登記規則第100条：
    「地積は、水平投影面積により、平方メートルを単位として定め、一平方メートルの
    百分の一（宅地及び鉱泉地以外の土地で十平方メートルを超えるものについては、
    一平方メートル）未満の端数は、切り捨てる。」
    戻り値: (丸めた地積, 適用した端数単位の説明)
    """
    is_sqm_unit = chimoku not in ("宅地", "鉱泉地") and area_sqm > 10
    if is_sqm_unit:
        rounded = math.floor(area_sqm)
        return float(rounded), "1㎡未満切り捨て（宅地・鉱泉地以外／10㎡超）"
    else:
        rounded = math.floor(area_sqm * 100) / 100
        return rounded, "0.01㎡未満切り捨て"


# ---------------------------------------------------------------------------
# SVG 生成
# ---------------------------------------------------------------------------
PAD = 40
PLOT_W = 640
PLOT_H = 640
TABLE_W = 360


def esc(s: str) -> str:
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


class SvgBuilder:
    def __init__(self):
        self.parts: list[str] = []

    def add(self, s: str):
        self.parts.append(s)

    def text(self, x, y, s, size=13, anchor="start", weight="normal", fill="#1E2530",
              rotate: Optional[float] = None, family="sans-serif"):
        transform = f' transform="rotate({rotate:.2f} {x:.2f} {y:.2f})"' if rotate else ""
        self.add(
            f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size}" font-family="{family}" '
            f'text-anchor="{anchor}" font-weight="{weight}" fill="{fill}"{transform}>{esc(s)}</text>'
        )

    def line(self, x1, y1, x2, y2, stroke="#1E2530", width=1.4, dash: Optional[str] = None):
        dasharray = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(
            f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" '
            f'stroke="{stroke}" stroke-width="{width}"{dasharray}/>'
        )

    def polygon(self, points_xy, fill, stroke="#2B5C86", width=1.8):
        pts = " ".join(f"{x:.2f},{y:.2f}" for x, y in points_xy)
        self.add(f'<polygon points="{pts}" fill="{fill}" fill-opacity="0.55" stroke="{stroke}" stroke-width="{width}"/>')

    def rect(self, x, y, w, h, fill="none", stroke="#DCD5C3", width=1):
        self.add(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>')

    def circle(self, x, y, r, fill="#1E2530", stroke="none"):
        self.add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{fill}" stroke="{stroke}"/>')

    def render(self, width, height) -> str:
        header = (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" font-family="\'Noto Sans JP\',\'Hiragino Sans\',sans-serif">\n'
            f'<rect x="0" y="0" width="{width}" height="{height}" fill="#FFFFFF"/>\n'
        )
        return header + "\n".join(self.parts) + "\n</svg>\n"


def build_transform(pts: list[Point]):
    xs = [p.x for p in pts]
    ys = [p.y for p in pts]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    range_x = max(max_x - min_x, 1e-6)
    range_y = max(max_y - min_y, 1e-6)
    inner_w = PLOT_W - 2 * PAD
    inner_h = PLOT_H - 2 * PAD
    scale = min(inner_w / range_y, inner_h / range_x)

    plot_left = 0
    plot_top = 0

    def to_xy(p: Point):
        sx = plot_left + PAD + (p.y - min_y) * scale
        sy = plot_top + PAD + (max_x - p.x) * scale  # 北=上
        return sx, sy

    return to_xy, scale, (min_x, max_x, min_y, max_y)


def draw_north_arrow(svg: SvgBuilder, x: float, y: float):
    svg.add(f'<g stroke="#1E2530" stroke-width="1.6" fill="#1E2530">')
    svg.add(f'<line x1="{x}" y1="{y+26}" x2="{x}" y2="{y-14}"/>')
    svg.add(f'<polygon points="{x-7},{y-6} {x+7},{y-6} {x},{y-20}"/>')
    svg.add("</g>")
    svg.text(x, y + 40, "N", size=14, anchor="middle", weight="bold")


def draw_scale_bar(svg: SvgBuilder, x: float, y: float, scale_px_per_unit: float, label: str):
    # 1メートル相当のバーを描画（scale_px_per_unitは「1座標単位=何px」のため、
    # 座標単位=メートル運用を前提とする）
    bar_len = scale_px_per_unit  # 1単位分
    svg.line(x, y, x + bar_len, y, stroke="#1E2530", width=2)
    svg.line(x, y - 5, x, y + 5, stroke="#1E2530", width=2)
    svg.line(x + bar_len, y - 5, x + bar_len, y + 5, stroke="#1E2530", width=2)
    svg.text(x + bar_len / 2, y - 10, "1m", size=11, anchor="middle")
    svg.text(x, y + 22, f"表示縮尺（自動フィット・目安）／記載縮尺: {label}", size=10, anchor="start", fill="#5B6470")


def _image_data_uri(path: str) -> str:
    mime, _ = mimetypes.guess_type(path)
    mime = mime or "image/png"
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def draw_character(svg: SvgBuilder, cx: float, cy: float, size: float,
                    image: Optional[str], label: str, color: str):
    """小さいキャラクターを描画する。

    image が指定されていればそれ（画像生成AIが作成したPNG等）をそのまま
    座標位置に埋め込む。指定がなければ、位置決めと組版だけを先に確認できる
    ための簡易プレースホルダー（丸顔アイコン）を描画する。プレースホルダーは
    最終的な学習漫画の見た目ではなく、あくまで「ここにキャラクターが乗る」
    ことを示す仮表示。
    """
    r = size / 2
    if image:
        data_uri = _image_data_uri(image)
        svg.add(
            f'<image x="{cx - r:.2f}" y="{cy - r:.2f}" width="{size:.2f}" '
            f'height="{size:.2f}" href="{data_uri}" preserveAspectRatio="xMidYMid meet"/>'
        )
        return
    svg.circle(cx, cy, r, fill=color, stroke="#1E2530")
    eye_dx, eye_dy, eye_r = r * 0.32, r * 0.15, r * 0.1
    svg.circle(cx - eye_dx, cy - eye_dy, eye_r, fill="#1E2530")
    svg.circle(cx + eye_dx, cy - eye_dy, eye_r, fill="#1E2530")
    svg.add(
        f'<path d="M {cx - r * 0.32:.2f} {cy + r * 0.2:.2f} '
        f'Q {cx:.2f} {cy + r * 0.5:.2f} {cx + r * 0.32:.2f} {cy + r * 0.2:.2f}" '
        f'stroke="#1E2530" stroke-width="2" fill="none"/>'
    )
    svg.text(cx, cy + r + 15, label, size=11, anchor="middle", fill="#5B6470")


def wrap_text_for_bubble(text: str, max_chars: int) -> list[str]:
    """日本語は分かち書きされないため、改行指定（\\n）を尊重しつつ文字数で折り返す。"""
    max_chars = max(4, max_chars)
    lines: list[str] = []
    for para in text.split("\n"):
        if not para:
            lines.append("")
            continue
        cur = ""
        for ch in para:
            cur += ch
            if len(cur) >= max_chars:
                lines.append(cur)
                cur = ""
        if cur:
            lines.append(cur)
    return lines or [""]


def draw_speech_bubble(svg: SvgBuilder, cx: float, cy: float, width: float,
                        text: str, tail_to: Optional[tuple[float, float]] = None):
    """吹き出しを描画する（角丸の枠＋折り返しテキスト＋任意の尻尾）。

    テキストはこのツール自身が組版する（AIに文字入りの画像を生成させない）。
    こうすることで、吹き出しの中の文言は常にJSON仕様書に書いた文字列と
    一致し、生成AI特有の文字化け・誤字のリスクを避けられる。
    """
    pad = 12
    line_h = 18
    lines = wrap_text_for_bubble(text, max_chars=max(6, int(width / 13)))
    h = pad * 2 + line_h * len(lines)
    x0, y0 = cx - width / 2, cy - h
    svg.add(
        f'<rect x="{x0:.2f}" y="{y0:.2f}" width="{width:.2f}" height="{h:.2f}" '
        f'rx="10" fill="#FFFFFF" stroke="#1E2530" stroke-width="1.6"/>'
    )
    if tail_to:
        tx, ty = tail_to
        bx, by = cx, y0 + h
        svg.add(
            f'<path d="M {bx - 10:.2f} {by:.2f} L {bx + 10:.2f} {by:.2f} '
            f'L {tx:.2f} {ty:.2f} Z" fill="#FFFFFF" stroke="#1E2530" stroke-width="1.6"/>'
        )
    for i, line in enumerate(lines):
        svg.text(cx, y0 + pad + line_h * (i + 1) - 5, line, size=12.5, anchor="middle")


def edge_label_position(x1, y1, x2, y2, offset=14):
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    dx, dy = x2 - x1, y2 - y1
    length = math.hypot(dx, dy) or 1
    nx, ny = -dy / length, dx / length  # 法線ベクトル
    lx, ly = mx + nx * offset, my + ny * offset
    angle = math.degrees(math.atan2(dy, dx))
    if angle > 90 or angle < -90:
        angle += 180
    return lx, ly, angle


def render_spec(spec: Spec) -> str:
    meta = spec.meta
    all_pts = list(spec.points.values())
    if not all_pts:
        raise ValueError("points が空です")
    to_xy, scale, bbox = build_transform(all_pts)

    svg = SvgBuilder()
    total_w = PLOT_W + TABLE_W
    total_h = max(PLOT_H, 120 + 90 * max(len(spec.parcels), 1))

    # --- タイトルブロック（規則77条1項の記録事項） ---
    title = meta.get("title", "地積測量図" if all(p.kind == "land" for p in spec.parcels) else "建物図面")
    svg.text(PAD, 30, title, size=20, weight="bold")
    info_lines = [
        f"地番区域: {meta.get('chiban_ward', '(未設定)')}",
        f"地番: {meta.get('chiban', '(未設定)')}" + (
            f"（隣接: {'、'.join(meta.get('adjacent_chiban', []))}）" if meta.get("adjacent_chiban") else ""
        ),
        f"事件: {meta.get('case', '-')}",
        f"求積方法: 座標法",
        f"平面直角座標系: {meta.get('coord_system_no', '(未設定)')}",
        f"作成者: {meta.get('surveyor', '(未設定)')}　作成年月日: {meta.get('date', '(未設定)')}",
    ]
    for i, line in enumerate(info_lines):
        svg.text(PAD, 50 + i * 16, line, size=11.5, fill="#5B6470")

    plot_origin_y = 50 + len(info_lines) * 16 + 20
    svg.add(f'<g transform="translate(0,{plot_origin_y})">')

    # --- 求積線・境界線 ---
    used_marks = set()
    drawn_points: set[str] = set()

    def draw_point_marker(p: Point, x: float, y: float):
        symbol, _ = MARK_SYMBOLS[p.mark]
        used_marks.add(p.mark)
        drawn_points.add(p.name)
        svg.circle(x, y, 3, fill="#1E2530")
        svg.text(x + 8, y - 8, f"{symbol}{p.name}", size=12, weight="bold")

    for parcel in spec.parcels:
        names = parcel.boundary
        pts = [spec.points[n] for n in names]
        xy = [to_xy(p) for p in pts]
        fill = FILL_COLORS.get(parcel.fill, parcel.fill)
        svg.polygon(xy, fill=fill)

        n = len(pts)
        for i in range(n):
            p1, p2 = pts[i], pts[(i + 1) % n]
            (x1, y1), (x2, y2) = xy[i], xy[(i + 1) % n]
            svg.line(x1, y1, x2, y2, stroke="#2B5C86", width=1.8)
            d = distance(p1, p2)
            lx, ly, angle = edge_label_position(x1, y1, x2, y2)
            svg.text(lx, ly, f"{d:.2f}m", size=10.5, anchor="middle", fill="#C9711F", rotate=angle)

        for p, (x, y) in zip(pts, xy):
            draw_point_marker(p, x, y)

        label_x, label_y = xy[0]
        svg.text(label_x, label_y - 20, parcel.label, size=13, weight="bold", fill="#2B5C86")

    # --- 引照線 ---
    for rl in spec.ref_lines:
        p1, p2 = spec.points[rl.frm], spec.points[rl.to]
        (x1, y1), (x2, y2) = to_xy(p1), to_xy(p2)
        svg.line(x1, y1, x2, y2, stroke="#5B6470", width=1, dash="4,3")
        if rl.label:
            lx, ly, angle = edge_label_position(x1, y1, x2, y2, offset=10)
            svg.text(lx, ly, rl.label, size=9.5, anchor="middle", fill="#5B6470", rotate=angle)
        # 境界線（parcels）に含まれない引照線の端点（基準点・多角点等）も描画する
        for p, (x, y) in ((p1, (x1, y1)), (p2, (x2, y2))):
            if p.name not in drawn_points:
                draw_point_marker(p, x, y)

    # --- キャラクター・吹き出し（学習漫画のコマへの組版） ---
    # 図形・座標・面積の正確さはここまでの描画がすべて担保する。ここから先は
    # 「その正確な図に、小さいキャラクターと吹き出しをどう乗せるか」という
    # レイアウトの話であり、キャラクターの絵自体（image未指定時はプレース
    # ホルダー）が最終品質かどうかとは別の話である。
    char_pos: dict[str, tuple[float, float, float]] = {}
    for ch in spec.characters:
        ax, ay = to_xy(spec.points[ch.anchor])
        cx, cy = ax + ch.dx, ay + ch.dy
        char_pos[ch.id] = (cx, cy, ch.size)
        draw_character(svg, cx, cy, ch.size, ch.image, ch.label, ch.color)

    for sb in spec.speech_bubbles:
        if sb.character:
            base_x, base_y, csize = char_pos[sb.character]
            bx, by = base_x + sb.dx, base_y + sb.dy
            tail_to = (base_x, base_y - csize / 2)
        else:
            ax, ay = to_xy(spec.points[sb.anchor])
            bx, by = ax + sb.dx, ay + sb.dy
            tail_to = (ax, ay)
        draw_speech_bubble(svg, bx, by, sb.width, sb.text, tail_to=tail_to)

    svg.add("</g>")

    draw_north_arrow(svg, PLOT_W - 50, plot_origin_y + 20)
    draw_scale_bar(svg, PAD, plot_origin_y + PLOT_H - PAD + 20, scale, meta.get("scale_label", "1:250"))

    # --- 境界標の種類 凡例（規則77条1項9号） ---
    legend_y = plot_origin_y + PLOT_H - PAD + 55
    svg.text(PAD, legend_y, "境界標の種類:", size=10.5, weight="bold", fill="#5B6470")
    lx = PAD + 110
    for mark in used_marks:
        symbol, name = MARK_SYMBOLS[mark]
        svg.text(lx, legend_y, f"{symbol} {name}", size=10.5, fill="#5B6470")
        lx += 30 + 11 * len(name)

    # --- 求積表（右カラム） ---
    tx = PLOT_W + 20
    ty = 30
    svg.text(tx, ty, "求積表（座標法・機械計算）", size=15, weight="bold")
    ty += 24
    for parcel in spec.parcels:
        pts = [spec.points[n] for n in parcel.boundary]
        svg.text(tx, ty, f"■ {parcel.label}", size=12.5, weight="bold", fill="#2B5C86")
        ty += 18
        svg.text(tx, ty, "符号     X(北)      Y(東)", size=10.5, family="monospace", fill="#5B6470")
        ty += 14
        for p in pts:
            svg.text(tx, ty, f"{p.name:<4}  {p.x:>9.2f}  {p.y:>9.2f}", size=10.5, family="monospace")
            ty += 14
        double_area = polygon_double_area(pts)
        area = abs(double_area) / 2
        ty += 4
        svg.text(tx, ty, f"倍面積 2A = {double_area:.2f}  →  面積 = {area:.2f}㎡", size=10.5, family="monospace")
        ty += 16
        if parcel.kind == "land":
            chimoku = parcel.chimoku or meta.get("chimoku", "宅地")
            rounded, rule = round_chiseki(area, chimoku)
            svg.text(tx, ty, f"地積（規則100条により丸め）: {rounded:.2f}㎡", size=11.5, weight="bold", fill="#C9711F")
            ty += 15
            svg.text(tx, ty, f"（{rule}）", size=9.5, fill="#5B6470")
            ty += 15
        else:
            svg.text(tx, ty, f"床面積（参考値・丸め規則は別途確認）: {area:.2f}㎡", size=11, weight="bold", fill="#C9711F")
            ty += 18
        ty += 12

    total_h = max(total_h, plot_origin_y + PLOT_H + 40, ty + 20)
    return svg.render(total_w, int(total_h))


# ---------------------------------------------------------------------------
# サンプル仕様書（動作確認・雛形コピー用）
# ---------------------------------------------------------------------------
EXAMPLE_SPEC = {
    "meta": {
        "title": "地積測量図",
        "chiban_ward": "S市N町三丁目（架空例）",
        "chiban": "206番1",
        "adjacent_chiban": ["206番2", "205番"],
        "case": "分筆登記",
        "surveyor": "民事秋子",
        "date": "令和7年10月1日",
        "scale_label": "1:250",
        "coord_system_no": "第Ⅷ系",
        "chimoku": "宅地",
    },
    "points": [
        {"name": "A", "x": 100.00, "y": 100.00, "mark": "kinzoku"},
        {"name": "B", "x": 100.00, "y": 118.50, "mark": "concrete"},
        {"name": "R", "x": 88.20, "y": 118.50, "mark": "plastic"},
        {"name": "S", "x": 88.20, "y": 100.00, "mark": "plastic"},
        {"name": "C", "x": 78.00, "y": 118.50, "mark": "concrete"},
        {"name": "D", "x": 78.00, "y": 100.00, "mark": "kinzoku"},
        {"name": "T1", "x": 105.00, "y": 95.00, "mark": "takakuten"},
    ],
    "parcels": [
        {"label": "206番1（分筆後）", "boundary": ["A", "B", "R", "S"], "kind": "land", "fill": "existing"},
        {"label": "206番2（分筆後・新設）", "boundary": ["S", "R", "C", "D"], "kind": "land", "fill": "new"},
    ],
    "reference_lines": [
        {"from": "T1", "to": "A", "label": "引照"},
    ],
}


def main():
    ap = argparse.ArgumentParser(description="座標仕様書から地積測量図・建物図面のSVGを生成する")
    ap.add_argument("spec", nargs="?", help="入力する仕様書(JSON)のパス")
    ap.add_argument("-o", "--out", help="出力SVGのパス（省略時は標準出力）")
    ap.add_argument("--example", action="store_true", help="サンプル仕様書(JSON)を標準出力に書き出して終了する")
    args = ap.parse_args()

    if args.example:
        json.dump(EXAMPLE_SPEC, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return

    if not args.spec:
        ap.error("spec を指定するか、--example でサンプルを確認してください")

    spec = load_spec(args.spec)
    svg = render_spec(spec)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"書き出しました: {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(svg)


if __name__ == "__main__":
    main()
