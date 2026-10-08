# D0314 4コマ解説図解 プロンプト（ChatGPT貼付用・試作B）

- 肢：D0314（民法／用益権・担保物権、出典 H20-Q01イ）。正解＝×（誤った記述）。誤解未習得2回（？が2回連続）。
- 記事：`note-articles/h20-mondai/q01-fudousan-shichi.md` イ「不動産質でも、設定者の承諾なく転質ができる」（冒頭の説明と肢ウも使う）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- タイプ：G 押さえどころ型（もう間違えないための3点を、質権の基本→転質の仕組み→同じ型の肢→暗記3点の順で見せる）。D0314 v02（事案→説明→ひっかけと勘違い→結論）とは別パターン。コマの使い方：コマ1＝aiko（質権の姿の比較図を大きく）、コマ2＝none（お金の流れ図）、コマ3＝tori（同じ型の肢イ・ウを並べる）、コマ4＝両方。
- ユーザーの困りごと：不動産質権・転質の理解が難しい。そのため、①質権は占有を質権者に移す（抵当権との違い。記事冒頭）、②転質は質権者Ｂがお金を借りる話でＡは関係しない（記事の具体例）、③同じ問のウ（使用・収益）も承諾なしでできる、の3段階で理解できる図にする。
- ①問いの事案：Ａの別荘にＢが質権を持ち、Ｂが自分がＣからお金を借りるために、その質権を担保に使う（転質）。
- ②出題者のねらい：転質に、設定者の承諾は要るか（コマ2のタグ）。
- ③ひっかけ：肢イもウも「設定者の承諾を得なければ、…できない」という同じ言い方で、どちらも誤り（コマ3のリボン。記事の問題文）。
- ④勘違い：転質も設定者の承諾が要る（コマ1の藍子の台詞）。
- ⑤正しい整理（暗記3点）：不動産質権は占有を質権者に移す／転質は自己の責任でできて承諾は不要（民法348条）／損失は不可抗力まで質権者の責任（コマ4）。
- 登場人物：Ａ（設定者）・Ｂ（質権者）・Ｃ（Ｂにお金を貸す人）をコマ1で人型タグ付きで左から順に紹介し、コマ2でも同じタグを使う。
- 線の意味：矢印は使わず、矢印のない細い線とラベルで関係を見せる。コマ1の比較図・コマ3のカードは印を付けない。青✓はコマ4のチェック3点だけ。
- 記事の範囲：不動産質権は占有を質権者に移す（抵当権は移さない）／質権者は使用・収益ができる（民法356条）／転質（責任転質、民法348条）／設定者の承諾は不要／転質の損失は不可抗力まで質権者が責任を負う。独自の理由づけは足さない。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D0314～H20-Q01イ～

## note記事の冒頭文

不動産質権を持つ質権者が、その不動産についてさらに転質をしたいと考えています。転質をするには、設定者の承諾を得なければならないのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（平成20年度　第1問　イ）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 転質は、承諾なしでできる | 「承諾なし」を黄色マーカー |
| コマ1 見出し | ラベル | ①　まず、不動産質権の姿 | — |
| コマ1 図 | 図・カード | 抵当権 / 占有を移さない / 不動産質権 / 占有を質権者に移す / 使って収益もできる / Ａ / 設定者 / Ｂ / 質権者 / Ｃ / Ｂにお金を貸す人 / Ｂが転質するのに、Ａの承諾は要る？ | — |
| コマ1 | 藍子（左・先に話す） | 転質も、設定者の承諾が要りますよね？ | — |
| コマ2 見出し | ラベル | ②　転質は、Ｂがお金を借りる話 | — |
| コマ2 図 | 図・カード | 出題者のねらい / 転質に、設定者の承諾は要るか / Ａ / 設定者 / Ａに断らなくてよい / Ｂ / 質権者 / Ａの別荘 / Ｂの質権 / Ｃ / Ｂにお金を貸す人 / お金を借りる / Ｂの質権を担保に使う / 質権の存続期間内に、自己の責任で、質物にさらに質権を設定する　＝　転質（責任転質、民法348条） | — |
| コマ3 見出し | ラベル | ③　承諾が要らないのは、転質だけではない | — |
| コマ3 図 | 図・カード | 転質 / 民法348条 / 質物にさらに質権を設定できる / 使用・収益 / 民法356条 / 用法に従って使い、収益を得られる / 承諾なしでできる / ひっかけ：イもウも、承諾を得なければ、という言い方 | — |
| コマ3 | トリ先生（右・答える） | イもウも、承諾なしでできるのよ | 「承諾なし」 |
| コマ4 見出し | ラベル | ④　もう間違えない3つの押さえどころ | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 承諾が要る、という記述は、誤りなんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。転質は承諾なしでできるのよ | 「承諾なしで」 |
| コマ4 チェック欄 | 3項目（青✓） | 不動産質権は、占有を質権者に移す / 転質は、自己の責任でできる。承諾は不要（民法348条） / 転質の損失は、不可抗力まで質権者が責任を負う | — |
| 結論帯 | 1行目 | 転質に、設定者の承諾は要らない | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0314　正解×（H20-Q01イ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 民法356条

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers, and the full-width letters Ａ Ｂ Ｃ only where specified below. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a collared light-blue blouse with thin blue pinstripes (sleeves rolled up) and a navy pencil skirt with navy pumps, no jacket, often holding a navy clipboard and a pencil; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. The legal parties Ａ, Ｂ, Ｃ are NOT characters: draw them only as small, faceless, flat pictogram figures, each with a small round label tag containing the full-width letter given in the text plan.

ANATOMY (critical, 藍子): keep her human anatomy strictly correct in every panel: exactly one head, one torso, exactly two arms (one left, one right) and exactly two hands in total. Never draw extra arms, extra hands, extra fingers, floating hands, duplicated hands, arms that do not grow from the shoulders, or fused hands. Each hand has exactly five fingers. Check that every shoulder, elbow, and wrist connects naturally. HAND COUNT RULE: before drawing each panel, assign both of 藍子's hands a job (for example, one hand points while the other hand holds the clipboard or hangs at her side; or one hand touches her chin while the other holds the clipboard; or both hands are raised in a small cheer). When she points, only ONE arm points; her other hand must not be clasped, raised, or clenched at the same time, so there are never three hands in a panel. POSE: change 藍子's pose from panel to panel (for example standing, sitting, leaning forward, resting a hand on her chin) and use a different set of poses each time this image is generated. CONTENT: in each panel, express through the diagram, labels, and scene the elements a reader needs in order to understand this article's content and pass the land and building surveyor exam, without adding any text beyond the given strings.

FIXED POSITIONS AND SPEECH BUBBLES: In every panel in which a character appears, 藍子 (the student) stands on the LEFT side and トリ先生 (the teacher) stands on the RIGHT side. A panel does not have to show both characters: when the diagram, the flowchart, or the items to memorize need more space, the PANEL line may show only one of the two characters, or show both very small; in that case follow the PANEL line, and a character who is not drawn has no speech bubble. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

CONTINUITY: any object, label, ribbon, tag, or figure that appears in more than one panel keeps the same look, the same color, and the same label text in every panel in which it appears (for example, a ribbon on a plot of land does not disappear after a step of the diagram), unless that panel's own description says that it changes. Every speech bubble's line breaks follow phrase boundaries as written inside its quotation marks; never split a word across lines.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall).

TITLE BANNER: text 「転質は、承諾なしでできる」 in large bold letters; the part 「承諾なし」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; ONLY 藍子 appears in this panel (no トリ先生), standing at the left and smaller than usual, so that the diagram can be drawn large; 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　まず、不動産質権の姿」
- A large comparison diagram fills the panel: two columns side by side in the same light gray with dark navy outlines and no marks. Left column: heading 「抵当権」, body 「占有を移さない」. Right column: heading 「不動産質権」, body 「占有を質権者に移す」, with a small yellow tag 「使って収益もできる」.
- Under the two columns, a row, laid out ONE row from left to right, of three small faceless flat pictogram figures in the same light gray-blue color, each with a small dark navy round tag and a short label: 「Ａ」 (label 「設定者」), 「Ｂ」 (label 「質権者」), 「Ｃ」 (label 「Ｂにお金を貸す人」).
- A small question badge 「Ｂが転質するのに、Ａの承諾は要る？」 sits at the top (a question badge only, with no check mark and no cross). Draw no question-mark icon, exclamation icon, or any other symbol anywhere else in the panel.
- 藍子 bubble (left, spoken first): 「転質も、設定者の
承諾が要りますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (explanatory, steady mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　転質は、Ｂがお金を借りる話」
- A full-width flow diagram fills the panel, with a small dark navy tag 「出題者のねらい」 at the top left and a line beside it: 「転質に、設定者の承諾は要るか」.
- Laid out ONE row from left to right: at the far left the pictogram 「Ａ」 (label 「設定者」) inside a dashed frame with the small note 「Ａに断らなくてよい」; in the middle the pictogram 「Ｂ」 (label 「質権者」) beside one flat house icon labeled 「Ａの別荘」 that carries a dark navy ribbon with white text 「Ｂの質権」; at the far right the pictogram 「Ｃ」 (label 「Ｂにお金を貸す人」).
- Between Ｂ and Ｃ run two plain thin dark navy lines (no arrowheads), one with the small label 「お金を借りる」 and one with the small label 「Ｂの質権を担保に使う」.
- At the bottom, one wide dark navy band with white text 「質権の存続期間内に、自己の責任で、質物にさらに質権を設定する　＝　転質（責任転質、民法348条）」.

PANEL 3 (explanatory, steady mood; ONLY トリ先生 appears in this panel (no 藍子), standing at the right and smaller than usual, so that the diagram or the items to memorize can be drawn large):
- Label tab: 「③　承諾が要らないのは、転質だけではない」
- Two cards side by side in the same light gray with dark navy outlines and no marks. Left card: heading 「転質」, small tag 「民法348条」, body 「質物にさらに質権を設定できる」. Right card: heading 「使用・収益」, small tag 「民法356条」, body 「用法に従って使い、収益を得られる」. Each card carries the same small yellow tag 「承諾なしでできる」.
- Under the two cards, one wide dark navy ribbon with large white text 「ひっかけ：イもウも、承諾を得なければ、という言い方」.
- The two cards have clearly different texts; the texts are NOT identical.
- トリ先生 bubble (right, spoken as the answer): 「イもウも、
承諾なしでできるのよ」 with the part 「承諾なし」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　もう間違えない3つの押さえどころ」
- 藍子 bubble (left, spoken first): 「承諾が要る、という
記述は、
誤りなんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。転質は
承諾なしで
できるのよ」 with the part 「承諾なしで」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark: 「不動産質権は、占有を質権者に移す」, 「転質は、自己の責任でできる。承諾は不要（民法348条）」, 「転質の損失は、不可抗力まで質権者が責任を負う」.

CONCLUSION BANNER (strong contrasting solid color, large text, two lines):
- Line 1: 「転質に、設定者の承諾は要らない」 with a yellow highlighter marker.
- Line 2: 「問題D0314　正解×（H20-Q01イ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two very small characters are drawn as specified and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 保, 占, 当, 承, 抗, 抵, 押, 権, 物, 解, 記, 諾, 違, 間 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that every panel marked as having no character contains no character and no speech bubble; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 不動産質の質権者が転質 | 薄い黄色のマーカー |
| タイトル2行目 | どこを押さえれば間違えない？ | 「間違えない？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D0314　H20-Q01イ | — |

### 見出し画像プロンプト本体

```text
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the two characters at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): follow the attached character-specification images exactly and do not redesign them. トリ先生 is the chubby bird teacher (round red glasses, blue shirt, red neckerchief), placed at the lower left of center. 藍子 is the young woman exam candidate (long wavy brown hair, pinstriped light-blue blouse with rolled sleeves, navy pencil skirt, no jacket), placed at the lower right of center. POSES ARE NOT FIXED: do not copy any pose from the attached images or from earlier header images; let each character take a free, natural pose of your own choosing that fits the topic and suits the character (for example standing, sitting, leaning, gesturing, or holding a small prop), and choose a different pose each time this image is generated. Keep both characters fully visible, with their faces clear of the title text, and keep 藍子's hairstyle exactly as in the attached images. Keep 藍子's human anatomy strictly correct: exactly one head, one torso, two arms (one left, one right) and two hands in total, each hand with exactly five fingers; never draw extra arms, hands, or fingers, floating or duplicated hands, arms not growing from the shoulders, or fused hands; check that every shoulder, elbow, and wrist connects naturally.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and the Arabic numeral 4; the only Latin letters and digits allowed are those in the subtitle exactly as written below. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it:
不動産質の質権者が転質
Line 2 is larger; the phrase 間違えない？ is red-orange and the rest is dark navy:
どこを押さえれば間違えない？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D0314　H20-Q01イ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a small villa house with a plain ribbon tag and a faceless silhouette beside it
Right side: two blank document sheets passing from one hand to another hand

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 不, 動, 産, 質, 権, 者, 転, 押, 間, 違, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D0314～H20-Q01イ～.png |
| 見出し画像（採用版） | 4コマ解説図解D0314～H20-Q01イ～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D0314～H20-Q01イ～_v01.png ／ 4コマ解説図解D0314～H20-Q01イ～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0314_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で質権の姿、コマ2で転質のお金の流れ、コマ3で同じ型の肢（イ・ウ）、コマ4で暗記3点が分かり、「次に同じ問が出たらどこを見るか」が言える
- [ ] 工程C：5点が、コマ1の藍子の台詞（勘違い）、コマ2の「出題者のねらい」タグと流れ図（事案）、コマ3の「ひっかけ」リボン、コマ4のチェック3点（正しい整理）として読み取れる
- [ ] 工程C：構成表の全文言を記事（H20-Q01の冒頭の説明・イ・ウ）と突き合わせ：占有を移す／使って収益／民法348条／民法356条／自己の責任で／不可抗力によるものまで
- [ ] 工程C：コマの使い方が隣り合うコマで同じにならない（aiko→none→tori→両方）。コマ3を「ひっかけと勘違い」の比較カードにしていない

## 生成後の照合チェック（文言の正本は上の構成表）
- [ ] 4コマ縦一列／タイトル帯・結論帯あり
- [ ] 全コマで藍子＝左・トリ先生＝右、全吹き出しの尾が話者へ向く。藍子の髪型が全コマで同じ
- [ ] タイトル・全セリフ・ラベルが構成表と一字一句一致
- [ ] スタンプ・矢印・ラベルが各カードの枠の内側に収まっている
- [ ] 色：はい・○＝青、いいえ・×＝赤、中立＝ネイビー。対比カードは左右で逆の極性
- [ ] 簡体字・英字なし、背景が不透明
- [ ] 記事の文言から外れていない（独自の理由づけなし）
- [ ] 顔アイコン・小さなキャラが指定の大きさ。キャラなしのコマにキャラ・吹き出しがない
- [ ] 図の部品（人物・バー・領域・タグ）の色が指定どおり（意味のない青・赤・緑・ピンクがない）。人物の頭の上に余計な印がない
- [ ] 台詞の綴りが一字一句正本どおり（特に「原則」「まとめて」など崩れやすい語）

## 試作B（2026-10-09）：D0314 v02が「ひっかけと勘違い」のコマ3を使う定型だったのに対し、ユーザー指示で、不動産質権・転質の理解を助ける『押さえどころ型』の別パターンとして作成。記事冒頭の説明（占有を移す・抵当権との違い）と肢ウ（使用・収益）を使う（同じ記事の範囲）。独自の理由づけは足していない。ChatGPTでの生成・検品はまだ。

## 改訂履歴（このファイルは `manga_specs.py` から生成。直すときは設計データを直して再生成する）

- 2026-10-09 試作B：初版（コマ3をひっかけと勘違いにせず、同じ型の肢イ・ウの並置にした）
