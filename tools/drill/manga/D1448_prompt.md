# D1448 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

- 肢：D1448（不動産登記法／申請総論（申請情報・添付情報・代理・却下取下・還付・電子申請・登記識別情報）、出典 R01-Q08ア）。正解＝×（誤った記述）。誤解3回。
- 記事：`note-articles/r1-mondai/q08-shinsei-tenpu.md` ア「会社法人等番号を提供すれば、支配人の権限を証する登記事項証明書は省略できる」
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- タイプ：F 手続・添付情報型（番号で足りるか、証明書が要るか）。コマの使い方：コマ1＝small（事案図を大きく）、コマ2＝none（2つのやり方を並べた図だけ）、コマ3＝faces（顔アイコンの会話＋勘違い⇔正しい整理のカード）、コマ4＝両方。
- ①問いの事案：会社法人等番号を持つ法人が所有する土地の、地目の変更の登記を、その法人の支配人が代理して申請する。支配人の権限を証する登記事項証明書を提供しなければならないか。
- ②出題者のねらい：会社法人等番号を提供する場合と、登記事項証明書を提供する場合を見分けさせる。
- ③ひっかけ：問題文の「登記所が同一であり、指定登記所以外のものでない限り」という条件づけに引かれて、番号があっても証明書が要る場面があると思わせる。
- ④勘違い・理解を誤るポイント：番号があっても、登記所が同一などの条件を満たさない限り、証明書を提供しなければならない（番号による省略の原則を狭めている）。
- ⑤正しい整理：会社法人等番号を有する法人は、その番号を提供するのが原則（令7条1項1号イ）。支配人などが法人を代理して申請するときは、代理人の権限を証する情報の提供を要しない（令7条1項2号、規則36条3項）。登記事項証明書を提供するのは、会社法人等番号の提供に代えて証明書を提供する場合（規則36条1項2号）。記事の具体例：会社の支配人が会社所有地の地目変更を申請するとき、申請情報に会社法人等番号を書いておけば、支配人の権限を証明する登記事項証明書を取り寄せて添付しなくてよい。
- 登場人物：当事者の記号は使わない。「法人（会社）」と「支配人」を文字ラベルの人型タグで、コマ1で紹介してから使う。
- 矢印の意味：矢印は使わない。コマ2は2つのカードを縦の仕切り線で分ける。
- 配色：コマ2は印を付けない。コマ3は左（条件を満たさない限り証明書が要る）＝赤✕1つ、右（番号を提供すれば証明書は要らない）＝青✓1つ。コマ1・2は印を付けない。
- 記事の範囲：会社法人等番号の提供（令7条1項1号イ）／支配人が代理して申請する場合の代理人の権限を証する情報の不提供（令7条1項2号、規則36条3項）／証明書の提供は番号に代える場合（規則36条1項2号）／会社の支配人が地目変更を申請する例のみ。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D1448～R01-Q08ア～

## note記事の冒頭文

会社法人等番号を持つ法人の所有する土地について、支配人が代理して、地目の変更の登記を申請します。登記所が同一などの条件を満たさない限り、支配人の権限を証する登記事項証明書を提供しなければならないのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（令和元年度　第8問　ア）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 番号を提供すれば、支配人の証明書は要らない | 「支配人の証明書は要らない」を黄色マーカー |
| コマ1 見出し | ラベル | ①　問いの事案 | — |
| コマ1 図 | 図・カード | 法人（会社） / 会社法人等番号あり / 支配人 / 会社所有の土地 / 地目の変更の登記を、支配人が代理して申請 / 支配人の権限を証する証明書は要る？ | — |
| コマ1 | 藍子（左・先に話す） | 支配人が申請するなら、証明書が要りますよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。番号を提供したか見てごらん | 「番号を提供」 |
| コマ2 見出し | ラベル | ②　出題者のねらい | — |
| コマ2 図 | 図・カード | 出題者のねらい / 番号で足りるのか、証明書が要るのかを見分ける / 会社法人等番号を提供する / 令7条1項1号イ / 原則。支配人が代理して申請するときは、代理人の権限を証する情報は要らない（令7条1項2号、規則36条3項） / 登記事項証明書を提供する / 規則36条1項2号 / 会社法人等番号の提供に代えて、証明書を提供する場合 | — |
| コマ3 見出し | ラベル | ③　ひっかけと勘違い | — |
| コマ3 図 | 図・カード | よくある勘違い / 登記所が同一などの条件を満たさない限り、証明書が要る / ひっかけ：登記所が同一でない限り、という条件づけ / 正しい整理 / 会社法人等番号を提供すれば、支配人の権限を証する証明書は要らない / たとえば：会社の支配人が会社所有地の地目変更を申請するとき、申請情報に会社法人等番号を書いておけば、証明書を取り寄せて添付しなくてよい | — |
| コマ3 | 藍子（左・1番目） | 登記所が同じでないと、省けませんよね？ | — |
| コマ3 | トリ先生（右・2番目） | 番号の省略の原則を、狭めているわね | 「狭めている」 |
| コマ3 | 藍子（左・3番目） | では、何を提供すれば足りますか？ | — |
| コマ3 | トリ先生（右・4番目） | 会社法人等番号を提供すれば足りるのよ | 「会社法人等番号」 |
| コマ4 見出し | ラベル | ④　結論は× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 条件つきで証明書が要る、は誤りなんですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。番号を提供すれば足りるのよ | 「番号を提供すれば足りる」 |
| コマ4 チェック欄 | 3項目（青✓） | 会社法人等番号を提供するのが原則（令7条1項1号イ） / 支配人が代理して申請するときは、代理人の権限を証する情報は要らない（令7条1項2号、規則36条3項） / 証明書を提供するのは、番号の提供に代える場合（規則36条1項2号） | — |
| 注記 | 小さな注記（コマ4の下） | 肢の登記所の条件は、平成27年の規則改正前の言い回しです | — |
| 結論帯 | 1行目 | 会社法人等番号を提供すれば、支配人の権限を証する証明書は要らない | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1448　正解×（R01-Q08ア） | — |

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a collared light-blue blouse with thin blue pinstripes (sleeves rolled up) and a navy pencil skirt with navy pumps, no jacket, often holding a navy clipboard and a pencil; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. Organizations and buildings in the diagrams are NOT characters: draw them only as simple, faceless, flat icons with the exact text labels given below.

ANATOMY (critical, 藍子): keep her human anatomy strictly correct in every panel: exactly one head, one torso, exactly two arms (one left, one right) and exactly two hands in total. Never draw extra arms, extra hands, extra fingers, floating hands, duplicated hands, arms that do not grow from the shoulders, or fused hands. Each hand has exactly five fingers. Check that every shoulder, elbow, and wrist connects naturally. HAND COUNT RULE: before drawing each panel, assign both of 藍子's hands a job (for example, one hand points while the other hand holds the clipboard or hangs at her side; or one hand touches her chin while the other holds the clipboard; or both hands are raised in a small cheer). When she points, only ONE arm points; her other hand must not be clasped, raised, or clenched at the same time, so there are never three hands in a panel. POSE: change 藍子's pose from panel to panel (for example standing, sitting, leaning forward, resting a hand on her chin) and use a different set of poses each time this image is generated. CONTENT: in each panel, express through the diagram, labels, and scene the elements a reader needs in order to understand this article's content and pass the land and building surveyor exam, without adding any text beyond the given strings.

FIXED POSITIONS AND SPEECH BUBBLES: In every panel in which a character appears, 藍子 (the student) stands on the LEFT side and トリ先生 (the teacher) stands on the RIGHT side. A panel does not have to show both characters: when the diagram, the flowchart, or the items to memorize need more space, the PANEL line may show only one of the two characters, show both at the normal size at the two outer edges, show both as small face icons in a vertical conversation column, or show both very small; in that case follow the PANEL line and its LAYOUT lines, and a character who is not drawn has no speech bubble; in a panel marked as face icons, each character appears only as a small round face icon inside the vertical conversation column described in the LAYOUT lines, with exactly one face icon for each speech bubble and never more face icons than bubbles. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

CONTINUITY: any object, label, ribbon, tag, or figure that appears in more than one panel keeps the same look, the same color, and the same label text in every panel in which it appears (for example, a ribbon on a plot of land does not disappear after a step of the diagram), unless that panel's own description says that it changes. Every speech bubble's line breaks follow phrase boundaries as written inside its quotation marks; never split a word across lines.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall). Between panel 4 and the conclusion banner, a thin one-line note strip (about 50 px tall) with small text, as given in the NOTE LINE below.

TITLE BANNER: text 「番号を提供すれば、支配人の証明書は要らない」 in large bold letters; the part 「支配人の証明書は要らない」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear VERY SMALL (each about 110 px tall in total, clearly smaller than the full-size characters in the other panels, never more than one third of the panel height), 藍子 at the lower left corner and トリ先生 at the lower right corner, so that the diagram or the items to memorize fill the panel; 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　問いの事案」
- A large relation diagram fills the panel: one flat office-building icon labeled 「法人（会社）」 with a small tag 「会社法人等番号あり」, and one faceless pictogram tag in light gray-blue labeled 「支配人」 standing beside it.
- Beside them, a plot-of-land block labeled 「会社所有の土地」 with a white card 「地目の変更の登記を、支配人が代理して申請」.
- A small question badge 「支配人の権限を証する証明書は要る？」 sits at the top (a question badge only, with no check mark and no cross).
- 藍子 bubble (left, spoken first): 「支配人が申請するなら、
証明書が要りますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
番号を提供したか
見てごらん」 with the part 「番号を提供」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　出題者のねらい」
- A full-width concept diagram fills the whole panel, with a small dark navy tag 「出題者のねらい」 at the top left and a line beside it: 「番号で足りるのか、証明書が要るのかを見分ける」.
- Two large cards side by side, both with the same pale gray fill, a dark navy outline, and a dark navy heading, separated by a tall plain dark navy divider line (no arrow). Left card, heading 「会社法人等番号を提供する」, small tag 「令7条1項1号イ」, body 「原則。支配人が代理して申請するときは、代理人の権限を証する情報は要らない（令7条1項2号、規則36条3項）」. Right card, heading 「登記事項証明書を提供する」, small tag 「規則36条1項2号」, body 「会社法人等番号の提供に代えて、証明書を提供する場合」.
- There is no check mark and no cross anywhere in this panel.

PANEL 3 (surprised then convinced mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　ひっかけと勘違い」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.
- Two large cards side by side, with a wide example strip under them.
- Left card, heading 「よくある勘違い」, body 「登記所が同一などの条件を満たさない限り、証明書が要る」, with ONE red cross only (no check mark on this card); a dark navy ribbon tag under the body, with large white text, reads 「ひっかけ：登記所が同一でない限り、という条件づけ」.
- Right card, heading 「正しい整理」, body 「会社法人等番号を提供すれば、支配人の権限を証する証明書は要らない」, with ONE blue check mark only (no cross on this card).
- Example strip under the two cards: 「たとえば：会社の支配人が会社所有地の地目変更を申請するとき、申請情報に会社法人等番号を書いておけば、証明書を取り寄せて添付しなくてよい」.
- The two cards have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「登記所が同じでないと、
省けませんよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「番号の省略の原則を、
狭めているわね」 with the part 「狭めている」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「では、何を提供すれば
足りますか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「会社法人等番号を
提供すれば足りるのよ」 with the part 「会社法人等番号」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は×」
- 藍子 bubble (left, spoken first): 「条件つきで証明書が
要る、は
誤りなんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。
番号を提供すれば
足りるのよ」 with the part 「番号を提供すれば足りる」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「会社法人等番号を提供するのが原則（令7条1項1号イ）」, 「支配人が代理して申請するときは、代理人の権限を証する情報は要らない（令7条1項2号、規則36条3項）」, 「証明書を提供するのは、番号の提供に代える場合（規則36条1項2号）」.

NOTE LINE (small text on a thin strip between panel 4 and the conclusion banner, one line, fully legible): 「肢の登記所の条件は、平成27年の規則改正前の言い回しです」

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「会社法人等番号を提供すれば、支配人の権限を証する証明書は要らない」 with a yellow highlighter marker.
- Line 2: 「問題D1448　正解×（R01-Q08ア）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two very small characters are drawn as specified and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 代, 号, 地, 所, 権, 番, 登, 肢, 規, 解, 記, 証, 請, 違 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the left comparison card has only a red cross and the right card only a blue check mark; confirm that the word 「原則」 is spelled exactly like this everywhere (never 「思則」); confirm that the very small characters are drawn at the specified small sizes (they must not grow and squeeze the diagram) and that nothing but the given text appears above the heads of the pictograms; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 支配人が法人を代理して申請 | 薄い黄色のマーカー |
| タイトル2行目 | 証明書は要る？ | 「証明書は要る？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D1448　R01-Q08ア | — |

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
支配人が法人を代理して申請
Line 2 is larger; the phrase 証明書は要る？ is red-orange and the rest is dark navy:
証明書は要る？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D1448　R01-Q08ア
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a small office building with an empty nameplate and a faceless silhouette in a suit beside it
Right side: a blank certificate sheet and a rubber stamp beside a small registry book

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 支, 配, 人, 法, 代, 理, 申, 請, 証, 明, 書, 要, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D1448～R01-Q08ア～.png |
| 見出し画像（採用版） | 4コマ解説図解D1448～R01-Q08ア～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D1448～R01-Q08ア～_v01.png ／ 4コマ解説図解D1448～R01-Q08ア～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D1448_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1の「法人」「支配人」と、コマ2の2つのやり方、コマ3の左右のカードが対応している
- [ ] 工程C：5点が、コマ1の事案図、コマ2の「出題者のねらい」タグ、コマ3の「ひっかけ」タグと左右のカード、コマ4の暗記3点として読み取れる
- [ ] 工程C：構成表の全文言を記事（R01-Q08ア）と突き合わせ：「会社法人等番号」「令7条1項1号イ」「令7条1項2号、規則36条3項」「規則36条1項2号」「番号の提供に代えて」
- [ ] 工程C：コマの使い方が隣り合うコマで同じにならない（small→none→faces→両方）。結論は×（登記所が同一などの条件を満たさない限り証明書が要る、という記述が誤り）

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

## v01：新規作成（2026-10-09）。一問一答で誤解が3回になった肢（4コマ未作成）。条文（令7条1項1号イ・2号、規則36条1項2号・3項）は note-articles/laws/ の原文で確認した。ChatGPTでの画像生成・検品はまだ。
- 確認結果の反映（2026-10-09）：年度別記事の確認（B-6）で、肢の「登記所が同一であり、かつ、法務大臣が指定した登記所以外のもの」は、平成27年11月2日施行の改正前の不動産登記規則36条2項1号（支配人等の代理人の権限を証する情報を省略できる場合）の文言と分かった。現行の規則36条3項は、会社法人等番号を有する法人の支配人等が代理するときは登記所の同一を問わない。結論（×）は変わらない。図には、小さな注記の帯で「肢の条件は改正前の規則の言い回し」と明記した。

## 改訂履歴（このファイルは `manga_specs.py` から生成。直すときは設計データを直して再生成する）

- 2026-10-09 v01：初版（v2ルール：吹き出しの改行、コマ間の継続、人体構造・手の割り当てを適用。一発合格ルール適用）

## 第二案（B案）：構成表2とプロンプト本体2

上の構成表・プロンプト本体（第一案）は、定型の「ひっかけと勘違い」型で組んだもの。この第二案は、`D0314-B_prompt.md` と同じ型（しくみの図解→押さえどころ→本番での読み方→暗記3点。「ひっかけと勘違い」の対比カードは使わない）で組んだ別構成。どちらか1つを選んで、ChatGPTに貼る。見出し画像・記事タイトル・冒頭文は第一案と共通。第二案の本文画像は、保存名の末尾に `_B案` を付ける（例：`4コマ解説図解<ID>～<出典>～_B案.png`）。

### 設計メモ2（工程A）
- 【型の選び方】型：型2（第二案・押さえどころ）。第一案（型1）の定型ではなく、その肢の理解の壁を越える順（しくみ図→押さえどころ→本番での読み方3ステップ→暗記3点）に組んだ。
- 【出題者のひっかけ】問題文の「登記所が同一であり、指定した登記所以外のものでない限り」という条件づけ。番号があっても登記所の条件を満たさなければ支配人の権限を証する登記事項証明書が要る、と思わせ、番号による省略の原則を狭めて書いている（記事：その点で誤り）。
- 【受験者の勘違い・定着していない点】番号の提供で済むのか、証明書が別に要るのかが曖昧で、条件づけの文を見ると『条件次第で証明書が要る』と信じてしまう。支配人が法人を代理して申請するときは代理人の権限を証する情報が要らないこと、証明書の提供は番号に代える場合であることが定着していない。
- 【対比する制度】「会社法人等番号を提供」⇔「登記事項証明書を提供」：会社法人等番号を提供する場合は、支配人の権限を証する証明書を別に提供しなくてよい（令7条1項1号イ、令7条1項2号、規則36条3項）／登記事項証明書を提供するのは、会社法人等番号の提供に代えて証明書を提供する場合だけ（規則36条1項2号）（番号を提供するのに証明書も別に要る、という結論が逆の肢が本肢）。
- 【第二案の位置づけ】第一案（定型：事案→出題者のねらい→ひっかけと勘違い→結論）とは別に、`D0314-B_prompt.md` と同じ型（しくみの図解→押さえどころ→本番での読み方→暗記3点）で組んだ別構成。「ひっかけと勘違い」の左右の対比カード（赤✕・青✓）は使わない。
- 【理解の壁】初見の読者は、「法人についての番号」と「支配人の権限を証する登記事項証明書」が別々の書類で、番号があっても証明書が別に要りそうに見える。肢の「登記所が同一であり、指定した登記所以外のものでない限り」という条件づけも、番号の省略に歯止めがあるように読める。→ 番号の提供が原則で、証明書は番号に代える場合だけ、という位置づけが見えない。
- 【定型からの変更点】①コマ1を「問いの事案」ではなく、法人・支配人・登記所の関係図（誰が誰を代理して何を提供するか）にする。②コマ2を「番号」と「証明書」の位置づけ（に代えて）と、支配人が代理するときの扱いの帯にする（第一案の「2つの提供のしかたを仕切り線で並べた図」とは、『に代えて』でつなぐ点と、下に支配人の帯を置く点で変えた）。③コマ3を、本番で条件づけの語に引かれないための読み方3ステップにする（ひっかけは、ステップ3の紺のリボンに問題文の言い回しを引用して入れる）。④コマ4は暗記3点と結論。
- 押さえどころ（記事の範囲）：(1) 会社法人等番号を有する法人が申請するときは、その番号を提供するのが原則（令7条1項1号イ）。(2) 支配人などが法人を代理して申請するときは、代理人の権限を証する情報の提供を要しない（令7条1項2号、規則36条3項）。(3) 登記事項証明書を提供するのは、会社法人等番号の提供に代えて証明書を提供する場合（規則36条1項2号）。(4) 記事のまとめ：肢は、番号があっても一定の登記所要件を満たさない限り証明書を提供しなければならない、と述べており、番号による省略の原則を狭めている点で誤り。
- 記事の具体例を使う：ある会社の支配人が会社所有地の地目変更を申請するとき、申請情報に会社法人等番号を書いておけば、支配人の権限を証明する登記事項証明書を取り寄せて添付しなくてよい。
- 登場人物：当事者の記号は使わない。「法人（会社）」「支配人」「登記所」を、コマ1で文字ラベルつきで紹介してから使う（人物は支配人の人型タグだけで、全員同じ薄い灰青）。
- 矢印の意味：コマ1の矢印は1本だけで、『申請情報を提供して登記を申請する』という意味（支配人から登記所へ）。法人と支配人のあいだは矢印でなく矢印のない細い線（ラベル『代理』）。コマ2・3は矢印を使わない（コマ2の『に代えて』は矢印のない小さなラベル）。
- 配色：コマ1〜3は印（✓✕）を付けない。コマ4の暗記3点だけ青✓。人物は薄い灰青、カードは薄い灰色・濃紺の枠・濃紺の見出し、帯・リボンは濃紺（白文字）、強調は黄色マーカーだけ。
- コマの使い方：コマ1＝side（キャラは通常の大きさ。図は中央）（関係図を大きく）、コマ2＝none（番号と証明書の位置づけの図だけ）、コマ3＝faces（顔アイコンの会話＋3ステップのカード）、コマ4＝両方。
- 記事の範囲：会社法人等番号の提供（令7条1項1号イ）／支配人が代理して申請する場合の代理人の権限を証する情報の不提供（令7条1項2号、規則36条3項）／証明書の提供は番号に代える場合（規則36条1項2号）／会社の支配人が地目変更を申請する例のみ。

### 構成表2（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 番号で足りる。証明書は番号に代える場合だけ | 「番号に代える場合だけ」を黄色マーカー |
| コマ1 見出し | ラベル | ①　申請のしくみ | — |
| コマ1 図 | 図・カード | 法人（会社） / 番号あり / 支配人 / 登記所 / 代理 / ①　申請情報を提供して、登記を申請 / 申請情報に、会社法人等番号を書く / 会社所有の土地 / 地目の変更の登記 / 支配人の権限を証する登記事項証明書も要る？ | — |
| コマ1 | 藍子（左・先に話す） | 支配人が申請するとき、何を出すんですか？ | — |
| コマ1 | トリ先生（右・答える） | 法人の会社法人等番号がカギになるのよ | 「会社法人等番号」 |
| コマ2 見出し | ラベル | ②　番号と証明書の位置づけ | — |
| コマ2 図 | 図・カード | 押さえどころ / 証明書は、番号に代える場合だけ / 番号に代える / に代えて / 会社法人等番号を提供 / 令7条1項1号イ / 会社法人等番号を有する法人が申請するときの原則 / 登記事項証明書を提供 / 規則36条1項2号 / 会社法人等番号の提供に代えて、証明書を提供する場合 / 支配人が法人を代理して申請するときは、代理人の権限を証する情報の提供を要しない（令7条1項2号、規則36条3項） | — |
| コマ3 見出し | ラベル | ③　本番での読み方3ステップ | — |
| コマ3 図 | 図・カード | ステップ1　代理人は支配人か / 支配人が法人を代理して申請している / ステップ2　番号を提供しているか / 提供していれば、支配人の権限を証する証明書は別に要らない / ステップ3　条件づけの語を見る / 条件づけで、番号による省略の原則を狭めている肢は誤り / ひっかけ：登記所が同一でない限り、という条件づけ | — |
| コマ3 | 藍子（左・1番目） | 条件つきの肢は、どう読めばいいですか？ | — |
| コマ3 | トリ先生（右・2番目） | 番号の省略の原則を狭めていないか見るのよ | 「狭めて」 |
| コマ3 | 藍子（左・3番目） | では、支配人の証明書は要らないんですね？ | — |
| コマ3 | トリ先生（右・4番目） | 要らないわ。証明書は番号に代える場合だけよ | 「番号に代える場合だけ」 |
| コマ4 見出し | ラベル | ④　これだけ覚える | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 番号を提供すれば足りる、と覚えます！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。支配人の証明書は別に要らないのよ | 「別に要らない」 |
| コマ4 チェック欄 | 3項目（青✓） | 会社法人等番号を提供するのが原則（令7条1項1号イ） / 支配人の代理なら、代理人の権限を証する情報は不要（令7条1項2号、規則36条3項） / 登記事項証明書は、番号の提供に代える場合だけ。登記所の条件で番号の省略を狭める肢は誤り（規則36条1項2号） | — |
| 注記 | 小さな注記（コマ4の下） | 肢の登記所の条件は、平成27年の規則改正前の言い回しです | — |
| 結論帯 | 1行目 | 会社法人等番号を提供すれば、支配人の権限を証する証明書は要らない | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1448　正解×（R01-Q08ア） | — |

### プロンプト本体2

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a collared light-blue blouse with thin blue pinstripes (sleeves rolled up) and a navy pencil skirt with navy pumps, no jacket, often holding a navy clipboard and a pencil; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. Organizations and buildings in the diagrams are NOT characters: draw them only as simple, faceless, flat icons with the exact text labels given below.

ANATOMY (critical, 藍子): keep her human anatomy strictly correct in every panel: exactly one head, one torso, exactly two arms (one left, one right) and exactly two hands in total. Never draw extra arms, extra hands, extra fingers, floating hands, duplicated hands, arms that do not grow from the shoulders, or fused hands. Each hand has exactly five fingers. Check that every shoulder, elbow, and wrist connects naturally. HAND COUNT RULE: before drawing each panel, assign both of 藍子's hands a job (for example, one hand points while the other hand holds the clipboard or hangs at her side; or one hand touches her chin while the other holds the clipboard; or both hands are raised in a small cheer). When she points, only ONE arm points; her other hand must not be clasped, raised, or clenched at the same time, so there are never three hands in a panel. POSE: change 藍子's pose from panel to panel (for example standing, sitting, leaning forward, resting a hand on her chin) and use a different set of poses each time this image is generated. CONTENT: in each panel, express through the diagram, labels, and scene the elements a reader needs in order to understand this article's content and pass the land and building surveyor exam, without adding any text beyond the given strings.

FIXED POSITIONS AND SPEECH BUBBLES: In every panel in which a character appears, 藍子 (the student) stands on the LEFT side and トリ先生 (the teacher) stands on the RIGHT side. A panel does not have to show both characters: when the diagram, the flowchart, or the items to memorize need more space, the PANEL line may show only one of the two characters, show both at the normal size at the two outer edges, show both as small face icons in a vertical conversation column, or show both very small; in that case follow the PANEL line and its LAYOUT lines, and a character who is not drawn has no speech bubble; in a panel marked as face icons, each character appears only as a small round face icon inside the vertical conversation column described in the LAYOUT lines, with exactly one face icon for each speech bubble and never more face icons than bubbles. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

CONTINUITY: any object, label, ribbon, tag, or figure that appears in more than one panel keeps the same look, the same color, and the same label text in every panel in which it appears (for example, a ribbon on a plot of land does not disappear after a step of the diagram), unless that panel's own description says that it changes. Every speech bubble's line breaks follow phrase boundaries as written inside its quotation marks; never split a word across lines.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall). Between panel 4 and the conclusion banner, a thin one-line note strip (about 50 px tall) with small text, as given in the NOTE LINE below.

TITLE BANNER: text 「番号で足りる。証明書は番号に代える場合だけ」 in large bold letters; the part 「番号に代える場合だけ」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　申請のしくみ」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A large relation diagram fills the panel, laid out ONE row from left to right: one flat office-building icon labeled 「法人（会社）」 with a small tag 「番号あり」, one faceless pictogram tag in light gray-blue labeled 「支配人」, and one flat registry-office building icon labeled 「登記所」.
- Between 「法人（会社）」 and 「支配人」, one plain thin dark navy line with no arrowhead and a small label 「代理」.
- One dark navy arrow from 「支配人」 to 「登記所」 labeled 「①　申請情報を提供して、登記を申請」 (this arrow means submitting the application information, not a sale and not a payment).
- Under the arrow, a white card with a dark navy outline: 「申請情報に、会社法人等番号を書く」. Below the row, a small block labeled 「会社所有の土地」 with a white card 「地目の変更の登記」.
- A small question badge 「支配人の権限を証する登記事項証明書も要る？」 sits at the top (a question badge only, with no check mark and no cross).
- 藍子 bubble (left, spoken first): 「支配人が申請するとき、
何を出すんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「法人の会社法人等番号が
カギになるのよ」 with the part 「会社法人等番号」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　番号と証明書の位置づけ」
- A full-width concept diagram fills the whole panel, with a small dark navy tag 「押さえどころ」 at the top left and a line beside it: 「証明書は、番号に代える場合だけ」, with the part 「番号に代える」 in a yellow highlighter marker.
- Two large cards side by side, both with the same pale gray fill, a dark navy outline, and a dark navy heading, joined in the middle by a small plain dark navy label 「に代えて」 (a label only, no arrow). Left card, heading 「会社法人等番号を提供」, small tag 「令7条1項1号イ」, body 「会社法人等番号を有する法人が申請するときの原則」. Right card, heading 「登記事項証明書を提供」, small tag 「規則36条1項2号」, body 「会社法人等番号の提供に代えて、証明書を提供する場合」.
- At the bottom, one wide dark navy band with white text 「支配人が法人を代理して申請するときは、代理人の権限を証する情報の提供を要しない（令7条1項2号、規則36条3項）」.
- There is no check mark and no cross anywhere in this panel.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　本番での読み方3ステップ」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three step cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a dark navy number badge, and a dark navy heading, with no check mark and no cross.
- Step card 1: heading 「ステップ1　代理人は支配人か」, body 「支配人が法人を代理して申請している」.
- Step card 2: heading 「ステップ2　番号を提供しているか」, body 「提供していれば、支配人の権限を証する証明書は別に要らない」.
- Step card 3: heading 「ステップ3　条件づけの語を見る」, body 「条件づけで、番号による省略の原則を狭めている肢は誤り」, with a dark navy ribbon tag under the body, with large white text, reading 「ひっかけ：登記所が同一でない限り、という条件づけ」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「条件つきの肢は、
どう読めばいいですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「番号の省略の原則を
狭めていないか
見るのよ」 with the part 「狭めて」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「では、支配人の証明書は
要らないんですね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「要らないわ。証明書は
番号に代える場合だけよ」 with the part 「番号に代える場合だけ」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　これだけ覚える」
- 藍子 bubble (left, spoken first): 「番号を提供すれば
足りる、と覚えます！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。
支配人の証明書は
別に要らないのよ」 with the part 「別に要らない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「会社法人等番号を提供するのが原則（令7条1項1号イ）」, 「支配人の代理なら、代理人の権限を証する情報は不要（令7条1項2号、規則36条3項）」, 「登記事項証明書は、番号の提供に代える場合だけ。登記所の条件で番号の省略を狭める肢は誤り（規則36条1項2号）」.

NOTE LINE (small text on a thin strip between panel 4 and the conclusion banner, one line, fully legible): 「肢の登記所の条件は、平成27年の規則改正前の言い回しです」

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「会社法人等番号を提供すれば、支配人の権限を証する証明書は要らない」 with a yellow highlighter marker.
- Line 2: 「問題D1448　正解×（R01-Q08ア）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two very small characters are drawn as specified and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 代, 号, 地, 所, 押, 権, 番, 登, 肢, 規, 解, 記, 証, 請 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the word 「原則」 is spelled exactly like this everywhere (never 「思則」); confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that no triangle, chevron, arrow, or connector is drawn between the stacked step cards; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

### 第二案の品質ゲート（工程C）
- [ ] 工程C：初見の読者：コマ1で、法人・支配人・登記所の関係と、矢印1本の意味（申請情報を提供して申請する）が言える。この図だけで、『申請情報に会社法人等番号を書く』ことが何のためかの問いに気づく
- [ ] 工程C：押さえどころ4つ（番号の提供が原則・証明書は番号に代える場合・支配人が代理するときは代理人の権限を証する情報が要らない・条件づけで省略の原則を狭めている肢は誤り）が、コマ1・2・3・4のどこかに図か文言で必ずある
- [ ] 工程C：構成表の全文言を記事（R01-Q08ア）と突き合わせ：「会社法人等番号」「令7条1項1号イ」「令7条1項2号、規則36条3項」「規則36条1項2号」「番号の提供に代えて」「番号による省略の原則を狭めている」
- [ ] 工程C：コマの使い方が隣り合うコマで同じにならない（small→none→faces→両方）。結論は×（登記所が同一などの条件を満たさない限り証明書が要る、という記述が誤り）
- [ ] 工程C：ひっかけ（問題文の『登記所が同一であり、〜以外のものでない限り』）がコマ3のステップ3のリボンに入っている。勘違いの内容は藍子のコマ3の質問と、ステップ3の『省略の原則を狭めている』で示されている
- [ ] 工程C：肝（ひっかけ・勘違い・対比）が図・押さえどころ・暗記3点にある：対比「会社法人等番号を提供」⇔「登記事項証明書を提供」がコマ2のカードに、ひっかけがコマ3のリボンに、『番号に代える場合だけ・条件で省略を狭める肢は誤り』が暗記3点にある

### 第二案の改訂履歴

- 2026-10-09 B案v02：4コマの目的（出題者のひっかけ・受験者の勘違い・対比する制度）を設計メモに明記。暗記3点の3つ目に『登記所の条件で番号の省略を狭める肢は誤り』を足し、肝を暗記3点に入れた。構成（図・押さえどころ・読み方）は変更なし
- 2026-10-09 B案v01：初版（第二案。D0314-Bと同じ型：しくみの図解→番号と証明書の位置づけ→本番での読み方3ステップ→暗記3点）
