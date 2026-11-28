"""一枚まとめの学習まんが：台本（src/<ID>.py）から、note記事・画像プロンプト・Codex/ChatGPT用の貼り付け文を作る。
使い方：python3 note-articles/ichimai-matome/manga/src/build_manga.py [ID ...]　（生成物は手で直さない）"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import MANGA, REL, sheet, scripts, plain  # noqa: E402
import catalog  # noqa: E402
from catalog import BY_ID, FIELDS  # noqa: E402
from manga_core import prompts_md  # noqa: E402
from manga_instr import instructions  # noqa: E402

KATA = REL + 'KATA.md'


def names(cid):
    return f"一枚まとめ漫画_{cid}"


def article(M, S, c):
    sheet_md = 'note-articles/ichimai-matome/' + catalog.path(c, 'md')
    L = [f"## 【土地家屋調査士試験】一枚まとめ（漫画版）_{c['title']}～{c['catch']}～", '',
         f"**一枚まとめ（漫画版）　{FIELDS[c['field']][0]}　｜　対象条文：{S['articles']}**", '', M['intro'], '', '---', '']
    for k, p in enumerate(M['pages'], 1):
        L += [f"> 【画像挿入】{k}ページ目：{p['caption']}", '']
    L += ['---', '', '### この一枚で言えること（文字で確かめたい人へ）', '']
    L += ['- ' + x for x in S['conclusion']] + ['', '### 間違えやすい点', '']
    L += ['- ' + x for x in S['traps']] + ['', f"根拠：{'、'.join(S['basis'])}", '',
          f"一枚の画像（表と書き方の例つき）は、一枚まとめ「{c['title']}」の記事にあります（`{sheet_md}`）。", '']
    return '\n'.join(L)


def build(M):
    cid = M['id']
    S, c = sheet(cid), BY_ID[cid]
    fp = names(cid)
    pr = prompts_md(f"一枚まとめ（漫画版）{cid}「{c['title']}」の画像プロンプト",
                    [f"記事：`{cid}_manga.md`。元のシート：`note-articles/ichimai-matome/src/sheets/{cid}.py`（中身はシートの範囲だけ）。全{len(M['pages'])}ページ、1ページ＝1枚（1024×1536）。"],
                    M['pages'], fp, M['header'], M['header_scene'])
    cx, gp = instructions(f"一枚まとめ {cid}", f"{REL}{cid}_prompts.md", M['pages'], fp, KATA)
    out = {f"{cid}_manga.md": article(M, S, c), f"{cid}_prompts.md": pr,
           f"{cid}-codex-instructions.md": cx, f"{cid}-chatgpt-github-instructions.md": gp}
    for k, v in out.items():
        open(os.path.join(MANGA, k), 'w', encoding='utf-8').write(v)
    return out


if __name__ == '__main__':
    want = set(sys.argv[1:])
    for M in scripts():
        if not want or M['id'] in want:
            build(M)
            print(M['id'], len(M['pages']), 'ページ')
