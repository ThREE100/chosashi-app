# D2016 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

- 肢：D2016（民法／相続・親族、出典 R07-Q03エ）。正解＝×（誤った記述）。誤解2026-10-05・10-08・10-09は〇と答えて誤解。2026-10-10に×で正解。
- 記事：`note-articles/r7-mondai/q03-souzoku.md` R07-Q03エ（保存行為だけでは単純承認とみなされない。民法921条1号の本文＝処分、ただし書＝保存行為・602条の期間内の賃貸は除外）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】肢の文は、民法921条1号の本文にある『相続財産の全部又は一部を』という言い回しを、そのまま使う。ところが本文で単純承認の引き金になっているのは『処分』であり、肢はその位置に、ただし書で除かれている『保存行為』を入れ替えて置いている。条文の語がそのまま並んでいるので、条文どおりの正しい記述に見える（記事の『ここが分かりにくいポイント』）。
- 【受験者の勘違い・定着していない点】（推測：回答履歴は〇→〇→〇→×で、誤答3回はすべて〇。4回目でやっと×） ①『相続財産に何か行為をした＝承認した』と、行為の種類を見分けずに考える。②条文の語の並びを覚えていて、本文（処分）とただし書（保存行為・短期賃貸）の入れ替えに気づかない。③『相続人は固有財産と同じ注意で管理する（918条）』を覚えているのに、管理にあたる保存行為が承認から外れていることと結びつかない。（①〜③は回答履歴と肢の言い回しからの推測）
- 【対比する制度】「処分」⇔「保存行為」：処分（家財を売り払う、預金を引き出して使う）は、財産を減らす・処分する行為で、単純承認とみなされる。保存行為（雨漏りの応急処置、鍵の交換）と民法602条に定める期間を超えない賃貸は、民法921条1号ただし書で除かれ、単純承認とみなされない（同じ『相続財産に手を付けた』場面でも、結論が逆になる）。
- 【型の選び方】型：型3（理由説明）＋型2の条文の作りの図。理由：『初見の読者が引っかかる壁』は、条文の語が肢にそのまま並んでいるため、本文（処分）とただし書（保存行為）の入れ替えに気づけない点。1肢が3回とも同じ誤り（〇と答えた）なので、結論の暗記ではなく、条文の作り（コマ2）と、なぜ保存行為が外れるか＝価値を維持するか減らすか（コマ3の理由）で組んだ。
- 記事の範囲：R07-Q03エ（民法921条1号、ただし書で保存行為は除外、602条以内の短期賃貸、保存行為＝財産価値を維持する行為、処分行為＝家財を売り払う・預金を引き出して使う、雨漏りの応急処置・鍵の交換の例、本文＝処分／ただし書＝保存行為の構造）。ただし書の『第602条に定める期間を超えない賃貸』は、記事の『602条以内の短期賃貸』と同じで、法令DB（note-articles/laws/minpou-3-shinzoku-souzoku.md の第921条）で原文を確かめた。
- extra_refs：図に入れる整理はすべて記事の範囲。記事にない整理はなし。同じ問の兄弟肢との関係（図には入れない）：D2014（イ。民法918条、決めるまでは固有財産と同一の注意で管理する義務）は、保存行為をしても承認にならないことの背景として読める（肢の誤りの根拠は921条1号ただし書）。D2017（オ。処分行為などの法定単純承認の事由があると、その相続人は限定承認ができない）は、処分が承認になることの帰結として別の肢で問われている。肢D2013（ア。放棄の申述先は家庭裁判所）・D2015（ウ。限定承認の弁済の順序）は別論点。
- 出題文の注意：肢の前半『自己のために相続が開始した事実を知りながら』は、記事が扱っていない言い回しなので、図の判断基準には入れない（図では肢の誤りを『保存行為』を引き金に置いた点に限る）。
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない。『相続人』を顔なしの人型タグ、『実家』を家のアイコンで、コマ1で紹介してから使う。
- 矢印の意味：矢印は使わない。コマ1は人型タグ・家・2枚のカード、コマ2は上下2枚のカード、コマ3は上下2枚のカード。
- 配色：コマ1〜3は印（✓✕）を付けない（みなされる・みなされないは文字で書く）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方：コマ1＝side（キャラは左右の端、図は中央）、コマ2＝none（条文の作りの図だけ）、コマ3＝faces（左に上下2枚のカードとリボン、右に会話4行）、コマ4＝既定（暗記3点と結論）。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D2016～R07-Q03エ～

## note記事の冒頭文

まだ承認も放棄も決めていない相続人が、相続財産の全部又は一部について、保存行為をしました。この行為によって、単純承認をしたものとみなされるのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（令和7年度　第3問　エ）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 保存行為では、単純承認にならない | 「単純承認にならない」を黄色マーカー |
| コマ1 見出し | ラベル | ①　問いの事案 | — |
| コマ1 図 | 図・カード | 相続人 / 承認も放棄も、まだ決めていない / 実家 / 雨漏りの応急処置 / 空き巣対策の鍵の交換 / 相続財産への行為 / 保存行為をしたら、単純承認とみなされる？ | — |
| コマ1 | 藍子（左・先に話す） | 条文の言い回しどおりだから、〇では？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。引き金は保存行為じゃないのよ | 「引き金は保存行為じゃない」 |
| コマ2 見出し | ラベル | ②　民法921条1号の作り | — |
| コマ2 図 | 図・カード | 出題者のねらい / 引き金と除外を、入れ替えていないか / 民法921条1号 / ただし / 本文 / 相続財産の全部又は一部を処分したとき → 単純承認とみなす / 処分 / ただし書 / 保存行為と、602条に定める期間を超えない賃貸 → みなさない / 保存行為 | — |
| コマ3 見出し | ラベル | ③　なぜ、保存行為は外れるのか | — |
| コマ3 図 | 図・カード | 処分 / 財産を減らす・処分する / 家財を売り払う。預金を引き出して使う / 単純承認とみなされる / 保存行為 / 財産の価値を維持する / 雨漏りの応急処置。鍵の交換 / 単純承認とみなされない / ひっかけ：処分の位置に、保存行為を入れ替えている | — |
| コマ3 | 藍子（左・1番目） | 全部又は一部、って条文どおりでは？ | — |
| コマ3 | トリ先生（右・2番目） | 引き金は処分。保存行為は外れるのよ | 「引き金は処分」 |
| コマ3 | 藍子（左・3番目） | どう見分ければいいんですか？ | — |
| コマ3 | トリ先生（右・4番目） | 価値を維持するか、減らすかよ | 「価値を維持する」 |
| コマ4 見出し | ラベル | ④　これだけ覚える | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 保存行為では、承認にならないんですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。引き金は処分なのよ | 「引き金は処分」 |
| コマ4 チェック欄 | 3項目（青✓） | 単純承認とみなされるのは、相続財産を処分したとき（民法921条1号本文） / 保存行為と、602条に定める期間を超えない賃貸は、みなされない（ただし書） / 保存行為でみなされる、という記述は× | — |
| 結論帯 | 1行目 | 保存行為をしても、単純承認とみなされない | 黄色マーカー |
| 結論帯 | 2行目 | 問題D2016　正解×（R07-Q03エ） | — |

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
- Conclusion banner at the bottom (about 110 px tall).

TITLE BANNER: text 「保存行為では、単純承認にならない」 in large bold letters; the part 「単純承認にならない」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　問いの事案」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A large relation diagram in the center area: one faceless pictogram tag in a light gray-blue color with a dark navy tag 「相続人」 (small label 「承認も放棄も、まだ決めていない」), standing beside a flat house icon labeled 「実家」.
- Under them, two white cards with dark navy outlines side by side: left card 「雨漏りの応急処置」, right card 「空き巣対策の鍵の交換」, both under a small plain label 「相続財産への行為」.
- A small question badge 「保存行為をしたら、単純承認とみなされる？」 sits at the top (a question badge only, with no check mark and no cross).
- 藍子 bubble (left, spoken first): 「条文の言い回し
どおりだから、〇では？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
引き金は保存行為
じゃないのよ」 with the part 「引き金は保存行為じゃない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　民法921条1号の作り」
- A full-width concept diagram fills the whole panel, with a small dark navy tag 「出題者のねらい」 at the top left and a line beside it: 「引き金と除外を、入れ替えていないか」, and a small tag 「民法921条1号」.
- Two large cards stacked from top to bottom, both exactly the same size, with the same pale gray fill, a dark navy outline, and a dark navy heading placed fully INSIDE each card, joined in the middle by a small plain dark navy label 「ただし」 (a label only, no arrow).
- Top card, heading 「本文」, body 「相続財産の全部又は一部を処分したとき → 単純承認とみなす」, with the part 「処分」 in a yellow highlighter marker.
- Bottom card, heading 「ただし書」, body 「保存行為と、602条に定める期間を超えない賃貸 → みなさない」, with the part 「保存行為」 in a yellow highlighter marker.
- There is no check mark and no cross anywhere in this panel.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ、保存行為は外れるのか」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Two cards stacked from top to bottom, both exactly the same size, with the same pale gray fill, a dark navy outline, and a dark navy heading, with no check mark and no cross. The cards are separated only by a small empty gap, with nothing drawn between them.
- Top card, heading 「処分」, small tag 「財産を減らす・処分する」, body 「家財を売り払う。預金を引き出して使う」, and a last line 「単純承認とみなされる」.
- Bottom card, heading 「保存行為」, small tag 「財産の価値を維持する」, body 「雨漏りの応急処置。鍵の交換」, and a last line 「単純承認とみなされない」.
- Under the two cards, one dark navy ribbon tag with large white text 「ひっかけ：処分の位置に、保存行為を入れ替えている」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「全部又は一部、って
条文どおりでは？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「引き金は処分。
保存行為は
外れるのよ」 with the part 「引き金は処分」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「どう見分ければ
いいんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「価値を維持するか、
減らすかよ」 with the part 「価値を維持する」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　これだけ覚える」
- 藍子 bubble (left, spoken first): 「保存行為では、
承認にならない
んですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。
引き金は処分なのよ」 with the part 「引き金は処分」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「単純承認とみなされるのは、相続財産を処分したとき（民法921条1号本文）」, 「保存行為と、602条に定める期間を超えない賃貸は、みなされない（ただし書）」, 「保存行為でみなされる、という記述は×」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「保存行為をしても、単純承認とみなされない」 with a yellow highlighter marker.
- Line 2: 「問題D2016　正解×（R07-Q03エ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two very small characters are drawn as specified and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 保, 号, 売, 対, 承, 解, 記, 認, 間 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 実家の雨漏りを直したら | 薄い黄色のマーカー |
| タイトル2行目 | 単純承認になる？ | 「単純承認になる？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D2016　R07-Q03エ | — |

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
実家の雨漏りを直したら
Line 2 is larger; the phrase 単純承認になる？ is red-orange and the rest is dark navy:
単純承認になる？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D2016　R07-Q03エ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: an old house with a ladder leaning on the roof and a small bucket beside it
Right side: a house key and a padlock beside a blank folder

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 実, 家, 雨, 漏, 直, 単, 純, 承, 認, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D2016～R07-Q03エ～.png |
| 見出し画像（採用版） | 4コマ解説図解D2016～R07-Q03エ～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D2016～R07-Q03エ～_v01.png ／ 4コマ解説図解D2016～R07-Q03エ～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D2016_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で『相続人が、まだ決めていない実家に応急処置と鍵の交換をした』事案と問い、コマ2で本文＝処分／ただし書＝保存行為・602条の期間内の賃貸、コマ3で価値を維持するか減らすかの見分け方、コマ4で結論（×）が言える
- [ ] 工程C：肝の確認：①単純承認の引き金は『処分』 ②保存行為と602条に定める期間を超えない賃貸は、ただし書で除かれる ③肢は引き金と除外の位置を入れ替えているので×
- [ ] 工程C：構成表の全文言を記事（R07-Q03エ）と突き合わせ：『処分』『保存行為』『602条に定める期間を超えない賃貸』『財産の価値を維持する』『家財を売り払う』『預金を引き出して使う』『雨漏りの応急処置』『鍵の交換』。条文は法令DBの民法第921条で原文確認済み
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方が隣り合うコマで同じにならない（side→none→faces→既定）。コマ4の正解欄は×

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

## v01：新規作成（2026-10-10）。一問一答で3回〇と答えて誤答した肢（4回目で×）。型3（理由説明）＋型2の条文の作りの図。記事の範囲内で組み、記事にない整理はなし。ChatGPTでの画像生成・検品はまだ。

## 改訂履歴（このファイルは `manga_specs.py` から生成。直すときは設計データを直して再生成する）

- 2026-10-10 v01：初版（一発合格ルール適用）
