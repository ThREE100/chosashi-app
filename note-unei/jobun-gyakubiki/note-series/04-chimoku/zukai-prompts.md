# 第4回「地目は「今の使い方」で決まる」図解・間違いノートのプロンプト

`src/build.py` が `src/d04.py` から作る（手で直さない）。画像の生成はChatGPTで行う。各図に note用（縦長）と Instagram用（1080×1440）の2つがある。文字はどちらも同じで、大きさと余白だけ違う。

## 確かめること

- 文字が「」の中と1字ずつ一致しているか（簡体字・繁体字・余計な文字がないか）。図番が入っていないか。
- ○（正しい）は青、×（思い込み）は赤。1つの箱に○と×が両方入っていないか。
- 背景が不透明か。直すときは、プロンプトの最後に「次の点だけを直して、ほかは変えない：…」と1文足す。

## 図の一覧

- `jg04_soron.png`（Instagram用 `jg04_soron_ig.png`）：総論：地目の決め方と変更の登記
- `jg04_kakuron01.png`（Instagram用 `jg04_kakuron01_ig.png`）：各論：地目が変わったら、誰がいつまでに
- `jg04_kakuron02.png`（Instagram用 `jg04_kakuron02_ig.png`）：各論：地目は今の使い方で決める
- `jg04_kakuron03.png`（Instagram用 `jg04_kakuron03_ig.png`）：各論：宅地か雑種地か、具体例で分ける
- `jg04_machigai01.png`（Instagram用 `jg04_machigai01_ig.png`）：間違いノート：土地を変えた人が申請する？
- `jg04_machigai02.png`（Instagram用 `jg04_machigai02_ig.png`）：間違いノート：地積の誤りにも、1か月の期限がある？
- `jg04_machigai03.png`（Instagram用 `jg04_machigai03_ig.png`）：間違いノート：高圧線の下と変電所は、地目が違う？
- `jg04_machigai04.png`（Instagram用 `jg04_machigai04_ig.png`）：間違いノート：名前で地目を選んでいない？

## 総論：地目の決め方と変更の登記

### note用（`jg04_soron.png`）

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
Title line 1: 「地目の決め方と変更の登記」
Title line 2: 「申請する人・期限・現況で決める・まぎらわしい地目」
Subtitle: 「条文の逆引き図鑑 第4回」


--- CARDS (each card: a short heading, a simple illustration, and one short conclusion tag; no sentences) ---
Card 1: heading 「申請する人」; illustration: a land plot with a name card of the registered owner on it, and a crossed-out card of a tenant beside it; conclusion tag 「表題部所有者・所有権の登記名義人」
Card 2: heading 「期限」; illustration: a calendar page with one month circled, next to a plot changing from field to house lot; conclusion tag 「変わった日から1か月以内」
Card 3: heading 「決め方」; illustration: a magnifying glass over a whole plot, showing a house in use; conclusion tag 「今の使い方で、全体を見て」
Card 4: heading 「まぎらわしい地目」; illustration: small icons of a gas tank, a steel tower, a tennis court and a horse track arranged in a grid; conclusion tag 「具体例は第69条に」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 図、地、変、所、権、登、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; Confirm the header is the fixed block described in HEADER LOCK (three centred lines of 62 / 45 / 35 px at y = 80 / 148 / 204 px, no 午後の部 or 午前の部, no empty gap or band, first card at y = 245 px). confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg04_soron_ig.png`）

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
Title line 1: 「地目の決め方と変更の登記」
Title line 2: 「申請する人・期限・現況で決める・まぎらわしい地目」
Subtitle: 「条文の逆引き図鑑 第4回」


--- CARDS (each card: a short heading, a simple illustration, and one short conclusion tag; no sentences) ---
Card 1: heading 「申請する人」; illustration: a land plot with a name card of the registered owner on it, and a crossed-out card of a tenant beside it; conclusion tag 「表題部所有者・所有権の登記名義人」
Card 2: heading 「期限」; illustration: a calendar page with one month circled, next to a plot changing from field to house lot; conclusion tag 「変わった日から1か月以内」
Card 3: heading 「決め方」; illustration: a magnifying glass over a whole plot, showing a house in use; conclusion tag 「今の使い方で、全体を見て」
Card 4: heading 「まぎらわしい地目」; illustration: small icons of a gas tank, a steel tower, a tennis court and a horse track arranged in a grid; conclusion tag 「具体例は第69条に」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 図、地、変、所、権、登、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; Confirm the header is the fixed block described in HEADER LOCK (three centred lines of 62 / 45 / 35 px at y = 80 / 148 / 204 px, no 午後の部 or 午前の部, no empty gap or band, first card at y = 245 px). confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 各論：地目が変わったら、誰がいつまでに

### note用（`jg04_kakuron01.png`）

```
Create a Japanese-language explainer infographic, portrait layout, 1080x1500 pixels,
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「地目が変わったら、誰がいつまでに」
Subtitle (smaller, in a pale-yellow band): 「不動産登記法第37条」


--- BODY ---
Left half: a timeline flowing left to right: 「現況が変わった日」 (icon: a field turning into a house lot) → a bracket 「1か月以内」 → 「変更の登記の申請」.
Under the timeline, a second short timeline for 「変わった後に所有者になった人」: 「自分の所有権の登記の日」 → 「1か月以内」.
Right half: a card 「申請する人」 with two blue check tags 「表題部所有者」「所有権の登記名義人」 and below it a red-crossed small card 「地上権者・借主ではない」.
Bottom left: a note 「登記原因の日付は、農地法の許可の日ではない」.
Bottom right: a pale red box 「地積の『更正』には申請の義務がない」.

--- FOOTER ---
Small note at the bottom: 「不動産登記法第37条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地、変、所、権、産、登、積、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg04_kakuron01_ig.png`）

```
Create a Japanese-language explainer infographic for an Instagram feed image, 1080x1440 pixels (3:4 portrait). Keep 54px side margins and 72px top and bottom margins free of text.
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「地目が変わったら、誰がいつまでに」
Subtitle (smaller, in a pale-yellow band): 「不動産登記法第37条」


--- BODY ---
Left half: a timeline flowing left to right: 「現況が変わった日」 (icon: a field turning into a house lot) → a bracket 「1か月以内」 → 「変更の登記の申請」.
Under the timeline, a second short timeline for 「変わった後に所有者になった人」: 「自分の所有権の登記の日」 → 「1か月以内」.
Right half: a card 「申請する人」 with two blue check tags 「表題部所有者」「所有権の登記名義人」 and below it a red-crossed small card 「地上権者・借主ではない」.
Bottom left: a note 「登記原因の日付は、農地法の許可の日ではない」.
Bottom right: a pale red box 「地積の『更正』には申請の義務がない」.

--- FOOTER ---
Small note at the bottom: 「不動産登記法第37条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地、変、所、権、産、登、積、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 各論：地目は今の使い方で決める

### note用（`jg04_kakuron02.png`）

```
Create a Japanese-language explainer infographic, portrait layout, 1080x1500 pixels,
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「地目は今の使い方で決める」
Subtitle (smaller, in a pale-yellow band): 「準則第68条が定める23の地目」


--- BODY ---
Top: a banner 「今の使い方」＋「土地の全体」 with an icon of a magnifying glass over a whole plot.
Middle: a grid of six small cards, each with an icon and a short label:
 「宅地」 (a house with its garden), 「墓地」 (a gravestone; small note 「動物は雑種地」), 「鉱泉地」 (a hot spring source; small note 「引いた旅館は宅地」), 「境内地」 (a temple hall), 「用悪水路」 (a small irrigation channel), 「雑種地」 (a parking lot; small note 「ほかのどれでもない土地」).
Bottom left: a card 「地下ではなく地上で見る」 with a cross-section of a hospital above a subway tunnel.
Bottom right: a pale red card 「ない地目：霊園・駐車場・工場用地」.

--- FOOTER ---
Small note at the bottom: 「不動産登記事務取扱手続準則第68条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、地、準、物、産、登、続、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg04_kakuron02_ig.png`）

```
Create a Japanese-language explainer infographic for an Instagram feed image, 1080x1440 pixels (3:4 portrait). Keep 54px side margins and 72px top and bottom margins free of text.
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「地目は今の使い方で決める」
Subtitle (smaller, in a pale-yellow band): 「準則第68条が定める23の地目」


--- BODY ---
Top: a banner 「今の使い方」＋「土地の全体」 with an icon of a magnifying glass over a whole plot.
Middle: a grid of six small cards, each with an icon and a short label:
 「宅地」 (a house with its garden), 「墓地」 (a gravestone; small note 「動物は雑種地」), 「鉱泉地」 (a hot spring source; small note 「引いた旅館は宅地」), 「境内地」 (a temple hall), 「用悪水路」 (a small irrigation channel), 「雑種地」 (a parking lot; small note 「ほかのどれでもない土地」).
Bottom left: a card 「地下ではなく地上で見る」 with a cross-section of a hospital above a subway tunnel.
Bottom right: a pale red card 「ない地目：霊園・駐車場・工場用地」.

--- FOOTER ---
Small note at the bottom: 「不動産登記事務取扱手続準則第68条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、地、準、物、産、登、続、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 各論：宅地か雑種地か、具体例で分ける

### note用（`jg04_kakuron03.png`）

```
Create a Japanese-language explainer infographic, portrait layout, 1080x1500 pixels,
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「宅地か雑種地か、具体例で分ける」
Subtitle (smaller, in a pale-yellow band): 「準則第69条」


--- BODY ---
Two large columns side by side.
Left column, pale blue header 「宅地」, with five small cards (icon + label): 「ガスタンク・石油タンク」, 「宅地に接続するテニスコート・プール」, 「永久的な農具小屋」, 「高圧線の下の建物」, 「判然と区切れる売店」.
Right column, pale gray header 「雑種地」, with five small cards (icon + label): 「鉄塔・変電所」, 「他に使えない高圧線の下」, 「水力発電の水路」, 「建物が付随的なゴルフ場」, 「建物が付随的なガソリンスタンド」.
Bottom: a wide card 「牧草栽培地」 split in two: left 「ふつうは畑」 (a field icon), right 「牧場地域内なら牧場」 (a ranch icon with a barn).

--- FOOTER ---
Small note at the bottom: 「不動産登記事務取扱手続準則第69条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、区、地、変、建、所、準、物、産、登、続、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg04_kakuron03_ig.png`）

```
Create a Japanese-language explainer infographic for an Instagram feed image, 1080x1440 pixels (3:4 portrait). Keep 54px side margins and 72px top and bottom margins free of text.
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「宅地か雑種地か、具体例で分ける」
Subtitle (smaller, in a pale-yellow band): 「準則第69条」


--- BODY ---
Two large columns side by side.
Left column, pale blue header 「宅地」, with five small cards (icon + label): 「ガスタンク・石油タンク」, 「宅地に接続するテニスコート・プール」, 「永久的な農具小屋」, 「高圧線の下の建物」, 「判然と区切れる売店」.
Right column, pale gray header 「雑種地」, with five small cards (icon + label): 「鉄塔・変電所」, 「他に使えない高圧線の下」, 「水力発電の水路」, 「建物が付随的なゴルフ場」, 「建物が付随的なガソリンスタンド」.
Bottom: a wide card 「牧草栽培地」 split in two: left 「ふつうは畑」 (a field icon), right 「牧場地域内なら牧場」 (a ranch icon with a barn).

--- FOOTER ---
Small note at the bottom: 「不動産登記事務取扱手続準則第69条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、区、地、変、建、所、準、物、産、登、続、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 間違いノート：土地を変えた人が申請する？

### note用（`jg04_machigai01.png`）

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
Title (large, bold): 「土地を変えた人が申請する？」
Subtitle (smaller): 「申請するのは所有者の側」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「山林を切り開いて宅地にしたのは地上権者なので、地目の変更の登記は地上権者が申請する。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「地目の変更の登記を申請するのは、表題部所有者か所有権の登記名義人。誰が工事をしたかは関係がない。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「『誰が変えたか』ではなく『誰が所有者として登記されているか』を見る」
  Step box 2: 「所有権の移転の登記の前なら、まだ売主が登記名義人」
  Step box 3: 「敷地権の目的の土地でも、申請するのは土地の所有権の登記名義人」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「第37条は申請の義務者を『表題部所有者又は所有権の登記名義人』と書いています。地上権者・借主・区分建物の所有者は出てきません。」

--- FOOTER ---
Small note: 「不動産登記法第37条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 区、地、変、建、所、敷、権、物、産、登、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg04_machigai01_ig.png`）

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
Title (large, bold): 「土地を変えた人が申請する？」
Subtitle (smaller): 「申請するのは所有者の側」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「山林を切り開いて宅地にしたのは地上権者なので、地目の変更の登記は地上権者が申請する。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「地目の変更の登記を申請するのは、表題部所有者か所有権の登記名義人。誰が工事をしたかは関係がない。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「『誰が変えたか』ではなく『誰が所有者として登記されているか』を見る」
  Step box 2: 「所有権の移転の登記の前なら、まだ売主が登記名義人」
  Step box 3: 「敷地権の目的の土地でも、申請するのは土地の所有権の登記名義人」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「第37条は申請の義務者を『表題部所有者又は所有権の登記名義人』と書いています。地上権者・借主・区分建物の所有者は出てきません。」

--- FOOTER ---
Small note: 「不動産登記法第37条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 区、地、変、建、所、敷、権、物、産、登、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 間違いノート：地積の誤りにも、1か月の期限がある？

### note用（`jg04_machigai02.png`）

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
Title (large, bold): 「地積の誤りにも、1か月の期限がある？」
Subtitle (smaller): 「義務は『変更』だけ」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「登記記録の地積の誤りを知ったら、1か月以内に地積の更正の登記を申請しなければならない。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「申請の義務があるのは、地目・地積が後から変わったときの『変更』の登記だけ。最初から誤っていた『更正』の登記には義務も期限もない。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「地積が後から変わったのか（変更）、最初から誤っていたのか（更正）を見る」
  Step box 2: 「変更なら、1か月以内の申請の義務がある」
  Step box 3: 「更正なら、義務も期限もない（申請はできる）」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「肢に『更正』と『1か月以内』が並んだら、まずひっかけを疑います。」

--- FOOTER ---
Small note: 「不動産登記法第37条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地、変、産、登、積、記、請、録; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg04_machigai02_ig.png`）

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
Title (large, bold): 「地積の誤りにも、1か月の期限がある？」
Subtitle (smaller): 「義務は『変更』だけ」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「登記記録の地積の誤りを知ったら、1か月以内に地積の更正の登記を申請しなければならない。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「申請の義務があるのは、地目・地積が後から変わったときの『変更』の登記だけ。最初から誤っていた『更正』の登記には義務も期限もない。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「地積が後から変わったのか（変更）、最初から誤っていたのか（更正）を見る」
  Step box 2: 「変更なら、1か月以内の申請の義務がある」
  Step box 3: 「更正なら、義務も期限もない（申請はできる）」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「肢に『更正』と『1か月以内』が並んだら、まずひっかけを疑います。」

--- FOOTER ---
Small note: 「不動産登記法第37条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地、変、産、登、積、記、請、録; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 間違いノート：高圧線の下と変電所は、地目が違う？

### note用（`jg04_machigai03.png`）

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
Title (large, bold): 「高圧線の下と変電所は、地目が違う？」
Subtitle (smaller): 「どちらも雑種地」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「高圧線の下の土地は雑種地だが、変電所の敷地は建物があるので宅地。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「他に使えない高圧線の下の土地も、変電所・鉄塔の敷地も、どちらも雑種地。ただし高圧線の下でも、建物の敷地として使っていれば宅地。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「準則第69条に名前が出ている施設かを見る」
  Step box 2: 「鉄塔・変電所の敷地は、建物があっても雑種地」
  Step box 3: 「高圧線の下は、建物の敷地なら宅地、他に使えなければ雑種地」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「『建物がある＝宅地』と決めつけないこと。変電所・火葬場のように、準則が個別に決めているものは条文の結論が優先です。」

--- FOOTER ---
Small note: 「不動産登記事務取扱手続準則第69条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、地、変、建、所、敷、準、物、産、登、続、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg04_machigai03_ig.png`）

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
Title (large, bold): 「高圧線の下と変電所は、地目が違う？」
Subtitle (smaller): 「どちらも雑種地」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「高圧線の下の土地は雑種地だが、変電所の敷地は建物があるので宅地。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「他に使えない高圧線の下の土地も、変電所・鉄塔の敷地も、どちらも雑種地。ただし高圧線の下でも、建物の敷地として使っていれば宅地。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「準則第69条に名前が出ている施設かを見る」
  Step box 2: 「鉄塔・変電所の敷地は、建物があっても雑種地」
  Step box 3: 「高圧線の下は、建物の敷地なら宅地、他に使えなければ雑種地」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「『建物がある＝宅地』と決めつけないこと。変電所・火葬場のように、準則が個別に決めているものは条文の結論が優先です。」

--- FOOTER ---
Small note: 「不動産登記事務取扱手続準則第69条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、地、変、建、所、敷、準、物、産、登、続、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 間違いノート：名前で地目を選んでいない？

### note用（`jg04_machigai04.png`）

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
Title (large, bold): 「名前で地目を選んでいない？」
Subtitle (smaller): 「地目は23種類だけ」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「規模の大きな墓地は霊園、公衆の遊楽のための土地は馬場と同じ雑種地。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「地目は準則第68条が定める23種類だけ。遺体・遺骨を埋める土地は規模にかかわらず墓地、公衆の遊楽のための土地は公園。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「肢の地目が23種類のどれかを確かめる（『霊園』は地目にない）」
  Step box 2: 「公園・墓地・境内地など、名前のある地目の定義に当てはまるかを見る」
  Step box 3: 「どれにも当たらないときだけ雑種地」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「雑種地は『以上のいずれにも該当しない土地』です。先に、名前のある22の地目に当てはまらないかを確かめます。」

--- FOOTER ---
Small note: 「不動産登記事務取扱手続準則第68条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、地、準、産、登、続、規、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg04_machigai04_ig.png`）

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
Title (large, bold): 「名前で地目を選んでいない？」
Subtitle (smaller): 「地目は23種類だけ」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「規模の大きな墓地は霊園、公衆の遊楽のための土地は馬場と同じ雑種地。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「地目は準則第68条が定める23種類だけ。遺体・遺骨を埋める土地は規模にかかわらず墓地、公衆の遊楽のための土地は公園。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「肢の地目が23種類のどれかを確かめる（『霊園』は地目にない）」
  Step box 2: 「公園・墓地・境内地など、名前のある地目の定義に当てはまるかを見る」
  Step box 3: 「どれにも当たらないときだけ雑種地」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「雑種地は『以上のいずれにも該当しない土地』です。先に、名前のある22の地目に当てはまらないかを確かめます。」

--- FOOTER ---
Small note: 「不動産登記事務取扱手続準則第68条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、地、準、産、登、続、規、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```
