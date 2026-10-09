# D0537・D1093・D1890 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、不動産登記法 第51条第1項の記事に差し込む4コマ（2本目）のプロンプトです。類似の誤解をまとめて、1本の4コマにしました。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（ブランチ `claude/kind-bell-y3f106` の `tools/drill/manga/`）に従い、同ブランチの生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-09）。下の「作成時の品質ゲート」にある `tools/drill/manga/` のパスは、そのブランチ上のパスです。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D0537・D1093・D1890（不動産登記法／区分建物・敷地権・共用部分、出典 H22-Q06イ／H27-Q17エ／R05-Q17ウ）。正解＝D0537・D1890＝〇／D1093＝×（誤った記述）。
- 記事：`note-articles/h22-mondai/q06-kyouyoububun.md` イ「共用部分の建物でも、床面積が変われば1か月以内に変更登記が必要」。ほか、H27-Q17エ（q17-kyouyoububun.md）、R05-Q17ウ（q17-kyouyoububun.md）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【型の選び方】型：型3（第三案・理由説明）の流れ。結論（共用部分でも義務は残る）だけでなく、『なぜ名義人でなく所有者なのか』が崩れない鍵なので、コマ2で通常の建物と共用部分の建物の義務者を並べ、コマ3の最後に理由を置いた。
- 【出題者のひっかけ】『共用部分である旨の登記がある建物』という前提だけを見せて、登記記録に名義人がいないから義務もない、と思わせる。D1093は『申請することを要しない』という言い回し（記事 H22-Q06イ、H27-Q17エ、R05-Q17ウ）。
- 【受験者の勘違い・定着していない点】共用部分である旨の登記がある建物は、変更の登記を申請する義務がなくなると思い込む。実際は、物理的な変更があれば義務は残り、義務者が『表題部所有者又は所有権の登記名義人』から『所有者』に変わるだけ（法51条1項かっこ書）。
- 【対比する制度】「通常の建物」⇔「共用部分である旨の登記がある建物」：通常の建物は表題部所有者又は所有権の登記名義人が申請／共用部分である旨の登記がある建物は所有者が申請（法51条1項かっこ書）。どちらも期限は変更があった日から1か月以内で、義務は消えない。
- 登場人物：当事者の記号は使わない。人物は文字タグ（『所有者』）だけで示す。
- 矢印の意味：矢印は使わない。コマ2は上下2枚のカードの並置。
- 会話順：藍子の誤解（共用部分だから義務はない）→トリ先生の訂正（床面積が変われば要る）→誰が申請するか→所有者。
- 配色：コマ3は左（よくある勘違い）＝赤✕1つ、右（正しい整理）＝青✓1つ。コマ1・2は印なし。コマ4の暗記3点は青✓。
- 記事の範囲：法51条1項かっこ書（共用部分である旨の登記がある建物は所有者）／床面積・種類の変更は登記事項の変更（記事 H22-Q06イ、R05-Q17ウ）／1か月。『名義人が登記記録に記録されていない』のは、共用部分である旨の登記をするときに登記官が職権で表題部所有者の登記又は権利に関する登記を抹消するため（法58条4項。法令DB『第58条』で確認。記事 H27-Q17エ の本文にはなく、`extra_refs` に記載）。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 共用部分の建物でも、変更の登記は所有者がする | 「所有者がする」を黄色マーカー |
| コマ1 見出し | ラベル | ①　問いの事案 | — |
| コマ1 図 | 図・カード | 共用部分である旨の登記がある集会室 / 集会室を増築して床面積が変わった / 登記記録に名義人の記録がない / 変更の登記は、必要？ | — |
| コマ1 | 藍子（左・先に話す） | 名義人がいないなら、義務もないのでは？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。名義人に引かれたわね | 「名義人に引かれた」 |
| コマ2 見出し | ラベル | ②　出題者のねらい | — |
| コマ2 図 | 図・カード | 出題者のねらい / 変更の登記を申請する人は誰か / 通常の建物 / 表題部所有者又は所有権の登記名義人が申請 / 共用部分である旨の登記がある建物 / 所有者が申請（法51条1項かっこ書） / どちらも、変更があった日から1か月以内に申請 | — |
| コマ3 見出し | ラベル | ③　ひっかけと勘違い | — |
| コマ3 図 | 図・カード | よくある勘違い / 共用部分の建物は名義人がいないので、変更の登記の義務はない / ひっかけ：名義人が登記記録にいない建物 / 正しい整理 / 床面積や種類が変われば、所有者が1か月以内に申請する / 理由：共用部分である旨の登記をすると、登記官が職権で名義人の登記を抹消するので、基準が所有者になる（法58条4項） | — |
| コマ3 | 藍子（左・1番目） | 共用部分だから、義務はないですよね？ | — |
| コマ3 | トリ先生（右・2番目） | 共用部分でも、床面積が変われば要るのよ | 「床面積が変われば」 |
| コマ3 | 藍子（左・3番目） | では、誰が申請するんですか？ | — |
| コマ3 | トリ先生（右・4番目） | 名義人の代わりに、所有者が申請するの | 「所有者が申請」 |
| コマ4 見出し | ラベル | ④　結論は義務が残る | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 共用部分でも、義務は残るんですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。申請するのは所有者よ | 「申請するのは所有者」 |
| コマ4 チェック欄 | 3項目（青✓） | 共用部分である旨の登記がある建物でも、床面積や種類が変われば、変更の登記が要る / 申請する人は、名義人ではなく所有者（法51条1項かっこ書） / 期限は、変更があった日から1か月以内。申請することを要しない、は誤り | — |
| 結論帯 | 1行目 | 共用部分の建物でも、所有者が1か月以内に申請する | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0537・D1093・D1890　D0537・D1890＝〇、D1093＝× | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記法58条4項：登記官は、共用部分である旨の登記又は団地共用部分である旨の登記をするときは、職権で、当該建物について表題部所有者の登記又は権利に関する登記を抹消しなければならない（法令DB `fudousan-touki-hou.md` 第58条で確認。law-commentary 第51条3項の解説にも同旨）。コマ1の『登記記録に名義人の記録がない』とコマ3の理由の説明の根拠。記事（H22-Q06イ、H27-Q17エ、R05-Q17ウ）には法58条4項の記載がない。

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

TITLE BANNER: text 「共用部分の建物でも、変更の登記は所有者がする」 in large bold letters; the part 「所有者がする」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　問いの事案」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram is drawn large in the center region: one simple building icon with a dark navy tag 「共用部分である旨の登記がある集会室」.
- Beside the building, two white note cards stacked: the upper card 「集会室を増築して床面積が変わった」 and the lower card 「登記記録に名義人の記録がない」.
- A small question badge 「変更の登記は、必要？」 sits above the building (a question badge only, with no check mark and no cross).
- 藍子 bubble (left, spoken first): 「名義人がいないなら、
義務もないのでは？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
名義人に
引かれたわね」 with the part 「名義人に引かれた」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　出題者のねらい」
- A full-width explanation panel fills the whole panel, with a small dark navy tag 「出題者のねらい」 at the top left and a line beside it: 「変更の登記を申請する人は誰か」.
- Two wide white cards stacked top and bottom, each with a dark navy outline and no arrow between them. The upper card has the heading 「通常の建物」 and the body 「表題部所有者又は所有権の登記名義人が申請」. The lower card has the heading 「共用部分である旨の登記がある建物」 and the body 「所有者が申請（法51条1項かっこ書）」.
- At the bottom, one wide dark navy band with white text: 「どちらも、変更があった日から1か月以内に申請」.
- There is no check mark and no cross anywhere in this panel.

PANEL 3 (surprised then convinced mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　ひっかけと勘違い」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.
- Two large cards side by side, with a wide reason strip under them.
- Left card, heading 「よくある勘違い」, body 「共用部分の建物は名義人がいないので、変更の登記の義務はない」, with ONE red cross only (no check mark on this card); a dark navy ribbon tag under the body, with large white text, reads 「ひっかけ：名義人が登記記録にいない建物」.
- Right card, heading 「正しい整理」, body 「床面積や種類が変われば、所有者が1か月以内に申請する」, with ONE blue check mark only (no cross on this card).
- Reason strip under the two cards: 「理由：共用部分である旨の登記をすると、登記官が職権で名義人の登記を抹消するので、基準が所有者になる（法58条4項）」.
- The two cards have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「共用部分だから、
義務はないですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「共用部分でも、床面積が
変われば要るのよ」 with the part 「床面積が変われば」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「では、誰が申請
するんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「名義人の代わりに、
所有者が申請するの」 with the part 「所有者が申請」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (relieved and convinced mood; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は義務が残る」
- 藍子 bubble (left, spoken first): 「共用部分でも、
義務は残るんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。
申請するのは
所有者よ」 with the part 「申請するのは所有者」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「共用部分である旨の登記がある建物でも、床面積や種類が変われば、変更の登記が要る」, 「申請する人は、名義人ではなく所有者（法51条1項かっこ書）」, 「期限は、変更があった日から1か月以内。申請することを要しない、は誤り」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「共用部分の建物でも、所有者が1か月以内に申請する」 with a yellow highlighter marker.
- Line 2: 「問題D0537・D1093・D1890　D0537・D1890＝〇、D1093＝×」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two very small characters are drawn as specified and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 代, 建, 所, 権, 物, 登, 記, 請, 違, 録 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the left comparison card has only a red cross and the right card only a blue check mark; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 保存名

- 4コマ（採用版）：`4コマ2_共用部分は所有者.png`
- 途中の版・不採用の版：`4コマ2_共用部分は所有者_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0537-D1093-D1890_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1の事案（共用部分の登記がある集会室を増築）と、コマ2・3の『通常の建物／共用部分の建物』の対比が対応している
- [ ] 工程C：肝の確認：コマ2で義務者が『表題部所有者又は所有権の登記名義人』⇔『所有者』と並び、コマ3で『義務は消えない』と『名義人がいないので所有者』の理由が読め、コマ4の暗記3点にも入っている
- [ ] 工程C：出典の確認：法51条1項かっこ書は法令DBの第51条で確認済み。法58条4項は記事にないため `extra_refs` に出典を書いた。ユーザーに『記事にない整理』であることを伝える
- [ ] 工程C：コマの使い方が隣り合うコマで同じにならない（side→none→faces→両方）。D1093は『要しない』が誤りの肢であることを結論帯に出す

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

- 2026-10-09 v01：初版（条文別『苦手克服』シリーズ 第51条第1項 用。共用部分の建物の申請義務を問う3肢を1本にまとめた。ChatGPTでの生成・検品はまだ）
