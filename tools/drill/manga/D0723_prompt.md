# D0723 4コマ解説図解 プロンプト（ChatGPT貼付用・v02）

- 肢：D0723（民法／物権変動・対抗要件、出典 H24-Q03ウ）。正解＝×（誤った記述）。誤解3回。
- 記事：`note-articles/h24-mondai/q03-taikouyouken.md` ウ「中間省略登記の合意があっても、債権者の代位行使は妨げられない」
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の5枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 登場人物：Ａ・Ｂ・Ｃ・Ｅ（Ｂの債権者）をコマ1で紹介（Ｄは使わない）。
- 矢印の意味を線種で区別：実線＝売却（所有権の移転）、点線＝登記の移転、コマ4の太い実線＝Ｅの請求（代位）。コマ2に凡例「実線＝売却　点線＝登記の移転」を入れる。
- 会話順：藍子の誤解（合意があればＥは請求できない）→中間省略登記とは→合意は経路の取決めにとどまる→結論（記述は×）。
- 配色：対比カードの○×は使わない（コマ2は左右の説明カードで印なし）。チェック欄は青。
- 記事の範囲：登記は原則Ａ→Ｂ→Ｃ／三者間の合意でＢを飛ばしてＡ→Ｃ／合意があってもＢの登記請求権は消滅しない（合意は登記を移す経路の取決め）／ＥはＢに代位してＡに請求できる（民法423条）。
- 注意：この肢は条文照合で「判例の出典が記事に示されていない」旨の指摘あり（#article-fix 対象）。図解は記事の文言どおりにとどめ、判例名・年月日・条文の追加はしない。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D0723～H24-Q03ウ～

## note記事の冒頭文

土地がＡからＢ、ＢからＣへと譲渡され、登記はＡのままです。三者で「Ｂを飛ばして、ＡからＣへ直接登記する」と合意した場合、Ｂにお金を貸しているＥは、もうＢに代わって登記を請求できないのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（平成24年度　第3問　ウ）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 中間省略登記の合意があっても、Ｅは代位して請求できる | 「Ｅは代位して請求できる」を黄色マーカー |
| コマ1 見出し | ラベル | ①　よくある思い込み | — |
| コマ1 図 | 図・カード | Ａ / Ｂ / Ｃ / 売却 / Ｅ / Ｂの債権者 / 登記名義はＡのまま / Ａ→Ｂ→Ｃと順次譲渡 | — |
| コマ1 | 藍子（左・先に話す） | 三者で合意したなら、Ｅはもう請求できませんよね？ | 「もう請求できませんよね？」 |
| コマ1 | トリ先生（右・答える） | 出たわね。その合意が何を決めたのか、見てごらん | — |
| コマ2 見出し | ラベル | ②　中間省略登記とは | — |
| コマ2 図 | 図・カード | 原則 / Ａ→Ｂ、Ｂ→Ｃと順に登記 / Ａ / Ｂ / Ｃ / 三者間の合意がある場合 / Ａ→Ｃへ直接登記 / 実線＝売却　点線＝登記の移転 | — |
| コマ2 | 藍子（左・先に話す） | 中間省略登記って、何ですか？ | — |
| コマ2 | トリ先生（右・答える） | Ｂを飛ばして、ＡからＣへ直接登記を移すことよ | 「Ｂを飛ばして」 |
| コマ3 見出し | ラベル | ③　合意で登記請求権は消えない | — |
| コマ3 図 | 図・カード | Ｂ / ＢのＡに対する登記請求権 / 消滅しない / 三者間の合意 / 登記を移す経路の取決め | — |
| コマ3 | 藍子（左・先に話す） | 合意をしたら、Ｂの登記請求権は消えるんですか？ | — |
| コマ3 | トリ先生（右・答える） | 消えないわ。合意は登記を移す経路の取決めなのよ | 「消えない」 |
| コマ4 見出し | ラベル | ④　結論は× | — |
| コマ4 図 | 図・カード | Ｅ / Ａ / Ｂに代わって、Ｂへの所有権移転登記を請求 / 代位（民法423条） | — |
| コマ4 | 藍子（左・先に話す） | Ｅは、Ｂに代わってＡに請求できるんですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。合意があっても代位行使は妨げられないのよ | 「代位行使は妨げられない」 |
| コマ4 チェック欄 | 3項目（青✓） | 三者間の合意があってもＢの登記請求権は消えない / ＥはＢに代位してＡに請求できる / 代位は自己の債権を守るための制度 | — |
| 結論帯 | 1行目 | 中間省略登記の合意があっても、債権者の代位行使は妨げられない | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0723　正解×（H24-Q03ウ） | — |

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers, and the full-width letters Ａ Ｂ Ｃ Ｅ only where specified below. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a navy business suit over a blouse with thin blue vertical stripes; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. The legal parties Ａ, Ｂ, Ｃ, Ｅ are NOT characters: draw them only as small, faceless, flat pictogram figures, each with a small round label tag containing the full-width letter given in the text plan.

ANATOMY (critical, 藍子): keep her human anatomy strictly correct in every panel: exactly one head, one torso, exactly two arms (one left, one right) and exactly two hands in total. Never draw extra arms, extra hands, extra fingers, floating hands, duplicated hands, arms that do not grow from the shoulders, or fused hands. Each hand has exactly five fingers. Check that every shoulder, elbow, and wrist connects naturally. HAND COUNT RULE: before drawing each panel, assign both of 藍子's hands a job (for example, one hand points while the other hand holds the clipboard or hangs at her side; or one hand touches her chin while the other holds the clipboard; or both hands are raised in a small cheer). When she points, only ONE arm points; her other hand must not be clasped, raised, or clenched at the same time, so there are never three hands in a panel. POSE: change 藍子's pose from panel to panel (for example standing, sitting, leaning forward, resting a hand on her chin) and use a different set of poses each time this image is generated. CONTENT: in each panel, express through the diagram, labels, and scene the elements a reader needs in order to understand this article's content and pass the land and building surveyor exam, without adding any text beyond the given strings.

FIXED POSITIONS AND SPEECH BUBBLES: In all four panels 藍子 (the student) stands on the LEFT side of the panel and トリ先生 (the teacher) stands on the RIGHT side. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

CONTINUITY: any object, label, ribbon, tag, or figure that appears in more than one panel keeps the same look, the same color, and the same label text in every panel in which it appears (for example, a ribbon on a plot of land does not disappear after a step of the diagram), unless that panel's own description says that it changes. Every speech bubble's line breaks follow phrase boundaries as written inside its quotation marks; never split a word across lines.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall).

TITLE BANNER: text 「中間省略登記の合意があっても、Ｅは代位して請求できる」 in large bold letters; the part 「Ｅは代位して請求できる」 has a yellow highlighter marker.

PANEL 1 (藍子 confident, トリ先生 exasperated but caring; 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　よくある思い込み」
- Small diagram in the middle: three faceless pictograms in a row with tags 「Ａ」, 「Ｂ」, and 「Ｃ」, joined by two SOLID navy arrows (Ａ to Ｂ and Ｂ to Ｃ), each labeled 「売却」. Below Ｂ stands a fourth pictogram with tag 「Ｅ」 joined to Ｂ by a thin line labeled 「Ｂの債権者」. Under Ａ a small plate reads 「登記名義はＡのまま」. Caption under the diagram: 「Ａ→Ｂ→Ｃと順次譲渡」.
- 藍子 bubble (left, spoken first): 「三者で合意したなら、
Ｅはもう請求できませんよね？」 with the part 「もう請求できませんよね？」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。その合意が
何を決めたのか、
見てごらん」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (藍子 puzzled, トリ先生 explaining with a wing-pointer; 藍子's hands: one hand touches her chin and the other holds the clipboard at her side (two hands in total)):
- Label tab: 「②　中間省略登記とは」
- Two explanation cards side by side, with no mark on either card. In this panel, DASHED navy arrows mean the transfer of the registration.
- Left card, heading 「原則」, body 「Ａ→Ｂ、Ｂ→Ｃと順に登記」, showing pictograms 「Ａ」, 「Ｂ」, 「Ｃ」 with two short dashed arrows.
- Right card, heading 「三者間の合意がある場合」, body 「Ａ→Ｃへ直接登記」, showing pictograms 「Ａ」, 「Ｂ」, 「Ｃ」 with one long dashed arrow from Ａ to Ｃ that skips Ｂ.
- A small legend at the bottom reads 「実線＝売却　点線＝登記の移転」.
- 藍子 bubble (left, spoken first): 「中間省略登記って、
何ですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「Ｂを飛ばして、
ＡからＣへ直接
登記を移すことよ」 with the part 「Ｂを飛ばして」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 3 (both characters point together at the same figure; 藍子 realizing; 藍子's hands: ONE hand points at the diagram with an extended arm and the other hand hangs at her side or holds the clipboard; her hands are NOT clasped and no third hand appears):
- Label tab: 「③　合意で登記請求権は消えない」
- Pictogram 「Ｂ」 holds a document labeled 「ＢのＡに対する登記請求権」 with a navy sticker 「消滅しない」 on it.
- Beside it, an explanation card (no mark) with the heading 「三者間の合意」 and the body 「登記を移す経路の取決め」.
- 藍子 bubble (left, spoken first): 「合意をしたら、
Ｂの登記請求権は
消えるんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「消えないわ。
合意は登記を移す経路の
取決めなのよ」 with the part 「消えない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は×」
- Pictogram 「Ｅ」 with a solid navy arrow to pictogram 「Ａ」 (a demand), labeled 「Ｂに代わって、Ｂへの所有権移転登記を請求」, and a small tag 「代位（民法423条）」.
- 藍子 bubble (left, spoken first): 「Ｅは、Ｂに代わって
Ａに請求できるんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。
合意があっても
代位行使は妨げられないのよ」 with the part 「代位行使は妨げられない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark: 「三者間の合意があってもＢの登記請求権は消えない」, 「ＥはＢに代位してＡに請求できる」, 「代位は自己の債権を守るための制度」.

CONCLUSION BANNER (strong contrasting solid color, large text, two lines):
- Line 1: 「中間省略登記の合意があっても、債権者の代位行使は妨げられない」 with a yellow highlighter marker.
- Line 2: 「問題D0723　正解×（H24-Q03ウ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm 藍子 is always on the left and トリ先生 always on the right and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 代, 債, 売, 対, 所, 権, 渡, 登, 解, 記, 請, 譲, 間 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 中間省略登記の合意があると | 薄い黄色のマーカー |
| タイトル2行目 | 債権者は代位できない？ | 「代位できない？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D0723　H24-Q03ウ | — |

### 見出し画像プロンプト本体

```text
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the two characters at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): follow the attached character-specification images exactly and do not redesign them. トリ先生 is the chubby bird teacher (round red glasses, blue shirt, red neckerchief) standing at the lower left of center with one wing raised as if explaining. 藍子 is the young woman exam candidate (long wavy brown hair, blouse with thin blue vertical stripes, navy suit) at the lower right of center, resting her chin on one hand with a pen, looking up at トリ先生 with a curious smile, an open textbook on the desk in front of her. Keep both characters facing each other and fully visible, with their faces clear of the title text, and keep 藍子's hairstyle exactly as in the attached images. Keep 藍子's human anatomy strictly correct: exactly one head, one torso, two arms (one left, one right) and two hands in total, each hand with exactly five fingers; never draw extra arms, hands, or fingers, floating or duplicated hands, arms not growing from the shoulders, or fused hands; check that every shoulder, elbow, and wrist connects naturally.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and the Arabic numeral 4; the only Latin letters and digits allowed are those in the subtitle exactly as written below. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it:
中間省略登記の合意があると
Line 2 is larger; the phrase 代位できない？ is red-orange and the rest is dark navy:
債権者は代位できない？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D0723　H24-Q03ウ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: three small houses in a row, the middle one drawn only as a faint outline
Right side: a thick registry book with a magnifying glass, and a hand reaching toward the book

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 中, 間, 省, 略, 登, 記, 合, 意, 債, 権, 者, 代, 位, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D0723～H24-Q03ウ～.png |
| 見出し画像（採用版） | 4コマ解説図解D0723～H24-Q03ウ～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D0723～H24-Q03ウ～_v01.png ／ 4コマ解説図解D0723～H24-Q03ウ～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0723_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：実線（売却）と点線（登記の移転）と請求の矢印が混ざらない。コマ2の凡例がある
- [ ] 工程C：構成表の全文言を記事（H24-Q03ウ）と突き合わせ：「合意は経路の取決め」「登記請求権は消滅しない」「代位（民法423条）」。判例名を足していない
- [ ] 工程C：結論が×（請求できないという記述が誤り）であることが、コマ4のラベル・台詞・結論帯から読み取れる

## 生成後の照合チェック（文言の正本は上の構成表）
- [ ] 4コマ縦一列／タイトル帯・結論帯あり
- [ ] 全コマで藍子＝左・トリ先生＝右、全吹き出しの尾が話者へ向く。藍子の髪型が全コマで同じ
- [ ] タイトル・全セリフ・ラベルが構成表と一字一句一致
- [ ] スタンプ・矢印・ラベルが各カードの枠の内側に収まっている
- [ ] 色：はい・○＝青、いいえ・×＝赤、中立＝ネイビー。対比カードは左右で逆の極性
- [ ] 簡体字・英字なし、背景が不透明
- [ ] 記事の文言から外れていない（独自の理由づけなし）

## 改訂履歴（このファイルは `manga_specs.py` から生成。直すときは設計データを直して再生成する）

- 2026-10-07 v02：①吹き出しの改行位置を文節の区切りで固定（17字以上は全て）／②コマをまたぐ図・ラベル・リボンの見た目の継続（CONTINUITY）を共通ルールに追加／③藍子の人体構造・手の割り当て・ポーズ変更・記事内容の理解に必要な要素の表現（共通ルール）。④記事の条文照合に「中間省略登記の合意で登記請求権が消えない点は出典が示されていない（一般原則からの整理）」との指摘がある。図の文言は記事の範囲内で、独自の理由づけは足していない
- 2026-10-07 v01：初版
