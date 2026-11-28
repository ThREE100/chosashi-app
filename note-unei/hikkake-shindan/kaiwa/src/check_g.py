"""学習まんが版の機械チェック。"""
import glob, importlib, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import bank, TYPES
from gakushu import build, art_labels, LEGEND
from claims import CLAIM
B = bank(); ng = []
import re
def nendo_label(it):
    m = re.match(r'([HR])(\d+)-Q(\d+)', it['q']); y = int(m.group(2))
    return f"{'平成' if m.group(1)=='H' else '令和'}{'元' if (m.group(1)=='R' and y==1) else y}年度 第{int(m.group(3))}問"
MARKS = '○×✓✔'
MARK_ART = ['stamp', 'check', 'tick', 'red cross', 'big cross', 'cross mark', 'circle mark', 'crossed-out', 'crossed out', 'red x', 'seal', 'red stop mark']
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
            allow = '｜'.join(pa.get('words', []) + ([pa['narration']] if pa.get('narration') else []))
            for run in art_labels(pa['art']):
                if run not in allow: ng.append(f"{tag}: {k}p-{j}の絵の指示に、文字の指定にない語：{run}")
            sps = [s for s, _ in pa.get('talk', [])]
            if any(a == b for a, b in zip(sps, sps[1:])): ng.append(f"{tag}: {k}p-{j}で同じ話し手が続く")
        n = sum(len(t) for pa in p['panels'] for t in ([t for _, t in pa.get('talk', [])] + pa.get('words', []) + ([pa['narration']] if pa.get('narration') else [])))
        if n > 220: ng.append(f"{tag}: {k}ページ目の文字が{n}字（220字まで）")
    if it['id'] not in CLAIM: ng.append(f"{tag}: claims.py に肢の記述がない")
    last = it['pages'][-1]['panels'][0].get('words', [])
    mark = '○' if truth else '×'
    if LEGEND not in last: ng.append(f"{tag}: まとめに凡例がない")
    if f"{mark}　{CLAIM.get(it['id'], '')}" not in last: ng.append(f"{tag}: まとめの○×がバンクと違う、または肢の記述の横にない")
    if ('正しくは' if not truth else 'ポイント') not in last: ng.append(f"{tag}: まとめの見出し（正しくは／ポイント）が違う")
    if sum(w.count('○') + w.count('×') for w in last) - LEGEND.count('○') - LEGEND.count('×') != 1: ng.append(f"{tag}: まとめの○×が1つでない")
    if not any(w == 'ひっかけの型：' + TYPES[it['type']].split('（')[0] for w in last): ng.append(f"{tag}: まとめの型が type と違う")
    blocks = re.split(r'^## (?=\d+ページ目)', pr, flags=re.M)[1:]
    n = len(it['pages'])
    if len(blocks) != n: ng.append(f"{tag}: プロンプトのページ数が違う")
    for k, (p, b) in enumerate(zip(it['pages'], blocks), 1):
        texts = [p['caption']] + [t for pa in p['panels'] for t in ([t for _, t in pa.get('talk', [])] + pa.get('words', []) + ([pa['narration']] if pa.get('narration') else []))]
        if k < n:
            for t in texts:
                if any(c in t for c in MARKS): ng.append(f"{tag}: {k}ページ目に○×の文字：{t}")
            for pa in p['panels']:
                low = pa['art'].lower()
                for w in MARK_ART:
                    if re.search(r'\b' + re.escape(w), low): ng.append(f"{tag}: {k}ページ目の絵に印の指示「{w}」")
            if 'NO JUDGEMENT MARKS' not in b: ng.append(f"{tag}: {k}ページ目のプロンプトに NO JUDGEMENT MARKS がない")
        elif 'NO JUDGEMENT MARKS' in b: ng.append(f"{tag}: 最後のページに NO JUDGEMENT MARKS がある")
    if not it['basis'].endswith('の結論に従う。') or nendo_label(it) not in it['basis']: ng.append(f"{tag}: 根拠に年度別記事の年度・問がない")
    if 'Doraemon' in pr or 'ドラえもん' in pr: ng.append(f"{tag}: 既存作品の名前がプロンプトにある")
print("NG", len(ng)); print("\n".join(ng)); sys.exit(1 if ng else 0)
