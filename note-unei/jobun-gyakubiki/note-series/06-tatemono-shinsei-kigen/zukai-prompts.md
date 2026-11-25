# 第6回「建物の表題登記・変更・滅失は「誰が・いつから1か月」」図解・間違いノートのプロンプト

`src/build.py` が `src/d06.py` から作る（手で直さない）。画像の生成はChatGPTで行う。各図に note用（縦長）と Instagram用（1080×1440）の2つがある。文字はどちらも同じで、大きさと余白だけ違う。

## 確かめること

- 文字が「」の中と1字ずつ一致しているか（簡体字・繁体字・余計な文字がないか）。図番が入っていないか。
- ○（正しい）は青、×（思い込み）は赤。1つの箱に○と×が両方入っていないか。
- 背景が不透明か。直すときは、プロンプトの最後に「次の点だけを直して、ほかは変えない：…」と1文足す。

## 図の一覧

- `jg06_soron.png`（Instagram用 `jg06_soron_ig.png`）：総論：建物の登記の申請と1か月の期限
- `jg06_kakuron01.png`（Instagram用 `jg06_kakuron01_ig.png`）：各論：表題登記は誰の名前で、いつまでに
- `jg06_kakuron02.png`（Instagram用 `jg06_kakuron02_ig.png`）：各論：表題部の変更の登記の起算点
- `jg06_kakuron03.png`（Instagram用 `jg06_kakuron03_ig.png`）：各論：滅失の登記を申請する人
- `jg06_machigai01.png`（Instagram用 `jg06_machigai01_ig.png`）：間違いノート：1か月は、前の持ち主の新築の日から？
- `jg06_machigai02.png`（Instagram用 `jg06_machigai02_ig.png`）：間違いノート：区分建物も、買った人の名前で表題登記？
- `jg06_machigai03.png`（Instagram用 `jg06_machigai03_ig.png`）：間違いノート：土地の所有者も、滅失の登記を申請できる？

## 総論：建物の登記の申請と1か月の期限

### note用（`jg06_soron.png`）

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
Title line 1: 「建物の登記の申請と1か月の期限」
Title line 2: 「表題登記・表題部の変更・滅失・区分建物の特則」
Subtitle: 「条文の逆引き図鑑 第6回」


--- CARDS (each card: a short heading, a simple illustration, and one short conclusion tag; no sentences) ---
Card 1: heading 「表題登記」; illustration: a newly built house with a calendar page and a circled month; conclusion tag 「取得の日から1か月」
Card 2: heading 「表題部の変更」; illustration: a house with an extension being added, and a calendar page; conclusion tag 「変わった日から1か月」
Card 3: heading 「滅失」; illustration: a house being torn down, and a calendar page; conclusion tag 「滅失の日から1か月」
Card 4: heading 「区分建物」; illustration: a small apartment building with a name card of the original builder held up in front; conclusion tag 「最初に建てた人の名前で」
Card 5: heading 「申請する人」; illustration: a house with its owner name card, and a crossed-out landowner card beside it; conclusion tag 「建物の所有者の側」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、区、図、変、建、所、滅、物、登、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; Confirm the header is the fixed block described in HEADER LOCK (three centred lines of 62 / 45 / 35 px at y = 80 / 148 / 204 px, no 午後の部 or 午前の部, no empty gap or band, first card at y = 245 px). confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg06_soron_ig.png`）

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
Title line 1: 「建物の登記の申請と1か月の期限」
Title line 2: 「表題登記・表題部の変更・滅失・区分建物の特則」
Subtitle: 「条文の逆引き図鑑 第6回」


--- CARDS (each card: a short heading, a simple illustration, and one short conclusion tag; no sentences) ---
Card 1: heading 「表題登記」; illustration: a newly built house with a calendar page and a circled month; conclusion tag 「取得の日から1か月」
Card 2: heading 「表題部の変更」; illustration: a house with an extension being added, and a calendar page; conclusion tag 「変わった日から1か月」
Card 3: heading 「滅失」; illustration: a house being torn down, and a calendar page; conclusion tag 「滅失の日から1か月」
Card 4: heading 「区分建物」; illustration: a small apartment building with a name card of the original builder held up in front; conclusion tag 「最初に建てた人の名前で」
Card 5: heading 「申請する人」; illustration: a house with its owner name card, and a crossed-out landowner card beside it; conclusion tag 「建物の所有者の側」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、区、図、変、建、所、滅、物、登、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; Confirm the header is the fixed block described in HEADER LOCK (three centred lines of 62 / 45 / 35 px at y = 80 / 148 / 204 px, no 午後の部 or 午前の部, no empty gap or band, first card at y = 245 px). confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 各論：表題登記は誰の名前で、いつまでに

### note用（`jg06_kakuron01.png`）

```
Create a Japanese-language explainer infographic, portrait layout, 1080x1500 pixels,
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「表題登記は誰の名前で、いつまでに」
Subtitle (smaller, in a pale-yellow band): 「第47条」


--- BODY ---
Two columns side by side.
Left column, header 「区分建物でない建物」: a timeline 「新築または取得の日」 → 「1か月以内」 → 「表題登記」; below it two person cards 「新築した人」「買った人」 each with a blue check 「自分の名前で」; a small note 「相続人も自分の名前で」.
Right column, header 「区分建物」: a large name card 「最初に建てた人（原始取得者）の名前で」; below it three small rows: 「買った人：自分の名前ではできない（代位はできる）」, 「相続人・合併後の会社：被承継人の名前で申請できる」, 「買った人に1か月の義務はない」.
Bottom: a yellow note 「1か月は前の持ち主の新築の日からではない」.

--- FOOTER ---
Small note at the bottom: 「不動産登記法第47条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 区、建、物、産、登、続、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg06_kakuron01_ig.png`）

```
Create a Japanese-language explainer infographic for an Instagram feed image, 1080x1440 pixels (3:4 portrait). Keep 54px side margins and 72px top and bottom margins free of text.
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「表題登記は誰の名前で、いつまでに」
Subtitle (smaller, in a pale-yellow band): 「第47条」


--- BODY ---
Two columns side by side.
Left column, header 「区分建物でない建物」: a timeline 「新築または取得の日」 → 「1か月以内」 → 「表題登記」; below it two person cards 「新築した人」「買った人」 each with a blue check 「自分の名前で」; a small note 「相続人も自分の名前で」.
Right column, header 「区分建物」: a large name card 「最初に建てた人（原始取得者）の名前で」; below it three small rows: 「買った人：自分の名前ではできない（代位はできる）」, 「相続人・合併後の会社：被承継人の名前で申請できる」, 「買った人に1か月の義務はない」.
Bottom: a yellow note 「1か月は前の持ち主の新築の日からではない」.

--- FOOTER ---
Small note at the bottom: 「不動産登記法第47条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 区、建、物、産、登、続、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 各論：表題部の変更の登記の起算点

### note用（`jg06_kakuron02.png`）

```
Create a Japanese-language explainer infographic, portrait layout, 1080x1500 pixels,
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「表題部の変更の登記の起算点」
Subtitle (smaller, in a pale-yellow band): 「第51条」


--- BODY ---
A horizontal timeline with three starting points, each a colored marker on the line with its own 「1か月」 bracket:
 marker 1 「変わった日」 → person card 「そのときの所有者」 (第1項),
 marker 2 「自分の所有権の登記の日」 → person card 「変わった後に買った人」 (第2項),
 marker 3 「共用部分の登記の日」 → person card 「それまで義務のなかった所有者」 (第3項).
Below the timeline, a small building with several units and one person submitting a form, with arrows to all units: 「一棟の変更は1人の申請で全部に効く」.
Bottom: two small cards 「外壁の張り替えだけ：登記は要らない」 and 「えい行移転：所在の変更の登記」.

--- FOOTER ---
Small note at the bottom: 「不動産登記法第51条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効、変、所、権、産、登、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg06_kakuron02_ig.png`）

```
Create a Japanese-language explainer infographic for an Instagram feed image, 1080x1440 pixels (3:4 portrait). Keep 54px side margins and 72px top and bottom margins free of text.
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「表題部の変更の登記の起算点」
Subtitle (smaller, in a pale-yellow band): 「第51条」


--- BODY ---
A horizontal timeline with three starting points, each a colored marker on the line with its own 「1か月」 bracket:
 marker 1 「変わった日」 → person card 「そのときの所有者」 (第1項),
 marker 2 「自分の所有権の登記の日」 → person card 「変わった後に買った人」 (第2項),
 marker 3 「共用部分の登記の日」 → person card 「それまで義務のなかった所有者」 (第3項).
Below the timeline, a small building with several units and one person submitting a form, with arrows to all units: 「一棟の変更は1人の申請で全部に効く」.
Bottom: two small cards 「外壁の張り替えだけ：登記は要らない」 and 「えい行移転：所在の変更の登記」.

--- FOOTER ---
Small note at the bottom: 「不動産登記法第51条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効、変、所、権、産、登、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 各論：滅失の登記を申請する人

### note用（`jg06_kakuron03.png`）

```
Create a Japanese-language explainer infographic, portrait layout, 1080x1500 pixels,
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「滅失の登記を申請する人」
Subtitle (smaller, in a pale-yellow band): 「第57条」


--- BODY ---
Center: a house being torn down, with a calendar 「滅失の日から1か月」.
Left: blue-check cards 「表題部所有者」「所有権の登記名義人」「移転の登記の前の売主」「区分所有者の1人（一棟の全部）」.
Right: red-cross cards 「土地の所有者」「仮登記の名義人」.
Bottom left: a note 「抵当権の登記があっても先に抹消しなくてよい」.
Bottom right: a note 「解体して建て直したら滅失＋表題登記」.

--- FOOTER ---
Small note at the bottom: 「不動産登記法第57条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 区、地、建、所、権、滅、産、登、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg06_kakuron03_ig.png`）

```
Create a Japanese-language explainer infographic for an Instagram feed image, 1080x1440 pixels (3:4 portrait). Keep 54px side margins and 72px top and bottom margins free of text.
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「滅失の登記を申請する人」
Subtitle (smaller, in a pale-yellow band): 「第57条」


--- BODY ---
Center: a house being torn down, with a calendar 「滅失の日から1か月」.
Left: blue-check cards 「表題部所有者」「所有権の登記名義人」「移転の登記の前の売主」「区分所有者の1人（一棟の全部）」.
Right: red-cross cards 「土地の所有者」「仮登記の名義人」.
Bottom left: a note 「抵当権の登記があっても先に抹消しなくてよい」.
Bottom right: a note 「解体して建て直したら滅失＋表題登記」.

--- FOOTER ---
Small note at the bottom: 「不動産登記法第57条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 区、地、建、所、権、滅、産、登、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 間違いノート：1か月は、前の持ち主の新築の日から？

### note用（`jg06_machigai01.png`）

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
Title (large, bold): 「1か月は、前の持ち主の新築の日から？」
Subtitle (smaller): 「起算点は自分が取得した日」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「新築後すぐに未登記で建物を買った人は、新築の日から1か月以内に表題登記を申請する。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「買った人の期限は、自分が所有権を取得した日から1か月。変更の登記でも、後から所有者になった人は自分の所有権の登記の日から。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「肢の人が、いつ所有者になったかを見る」
  Step box 2: 「表題登記なら『取得の日』、変更の登記なら『自分の所有権の登記の日』から数える」
  Step box 3: 「工事の完了の日・新築の日は、そのとき所有者だった人の起算点」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「条文の起算点は、申請する人ごとに決まります。『誰の』『何の日』から1か月かを、人ごとに確かめます。」

--- FOOTER ---
Small note: 「不動産登記法第47条第1項・第51条第2項」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 変、建、所、権、物、産、登、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg06_machigai01_ig.png`）

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
Title (large, bold): 「1か月は、前の持ち主の新築の日から？」
Subtitle (smaller): 「起算点は自分が取得した日」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「新築後すぐに未登記で建物を買った人は、新築の日から1か月以内に表題登記を申請する。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「買った人の期限は、自分が所有権を取得した日から1か月。変更の登記でも、後から所有者になった人は自分の所有権の登記の日から。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「肢の人が、いつ所有者になったかを見る」
  Step box 2: 「表題登記なら『取得の日』、変更の登記なら『自分の所有権の登記の日』から数える」
  Step box 3: 「工事の完了の日・新築の日は、そのとき所有者だった人の起算点」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「条文の起算点は、申請する人ごとに決まります。『誰の』『何の日』から1か月かを、人ごとに確かめます。」

--- FOOTER ---
Small note: 「不動産登記法第47条第1項・第51条第2項」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 変、建、所、権、物、産、登、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 間違いノート：区分建物も、買った人の名前で表題登記？

### note用（`jg06_machigai02.png`）

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
Title (large, bold): 「区分建物も、買った人の名前で表題登記？」
Subtitle (smaller): 「表題部所有者は原始取得者」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「表題登記のない区分建物を買った人や、新築した人の相続人は、自分を表題部所有者として表題登記を申請する。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「区分建物の表題部所有者は最初に建てた人（原始取得者）。相続人・合併後の会社は被承継人の名前で申請でき、買った人は代位で申請する。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「区分建物か、区分建物でない建物かを見る」
  Step box 2: 「区分建物なら、表題部所有者は原始取得者の名前」
  Step box 3: 「区分建物でないなら、取得した人・相続人が自分の名前で申請する」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「第47条第2項は『被承継人を表題部所有者とする』『申請することができる』。名前の扱いと、義務ではないことの2点が出題されます。」

--- FOOTER ---
Small note: 「不動産登記法第47条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 区、建、所、物、産、登、続、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg06_machigai02_ig.png`）

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
Title (large, bold): 「区分建物も、買った人の名前で表題登記？」
Subtitle (smaller): 「表題部所有者は原始取得者」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「表題登記のない区分建物を買った人や、新築した人の相続人は、自分を表題部所有者として表題登記を申請する。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「区分建物の表題部所有者は最初に建てた人（原始取得者）。相続人・合併後の会社は被承継人の名前で申請でき、買った人は代位で申請する。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「区分建物か、区分建物でない建物かを見る」
  Step box 2: 「区分建物なら、表題部所有者は原始取得者の名前」
  Step box 3: 「区分建物でないなら、取得した人・相続人が自分の名前で申請する」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「第47条第2項は『被承継人を表題部所有者とする』『申請することができる』。名前の扱いと、義務ではないことの2点が出題されます。」

--- FOOTER ---
Small note: 「不動産登記法第47条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 区、建、所、物、産、登、続、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 間違いノート：土地の所有者も、滅失の登記を申請できる？

### note用（`jg06_machigai03.png`）

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
Title (large, bold): 「土地の所有者も、滅失の登記を申請できる？」
Subtitle (smaller): 「申請するのは建物の名義人」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「借地の上の建物が取り壊されたら、土地の所有者が、借地人の承諾を得て滅失の登記を申請できる。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「滅失の登記を申請するのは、建物の表題部所有者か所有権の登記名義人。土地の所有者・仮登記の名義人は申請できない。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「肢の人が、建物の登記記録に名前がある人かを見る」
  Step box 2: 「建物の表題部所有者・所有権の登記名義人なら申請する」
  Step box 3: 「土地の所有者・仮登記の名義人は申請できない（承諾があっても）」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「『承諾を証する情報を付ければ』という肢でも、申請できる人の範囲は広がりません。」

--- FOOTER ---
Small note: 「不動産登記法第57条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地、建、所、権、滅、物、産、登、記、請、録; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg06_machigai03_ig.png`）

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
Title (large, bold): 「土地の所有者も、滅失の登記を申請できる？」
Subtitle (smaller): 「申請するのは建物の名義人」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「借地の上の建物が取り壊されたら、土地の所有者が、借地人の承諾を得て滅失の登記を申請できる。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「滅失の登記を申請するのは、建物の表題部所有者か所有権の登記名義人。土地の所有者・仮登記の名義人は申請できない。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「肢の人が、建物の登記記録に名前がある人かを見る」
  Step box 2: 「建物の表題部所有者・所有権の登記名義人なら申請する」
  Step box 3: 「土地の所有者・仮登記の名義人は申請できない（承諾があっても）」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「『承諾を証する情報を付ければ』という肢でも、申請できる人の範囲は広がりません。」

--- FOOTER ---
Small note: 「不動産登記法第57条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地、建、所、権、滅、物、産、登、記、請、録; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```
