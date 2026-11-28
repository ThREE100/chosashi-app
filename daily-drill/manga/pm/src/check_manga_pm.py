"""毎日ドリル（夜）の学習まんがの機械チェック（NG 0件にする）。
共通のチェックに加えて、問題データ（PM-NN.json）との照合：
 1. 答え（answers）の値が全部、漫画のどこかに出てくる（落としていない）
 2. 漫画の数（3桁以上・小数・角度の数）が問題データの中にある。例外は wrong_values（わざと見せる誤り。答えと同じ数は入れない）と、
    calc（計算の途中の数。calc.py が問題データから計算し直して、漫画の文字と最後の桁まで合うものだけ）
 3. refs（漫画が名指しする【条件】【注】の番号）の文に、その語がある
 4. 問題の図の求める点の座標が答えと同じ（図とデータの食い違いがない）
 5. 図：fig/ の SVG が問題データから作り直したものと同じ、PNG があり枠と縦横比が同じ、URL がリポジトリの中を指す
 6. 生成物が台本から作り直したものと同じ"""
import contextlib
import io
import json
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT, FIG, problem, scripts  # noqa: E402
import build_manga_pm as BLD  # noqa: E402
import figs  # noqa: E402
import calc as CALC  # noqa: E402
from manga_core import figs_of  # noqa: E402
from manga_check import common, all_texts, numbers_from  # noqa: E402

ng = []
for M in scripts():
    tag = f"Day{M['day']:03d}"
    P = problem(M['problem'])
    if P['day'] != M['day']:
        ng.append(f"{tag}: 問題 {M['problem']} の日（{P['day']}）が台本と違う")
    base = f"day{M['day']:03d}-pm-manga"
    md = open(os.path.join(OUT, base + '.md'), encoding='utf-8').read()
    pr = open(os.path.join(OUT, base + '_prompts.md'), encoding='utf-8').read()
    ng += common(tag, M['pages'], md, pr, fig_dir=FIG, max_pages=24)
    txt = '\n'.join(all_texts(M['pages']))
    vals = []
    for a in P['answers']:
        vals += a['value'] if a['kind'] == 'xy' else [a['value']]
    for v in vals:
        if v not in txt:
            ng.append(f"{tag}: 答え「{v}」が漫画にない")
    wrong = M.get('wrong_values', [])
    for v in wrong:
        if v in vals:
            ng.append(f"{tag}: wrong_values に答えと同じ数「{v}」")
    c_ng, c_ok = CALC.check(P, M.get('calc', []))
    ng += [f"{tag}: {x}" for x in c_ng]
    for _, shown in M.get('calc', []):
        if shown not in txt:
            ng.append(f"{tag}: calc の「{shown}」が漫画にない（使わない計算は消す）")
    ng += [f"{tag}: {x}" for x in numbers_from(M['pages'], json.dumps(P, ensure_ascii=False), allow=list(wrong) + sorted(c_ok))]
    for sec, i, w in M.get('refs', []):
        if w not in P['text'][sec][i - 1]:
            ng.append(f"{tag}: 【{sec}】の{i}に「{w}」がない")
    for a in P['answers']:
        if a['kind'] == 'xy':
            nm = a['label'].replace('点', '')
            xy = P['fig']['points'].get(nm, {}).get('xy')
            if xy and [f"{c:.2f}" for c in xy] != a['value']:
                ng.append(f"{tag}: 図の点{nm}の座標 {xy} が答え {a['value']} と違う")
    for k, _, f in figs_of(M['pages']):
        sp = os.path.join(FIG, f['name'] + '.svg')
        if not os.path.exists(sp) or open(sp, encoding='utf-8').read() != figs.make_svg(f, P):
            ng.append(f"{tag}: 図 {f['name']}.svg が問題データから作り直したものと違う（build_manga_pm.py を流す）")
        if f['name'] + '.png' not in pr or 'raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/' + f['name'] + '.png' not in pr:
            ng.append(f"{tag}: プロンプトに図 {f['name']} のファイル名・URLがない")
    before = {f: open(os.path.join(OUT, f), encoding='utf-8').read() for f in (base + '.md', base + '_prompts.md', base + '-codex-instructions.md', base + '-chatgpt-github-instructions.md')}
    with contextlib.redirect_stdout(io.StringIO()):
        new = BLD.build(M, with_fig=False)
    for f, v in new.items():
        if before.get(f) != v:
            ng.append(f"{tag}: {f} が台本から作り直したものと違った（build_manga_pm.py を流して作り直した）")
print('NG', len(ng))
print('\n'.join(ng))
sys.exit(1 if ng else 0)
