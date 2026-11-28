"""機械チェック：名前を出さない・個人の結果を出さない・肢と正誤はバンクのまま・吹き出しの長さ・話し手の並び。"""
import glob, importlib, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import bank, build, OUT, TYPES
B = bank(); ng = []
NAMES = ['トリ', '藍子', '先生', '生徒', 'アイコ']
PERSONAL = ['回目', '間違えた回数', '誤答回数', '誤解', '復習', 'ドリル', '演習結果', 'わたしが', '私が']
for f in sorted(glob.glob(os.path.join(os.path.dirname(__file__), 'd[0-9][0-9].py'))):
    it = importlib.import_module(os.path.basename(f)[:-3]).ITEM; tag = it['id']
    title, md, pr, stem, truth = build(it, B)
    if it['type'] not in TYPES: ng.append(f"{tag}: 型が不明")
    if len(it['catch']) > 25: ng.append(f"{tag}: キャッチが25字超")
    if stem not in md: ng.append(f"{tag}: 肢の文がバンクと違う")
    for w in NAMES:
        if w in md: ng.append(f"{tag}: 記事に名前・役割名「{w}」")
    for w in PERSONAL:
        if w in md: ng.append(f"{tag}: 個人の結果の語「{w}」")
    if len(it['pages']) != 3: ng.append(f"{tag}: 漫画は3ページ")
    for k, p in enumerate(it['pages'], 1):
        if len(p['panels']) != 3: ng.append(f"{tag}: 漫画{k}のコマは3つ")
        for j, pa in enumerate(p['panels'], 1):
            for sp, t in pa['talk']:
                if any(w in t for w in NAMES): ng.append(f"{tag}: 漫画{k}-{j}の吹き出しに名前")
                if len(t) > 36: ng.append(f"{tag}: 漫画{k}-{j}の吹き出しが36字超：{t}")
            sps = [s for s, _ in pa['talk']]
            if any(a == b for a, b in zip(sps, sps[1:])): ng.append(f"{tag}: 漫画{k}-{j}で同じ話し手が続く")
            for w in pa.get('words', []):
                if w not in pa.get('fig', '') and w not in ''.join(t for _, t in pa['talk']):
                    pass
    if ('○（正しい）' if truth else '×（誤り）') not in md: ng.append(f"{tag}: 正誤がバンクと違う")
print("NG", len(ng)); print("\n".join(ng))
sys.exit(1 if ng else 0)
