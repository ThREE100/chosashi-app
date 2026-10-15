# 民法編・総合記事（第2章 物権）　見出し画像プロンプト（note見出し画像・1280×670px）

総合記事「直前期の苦手論点つぶし総合記事①民法編（2/3）」（`note-articles/column/sokatsu-01-minpou-ch2.md`。物権（共有・占有・物権的請求権・通行権））の見出し画像です。4コマ解説図解の見出し画像のプロンプト（`tools/drill/manga/gen_prompts.py` の `header_prompt`、mainブランチ）と同じ構成・同じ配色（水彩の空）で作りました。サブタイトルは、この章用の文言です。画像は生成していません。

ChatGPTに、キャラクターの参照画像（トリ先生と藍子の基準画像。`CHATGPT_MANGA_WORKFLOW.md` §3の6枚）を添付し、どちらがトリ先生でどちらが藍子かを一言添えて、下のコードブロックを貼ります。

## 見出し画像の文言（正本）

- タイトル1行目：共有・占有・通行権の肢（薄い黄色のマーカー）
- タイトル2行目：単独で何ができる？（「何ができる？」を赤みのあるオレンジ）
- サブタイトル：苦手論点つぶし　民法編　物権

1行目・2行目は、結論を書かず、問いかけにしています（1行16字以内）。全体版・ほかの章の見出し画像（`prompt_midashi_sokatsu-01-minpou.md` と、`prompt_midashi_sokatsu-01-minpou-ch1〜3.md`）とは、タイトルの文言とテーマの場面を変えて、並べても区別できるようにしてあります。

## 見出し画像プロンプト本体

```text
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the two characters at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): follow the attached character-specification images exactly and do not redesign them. トリ先生 is the chubby bird teacher (round red glasses, blue shirt, red neckerchief), placed at the lower left of center. 藍子 is the young woman exam candidate (long wavy brown hair, pinstriped light-blue blouse with rolled sleeves, navy pencil skirt, no jacket), placed at the lower right of center. POSES ARE NOT FIXED: do not copy any pose from the attached images or from earlier header images; let each character take a free, natural pose of your own choosing that fits the topic and suits the character (for example standing, sitting, leaning, gesturing, or holding a small prop), and choose a different pose each time this image is generated. Keep both characters fully visible, with their faces clear of the title text, and keep 藍子's hairstyle exactly as in the attached images. Keep 藍子's human anatomy strictly correct: exactly one head, one torso, two arms (one left, one right) and two hands in total, each hand with exactly five fingers; never draw extra arms, hands, or fingers, floating or duplicated hands, arms not growing from the shoulders, or fused hands; check that every shoulder, elbow, and wrist connects naturally.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and no Arabic numerals or Latin letters at all; the only text is the three lines given below. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it:
共有・占有・通行権の肢
Line 2 is larger; the phrase 何ができる？ is red-orange and the rest is dark navy:
単独で何ができる？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
苦手論点つぶし　民法編　物権
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a flat house with a garden fence, a plot of land divided into three equal parts by thin lines, and a key
Right side: a narrow path leading through a gate to a road, and a blank land deed with a rubber stamp

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written (cartoon expression marks such as ！ and ？ beside the characters' faces are decoration, are allowed, and are not extra text); scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 共, 有, 占, 通, 行, 権, 肢, 単, 独, 何, 苦, 手, 論, 点, 民, 法, 編, 物; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere. Never delete, redo, or regenerate anything because of an expression mark or a symbol beside a character; deliver the first image as it is.
```

## 保存名

- 見出し画像（採用版）：`総合記事1_民法編_第2章_見出し.png`
- 途中の版・不採用の版：`総合記事1_民法編_第2章_見出し_v01.png`

## 見出し画像の検品

- [ ] 画像内の文字は、タイトル2行とサブタイトルだけ。文言が上の正本と一字一句一致、簡体字・余計な文字なし（数字・英字もなし）
- [ ] トリ先生が左下、藍子が右下で向き合い、顔がタイトルに重ならない。藍子の髪型が参照画像どおり
- [ ] 左右のテーマの場面に文字がなく、タイトル・キャラより目立たない
- [ ] 背景が不透明（透過・チェッカーボードなし）、中央でトリミングしても主要要素が切れない
