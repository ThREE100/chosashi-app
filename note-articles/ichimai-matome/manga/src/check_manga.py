"""一枚まとめの学習まんがの機械チェック（NG 0件にする）。
共通（名前・役割名・個人の結果の語・文字数・話し手の連続・既存作品の名前）に加えて、シートとの照合：
 1. 漫画の「第N条」が、シートの根拠（basis・articles）に挙がった条だけ
 2. シートの結論・間違えやすい点の太字の語が、漫画のどこかに出てくる（落としていない）
 3. 漫画の数（3桁以上・小数）がシートの中にある
 4. 生成物が台本から作り直したものと同じ（手で直していない）"""
import os
import re
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import MANGA, sheet, scripts, bold, sheet_text  # noqa: E402
import build_manga as BLD  # noqa: E402
from manga_check import common, all_texts, numbers_from, articles_in  # noqa: E402

ng = []
for M in scripts():
    cid = M['id']
    S = sheet(cid)
    md = open(os.path.join(MANGA, f"{cid}_manga.md"), encoding='utf-8').read()
    pr = open(os.path.join(MANGA, f"{cid}_prompts.md"), encoding='utf-8').read()
    ng += common(cid, M['pages'], md, pr)
    allowed = set(re.findall(r'第(\d+(?:の\d+)?)条', ' '.join(S['basis']) + S['articles']))
    for a, b in re.findall(r'第(\d+)条〜第(\d+)条', ' '.join(S['basis']) + S['articles']):
        allowed |= {str(i) for i in range(int(a), int(b) + 1)}
    ng += [f"{cid}: {x}" for x in articles_in(M['pages'], allowed, '（シートの basis・articles）')]
    txt = '\n'.join(all_texts(M['pages']))
    for w in bold(S['conclusion'] + S['traps']):
        if w not in txt:
            ng.append(f"{cid}: シートの太字の語「{w}」が漫画にない")
    ng += [f"{cid}: {x}" for x in numbers_from(M['pages'], sheet_text(S))]
    # 生成物が最新か
    import io
    import contextlib
    before = {f: open(os.path.join(MANGA, f), encoding='utf-8').read() for f in (f"{cid}_manga.md", f"{cid}_prompts.md", f"{cid}-codex-instructions.md", f"{cid}-chatgpt-github-instructions.md")}
    with contextlib.redirect_stdout(io.StringIO()):
        new = BLD.build(M)
    for f, v in new.items():
        if before.get(f) != v:
            ng.append(f"{cid}: {f} が台本から作り直したものと違った（build_manga.py を流して作り直した）")
print('NG', len(ng))
print('\n'.join(ng))
sys.exit(1 if ng else 0)
