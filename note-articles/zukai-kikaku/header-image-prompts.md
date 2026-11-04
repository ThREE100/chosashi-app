# 図解企画6本 見出し画像のプロンプト（note用・Instagram用）

作成 2026-11-05（`src/gen_prompts.py` で作る。手で直さない）。企画ごとに、**note用（1280×670）とInstagram用（1080×1440・3:4）の2種類**。
画像の生成と目視確認はChatGPTで行う（未実施）。キャラクターシート `キャラクターシート_MC-01〜MC-04` の4枚を添付してから貼る。見出し画像のキャラクターはMC1人だけ（トリ先生・藍子は入れない）。

## 確かめること

- 大きさが指定どおりか（note用 1280×670、Instagram用 1080×1440）。
- 文字が、各表の文面と**1字ずつ**一致しているか（簡体字・繁体字・余計な文字・数字・英字がないか）。
- キャラクターがMC1人だけか。手や腕の数が合っているか。
- Instagram用は、文字と主要な絵が外側の余白（左右54px・上下72px）の内側にあるか。アカウント名・URLが入っていないか。
- 背景が不透明か。
- 直すときは、プロンプトの最後に「次の点だけを直して、ほかは変えない：…」と1文足して再生成する。

文字が崩れるときは、「TEXT」の部分を「No text」に書き換えて文字なしで作らせ、文字はCanvaなどで重ねる。

## KZ_01　土地の一生・建物の一生

| 用途 | サイズ | 文字 |
|---|---|---|
| note用 | 1280×670 | 「土地と建物の」／「一生を一本の線で」／「登記が時間順に起こすこと」 |
| Instagram用 | 1080×1440 | 「土地と建物の」／「一生を一本の線で」／「登記が時間順に起こすこと」／「一月以内か、期限の定めなしか」 |

### note用（1280×670）

```
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the single character at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): this image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets. POSE IS NOT FIXED: let her take a free, natural pose of your own choosing that fits the topic, and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text. Keep her human anatomy strictly correct: exactly one head, one torso, two arms and two hands in total, each hand with exactly five fingers; no extra or floating hands or arms.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese or Traditional Chinese characters; every glyph must match the standard Japanese form exactly. Reproduce the exact text strings given below verbatim; do not paraphrase or substitute any character. No stray or decorative glyphs of any kind.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge; no transparency, no checkerboard, no unpainted edge.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow. Line 1 is dark navy with a pale yellow marker stroke behind it:
土地と建物の
Line 2 is larger; the phrase 一本の線 is red-orange and the rest is dark navy:
一生を一本の線で
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
登記が時間順に起こすこと
Do not write any other text anywhere in the image.

TOPIC SCENES (illustration only, no text on any object; soft and slightly faded): Left side: a small plot of land with a boundary line and a tiny signpost. Right side: a small house under construction with a scaffold and a calendar page with no numbers.

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the character and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, arrow between boxes, check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text is the two title lines and the subtitle, exactly as written; scan every kanji (土・地・建・物・一・生・本・線・登・記・時・間・順・起) for Simplified or Traditional Chinese forms; confirm the MC character is the only character; confirm the canvas is fully opaque.
```

### Instagram用（1080×1440・3:4）

```
Create an Instagram feed cover image, portrait layout, EXACTLY 1080x1440 pixels (3:4).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com header images of the same series. Fill the whole canvas with the pastel sky and soft clouds.

INSTAGRAM FEED FORMAT (critical): the profile grid crops the image, so keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom. Do not draw any account name, handle, URL, hashtag or call-to-action text, and no logo or watermark.

CHARACTERS (critical): this image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets. POSE IS NOT FIXED: let her take a free, natural pose of your own choosing that fits the topic, and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text. Keep her human anatomy strictly correct: exactly one head, one torso, two arms and two hands in total, each hand with exactly five fingers; no extra or floating hands or arms.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese or Traditional Chinese characters; every glyph must match the standard Japanese form exactly. Reproduce the exact text strings given below verbatim; do not paraphrase or substitute any character. No stray or decorative glyphs of any kind.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge; no transparency, no checkerboard, no unpainted edge.

TEXT (reproduce verbatim, nothing else), centered in the upper part of the canvas between y=120px and y=620px, over a soft white cloud-shaped glow, bold rounded font. Line 1, large, dark navy with a pale yellow marker stroke behind it:
土地と建物の
Line 2, very large; the phrase 一本の線 is red-orange and the rest is dark navy:
一生を一本の線で
Line 3, in a light blue rounded pill-shaped band with navy text:
登記が時間順に起こすこと
Line 4, smaller, dark navy, below the band:
一月以内か、期限の定めなしか
Do not write any other text anywhere in the image.

SCENE: the MC character stands at the bottom center (about y=760px to y=1360px). Behind and beside her, drawn simply and softly: a small plot of land with a boundary line, a small house model, and a winding path with blank signposts. No text on any object; props stay soft so they never compete with the title or the character.

LAYOUT: keep a clear, uncluttered zone behind the title block. Do not draw any flowchart, arrow between boxes, check mark or cross mark.

Final check before rendering: confirm the image is exactly 1080x1440 portrait; confirm the only text is the 4 title lines, exactly as written; scan every kanji (土・地・建・物・一・生・本・線・登・記・時・間・順・起・月・以・内・期・限・定) for Simplified or Traditional Chinese forms; confirm the MC character is the only character; confirm nothing important lies within the outer safe margin; confirm the canvas is fully opaque.
```

## KZ_02　似た用語の対比図鑑

| 用途 | サイズ | 文字 |
|---|---|---|
| note用 | 1280×670 | 「似ている用語の」／「対比図鑑」／「分筆と分割、合体と合併ほか」 |
| Instagram用 | 1080×1440 | 「似ている用語の」／「対比図鑑」／「分筆と分割、合体と合併ほか」／「混同しやすい組を二列で比べる」 |

### note用（1280×670）

```
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the single character at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): this image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets. POSE IS NOT FIXED: let her take a free, natural pose of your own choosing that fits the topic, and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text. Keep her human anatomy strictly correct: exactly one head, one torso, two arms and two hands in total, each hand with exactly five fingers; no extra or floating hands or arms.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese or Traditional Chinese characters; every glyph must match the standard Japanese form exactly. Reproduce the exact text strings given below verbatim; do not paraphrase or substitute any character. No stray or decorative glyphs of any kind.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge; no transparency, no checkerboard, no unpainted edge.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow. Line 1 is dark navy with a pale yellow marker stroke behind it:
似ている用語の
Line 2 is larger; the phrase 対比 is red-orange and the rest is dark navy:
対比図鑑
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
分筆と分割、合体と合併ほか
Do not write any other text anywhere in the image.

TOPIC SCENES (illustration only, no text on any object; soft and slightly faded): Left side: an open picture book with two facing blank pages. Right side: two small blocks, one a plot of land and one a house, standing side by side.

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the character and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, arrow between boxes, check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text is the two title lines and the subtitle, exactly as written; scan every kanji (似・用・語・対・比・図・鑑・分・筆・割・合・体・併) for Simplified or Traditional Chinese forms; confirm the MC character is the only character; confirm the canvas is fully opaque.
```

### Instagram用（1080×1440・3:4）

```
Create an Instagram feed cover image, portrait layout, EXACTLY 1080x1440 pixels (3:4).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com header images of the same series. Fill the whole canvas with the pastel sky and soft clouds.

INSTAGRAM FEED FORMAT (critical): the profile grid crops the image, so keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom. Do not draw any account name, handle, URL, hashtag or call-to-action text, and no logo or watermark.

CHARACTERS (critical): this image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets. POSE IS NOT FIXED: let her take a free, natural pose of your own choosing that fits the topic, and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text. Keep her human anatomy strictly correct: exactly one head, one torso, two arms and two hands in total, each hand with exactly five fingers; no extra or floating hands or arms.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese or Traditional Chinese characters; every glyph must match the standard Japanese form exactly. Reproduce the exact text strings given below verbatim; do not paraphrase or substitute any character. No stray or decorative glyphs of any kind.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge; no transparency, no checkerboard, no unpainted edge.

TEXT (reproduce verbatim, nothing else), centered in the upper part of the canvas between y=120px and y=620px, over a soft white cloud-shaped glow, bold rounded font. Line 1, large, dark navy with a pale yellow marker stroke behind it:
似ている用語の
Line 2, very large; the phrase 対比 is red-orange and the rest is dark navy:
対比図鑑
Line 3, in a light blue rounded pill-shaped band with navy text:
分筆と分割、合体と合併ほか
Line 4, smaller, dark navy, below the band:
混同しやすい組を二列で比べる
Do not write any other text anywhere in the image.

SCENE: the MC character stands at the bottom center (about y=760px to y=1360px). Behind and beside her, drawn simply and softly: an open picture book with two facing blank pages, and a small plot of land and a small house standing side by side. No text on any object; props stay soft so they never compete with the title or the character.

LAYOUT: keep a clear, uncluttered zone behind the title block. Do not draw any flowchart, arrow between boxes, check mark or cross mark.

Final check before rendering: confirm the image is exactly 1080x1440 portrait; confirm the only text is the 4 title lines, exactly as written; scan every kanji (似・用・語・対・比・図・鑑・分・筆・割・合・体・併・混・同・組・二・列) for Simplified or Traditional Chinese forms; confirm the MC character is the only character; confirm nothing important lies within the outer safe margin; confirm the canvas is fully opaque.
```

## KZ_03　表示に関する登記の添付情報 早見図

| 用途 | サイズ | 文字 |
|---|---|---|
| note用 | 1280×670 | 「表示の登記の」／「添付情報早見図」／「何の登記に何を付けるか」 |
| Instagram用 | 1080×1440 | 「表示の登記の」／「添付情報早見図」／「何の登記に何を付けるか」／「令別表の項で決まる」 |

### note用（1280×670）

```
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the single character at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): this image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets. POSE IS NOT FIXED: let her take a free, natural pose of your own choosing that fits the topic, and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text. Keep her human anatomy strictly correct: exactly one head, one torso, two arms and two hands in total, each hand with exactly five fingers; no extra or floating hands or arms.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese or Traditional Chinese characters; every glyph must match the standard Japanese form exactly. Reproduce the exact text strings given below verbatim; do not paraphrase or substitute any character. No stray or decorative glyphs of any kind.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge; no transparency, no checkerboard, no unpainted edge.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow. Line 1 is dark navy with a pale yellow marker stroke behind it:
表示の登記の
Line 2 is larger; the phrase 早見図 is red-orange and the rest is dark navy:
添付情報早見図
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
何の登記に何を付けるか
Do not write any other text anywhere in the image.

TOPIC SCENES (illustration only, no text on any object; soft and slightly faded): Left side: a clipboard with blank sheets and a few paper clips. Right side: a small stack of blank documents and a rubber stamp with no text.

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the character and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, arrow between boxes, check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text is the two title lines and the subtitle, exactly as written; scan every kanji (表・示・登・記・添・付・情・報・早・見・図・何) for Simplified or Traditional Chinese forms; confirm the MC character is the only character; confirm the canvas is fully opaque.
```

### Instagram用（1080×1440・3:4）

```
Create an Instagram feed cover image, portrait layout, EXACTLY 1080x1440 pixels (3:4).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com header images of the same series. Fill the whole canvas with the pastel sky and soft clouds.

INSTAGRAM FEED FORMAT (critical): the profile grid crops the image, so keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom. Do not draw any account name, handle, URL, hashtag or call-to-action text, and no logo or watermark.

CHARACTERS (critical): this image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets. POSE IS NOT FIXED: let her take a free, natural pose of your own choosing that fits the topic, and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text. Keep her human anatomy strictly correct: exactly one head, one torso, two arms and two hands in total, each hand with exactly five fingers; no extra or floating hands or arms.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese or Traditional Chinese characters; every glyph must match the standard Japanese form exactly. Reproduce the exact text strings given below verbatim; do not paraphrase or substitute any character. No stray or decorative glyphs of any kind.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge; no transparency, no checkerboard, no unpainted edge.

TEXT (reproduce verbatim, nothing else), centered in the upper part of the canvas between y=120px and y=620px, over a soft white cloud-shaped glow, bold rounded font. Line 1, large, dark navy with a pale yellow marker stroke behind it:
表示の登記の
Line 2, very large; the phrase 早見図 is red-orange and the rest is dark navy:
添付情報早見図
Line 3, in a light blue rounded pill-shaped band with navy text:
何の登記に何を付けるか
Line 4, smaller, dark navy, below the band:
令別表の項で決まる
Do not write any other text anywhere in the image.

SCENE: the MC character stands at the bottom center (about y=760px to y=1360px). Behind and beside her, drawn simply and softly: a clipboard with blank sheets, paper clips, and a small stack of blank documents. No text on any object; props stay soft so they never compete with the title or the character.

LAYOUT: keep a clear, uncluttered zone behind the title block. Do not draw any flowchart, arrow between boxes, check mark or cross mark.

Final check before rendering: confirm the image is exactly 1080x1440 portrait; confirm the only text is the 4 title lines, exactly as written; scan every kanji (表・示・登・記・添・付・情・報・早・見・図・何・令・別・項・決) for Simplified or Traditional Chinese forms; confirm the MC character is the only character; confirm nothing important lies within the outer safe margin; confirm the canvas is fully opaque.
```

## KZ_04　条文の読み方 図解

| 用途 | サイズ | 文字 |
|---|---|---|
| note用 | 1280×670 | 「条文の読み方」／「図解で読み解く」／「ただし書・準用・前項・みなす」 |
| Instagram用 | 1080×1440 | 「条文の読み方」／「図解で読み解く」／「ただし書・準用・前項・みなす」／「実際の条文を例にして」 |

### note用（1280×670）

```
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the single character at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): this image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets. POSE IS NOT FIXED: let her take a free, natural pose of your own choosing that fits the topic, and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text. Keep her human anatomy strictly correct: exactly one head, one torso, two arms and two hands in total, each hand with exactly five fingers; no extra or floating hands or arms.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese or Traditional Chinese characters; every glyph must match the standard Japanese form exactly. Reproduce the exact text strings given below verbatim; do not paraphrase or substitute any character. No stray or decorative glyphs of any kind.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge; no transparency, no checkerboard, no unpainted edge.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow. Line 1 is dark navy with a pale yellow marker stroke behind it:
条文の読み方
Line 2 is larger; the phrase 読み解く is red-orange and the rest is dark navy:
図解で読み解く
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
ただし書・準用・前項・みなす
Do not write any other text anywhere in the image.

TOPIC SCENES (illustration only, no text on any object; soft and slightly faded): Left side: a large open statute book and a magnifying glass. Right side: a small stack of books and a pen.

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the character and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, arrow between boxes, check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text is the two title lines and the subtitle, exactly as written; scan every kanji (条・文・読・方・図・解・書・準・用・前・項) for Simplified or Traditional Chinese forms; confirm the MC character is the only character; confirm the canvas is fully opaque.
```

### Instagram用（1080×1440・3:4）

```
Create an Instagram feed cover image, portrait layout, EXACTLY 1080x1440 pixels (3:4).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com header images of the same series. Fill the whole canvas with the pastel sky and soft clouds.

INSTAGRAM FEED FORMAT (critical): the profile grid crops the image, so keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom. Do not draw any account name, handle, URL, hashtag or call-to-action text, and no logo or watermark.

CHARACTERS (critical): this image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets. POSE IS NOT FIXED: let her take a free, natural pose of your own choosing that fits the topic, and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text. Keep her human anatomy strictly correct: exactly one head, one torso, two arms and two hands in total, each hand with exactly five fingers; no extra or floating hands or arms.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese or Traditional Chinese characters; every glyph must match the standard Japanese form exactly. Reproduce the exact text strings given below verbatim; do not paraphrase or substitute any character. No stray or decorative glyphs of any kind.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge; no transparency, no checkerboard, no unpainted edge.

TEXT (reproduce verbatim, nothing else), centered in the upper part of the canvas between y=120px and y=620px, over a soft white cloud-shaped glow, bold rounded font. Line 1, large, dark navy with a pale yellow marker stroke behind it:
条文の読み方
Line 2, very large; the phrase 読み解く is red-orange and the rest is dark navy:
図解で読み解く
Line 3, in a light blue rounded pill-shaped band with navy text:
ただし書・準用・前項・みなす
Line 4, smaller, dark navy, below the band:
実際の条文を例にして
Do not write any other text anywhere in the image.

SCENE: the MC character stands at the bottom center (about y=760px to y=1360px). Behind and beside her, drawn simply and softly: a large open statute book with a magnifying glass, and a small stack of books. No text on any object; props stay soft so they never compete with the title or the character.

LAYOUT: keep a clear, uncluttered zone behind the title block. Do not draw any flowchart, arrow between boxes, check mark or cross mark.

Final check before rendering: confirm the image is exactly 1080x1440 portrait; confirm the only text is the 4 title lines, exactly as written; scan every kanji (条・文・読・方・図・解・書・準・用・前・項・実・際・例) for Simplified or Traditional Chinese forms; confirm the MC character is the only character; confirm nothing important lies within the outer safe margin; confirm the canvas is fully opaque.
```

## KZ_05　記述式の「解く順番」図

| 用途 | サイズ | 文字 |
|---|---|---|
| note用 | 1280×670 | 「記述式の」／「解く順番」／「土地と建物の型別に示す」 |
| Instagram用 | 1080×1440 | 「記述式の」／「解く順番」／「土地と建物の型別に示す」／「座標や求積の前にできること」 |

### note用（1280×670）

```
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the single character at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): this image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets. POSE IS NOT FIXED: let her take a free, natural pose of your own choosing that fits the topic, and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text. Keep her human anatomy strictly correct: exactly one head, one torso, two arms and two hands in total, each hand with exactly five fingers; no extra or floating hands or arms.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese or Traditional Chinese characters; every glyph must match the standard Japanese form exactly. Reproduce the exact text strings given below verbatim; do not paraphrase or substitute any character. No stray or decorative glyphs of any kind.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge; no transparency, no checkerboard, no unpainted edge.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow. Line 1 is dark navy with a pale yellow marker stroke behind it:
記述式の
Line 2 is larger; the phrase 解く順番 is red-orange and the rest is dark navy:
解く順番
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
土地と建物の型別に示す
Do not write any other text anywhere in the image.

TOPIC SCENES (illustration only, no text on any object; soft and slightly faded): Left side: a stopwatch and an answer sheet with a pencil. Right side: a small stack of blank sheets and a calculator with no numbers on its screen.

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the character and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, arrow between boxes, check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text is the two title lines and the subtitle, exactly as written; scan every kanji (記・述・式・解・順・番・土・地・建・物・型・別・示) for Simplified or Traditional Chinese forms; confirm the MC character is the only character; confirm the canvas is fully opaque.
```

### Instagram用（1080×1440・3:4）

```
Create an Instagram feed cover image, portrait layout, EXACTLY 1080x1440 pixels (3:4).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com header images of the same series. Fill the whole canvas with the pastel sky and soft clouds.

INSTAGRAM FEED FORMAT (critical): the profile grid crops the image, so keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom. Do not draw any account name, handle, URL, hashtag or call-to-action text, and no logo or watermark.

CHARACTERS (critical): this image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets. POSE IS NOT FIXED: let her take a free, natural pose of your own choosing that fits the topic, and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text. Keep her human anatomy strictly correct: exactly one head, one torso, two arms and two hands in total, each hand with exactly five fingers; no extra or floating hands or arms.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese or Traditional Chinese characters; every glyph must match the standard Japanese form exactly. Reproduce the exact text strings given below verbatim; do not paraphrase or substitute any character. No stray or decorative glyphs of any kind.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge; no transparency, no checkerboard, no unpainted edge.

TEXT (reproduce verbatim, nothing else), centered in the upper part of the canvas between y=120px and y=620px, over a soft white cloud-shaped glow, bold rounded font. Line 1, large, dark navy with a pale yellow marker stroke behind it:
記述式の
Line 2, very large; the phrase 解く順番 is red-orange and the rest is dark navy:
解く順番
Line 3, in a light blue rounded pill-shaped band with navy text:
土地と建物の型別に示す
Line 4, smaller, dark navy, below the band:
座標や求積の前にできること
Do not write any other text anywhere in the image.

SCENE: the MC character stands at the bottom center (about y=760px to y=1360px). Behind and beside her, drawn simply and softly: a stopwatch, an answer sheet with a pencil, and a calculator with a blank screen. No text on any object; props stay soft so they never compete with the title or the character.

LAYOUT: keep a clear, uncluttered zone behind the title block. Do not draw any flowchart, arrow between boxes, check mark or cross mark.

Final check before rendering: confirm the image is exactly 1080x1440 portrait; confirm the only text is the 4 title lines, exactly as written; scan every kanji (記・述・式・解・順・番・土・地・建・物・型・別・示・座・標・求・積・前) for Simplified or Traditional Chinese forms; confirm the MC character is the only character; confirm nothing important lies within the outer safe margin; confirm the canvas is fully opaque.
```

## KZ_06　ある一日の登記ストーリー

| 用途 | サイズ | 文字 |
|---|---|---|
| note用 | 1280×670 | 「ある一日の」／「登記ストーリー」／「新築から表題登記まで」 |
| Instagram用 | 1080×1440 | 「ある一日の」／「登記ストーリー」／「新築から表題登記まで」／「トリ先生と藍子の四コマ」 |

### note用（1280×670）

```
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the single character at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): this image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets. POSE IS NOT FIXED: let her take a free, natural pose of your own choosing that fits the topic, and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text. Keep her human anatomy strictly correct: exactly one head, one torso, two arms and two hands in total, each hand with exactly five fingers; no extra or floating hands or arms.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese or Traditional Chinese characters; every glyph must match the standard Japanese form exactly. Reproduce the exact text strings given below verbatim; do not paraphrase or substitute any character. No stray or decorative glyphs of any kind.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge; no transparency, no checkerboard, no unpainted edge.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow. Line 1 is dark navy with a pale yellow marker stroke behind it:
ある一日の
Line 2 is larger; the phrase ストーリー is red-orange and the rest is dark navy:
登記ストーリー
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
新築から表題登記まで
Do not write any other text anywhere in the image.

TOPIC SCENES (illustration only, no text on any object; soft and slightly faded): Left side: a newly built small house with a blank signboard. Right side: a small government office building and a surveying tripod.

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the character and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, arrow between boxes, check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text is the two title lines and the subtitle, exactly as written; scan every kanji (一・日・登・記・新・築・表・題) for Simplified or Traditional Chinese forms; confirm the MC character is the only character; confirm the canvas is fully opaque.
```

### Instagram用（1080×1440・3:4）

```
Create an Instagram feed cover image, portrait layout, EXACTLY 1080x1440 pixels (3:4).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com header images of the same series. Fill the whole canvas with the pastel sky and soft clouds.

INSTAGRAM FEED FORMAT (critical): the profile grid crops the image, so keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom. Do not draw any account name, handle, URL, hashtag or call-to-action text, and no logo or watermark.

CHARACTERS (critical): this image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets. POSE IS NOT FIXED: let her take a free, natural pose of your own choosing that fits the topic, and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text. Keep her human anatomy strictly correct: exactly one head, one torso, two arms and two hands in total, each hand with exactly five fingers; no extra or floating hands or arms.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese or Traditional Chinese characters; every glyph must match the standard Japanese form exactly. Reproduce the exact text strings given below verbatim; do not paraphrase or substitute any character. No stray or decorative glyphs of any kind.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge; no transparency, no checkerboard, no unpainted edge.

TEXT (reproduce verbatim, nothing else), centered in the upper part of the canvas between y=120px and y=620px, over a soft white cloud-shaped glow, bold rounded font. Line 1, large, dark navy with a pale yellow marker stroke behind it:
ある一日の
Line 2, very large; the phrase ストーリー is red-orange and the rest is dark navy:
登記ストーリー
Line 3, in a light blue rounded pill-shaped band with navy text:
新築から表題登記まで
Line 4, smaller, dark navy, below the band:
トリ先生と藍子の四コマ
Do not write any other text anywhere in the image.

SCENE: the MC character stands at the bottom center (about y=760px to y=1360px). Behind and beside her, drawn simply and softly: a newly built small house, a small government office building and a surveying tripod. No text on any object; props stay soft so they never compete with the title or the character.

LAYOUT: keep a clear, uncluttered zone behind the title block. Do not draw any flowchart, arrow between boxes, check mark or cross mark.

Final check before rendering: confirm the image is exactly 1080x1440 portrait; confirm the only text is the 4 title lines, exactly as written; scan every kanji (一・日・登・記・新・築・表・題・先・生・藍・子・四) for Simplified or Traditional Chinese forms; confirm the MC character is the only character; confirm nothing important lies within the outer safe margin; confirm the canvas is fully opaque.
```
