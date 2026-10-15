#!/usr/bin/env python3
"""民法編を章ごとに分けた記事（sokatsu-01-minpou-ch1〜3.md）の見出し画像プロンプトを作る。
4コマ解説図解の見出し画像の生成器 gen_prompts.header_prompt を使い、サブタイトルだけ差し替える（数字のない文言）。
使い方: python3 note-articles/sokatsu-zukai/01-minpou/src/gen_midashi_ch.py"""
import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "tools/drill/manga"))
import gen_prompts as g

CH = {
    1: dict(name="総則", full="総則（意思表示・制限行為能力・代理・時効・条件）",
            h1="取消し・代理・時効の肢", h2="善意だけで守られる？", hkey="守られる？",
            sub="苦手論点つぶし　民法編　総則",
            scene_l="a faceless person signing a blank contract sheet with a rubber stamp beside it, and a small hourglass",
            scene_r="a blank calendar page, a balance scale of justice, and a small blank document folder"),
    2: dict(name="物権", full="物権（共有・占有・物権的請求権・通行権）",
            h1="共有・占有・通行権の肢", h2="単独で何ができる？", hkey="何ができる？",
            sub="苦手論点つぶし　民法編　物権",
            scene_l="a flat house with a garden fence, a plot of land divided into three equal parts by thin lines, and a key",
            scene_r="a narrow path leading through a gate to a road, and a blank land deed with a rubber stamp"),
    3: dict(name="対抗要件・担保・相続", full="物権変動・対抗要件、地上権・質権、相続",
            h1="二重売買と相続の肢", h2="登記が要るのは誰に？", hkey="誰に？",
            sub="苦手論点つぶし　民法編　対抗要件・担保・相続",
            scene_l="two faceless buyers on either side of one flat house, and a blank registry ledger with a rubber stamp",
            scene_r="a family tree sketch with blank nodes, a small wooden box, and a house key"),
}
OUT = ROOT / "note-articles/sokatsu-zukai/01-minpou"
a = "and the Arabic numeral 4; the only Latin letters and digits allowed are those in the subtitle exactly as written below."
for k, c in CH.items():
    assert len(c["h1"]) <= 16 and len(c["h2"]) <= 16, c
    sp = dict(header=dict(h1=c["h1"], h2=c["h2"], hkey=c["hkey"], scene_l=c["scene_l"], scene_r=c["scene_r"]))
    g.header_texts = lambda s, c=c: (c["h1"], c["h2"], c["sub"])
    body = g.header_prompt(sp)
    assert a in body
    body = body.replace(a, "and no Arabic numerals or Latin letters at all; the only text is the three lines given below.")
    out = f"""# 民法編・総合記事（第{k}章 {c['name']}）　見出し画像プロンプト（note見出し画像・1280×670px）

総合記事「直前期の苦手論点つぶし総合記事①民法編（{k}/3）」（`note-articles/column/sokatsu-01-minpou-ch{k}.md`。{c['full']}）の見出し画像です。4コマ解説図解の見出し画像のプロンプト（`tools/drill/manga/gen_prompts.py` の `header_prompt`、mainブランチ）と同じ構成・同じ配色（水彩の空）で作りました。サブタイトルは、この章用の文言です。画像は生成していません。

ChatGPTに、キャラクターの参照画像（トリ先生と藍子の基準画像。`CHATGPT_MANGA_WORKFLOW.md` §3の6枚）を添付し、どちらがトリ先生でどちらが藍子かを一言添えて、下のコードブロックを貼ります。

## 見出し画像の文言（正本）

- タイトル1行目：{c['h1']}（薄い黄色のマーカー）
- タイトル2行目：{c['h2']}（「{c['hkey']}」を赤みのあるオレンジ）
- サブタイトル：{c['sub']}

1行目・2行目は、結論を書かず、問いかけにしています（1行16字以内）。全体版・ほかの章の見出し画像（`prompt_midashi_sokatsu-01-minpou.md` と、`prompt_midashi_sokatsu-01-minpou-ch1〜3.md`）とは、タイトルの文言とテーマの場面を変えて、並べても区別できるようにしてあります。

## 見出し画像プロンプト本体

```text
{body}
```

## 保存名

- 見出し画像（採用版）：`総合記事1_民法編_第{k}章_見出し.png`
- 途中の版・不採用の版：`総合記事1_民法編_第{k}章_見出し_v01.png`

## 見出し画像の検品

- [ ] 画像内の文字は、タイトル2行とサブタイトルだけ。文言が上の正本と一字一句一致、簡体字・余計な文字なし（数字・英字もなし）
- [ ] トリ先生が左下、藍子が右下で向き合い、顔がタイトルに重ならない。藍子の髪型が参照画像どおり
- [ ] 左右のテーマの場面に文字がなく、タイトル・キャラより目立たない
- [ ] 背景が不透明（透過・チェッカーボードなし）、中央でトリミングしても主要要素が切れない
"""
    (OUT / f"prompt_midashi_sokatsu-01-minpou-ch{k}.md").write_text(out, encoding="utf8")
    print("written", k, len(out))
