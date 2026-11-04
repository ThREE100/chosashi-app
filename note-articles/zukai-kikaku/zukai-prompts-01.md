# 土地の一生・建物の一生 図解画像のプロンプト（ChatGPT用・note用とInstagram用）

作成 2026-11-05（`src/gen_prompts.py` で作る。手で直さない）。記事 `01-tochi-tatemono-isshou.md` に差し込む図2枚について、**note用（縦長・図ごとのサイズ）とInstagram用（1080×1440・3:4）の2種類**を用意した。

## 使い方

1. 図ごとに、noteに使うなら「note用」、Instagramに使うなら「Instagram用」のコードブロックを、そのままChatGPTに貼る。文字は同じで、大きさと余白だけ違う。
2. 画像の中に図番は入れない（管理番号は、PNG名と記事のマーカーだけ）。
3. 色の約束：**表示に関する登記＝青、権利に関する登記＝薄い橙**。ほかの色は意味を持たせない（手順は薄い黄と水色）。同じ企画の図を並べたとき、色がそろっているか確かめる。
4. ファイル名は、note用が `kz01_zu01.png` から、Instagram用が `kz01_ig01.png` から。
5. 直すときは、プロンプトの最後に「次の点だけを直して、ほかは変えない：…」と1文足して再生成する。

## 確かめること

- 大きさが指定どおりか（note用は図ごとに違う、Instagram用は1080×1440）。
- 文字が、各プロンプトの「Words allowed」と**1字ずつ**一致しているか（簡体字・繁体字になっていないか、余計な文字・数字がないか）。
- 条文番号・項番号が正しく出ているか。
- 図番（図1など）が画像に入っていないか。
- Instagram用は、文字と主要な絵が外側の余白（左右54px・上下72px）の内側にあるか。アカウント名・URLが入っていないか。
- 背景が不透明か。

文字が何度やっても崩れるときは、「Words allowed」の行を残したまま「No text」の版（文字なしの枠と絵だけ）を作らせて、文字はCanvaで入れる。

## 図の一覧

| 管理番号 | 内容 | note用のサイズ | Instagram用のサイズ |
|---|---|---|---|
| zu01 | 土地の一生 | 1080x1800 | 1080x1440 |
| zu02 | 建物の一生 | 1080x1900 | 1080x1440 |

## 図1：土地の一生（zu01）

### note用（1080x1800）

```
Create a Japanese-language infographic, portrait layout, 1080x1800 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: a winding path with small signposts and milestones, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「土地の一生を一本の線で」 / subtitle band: 「登記が起こす出来事を時間順に」

--- BODY (one winding vertical path from top to bottom with four milestone cards on the path, and one side card branching off to the right after the first card) ---
 - Milestone card 1 (blue): heading 「表題登記」, line 「第36条　取得の日から一月以内」
 - Side card, pale orange, branching from card 1: heading 「所有権の保存」, line 「第74条　表題部所有者などが申請」
 - Milestone card 2 (blue): heading 「地目・地積の変更」, line 「第37条　変更の日から一月以内」
 - Milestone card 3 (blue): heading 「分筆・合筆」, line 「第39条　申請の期限の定めなし」, small tag 「合筆には制限がある　第41条」
 - Milestone card 4 (blue): heading 「滅失」, line 「第42条　滅失の日から一月以内」

--- FOOTER --- conclusion band: 「一月以内の登記と、期限の定めのない登記」

Words allowed on this poster (exactly these strings, nothing else): 「土地の一生を一本の線で」 / 「登記が起こす出来事を時間順に」 / 「表題登記」 / 「第36条　取得の日から一月以内」 / 「所有権の保存」 / 「第74条　表題部所有者などが申請」 / 「地目・地積の変更」 / 「第37条　変更の日から一月以内」 / 「分筆・合筆」 / 「第39条　申請の期限の定めなし」 / 「合筆には制限がある　第41条」 / 「滅失」 / 「第42条　滅失の日から一月以内」 / 「一月以内の登記と、期限の定めのない登記」

Final check before rendering: confirm the canvas is exactly 1080x1800 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 土、地、一、生、本、線、登、記、起、出、来、事、時、間、順、表、題、第、条、取、得、日、月、以、内、所、有、権、保、存、部、者、申、請、目、積、変、更、分、筆、合、期、限、定、制、滅、失.
```

### Instagram用（1080x1440・3:4）

```
Create a Japanese-language infographic, portrait layout, 1080x1440 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: a winding path with small signposts and milestones, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「土地の一生を一本の線で」 / subtitle band: 「登記が起こす出来事を時間順に」

--- BODY (one winding vertical path from top to bottom with four milestone cards on the path, and one side card branching off to the right after the first card) ---
 - Milestone card 1 (blue): heading 「表題登記」, line 「第36条　取得の日から一月以内」
 - Side card, pale orange, branching from card 1: heading 「所有権の保存」, line 「第74条　表題部所有者などが申請」
 - Milestone card 2 (blue): heading 「地目・地積の変更」, line 「第37条　変更の日から一月以内」
 - Milestone card 3 (blue): heading 「分筆・合筆」, line 「第39条　申請の期限の定めなし」, small tag 「合筆には制限がある　第41条」
 - Milestone card 4 (blue): heading 「滅失」, line 「第42条　滅失の日から一月以内」

--- FOOTER --- conclusion band: 「一月以内の登記と、期限の定めのない登記」

INSTAGRAM FEED FORMAT (critical): the canvas is EXACTLY 1080x1440 pixels (3:4). Keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom, because the profile grid crops the image. Make the type slightly larger than the note version and compress the spacing so that everything fits in 1440px of height. Do not draw any account name, handle, URL or call-to-action text.

Words allowed on this poster (exactly these strings, nothing else): 「土地の一生を一本の線で」 / 「登記が起こす出来事を時間順に」 / 「表題登記」 / 「第36条　取得の日から一月以内」 / 「所有権の保存」 / 「第74条　表題部所有者などが申請」 / 「地目・地積の変更」 / 「第37条　変更の日から一月以内」 / 「分筆・合筆」 / 「第39条　申請の期限の定めなし」 / 「合筆には制限がある　第41条」 / 「滅失」 / 「第42条　滅失の日から一月以内」 / 「一月以内の登記と、期限の定めのない登記」

Final check before rendering: confirm the canvas is exactly 1080x1440 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 土、地、一、生、本、線、登、記、起、出、来、事、時、間、順、表、題、第、条、取、得、日、月、以、内、所、有、権、保、存、部、者、申、請、目、積、変、更、分、筆、合、期、限、定、制、滅、失.
```

## 図2：建物の一生（zu02）

### note用（1080x1900）

```
Create a Japanese-language infographic, portrait layout, 1080x1900 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: a winding path with small signposts and milestones, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「建物の一生を一本の線で」 / subtitle band: 「順番は一例」

--- BODY (one winding vertical path from top to bottom with five milestone cards on the path, and one side card branching off to the right after the first card) ---
 - Milestone card 1 (blue): small text 「新築」, heading 「建物の表題登記」, line 「第47条　取得の日から一月以内」
 - Side card, pale orange, branching from card 1: heading 「所有権の保存」, line 「第74条　表題部所有者などが申請」
 - Milestone card 2 (blue): small text 「増築・用途や構造の変更」, heading 「表題部の変更」, line 「第51条　変更の日から一月以内」
 - Milestone card 3 (blue): heading 「分割・区分・合併」, line 「第54条　申請の期限の定めなし」, small tag 「合併には制限がある　第56条」
 - Milestone card 4 (blue): heading 「合体」, line 「第49条　合体の日から一月以内」
 - Milestone card 5 (blue): heading 「滅失」, line 「第57条　滅失の日から一月以内」

--- FOOTER --- conclusion band: 「一月以内の登記と、期限の定めのない登記」

Words allowed on this poster (exactly these strings, nothing else): 「建物の一生を一本の線で」 / 「順番は一例」 / 「新築」 / 「建物の表題登記」 / 「第47条　取得の日から一月以内」 / 「所有権の保存」 / 「第74条　表題部所有者などが申請」 / 「増築・用途や構造の変更」 / 「表題部の変更」 / 「第51条　変更の日から一月以内」 / 「分割・区分・合併」 / 「第54条　申請の期限の定めなし」 / 「合併には制限がある　第56条」 / 「合体」 / 「第49条　合体の日から一月以内」 / 「滅失」 / 「第57条　滅失の日から一月以内」 / 「一月以内の登記と、期限の定めのない登記」

Final check before rendering: confirm the canvas is exactly 1080x1900 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 建、物、一、生、本、線、順、番、例、新、築、表、題、登、記、第、条、取、得、日、月、以、内、所、有、権、保、存、部、者、申、請、増、用、途、構、造、変、更、分、割、区、合、併、期、限、定、制、体、滅、失.
```

### Instagram用（1080x1440・3:4）

```
Create a Japanese-language infographic, portrait layout, 1080x1440 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: a winding path with small signposts and milestones, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「建物の一生を一本の線で」 / subtitle band: 「順番は一例」

--- BODY (one winding vertical path from top to bottom with five milestone cards on the path, and one side card branching off to the right after the first card) ---
 - Milestone card 1 (blue): small text 「新築」, heading 「建物の表題登記」, line 「第47条　取得の日から一月以内」
 - Side card, pale orange, branching from card 1: heading 「所有権の保存」, line 「第74条　表題部所有者などが申請」
 - Milestone card 2 (blue): small text 「増築・用途や構造の変更」, heading 「表題部の変更」, line 「第51条　変更の日から一月以内」
 - Milestone card 3 (blue): heading 「分割・区分・合併」, line 「第54条　申請の期限の定めなし」, small tag 「合併には制限がある　第56条」
 - Milestone card 4 (blue): heading 「合体」, line 「第49条　合体の日から一月以内」
 - Milestone card 5 (blue): heading 「滅失」, line 「第57条　滅失の日から一月以内」

--- FOOTER --- conclusion band: 「一月以内の登記と、期限の定めのない登記」

INSTAGRAM FEED FORMAT (critical): the canvas is EXACTLY 1080x1440 pixels (3:4). Keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom, because the profile grid crops the image. Make the type slightly larger than the note version and compress the spacing so that everything fits in 1440px of height. Do not draw any account name, handle, URL or call-to-action text.

Words allowed on this poster (exactly these strings, nothing else): 「建物の一生を一本の線で」 / 「順番は一例」 / 「新築」 / 「建物の表題登記」 / 「第47条　取得の日から一月以内」 / 「所有権の保存」 / 「第74条　表題部所有者などが申請」 / 「増築・用途や構造の変更」 / 「表題部の変更」 / 「第51条　変更の日から一月以内」 / 「分割・区分・合併」 / 「第54条　申請の期限の定めなし」 / 「合併には制限がある　第56条」 / 「合体」 / 「第49条　合体の日から一月以内」 / 「滅失」 / 「第57条　滅失の日から一月以内」 / 「一月以内の登記と、期限の定めのない登記」

Final check before rendering: confirm the canvas is exactly 1080x1440 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 建、物、一、生、本、線、順、番、例、新、築、表、題、登、記、第、条、取、得、日、月、以、内、所、有、権、保、存、部、者、申、請、増、用、途、構、造、変、更、分、割、区、合、併、期、限、定、制、体、滅、失.
```

## 見出し画像

見出し画像（note用 1280x670・Instagram用 1080x1440）は `header-image-prompts.md`、キャプションは `instagram-captions.md`。
