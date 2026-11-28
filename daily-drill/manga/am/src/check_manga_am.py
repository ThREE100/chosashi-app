"""毎日ドリル（朝）の学習まんがの機械チェック（NG 0件にする）。
共通のチェックに加えて、問題データ（AM-NNN.json）との照合：
 1. まとめの板の「ア ○ …」の○×が、各肢の truth と同じ。5肢すべてがある
 2. まとめの見出しの「選択肢N（…）」が、mode と choices から出した正解と同じ
 3. コマの中で肢の記号と○×を並べたとき（words に記号1つ・○×1つ）、truth と同じ
 4. 漫画の「第N条」が、問題の根拠（basis の article・note）に挙がった条だけ
 5. 漫画の数（3桁以上・小数）が問題データの中にある
 6. 生成物が台本から作り直したものと同じ
 7. 最後のページのほかには○×を出さない（文字にも、絵の指示にも。プロンプトに NO JUDGEMENT MARKS）。最後のページに問いの向きと凡例がある（2026-11-28 ユーザー指示）"""
import contextlib
import io
import json
import os
import re
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT, problem, scripts, answer, ASK  # noqa: E402
import build_manga_am as BLD  # noqa: E402
from manga_check import common, numbers_from, articles_in  # noqa: E402
from manga_core import texts_of  # noqa: E402

MARK_ART = ['stamp', 'check', 'red cross', 'big cross', 'circle mark', '○', '×', '✓', '✔']

ng = []
for M in scripts():
    tag = f"Day{M['day']:03d}"
    P = problem(M['problem'])
    if P['day'] != M['day']:
        ng.append(f"{tag}: 問題 {M['problem']} の日（{P['day']}）が台本と違う")
    base = f"day{M['day']:03d}-am-manga"
    md = open(os.path.join(OUT, base + '.md'), encoding='utf-8').read()
    pr = open(os.path.join(OUT, base + '_prompts.md'), encoding='utf-8').read()
    ng += common(tag, M['pages'], md, pr)
    truth = {s['label']: ('○' if s['truth'] else '×') for s in P['statements']}
    last = M['pages'][-1]['panels'][0]['words']
    seen = {}
    for w in last:
        m = re.match(r'([アイウエオ]) ([○×])', w)
        if m:
            seen[m.group(1)] = m.group(2)
    for lb, mk in truth.items():
        if seen.get(lb) != mk:
            ng.append(f"{tag}: まとめの{lb}が「{seen.get(lb)}」（データは{mk}）")
    n, pick = answer(P)
    if last[0] != f"答え：選択肢{n}（{'・'.join(pick)}）":
        ng.append(f"{tag}: まとめの答え「{last[0]}」がデータの正解（選択肢{n}・{'・'.join(pick)}）と違う")
    if last[1] != ASK[P['mode']] or not last[2].startswith('○＝'):
        ng.append(f"{tag}: まとめに問いの向き「{ASK[P['mode']]}」と凡例がない（common.kotae で作る）")
    for k, pg in enumerate(M['pages'][:-1], 1):
        for j, p in enumerate(pg['panels'], 1):
            for t in texts_of(p):
                if any(c in t for c in '○×✓✔'):
                    ng.append(f"{tag}: {k}p-{j}の文字「{t}」に○×がある（○×は最後のページだけ）")
            low = p['art'].lower()
            for w in MARK_ART:
                if w in low:
                    ng.append(f"{tag}: {k}p-{j}の絵の指示に正誤の印「{w}」がある（最後のページだけ）")
    for k in range(1, len(M['pages'])):
        m = re.search(rf'\n## {k}ページ目.*?(?=\n## \d+ページ目|\n## 見出し画像|\Z)', pr, re.S)
        b = m.group(0) if m else ''
        if 'NO JUDGEMENT MARKS' not in b:
            ng.append(f"{tag}: {k}ページ目のプロンプトに NO JUDGEMENT MARKS がない")
    for k, pg in enumerate(M['pages'], 1):
        for j, p in enumerate(pg['panels'], 1):
            ws = p.get('words', [])
            lbs = [w for w in ws if w in truth]
            mks = [w for w in ws if w in ('○', '×')]
            if len(lbs) == 1 and len(mks) == 1 and truth[lbs[0]] != mks[0]:
                ng.append(f"{tag}: {k}p-{j}の{lbs[0]}が{mks[0]}（データは{truth[lbs[0]]}）")
    src = json.dumps(P, ensure_ascii=False)
    allowed = set(re.findall(r'第(\d+(?:の\d+)?)条', src))
    ng += [f"{tag}: {x}" for x in articles_in(M['pages'], allowed, '（問題データの根拠）')]
    ng += [f"{tag}: {x}" for x in numbers_from(M['pages'], src)]
    before = {f: open(os.path.join(OUT, f), encoding='utf-8').read() for f in (base + '.md', base + '_prompts.md', base + '-codex-instructions.md', base + '-chatgpt-github-instructions.md')}
    with contextlib.redirect_stdout(io.StringIO()):
        new = BLD.build(M)
    for f, v in new.items():
        if before.get(f) != v:
            ng.append(f"{tag}: {f} が台本から作り直したものと違った（build_manga_am.py を流して作り直した）")
print('NG', len(ng))
print('\n'.join(ng))
sys.exit(1 if ng else 0)
