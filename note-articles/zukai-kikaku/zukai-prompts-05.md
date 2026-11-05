# 記述式の「解く順番」図 図解画像のプロンプト（ChatGPT用・note用とInstagram用）

作成 2026-11-05（`src/gen_prompts.py` で作る。手で直さない）。記事 `05-kijutsu-tokujunban.md` に差し込む図2枚について、**note用（縦長・図ごとのサイズ）とInstagram用（1080×1350・4:5）の2種類**を用意した。

## 使い方

1. 図ごとに、noteに使うなら「note用」、Instagramに使うなら「Instagram用」のコードブロックを、そのままChatGPTに貼る。文字は同じで、大きさと余白だけ違う。
2. 画像の中に図番は入れない（管理番号は、PNG名と記事のマーカーだけ）。
3. 色の約束：**表示に関する登記＝青、権利に関する登記＝薄い橙**。ほかの色は意味を持たせない（手順は薄い黄と水色）。同じ企画の図を並べたとき、色がそろっているか確かめる。
4. ファイル名は、note用が `kz05_zu01.png` から、Instagram用が `kz05_ig01.png` から。
5. 直すときは、プロンプトの最後に「次の点だけを直して、ほかは変えない：…」と1文足して再生成する。

## 確かめること

- 大きさが指定どおりか（note用は図ごとに違う、Instagram用は1080×1350）。
- 文字が、各プロンプトの「Words allowed」と**1字ずつ**一致しているか（簡体字・繁体字になっていないか、余計な文字・数字がないか）。
- 条文番号・項番号が正しく出ているか。
- 図番（図1など）が画像に入っていないか。
- Instagram用は、文字と主要な絵が外側の余白（左右54px・上下68px）の内側にあるか。アカウント名・URLが入っていないか。
- 背景が不透明か。

文字が何度やっても崩れるときは、「Words allowed」の行を残したまま「No text」の版（文字なしの枠と絵だけ）を作らせて、文字はCanvaで入れる。

## 図の一覧

| 管理番号 | 内容 | note用のサイズ | Instagram用のサイズ |
|---|---|---|---|
| zu01 | 土地（第21問）の解く順番 | 1080x1800 | 1080x1350 |
| zu02 | 建物（第22問）の解く順番 | 1080x1800 | 1080x1350 |

## 図1：土地（第21問）の解く順番（zu01）

### note用（1080x1800）

```
Create a Japanese-language infographic, portrait layout, 1080x1800 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: a stopwatch and an answer sheet with a pencil, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「土地の記述式　解く順番」 / subtitle band: 「座標の前にできることから」

--- BODY (a vertical staircase of seven steps from top to bottom, each step a rounded card; the first three steps are light blue, the middle two are pale yellow, the last two are pale orange) ---
 - Step 1: heading 「問と注を先に読む」, line 「注は系統ごとに仕分ける」
 - Step 2: heading 「時系列メモ」, line 「期限と所有者を書き出す」
 - Step 3: heading 「座標に左右されない欄」, line 「記述問題と申請書の一部を先に」
 - Step 4: heading 「点を順に出す」, line 「放射と交点の計算」
 - Step 5: heading 「面積と公差の判定」, line 「地積更正の要否」
 - Step 6: heading 「地積測量図」, line 「作図に使う時間を先に決める」
 - Step 7: heading 「見直し」, line 「検算と書き漏れ」

--- FOOTER --- conclusion band: 「手が止まったら、書ける欄へ戻る」

Words allowed on this poster (exactly these strings, nothing else): 「土地の記述式　解く順番」 / 「座標の前にできることから」 / 「問と注を先に読む」 / 「注は系統ごとに仕分ける」 / 「時系列メモ」 / 「期限と所有者を書き出す」 / 「座標に左右されない欄」 / 「記述問題と申請書の一部を先に」 / 「点を順に出す」 / 「放射と交点の計算」 / 「面積と公差の判定」 / 「地積更正の要否」 / 「地積測量図」 / 「作図に使う時間を先に決める」 / 「見直し」 / 「検算と書き漏れ」 / 「手が止まったら、書ける欄へ戻る」

Final check before rendering: confirm the canvas is exactly 1080x1800 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 土、地、記、述、式、解、順、番、座、標、前、問、注、先、読、系、統、仕、分、時、列、期、限、所、有、者、書、出、左、右、欄、題、申、請、一、部、点、放、射、交、計、算、面、積、公、差、判、定、更、正、要、否、測、量、図、作、使、間、決、見、直、検、漏、手、止、戻.
```

### Instagram用（1080x1350・4:5）

```
Create a Japanese-language infographic, portrait layout, 1080x1350 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: a stopwatch and an answer sheet with a pencil, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「土地の記述式　解く順番」 / subtitle band: 「座標の前にできることから」

--- BODY (a vertical staircase of seven steps from top to bottom, each step a rounded card; the first three steps are light blue, the middle two are pale yellow, the last two are pale orange) ---
 - Step 1: heading 「問と注を先に読む」, line 「注は系統ごとに仕分ける」
 - Step 2: heading 「時系列メモ」, line 「期限と所有者を書き出す」
 - Step 3: heading 「座標に左右されない欄」, line 「記述問題と申請書の一部を先に」
 - Step 4: heading 「点を順に出す」, line 「放射と交点の計算」
 - Step 5: heading 「面積と公差の判定」, line 「地積更正の要否」
 - Step 6: heading 「地積測量図」, line 「作図に使う時間を先に決める」
 - Step 7: heading 「見直し」, line 「検算と書き漏れ」

--- FOOTER --- conclusion band: 「手が止まったら、書ける欄へ戻る」

INSTAGRAM FEED FORMAT (critical): the canvas is EXACTLY 1080x1350 pixels (4:5). Keep every text and every important drawing inside a safe margin of 54px on the left and right and 68px at the top and bottom, because the profile grid crops the image. Make the type slightly larger than the note version and compress the spacing so that everything fits in 1350px of height. BOTTOM ALIGNMENT (critical): the bottom edges of the cards or boxes must line up: the last card of every column (or the last row) ends on one and the same horizontal line at the bottom margin, cards in the same row have the same height, and the gaps between cards are equal; absorb any spare height inside the cards (larger illustration area, vertical centring, padding), never as a ragged gap under one column. Do not draw any account name, handle, URL or call-to-action text.

Words allowed on this poster (exactly these strings, nothing else): 「土地の記述式　解く順番」 / 「座標の前にできることから」 / 「問と注を先に読む」 / 「注は系統ごとに仕分ける」 / 「時系列メモ」 / 「期限と所有者を書き出す」 / 「座標に左右されない欄」 / 「記述問題と申請書の一部を先に」 / 「点を順に出す」 / 「放射と交点の計算」 / 「面積と公差の判定」 / 「地積更正の要否」 / 「地積測量図」 / 「作図に使う時間を先に決める」 / 「見直し」 / 「検算と書き漏れ」 / 「手が止まったら、書ける欄へ戻る」

Final check before rendering: confirm the canvas is exactly 1080x1350 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 土、地、記、述、式、解、順、番、座、標、前、問、注、先、読、系、統、仕、分、時、列、期、限、所、有、者、書、出、左、右、欄、題、申、請、一、部、点、放、射、交、計、算、面、積、公、差、判、定、更、正、要、否、測、量、図、作、使、間、決、見、直、検、漏、手、止、戻.
```

## 図2：建物（第22問）の解く順番（zu02）

### note用（1080x1800）

```
Create a Japanese-language infographic, portrait layout, 1080x1800 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: a stopwatch and an answer sheet with a pencil, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「建物の記述式　解く順番」 / subtitle band: 「求積と作図に時間を残す」

--- BODY (a vertical staircase of seven steps from top to bottom, each step a rounded card; the first three steps are light blue, the middle two are pale yellow, the last two are pale orange) ---
 - Step 1: heading 「問とただし書きを先に読む」, line 「書き方の指示を見落とさない」
 - Step 2: heading 「事実関係と登記記録」, line 「時系列メモと申請の期限」
 - Step 3: heading 「登記記録を写す欄」, line 「写すだけの欄から埋める」
 - Step 4: heading 「求積」, line 「壁心か内法かを確かめる」
 - Step 5: heading 「作図」, line 「建物図面と各階平面図」
 - Step 6: heading 「問の穴埋め」, line 「最後に回すが、時間は残す」
 - Step 7: heading 「見直し」, line 「検算と書き漏れ」

--- FOOTER --- conclusion band: 「いちばん重いのは、求積と作図」

Words allowed on this poster (exactly these strings, nothing else): 「建物の記述式　解く順番」 / 「求積と作図に時間を残す」 / 「問とただし書きを先に読む」 / 「書き方の指示を見落とさない」 / 「事実関係と登記記録」 / 「時系列メモと申請の期限」 / 「登記記録を写す欄」 / 「写すだけの欄から埋める」 / 「求積」 / 「壁心か内法かを確かめる」 / 「作図」 / 「建物図面と各階平面図」 / 「問の穴埋め」 / 「最後に回すが、時間は残す」 / 「見直し」 / 「検算と書き漏れ」 / 「いちばん重いのは、求積と作図」

Final check before rendering: confirm the canvas is exactly 1080x1800 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 建、物、記、述、式、解、順、番、求、積、作、図、時、間、残、問、書、先、読、方、指、示、見、落、事、実、関、係、登、録、系、列、申、請、期、限、写、欄、埋、壁、心、内、法、確、面、各、階、平、穴、最、後、回、直、検、算、漏、重.
```

### Instagram用（1080x1350・4:5）

```
Create a Japanese-language infographic, portrait layout, 1080x1350 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: a stopwatch and an answer sheet with a pencil, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「建物の記述式　解く順番」 / subtitle band: 「求積と作図に時間を残す」

--- BODY (a vertical staircase of seven steps from top to bottom, each step a rounded card; the first three steps are light blue, the middle two are pale yellow, the last two are pale orange) ---
 - Step 1: heading 「問とただし書きを先に読む」, line 「書き方の指示を見落とさない」
 - Step 2: heading 「事実関係と登記記録」, line 「時系列メモと申請の期限」
 - Step 3: heading 「登記記録を写す欄」, line 「写すだけの欄から埋める」
 - Step 4: heading 「求積」, line 「壁心か内法かを確かめる」
 - Step 5: heading 「作図」, line 「建物図面と各階平面図」
 - Step 6: heading 「問の穴埋め」, line 「最後に回すが、時間は残す」
 - Step 7: heading 「見直し」, line 「検算と書き漏れ」

--- FOOTER --- conclusion band: 「いちばん重いのは、求積と作図」

INSTAGRAM FEED FORMAT (critical): the canvas is EXACTLY 1080x1350 pixels (4:5). Keep every text and every important drawing inside a safe margin of 54px on the left and right and 68px at the top and bottom, because the profile grid crops the image. Make the type slightly larger than the note version and compress the spacing so that everything fits in 1350px of height. BOTTOM ALIGNMENT (critical): the bottom edges of the cards or boxes must line up: the last card of every column (or the last row) ends on one and the same horizontal line at the bottom margin, cards in the same row have the same height, and the gaps between cards are equal; absorb any spare height inside the cards (larger illustration area, vertical centring, padding), never as a ragged gap under one column. Do not draw any account name, handle, URL or call-to-action text.

Words allowed on this poster (exactly these strings, nothing else): 「建物の記述式　解く順番」 / 「求積と作図に時間を残す」 / 「問とただし書きを先に読む」 / 「書き方の指示を見落とさない」 / 「事実関係と登記記録」 / 「時系列メモと申請の期限」 / 「登記記録を写す欄」 / 「写すだけの欄から埋める」 / 「求積」 / 「壁心か内法かを確かめる」 / 「作図」 / 「建物図面と各階平面図」 / 「問の穴埋め」 / 「最後に回すが、時間は残す」 / 「見直し」 / 「検算と書き漏れ」 / 「いちばん重いのは、求積と作図」

Final check before rendering: confirm the canvas is exactly 1080x1350 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 建、物、記、述、式、解、順、番、求、積、作、図、時、間、残、問、書、先、読、方、指、示、見、落、事、実、関、係、登、録、系、列、申、請、期、限、写、欄、埋、壁、心、内、法、確、面、各、階、平、穴、最、後、回、直、検、算、漏、重.
```

## 見出し画像

見出し画像（note用 1280x670・Instagram用 1080x1350）は `header-image-prompts.md`、キャプションは `instagram-captions.md`。
