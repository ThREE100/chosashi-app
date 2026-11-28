"""学習まんが版の機械チェック。"""
import glob, importlib, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import bank, TYPES
from gakushu import build
B = bank(); ng = []
NAMES = ['トリ', '藍子', '先生', '生徒', 'アイコ']
PERSONAL = ['回目', '間違えた回数', '誤答回数', '復習', 'ドリル', '演習結果', 'わたしが', '私が']
for f in sorted(glob.glob(os.path.join(os.path.dirname(__file__), 'g[0-9][0-9].py'))):
    it = importlib.import_module(os.path.basename(f)[:-3]).ITEM; tag = it['id']
    title, md, pr, stem, truth = build(it, B)
    if it['type'] not in TYPES: ng.append(f"{tag}: 型が不明")
    if len(it['catch']) > 25: ng.append(f"{tag}: キャッチが25字超")
    if stem not in md: ng.append(f"{tag}: 肢の文がバンクと違う")
    if ('○（正しい）' if truth else '×（誤り）') not in md: ng.append(f"{tag}: 正誤がバンクと違う")
    for w in NAMES + PERSONAL:
        if w in md: ng.append(f"{tag}: 記事に「{w}」")
    for k, p in enumerate(it['pages'], 1):
        for j, pa in enumerate(p['panels'], 1):
            texts = [t for _, t in pa.get('talk', [])] + pa.get('words', []) + ([pa['narration']] if pa.get('narration') else [])
            for t in texts:
                if any(w in t for w in NAMES): ng.append(f"{tag}: {k}p-{j}に名前・役割名：{t}")
                if any(w in t for w in PERSONAL): ng.append(f"{tag}: {k}p-{j}に個人の結果の語：{t}")
            for sp, t in pa.get('talk', []):
                if len(t) > 30: ng.append(f"{tag}: {k}p-{j}の吹き出しが30字超：{t}")
            if pa.get('narration') and len(pa['narration']) > 28: ng.append(f"{tag}: {k}p-{j}のナレーションが28字超")
            sps = [s for s, _ in pa.get('talk', [])]
            if any(a == b for a, b in zip(sps, sps[1:])): ng.append(f"{tag}: {k}p-{j}で同じ話し手が続く")
        n = sum(len(t) for pa in p['panels'] for t in ([t for _, t in pa.get('talk', [])] + pa.get('words', []) + ([pa['narration']] if pa.get('narration') else [])))
        if n > 220: ng.append(f"{tag}: {k}ページ目の文字が{n}字（220字まで）")
    if 'Doraemon' in pr or 'ドラえもん' in pr: ng.append(f"{tag}: 既存作品の名前がプロンプトにある")
print("NG", len(ng)); print("\n".join(ng)); sys.exit(1 if ng else 0)
