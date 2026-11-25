# 第9回「申請人がいないとき・違うとき」図解・間違いノートのプロンプト

`src/build.py` が `src/d09.py` から作る（手で直さない）。画像の生成はChatGPTで行う。各図に note用（縦長）と Instagram用（1080×1440）の2つがある。文字はどちらも同じで、大きさと余白だけ違う。

## 確かめること

- 文字が「」の中と1字ずつ一致しているか（簡体字・繁体字・余計な文字がないか）。図番が入っていないか。
- ○（正しい）は青、×（思い込み）は赤。1つの箱に○と×が両方入っていないか。
- 背景が不透明か。直すときは、プロンプトの最後に「次の点だけを直して、ほかは変えない：…」と1文足す。

## 図の一覧

- `jg09_soron.png`（Instagram用 `jg09_soron_ig.png`）：総論：申請人がいないとき・違うとき
- `jg09_kakuron01.png`（Instagram用 `jg09_kakuron01_ig.png`）：各論：名義人が亡くなったら
- `jg09_kakuron02.png`（Instagram用 `jg09_kakuron02_ig.png`）：各論：表題部所有者の更正は誰が申請するか
- `jg09_kakuron03.png`（Instagram用 `jg09_kakuron03_ig.png`）：各論：代位で申請できる人・できない人
- `jg09_machigai01.png`（Instagram用 `jg09_machigai01_ig.png`）：間違いノート：相続の登記をしてからでないと、表示の登記はできない？
- `jg09_machigai02.png`（Instagram用 `jg09_machigai02_ig.png`）：間違いノート：持分の更正は、共有者全員の承諾が要る？
- `jg09_machigai03.png`（Instagram用 `jg09_machigai03_ig.png`）：間違いノート：誤って登記された本人が、更正を申請できる？
- `jg09_machigai04.png`（Instagram用 `jg09_machigai04_ig.png`）：間違いノート：買った人なら、いつでも代位で分筆できる？

## 総論：申請人がいないとき・違うとき

### note用（`jg09_soron.png`）

```
Create a Japanese-language infographic poster, portrait layout, 1080x1920 pixels,
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. Use a warm library and bookshelf motif for the frame, drawn simply.

GLANCEABLE-POSTER REQUIREMENT: each card shows only its heading, one illustration and one short conclusion tag; no sentences, no quoted article text inside the cards.

LAYOUT LOCK (critical): keep the header exactly as fixed below; align the bottom edges of cards placed side by side on the same baseline and absorb spare height inside the cards; when there are five cards, place cards 1 to 4 in a 2x2 grid and card 5 as one full-width card; never leave an empty grid cell.

HEADER LOCK (critical): the header is a fixed block of exactly THREE centred lines at the top, measured on a 1080 px wide canvas (the pixel values are the same for every canvas height), in a heavy rounded Japanese gothic (Noto Sans JP Black / ExtraBold style), near-black (#1A1A1A) on the plain cream background (#F7F3EE). Do not draw a band, frame or box behind the header.
  Line 1 = the first Title line (the question title): font size 62 px, about 800 px wide (about 74% of the canvas width), vertical centre at y = 80 px. The title must stay on ONE line (never wrap it into two lines): if it would be wider than 990 px, reduce the font size until it fits on that one line (not below 36 px).
  Line 2 = the second Title line (the topic list): font size 45 px, one line only, about 990 px wide (about 92% of the canvas width, left and right ends about 45 px from the edges); if the text would be wider than 990 px, reduce the font size until it fits (not below 36 px), never wrap it; vertical centre at y = 148 px.
  Line 3 = the Subtitle (the year and question number only, e.g. 令和3年度 第3問; never write 午後の部 or 午前の部): font size 35 px, about 330 px wide, vertical centre at y = 204 px.
  The line pitch is 68 px (line 1 to line 2) and 56 px (line 2 to line 3); the three lines are tightly stacked with no empty gap between them. The whole header block runs from y = 48 px (top of line 1) to y = 223 px (bottom of line 3), i.e. about 175 px tall, and the first group header or card starts at y = 245 px. There is NO empty band above line 1 and NO empty band between line 3 and the first group header or card. Do not enlarge any header line to fill space.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title line 1: 「申請人がいないとき・違うとき」
Title line 2: 「相続人・表題部所有者の更正・代位」
Subtitle: 「条文の逆引き図鑑 第9回」


--- CARDS (each card: a short heading, a simple illustration, and one short conclusion tag; no sentences) ---
Card 1: heading 「名義人が死亡」; illustration: a registry book with a ribbon of mourning, and an heir holding a form beside it; conclusion tag 「相続人がそのまま申請」
Card 2: heading 「相続の登記は」; illustration: a crossed-out step on a staircase labeled with a house icon; conclusion tag 「先にしなくてよい」
Card 3: heading 「表題部所有者の誤り」; illustration: two name cards, one crossed out, with an arrow to the correct one and a small seal of consent; conclusion tag 「真の所有者が承諾を得て」
Card 4: heading 「持分の誤り」; illustration: two pie charts with slightly different slices and a small seal of consent; conclusion tag 「持分が変わる人の承諾」
Card 5: heading 「代位」; illustration: a person stepping in front of another person to hand in a form; conclusion tag 「守るべき権利があるとき」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 図、変、所、権、登、続、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; Confirm the header is the fixed block described in HEADER LOCK (three centred lines of 62 / 45 / 35 px at y = 80 / 148 / 204 px, no 午後の部 or 午前の部, no empty gap or band, first card at y = 245 px). confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg09_soron_ig.png`）

```
Create a Japanese-language infographic poster for an Instagram feed image, 1080x1440 pixels (3:4 portrait). Keep 54px side margins and 72px top and bottom margins free of text.
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. Use a warm library and bookshelf motif for the frame, drawn simply.

GLANCEABLE-POSTER REQUIREMENT: each card shows only its heading, one illustration and one short conclusion tag; no sentences, no quoted article text inside the cards.

LAYOUT LOCK (critical): keep the header exactly as fixed below; align the bottom edges of cards placed side by side on the same baseline and absorb spare height inside the cards; when there are five cards, place cards 1 to 4 in a 2x2 grid and card 5 as one full-width card; never leave an empty grid cell.

HEADER LOCK (critical): the header is a fixed block of exactly THREE centred lines at the top, measured on a 1080 px wide canvas (the pixel values are the same for every canvas height), in a heavy rounded Japanese gothic (Noto Sans JP Black / ExtraBold style), near-black (#1A1A1A) on the plain cream background (#F7F3EE). Do not draw a band, frame or box behind the header.
  Line 1 = the first Title line (the question title): font size 62 px, about 800 px wide (about 74% of the canvas width), vertical centre at y = 80 px. The title must stay on ONE line (never wrap it into two lines): if it would be wider than 990 px, reduce the font size until it fits on that one line (not below 36 px).
  Line 2 = the second Title line (the topic list): font size 45 px, one line only, about 990 px wide (about 92% of the canvas width, left and right ends about 45 px from the edges); if the text would be wider than 990 px, reduce the font size until it fits (not below 36 px), never wrap it; vertical centre at y = 148 px.
  Line 3 = the Subtitle (the year and question number only, e.g. 令和3年度 第3問; never write 午後の部 or 午前の部): font size 35 px, about 330 px wide, vertical centre at y = 204 px.
  The line pitch is 68 px (line 1 to line 2) and 56 px (line 2 to line 3); the three lines are tightly stacked with no empty gap between them. The whole header block runs from y = 48 px (top of line 1) to y = 223 px (bottom of line 3), i.e. about 175 px tall, and the first group header or card starts at y = 245 px. There is NO empty band above line 1 and NO empty band between line 3 and the first group header or card. Do not enlarge any header line to fill space.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title line 1: 「申請人がいないとき・違うとき」
Title line 2: 「相続人・表題部所有者の更正・代位」
Subtitle: 「条文の逆引き図鑑 第9回」


--- CARDS (each card: a short heading, a simple illustration, and one short conclusion tag; no sentences) ---
Card 1: heading 「名義人が死亡」; illustration: a registry book with a ribbon of mourning, and an heir holding a form beside it; conclusion tag 「相続人がそのまま申請」
Card 2: heading 「相続の登記は」; illustration: a crossed-out step on a staircase labeled with a house icon; conclusion tag 「先にしなくてよい」
Card 3: heading 「表題部所有者の誤り」; illustration: two name cards, one crossed out, with an arrow to the correct one and a small seal of consent; conclusion tag 「真の所有者が承諾を得て」
Card 4: heading 「持分の誤り」; illustration: two pie charts with slightly different slices and a small seal of consent; conclusion tag 「持分が変わる人の承諾」
Card 5: heading 「代位」; illustration: a person stepping in front of another person to hand in a form; conclusion tag 「守るべき権利があるとき」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 図、変、所、権、登、続、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; Confirm the header is the fixed block described in HEADER LOCK (three centred lines of 62 / 45 / 35 px at y = 80 / 148 / 204 px, no 午後の部 or 午前の部, no empty gap or band, first card at y = 245 px). confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 各論：名義人が亡くなったら

### note用（`jg09_kakuron01.png`）

```
Create a Japanese-language explainer infographic, portrait layout, 1080x1500 pixels,
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「名義人が亡くなったら」
Subtitle (smaller, in a pale-yellow band): 「第30条」


--- BODY ---
Top: a registry book with a small black ribbon (the registered owner has died), with an arrow to an heir holding a form, labeled 「相続人がそのまま申請できる」.
Middle: a short staircase of two steps, the first step 「相続の登記」 crossed out with a red line, and an arrow skipping directly to 「表示の登記（分筆・合併・滅失・変更）」, labeled 「先にしなくてよい」.
Lower left: a card 「相続人が複数でも1人から」.
Lower right: a card 「遺産の分割の禁止があっても分筆はできる」.
Bottom: a note 「申請情報に相続人である旨を書く（一覧図の写しを付けても書く）」.

--- FOOTER ---
Small note at the bottom: 「不動産登記法第30条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 図、変、滅、産、登、筆、続、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg09_kakuron01_ig.png`）

```
Create a Japanese-language explainer infographic for an Instagram feed image, 1080x1440 pixels (3:4 portrait). Keep 54px side margins and 72px top and bottom margins free of text.
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「名義人が亡くなったら」
Subtitle (smaller, in a pale-yellow band): 「第30条」


--- BODY ---
Top: a registry book with a small black ribbon (the registered owner has died), with an arrow to an heir holding a form, labeled 「相続人がそのまま申請できる」.
Middle: a short staircase of two steps, the first step 「相続の登記」 crossed out with a red line, and an arrow skipping directly to 「表示の登記（分筆・合併・滅失・変更）」, labeled 「先にしなくてよい」.
Lower left: a card 「相続人が複数でも1人から」.
Lower right: a card 「遺産の分割の禁止があっても分筆はできる」.
Bottom: a note 「申請情報に相続人である旨を書く（一覧図の写しを付けても書く）」.

--- FOOTER ---
Small note at the bottom: 「不動産登記法第30条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 図、変、滅、産、登、筆、続、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 各論：表題部所有者の更正は誰が申請するか

### note用（`jg09_kakuron02.png`）

```
Create a Japanese-language explainer infographic, portrait layout, 1080x1500 pixels,
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「表題部所有者の更正は誰が申請するか」
Subtitle (smaller, in a pale-yellow band): 「第33条」


--- BODY ---
Two panels side by side.
Left panel 「所有者そのものの誤り」: a registry card with a wrong name crossed out, a person 「真の所有者」 holding a form with a blue check 「申請できる」, a small seal icon 「誤って登記された人の承諾（または裁判）」, and the wrongly registered person with a red cross 「申請できない」.
Right panel 「共有者の持分の誤り」: three person icons with pie charts, one of them holding a form 「共有者の1人から申請できる」; the two whose slices change have seal icons 「承諾が要る」, the one whose slice does not change has a gray tag 「承諾は要らない」.

--- FOOTER ---
Small note at the bottom: 「不動産登記法第33条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 所、産、登、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg09_kakuron02_ig.png`）

```
Create a Japanese-language explainer infographic for an Instagram feed image, 1080x1440 pixels (3:4 portrait). Keep 54px side margins and 72px top and bottom margins free of text.
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「表題部所有者の更正は誰が申請するか」
Subtitle (smaller, in a pale-yellow band): 「第33条」


--- BODY ---
Two panels side by side.
Left panel 「所有者そのものの誤り」: a registry card with a wrong name crossed out, a person 「真の所有者」 holding a form with a blue check 「申請できる」, a small seal icon 「誤って登記された人の承諾（または裁判）」, and the wrongly registered person with a red cross 「申請できない」.
Right panel 「共有者の持分の誤り」: three person icons with pie charts, one of them holding a form 「共有者の1人から申請できる」; the two whose slices change have seal icons 「承諾が要る」, the one whose slice does not change has a gray tag 「承諾は要らない」.

--- FOOTER ---
Small note at the bottom: 「不動産登記法第33条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 所、産、登、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 各論：代位で申請できる人・できない人

### note用（`jg09_kakuron03.png`）

```
Create a Japanese-language explainer infographic, portrait layout, 1080x1500 pixels,
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「代位で申請できる人・できない人」
Subtitle (smaller, in a pale-yellow band): 「民法第423条」


--- BODY ---
Top: a question card 「自分の権利を守るために、その登記が必要か」.
Two columns below.
 Left column, blue header 「必要＝代位できる」: cards 「土地の一部を買った人（分筆）」, 「附属建物だけを買った人（分割）」, 「一部の処分禁止の仮処分の債権者」, 「共有物分割の判決が確定した共有者」, 「区分建物を買った人（表題登記）」.
 Right column, red header 「不要＝代位できない」: cards 「土地の全部を買った人」, 「合筆して売る約束の買主」, 「一部に地役権の設定を受けた人」, 「共有の一部の持分を買った人」.
Bottom: a note 「代位原因と、それを証する情報を出す」.

--- FOOTER ---
Small note at the bottom: 「民法第423条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 区、地、建、権、物、登、筆、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg09_kakuron03_ig.png`）

```
Create a Japanese-language explainer infographic for an Instagram feed image, 1080x1440 pixels (3:4 portrait). Keep 54px side margins and 72px top and bottom margins free of text.
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「代位で申請できる人・できない人」
Subtitle (smaller, in a pale-yellow band): 「民法第423条」


--- BODY ---
Top: a question card 「自分の権利を守るために、その登記が必要か」.
Two columns below.
 Left column, blue header 「必要＝代位できる」: cards 「土地の一部を買った人（分筆）」, 「附属建物だけを買った人（分割）」, 「一部の処分禁止の仮処分の債権者」, 「共有物分割の判決が確定した共有者」, 「区分建物を買った人（表題登記）」.
 Right column, red header 「不要＝代位できない」: cards 「土地の全部を買った人」, 「合筆して売る約束の買主」, 「一部に地役権の設定を受けた人」, 「共有の一部の持分を買った人」.
Bottom: a note 「代位原因と、それを証する情報を出す」.

--- FOOTER ---
Small note at the bottom: 「民法第423条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 区、地、建、権、物、登、筆、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 間違いノート：相続の登記をしてからでないと、表示の登記はできない？

### note用（`jg09_machigai01.png`）

```
Create a Japanese-language infographic, portrait layout, 1080x1920 pixels,
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. Use a notebook-page motif (a ruled notebook page with a red margin line).

MISTAKE-NOTEBOOK EXPLAINER REQUIREMENT: this image resolves one specific point of confusion; written conditions in the flow and a 1-3 sentence callout are allowed. Prioritize clarity of the reasoning.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「相続の登記をしてからでないと、表示の登記はできない？」
Subtitle (smaller): 「相続人がそのまま申請できる」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「名義人が亡くなったら、まず相続による所有権の移転の登記をして、そのあとで合併や滅失の登記を申請する。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「第30条により、相続人は相続の登記をしないまま表示の登記を申請できる。相続人が複数でも、その1人から申請できる。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「申請するのが表示の登記か、権利の登記かを見る」
  Step box 2: 「表示の登記なら、相続人が被相続人名義のまま申請できる」
  Step box 3: 「申請情報には、相続人である旨を書く」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「肢に『相続による所有権の移転の登記をした後でなければ』と書いてあったら、表示の登記ではほぼ誤りです。」

--- FOOTER ---
Small note: 「不動産登記法第30条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 所、権、滅、産、登、続、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg09_machigai01_ig.png`）

```
Create a Japanese-language infographic for an Instagram feed image, 1080x1440 pixels (3:4 portrait). Keep 54px side margins and 72px top and bottom margins free of text.
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. Use a notebook-page motif (a ruled notebook page with a red margin line).

MISTAKE-NOTEBOOK EXPLAINER REQUIREMENT: this image resolves one specific point of confusion; written conditions in the flow and a 1-3 sentence callout are allowed. Prioritize clarity of the reasoning.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「相続の登記をしてからでないと、表示の登記はできない？」
Subtitle (smaller): 「相続人がそのまま申請できる」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「名義人が亡くなったら、まず相続による所有権の移転の登記をして、そのあとで合併や滅失の登記を申請する。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「第30条により、相続人は相続の登記をしないまま表示の登記を申請できる。相続人が複数でも、その1人から申請できる。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「申請するのが表示の登記か、権利の登記かを見る」
  Step box 2: 「表示の登記なら、相続人が被相続人名義のまま申請できる」
  Step box 3: 「申請情報には、相続人である旨を書く」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「肢に『相続による所有権の移転の登記をした後でなければ』と書いてあったら、表示の登記ではほぼ誤りです。」

--- FOOTER ---
Small note: 「不動産登記法第30条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 所、権、滅、産、登、続、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 間違いノート：持分の更正は、共有者全員の承諾が要る？

### note用（`jg09_machigai02.png`）

```
Create a Japanese-language infographic, portrait layout, 1080x1920 pixels,
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. Use a notebook-page motif (a ruled notebook page with a red margin line).

MISTAKE-NOTEBOOK EXPLAINER REQUIREMENT: this image resolves one specific point of confusion; written conditions in the flow and a 1-3 sentence callout are allowed. Prioritize clarity of the reasoning.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「持分の更正は、共有者全員の承諾が要る？」
Subtitle (smaller): 「持分が変わる人の承諾だけ」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「3人の共有のうち2人の持分を入れ替える更正は、残りの1人を含めた全員の承諾が要る。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「承諾が要るのは、更正で持分が変わる他の共有者だけ。持分が変わらない共有者の承諾は要らない。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「更正の前と後の持分を、共有者ごとに並べる」
  Step box 2: 「持分が変わる共有者に印を付ける」
  Step box 3: 「申請する共有者以外で印のついた人の承諾を付ける」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「第33条第4項は『その持分を更正することとなる他の共有者』の承諾。持分が変わらない人は入りません。」

--- FOOTER ---
Small note: 「不動産登記法第33条第4項」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 変、産、登、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg09_machigai02_ig.png`）

```
Create a Japanese-language infographic for an Instagram feed image, 1080x1440 pixels (3:4 portrait). Keep 54px side margins and 72px top and bottom margins free of text.
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. Use a notebook-page motif (a ruled notebook page with a red margin line).

MISTAKE-NOTEBOOK EXPLAINER REQUIREMENT: this image resolves one specific point of confusion; written conditions in the flow and a 1-3 sentence callout are allowed. Prioritize clarity of the reasoning.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「持分の更正は、共有者全員の承諾が要る？」
Subtitle (smaller): 「持分が変わる人の承諾だけ」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「3人の共有のうち2人の持分を入れ替える更正は、残りの1人を含めた全員の承諾が要る。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「承諾が要るのは、更正で持分が変わる他の共有者だけ。持分が変わらない共有者の承諾は要らない。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「更正の前と後の持分を、共有者ごとに並べる」
  Step box 2: 「持分が変わる共有者に印を付ける」
  Step box 3: 「申請する共有者以外で印のついた人の承諾を付ける」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「第33条第4項は『その持分を更正することとなる他の共有者』の承諾。持分が変わらない人は入りません。」

--- FOOTER ---
Small note: 「不動産登記法第33条第4項」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 変、産、登、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 間違いノート：誤って登記された本人が、更正を申請できる？

### note用（`jg09_machigai03.png`）

```
Create a Japanese-language infographic, portrait layout, 1080x1920 pixels,
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. Use a notebook-page motif (a ruled notebook page with a red margin line).

MISTAKE-NOTEBOOK EXPLAINER REQUIREMENT: this image resolves one specific point of confusion; written conditions in the flow and a 1-3 sentence callout are allowed. Prioritize clarity of the reasoning.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「誤って登記された本人が、更正を申請できる？」
Subtitle (smaller): 「申請できるのは真の所有者」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「自分が誤って表題部所有者として登記されているので、自分から表題部所有者の更正の登記を申請できる。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「表題部所有者そのものの更正を申請できるのは、真の所有者だけ。誤って登記されている人の承諾（または裁判）を得て申請する。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「誤っているのが『所有者そのもの』か『共有者の持分』かを見る」
  Step box 2: 「所有者そのものなら、申請するのは真の所有者」
  Step box 3: 「共有者の持分なら、表題部所有者である共有者が申請する」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「第1項と第3項で、申請できる人が入れ替わります。『誰が』を条文の項ごとに確かめます。」

--- FOOTER ---
Small note: 「不動産登記法第33条第1項・第2項」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 所、産、登、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg09_machigai03_ig.png`）

```
Create a Japanese-language infographic for an Instagram feed image, 1080x1440 pixels (3:4 portrait). Keep 54px side margins and 72px top and bottom margins free of text.
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. Use a notebook-page motif (a ruled notebook page with a red margin line).

MISTAKE-NOTEBOOK EXPLAINER REQUIREMENT: this image resolves one specific point of confusion; written conditions in the flow and a 1-3 sentence callout are allowed. Prioritize clarity of the reasoning.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「誤って登記された本人が、更正を申請できる？」
Subtitle (smaller): 「申請できるのは真の所有者」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「自分が誤って表題部所有者として登記されているので、自分から表題部所有者の更正の登記を申請できる。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「表題部所有者そのものの更正を申請できるのは、真の所有者だけ。誤って登記されている人の承諾（または裁判）を得て申請する。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「誤っているのが『所有者そのもの』か『共有者の持分』かを見る」
  Step box 2: 「所有者そのものなら、申請するのは真の所有者」
  Step box 3: 「共有者の持分なら、表題部所有者である共有者が申請する」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「第1項と第3項で、申請できる人が入れ替わります。『誰が』を条文の項ごとに確かめます。」

--- FOOTER ---
Small note: 「不動産登記法第33条第1項・第2項」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 所、産、登、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 間違いノート：買った人なら、いつでも代位で分筆できる？

### note用（`jg09_machigai04.png`）

```
Create a Japanese-language infographic, portrait layout, 1080x1920 pixels,
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. Use a notebook-page motif (a ruled notebook page with a red margin line).

MISTAKE-NOTEBOOK EXPLAINER REQUIREMENT: this image resolves one specific point of confusion; written conditions in the flow and a 1-3 sentence callout are allowed. Prioritize clarity of the reasoning.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「買った人なら、いつでも代位で分筆できる？」
Subtitle (smaller): 「その登記が必要なときだけ」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「土地を買った人や地役権の設定を受けた人は、売主に代位して分筆の登記を申請できる。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「代位できるのは、自分の権利を守るためにその登記が必要なときだけ。全部を買った人・一部に地役権を受けた人・持分を買った人には分筆が要らないので、代位できない。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「その人が、どんな登記をしたいのかを確かめる」
  Step box 2: 「その登記をするのに、分筆・分割・合筆が欠かせないかを見る」
  Step box 3: 「欠かせないなら代位できる、要らないなら代位できない」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「地役権は土地の一部にも設定でき、そのまま登記できます（範囲を書けばよい）。だから分筆を代位する必要がありません。」

--- FOOTER ---
Small note: 「民法第423条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地、権、登、筆、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg09_machigai04_ig.png`）

```
Create a Japanese-language infographic for an Instagram feed image, 1080x1440 pixels (3:4 portrait). Keep 54px side margins and 72px top and bottom margins free of text.
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. Use a notebook-page motif (a ruled notebook page with a red margin line).

MISTAKE-NOTEBOOK EXPLAINER REQUIREMENT: this image resolves one specific point of confusion; written conditions in the flow and a 1-3 sentence callout are allowed. Prioritize clarity of the reasoning.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「買った人なら、いつでも代位で分筆できる？」
Subtitle (smaller): 「その登記が必要なときだけ」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「土地を買った人や地役権の設定を受けた人は、売主に代位して分筆の登記を申請できる。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「代位できるのは、自分の権利を守るためにその登記が必要なときだけ。全部を買った人・一部に地役権を受けた人・持分を買った人には分筆が要らないので、代位できない。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「その人が、どんな登記をしたいのかを確かめる」
  Step box 2: 「その登記をするのに、分筆・分割・合筆が欠かせないかを見る」
  Step box 3: 「欠かせないなら代位できる、要らないなら代位できない」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「地役権は土地の一部にも設定でき、そのまま登記できます（範囲を書けばよい）。だから分筆を代位する必要がありません。」

--- FOOTER ---
Small note: 「民法第423条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地、権、登、筆、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```
