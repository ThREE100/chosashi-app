"""第4回以降の header-prompts.md と codex-instructions.md を、第3回のファイルを型にして作る。
型（背景・人物・文字・透明の禁止・最終確認の文）は第3回のまま使い、回ごとに変わる所（タイトル2行・サブタイトル・
注意する漢字・左右の題材・ポーズの案・ファイル名・記事名）だけを header_specs.py の値に差し替える。
使い方：python3 note-unei/hitogara/src/make_headers.py [番号 ...]（省くと header_specs.py の全部）
"""
import os, re, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from header_specs import SPECS
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "03-ikkagetsu-shinsei-gimu"
TPL_H = open(f"{HERE}/{BASE}/header-prompts.md", encoding="utf-8").read()
TPL_C = open(f"{HERE}/{BASE}/codex-instructions.md", encoding="utf-8").read()
OLD_TEXT = re.search(r"Line 1 is dark navy.*?\n起算点と過料を全部並べる\n", TPL_H, re.S).group(0)
OLD_SCENE = re.search(r"Left side: .*?counting\.\n", TPL_H, re.S).group(0)
OLD_KANJI = "申、請、登、記、数、起、算、点、過、料、全、部、並"

def kanji_of(*ss):
    out = []
    for s in ss:
        for ch in s:
            if '一' <= ch <= '鿿' and ch not in out: out.append(ch)
    return "、".join(out)

def build(sp):
    n = sp["no"]; d = sp["dir"]
    hl = sp["line2"].replace(sp["hl"], "", 1) if sp["hl"] else sp["line2"]
    hl_desc = f"Line 2 is larger; the phrase {sp['hl']} is red-orange and the rest is dark navy:" if sp["hl"] else "Line 2 is larger and dark navy:"
    text = (f"Line 1 is dark navy with a pale yellow marker stroke behind it:\n{sp['line1']}\n{hl_desc}\n{sp['line2']}\n"
            f"Below the title, a light blue rounded pill-shaped subtitle band with navy text:\n{sp['sub']}\n")
    scene = f"Left side: {sp['left']}\nRight side: {sp['right']}\nFor her pose this time, a suggestion that fits the topic (not mandatory): {sp['pose']}\n"
    h = TPL_H
    head, rest = h.split("## note用", 1)
    head = (f"# 第{n}回「{sp['title']}」見出し画像プロンプト\n\n"
            "`03-ikkagetsu-shinsei-gimu/header-prompts.md` と同じ型（2026-11-27改定：背景はトリニティ・カレッジ図書館のロングルームを思わせる重厚な歴史的図書館の内装、"
            "背景に胸像・彫像など参照画像の人物以外の人型を一切入れない、人物の腕は左右1本ずつ、参照するキャラクターシートは I-01・I-02・I-03 の3枚）。"
            "`src/make_headers.py` が第3回のプロンプトを型にして、タイトル・サブタイトル・題材・ポーズの案だけを差し替えて作る（手で直さない。直すときは `src/header_specs.py` を直して作り直す）。"
            f"数字は画像に入れない方針なので、タイトルに数は入れず言葉だけにしている。題材の場面：{sp['scene_note']}\n\n"
            "使い方・確かめることは `note-drafts/header-image-prompts.md` と同じ。\n\n")
    body = "## note用" + rest
    body = body.replace(OLD_TEXT, text).replace(OLD_SCENE, scene).replace(OLD_KANJI, kanji_of(sp["line1"], sp["line2"], sp["sub"]))
    body = body.replace("hitogara03_", f"hitogara{n:02d}_")
    assert OLD_TEXT not in body and OLD_SCENE not in body and body.count(f"hitogara{n:02d}_header_") == 2
    open(f"{HERE}/{d}/header-prompts.md", "w", encoding="utf-8").write(head + body)
    c = TPL_C.replace("第3回", f"第{n}回").replace("申請の義務がある登記を全部並べる（「一月以内」と過料）", sp["title"])
    c = c.replace(BASE, d).replace("hitogara03_", f"hitogara{n:02d}_")
    figs = "・".join(f"`{f}`" for f in sp["figs"])
    c = re.sub(r"- 本文の図（.*?）は作成済み", f"- 本文の図（{figs}）は作成済み", c)
    assert "03-ikkagetsu" not in c and "zu01_kisanten" not in c
    open(f"{HERE}/{d}/codex-instructions.md", "w", encoding="utf-8").write(c)

if __name__ == "__main__":
    want = [int(x) for x in sys.argv[1:]]
    for sp in SPECS:
        if want and sp["no"] not in want: continue
        build(sp); print("作成：", sp["dir"])
