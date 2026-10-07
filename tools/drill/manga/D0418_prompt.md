# D0418 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

- 肢：D0418（民法／用益権・担保物権、出典 H21-Q02ウ）。正解＝〇。誤解4回。
- 記事：`note-articles/h21-mondai/q02-chijouken.md` ウ「地上権者は、土地所有者の承諾なく譲渡・抵当権設定ができる」
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の5枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 登場人物：Ａ（土地の所有者）・Ｂ（地上権者）・Ｃ（譲受人）をコマ1で紹介。Ｄ（お金を貸す人）はコマ2で初登場（ＢがＤのために抵当権を設定する矢印と同時に紹介）。
- 矢印の意味：実線の矢印はすべて取引（譲渡・抵当権の設定）。承諾の有無は矢印ではなくラベル・帯で示す。
- 会話順：藍子が誤解（賃借権との混同）→トリ先生が物権と指摘→対比カード→結論。
- 配色：コマ3の対比は、地上権＝青✓（承諾はいらない）、賃借権＝赤✕（承諾がないと譲渡できない）。逆の極性。
- 記事の範囲：地上権は物権で自由に処分できる／賃借権は所有者の承諾がなければ譲渡できない、のみ。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D0418～H21-Q02ウ～

## note記事の冒頭文

地上権を持っている人が、その権利を他人に譲ったり、担保に入れたりするとき、土地の所有者の承諾は必要なのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（平成21年度　第2問　ウ）。先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 地上権は、所有者の承諾なしで譲渡できる | 「所有者の承諾なしで譲渡できる」を黄色マーカー |
| コマ1 見出し | ラベル | ①　よくある思い込み | — |
| コマ1 図 | 図・カード | Ａ / Ｂ / Ｃ / 地上権を譲渡 / 承諾は要る？ / Ａ（土地の所有者）　Ｂ（地上権者）　Ｃ（譲受人） | — |
| コマ1 | 藍子（左・先に話す） | 地上権を譲るには、所有者の承諾が要りますよね？ | 「承諾が要りますよね？」 |
| コマ1 | トリ先生（右・答える） | 出たわね。賃借権と混ぜた思い込みよ | — |
| コマ2 見出し | ラベル | ②　地上権は物権 | — |
| コマ2 図 | 図・カード | 地上権 / 物権 / Ｂ / Ｃ / 譲渡 / Ｄ / 抵当権を設定 / Ａの承諾なしでできる | — |
| コマ2 | 藍子（左・先に話す） | 地上権って、どんな権利なんですか？ | — |
| コマ2 | トリ先生（右・答える） | 物権よ。権利者が自由に処分できる財産なの | 「自由に処分できる財産」 |
| コマ3 見出し | ラベル | ③　賃借権との違い | — |
| コマ3 図 | 図・カード | 地上権（物権） / 所有者の承諾はいらない / 賃借権 / 所有者の承諾がないと譲渡できない | — |
| コマ3 | 藍子（左・先に話す） | 賃借権は承諾が要るのに、地上権は違うんですか？ | — |
| コマ3 | トリ先生（右・答える） | そこが大きな違いよ。賃借権は承諾がないと譲れないの | 「大きな違い」 |
| コマ4 見出し | ラベル | ④　結論は〇 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 地上権者は、承諾なしで譲渡も抵当権設定もできるんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。物権だから、自分の財産として自由に動かせるのよ | 「自由に動かせる」 |
| コマ4 チェック欄 | 3項目（青✓） | 地上権は物権である / 所有者の承諾なしで譲渡できる / 所有者の承諾なしで抵当権を設定できる | — |
| 結論帯 | 1行目 | 地上権者は、所有者の承諾なしに譲渡も抵当権設定もできる | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0418　正解〇（H21-Q02ウ） | — |

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers, and the full-width letters Ａ Ｂ Ｃ Ｄ only where specified below. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a navy business suit over a blouse with thin blue vertical stripes; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. The legal parties Ａ, Ｂ, Ｃ, Ｄ are NOT characters: draw them only as small, faceless, flat pictogram figures, each with a small round label tag containing the full-width letter given in the text plan.

FIXED POSITIONS AND SPEECH BUBBLES: In all four panels 藍子 (the student) stands on the LEFT side of the panel and トリ先生 (the teacher) stands on the RIGHT side. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall).

TITLE BANNER: text 「地上権は、所有者の承諾なしで譲渡できる」 in large bold letters; the part 「所有者の承諾なしで譲渡できる」 has a yellow highlighter marker.

PANEL 1 (藍子 confident, トリ先生 exasperated but caring):
- Label tab: 「①　よくある思い込み」
- Small diagram in the middle: three faceless pictograms in a row: tag 「Ａ」 (the land owner, standing next to a small plot-of-land icon), tag 「Ｂ」 (a person standing on the same plot), and tag 「Ｃ」 (a person who wants to receive the right). A solid navy arrow from Ｂ to Ｃ carries the label 「地上権を譲渡」. A small question badge above Ａ reads 「承諾は要る？」 (a question badge only, with no check mark and no cross). Caption under the diagram: 「Ａ（土地の所有者）　Ｂ（地上権者）　Ｃ（譲受人）」.
- 藍子 bubble (left, spoken first): 「地上権を譲るには、所有者の承諾が要りますよね？」 with the part 「承諾が要りますよね？」 highlighted in yellow.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。賃借権と混ぜた思い込みよ」.

PANEL 2 (藍子 puzzled, トリ先生 explaining with a wing-pointer):
- Label tab: 「②　地上権は物権」
- A central card with the heading 「地上権」 and the body 「物権」.
- Below the card, pictogram 「Ｂ」 with two solid navy arrows: one to pictogram 「Ｃ」 labeled 「譲渡」, and one to a new pictogram with tag 「Ｄ」 (a person who lends money) labeled 「抵当権を設定」.
- Under both arrows, a dark navy banner reads 「Ａの承諾なしでできる」.
- 藍子 bubble (left, spoken first): 「地上権って、どんな権利なんですか？」.
- トリ先生 bubble (right, spoken as the answer): 「物権よ。権利者が自由に処分できる財産なの」 with the part 「自由に処分できる財産」 highlighted in yellow.

PANEL 3 (both characters point together at the same figure; 藍子 realizing):
- Label tab: 「③　賃借権との違い」
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows a BLUE check mark; the right card shows a RED cross. Do not draw the same mark on both cards. The two cards also have clearly different texts; the two texts are NOT identical.
- Left card, heading 「地上権（物権）」, body 「所有者の承諾はいらない」, with ONE blue check mark only (no cross on this card).
- Right card, heading 「賃借権」, body 「所有者の承諾がないと譲渡できない」, with ONE red cross only (no check mark on this card).
- 藍子 bubble (left, spoken first): 「賃借権は承諾が要るのに、地上権は違うんですか？」.
- トリ先生 bubble (right, spoken as the answer): 「そこが大きな違いよ。賃借権は承諾がないと譲れないの」 with the part 「大きな違い」 highlighted in yellow.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly):
- Label tab: 「④　結論は〇」
- 藍子 bubble (left, spoken first): 「地上権者は、承諾なしで譲渡も抵当権設定もできるんですね！」.
- トリ先生 bubble (right, spoken as the answer): 「そう。物権だから、自分の財産として自由に動かせるのよ」 with the part 「自由に動かせる」 highlighted in yellow.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark: 「地上権は物権である」, 「所有者の承諾なしで譲渡できる」, 「所有者の承諾なしで抵当権を設定できる」.

CONCLUSION BANNER (strong contrasting solid color, large text, two lines):
- Line 1: 「地上権者は、所有者の承諾なしに譲渡も抵当権設定もできる」 with a yellow highlighter marker.
- Line 2: 「問題D0418　正解〇（H21-Q02ウ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm 藍子 is always on the left and トリ先生 always on the right and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 地, 当, 所, 承, 抵, 権, 渡, 物, 解, 諾, 譲, 違 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm the left comparison card has only a blue check mark and the right card only a red cross; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景3案）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。**背景だけ3案**：案A＝苦手分析シリーズ踏襲、案B＝4コマ原稿用紙風、案C＝間違いノート風。1つ選んでChatGPTに貼る。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 地上権を譲るとき | 薄い黄色のマーカー |
| タイトル2行目 | 所有者の承諾は要る？ | 「承諾は要る？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D0418　H21-Q02ウ | — |

### 案A：苦手分析シリーズ踏襲（水彩の空）

```text
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the two characters at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): follow the attached character-specification images exactly and do not redesign them. トリ先生 is the chubby bird teacher (round red glasses, blue shirt, red neckerchief) standing at the lower left of center with one wing raised as if explaining. 藍子 is the young woman exam candidate (long wavy brown hair, blouse with thin blue vertical stripes, navy suit) at the lower right of center, resting her chin on one hand with a pen, looking up at トリ先生 with a curious smile, an open textbook on the desk in front of her. Keep both characters facing each other and fully visible, with their faces clear of the title text, and keep 藍子's hairstyle exactly as in the attached images.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and the Arabic numeral 4; the only Latin letters and digits allowed are those in the subtitle exactly as written below. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it:
地上権を譲るとき
Line 2 is larger; the phrase 承諾は要る？ is red-orange and the rest is dark navy:
所有者の承諾は要る？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D0418　H21-Q02ウ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a plot of land with a small house standing on it and an empty signpost board
Right side: two hands passing a rolled deed scroll and a small key, with a small bank building behind them

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 上, 権, 譲, 所, 有, 者, 承, 諾, 要, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

### 案B：4コマ原稿用紙風

```text
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: warm, clean Japanese comic-draft illustration on cream manuscript paper, with thin dark-gray outlines and light-gray screen-tone dots in the corners. Keep exactly the same overall layout: the title block at the top center, the two characters at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with cream manuscript paper. Faint, thin gray panel-frame lines form an empty four-panel grid behind everything (empty frames, nothing inside them except the faded scenes at the left and right edges).

CHARACTERS (critical): follow the attached character-specification images exactly and do not redesign them. トリ先生 is the chubby bird teacher (round red glasses, blue shirt, red neckerchief) standing at the lower left of center with one wing raised as if explaining. 藍子 is the young woman exam candidate (long wavy brown hair, blouse with thin blue vertical stripes, navy suit) at the lower right of center, resting her chin on one hand with a pen, looking up at トリ先生 with a curious smile, an open textbook on the desk in front of her. Keep both characters facing each other and fully visible, with their faces clear of the title text, and keep 藍子's hairstyle exactly as in the attached images.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and the Arabic numeral 4; the only Latin letters and digits allowed are those in the subtitle exactly as written below. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white paper label with a thin gray border so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it:
地上権を譲るとき
Line 2 is larger; the phrase 承諾は要る？ is red-orange and the rest is dark navy:
所有者の承諾は要る？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D0418　H21-Q02ウ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a plot of land with a small house standing on it and an empty signpost board
Right side: two hands passing a rolled deed scroll and a small key, with a small bank building behind them

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 上, 権, 譲, 所, 有, 者, 承, 諾, 要, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

### 案C：間違いノート風

```text
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: warm, clean flat illustration on a pale cream notebook page, with thin outlines and soft pastel colors. Keep exactly the same overall layout: the title block at the top center, the two characters at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with a pale cream notebook page with faint light-blue ruled lines and a soft margin line. In the lower corners place a pencil and an eraser, and a few small blank sticky notes (no writing on them). A few loose hand-drawn pen circles (plain circles with nothing inside) are scattered softly in the background.

CHARACTERS (critical): follow the attached character-specification images exactly and do not redesign them. トリ先生 is the chubby bird teacher (round red glasses, blue shirt, red neckerchief) standing at the lower left of center with one wing raised as if explaining. 藍子 is the young woman exam candidate (long wavy brown hair, blouse with thin blue vertical stripes, navy suit) at the lower right of center, resting her chin on one hand with a pen, looking up at トリ先生 with a curious smile, an open textbook on the desk in front of her. Keep both characters facing each other and fully visible, with their faces clear of the title text, and keep 藍子's hairstyle exactly as in the attached images.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and the Arabic numeral 4; the only Latin letters and digits allowed are those in the subtitle exactly as written below. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white tape-style label with a thin navy border so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it:
地上権を譲るとき
Line 2 is larger; the phrase 承諾は要る？ is red-orange and the rest is dark navy:
所有者の承諾は要る？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D0418　H21-Q02ウ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a plot of land with a small house standing on it and an empty signpost board
Right side: two hands passing a rolled deed scroll and a small key, with a small bank building behind them

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 上, 権, 譲, 所, 有, 者, 承, 諾, 要, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

### 見出し画像の検品
- [ ] 画像内の文字は、タイトル2行とサブタイトルだけ。文言が上の表と一字一句一致、簡体字・余計な文字なし
- [ ] トリ先生が左下、藍子が右下で向き合い、顔がタイトルに重ならない。藍子の髪型が参照画像どおり
- [ ] 左右のテーマの場面に文字がなく、タイトル・キャラより目立たない
- [ ] 背景が不透明（透過・チェッカーボードなし）、中央でトリミングしても主要要素が切れない

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0418_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：Ｄ（コマ2で初登場）は、同じコマの「抵当権を設定」の矢印と人型タグで紹介されている
- [ ] 工程C：構成表の全文言を記事（H21-Q02ウ）と突き合わせ：「物権」「自由に処分できる財産」「承諾がなければ譲渡できない賃借権」
- [ ] 工程C：コマ3の左右のカードのマークが逆で、文言が別々（地上権の承諾はいらない／賃借権の承諾がないと譲渡できない）

## 生成後の照合チェック（文言の正本は上の構成表）
- [ ] 4コマ縦一列／タイトル帯・結論帯あり
- [ ] 全コマで藍子＝左・トリ先生＝右、全吹き出しの尾が話者へ向く。藍子の髪型が全コマで同じ
- [ ] タイトル・全セリフ・ラベルが構成表と一字一句一致
- [ ] スタンプ・矢印・ラベルが各カードの枠の内側に収まっている
- [ ] 色：はい・○＝青、いいえ・×＝赤、中立＝ネイビー。対比カードは左右で逆の極性
- [ ] 簡体字・英字なし、背景が不透明
- [ ] 記事の文言から外れていない（独自の理由づけなし）
