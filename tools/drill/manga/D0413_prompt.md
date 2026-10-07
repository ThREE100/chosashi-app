# D0413 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

- 肢：D0413（民法／時効・条件期限、出典 H21-Q01ウ）。正解＝×（誤った記述）。誤解3回。
- 記事：`note-articles/h21-mondai/q01-jikou-touki.md` ウ「元所有者Bに対しては、登記がなくても時効取得を主張できる」（対比：D0414・D0412・D0411）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の5枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 登場人物：Ａ（時効取得を主張する占有者）・Ｂ（元の所有者）をコマ1で紹介。甲土地は「甲土地」の文字ラベルのブロック。
- 矢印の意味：矢印は使わない（取引も手続もない）。コマ2は向かい合う2人の配置、コマ3は対比カード。
- 会話順：藍子の誤解（Ｂにも登記がないと主張できない）→時効取得者と元所有者は当事者→相手方による違い→結論（記述は×）。
- 配色：コマ3は左（元の所有者Ｂ＝当事者）だけ青✓（登記なしで主張できる）、右（第三者との関係）は印なし。
- 記事の範囲：Ａと元の所有者Ｂは、時効の効果をめぐって直接向き合う「当事者」の関係で、対抗関係に立たない／Ａは登記を備えていなくても元の所有者Ｂに時効取得を主張できる／登記が問題になるのは、あくまで第三者との関係。対比：D0414・D0412・D0411（逆の結論になる類似肢）は図に入れない。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D0413～H21-Q01ウ～

## note記事の冒頭文

ある人が、過失なく自分の土地だと信じて他人の土地を占有し続けています。この人は、登記をしなければ、元の所有者に時効取得を主張できないのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（平成21年度　第1問　ウ）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 元の所有者には、登記なしで時効取得を主張できる | 「登記なしで時効取得を主張できる」を黄色マーカー |
| コマ1 見出し | ラベル | ①　よくある思い込み | — |
| コマ1 図 | 図・カード | 甲土地 / Ａ / 占有を続けている / Ｂ / 元の所有者 / 登記が要る？ / Ａ（占有者）　Ｂ（元の所有者） | — |
| コマ1 | 藍子（左・先に話す） | Ｂにも、登記がないと時効取得を主張できませんよね？ | 「登記がないと主張できませんよね？」 |
| コマ1 | トリ先生（右・答える） | 出たわね。登記が要る相手を取り違えているわよ | — |
| コマ2 見出し | ラベル | ②　ＡとＢは当事者 | — |
| コマ2 図 | 図・カード | Ａ / Ｂ / 甲土地 / 当事者の関係 / 対抗関係には立たない | — |
| コマ2 | 藍子（左・先に話す） | ＡとＢは、どんな関係なんですか？ | — |
| コマ2 | トリ先生（右・答える） | 時効の効果をめぐって向き合う、当事者の関係よ | 「当事者の関係」 |
| コマ3 見出し | ラベル | ③　登記が問題になる相手 | — |
| コマ3 図 | 図・カード | 元の所有者Ｂ（当事者） / 登記がなくても、主張できる / 第三者との関係 / 登記が問題になるのは、ここだけ | — |
| コマ3 | 藍子（左・先に話す） | じゃあ、登記が問題になるのは誰との関係ですか？ | — |
| コマ3 | トリ先生（右・答える） | あくまで第三者との関係よ。Ｂは第三者ではないわ | 「あくまで第三者との関係」 |
| コマ4 見出し | ラベル | ④　結論は× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 登記をしなければ主張できないという記述は、誤りなんですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。Ｂは当事者だから、登記なしで主張できるのよ | 「登記なしで主張できる」 |
| コマ4 チェック欄 | 3項目（青✓） | ＡとＢは当事者の関係で、対抗関係に立たない / 登記が問題になるのは、第三者との関係 / 登記がなくても、Ｂに時効取得を主張できる | — |
| 結論帯 | 1行目 | ＡとＢは当事者。登記が問題になるのは第三者との関係 | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0413　正解×（H21-Q01ウ） | — |

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers, and the full-width letters Ａ Ｂ only where specified below. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a navy business suit over a blouse with thin blue vertical stripes; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. The legal parties Ａ, Ｂ are NOT characters: draw them only as small, faceless, flat pictogram figures, each with a small round label tag containing the full-width letter given in the text plan.

ANATOMY (critical, 藍子): keep her human anatomy strictly correct in every panel: exactly one head, one torso, exactly two arms (one left, one right) and exactly two hands in total. Never draw extra arms, extra hands, extra fingers, floating hands, duplicated hands, arms that do not grow from the shoulders, or fused hands. Each hand has exactly five fingers. Check that every shoulder, elbow, and wrist connects naturally. HAND COUNT RULE: before drawing each panel, assign both of 藍子's hands a job (for example, one hand points while the other hand holds the clipboard or hangs at her side; or one hand touches her chin while the other holds the clipboard; or both hands are raised in a small cheer). When she points, only ONE arm points; her other hand must not be clasped, raised, or clenched at the same time, so there are never three hands in a panel. POSE: change 藍子's pose from panel to panel (for example standing, sitting, leaning forward, resting a hand on her chin) and use a different set of poses each time this image is generated. CONTENT: in each panel, express through the diagram, labels, and scene the elements a reader needs in order to understand this article's content and pass the land and building surveyor exam, without adding any text beyond the given strings.

FIXED POSITIONS AND SPEECH BUBBLES: In all four panels 藍子 (the student) stands on the LEFT side of the panel and トリ先生 (the teacher) stands on the RIGHT side. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

CONTINUITY: any object, label, ribbon, tag, or figure that appears in more than one panel keeps the same look, the same color, and the same label text in every panel in which it appears (for example, a ribbon on a plot of land does not disappear after a step of the diagram), unless that panel's own description says that it changes. Every speech bubble's line breaks follow phrase boundaries as written inside its quotation marks; never split a word across lines.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall).

TITLE BANNER: text 「元の所有者には、登記なしで時効取得を主張できる」 in large bold letters; the part 「登記なしで時効取得を主張できる」 has a yellow highlighter marker.

PANEL 1 (藍子 confident, トリ先生 exasperated but caring; 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　よくある思い込み」
- Small diagram in the middle: a flat plot-of-land block labeled 「甲土地」 with a faceless pictogram tag 「Ａ」 standing on it (small label 「占有を続けている」), and a faceless pictogram tag 「Ｂ」 standing beside it (small label 「元の所有者」). A small question badge above the plot reads 「登記が要る？」 (a question badge only, with no check mark and no cross). Caption under the diagram: 「Ａ（占有者）　Ｂ（元の所有者）」.
- 藍子 bubble (left, spoken first): 「Ｂにも、登記がないと
時効取得を主張
できませんよね？」 with the part 「登記がないと主張できませんよね？」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
登記が要る相手を
取り違えているわよ」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (藍子 puzzled, トリ先生 explaining with a wing-pointer; 藍子's hands: one hand touches her chin and the other holds the clipboard at her side (two hands in total)):
- Label tab: 「②　ＡとＢは当事者」
- Two faceless pictograms with tags 「Ａ」 and 「Ｂ」 face each other across the plot block 「甲土地」, with no arrow between them.
- A dark navy tag between them reads 「当事者の関係」, and a small tag under it reads 「対抗関係には立たない」.
- 藍子 bubble (left, spoken first): 「ＡとＢは、
どんな関係なんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「時効の効果をめぐって
向き合う、
当事者の関係よ」 with the part 「当事者の関係」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 3 (both characters point together at the same figure; 藍子 realizing; 藍子's hands: ONE hand points at the diagram with an extended arm and the other hand hangs at her side or holds the clipboard; her hands are NOT clasped and no third hand appears):
- Label tab: 「③　登記が問題になる相手」
- Left card, heading 「元の所有者Ｂ（当事者）」, body 「登記がなくても、主張できる」, with ONE blue check mark only (no cross on this card).
- Right card, heading 「第三者との関係」, body 「登記が問題になるのは、ここだけ」, with no mark on this card.
- 藍子 bubble (left, spoken first): 「じゃあ、登記が
問題になるのは
誰との関係ですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「あくまで第三者との
関係よ。
Ｂは第三者ではないわ」 with the part 「あくまで第三者との関係」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は×」
- 藍子 bubble (left, spoken first): 「登記をしなければ
主張できないという
記述は、
誤りなんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。
Ｂは当事者だから、
登記なしで主張できるのよ」 with the part 「登記なしで主張できる」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark: 「ＡとＢは当事者の関係で、対抗関係に立たない」, 「登記が問題になるのは、第三者との関係」, 「登記がなくても、Ｂに時効取得を主張できる」.

CONCLUSION BANNER (strong contrasting solid color, large text, two lines):
- Line 1: 「ＡとＢは当事者。登記が問題になるのは第三者との関係」 with a yellow highlighter marker.
- Line 2: 「問題D0413　正解×（H21-Q01ウ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm 藍子 is always on the left and トリ先生 always on the right and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 効, 占, 地, 対, 張, 当, 所, 抗, 登, 解, 記, 違 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 時効で取得した土地を | 薄い黄色のマーカー |
| タイトル2行目 | 元の所有者に主張できる？ | 「主張できる？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D0413　H21-Q01ウ | — |

### 見出し画像プロンプト本体

```text
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the two characters at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): follow the attached character-specification images exactly and do not redesign them. トリ先生 is the chubby bird teacher (round red glasses, blue shirt, red neckerchief), placed at the lower left of center. 藍子 is the young woman exam candidate (long wavy brown hair, blouse with thin blue vertical stripes, navy suit), placed at the lower right of center. POSES ARE NOT FIXED: do not copy any pose from the attached images or from earlier header images; let each character take a free, natural pose of your own choosing that fits the topic and suits the character (for example standing, sitting, leaning, gesturing, or holding a small prop), and choose a different pose each time this image is generated. Keep both characters fully visible, with their faces clear of the title text, and keep 藍子's hairstyle exactly as in the attached images. Keep 藍子's human anatomy strictly correct: exactly one head, one torso, two arms (one left, one right) and two hands in total, each hand with exactly five fingers; never draw extra arms, hands, or fingers, floating or duplicated hands, arms not growing from the shoulders, or fused hands; check that every shoulder, elbow, and wrist connects naturally.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and the Arabic numeral 4; the only Latin letters and digits allowed are those in the subtitle exactly as written below. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it:
時効で取得した土地を
Line 2 is larger; the phrase 主張できる？ is red-orange and the rest is dark navy:
元の所有者に主張できる？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D0413　H21-Q01ウ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a plot of land with a long calendar strip of many blank pages beside it
Right side: two faceless silhouettes facing each other across a small fence

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 時, 効, 取, 得, 土, 地, 元, 所, 有, 者, 主, 張, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D0413～H21-Q01ウ～.png |
| 見出し画像（採用版） | 4コマ解説図解D0413～H21-Q01ウ～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D0413～H21-Q01ウ～_v01.png ／ 4コマ解説図解D0413～H21-Q01ウ～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0413_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：Ａ・Ｂはコマ1で人型タグ付きで紹介され、コマ2〜4で同じ位置関係（Ａ＝左、Ｂ＝右）
- [ ] 工程C：構成表の全文言を記事（H21-Q01ウ）と突き合わせ：「当事者」「対抗関係に立たない」「登記が問題になるのは、あくまで第三者との関係」
- [ ] 工程C：コマ3は青✓1つだけで、右カードに印がない。結論は×（登記をしなければ主張できないという記述が誤り）

## 生成後の照合チェック（文言の正本は上の構成表）
- [ ] 4コマ縦一列／タイトル帯・結論帯あり
- [ ] 全コマで藍子＝左・トリ先生＝右、全吹き出しの尾が話者へ向く。藍子の髪型が全コマで同じ
- [ ] タイトル・全セリフ・ラベルが構成表と一字一句一致
- [ ] スタンプ・矢印・ラベルが各カードの枠の内側に収まっている
- [ ] 色：はい・○＝青、いいえ・×＝赤、中立＝ネイビー。対比カードは左右で逆の極性
- [ ] 簡体字・英字なし、背景が不透明
- [ ] 記事の文言から外れていない（独自の理由づけなし）

## 改訂履歴（このファイルは `manga_specs.py` から生成。直すときは設計データを直して再生成する）

- 2026-10-07 v01：初版（v2ルール：吹き出しの改行、コマ間の継続、人体構造・手の割り当てを適用）
