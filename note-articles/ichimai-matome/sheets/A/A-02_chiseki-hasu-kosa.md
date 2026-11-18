## 【土地家屋調査士試験】A_02_一枚まとめ_地積の端数処理と公差～切り捨てと、精度区分の見分け方～

**一枚まとめ　土地の表示の登記　｜　対象条文：不動産登記規則第10条・第77条・第100条、準則第70条・第72条**

> 【画像挿入】A-02_chiseki-hasu-kosa.png　（この一枚の画像。保存しておけば、通信なしで見返せます）

### この一枚で言えること

- 地積は**切り捨て**。四捨五入はしない。宅地と鉱泉地は0.01㎡未満、それ以外で10㎡を超える土地は**1㎡未満**を切り捨てる（規則第100条）。
- 公差（誤差の限度）の精度区分は、**地目ではなく地域**で決まる。市街地地域は甲二、村落・農耕地域は乙一、山林・原野地域は乙三まで。
- 分筆の前後の地積の差は、**分筆前の地積を基準**にした誤差の限度と比べる（準則第72条第1項）。

### 端数の切り捨て（規則第100条）

| 土地 | 切り捨てる端数 | 表し方 |
|---|---|---|
| 宅地・鉱泉地 | 0.01㎡未満 | 小数第2位まで |
| それ以外で10㎡を超える | 1㎡未満 | 整数 |
| それ以外で10㎡以下 | 0.01㎡未満 | 小数第2位まで |

### 精度区分の見分け方（規則第10条第4項、第77条第5項で準用）

| 地域 | 中身 | 誤差の限度 |
|---|---|---|
| 市街地地域 | 主に宅地が占める地域とその周辺 | 精度区分甲二まで |
| 村落・農耕地域 | 主に田・畑・塩田が占める地域とその周辺 | 精度区分乙一まで |
| 山林・原野地域 | 主に山林・牧場・原野が占める地域とその周辺 | 精度区分乙三まで |

地域の中身は規則第10条第2項。精度区分そのもの（公差の式）は国土調査法施行令別表第四に定めがある。

### 計算例：端数の切り捨てと、分筆前後の差

- 宅地 253.60735㎡ → **253.60㎡**（0.01未満を切り捨て。四捨五入なら253.61で誤り）
- 雑種地 244.789㎡ → **244㎡**（10㎡を超えるので1未満を切り捨て）
- 雑種地 9.876㎡ → **9.87㎡**（10㎡以下なので0.01未満を切り捨て）
- 畑 10.995㎡ → **10㎡**（10㎡を超える）
- 分筆前 300.00㎡、分筆後 146.62＋153.22＝299.84㎡ → 差 0.16㎡。これを分筆前の300.00㎡を基準にした誤差の限度と比べる。

### 間違えやすい点

1. 宅地でも、村落・農耕地域にあれば**乙一**。地目につられて甲二にしない。
2. 雑種地・畑などは、10㎡を超えれば**整数**。10㎡以下なら小数第2位まで残る。
3. 比べるのは分筆前の地積と**分筆後の地積（切り捨て後）の合計**。基準は分筆後ではなく分筆前の地積。

### 根拠とくわしい記事

- 根拠：不動産登記規則第10条第2項・第4項、第77条第5項、第100条、準則第70条・第72条第1項
- くわしく読める記事：`topics/KE_03_chimoku-23shurui.md`

**確認事項（原文を確かめられなかった根拠）**

- 精度区分ごとの公差の計算式・係数（国土調査法施行令別表第四）は、note-articles/laws/ に原文がないため、このシートでは式と数値を載せていない。

---

## 見出し画像用フレーズ

- 1行目：地積の端数処理と
- 2行目：公差の見分け方（強調：公差）
- 副題：一枚まとめ　土地の表示の登記

---

## 見出し画像プロンプト（note用・1280×670）

女性のMCキャラクター1人だけを描く（トリ先生・藍子は入れない）。キャラクターシート（MC-01〜MC-04）の4枚を添付してから貼る。

```
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the single character at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): this header image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets, and do not invent or change any of them. Place her at the bottom center. POSE IS NOT FIXED: do not copy any pose from the attached images or from earlier header images; let her take a free, natural pose of your own choosing that fits the topic and suits her (for example standing, sitting, leaning, gesturing, or holding a small prop), and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text, and keep her hairstyle exactly as in the attached images. Keep her human anatomy strictly correct: exactly one head, one torso, two arms (one left, one right) and two hands in total, each hand with exactly five fingers; never draw extra arms, hands, or fingers, floating or duplicated hands, arms not growing from the shoulders, or fused hands; check that every shoulder, elbow, and wrist connects naturally.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it:
地積の端数処理と
Line 2 is larger; the phrase 公差 is red-orange and the rest is dark navy:
公差の見分け方
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
一枚まとめ　土地の表示の登記
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no numbers, no watermark.

TOPIC SCENES (illustration only, no text and no numbers on any object; keep them soft and slightly faded so they never compete with the title or the character):
Left side: a calculator next to a survey drawing of a land plot and a pencil, all without any text
Right side: three small landscapes side by side: a town with houses, farm fields, and a forested mountain, all without any text

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the character and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written (cartoon expression marks such as ！ and ？ beside the character's face are decoration, are allowed, and are not extra text); scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地、積、端、数、処、理、公、差、見、分、方、一、枚、土、表、示、登、記; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm the MC character is the only character in the image (no トリ先生, no 藍子), that she matches the attached MC character sheets, and that she keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere. Never delete, redo, or regenerate anything because of an expression mark or a symbol beside a character; deliver the first image as it is.
```

---

## 見出し画像プロンプト（Instagram用・1080×1440）

```
Create an Instagram feed image, portrait layout, EXACTLY 1080x1440 pixels (3:4).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Layout: the title block in the upper part (between y=120px and y=620px), the single character at the bottom center (about y=760px to y=1360px), and the topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): this header image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets, and do not invent or change any of them. Place her at the bottom center. POSE IS NOT FIXED: do not copy any pose from the attached images or from earlier header images; let her take a free, natural pose of your own choosing that fits the topic and suits her (for example standing, sitting, leaning, gesturing, or holding a small prop), and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text, and keep her hairstyle exactly as in the attached images. Keep her human anatomy strictly correct: exactly one head, one torso, two arms (one left, one right) and two hands in total, each hand with exactly five fingers; never draw extra arms, hands, or fingers, floating or duplicated hands, arms not growing from the shoulders, or fused hands; check that every shoulder, elbow, and wrist connects naturally.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it:
地積の端数処理と
Line 2 is larger; the phrase 公差 is red-orange and the rest is dark navy:
公差の見分け方
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
一枚まとめ　土地の表示の登記
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no numbers, no watermark.

TOPIC SCENES (illustration only, no text and no numbers on any object; keep them soft and slightly faded so they never compete with the title or the character):
Left side: a calculator next to a survey drawing of a land plot and a pencil, all without any text
Right side: three small landscapes side by side: a town with houses, farm fields, and a forested mountain, all without any text

INSTAGRAM FEED FORMAT (critical): the profile grid crops the image, so keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom. Do not draw any account name, handle, URL, hashtag or call-to-action text. Make the title letters slightly larger than in the note version.

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the character and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1080x1440 portrait (3:4); confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written (cartoon expression marks such as ！ and ？ beside the character's face are decoration, are allowed, and are not extra text); scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地、積、端、数、処、理、公、差、見、分、方、一、枚、土、表、示、登、記; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm the MC character is the only character in the image (no トリ先生, no 藍子), that she matches the attached MC character sheets, and that she keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere. Never delete, redo, or regenerate anything because of an expression mark or a symbol beside a character; deliver the first image as it is.
```

---

*画像（A-02_chiseki-hasu-kosa.png）のサイズ：1080×3212。HTMLで組んで書き出した文字の図。*
