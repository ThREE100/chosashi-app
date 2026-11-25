# 第11回「地図・図面の訂正と保存期間」図解・間違いノートのプロンプト

`src/build.py` が `src/d11.py` から作る（手で直さない）。画像の生成はChatGPTで行う。各図に note用（縦長）と Instagram用（1080×1440）の2つがある。文字はどちらも同じで、大きさと余白だけ違う。

## 確かめること

- 文字が「」の中と1字ずつ一致しているか（簡体字・繁体字・余計な文字がないか）。図番が入っていないか。
- ○（正しい）は青、×（思い込み）は赤。1つの箱に○と×が両方入っていないか。
- 背景が不透明か。直すときは、プロンプトの最後に「次の点だけを直して、ほかは変えない：…」と1文足す。

## 図の一覧

- `jg11_soron.png`（Instagram用 `jg11_soron_ig.png`）：総論：地図・図面の訂正と保存期間
- `jg11_kakuron01.png`（Instagram用 `jg11_kakuron01_ig.png`）：各論：精度区分は地域で決まる
- `jg11_kakuron02.png`（Instagram用 `jg11_kakuron02_ig.png`）：各論：地図の訂正の申出
- `jg11_kakuron03.png`（Instagram用 `jg11_kakuron03_ig.png`）：各論：図面の訂正か、更正の登記か
- `jg11_kakuron04.png`（Instagram用 `jg11_kakuron04_ig.png`）：各論：いつまで残すか
- `jg11_machigai01.png`（Instagram用 `jg11_machigai01_ig.png`）：間違いノート：閉鎖したら、どれも同じ年数？
- `jg11_machigai02.png`（Instagram用 `jg11_machigai02_ig.png`）：間違いノート：滅失や合併の申請情報は、特別に長い？
- `jg11_machigai03.png`（Instagram用 `jg11_machigai03_ig.png`）：間違いノート：地図が乙一なら、乙一で判断？
- `jg11_machigai04.png`（Instagram用 `jg11_machigai04_ig.png`）：間違いノート：図面に誤りがあれば、訂正の申出？
- `jg11_machigai05.png`（Instagram用 `jg11_machigai05_ig.png`）：間違いノート：地図の誤りは、すぐ申し出ないといけない？

## 総論：地図・図面の訂正と保存期間

### note用（`jg11_soron.png`）

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
Title line 1: 「地図・図面の訂正と保存期間」
Title line 2: 「精度区分・地図の訂正・図面の訂正・保存期間」
Subtitle: 「条文の逆引き図鑑 第11回」


--- CARDS (each card: a short heading, a simple illustration, and one short conclusion tag; no sentences) ---
Card 1: heading 「精度区分」; illustration: three small landscapes (town, farmland, forest) each with a ruler badge; conclusion tag 「土地のある地域で決まる」
Card 2: heading 「地図の訂正の申出」; illustration: a map sheet with a corrected boundary line and a person handing in a form; conclusion tag 「所有者の側から・義務はない」
Card 3: heading 「図面の訂正の申出」; illustration: a survey drawing with a pencil and an eraser, beside a fork sign; conclusion tag 「更正の登記ができるなら更正」
Card 4: heading 「地図の類」; illustration: a map sheet inside a glass case with an infinity mark; conclusion tag 「閉鎖しても永久」
Card 5: heading 「閉鎖した登記記録」; illustration: two closed binders, one with a field icon and one with a house icon; conclusion tag 「土地は五十年・建物は三十年」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 区、図、地、建、所、物、登、記、録; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; Confirm the header is the fixed block described in HEADER LOCK (three centred lines of 62 / 45 / 35 px at y = 80 / 148 / 204 px, no 午後の部 or 午前の部, no empty gap or band, first card at y = 245 px). confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg11_soron_ig.png`）

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
Title line 1: 「地図・図面の訂正と保存期間」
Title line 2: 「精度区分・地図の訂正・図面の訂正・保存期間」
Subtitle: 「条文の逆引き図鑑 第11回」


--- CARDS (each card: a short heading, a simple illustration, and one short conclusion tag; no sentences) ---
Card 1: heading 「精度区分」; illustration: three small landscapes (town, farmland, forest) each with a ruler badge; conclusion tag 「土地のある地域で決まる」
Card 2: heading 「地図の訂正の申出」; illustration: a map sheet with a corrected boundary line and a person handing in a form; conclusion tag 「所有者の側から・義務はない」
Card 3: heading 「図面の訂正の申出」; illustration: a survey drawing with a pencil and an eraser, beside a fork sign; conclusion tag 「更正の登記ができるなら更正」
Card 4: heading 「地図の類」; illustration: a map sheet inside a glass case with an infinity mark; conclusion tag 「閉鎖しても永久」
Card 5: heading 「閉鎖した登記記録」; illustration: two closed binders, one with a field icon and one with a house icon; conclusion tag 「土地は五十年・建物は三十年」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 区、図、地、建、所、物、登、記、録; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; Confirm the header is the fixed block described in HEADER LOCK (three centred lines of 62 / 45 / 35 px at y = 80 / 148 / 204 px, no 午後の部 or 午前の部, no empty gap or band, first card at y = 245 px). confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 各論：精度区分は地域で決まる

### note用（`jg11_kakuron01.png`）

```
Create a Japanese-language explainer infographic, portrait layout, 1080x1500 pixels,
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「精度区分は地域で決まる」
Subtitle (smaller, in a pale-yellow band): 「不動産登記規則第10条」


--- BODY ---
Three columns side by side, each with a small landscape illustration on top:
 column 1 「市街地地域」 (houses and roads) → badge 「甲二まで」 and a small chip 「縮尺 二百五十分の一か五百分の一」;
 column 2 「村落・農耕地域」 (fields and a farmhouse) → badge 「乙一まで」 and a chip 「縮尺 五百分の一か千分の一」;
 column 3 「山林・原野地域」 (forest and hills) → badge 「乙三まで」 and a chip 「縮尺 千分の一か二千五百分の一」.
Below the columns: a map sheet labeled 「備え付けの地図の精度」 with a gray dashed arrow to the badges, crossed out, and a note 「地図の精度ではなく、土地のある地域で決まる」.

--- FOOTER ---
Small note at the bottom: 「不動産登記規則第10条第2項・第4項」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、区、図、地、産、登、規、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg11_kakuron01_ig.png`）

```
Create a Japanese-language explainer infographic for an Instagram feed image, 1080x1440 pixels (3:4 portrait). Keep 54px side margins and 72px top and bottom margins free of text.
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「精度区分は地域で決まる」
Subtitle (smaller, in a pale-yellow band): 「不動産登記規則第10条」


--- BODY ---
Three columns side by side, each with a small landscape illustration on top:
 column 1 「市街地地域」 (houses and roads) → badge 「甲二まで」 and a small chip 「縮尺 二百五十分の一か五百分の一」;
 column 2 「村落・農耕地域」 (fields and a farmhouse) → badge 「乙一まで」 and a chip 「縮尺 五百分の一か千分の一」;
 column 3 「山林・原野地域」 (forest and hills) → badge 「乙三まで」 and a chip 「縮尺 千分の一か二千五百分の一」.
Below the columns: a map sheet labeled 「備え付けの地図の精度」 with a gray dashed arrow to the badges, crossed out, and a note 「地図の精度ではなく、土地のある地域で決まる」.

--- FOOTER ---
Small note at the bottom: 「不動産登記規則第10条第2項・第4項」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、区、図、地、産、登、規、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 各論：地図の訂正の申出

### note用（`jg11_kakuron02.png`）

```
Create a Japanese-language explainer infographic, portrait layout, 1080x1500 pixels,
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「地図の訂正の申出」
Subtitle (smaller, in a pale-yellow band): 「不動産登記規則第16条」


--- BODY ---
Center: a map sheet with one parcel whose boundary is redrawn with a blue pencil.
Left panel 「申出ができる人」: blue chips 「表題部所有者」「所有権の登記名義人」「相続人などの一般承継人」 and a small note 「共有なら一人から」; red chips with a cross 「抵当権者」「登記を受ける前の買主」.
Right panel 「添えるもの」: 「区画・位置・形状の誤り」 → 「土地所在図か地積測量図」; 「地番だけの誤り」 → 「要らない」.
Bottom row of three small boxes: 「義務も期限もない」, 「登記官は職権でも直せる」, 「地積に錯誤があるときは地積の更正と併せて」.
A small red note at the very bottom: 「ほかの土地の区画まで動かす訂正は受けられない」.

--- FOOTER ---
Small note at the bottom: 「不動産登記規則第16条第1項・第2項・第5項・第13項・第15項」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、区、図、地、所、権、産、画、番、登、積、続、規、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg11_kakuron02_ig.png`）

```
Create a Japanese-language explainer infographic for an Instagram feed image, 1080x1440 pixels (3:4 portrait). Keep 54px side margins and 72px top and bottom margins free of text.
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「地図の訂正の申出」
Subtitle (smaller, in a pale-yellow band): 「不動産登記規則第16条」


--- BODY ---
Center: a map sheet with one parcel whose boundary is redrawn with a blue pencil.
Left panel 「申出ができる人」: blue chips 「表題部所有者」「所有権の登記名義人」「相続人などの一般承継人」 and a small note 「共有なら一人から」; red chips with a cross 「抵当権者」「登記を受ける前の買主」.
Right panel 「添えるもの」: 「区画・位置・形状の誤り」 → 「土地所在図か地積測量図」; 「地番だけの誤り」 → 「要らない」.
Bottom row of three small boxes: 「義務も期限もない」, 「登記官は職権でも直せる」, 「地積に錯誤があるときは地積の更正と併せて」.
A small red note at the very bottom: 「ほかの土地の区画まで動かす訂正は受けられない」.

--- FOOTER ---
Small note at the bottom: 「不動産登記規則第16条第1項・第2項・第5項・第13項・第15項」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、区、図、地、所、権、産、画、番、登、積、続、規、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 各論：図面の訂正か、更正の登記か

### note用（`jg11_kakuron03.png`）

```
Create a Japanese-language explainer infographic, portrait layout, 1080x1500 pixels,
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「図面の訂正か、更正の登記か」
Subtitle (smaller, in a pale-yellow band): 「不動産登記規則第88条」


--- BODY ---
A two-way fork drawn as a 判定の流れ図:
Top box: 「申請のときの図面に誤りがある」 (a survey drawing icon with a pencil).
Question box: 「登記記録の地積や床面積まで違っているか」.
 はい (blue arrow, left) → box 「表題部の更正の登記で直す」 with chips 「求積の計算の誤り」「算入しない出窓を算入した」;
 いいえ (red arrow, right) → box 「図面の訂正の申出」 with chips 「地番の書き誤り」 and a note 「訂正後の図面を出す（省けない）」.
Bottom: a small gray note 「申し出られるのは所有者の側だけで、何人もではない」.

--- FOOTER ---
Small note at the bottom: 「不動産登記規則第88条第1項・第2項」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、図、地、所、産、番、登、積、規、記、請、録; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg11_kakuron03_ig.png`）

```
Create a Japanese-language explainer infographic for an Instagram feed image, 1080x1440 pixels (3:4 portrait). Keep 54px side margins and 72px top and bottom margins free of text.
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「図面の訂正か、更正の登記か」
Subtitle (smaller, in a pale-yellow band): 「不動産登記規則第88条」


--- BODY ---
A two-way fork drawn as a 判定の流れ図:
Top box: 「申請のときの図面に誤りがある」 (a survey drawing icon with a pencil).
Question box: 「登記記録の地積や床面積まで違っているか」.
 はい (blue arrow, left) → box 「表題部の更正の登記で直す」 with chips 「求積の計算の誤り」「算入しない出窓を算入した」;
 いいえ (red arrow, right) → box 「図面の訂正の申出」 with chips 「地番の書き誤り」 and a note 「訂正後の図面を出す（省けない）」.
Bottom: a small gray note 「申し出られるのは所有者の側だけで、何人もではない」.

--- FOOTER ---
Small note at the bottom: 「不動産登記規則第88条第1項・第2項」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、図、地、所、産、番、登、積、規、記、請、録; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 各論：いつまで残すか

### note用（`jg11_kakuron04.png`）

```
Create a Japanese-language explainer infographic, portrait layout, 1080x1500 pixels,
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「いつまで残すか」
Subtitle (smaller, in a pale-yellow band): 「不動産登記規則第28条」


--- BODY ---
Four horizontal bands like shelves, each with icons on the left and a duration badge on the right:
 band 1, deep blue: 「地図・地図に準ずる図面・建物所在図」 (map sheets) → badge 「閉鎖しても永久」;
 band 2, blue-gray: 「申請のときの図面（土地所在図・地積測量図・建物図面・各階平面図）」 → badge 「使っている間は永久／閉鎖したら三十年」;
 band 3, green-gray: 「閉鎖した登記記録」 → two badges 「土地 五十年」「建物 三十年」;
 band 4, light orange: 「申請情報と添付情報」 → badge 「受付の日から三十年」 with a small chip 「表示も権利も、書面でも」.
Bottom: a small note 「閉鎖しても永久なのは、地図の類だけ」.

--- FOOTER ---
Small note at the bottom: 「不動産登記規則第28条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、図、地、建、所、権、準、物、産、登、積、規、記、請、録; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg11_kakuron04_ig.png`）

```
Create a Japanese-language explainer infographic for an Instagram feed image, 1080x1440 pixels (3:4 portrait). Keep 54px side margins and 72px top and bottom margins free of text.
clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type. The image explains how one article of law works, so it may use short labels inside boxes and arrows, but keep each label short.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).

MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.

--- HEADER ---
Title (large, bold): 「いつまで残すか」
Subtitle (smaller, in a pale-yellow band): 「不動産登記規則第28条」


--- BODY ---
Four horizontal bands like shelves, each with icons on the left and a duration badge on the right:
 band 1, deep blue: 「地図・地図に準ずる図面・建物所在図」 (map sheets) → badge 「閉鎖しても永久」;
 band 2, blue-gray: 「申請のときの図面（土地所在図・地積測量図・建物図面・各階平面図）」 → badge 「使っている間は永久／閉鎖したら三十年」;
 band 3, green-gray: 「閉鎖した登記記録」 → two badges 「土地 五十年」「建物 三十年」;
 band 4, light orange: 「申請情報と添付情報」 → badge 「受付の日から三十年」 with a small chip 「表示も権利も、書面でも」.
Bottom: a small note 「閉鎖しても永久なのは、地図の類だけ」.

--- FOOTER ---
Small note at the bottom: 「不動産登記規則第28条」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、図、地、建、所、権、準、物、産、登、積、規、記、請、録; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm nothing is drawn below the footer note; confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 間違いノート：閉鎖したら、どれも同じ年数？

### note用（`jg11_machigai01.png`）

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
Title (large, bold): 「閉鎖したら、どれも同じ年数？」
Subtitle (smaller): 「永久・五十年・三十年の分かれ目」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「閉鎖した地積測量図も、地図と同じく永久に保存される。土地の閉鎖登記記録も永久。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「閉鎖しても永久なのは地図・地図に準ずる図面・建物所在図だけ。閉鎖した地積測量図などの図面は30年、土地の閉鎖登記記録は50年、建物の閉鎖登記記録は30年。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「まず『地図の類』か『申請のときの図面』か『登記記録』かを分ける」
  Step box 2: 「地図の類なら、閉鎖しても永久」
  Step box 3: 「図面なら閉鎖後30年、登記記録なら土地50年・建物30年」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「『地図』と『地積測量図』は名前が似ていますが、地図は登記所が備えるもの、地積測量図は申請人が出すもの。出どころで年数が変わります。」

--- FOOTER ---
Small note: 「不動産登記規則第28条第2号〜第5号・第13号」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、号、図、地、変、建、所、準、物、産、登、積、規、記、請、録; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg11_machigai01_ig.png`）

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
Title (large, bold): 「閉鎖したら、どれも同じ年数？」
Subtitle (smaller): 「永久・五十年・三十年の分かれ目」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「閉鎖した地積測量図も、地図と同じく永久に保存される。土地の閉鎖登記記録も永久。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「閉鎖しても永久なのは地図・地図に準ずる図面・建物所在図だけ。閉鎖した地積測量図などの図面は30年、土地の閉鎖登記記録は50年、建物の閉鎖登記記録は30年。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「まず『地図の類』か『申請のときの図面』か『登記記録』かを分ける」
  Step box 2: 「地図の類なら、閉鎖しても永久」
  Step box 3: 「図面なら閉鎖後30年、登記記録なら土地50年・建物30年」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「『地図』と『地積測量図』は名前が似ていますが、地図は登記所が備えるもの、地積測量図は申請人が出すもの。出どころで年数が変わります。」

--- FOOTER ---
Small note: 「不動産登記規則第28条第2号〜第5号・第13号」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、号、図、地、変、建、所、準、物、産、登、積、規、記、請、録; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 間違いノート：滅失や合併の申請情報は、特別に長い？

### note用（`jg11_machigai02.png`）

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
Title (large, bold): 「滅失や合併の申請情報は、特別に長い？」
Subtitle (smaller): 「申請情報はどれも受付から三十年」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「建物の合併の登記の申請情報は永久に保存される。滅失の登記なら建物がなくなるので、もっと短い。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「申請情報とその添付情報は、どの登記でも受付の日から30年。表示の登記も権利の登記も、書面で出した申請書も同じ。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「問われているのが『申請情報・添付情報』かを確かめる」
  Step box 2: 「そうなら、登記の種類にかかわらず受付の日から30年」
  Step box 3: 「起算点は『受付の日』（閉鎖した日ではない）」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「登記の種類で年数を覚え分ける必要はありません。『申請書類は30年』と1つで覚えます。」

--- FOOTER ---
Small note: 「不動産登記規則第28条第9号・第10号」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、号、建、権、滅、物、産、登、規、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg11_machigai02_ig.png`）

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
Title (large, bold): 「滅失や合併の申請情報は、特別に長い？」
Subtitle (smaller): 「申請情報はどれも受付から三十年」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「建物の合併の登記の申請情報は永久に保存される。滅失の登記なら建物がなくなるので、もっと短い。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「申請情報とその添付情報は、どの登記でも受付の日から30年。表示の登記も権利の登記も、書面で出した申請書も同じ。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「問われているのが『申請情報・添付情報』かを確かめる」
  Step box 2: 「そうなら、登記の種類にかかわらず受付の日から30年」
  Step box 3: 「起算点は『受付の日』（閉鎖した日ではない）」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「登記の種類で年数を覚え分ける必要はありません。『申請書類は30年』と1つで覚えます。」

--- FOOTER ---
Small note: 「不動産登記規則第28条第9号・第10号」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、号、建、権、滅、物、産、登、規、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 間違いノート：地図が乙一なら、乙一で判断？

### note用（`jg11_machigai03.png`）

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
Title (large, bold): 「地図が乙一なら、乙一で判断？」
Subtitle (smaller): 「公差は土地のある地域で決まる」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「市街地の土地でも、備え付けの地図が乙一で作られているなら、地積の更正が要るかは乙一の公差で判断する。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「精度区分は土地のある地域で決まる。市街地地域なら、地図の精度にかかわらず甲二の公差で判断する。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「土地がどの地域にあるかを見る」
  Step box 2: 「市街地地域は甲二まで、村落・農耕地域は乙一まで、山林・原野地域は乙三まで」
  Step box 3: 「備え付けの地図の精度は判断に使わない」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「記述式でも同じです。問題文の『地図の精度』に引っ張られず、地域で公差の表の行を選びます。」

--- FOOTER ---
Small note: 「不動産登記規則第10条第4項・第77条第5項」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、区、図、地、産、登、積、規、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg11_machigai03_ig.png`）

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
Title (large, bold): 「地図が乙一なら、乙一で判断？」
Subtitle (smaller): 「公差は土地のある地域で決まる」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「市街地の土地でも、備え付けの地図が乙一で作られているなら、地積の更正が要るかは乙一の公差で判断する。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「精度区分は土地のある地域で決まる。市街地地域なら、地図の精度にかかわらず甲二の公差で判断する。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「土地がどの地域にあるかを見る」
  Step box 2: 「市街地地域は甲二まで、村落・農耕地域は乙一まで、山林・原野地域は乙三まで」
  Step box 3: 「備え付けの地図の精度は判断に使わない」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「記述式でも同じです。問題文の『地図の精度』に引っ張られず、地域で公差の表の行を選びます。」

--- FOOTER ---
Small note: 「不動産登記規則第10条第4項・第77条第5項」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、区、図、地、産、登、積、規、記; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 間違いノート：図面に誤りがあれば、訂正の申出？

### note用（`jg11_machigai04.png`）

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
Title (large, bold): 「図面に誤りがあれば、訂正の申出？」
Subtitle (smaller): 「登記記録まで違うなら更正の登記」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「地積測量図の求積の計算を誤って、登記記録の地積も違ってしまった。地積測量図の訂正の申出で直せる。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「登記記録の地積まで違うなら、表題部の更正の登記で直す。訂正の申出ができるのは、登記記録はそのままで図面だけが違うとき。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「図面の誤りで、登記記録の数値まで違っているかを見る」
  Step box 2: 「違っているなら、更正の登記（新しい図面を添える）」
  Step box 3: 「違っていないなら、訂正の申出（訂正後の図面を出す）」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「第88条第1項のただし書『更正の登記をすることができる場合は、この限りでない』が答えそのものです。」

--- FOOTER ---
Small note: 「不動産登記規則第88条第1項」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、図、地、産、登、積、規、記、録; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg11_machigai04_ig.png`）

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
Title (large, bold): 「図面に誤りがあれば、訂正の申出？」
Subtitle (smaller): 「登記記録まで違うなら更正の登記」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「地積測量図の求積の計算を誤って、登記記録の地積も違ってしまった。地積測量図の訂正の申出で直せる。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「登記記録の地積まで違うなら、表題部の更正の登記で直す。訂正の申出ができるのは、登記記録はそのままで図面だけが違うとき。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「図面の誤りで、登記記録の数値まで違っているかを見る」
  Step box 2: 「違っているなら、更正の登記（新しい図面を添える）」
  Step box 3: 「違っていないなら、訂正の申出（訂正後の図面を出す）」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「第88条第1項のただし書『更正の登記をすることができる場合は、この限りでない』が答えそのものです。」

--- FOOTER ---
Small note: 「不動産登記規則第88条第1項」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、図、地、産、登、積、規、記、録; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```

## 間違いノート：地図の誤りは、すぐ申し出ないといけない？

### note用（`jg11_machigai05.png`）

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
Title (large, bold): 「地図の誤りは、すぐ申し出ないといけない？」
Subtitle (smaller): 「義務はなく、職権でも直る」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「地図の区画の誤りを見つけたら、1月以内に訂正の申出をしなければならない。登記官は申出がなければ直せない。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「地図の訂正の申出は『できる』で、義務も期限もない。登記官は職権でも直せる。義務になるのは、地積に錯誤があるときに地積の更正の登記と併せて申し出ることだけ。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「条文の語尾が『できる』か『しなければならない』かを見る」
  Step box 2: 「申出は『できる』なので、義務も期限もない」
  Step box 3: 「『しなければならない』は、地積に錯誤があるときの併せての申出だけ」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「一月以内の申請義務があるのは、表題登記や表題部の変更の登記（第6回）です。地図の訂正は別物です。」

--- FOOTER ---
Small note: 「不動産登記規則第16条第1項・第2項・第15項」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、区、図、地、変、権、物、産、画、登、積、規、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
```

### Instagram用（`jg11_machigai05_ig.png`）

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
Title (large, bold): 「地図の誤りは、すぐ申し出ないといけない？」
Subtitle (smaller): 「義務はなく、職権でも直る」


--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---
Left box, pale red background, label 「よくある思い込み」, text 「地図の区画の誤りを見つけたら、1月以内に訂正の申出をしなければならない。登記官は申出がなければ直せない。」, with ONE red cross mark only.
Right box, pale blue background, label 「正しい判断」, text 「地図の訂正の申出は『できる』で、義務も期限もない。登記官は職権でも直せる。義務になるのは、地積に錯誤があるときに地積の更正の登記と併せて申し出ることだけ。」, with ONE blue circle mark only.

--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---
  Step box 1: 「条文の語尾が『できる』か『しなければならない』かを見る」
  Step box 2: 「申出は『できる』なので、義務も期限もない」
  Step box 3: 「『しなければならない』は、地積に錯誤があるときの併せての申出だけ」

--- CALLOUT (yellow sticky-note style box) ---
Label 「誤りやすいポイント」, text 「一月以内の申請義務があるのは、表題登記や表題部の変更の登記（第6回）です。地図の訂正は別物です。」

--- FOOTER ---
Small note: 「不動産登記規則第16条第1項・第2項・第15項」

Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 則、区、図、地、変、権、物、産、画、登、積、規、記、請; confirm there is no figure number or panel number; confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn below the footer (no recap panel, no trophy, no extra text block); confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.
Do not add any account name, URL, hashtag or the word note anywhere in the image.
```
