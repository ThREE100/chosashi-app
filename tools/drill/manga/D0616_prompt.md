# D0616 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

- 肢：D0616（民法／時効・条件期限、出典 H23-Q02ア）。正解＝〇。誤解3回。
- 記事：`note-articles/h23-mondai/q02-jikou-engyo.md` ア「連帯保証人は、主債務の消滅時効を援用できる」
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の5枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 登場人物：Ａ（主債務者）・Ｂ（債権者）・Ｃ（連帯保証人）をコマ1で紹介。
- 矢印の意味：コマ1の矢印は債務・保証の関係。コマ2は時系列の3つの別カード（矢印でつながない。③だけ請求の矢印Ｂ→Ｃが入る）。
- 会話順：藍子の誤解（承認したから援用できない）→時系列→承認と援用は別の話→結論。
- 配色：コマ3は左右の対比ではなく、右カードの「援用できる」だけに青✓（左は印なし）。
- 記事の範囲：保証人は消滅時効について正当な利益を有する者として援用権者（民法145条）／時効完成前の保証債務の承認は保証債務の話にすぎない。出題当時の法文の違いは図に入れない。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D0616～H23-Q02ア～

## note記事の冒頭文

連帯保証人が、時効が完成する前に、自分の保証債務を認めていました。その後に主債務の消滅時効が完成したとき、連帯保証人は時効を援用して、請求を拒めるのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（平成23年度　第2問　ア）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 連帯保証人は、主債務の消滅時効を援用できる | 「主債務の消滅時効を援用できる」を黄色マーカー |
| コマ1 見出し | ラベル | ①　よくある思い込み | — |
| コマ1 図 | 図・カード | Ａ / Ｂ / Ｃ / 売買代金債務 / 連帯保証 / Ａ（主債務者）　Ｂ（債権者）　Ｃ（連帯保証人） | — |
| コマ1 | 藍子（左・先に話す） | Ｃは承認したので、もう援用できませんよね？ | 「もう援用できませんよね？」 |
| コマ1 | トリ先生（右・答える） | 出たわね。何を承認したのか、よく見なさい | — |
| コマ2 見出し | ラベル | ②　時系列を整理 | — |
| コマ2 図 | 図・カード | Ｃ / ①Ｃが保証債務を承認 / 時効の完成前 / ②Ａの債務の消滅時効が完成 / Ｂ / ③ＢがＣに履行を請求 | — |
| コマ2 | 藍子（左・先に話す） | 承認したのは、時効が完成する前なんですよね？ | — |
| コマ2 | トリ先生（右・答える） | そう。承認は、自分の保証債務についてだけよ | 「自分の保証債務」 |
| コマ3 見出し | ラベル | ③　承認と援用は別の話 | — |
| コマ3 図 | 図・カード | 保証債務の承認 / 自分の保証債務についての話 / 主債務の時効の援用 / 保証人は援用できる（民法145条） | — |
| コマ3 | 藍子（左・先に話す） | 承認と援用は、別の問題なんですか？ | — |
| コマ3 | トリ先生（右・答える） | そう。保証人は、正当な利益を有する者として援用できるのよ | 「正当な利益を有する者」 |
| コマ4 見出し | ラベル | ④　結論は〇 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | Ｃは、Ｂの請求を拒めるんですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。時効完成前に承認していても援用できるのよ | 「援用できる」 |
| コマ4 チェック欄 | 3項目（青✓） | 保証人は消滅時効の援用権者 / 保証債務の承認と主債務の援用は別問題 / ＣはＢの請求を拒める | — |
| 結論帯 | 1行目 | 承認していても、連帯保証人は主債務の時効を援用できる | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0616　正解〇（H23-Q02ア） | — |

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers, and the full-width letters Ａ Ｂ Ｃ only where specified below. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a navy business suit over a blouse with thin blue vertical stripes; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. The legal parties Ａ, Ｂ, Ｃ are NOT characters: draw them only as small, faceless, flat pictogram figures, each with a small round label tag containing the full-width letter given in the text plan.

FIXED POSITIONS AND SPEECH BUBBLES: In all four panels 藍子 (the student) stands on the LEFT side of the panel and トリ先生 (the teacher) stands on the RIGHT side. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall).

TITLE BANNER: text 「連帯保証人は、主債務の消滅時効を援用できる」 in large bold letters; the part 「主債務の消滅時効を援用できる」 has a yellow highlighter marker.

PANEL 1 (藍子 confident, トリ先生 exasperated but caring):
- Label tab: 「①　よくある思い込み」
- Small diagram in the middle: three faceless pictograms in a row with tags 「Ａ」, 「Ｂ」, and 「Ｃ」. A navy arrow from Ａ to Ｂ is labeled 「売買代金債務」. A navy arrow from Ｃ to Ｂ is labeled 「連帯保証」. Caption under the diagram: 「Ａ（主債務者）　Ｂ（債権者）　Ｃ（連帯保証人）」.
- 藍子 bubble (left, spoken first): 「Ｃは承認したので、もう援用できませんよね？」 with the part 「もう援用できませんよね？」 highlighted in yellow.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。何を承認したのか、よく見なさい」.

PANEL 2 (藍子 puzzled, トリ先生 explaining with a wing-pointer):
- Label tab: 「②　時系列を整理」
- Three SEPARATE numbered cards in a row, left to right. Do NOT connect the cards with arrows. The only arrow in this panel is inside card 3.
- Card 1: pictogram 「Ｃ」 with a small speech mark; text 「①Ｃが保証債務を承認」 and a small tag 「時効の完成前」.
- Card 2: a calendar icon; text 「②Ａの債務の消滅時効が完成」.
- Card 3: pictograms 「Ｂ」 and 「Ｃ」 with one navy arrow from Ｂ to Ｃ (a demand for payment); text 「③ＢがＣに履行を請求」.
- 藍子 bubble (left, spoken first): 「承認したのは、時効が完成する前なんですよね？」.
- トリ先生 bubble (right, spoken as the answer): 「そう。承認は、自分の保証債務についてだけよ」 with the part 「自分の保証債務」 highlighted in yellow.

PANEL 3 (both characters point together at the same figure; 藍子 realizing):
- Label tab: 「③　承認と援用は別の話」
- Left card, heading 「保証債務の承認」, body 「自分の保証債務についての話」, with no mark on this card.
- Right card, heading 「主債務の時効の援用」, body 「保証人は援用できる（民法145条）」, with ONE blue check mark only (no cross on this card).
- 藍子 bubble (left, spoken first): 「承認と援用は、別の問題なんですか？」.
- トリ先生 bubble (right, spoken as the answer): 「そう。保証人は、正当な利益を有する者として援用できるのよ」 with the part 「正当な利益を有する者」 highlighted in yellow.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly):
- Label tab: 「④　結論は〇」
- 藍子 bubble (left, spoken first): 「Ｃは、Ｂの請求を拒めるんですね！」.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。時効完成前に承認していても援用できるのよ」 with the part 「援用できる」 highlighted in yellow.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark: 「保証人は消滅時効の援用権者」, 「保証債務の承認と主債務の援用は別問題」, 「ＣはＢの請求を拒める」.

CONCLUSION BANNER (strong contrasting solid color, large text, two lines):
- Line 1: 「承認していても、連帯保証人は主債務の時効を援用できる」 with a yellow highlighter marker.
- Line 2: 「問題D0616　正解〇（H23-Q02ア）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm 藍子 is always on the left and トリ先生 always on the right and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 代, 保, 債, 効, 売, 帯, 当, 承, 援, 権, 解, 証, 認, 請, 買 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 連帯保証人が承認していても | 薄い黄色のマーカー |
| タイトル2行目 | 時効を援用できる？ | 「援用できる？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D0616　H23-Q02ア | — |

### 見出し画像プロンプト本体

```text
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the two characters at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): follow the attached character-specification images exactly and do not redesign them. トリ先生 is the chubby bird teacher (round red glasses, blue shirt, red neckerchief) standing at the lower left of center with one wing raised as if explaining. 藍子 is the young woman exam candidate (long wavy brown hair, blouse with thin blue vertical stripes, navy suit) at the lower right of center, resting her chin on one hand with a pen, looking up at トリ先生 with a curious smile, an open textbook on the desk in front of her. Keep both characters facing each other and fully visible, with their faces clear of the title text, and keep 藍子's hairstyle exactly as in the attached images.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and the Arabic numeral 4; the only Latin letters and digits allowed are those in the subtitle exactly as written below. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it:
連帯保証人が承認していても
Line 2 is larger; the phrase 援用できる？ is red-orange and the rest is dark navy:
時効を援用できる？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D0616　H23-Q02ア
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a blank calendar page and an hourglass with the sand almost run out
Right side: two interlocked rings and a pen resting on a blank contract sheet

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 連, 帯, 保, 証, 人, 承, 認, 時, 効, 援, 用, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

### 見出し画像の検品
- [ ] 画像内の文字は、タイトル2行とサブタイトルだけ。文言が上の表と一字一句一致、簡体字・余計な文字なし
- [ ] トリ先生が左下、藍子が右下で向き合い、顔がタイトルに重ならない。藍子の髪型が参照画像どおり
- [ ] 左右のテーマの場面に文字がなく、タイトル・キャラより目立たない
- [ ] 背景が不透明（透過・チェッカーボードなし）、中央でトリミングしても主要要素が切れない

## 画像ファイル名（名づけルール）

ChatGPTで生成した画像は、保存するときに次の名前へ変更する（拡張子は生成された形式のまま：png・webp など）。`MANGA_RULES.md` の「画像ファイル名」に従う。

| 画像 | ファイル名 |
|---|---|
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D0616～H23-Q02ア～.png |
| 見出し画像（採用版） | 4コマ解説図解D0616～H23-Q02ア～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D0616～H23-Q02ア～_v01.png ／ 4コマ解説図解D0616～H23-Q02ア～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0616_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ2の3カードは番号付きの別カードで、矢印は③のＢ→Ｃ（請求）だけ。①②は出来事であることがラベルで分かる
- [ ] 工程C：構成表の全文言を記事（H23-Q02ア）と突き合わせ：「正当な利益を有する者」「保証債務についての話にすぎない」
- [ ] 工程C：「承認」と「援用」の主語（Ｃの保証債務の承認／Ａの債務の時効の援用）が取り違えられていない

## 生成後の照合チェック（文言の正本は上の構成表）
- [ ] 4コマ縦一列／タイトル帯・結論帯あり
- [ ] 全コマで藍子＝左・トリ先生＝右、全吹き出しの尾が話者へ向く。藍子の髪型が全コマで同じ
- [ ] タイトル・全セリフ・ラベルが構成表と一字一句一致
- [ ] スタンプ・矢印・ラベルが各カードの枠の内側に収まっている
- [ ] 色：はい・○＝青、いいえ・×＝赤、中立＝ネイビー。対比カードは左右で逆の極性
- [ ] 簡体字・英字なし、背景が不透明
- [ ] 記事の文言から外れていない（独自の理由づけなし）
