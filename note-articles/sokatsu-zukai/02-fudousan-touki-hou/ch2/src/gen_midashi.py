#!/usr/bin/env python3
"""総合記事②不動産登記法編 第2章：note見出し画像（1280×670px）のプロンプトを組み立てる。
4コマ解説図解の見出し画像のプロンプト（tools/drill/manga/gen_prompts.py の header_prompt）と同じ構成・同じ配色（水彩の空）。
使い方: python3 note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch2/src/gen_midashi.py   → ../prompt_midashi_sokatsu02_ch2.md"""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "tools" / "drill" / "manga"))
import gen_prompts

H1, H2, HKEY = "添付も、通知も、税金も", "何を・誰に・いくら？", "いくら？"
SUB = "苦手論点つぶし　不動産登記法編②　添付と手続の作法"
SP = dict(id="sokatsu02ch2", src="", header=dict(h1=H1, h2=H2, hkey=HKEY,
          scene_l="a stack of document sheets held by a paper clip, with a small blank certificate and a rubber stamp, no text",
          scene_r="a small key icon beside an archive box and a few coins, no text"))
gen_prompts.header_texts = lambda sp: (H1, H2, SUB)

def main():
    prompt = gen_prompts.header_prompt(SP)
    old = "and the Arabic numeral 4; the only Latin letters and digits allowed are those in the subtitle exactly as written below."
    assert old in prompt
    prompt = prompt.replace(old, "and the circled numeral ② that appears in the subtitle; no Latin letters and no Arabic digits are allowed anywhere in the image.")
    kan = gen_prompts.header_kanji(H1, H2, SUB)
    out = "# 総合記事②不動産登記法編 第2章　見出し画像プロンプト（note見出し画像・1280×670px）\n\n"
    out += ("総合記事②「直前期の苦手論点つぶし 不動産登記法編」第2章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch2.md`）の見出し画像です。"
            "4コマ解説図解の見出し画像のプロンプト（`tools/drill/manga/gen_prompts.py` の `header_prompt`）を参照して、同じ構成・同じ配色（水彩の空）で作りました。画像は生成していません。\n\n"
            "ChatGPTに、キャラクターの参照画像（トリ先生と藍子の基準画像。`CHATGPT_MANGA_WORKFLOW.md` §3の6枚）を添付し、どちらがトリ先生でどちらが藍子かを一言添えて、下のコードブロックを貼ります。\n\n")
    out += "## 見出し画像の文言（正本）\n\n"
    out += f"- タイトル1行目：{H1}（薄い黄色のマーカー）\n- タイトル2行目：{H2}（「{HKEY}」を赤みのあるオレンジ）\n- サブタイトル：{SUB}\n\n"
    out += "1行目・2行目は、結論を書かず、問いかけにしています（1行16字以内）。記事の副題『申請の「付属品」と「手続の作法」を一気に整理』のうち、添付情報（何を）・登記識別情報（誰に）・登録免許税（いくら）の3つを、1行目の「添付も、通知も、税金も」と2行目の問いかけ「何を・誰に・いくら？」にしました。サブタイトルは、シリーズの他の章と区別がつくよう「不動産登記法編②」と章のテーマ「添付と手続の作法」を入れました。\n\n"
    out += "## 見出し画像プロンプト本体\n\n```text\n" + prompt + "\n```\n\n"
    out += "## 保存名\n\n- 見出し画像（採用版）：`不動産登記法編2章_見出し.png`\n- 途中の版・不採用の版：`不動産登記法編2章_見出し_v01.png`\n\n"
    out += ("## 見出し画像の検品\n\n- [ ] 画像内の文字は、タイトル2行とサブタイトルだけ。文言が上の正本と一字一句一致、簡体字・余計な文字なし\n"
            "- [ ] トリ先生が左下、藍子が右下で向き合い、顔がタイトルに重ならない。藍子の髪型が参照画像どおり\n"
            "- [ ] 左右のテーマの場面に文字がなく、タイトル・キャラより目立たない\n"
            "- [ ] 背景が不透明（透過・チェッカーボードなし）、中央でトリミングしても主要要素が切れない\n")
    (HERE.parent / "prompt_midashi_sokatsu02_ch2.md").write_text(out, encoding="utf8")
    print("kanji:", "".join(kan)); print(len(out))

main()
