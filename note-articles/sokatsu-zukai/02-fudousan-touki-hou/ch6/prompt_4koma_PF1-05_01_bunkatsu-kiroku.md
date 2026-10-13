# D0779・D1169 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②不動産登記法編 第6章「建物の分割・分棟・合併」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch6.md`）の、論点【PF1-5】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PF1-05_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D0779・D1169（不動産登記法／建物の分割・合併・合体・滅失・変更、出典 H24-Q14オ／H28-Q13オ）。正解＝D0779＝〇（正しい記述）／D1169＝×（誤った記述）。
- 記事：`note-articles/h24-mondai/q14-tatemono-bunkatsu.md` オ（H24：所有権の登記後に附属建物の新築の変更登記があれば、乙建物に分割による所有権の登記をする旨が記録される。規則128条2項）。ほか、H28-Q13オ（h28-mondai/q13-tatemono-bunkatsu.md。同じ場面で転写とするのは誤り）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】D0779とD1169は同じ場面（所有権の登記の後に、分割に係る附属建物の新築による表題部の変更の登記がされていたとき）の裏表で、乙建物の登記記録に『分割による所有権の登記をする旨が記録される』（〇）か『所有権の登記が転写される』（×）かを、逆の言い方で問う。分割の権利部は転写が原則なので、『転写される』が自然に見える。
- 【受験者の勘違い・定着していない点】（推測）①分割なら乙建物に権利に関する登記が転写される、という原則だけを覚えている。②『所有権の登記の後に附属建物の新築の変更登記がされていたとき』という例外の条件が定着していない。③2つの肢が同じ場面の裏表だと気づかない。
- 【対比する制度】「転写」⇔「分割による所有権の登記をする旨を記録」：原則は、分割前の建物の権利に関する登記を乙建物に転写する（規則128条1項）／所有権の登記の後に分割に係る附属建物の新築による表題部の変更の登記がされていたときは、転写に代えて、乙建物の甲区に分割による所有権の登記をする旨を記録する（規則128条2項。結論が逆になる点）。
- 【型の選び方】型：型3（理由説明）。理由：結論（旨を記録）だけ覚えても、原則の『転写』が頭に残ると崩れる。なぜ転写できないか（所有権の登記は甲建物に対するもので、附属建物はその後に新築された）と、乙建物の甲区に何が記録されるかを、コマ3の理由のカード3枚（印なし）に置いた。コマ1は『まず・次に・最後に』の3枚のカードで時の順を見せ、コマ2は原則と例外の左右の対比。壁＝『分割なら権利の登記は写される』という原則だけの理解。
- コマごとに読者が言えること：コマ1＝甲建物に所有権の登記がされた後に附属建物を新築し、それを分割して乙建物にした場合に、乙建物の登記記録に何が記録されるかを問うている。コマ2＝原則は転写、この場面は例外で旨を記録。コマ3＝所有権の登記は甲建物に対するものでそのまま写せない。乙建物の甲区には、分割による所有権の登記をする旨・名義人の氏名・住所・登記の年月日などが記録される。コマ4＝D0779は〇、D1169は×。
- 記事の範囲：H24-Q14オ（規則128条2項。この要件に当たらない場合は、分割前の所有権の登記が乙建物の登記記録に転写される〈同条1項で準用する規則102条〉）、H28-Q13オ（所有権の登記は甲建物に対するものなので、そのまま転写できない。乙建物の甲区に、分割による所有権の登記をする旨・名義人の氏名住所〈共有のときは持分〉・登記の年月日が記録される）。『甲建物に対するものだから』という理由は記事の説明で、条文の文言ではない。
- extra_refs：規則128条（1項 第百二条及び第百四条第一項から第三項までの規定は、建物の分割の登記について準用する、2項 現に効力を有する所有権の登記がされた後分割に係る附属建物の新築による表題部の登記事項に関する変更の登記がされていたときは、転写に代えて、乙建物の登記記録の甲区に、一 分割による所有権の登記をする旨、二 所有権の登記名義人の氏名又は名称及び住所並びに持分、三 法人識別事項等、四 登記の年月日を記録する）は法令DB note-articles/laws/fudousan-touki-kisoku-1.md で原文を確認。
- 登場人物：人型は使わず、建物は文字のカードで示す。
- 矢印の意味：矢印は使わない。コマ1は縦3枚のカードと疑問バッジ、コマ2は左右のカード、コマ3は縦3枚のカード。
- 配色：コマ1〜3は印（✓✕）を付けない。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、帯・リボンは濃紺（白文字）、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝side、コマ2＝none（図が主役）、コマ3＝faces（左に理由のカード3枚、右に会話4つの縦並び）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 乙建物には、転写でなく旨を記録する場合 | 「旨を記録」を黄色マーカー |
| コマ1 見出し | ラベル | ①　分割した乙建物には何が記録される？ | — |
| コマ1 図 | 図・カード | 乙建物の登記記録には、何が記録される？ / まず / 甲建物に、所有権の登記がされる / 次に / 附属建物を新築して、表題部の変更の登記 / 最後に / その附属建物を分割して、乙建物にする | — |
| コマ1 | 藍子（左・先に話す） | 所有権の登記は、そのまま写されますよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。写すのは原則だけよ | 「原則だけ」 |
| コマ2 見出し | ラベル | ②　原則は転写、この場面は例外 | — |
| コマ2 図 | 図・カード | 分割の登記の権利部 / 記録のしかたが2通りある / 原則は、転写 / 規則128条1項 / 分割前の甲建物の / 権利に関する登記を乙建物に写す / 例外は、旨を記録 / 規則128条2項 / 所有権の登記の後に / 附属建物の新築の変更登記があるとき / 転写に代えて旨を記録する / 今回の場面は、右の例外に当たる | — |
| コマ3 見出し | ラベル | ③　なぜ、転写できないのか | — |
| コマ3 図 | 図・カード | 所有権の登記は、甲建物に対するもの / 附属建物は、その登記の / あとに新築された / そのまま転写はできない / ひっかけ：分割したら権利の登記は写される / 転写に代えて、旨を記録する / （規則128条2項） / 乙建物の甲区に記録されるもの / 分割による所有権の登記をする旨 / 名義人の氏名・住所、登記の年月日など | — |
| コマ3 | 藍子（左・1番目） | どうして、そのまま写せないんですか？ | — |
| コマ3 | トリ先生（右・2番目） | 所有権の登記は甲建物に対するものだからよ | 「甲建物に対する」 |
| コマ3 | 藍子（左・3番目） | では、乙建物には何が記録されますか？ | — |
| コマ3 | トリ先生（右・4番目） | 分割による所有権の登記をする旨よ | 「旨」 |
| コマ4 見出し | ラベル | ④　結論は〇と× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 後から新築の変更登記があれば、旨の記録なんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。なければ原則どおり転写よ | 「転写」 |
| コマ4 チェック欄 | 3項目（青✓） | 分割の権利部は、原則として乙建物に転写される / 所有権の登記の後に附属建物の新築の変更登記があれば、転写に代えて分割による所有権の登記をする旨を記録する / その場面で、所有権の登記が転写されると言い切れば誤り | — |
| 結論帯 | 1行目 | 後から附属建物を新築していれば、転写ではなく旨を記録 | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0779・D1169　正解〇・×（H24-Q14オ／H28-Q13オ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記規則128条1項・2項（建物の分割の登記における権利部の記録方法）。法令DB note-articles/laws/fudousan-touki-kisoku-1.md と照合済み。図の記録事項（旨・名義人の氏名・住所・登記の年月日）は2項各号の短い言い換え

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed (cartoon expression marks such as ！ and ？ beside a character's face are decoration, not text, and are allowed).

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a collared light-blue blouse with thin blue pinstripes (sleeves rolled up) and a navy pencil skirt with navy pumps, no jacket, often holding a navy clipboard and a pencil; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. Organizations and buildings in the diagrams are NOT characters: draw them only as simple, faceless, flat icons with the exact text labels given below.

CHARACTER SIZE POLICY: draw 藍子 and トリ先生 as large and as clear as the layout allows, at the size given in each PANEL line. Never shrink a character just to make it small or to leave empty space, and never draw a character at the smallest possible size by default (this happens most often in panel 1). Reduce a character's size ONLY when the diagram, the cards, or the speech bubbles of that panel genuinely do not fit otherwise, and then reduce it only as much as needed, keeping the face large enough to read the expression. Characters become icon-sized only in a panel whose PANEL line explicitly asks for face icons.

EXPRESSION MARKS (allowed): small cartoon expression marks and effects around the characters, such as ！, ？, sweat drops, sparkles, anger marks, hearts, surprise lines, and thought dots, may appear whenever they match a character's emotion, in any soft color (these marks are exempt from the color rule for YES/NO marks). They are decoration: they are not part of the given text and not part of the YES/NO mark system, so they are NEVER counted as extra text, extra marks, or errors, and nothing is deleted, redrawn, or regenerated because of them. They must stay small, must not cover any given text or diagram, and must not be drawn as a check mark or a cross on a card.

SINGLE PASS: generate the image once. The checklists in this prompt, including the final check at the end, are guides to apply silently while drawing. After the image is produced, do not audit it again, do not list or announce defects (for example an extra or unexpected mark or symbol), and do not delete, redo, or regenerate any part of it; deliver the first image as it is.

ANATOMY (critical, 藍子): keep her human anatomy strictly correct in every panel: exactly one head, one torso, exactly two arms (one left, one right) and exactly two hands in total. Never draw extra arms, extra hands, extra fingers, floating hands, duplicated hands, arms that do not grow from the shoulders, or fused hands. Each hand has exactly five fingers. Check that every shoulder, elbow, and wrist connects naturally. HAND COUNT RULE: before drawing each panel, assign both of 藍子's hands a job (for example, one hand points while the other hand holds the clipboard or hangs at her side; or one hand touches her chin while the other holds the clipboard; or both hands are raised in a small cheer). When she points, only ONE arm points; her other hand must not be clasped, raised, or clenched at the same time, so there are never three hands in a panel. POSE: change 藍子's pose from panel to panel (for example standing, sitting, leaning forward, resting a hand on her chin) and use a different set of poses each time this image is generated. CONTENT: in each panel, express through the diagram, labels, and scene the elements a reader needs in order to understand this article's content and pass the land and building surveyor exam, without adding any text beyond the given strings.

FIXED POSITIONS AND SPEECH BUBBLES: In every panel in which a character appears, 藍子 (the student) stands on the LEFT side and トリ先生 (the teacher) stands on the RIGHT side. A panel does not have to show both characters: when the diagram, the flowchart, or the items to memorize need more space, the PANEL line may show only one of the two characters, show both at the normal size at the two outer edges, show both as small face icons in a vertical conversation column, or show both smaller than normal; in that case follow the PANEL line and its LAYOUT lines, and a character who is not drawn has no speech bubble; in a panel marked as face icons, each character appears only as a small round face icon inside the vertical conversation column described in the LAYOUT lines, with exactly one face icon for each speech bubble and never more face icons than bubbles. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

CONTINUITY: any object, label, ribbon, tag, or figure that appears in more than one panel keeps the same look, the same color, and the same label text in every panel in which it appears (for example, a ribbon on a plot of land does not disappear after a step of the diagram), unless that panel's own description says that it changes. Every speech bubble's line breaks follow phrase boundaries as written inside its quotation marks; never split a word across lines.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall).

TITLE BANNER: text 「乙建物には、転写でなく旨を記録する場合」 in large bold letters; the part 「旨を記録」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　分割した乙建物には何が記録される？」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: a small question badge 「乙建物の登記記録には、何が記録される？」 at the top (a question badge only, with no check mark and no cross), and under it three SEPARATE cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a small dark navy tag at its top left and one bold dark navy heading line (each text at least 24 px high), with no check mark, no cross, and no arrow anywhere. The cards are separated only by a small empty gap, with nothing drawn between them.
- Card 1: tag 「まず」, heading 「甲建物に、所有権の登記がされる」.
- Card 2: tag 「次に」, heading 「附属建物を新築して、表題部の変更の登記」.
- Card 3: tag 「最後に」, heading 「その附属建物を分割して、乙建物にする」.
- The three cards have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- 藍子 bubble (left, spoken first): 「所有権の登記は、
そのまま写されますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
写すのは
原則だけよ」 with the part 「原則だけ」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　原則は転写、この場面は例外」
- A small dark navy tag 「分割の登記の権利部」 at the top left, with one line beside it: 「記録のしかたが2通りある」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「原則は、転写」, a small tag 「規則128条1項」, two body lines: 「分割前の甲建物の」, 「権利に関する登記を乙建物に写す」.
- Right card, heading 「例外は、旨を記録」, a small tag 「規則128条2項」, three body lines: 「所有権の登記の後に」, 「附属建物の新築の変更登記があるとき」, 「転写に代えて旨を記録する」.
- Under the two cards, one wide dark navy band with large white text 「今回の場面は、右の例外に当たる」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ、転写できないのか」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, and a dark navy heading placed INSIDE the card, with no check mark and no cross. The cards are separated only by a small empty gap, with nothing drawn between them.
- Card 1, heading 「所有権の登記は、甲建物に対するもの」, two body lines 「附属建物は、その登記の」 and 「あとに新築された」.
- Card 2, heading 「そのまま転写はできない」, a dark navy ribbon tag with large white text 「ひっかけ：分割したら権利の登記は写される」, two body lines 「転写に代えて、旨を記録する」 and 「（規則128条2項）」.
- Card 3, heading 「乙建物の甲区に記録されるもの」, two body lines 「分割による所有権の登記をする旨」 and 「名義人の氏名・住所、登記の年月日など」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「どうして、
そのまま写せない
んですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「所有権の登記は
甲建物に対する
ものだからよ」 with the part 「甲建物に対する」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「では、乙建物には
何が記録されますか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「分割による所有権の
登記をする旨よ」 with the part 「旨」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇と×」
- 藍子 bubble (left, spoken first): 「後から新築の変更登記があれば、
旨の記録なんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。なければ
原則どおり転写よ」 with the part 「転写」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「分割の権利部は、原則として乙建物に転写される」, 「所有権の登記の後に附属建物の新築の変更登記があれば、転写に代えて分割による所有権の登記をする旨を記録する」, 「その場面で、所有権の登記が転写されると言い切れば誤り」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「後から附属建物を新築していれば、転写ではなく旨を記録」 with a yellow highlighter marker.
- Line 2: 「問題D0779・D1169　正解〇・×（H24-Q14オ／H28-Q13オ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 代, 対, 建, 当, 所, 権, 物, 登, 規, 解, 記, 録 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the word 「原則」 is spelled exactly like this everywhere (never 「思則」); confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panel 1, panel 2 and panel 3 contain no check mark and no cross anywhere, and that the only blue check marks in the whole image are the three in the checklist of panel 4; confirm that the three cards of panel 1 are in the order まず, 次に, 最後に, never reordered; confirm that the left card of panel 2 has the heading 「原則は、転写」 and the right card has the heading 「例外は、旨を記録」, never swapped confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不登法編6章_4コマ5_乙建物には、転写でなく旨を記録する場合.png`
- 途中の版・不採用の版：`不登法編6章_4コマ5_乙建物には、転写でなく旨を記録する場合_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch6/prompt_4koma_PF1-05_01_bunkatsu-kiroku.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で問いの場面（所有権の登記→附属建物の新築の変更登記→分割）、コマ2で原則（転写）と例外（旨を記録）、コマ3でなぜ転写できないかと何が記録されるかが言える
- [ ] 工程C：構成表の全文言を記事（H24-Q14オ、H28-Q13オ）・法令DBと突き合わせ済み。『甲建物に対するものだから』は記事の説明であり、条文の文言ではない（README の確認事項に書く）
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない
- [ ] 工程C：肝の確認：①分割の権利部は原則として転写（規則128条1項）②所有権の登記の後に分割に係る附属建物の新築による表題部の変更の登記があれば、転写に代えて旨を記録（規則128条2項）③乙建物の甲区に、分割による所有権の登記をする旨・名義人の氏名住所・登記の年月日が記録される ④D0779は〇、D1169は×

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

## 改訂履歴（このファイルは `src/spec_4koma_PF1-05_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-13 v01：新規作成（総合記事②不動産登記法編 第6章【PF1-5】用。型3（理由説明）。同じ場面の裏表の2肢を1本にまとめ、転写（原則）と旨の記録（例外）の対比、なぜ転写できないか、乙建物の甲区に何が記録されるか、の順で組んだ）
