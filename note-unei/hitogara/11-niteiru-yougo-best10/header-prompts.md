# 第11回「似ている用語ベスト10（同じ問の解説に並んで出てくる組）」見出し画像プロンプト

`03-ikkagetsu-shinsei-gimu/header-prompts.md` と同じ型（2026-11-27改定：背景はトリニティ・カレッジ図書館のロングルームを思わせる重厚な歴史的図書館の内装、背景に胸像・彫像など参照画像の人物以外の人型を一切入れない、人物の腕は左右1本ずつ、参照するキャラクターシートは I-01・I-02・I-03 の3枚）。`src/make_headers.py` が第3回のプロンプトを型にして、タイトル・サブタイトル・題材・ポーズの案だけを差し替えて作る（手で直さない。直すときは `src/header_specs.py` を直して作り直す）。数字は画像に入れない方針なので、タイトルに数は入れず言葉だけにしている。題材の場面：対になった本の並ぶ書架、縦に二列に分けたノート

使い方・確かめることは `note-drafts/header-image-prompts.md` と同じ。

## note用（1280×670）

ファイル名：`hitogara11_header_note.png`

```
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with clean outlines and warm, rich colors. SETTING: the interior of a grand, historic library reminiscent of the Long Room of the Trinity College Library: a long hall with a high, dark wooden barrel-vaulted ceiling, tall two-storey dark oak bookcases packed with old leather-bound books on both sides, an upper gallery (a balcony walkway with a carved wooden railing) running along the bookcases, wooden rolling ladders, and warm golden light falling from tall windows onto the polished floor. Draw it as an original illustration inspired by that dignified, historic atmosphere, not a copy of the real room; no readable book titles, signs, or inscriptions anywhere. NO HUMAN-SHAPED FIGURES IN THE BACKGROUND (critical): do not draw any bust, statue, sculpture, portrait, painting of a person, mannequin, silhouette, or any other human-shaped figure anywhere in the library; create the dignified atmosphere only with the bookcases, the upper gallery, and the carved, decorated ceiling. The main character is the only human figure in the whole image. Keep exactly the same overall layout: the title block at the top center, the single character at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with this library interior.

CHARACTERS (critical): this header image features ONE character only: the main character shown in the attached character-specification images (キャラクターシート_I-01, I-02, I-03). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one main character. Follow the attached character sheets (I-01, I-02, I-03) exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets, and do not invent or change any of them. Place her at the bottom center. POSE IS NOT FIXED: do not copy any pose from the attached images or from earlier header images; let her take a free, natural pose of your own choosing that fits the topic and suits her (for example standing, sitting, leaning, gesturing, or holding a small prop), and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text, and keep her hairstyle exactly as in the attached images. Keep her human anatomy strictly correct: exactly one head, one torso, and exactly two arms in total: one left arm growing from her left shoulder and one right arm growing from her right shoulder (one arm on each side, never two arms on the same side), and two hands in total, each hand with exactly five fingers; never draw extra arms, hands, or fingers, floating or duplicated hands, arms not growing from the shoulders, or fused hands; check that every shoulder, elbow, and wrist connects naturally.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft, rounded cream-white glow so it reads clearly against the library. Line 1 is dark navy with a pale yellow marker stroke behind it:
似ている用語を
Line 2 is larger; the phrase 並べて is red-orange and the rest is dark navy:
並べて比べる
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
同じ問に出てくる組を数えた
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the character):
Left side: pairs of matching books standing side by side on a shelf, each pair in the same color but a slightly different size, with blank spines (no writing, no numbers, no letters).
Right side: an open notebook whose page is divided into two clean columns by a vertical line, with blank lines only (no writing, no numbers, no letters), and a pencil resting on it.
For her pose this time, a suggestion that fits the topic (not mandatory): she holds up two similar-looking books, one in each hand, tilting her head slightly with a puzzled but amused expression, as if asking which is which.

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the character and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written (cartoon expression marks such as ！ and ？ beside the characters' faces are decoration, are allowed, and are not extra text); scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 似、用、語、並、比、同、問、出、組、数; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm the main character is the only character in the image (no トリ先生, no 藍子), that she matches the attached character sheets (I-01, I-02, I-03), that she keeps the same hairstyle, and that she has exactly one left arm and one right arm; confirm there is no bust, statue, portrait, or other human-shaped figure anywhere in the background; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere. Never delete, redo, or regenerate anything because of an expression mark or a symbol beside a character; deliver the first image as it is.
```

## Instagram用（1080×1440）

ファイル名：`hitogara11_header_ig.png`

```
Create an Instagram feed image, 1080x1440px (3:4 portrait aspect ratio). Keep 54px side margins and 72px top and bottom margins free of text.

STYLE: soft Japanese watercolor-like illustration with clean outlines and warm, rich colors. SETTING: the interior of a grand, historic library reminiscent of the Long Room of the Trinity College Library: a long hall with a high, dark wooden barrel-vaulted ceiling, tall two-storey dark oak bookcases packed with old leather-bound books on both sides, an upper gallery (a balcony walkway with a carved wooden railing) running along the bookcases, wooden rolling ladders, and warm golden light falling from tall windows onto the polished floor. Draw it as an original illustration inspired by that dignified, historic atmosphere, not a copy of the real room; no readable book titles, signs, or inscriptions anywhere. NO HUMAN-SHAPED FIGURES IN THE BACKGROUND (critical): do not draw any bust, statue, sculpture, portrait, painting of a person, mannequin, silhouette, or any other human-shaped figure anywhere in the library; create the dignified atmosphere only with the bookcases, the upper gallery, and the carved, decorated ceiling. The main character is the only human figure in the whole image. Layout for portrait: the title block in the upper third, the single character in the lower half at the center, and topic scenes softly at the left and right around her.
Fill the whole canvas with this library interior.

CHARACTERS (critical): this header image features ONE character only: the main character shown in the attached character-specification images (キャラクターシート_I-01, I-02, I-03). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one main character. Follow the attached character sheets (I-01, I-02, I-03) exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets, and do not invent or change any of them. Place her at the bottom center. POSE IS NOT FIXED: do not copy any pose from the attached images or from earlier header images; let her take a free, natural pose of your own choosing that fits the topic and suits her (for example standing, sitting, leaning, gesturing, or holding a small prop), and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text, and keep her hairstyle exactly as in the attached images. Keep her human anatomy strictly correct: exactly one head, one torso, and exactly two arms in total: one left arm growing from her left shoulder and one right arm growing from her right shoulder (one arm on each side, never two arms on the same side), and two hands in total, each hand with exactly five fingers; never draw extra arms, hands, or fingers, floating or duplicated hands, arms not growing from the shoulders, or fused hands; check that every shoulder, elbow, and wrist connects naturally.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft, rounded cream-white glow so it reads clearly against the library. Line 1 is dark navy with a pale yellow marker stroke behind it:
似ている用語を
Line 2 is larger; the phrase 並べて is red-orange and the rest is dark navy:
並べて比べる
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
同じ問に出てくる組を数えた
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the character):
Left side: pairs of matching books standing side by side on a shelf, each pair in the same color but a slightly different size, with blank spines (no writing, no numbers, no letters).
Right side: an open notebook whose page is divided into two clean columns by a vertical line, with blank lines only (no writing, no numbers, no letters), and a pencil resting on it.
For her pose this time, a suggestion that fits the topic (not mandatory): she holds up two similar-looking books, one in each hand, tilting her head slightly with a puzzled but amused expression, as if asking which is which.

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the character and the title away from the extreme edges so nothing important touches the edges. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1080x1440 portrait; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written (cartoon expression marks such as ！ and ？ beside the characters' faces are decoration, are allowed, and are not extra text); scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 似、用、語、並、比、同、問、出、組、数; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm the main character is the only character in the image (no トリ先生, no 藍子), that she matches the attached character sheets (I-01, I-02, I-03), that she keeps the same hairstyle, and that she has exactly one left arm and one right arm; confirm there is no bust, statue, portrait, or other human-shaped figure anywhere in the background; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere. Never delete, redo, or regenerate anything because of an expression mark or a symbol beside a character; deliver the first image as it is.

Do not add any account name, URL, hashtag or the word note anywhere in the image.
```
