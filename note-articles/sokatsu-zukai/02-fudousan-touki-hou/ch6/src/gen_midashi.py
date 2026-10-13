#!/usr/bin/env python3
"""総合記事②不動産登記法編 第6章：note見出し画像（1280×670px）のプロンプトを組み立てる。
4コマ解説図解の見出し画像のプロンプト（tools/drill/manga/gen_prompts.py の header_prompt）と同じ構成・同じ配色（水彩の空）。
使い方: python3 note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch6/src/gen_midashi.py   → ../prompt_midashi_sokatsu02_ch6.md"""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "tools" / "drill" / "manga"))
import gen_prompts

H1, H2, HKEY = "合併も、分割も、分棟も", "どこまでできる？", "できる？"
SUB = "苦手論点つぶし　不動産登記法編⑥　建物の分割・分棟・合併"
SP = dict(id="sokatsu02ch6", src="", header=dict(h1=H1, h2=H2, hkey=HKEY,
          scene_l="a long building icon with its middle section removed and a smaller annex being pulled apart from the main building, no text",
          scene_r="two small building icons merging into one next to a blank application sheet and a rubber stamp, no text"))
gen_prompts.header_texts = lambda sp: (H1, H2, SUB)

def main():
    prompt = gen_prompts.header_prompt(SP)
    old = "and the Arabic numeral 4; the only Latin letters and digits allowed are those in the subtitle exactly as written below."
    assert old in prompt
    prompt = prompt.replace(old, "and the circled numeral ⑥ in the subtitle; no Latin letters and no Arabic digits anywhere in the image.")
    kan = gen_prompts.header_kanji(H1, H2, SUB)
    out = "# 総合記事②不動産登記法編 第6章　見出し画像プロンプト（note見出し画像・1280×670px）\n\n"
    out += ("総合記事②不動産登記法編 第6章「建物の分割・分棟・合併」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch6.md`）の見出し画像です。"
            "4コマ解説図解の見出し画像のプロンプト（`tools/drill/manga/gen_prompts.py` の `header_prompt`）を参照して、同じ構成・同じ配色（水彩の空）で作りました。画像は生成していません。\n\n"
            "ChatGPTに、キャラクターの参照画像（トリ先生と藍子の基準画像。`CHATGPT_MANGA_WORKFLOW.md` §3の6枚）を添付し、どちらがトリ先生でどちらが藍子かを一言添えて、下のコードブロックを貼ります。\n\n")
    out += "## 見出し画像の文言（正本）\n\n"
    out += f"- タイトル1行目：{H1}（薄い黄色のマーカー）\n- タイトル2行目：{H2}（「{HKEY}」を赤みのあるオレンジ）\n- サブタイトル：{SUB}\n\n"
    out += "1行目・2行目は、結論を書かず、問いかけにしています（1行16字以内）。章のテーマ『建物の分割・分棟・合併』から、3つの登記の名前を1行目に並べ、『どこまでできる？（合併できる範囲、まとめて申請できる範囲）』を2行目に使いました。サブタイトルの『⑥』は、総合記事の第6章を表します（丸数字の1字だけです）。\n\n"
    out += "## 見出し画像プロンプト本体\n\n```text\n" + prompt + "\n```\n\n"
    out += "## 保存名\n\n- 見出し画像（採用版）：`不登法編6章_見出し.png`\n- 途中の版・不採用の版：`不登法編6章_見出し_v01.png`\n\n"
    out += ("## 見出し画像の検品\n\n- [ ] 画像内の文字は、タイトル2行とサブタイトルだけ。文言が上の正本と一字一句一致、簡体字・余計な文字なし（サブタイトルの『⑥』が丸数字のまま描かれている）\n"
            "- [ ] トリ先生が左下、藍子が右下で向き合い、顔がタイトルに重ならない。藍子の髪型が参照画像どおり\n"
            "- [ ] 左右のテーマの場面に文字がなく、タイトル・キャラより目立たない\n"
            "- [ ] 背景が不透明（透過・チェッカーボードなし）、中央でトリミングしても主要要素が切れない\n")
    (HERE.parent / "prompt_midashi_sokatsu02_ch6.md").write_text(out, encoding="utf8")
    print("kanji:", "".join(kan)); print(len(out))

main()
