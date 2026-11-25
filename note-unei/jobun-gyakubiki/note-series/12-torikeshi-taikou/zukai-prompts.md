# 第12回「取消し・時効と登記、どちらが勝つか」図解・間違いノートのプロンプト

`src/build.py` が `src/d12.py` から作る（手で直さない）。画像の生成はChatGPTで行う。各図に note用（縦長）と Instagram用（1080×1440）の2つがある。文字はどちらも同じで、大きさと余白だけ違う。

## 確かめること

- 文字が「」の中と1字ずつ一致しているか（簡体字・繁体字・余計な文字がないか）。図番が入っていないか。
- ○（正しい）は青、×（思い込み）は赤。1つの箱に○と×が両方入っていないか。
- 背景が不透明か。直すときは、プロンプトの最後に「次の点だけを直して、ほかは変えない：…」と1文足す。

## 図の一覧

- `jg12_soron.png`（Instagram用 `jg12_soron_ig.png`）：総論：取消し・時効と登記、どちらが勝つか
- `jg12_kakuron01.png`（Instagram用 `jg12_kakuron01_ig.png`）：各論：取消しの前か後か
- `jg12_kakuron02.png`（Instagram用 `jg12_kakuron02_ig.png`）：各論：仮装の売買と第三者
- `jg12_kakuron03.png`（Instagram用 `jg12_kakuron03_ig.png`）：各論：登記がなくても勝てる相手、勝てない相手
- `jg12_machigai01.png`（Instagram用 `jg12_machigai01_ig.png`）：間違いノート：取消し前の第三者にも、登記が要る？
- `jg12_machigai02.png`（Instagram用 `jg12_machigai02_ig.png`）：間違いノート：善意の第三者がいたら、取り消せない？
- `jg12_machigai03.png`（Instagram用 `jg12_machigai03_ig.png`）：間違いノート：時効で取得したら、いつでも登記が要る？
- `jg12_machigai04.png`（Instagram用 `jg12_machigai04_ig.png`）：間違いノート：背信的悪意者から買った人にも、登記なしで勝てる？

## 総論：取消し・時効と登記、どちらが勝つか

### note用（`jg12_soron.png`）

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
Title line 1: 「取消し・時効と登記、どちらが勝つか」
Title line 2: 「取消しの前後・時効の前後・登記が要らない相手」
Subtitle: 「条文の逆引き図鑑 第12回」


--- CARDS (each card: a short heading, a simple illustration, and one short conclusion tag; no sentences) ---
Card 1: heading 「取消し前の第三者」; illustration: a timeline with a person standing before a red mark labeled with a cross; conclusion tag 「民法の個別の規定で守る」
Card 2: heading 「取消し後の第三者」; illustration: two people racing toward a registry office building; conclusion tag 「登記の早いほうが勝つ」
Card 3: heading 「時効完成前の第三者」; illustration: an hourglass still running, with a fence and a house; conclusion tag 「登記がなくても勝てる」
Card 4: heading 「時効完成後の第三者」; illustration: an hourglass finished, and two people racing to a registry office; conclusion tag 「登記の早いほうが勝つ」
Card 5: heading 「登記が要らない相手」; illustration: a squatter in front of a house, and an owner pointing calmly; conclusion tag 「不法占拠者・無権利者」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効、図、権、登、規、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; Confirm the header is the fixed block described in HEADER LOCK (three centred lines of 62 / 45 / 35 px at y = 80 / 148 / 204 px, no 午後の部 or 午前の部, no empty gap or band, first card at y = 245 px). confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg12_soron_ig.png`）

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
Title line 1: 「取消し・時効と登記、どちらが勝つか」
Title line 2: 「取消しの前後・時効の前後・登記が要らない相手」
Subtitle: 「条文の逆引き図鑑 第12回」


--- CARDS (each card: a short heading, a simple illustration, and one short conclusion tag; no sentences) ---
Card 1: heading 「取消し前の第三者」; illustration: a timeline with a person standing before a red mark labeled with a cross; conclusion tag 「民法の個別の規定で守る」
Card 2: heading 「取消し後の第三者」; illustration: two people racing toward a registry office building; conclusion tag 「登記の早いほうが勝つ」
Card 3: heading 「時効完成前の第三者」; illustration: an hourglass still running, with a fence and a house; conclusion tag 「登記がなくても勝てる」
Card 4: heading 「時効完成後の第三者」; illustration: an hourglass finished, and two people racing to a registry office; conclusion tag 「登記の早いほうが勝つ」
Card 5: heading 「登記が要らない相手」; illustration: a squatter in front of a house, and an owner pointing calmly; conclusion tag 「不法占拠者・無権利者」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効、図、権、登、規、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; Confirm the header is the fixed block described in HEADER LOCK (three centred lines of 62 / 45 / 35 px at y = 80 / 148 / 204 px, no 午後の部 or 午前の部, no empty gap or band, first card at y = 245 px). confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 各論：取消しの前か後か

### note用（`jg12_kakuron01.png`）

```
Create a Japanese-language explainer infographic, portrait layout, 1080x1500 pixels,
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「取消しの前か後か」
Subtitle (smaller, in a pale-yellow band): 「民法第96条・第177条」


--- BODY ---
A horizontal timeline from left to right with a big vertical red line in the middle labeled 「取消し」.
Left side 「取消し前の第三者」: two stacked boxes —
 blue box 「詐欺」 → 「善意で過失のない第三者には対抗できない（登記は要らない）」;
 orange box 「強迫・制限行為能力」 → 「善意の第三者にも対抗できる」.
Right side 「取消し後の第三者」: one green-gray box 「登記の早いほうが勝つ」 with two small figures racing toward a registry office icon.
Bottom: a small gray note 「取消しそのものは、いつでもできる」.

--- FOOTER ---
Small note at the bottom: 「民法第96条第3項・第177条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 登、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg12_kakuron01_ig.png`）

```
Create a Japanese-language explainer infographic for an Instagram feed image, 1080x1440 pixels (3:4 portrait). Keep 54px side margins and 72px top and bottom margins free of text.
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「取消しの前か後か」
Subtitle (smaller, in a pale-yellow band): 「民法第96条・第177条」


--- BODY ---
A horizontal timeline from left to right with a big vertical red line in the middle labeled 「取消し」.
Left side 「取消し前の第三者」: two stacked boxes —
 blue box 「詐欺」 → 「善意で過失のない第三者には対抗できない（登記は要らない）」;
 orange box 「強迫・制限行為能力」 → 「善意の第三者にも対抗できる」.
Right side 「取消し後の第三者」: one green-gray box 「登記の早いほうが勝つ」 with two small figures racing toward a registry office icon.
Bottom: a small gray note 「取消しそのものは、いつでもできる」.

--- FOOTER ---
Small note at the bottom: 「民法第96条第3項・第177条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 登、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 各論：仮装の売買と第三者

### note用（`jg12_kakuron02.png`）

```
Create a Japanese-language explainer infographic, portrait layout, 1080x1500 pixels,
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「仮装の売買と第三者」
Subtitle (smaller, in a pale-yellow band): 「民法第94条第2項」


--- BODY ---
A left-to-right chain of four person icons connected by arrows: 「売主」 → 「仮装の買主」 → 「善意の第三者」 → 「悪意の転得者」.
Above the first arrow: a dashed outline label 「仮装（無効）」.
Under 「善意の第三者」: a blue shield 「守られる（登記がなくても、過失があっても）」.
Under 「悪意の転得者」: a blue chip 「善意の人を経由したので守られる」.
Bottom: a separate small panel 「不実の登記を知りながら放置」 → 「第九十四条第二項の類推」.

--- FOOTER ---
Small note at the bottom: 「民法第94条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効、登、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg12_kakuron02_ig.png`）

```
Create a Japanese-language explainer infographic for an Instagram feed image, 1080x1440 pixels (3:4 portrait). Keep 54px side margins and 72px top and bottom margins free of text.
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「仮装の売買と第三者」
Subtitle (smaller, in a pale-yellow band): 「民法第94条第2項」


--- BODY ---
A left-to-right chain of four person icons connected by arrows: 「売主」 → 「仮装の買主」 → 「善意の第三者」 → 「悪意の転得者」.
Above the first arrow: a dashed outline label 「仮装（無効）」.
Under 「善意の第三者」: a blue shield 「守られる（登記がなくても、過失があっても）」.
Under 「悪意の転得者」: a blue chip 「善意の人を経由したので守られる」.
Bottom: a separate small panel 「不実の登記を知りながら放置」 → 「第九十四条第二項の類推」.

--- FOOTER ---
Small note at the bottom: 「民法第94条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効、登、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 各論：登記がなくても勝てる相手、勝てない相手

### note用（`jg12_kakuron03.png`）

```
Create a Japanese-language explainer infographic, portrait layout, 1080x1500 pixels,
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「登記がなくても勝てる相手、勝てない相手」
Subtitle (smaller, in a pale-yellow band): 「民法第177条」


--- BODY ---
Two columns.
Left column, blue header 「登記がなくても勝てる」: chips 「不法に占拠する人」「まったくの無権利者」「登記の申請を頼まれていた人」「背信的悪意者」「時効完成前に買った人（時効取得した人から見て）」「勝手に単独の相続の登記をした相続人から買った人（自分の相続分）」.
Right column, orange header 「登記の先後で決まる（第三者）」: chips 「二重に買った人」「他の共有者」「取消し後・時効完成後に現れた人」「背信的悪意者から買った善意の人」「相続人の債権者（遺贈を受けた人から見て）」「解除前に現れた人」.
Bottom: a note 「第三者＝登記がないことを主張する正当な利益のある人」.

--- FOOTER ---
Small note at the bottom: 「民法第177条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効、権、登、続、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg12_kakuron03_ig.png`）

```
Create a Japanese-language explainer infographic for an Instagram feed image, 1080x1440 pixels (3:4 portrait). Keep 54px side margins and 72px top and bottom margins free of text.
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「登記がなくても勝てる相手、勝てない相手」
Subtitle (smaller, in a pale-yellow band): 「民法第177条」


--- BODY ---
Two columns.
Left column, blue header 「登記がなくても勝てる」: chips 「不法に占拠する人」「まったくの無権利者」「登記の申請を頼まれていた人」「背信的悪意者」「時効完成前に買った人（時効取得した人から見て）」「勝手に単独の相続の登記をした相続人から買った人（自分の相続分）」.
Right column, orange header 「登記の先後で決まる（第三者）」: chips 「二重に買った人」「他の共有者」「取消し後・時効完成後に現れた人」「背信的悪意者から買った善意の人」「相続人の債権者（遺贈を受けた人から見て）」「解除前に現れた人」.
Bottom: a note 「第三者＝登記がないことを主張する正当な利益のある人」.

--- FOOTER ---
Small note at the bottom: 「民法第177条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効、権、登、続、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 間違いノート：取消し前の第三者にも、登記が要る？

### note用（`jg12_machigai01.png`）

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
Title (large, bold): 「取消し前の第三者にも、登記が要る？」
Subtitle (smaller): 「取消し前は第九十六条第三項で決まる」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「詐欺で売った人が取り消す前に、善意無過失の第三者に転売されていた。第三者に登記がないので、取消しを対抗できる。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「取消し前の第三者は第96条第3項で守られる。善意で過失がなければ、登記がなくても取消しを対抗できない。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「第三者が現れたのが取消しの前か後かを決める」
  Step box 2: 「前なら、詐欺は善意無過失の第三者に対抗できない（登記は問わない）」
  Step box 3: 「後なら、第177条で登記の早いほうが勝つ」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「『登記の先後』の話になるのは取消し後だけ。取消し前に登記の有無を持ち出したら、ひっかけを疑います。」

--- FOOTER ---
Small note: 「民法第96条第3項」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 登、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg12_machigai01_ig.png`）

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
Title (large, bold): 「取消し前の第三者にも、登記が要る？」
Subtitle (smaller): 「取消し前は第九十六条第三項で決まる」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「詐欺で売った人が取り消す前に、善意無過失の第三者に転売されていた。第三者に登記がないので、取消しを対抗できる。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「取消し前の第三者は第96条第3項で守られる。善意で過失がなければ、登記がなくても取消しを対抗できない。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「第三者が現れたのが取消しの前か後かを決める」
  Step box 2: 「前なら、詐欺は善意無過失の第三者に対抗できない（登記は問わない）」
  Step box 3: 「後なら、第177条で登記の早いほうが勝つ」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「『登記の先後』の話になるのは取消し後だけ。取消し前に登記の有無を持ち出したら、ひっかけを疑います。」

--- FOOTER ---
Small note: 「民法第96条第3項」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 登、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 間違いノート：善意の第三者がいたら、取り消せない？

### note用（`jg12_machigai02.png`）

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
Title (large, bold): 「善意の第三者がいたら、取り消せない？」
Subtitle (smaller): 「取消しはできる。対抗できないだけ」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「詐欺で買った人が、だまされたと知らずに善意の人のために抵当権を設定した。もう詐欺を理由に取り消すことはできない。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「取消しそのものはできる。善意で過失のない抵当権者には、取消しの効果を対抗できないだけ。強迫と制限行為能力の取消しなら、善意の第三者にも対抗できる。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「『取り消せるか』と『第三者に対抗できるか』を分ける」
  Step box 2: 「取消しは、詐欺・強迫・制限行為能力のどれでもできる」
  Step box 3: 「第三者に対抗できないのは、詐欺のときの善意無過失の第三者だけ」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「制限行為能力者の取消しには、善意の第三者を守る規定がありません。だから取消し前の善意の買主にも対抗できます。」

--- FOOTER ---
Small note: 「民法第96条第1項・第3項」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効、権、規; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg12_machigai02_ig.png`）

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
Title (large, bold): 「善意の第三者がいたら、取り消せない？」
Subtitle (smaller): 「取消しはできる。対抗できないだけ」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「詐欺で買った人が、だまされたと知らずに善意の人のために抵当権を設定した。もう詐欺を理由に取り消すことはできない。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「取消しそのものはできる。善意で過失のない抵当権者には、取消しの効果を対抗できないだけ。強迫と制限行為能力の取消しなら、善意の第三者にも対抗できる。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「『取り消せるか』と『第三者に対抗できるか』を分ける」
  Step box 2: 「取消しは、詐欺・強迫・制限行為能力のどれでもできる」
  Step box 3: 「第三者に対抗できないのは、詐欺のときの善意無過失の第三者だけ」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「制限行為能力者の取消しには、善意の第三者を守る規定がありません。だから取消し前の善意の買主にも対抗できます。」

--- FOOTER ---
Small note: 「民法第96条第1項・第3項」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効、権、規; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 間違いノート：時効で取得したら、いつでも登記が要る？

### note用（`jg12_machigai03.png`）

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
Title (large, bold): 「時効で取得したら、いつでも登記が要る？」
Subtitle (smaller): 「完成の前に買った人とは当事者の関係」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「他人の土地を占有して時効が完成した。その前に所有者から買って登記した人がいるので、時効で取得した人は登記がないと勝てない。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「時効の完成前に買った人に対しては、登記がなくても勝てる。登記の先後で決まるのは、時効の完成後に買った人との関係だけ。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「第三者が買ったのが時効の完成の前か後かを見る」
  Step box 2: 「前なら、時効で取得した人は登記がなくても勝てる」
  Step box 3: 「後なら、登記の早いほうが勝つ」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「時効の完成日は、占有を始めた日から10年か20年。善意無過失なら10年（民法第162条第2項）で数えます。」

--- FOOTER ---
Small note: 「民法第177条・第162条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効、地、所、登、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg12_machigai03_ig.png`）

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
Title (large, bold): 「時効で取得したら、いつでも登記が要る？」
Subtitle (smaller): 「完成の前に買った人とは当事者の関係」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「他人の土地を占有して時効が完成した。その前に所有者から買って登記した人がいるので、時効で取得した人は登記がないと勝てない。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「時効の完成前に買った人に対しては、登記がなくても勝てる。登記の先後で決まるのは、時効の完成後に買った人との関係だけ。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「第三者が買ったのが時効の完成の前か後かを見る」
  Step box 2: 「前なら、時効で取得した人は登記がなくても勝てる」
  Step box 3: 「後なら、登記の早いほうが勝つ」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「時効の完成日は、占有を始めた日から10年か20年。善意無過失なら10年（民法第162条第2項）で数えます。」

--- FOOTER ---
Small note: 「民法第177条・第162条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効、地、所、登、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 間違いノート：背信的悪意者から買った人にも、登記なしで勝てる？

### note用（`jg12_machigai04.png`）

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
Title (large, bold): 「背信的悪意者から買った人にも、登記なしで勝てる？」
Subtitle (smaller): 「その人自身で判断する」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「二重譲渡の相手が背信的悪意者だった。そこから買った善意の人にも、最初の買主は登記なしで所有権を主張できる。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「背信的悪意者から買った人は、その人自身が背信的悪意者でなければ第三者に当たる。最初の買主は、登記がなければその人に勝てない。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「登記がないことを主張している人自身が、背信的悪意者かを見る」
  Step box 2: 「自身が背信的悪意者なら、登記なしで勝てる」
  Step box 3: 「そうでなければ、登記の先後で決まる」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「前の人が背信的悪意者でも、後の人には引き継がれません。人ごとに判断します。」

--- FOOTER ---
Small note: 「民法第177条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 所、権、登、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg12_machigai04_ig.png`）

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
Title (large, bold): 「背信的悪意者から買った人にも、登記なしで勝てる？」
Subtitle (smaller): 「その人自身で判断する」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「二重譲渡の相手が背信的悪意者だった。そこから買った善意の人にも、最初の買主は登記なしで所有権を主張できる。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「背信的悪意者から買った人は、その人自身が背信的悪意者でなければ第三者に当たる。最初の買主は、登記がなければその人に勝てない。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「登記がないことを主張している人自身が、背信的悪意者かを見る」
  Step box 2: 「自身が背信的悪意者なら、登記なしで勝てる」
  Step box 3: 「そうでなければ、登記の先後で決まる」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「前の人が背信的悪意者でも、後の人には引き継がれません。人ごとに判断します。」

--- FOOTER ---
Small note: 「民法第177条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 所、権、登、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```
