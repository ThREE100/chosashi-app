# 「数字の図鑑」 見出し画像のプロンプト（note用・Instagram用）

2026-11-04 作成（`src/gen_prompts.py` で作る）。記事のタイトル「【土地家屋調査士】不動産登記法の「数字の図鑑」〜一月・二年・三年・十年…期限と数字は、「何の登記か」と「いつから数えるか」で整理すると覚えやすい〜」に合わせて、2種類を用意した。どちらも女性のMCキャラクター1人だけを描く（トリ先生・藍子は入れない）。
画像の生成と目視確認はChatGPTで行う（未実施）。キャラクターシート `キャラクターシート_MC-01〜MC-04` の4枚を添付してから貼る。

| 用途 | サイズ | 文字 |
|---|---|---|
| note用（記事の見出し画像） | 1280×670（横長） | 「不動産登記法の」／「数字の図鑑」／「何の登記か　いつから数えるか」 |
| Instagram用（表紙・フィードの1枚） | 1080×1350（4:5） | 「不動産登記法の」／「数字の図鑑」／「期限と数字を整理する」／「何の登記か　いつから数えるか」 |

## 確かめること

- 大きさが指定どおりか（note用 1280×670、Instagram用 1080×1350）。
- 文字が、上の文面と**1字ずつ**一致しているか（簡体字・繁体字の字形になっていないか、余計な文字・数字・英字がないか）。
- キャラクターがMC1人だけか。シートの髪型・服装と合っているか。手や腕の数が合っているか。
- Instagram用は、文字と主要な絵が外側の余白（左右54px・上下72px）の内側にあるか。アカウント名・URLが入っていないか。
- カレンダーの絵に数字が入っていないか。
- 背景が不透明か。
- 直すときは、プロンプトの最後に「次の点だけを直して、ほかは変えない：…」と1文足して再生成する。

文字が崩れるときは、「TEXT」の部分を「No text」に書き換えて文字なしの背景とキャラクターだけを作らせ、文字はCanvaなどで重ねる。

## note用（1280×670）

```
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the single character at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): this image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets. POSE IS NOT FIXED: let her take a free, natural pose of your own choosing that fits the topic (for example opening a small drawer of a big cabinet, holding a notebook, or pointing at a drawer label), and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text. Keep her human anatomy strictly correct: exactly one head, one torso, two arms and two hands in total, each hand with exactly five fingers; no extra or floating hands or arms.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese or Traditional Chinese characters; every glyph must match the standard Japanese form exactly. Reproduce the exact text strings given below verbatim; do not paraphrase or substitute any character. No stray or decorative glyphs of any kind.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge; no transparency, no checkerboard, no unpainted edge.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow. Line 1 is dark navy with a pale yellow marker stroke behind it:
不動産登記法の
Line 2 is larger; the phrase 数字 is red-orange and the rest is dark navy:
数字の図鑑
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
何の登記か　いつから数えるか
Do not write any other text anywhere in the image.

TOPIC SCENES (illustration only, no text on any object; soft and slightly faded): Left side: a wooden specimen cabinet with seven small blank drawers in different colors (blue, pale orange, red-orange, gray-green, purple-gray). Right side: a calendar page with no numbers on it, an hourglass, and a small stack of notebooks.

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the character and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, arrow between boxes, check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text is the two title lines and the subtitle, exactly as written; scan every kanji (不・動・産・登・記・法・数・字・図・鑑・何・日・始) for Simplified or Traditional Chinese forms; confirm the MC character is the only character; confirm the canvas is fully opaque.
```

## Instagram用（1080×1350・4:5）

```
Create an Instagram feed cover image, portrait layout, EXACTLY 1080x1350 pixels (4:5).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com header images of the same series. Fill the whole canvas with the pastel sky and soft clouds.

INSTAGRAM FEED FORMAT (critical): the profile grid crops the image, so keep every text and every important drawing inside a safe margin of 54px on the left and right and 68px at the top and bottom. Do not draw any account name, handle, URL, hashtag or call-to-action text, and no logo or watermark.

CHARACTERS (critical): this image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets. POSE IS NOT FIXED: let her take a free, natural pose of your own choosing that fits the topic (for example opening a small drawer of a big cabinet, holding a notebook, or pointing at a drawer label), and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text. Keep her human anatomy strictly correct: exactly one head, one torso, two arms and two hands in total, each hand with exactly five fingers; no extra or floating hands or arms.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese or Traditional Chinese characters; every glyph must match the standard Japanese form exactly. Reproduce the exact text strings given below verbatim; do not paraphrase or substitute any character. No stray or decorative glyphs of any kind.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge; no transparency, no checkerboard, no unpainted edge.

TEXT (reproduce verbatim, nothing else), centered in the upper part of the canvas between y=100px and y=570px, over a soft white cloud-shaped glow, bold rounded font. Line 1, large, dark navy with a pale yellow marker stroke behind it:
不動産登記法の
Line 2, very large; the phrase 数字 is red-orange and the rest is dark navy:
数字の図鑑
Line 3, in a light blue rounded pill-shaped band with navy text:
期限と数字を整理する
Line 4, smaller, dark navy, below the band:
何の登記か　いつから数えるか
Do not write any other text anywhere in the image.

SCENE: the MC character stands at the bottom center (about y=700px to y=1280px), with a big wooden specimen cabinet of seven blank drawers in different colors (blue, pale orange, red-orange, gray-green, purple-gray) behind her, drawn simply. A calendar page with no numbers on it and an hourglass sit on a desk at the lower right. No text on any object; props stay soft so they never compete with the title or the character.

LAYOUT: keep a clear, uncluttered zone behind the title block. Do not draw any flowchart, arrow between boxes, check mark or cross mark.

Final check before rendering: confirm the image is exactly 1080x1350 portrait (4:5); confirm the only text is the four title lines, exactly as written; scan every kanji (不・動・産・登・記・法・数・字・図・鑑・期・限・整・理・何・日・始) for Simplified or Traditional Chinese forms; confirm the MC character is the only character; confirm nothing important lies within the outer safe margin; confirm the canvas is fully opaque.
```
