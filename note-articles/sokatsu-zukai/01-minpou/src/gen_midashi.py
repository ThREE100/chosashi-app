#!/usr/bin/env python3
"""総合記事（民法編）の見出し画像プロンプトを作る。4コマの見出し画像の生成器 gen_prompts.header_prompt を使い、
サブタイトルだけこの記事用に差し替える（数字のない文言なので、数字の許可の一文も直す）。
使い方: python3 note-articles/sokatsu-zukai/01-minpou/src/gen_midashi.py"""
import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "tools/drill/manga"))
import gen_prompts as g

H1, H2, HKEY = "何度も間違える民法の肢", "間違い方に型はある？", "型はある？"
SUB = "直前期の苦手論点つぶし　民法編"
sp = dict(header=dict(h1=H1, h2=H2, hkey=HKEY,
                      scene_l="a stack of blank civil-law textbooks with a small gavel, and a flat house icon beside them",
                      scene_r="an open blank notebook with a magnifying glass and a pencil, and a few blank sticky notes"))
g.header_texts = lambda s: (H1, H2, SUB)
body = g.header_prompt(sp)
a = "and the Arabic numeral 4; the only Latin letters and digits allowed are those in the subtitle exactly as written below."
assert a in body
body = body.replace(a, "and no Arabic numerals or Latin letters at all; the only text is the three lines given below.")
out = f"""# 民法編・総合記事　見出し画像プロンプト（note見出し画像・1280×670px）

総合記事「直前期の苦手論点つぶし総合記事①民法編」（`note-articles/column/sokatsu-01-minpou.md`）の見出し画像です。4コマ解説図解の見出し画像のプロンプト（`tools/drill/manga/gen_prompts.py` の `header_prompt`、mainブランチ）と同じ構成・同じ配色（水彩の空）で作りました。サブタイトルは、この総合記事用の文言です。画像は生成していません。

ChatGPTに、キャラクターの参照画像（トリ先生と藍子の基準画像。`CHATGPT_MANGA_WORKFLOW.md` §3の6枚）を添付し、どちらがトリ先生でどちらが藍子かを一言添えて、下のコードブロックを貼ります。

## 見出し画像の文言（正本）

- タイトル1行目：{H1}（薄い黄色のマーカー）
- タイトル2行目：{H2}（「{HKEY}」を赤みのあるオレンジ）
- サブタイトル：{SUB}

1行目・2行目は、結論を書かず、問いかけにしています（1行16字以内）。

## 見出し画像プロンプト本体

```text
{body}
```

## 保存名

- 見出し画像（採用版）：`総合記事1_民法編_見出し.png`
- 途中の版・不採用の版：`総合記事1_民法編_見出し_v01.png`

## 見出し画像の検品

- [ ] 画像内の文字は、タイトル2行とサブタイトルだけ。文言が上の正本と一字一句一致、簡体字・余計な文字なし（数字・英字もなし）
- [ ] トリ先生が左下、藍子が右下で向き合い、顔がタイトルに重ならない。藍子の髪型が参照画像どおり
- [ ] 左右のテーマの場面に文字がなく、タイトル・キャラより目立たない
- [ ] 背景が不透明（透過・チェッカーボードなし）、中央でトリミングしても主要要素が切れない
"""
(ROOT / "note-articles/sokatsu-zukai/01-minpou/prompt_midashi_sokatsu-01-minpou.md").write_text(out, encoding="utf8")
print("written", len(out))
