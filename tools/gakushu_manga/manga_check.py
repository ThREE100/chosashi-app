"""学習まんがの台本の共通の機械チェック。各仕組みの check.py が呼び、元データとの照合（正誤・条文・数値）は各仕組みで足す。
返り値は NG の文のリスト。"""
import os
import re
from manga_core import texts_of, figs_of, W, H

NAMES = ['トリ', '藍子', '先生', '生徒', 'アイコ']
PERSONAL = ['回目', '間違えた回数', '誤答回数', '演習結果', '正答率', 'わたしが', '私が', '解いた結果']
WORKS = ['Doraemon', 'ドラえもん', 'Conan', 'コナン', 'Pokemon', 'ポケモン']
LIM_BUBBLE, LIM_NARR, LIM_PAGE = 30, 28, 220
ART = re.compile(r'第[0-9]+条(?:の[0-9]+)?')


def all_texts(pages):
    return [t for pg in pages for p in pg['panels'] for t in texts_of(p)]


def common(tag, pages, md=None, prompts=None, fig_dir=None):
    ng = []
    if not 4 <= len(pages) <= 14:
        ng.append(f"{tag}: ページ数が{len(pages)}（4〜14にする）")
    for k, pg in enumerate(pages, 1):
        for key in ('caption', 'aim', 'layout', 'panels'):
            if not pg.get(key):
                ng.append(f"{tag}: {k}ページ目に {key} がない")
        for j, p in enumerate(pg['panels'], 1):
            for t in texts_of(p):
                if any(w in t for w in NAMES):
                    ng.append(f"{tag}: {k}p-{j}に名前・役割名：{t}")
                if any(w in t for w in PERSONAL):
                    ng.append(f"{tag}: {k}p-{j}に個人の結果の語：{t}")
            for sp, t in p.get('talk', []):
                if sp not in ('S', 'T'):
                    ng.append(f"{tag}: {k}p-{j}の話し手が S/T でない")
                if len(t) > LIM_BUBBLE:
                    ng.append(f"{tag}: {k}p-{j}の吹き出しが{LIM_BUBBLE}字超（{len(t)}字）：{t}")
            if p.get('narration') and len(p['narration']) > LIM_NARR:
                ng.append(f"{tag}: {k}p-{j}のナレーションが{LIM_NARR}字超：{p['narration']}")
            sps = [s for s, _ in p.get('talk', [])]
            if any(a == b for a, b in zip(sps, sps[1:])):
                ng.append(f"{tag}: {k}p-{j}で同じ話し手が続く")
            f = p.get('fig')
            if f:
                x, y, w, h = f['rect']
                if x < 0 or y < 0 or x + w > W or y + h > H or w < 300 or h < 200:
                    ng.append(f"{tag}: {k}p-{j}の図の枠がページの外か小さすぎる：{f['rect']}")
                if fig_dir:
                    fp = os.path.join(fig_dir, f['name'] + '.png')
                    if not os.path.exists(fp):
                        ng.append(f"{tag}: 図がない：{fp}")
                    else:
                        from PIL import Image
                        iw, ih = Image.open(fp).size
                        if abs(iw / ih - w / h) > 0.02:
                            ng.append(f"{tag}: 図 {f['name']} の縦横比（{iw}×{ih}）が枠（{w}×{h}）と違う")
        n = sum(len(t) for p in pg['panels'] for t in texts_of(p))
        if n > LIM_PAGE:
            ng.append(f"{tag}: {k}ページ目の文字が{n}字（{LIM_PAGE}字まで）")
    names = [f['name'] for _, _, f in figs_of(pages)]
    if len(names) != len(set(names)):
        ng.append(f"{tag}: 図の名前が重なっている")
    for s in [md or '', prompts or '']:
        for w in WORKS:
            if w in s:
                ng.append(f"{tag}: 既存作品の名前「{w}」")
    if md:
        for w in NAMES + PERSONAL:
            if w in md:
                ng.append(f"{tag}: 記事に「{w}」")
    return ng


def numbers_from(pages, source, allow=()):
    """漫画の文字にある数（3以上の桁・小数・角度）が、元データの文字のどこかにあるか（作った数を描かせない）。"""
    ng = []
    src = source.replace(',', '')
    for t in all_texts(pages):
        for m in re.finditer(r'\d+(?:\.\d+)?', t):
            v = m.group(0)
            if (len(v) >= 3 or '.' in v) and v not in src and v not in allow:
                ng.append(f"数「{v}」が元データにない：{t}")
    return ng


def articles_in(pages, allowed, law_hint=''):
    """漫画の「第N条」が、元データの根拠に挙がった条かどうか。allowed は '39' や '76の2' の集合。"""
    ng = []
    for t in all_texts(pages):
        for m in ART.finditer(t):
            a = m.group(0)[1:].replace('条', '')
            if a not in allowed:
                ng.append(f"条「{m.group(0)}」が元データの根拠にない{law_hint}：{t}")
    return ng
