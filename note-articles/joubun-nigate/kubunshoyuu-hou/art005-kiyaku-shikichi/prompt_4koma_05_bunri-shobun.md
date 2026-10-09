# D1795・D1798・D1799 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、区分所有法 第5条（規約敷地）の記事に差し込む4コマ（5本目）のプロンプトです。類似の誤解をまとめて、1本の4コマにしました。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（ブランチ `claude/kind-bell-y3f106` の `tools/drill/manga/`）に従い、同ブランチの生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-09）。下の「作成時の品質ゲート」にある `tools/drill/manga/` のパスは、そのブランチ上のパスです。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D1795・D1798・D1799（不動産登記法／区分建物・敷地権・共用部分、出典 R04-Q18ア・エ・オ）。正解＝D1795・D1799＝×（誤った記述）／D1798＝〇。
- 記事：`note-articles/r4-mondai/q18-shikichiken.md` ア「共有持分権を敷地権として丁区分建物の表題登記を申請できる」・エ「一部の区分建物についてのみ分離処分可能規約を設定できる」・オ「分離処分には前提として敷地権登記の抹消が必要」
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【型の選び方】型：型3（第三案・理由説明）の流れ。理由：結論（共有持分も敷地権／持分だけ売るには先に敷地権を抹消）だけでなく、『なぜ先に抹消が要るのか』（敷地権である旨の登記がある土地には、持分の移転の登記ができない）が分からないと崩れるため、コマ2に原則→分離処分を可能にする→移転、の3枚を置き、コマ3の最後に理由を置いた。
- 【出題者のひっかけ】『共有持分権を敷地権として』『敷地権である旨の登記がされた後の売買を原因とする共有持分権の移転の登記』と、持分と売買の話にして、敷地権と分離処分の原則が見えにくい書き方をする（記事 R04-Q18ア・エ・オ）。
- 【受験者の勘違い・定着していない点】①共有持分は敷地権にならないと思う。②敷地権である旨の登記がある土地の持分も、そのまま売買で移転できると思う。③分離処分可能規約は、区分所有者全員にそろえて設定しなければならないと思う。実際は、敷地利用権が数人で有する所有権なども分離処分できず（区分所有法22条1項）共有持分も敷地権になる／持分だけ移すには先に敷地権の登記を抹消する（法73条2項）／規約は一部の区分建物についてだけでも設定できる。
- 【対比する制度】「原則：分離処分できない」⇔「分離処分を可能にする」：原則は専有部分と敷地利用権を分離して処分できない／規約に別段の定めをすれば分離して処分でき、持分だけの移転登記ができる。結論が逆になる点。
- 会話順：藍子の誤解（共有持分は敷地権にならない）→トリ先生の訂正（共有持分も敷地権）→持分だけ売るには→先に敷地権の登記を抹消。
- 記事の範囲：区分所有法22条1項（分離処分の禁止、規約に別段の定めがあるときは例外）／法73条2項（敷地権である旨の登記をした土地には、敷地権の移転の登記をすることができない）／一部の区分建物についてだけ分離処分可能規約を設定できる（記事 R04-Q18エ）。
- 登場人物：当事者の記号は使わない。建物・土地はアイコンと文字ラベルで示す。
- 矢印の意味：矢印は使わない（取引も手続も流れもない）。コマ2は別々のカード。
- 配色：コマ3は左（よくある勘違い）＝赤✕1つ、右（正しい整理）＝青✓1つ。コマ1・2は印なし。コマ4の暗記3点は青✓。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 共有持分も敷地権になる。持分だけ売るには先に敷地権を抹消 | 「先に敷地権を抹消」を黄色マーカー |
| コマ1 見出し | ラベル | ①　問いの事案 | — |
| コマ1 図 | 図・カード | A・B共有の土地 / 丁区分建物（Aの部屋） / Aは、土地の持分だけを売りたい / 敷地権になる？　持分だけ売れる？ | — |
| コマ1 | 藍子（左・先に話す） | 共有持分は、敷地権にならないのでは？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。『共有持分』に引かれたわね | 「共有持分」 |
| コマ2 見出し | ラベル | ②　出題者のねらい | — |
| コマ2 図 | 図・カード | 出題者のねらい / 分離処分の原則と、例外までの手順 / 原則：分離処分できない / 敷地利用権が数人で有する所有権などのとき、専有部分と一体（区分所有法22条1項）。共有持分も敷地権になる / 分離処分を可能にする / 規約に別段の定めを設定する。一部の区分建物についてだけでもよい / 持分だけを移転する / 前提として、敷地権の登記を抹消する表題部の変更の登記が要る（法73条2項） | — |
| コマ3 見出し | ラベル | ③　ひっかけと勘違い | — |
| コマ3 図 | 図・カード | よくある勘違い / 共有持分は敷地権にならない。持分だけの移転登記は、そのままできる / ひっかけ：共有持分、売買という言葉 / 正しい整理 / 共有持分も敷地権になる。持分だけ移すには、先に敷地権の登記を抹消する / 理由：敷地権である旨の登記をした土地には、敷地権の移転の登記をすることができない（法73条2項） | — |
| コマ3 | 藍子（左・1番目） | 持分だけの移転登記は、できますよね？ | — |
| コマ3 | トリ先生（右・2番目） | 先に、敷地権の登記を抹消するのよ | 「敷地権の登記を抹消」 |
| コマ3 | 藍子（左・3番目） | なぜ、先に抹消が要るんですか？ | — |
| コマ3 | トリ先生（右・4番目） | 敷地権の土地には、移転できないの | 「移転できない」 |
| コマ4 見出し | ラベル | ④　結論は先に抹消 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 規約、抹消、移転の順なんですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。丁だけでもできるのよ | 「丁だけでも」 |
| コマ4 チェック欄 | 3項目（青✓） | 敷地利用権が数人で有する所有権などのとき、専有部分と敷地利用権は分離して処分できない。共有持分も敷地権になる（区分所有法22条1項） / 規約に別段の定めをすれば、分離して処分できる。丁区分建物についてだけ設定してもよい / 敷地権である旨の登記がある土地は、先に敷地権の登記を抹消してからでないと、持分だけの移転登記はできない（法73条2項） | — |
| 結論帯 | 1行目 | 持分だけ売るには、規約、敷地権の抹消、移転の順 | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1795・D1798・D1799　D1798＝〇、D1795・D1799＝× | — |

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

TITLE BANNER: text 「共有持分も敷地権になる。持分だけ売るには先に敷地権を抹消」 in large bold letters; the part 「先に敷地権を抹消」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　問いの事案」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram is drawn large in the center region: one land plot icon with a dark navy tag 「A・B共有の土地」 and, on it, one apartment building icon with a dark navy tag 「丁区分建物（Aの部屋）」.
- A white note card beside the plot reads 「Aは、土地の持分だけを売りたい」. A small question badge 「敷地権になる？　持分だけ売れる？」 sits above the diagram (a question badge only, with no check mark and no cross).
- 藍子 bubble (left, spoken first): 「共有持分は、
敷地権にならないのでは？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
『共有持分』に
引かれたわね」 with the part 「共有持分」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　出題者のねらい」
- A full-width explanation panel fills the whole panel, with a small dark navy tag 「出題者のねらい」 at the top left and a line beside it: 「分離処分の原則と、例外までの手順」.
- Three wide white cards stacked top to bottom with dark navy outlines and no arrows between them. Card 1, heading 「原則：分離処分できない」, body 「敷地利用権が数人で有する所有権などのとき、専有部分と一体（区分所有法22条1項）。共有持分も敷地権になる」. Card 2, heading 「分離処分を可能にする」, body 「規約に別段の定めを設定する。一部の区分建物についてだけでもよい」. Card 3, heading 「持分だけを移転する」, body 「前提として、敷地権の登記を抹消する表題部の変更の登記が要る（法73条2項）」.
- There is no check mark and no cross anywhere in this panel.

PANEL 3 (surprised then convinced mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　ひっかけと勘違い」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.
- Two large cards side by side, with a wide reason strip under them.
- Left card, heading 「よくある勘違い」, body 「共有持分は敷地権にならない。持分だけの移転登記は、そのままできる」, with ONE red cross only (no check mark on this card); a dark navy ribbon tag under the body, with large white text, reads 「ひっかけ：共有持分、売買という言葉」.
- Right card, heading 「正しい整理」, body 「共有持分も敷地権になる。持分だけ移すには、先に敷地権の登記を抹消する」, with ONE blue check mark only (no cross on this card).
- Reason strip under the two cards: 「理由：敷地権である旨の登記をした土地には、敷地権の移転の登記をすることができない（法73条2項）」.
- The two cards have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「持分だけの移転登記は、
できますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「先に、敷地権の登記を
抹消するのよ」 with the part 「敷地権の登記を抹消」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「なぜ、先に抹消が
要るんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「敷地権の土地には、
移転できないの」 with the part 「移転できない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (relieved and convinced mood; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は先に抹消」
- 藍子 bubble (left, spoken first): 「規約、抹消、移転の
順なんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。
丁だけでも
できるのよ」 with the part 「丁だけでも」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「敷地利用権が数人で有する所有権などのとき、専有部分と敷地利用権は分離して処分できない。共有持分も敷地権になる（区分所有法22条1項）」, 「規約に別段の定めをすれば、分離して処分できる。丁区分建物についてだけ設定してもよい」, 「敷地権である旨の登記がある土地は、先に敷地権の登記を抹消してからでないと、持分だけの移転登記はできない（法73条2項）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「持分だけ売るには、規約、敷地権の抹消、移転の順」 with a yellow highlighter marker.
- Line 2: 「問題D1795・D1798・D1799　D1798＝〇、D1795・D1799＝×」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two very small characters are drawn as specified and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 地, 売, 建, 所, 権, 物, 登, 規, 記, 買, 違 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the left comparison card has only a red cross and the right card only a blue check mark; confirm that the word 「原則」 is spelled exactly like this everywhere (never 「思則」); confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 保存名

- 4コマ（採用版）：`4コマ5_持分だけ売るには先に敷地権を抹消.png`
- 途中の版・不採用の版：`4コマ5_持分だけ売るには先に敷地権を抹消_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D1795-D1798-D1799_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1の事案（共有の土地の上のマンション、持分だけ売りたい）と、コマ2の3枚のカードが対応している
- [ ] 工程C：肝の確認：コマ2に原則・分離処分を可能にする・持分だけを移転する、コマ3に理由（敷地権である旨の登記がある土地には持分の移転ができない）、コマ4の暗記3点に『先に敷地権の登記を抹消』が入っている
- [ ] 工程C：出典の確認：区分所有法22条1項・不動産登記法73条2項は法令DBで確認済み。記事 R04-Q18ア・エ・オの本文と図の文言が一致している
- [ ] 工程C：コマの使い方が隣り合うコマで同じにならない（side→none→faces→両方）。結論は D1795・D1799＝×、D1798＝〇

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

## 改訂履歴（このファイルは `manga_specs.py` から生成。直すときは設計データを直して再生成する）

- 2026-10-09 v01：初版（条文別『苦手克服』シリーズ（note-articles/joubun-nigate/）の規約敷地用。共有持分の敷地権と分離処分の手順を問う3肢を1本にまとめた。ChatGPTでの生成・検品はまだ）
