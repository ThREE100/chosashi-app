"""s02 第3部：建物図面（500分の1）・各階平面図（250分の1）。附属建物（符号1）を描くため、spec に annex（附属建物の外形）を持たせる。
共有の draw_forms.tatemono_solved は主である建物の1階・2階しか描かないので、このファイルを読み込んだときに、
spec に 'annex' があるときだけ下の annex_solved で描く包み（それ以外の spec は元の関数にそのまま渡す）を置く。共有のファイルは書き換えない。"""
import math
import os
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))
import draw_forms as DF  # noqa: E402
from common_s02 import (SITE, M, M2, G, HALF_M, HALF_G, F1, F2, F3, DN, DW, DE, DS, EW2, NS2, area, floor2, ADDR, LOT, LOC)  # noqa: E402

assert (floor2(area(list(M.values()))), floor2(area(M2)), floor2(area(list(G.values())))) == (F1, F2, F3)
site = [SITE[k] for k in 'ABCD']
b1 = [M[k] for k in ('m1', 'm2', 'm3', 'm4', 'm5', 'm6')]
gg = [G[k] for k in ('g1', 'g2', 'g3', 'g4')]
m1, g2, g4 = M['m1'], G['g2'], G['g4']
yd = 305.0     # 北・西の距離を描く位置
DISTS = [
 [(SITE['A'][0], 305.80), (m1[0] + HALF_M, 305.80), f'{DN:.2f}'],          # 北：筆界 → 主である建物の北の外壁
 [(513.00, SITE['A'][1]), (513.00, m1[1] - HALF_M), f'{DW:.2f}'],          # 西
 [(509.00, g2[1] + HALF_G), (509.00, SITE['B'][1]), f'{DE:.2f}'],          # 東：附属建物の東の外壁 → 筆界
 [(SITE['D'][0], 318.40), (g4[0] - HALF_G, 318.40), f'{DS:.2f}'],          # 南
]
for (a, b, t) in DISTS:
    assert f'{math.hypot(a[0] - b[0], a[1] - b[1]):.2f}' == t, (a, b, t)


def annex_solved(s):
    """建物図面（主である建物と附属建物の1階・距離・主附の別と符号）と、各階平面図（主の1階・2階、附属建物）"""
    cells = [(70, '土地の所在', s['addr']), (36, '地番', s['lot']), (36, '家屋番号', s['house']), (40, '縮尺', '1/500')]
    p1, ar = DF.frame(DF.BD_H, '建　物　図　面', cells, [(91, '作成者', '（略）'), (91, '申請人', '（略）')], top_h=14.0, foot_h=12.0)
    st = [tuple(c) for c in s['site']]
    Xs, Ys = [c[0] for c in st], [c[1] for c in st]
    m = DF.Map(ar, 500, (min(Xs) - 2.5, max(Xs) + 2.5, min(Ys) - 3.0, max(Ys) + 3.0))
    p1.append(DF._poly(m, st, 0.5))
    p1.append(DF._poly(m, s['bld1'], 0.7, fill='#e8f4f0'))
    p1.append(DF._poly(m, s['annex'], 0.7, fill='#fdf3e3'))
    for t, xy, size in s['marks']:
        x, y = m(*xy)
        p1.append(DF._t(x, y, t, size, 'middle', weight='700'))
    for a, b, t in s['dists']:
        qa, qb = m(*a), m(*b)
        p1.append(DF._l(qa[0], qa[1], qb[0], qb[1], 0.3, DF.ACC))
        vert = abs(qa[0] - qb[0]) < 0.01
        if vert:
            p1.append(DF._t(qa[0] + 1.0, (qa[1] + qb[1]) / 2 + 0.9, t, 2.6, 'start', color=DF.ACC))
        else:
            p1.append(DF._t((qa[0] + qb[0]) / 2, qa[1] - 0.9, t, 2.6, 'middle', color=DF.ACC))
    for t, xy in s['adj']:
        x, y = m(*xy)
        p1.append(DF._t(x, y, t, 3.0, 'middle', color=DF.MUTE))
    x, y = m(*s['lot_xy'])
    p1.append(DF._t(x, y, s['lot'], 3.4, 'middle', weight='700'))
    p1.append(DF.north_mark(ar[0] + ar[2] - 8, ar[1] + 12))
    # 各階平面図：3つの区画（主である建物の1階・2階、附属建物 符号1）
    cells2 = [(70, '建物の所在', s['addr'] + s['lot'] + '地'), (36, '家屋番号', s['house']), (36, '', ''), (40, '縮尺', '1/250')]
    p2, ar2 = DF.frame(DF.FP_H, '各　階　平　面　図', cells2, [(91, '作成者', '（略）'), (91, '申請人', '（略）')], top_h=14.0, foot_h=12.0)
    ax, ay, aw, ah = ar2
    ws = [aw * 0.37, aw * 0.37, aw * 0.26]
    x0 = ax
    for i, (name, pts_, under) in enumerate((('主である建物　1階', s['bld1'], None), ('主である建物　2階', s['bld2'], s['bld1']), ('符号1　附属建物　1階', s['annex'], None))):
        ref = under or pts_
        sub = (x0, ay + 6, ws[i], ah * 0.60)
        bn0, bn1 = min(c[0] for c in ref), max(c[0] for c in ref)
        bx0, bx1 = min(c[1] for c in ref), max(c[1] for c in ref)
        mm = DF.Map(sub, 250, (bn0 - 0.5, bn1 + 0.5, bx0 - 0.5, bx1 + 0.5))
        if under:
            p2.append(DF._poly(mm, under, 0.35, '1.4 1.0'))
        p2.append(DF._poly(mm, pts_, 0.7, fill='#e8f4f0' if i < 2 else '#fdf3e3'))
        n = len(pts_)
        cxy = (sum(c[0] for c in pts_) / n, sum(c[1] for c in pts_) / n)
        for j in range(n):
            u, v = pts_[j], pts_[(j + 1) % n]
            L = math.hypot(u[0] - v[0], u[1] - v[1])
            side = 1 if ((v[1] - u[1]) * (cxy[0] - u[0]) - (v[0] - u[0]) * (cxy[1] - u[1])) < 0 else -1
            p2.append(DF.dist_label(mm, u, v, f'{L:.2f}', side=-side, off=2.4, size=2.6))
        p2.append(DF._t(sub[0] + 2, sub[1] - 1.4, name, 3.2, weight='700'))
        if i < 2:
            p2.append(DF._l(x0 + ws[i], ay + 2, x0 + ws[i], ay + ah * 0.66, 0.2, DF.MUTE, '0.8 0.8'))
        x0 += ws[i]
    y = ay + ah * 0.66 + 5
    p2.append(DF._l(ax, y - 3.5, ax + aw, y - 3.5, 0.2, DF.MUTE))
    p2.append(DF._t(ax + 2, y, '床面積と求積方法', 3.0, weight='700'))
    for i, line in enumerate(s['areas']):
        p2.append(DF._t(ax + 2 + (i % 2) * aw * 0.5, y + 4.6 + (i // 2) * 4.2, line, 2.8))
    p2.append(DF.north_mark(ax + aw - 6, ay + ah * 0.66 + 6))
    return DF.svg_wrap(DF.BD_H, p1), DF.svg_wrap(DF.FP_H, p2)


if not getattr(DF.tatemono_solved, '_annex_wrap', False):
    _orig = DF.tatemono_solved

    def _wrap(s):
        return annex_solved(s) if 'annex' in s else _orig(s)
    _wrap._annex_wrap = True
    DF.tatemono_solved = _wrap

SPEC = {
 'site': [list(c) for c in site], 'bld1': [list(c) for c in b1], 'bld2': [list(c) for c in M2], 'annex': [list(c) for c in gg],
 'dists': [[list(a), list(b), t] for a, b, t in DISTS],
 'marks': [['主である建物', [512.9, 306.6], 3.0], ['符号1', [509.6, 318.42], 3.0]],
 'addr': ADDR, 'lot': LOT, 'house': '',
 'adj': [['市道', [521.6, 311.0]], ['6番', [511.0, 297.6]], ['8番', [511.0, 324.4]], ['12番', [500.4, 311.0]]],
 'lot_xy': [504.4, 307.0],
 'areas': [f'主である建物　1階：10.01×7.28−2.73×1.82＝{area(b1):.4f}→{F1:.2f}㎡',
           f'符号1（附属建物）：3.65×5.95＝{area(gg):.4f}→{F3:.2f}㎡',
           f'主である建物　2階：{EW2:.2f}×{NS2:.2f}＝{EW2 * NS2:.4f}→{F2:.2f}㎡',
           '（寸法は壁の中心線間。単位 m）'],
}
assert SPEC['areas'][0].endswith('67.90㎡') and SPEC['areas'][2].endswith('39.74㎡')

DRAW = {
 'draw': 'tatemono', 'minutes': 20,
 'title': '建物図面（500分の1）・各階平面図（250分の1）：主である建物と附属建物（符号1）',
 'text': {
  'lead': '第1部・第2部の事案について、建物表題登記の申請書に添付する建物図面及び各階平面図を、答案用紙（実物と同じ大きさ）に作成しなさい。あわせて、解答欄に、図面に書く床面積・距離と建物の所在を答えなさい。第1部の【測量成果】の座標値・寸法を使う。',
  'conditions': [
   '本件土地・主である建物の1階・車庫の外形は、第1部の【測量成果】の座標値のとおりである（壁の中心線の交点）。主である建物の2階は、壁の中心線で東西7.28メートル・南北5.46メートルの長方形（第1部で外面の寸法から直したもの）で、北の壁・西の壁が1階の北の壁・西の壁の真上にある。',
   '図面の建物の形状は壁の中心線で描き、建物の位置を示す距離は、第1部の注3のとおり、筆界から外壁の面までの距離を書く（主である建物は北側・西側、車庫は東側・南側）。',
   '車庫は、主である建物の附属建物として、符号1を付して登記を申請する（第2部）。本件土地の物置は建物ではないので、図面に描かない。',
  ],
  'hearing': [
   '田中浩二の話：「2階のベランダや玄関ポーチも、図面に描いてほしい。」',
  ],
  'notes': [
   '建物図面は不動産登記規則第82条により縮尺500分の1（1メートルが2ミリメートル）、各階平面図は同規則第83条により縮尺250分の1（1メートルが4ミリメートル）で作成する（図の上を北とする）。',
   '答案用紙の「作成者」「申請人」の欄は（略）と印刷されており、記入を要しない。家屋番号の欄は、建物表題登記の申請なので記入を要しない。',
   '建物図面には、方位、縮尺、敷地の地番と形状、隣接地の地番、主である建物と附属建物の1階の位置及び形状、主である建物又は附属建物の別と附属建物の符号、建物の位置を示す距離を書く。各階平面図には、各階の別、各階の平面の形状、1階の位置（2階の図に点線で）、各階の周囲の長さ、床面積と求積方法、主である建物又は附属建物の別と附属建物の符号を書く。',
  ],
 },
 'tables': [
  {'title': '第1部の測量成果（壁の中心線の交点。X北・Y東）', 'cols': ['点', 'X（北）', 'Y（東）', '点', 'X（北）', 'Y（東）'],
   'rows': [[a, f'{SITE[a][0]:.2f}', f'{SITE[a][1]:.2f}', mk, f'{M[mk][0]:.2f}', f'{M[mk][1]:.2f}'] for a, mk in zip('ABCD', ('m1', 'm2', 'm3', 'm4'))]
          + [['m5', f'{M["m5"][0]:.2f}', f'{M["m5"][1]:.2f}', 'g1', f'{G["g1"][0]:.2f}', f'{G["g1"][1]:.2f}'],
             ['m6', f'{M["m6"][0]:.2f}', f'{M["m6"][1]:.2f}', 'g2', f'{G["g2"][0]:.2f}', f'{G["g2"][1]:.2f}'],
             ['', '', '', 'g3', f'{G["g3"][0]:.2f}', f'{G["g3"][1]:.2f}'],
             ['', '', '', 'g4', f'{G["g4"][0]:.2f}', f'{G["g4"][1]:.2f}']]},
 ],
 'answers': [
  {'label': '主である建物の1階の床面積（㎡）', 'kind': 'area', 'value': f'{F1:.2f}'},
  {'label': '附属建物（符号1）の床面積（㎡）', 'kind': 'area', 'value': f'{F3:.2f}'},
  {'label': '建物図面：北側の筆界から主である建物の外壁まで（m）', 'kind': 'len', 'value': f'{DN:.2f}'},
  {'label': '建物図面：西側の筆界から主である建物の外壁まで（m）', 'kind': 'len', 'value': f'{DW:.2f}'},
  {'label': '建物図面：東側の筆界から附属建物の外壁まで（m）', 'kind': 'len', 'value': f'{DE:.2f}'},
  {'label': '建物図面：南側の筆界から附属建物の外壁まで（m）', 'kind': 'len', 'value': f'{DS:.2f}'},
  {'label': '建物の所在', 'kind': 'text', 'value': LOC},
 ],
 'spec': SPEC,
 'rubric': [
  ['【建物図面】縮尺500分の1（1m＝2mm）で、本件土地の形状（東西22.00m×南北18.00m＝44mm×36mm）を描いた', '規則第82条第2項・第3項'],
  ['敷地の地番（7番）、隣接地の地番（6番・8番・12番）と市道、方位（北）を書いた', '規則第82条第2項'],
  ['主である建物の1階（北東の欠けのある6角形）と附属建物（車庫）の位置・形状を描いた（2階・ベランダ・ポーチ・物置は描かない）', '規則第82条第1項'],
  ['「主である建物」の別と、附属建物の符号「符号1」を書いた', '規則第82条第2項'],
  ['建物の位置を示す距離（北3.52・西2.22・東1.70・南4.00）を、外壁の面までの距離で書いた（中心線までの3.60・2.30・1.75・4.05、フェンスからの3.70は誤り）', '第1部の注3'],
  ['【各階平面図】縮尺250分の1（1m＝4mm）で、主である建物の1階・2階と附属建物の各階の別と平面の形状を描いた', '規則第83条第1項・第2項'],
  ['主である建物の2階の図に、1階の位置を点線で示した', '規則第83条第1項'],
  ['各階の周囲の長さ（各辺の長さ）を書いた：主の1階6辺・2階4辺、車庫4辺', '規則第83条第1項'],
  ['各階の床面積（67.90・39.74・21.71）と求積方法を書いた', '規則第83条第1項'],
  ['各階平面図にも「主である建物」の別と「符号1」を書いた', '規則第83条第1項'],
 ],
 'steps': [
  '建物図面：1/500で敷地（A〜D）を描き、座標から主である建物の1階（m1〜m6）と車庫（g1〜g4）を置く。距離は筆界から外壁の面まで（中心線から0.08・0.05外）。',
  '主である建物・符号1の別を図の中に書く。所在は、建物がすべて7番の中にある（m・g の座標が A〜D の範囲の内側）ので7番地。',
  '各階平面図：1/250で主の1階・2階と車庫を別々に描き、各辺の長さ、2階の図には1階を点線で。床面積と求積方法は第1部の式を写す。',
 ],
 'trap': '建物図面は1階だけで、附属建物も必ず描き、主である建物又は附属建物の別と符号を書く（規則第82条第2項）。各階平面図にも符号を書く（規則第83条第1項）。距離は外壁の面まで。ベランダ・ポーチは床面積に入らず、物置は建物でないので描かない。',
 'keys': [{'title': '距離（普通の四則計算）', 'steps': [
  {'title': '北側の筆界から主である建物の外壁まで', 'formula': f'{SITE["A"][0]:.2f} − {m1[0]:.2f} − 0.08', 'keys': f'{SITE["A"][0]:g} [−] {m1[0]:g} [−] 0.08 [=]', 'display': f'{DN:g}'},
  {'title': '西側の筆界から主である建物の外壁まで', 'formula': f'{m1[1]:.2f} − 0.08 − {SITE["A"][1]:.2f}', 'keys': f'{m1[1]:g} [−] 0.08 [−] {SITE["A"][1]:g} [=]', 'display': f'{DW:g}'},
  {'title': '東側の筆界から附属建物の外壁まで', 'formula': f'{SITE["B"][1]:.2f} − {g2[1]:.2f} − 0.05', 'keys': f'{SITE["B"][1]:g} [−] {g2[1]:g} [−] 0.05 [=]', 'display': f'{DE:g}'},
  {'title': '南側の筆界から附属建物の外壁まで', 'formula': f'{g4[0]:.2f} − 0.05 − {SITE["D"][0]:.2f}', 'keys': f'{g4[0]:g} [−] 0.05 [−] {SITE["D"][0]:g} [=]', 'display': f'{DS:g}'},
 ]}],
}
