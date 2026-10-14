# D1634・D1644 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②「直前期の苦手論点つぶし 不動産登記法編」第2章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch2.md`）の、論点【PB-6】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PB-06_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D1634・D1644（不動産登記法／申請総論（却下・取下げ）、出典 R03-Q04オ／R03-Q06オ）。正解＝D1634＝×（誤った記述）／D1644＝×（誤った記述）。
- 記事：`note-articles/r3-mondai/q04-denshi-shinsei.md` オ（R03-Q04：電子申請の取下げは、電子情報処理組織を使用して取り下げる旨の情報を提供する方法による。規則39条1項1号）。ほか、R03-Q06オ（r3-mondai/q06-kyakka.md。電子申請の却下の決定書も、電磁的記録ではなく書面で作成され、申請人ごとに交付・送付される。規則38条1項・2項）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】2肢とも×だが、外し方が逆である。D1634は電子申請で出したのに、取下げは『書面を登記所に提出する方法によってすることができる』と、書面申請の取下げの方法（規則39条1項2号）を持ち込む。D1644は『電子申請の方法によってされた登記の申請を却下するときは、その決定書は電磁的記録をもって作成される』と、電子申請だから出口も電子だと思わせる。
- 【受験者の勘違い・定着していない点】（推測）①取下げの方法は、申請の方法に関係なく選べると考える（実際は申請の区分に応じて、電子申請は電子情報処理組織、書面申請は書面の提出と決まっている）。②逆に、電子申請なら却下の決定書も電子になると、取下げの『入口と出口をそろえる』を却下にまで広げる（却下の決定書は、決定書を作成して交付するもので、電子申請でも書面で交付・送付されると記事は整理している）。
- 【対比する制度】「取下げは、申請と同じ方法」⇔「却下は、決定書を作成して交付」：取下げは申請の区分に応じた方法でする（電子申請は電子で、書面申請は書面で。規則39条1項）／却下は、申請の方法にかかわらず決定書を作成して申請人ごとに交付する（送付する方法でもよい。規則38条1項・2項。電子申請でも書面で交付・送付される点は記事の整理）（結論が逆になる点）。
- 【型の選び方】型：型4（複数肢の対比。コマ1は比較表）に型3（理由のコマ）を組み合わせる。理由：2肢は別々の場面（取下げと却下）で共通の日付がなく、どちらも×だが外し方が逆で、読者は自分で並べ直せない。コマ1＝2肢の比較表（肢／申請の場面／肢の言い分）、コマ2＝分かれ目の左右のカード、コマ3＝理由のカード3枚（取下げは区分ごとに方法が決まる／却下には区分がない／電子申請でも書面と整理）と会話4つ、コマ4＝2肢とも×の整理。壁＝『書面でも取り下げられる』と『電子申請なら決定書も電子』の両極。
- コマごとに読者が言えること：コマ1＝2肢は、電子申請をした後の取下げと、電子申請の却下の決定書で、言い分が逆向きに外している。コマ2＝取下げは申請と同じ方法でする。却下は、決定書を作成して交付する。コマ3＝取下げは申請の区分ごとに方法が決まるが、却下には区分ごとの定めがなく、電子申請でも書面で交付・送付と整理される。コマ4＝D1634もD1644も×。
- 記事の範囲：R03-Q04オ（規則39条1項1号・2号）、R03-Q06オ（規則38条1項・2項）。条文は法令DB（note-articles/laws/fudousan-touki-kisoku-1.md 第38条・第39条）で原文を確認した。規則38条は『決定書を作成して、これを申請人ごとに交付する』『送付する方法によりすることができる』と定めるのみで、電子申請の決定書が書面であることまでは条文からは言えない。図では『書面で交付・送付』を『整理による』と添えて断定せず、『電磁的記録で作るとは定めていない』という条文の範囲の事実と分けた。
- extra_refs：不動産登記規則38条1項（登記官は、申請を却下するときは、決定書を作成して、これを申請人ごとに交付するものとする。代理人によって申請がされた場合は、当該代理人に交付すれば足りる）・同2項（前項の交付は、当該決定書を送付する方法によりすることができる）、同39条1項（申請の取下げは、電子申請は電子情報処理組織を使用して申請を取り下げる旨の情報を登記所に提供する方法、書面申請は申請を取り下げる旨の情報を記載した書面を登記所に提出する方法）は、法令DBで原文を確認した。
- 登場人物：人型は使わず、取下げ・決定書は文字のカードで示す。
- 矢印の意味：矢印は使わない。コマ1は表、コマ2は左右のカード、コマ3は縦3枚のカード。
- 配色：コマ1〜3は印（✓✕）を付けない。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、帯・リボンは濃紺（白文字）、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝small（表が横いっぱいに要るので、キャラは小さく。約150px）、コマ2＝none（図が主役）、コマ3＝faces（左に理由のカード3枚、右に会話4つの縦並び）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 取下げは、申請と同じ方法で | 「同じ方法」を黄色マーカー |
| コマ1 見出し | ラベル | ①　2つの肢は、場面が違う | — |
| コマ1 図 | 図・カード | 肢 / 電子申請の場面 / 肢の言い分 / 肢D1634 / 電子申請をした後の、申請の取下げ / 取り下げる旨の書面を登記所に提出する方法でできる / 肢D1644 / 電子申請を却下するときの、決定書 / その決定書は、電磁的記録で作成される | — |
| コマ1 | 藍子（左・先に話す） | 電子申請なら、どちらも電子ですよね？ | — |
| コマ1 | トリ先生（右・答える） | どちらの肢も×よ。外し方は逆なの | 「外し方は逆」 |
| コマ2 見出し | ラベル | ②　取下げと却下は、方法の決まり方が違う | — |
| コマ2 図 | 図・カード | 不動産登記規則 / 電子申請をした後の、出口の話 / 取下げは、申請と同じ方法 / 規則39条1項 / 電子申請は、電子で取り下げる / 書面申請は、書面で取り下げる / 肢D1634は、こちらの場面 / 却下は、決定書を作成して交付 / 規則38条1項・2項 / 申請の方法に関係なく、決定書を交付 / 送付する方法でもよい / 肢D1644は、こちらの場面 / 入口と出口をそろえるのは、取下げの方 | — |
| コマ3 見出し | ラベル | ③　電子申請でも、決定書は別 | — |
| コマ3 図 | 図・カード | 取下げは、申請の区分で決まる / 電子申請は、電子情報処理組織を使用して / 書面申請は、書面を提出して / 却下には、区分ごとの定めがない / 決定書を作成して、申請人ごとに交付 / 送付する方法でもよい / 電子申請の決定書も、書面と整理 / ひっかけ：電子申請なら、決定書も電子 / 電磁的記録で作るとは、定めていない / 書面で、という点は整理による | — |
| コマ3 | 藍子（左・1番目） | 電子申請なら、決定書も電子ですよね？ | — |
| コマ3 | トリ先生（右・2番目） | それが罠。そろえるのは取下げの方よ | 「それが罠」 |
| コマ3 | 藍子（左・3番目） | では、決定書はどうなるのですか？ | — |
| コマ3 | トリ先生（右・4番目） | 書面で交付か送付、と整理されているわ | 「書面で交付か送付」 |
| コマ4 見出し | ラベル | ④　結論は×と× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | どちらの肢も、×なんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。取下げと却下は、別の話よ | 「別の話」 |
| コマ4 チェック欄 | 3項目（青✓） | 電子申請の取下げは、電子情報処理組織で行う（規則39条1項。肢D1634は×） / 書面申請の取下げは、取り下げる旨の書面の提出で行う（規則39条1項） / 却下は決定書を作成して交付する。電子申請でも書面と整理（肢D1644は×） | — |
| 結論帯 | 1行目 | 取下げは申請と同じ方法。却下は決定書を作成して交付 | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1634・D1644　正解×・×（R03-Q04オ／R03-Q06オ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記規則38条1項・2項（申請の却下：決定書を作成して申請人ごとに交付。送付する方法でもよい）、同39条1項（申請の取下げ：電子申請は電子情報処理組織を使用する方法、書面申請は書面を提出する方法）。法令DB note-articles/laws/fudousan-touki-kisoku-1.md と照合済み

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

TITLE BANNER: text 「取下げは、申請と同じ方法で」 in large bold letters; the part 「同じ方法」 has a yellow highlighter marker.

PANEL 1 (curious, puzzled mood; both characters appear SMALLER than in the other panels, only because this panel's diagram or text needs the room (each about 150 px tall; never below 110 px and never more than one third of the panel height; use the largest size in this range that still lets the diagram fill the panel), 藍子 at the lower left corner and トリ先生 at the lower right corner; 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　2つの肢は、場面が違う」
- A wide table that fills the full panel width. The header row is dark navy with white text and has three columns: 「肢」, 「電子申請の場面」, 「肢の言い分」. The two body rows have the same pale gray fill and a dark navy outline, each text at least 24 px high, with no check mark, no cross, and no arrow.
- Body row 1: 「肢D1634」, 「電子申請をした後の、申請の取下げ」, 「取り下げる旨の書面を登記所に提出する方法でできる」.
- Body row 2: 「肢D1644」, 「電子申請を却下するときの、決定書」, 「その決定書は、電磁的記録で作成される」.
- The two rows have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- 藍子 bubble (left, spoken first): 「電子申請なら、
どちらも電子
ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「どちらの肢も×よ。
外し方は逆なの」 with the part 「外し方は逆」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　取下げと却下は、方法の決まり方が違う」
- A small dark navy tag 「不動産登記規則」 at the top left, with one line beside it: 「電子申請をした後の、出口の話」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「取下げは、申請と同じ方法」, a small tag 「規則39条1項」, two body lines: 「電子申請は、電子で取り下げる」, 「書面申請は、書面で取り下げる」, and a small dark navy tag 「肢D1634は、こちらの場面」.
- Right card, heading 「却下は、決定書を作成して交付」, a small tag 「規則38条1項・2項」, two body lines: 「申請の方法に関係なく、決定書を交付」, 「送付する方法でもよい」, and a small dark navy tag 「肢D1644は、こちらの場面」.
- Under the two cards, one wide dark navy band with large white text 「入口と出口をそろえるのは、取下げの方」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　電子申請でも、決定書は別」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, and a dark navy heading placed INSIDE the card, with no check mark and no cross. The cards are separated only by a small empty gap, with nothing drawn between them.
- Card 1, heading 「取下げは、申請の区分で決まる」, two body lines 「電子申請は、電子情報処理組織を使用して」 and 「書面申請は、書面を提出して」.
- Card 2, heading 「却下には、区分ごとの定めがない」, two body lines 「決定書を作成して、申請人ごとに交付」 and 「送付する方法でもよい」.
- Card 3, heading 「電子申請の決定書も、書面と整理」, a dark navy ribbon tag with large white text 「ひっかけ：電子申請なら、決定書も電子」, two body lines 「電磁的記録で作るとは、定めていない」 and 「書面で、という点は整理による」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「電子申請なら、
決定書も電子
ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「それが罠。
そろえるのは
取下げの方よ」 with the part 「それが罠」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「では、決定書は
どうなるのですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「書面で交付か
送付、と整理
されているわ」 with the part 「書面で交付か送付」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は×と×」
- 藍子 bubble (left, spoken first): 「どちらの肢も、
×なんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
取下げと却下は、
別の話よ」 with the part 「別の話」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「電子申請の取下げは、電子情報処理組織で行う（規則39条1項。肢D1634は×）」, 「書面申請の取下げは、取り下げる旨の書面の提出で行う（規則39条1項）」, 「却下は決定書を作成して交付する。電子申請でも書面と整理（肢D1644は×）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「取下げは申請と同じ方法。却下は決定書を作成して交付」 with a yellow highlighter marker.
- Line 2: 「問題D1634・D1644　正解×・×（R03-Q04オ／R03-Q06オ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 所, 登, 肢, 規, 解, 記, 請, 違, 録 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the smaller characters are drawn within the specified size range (they must not grow and squeeze the diagram, and must not be shrunk below the range) and that nothing but the given text appears above the heads of the pictograms; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panel 1, panel 2 and panel 3 contain no check mark and no cross anywhere, and that the only blue check marks in the whole image are the three in the checklist of panel 4; confirm that the table in panel 1 has exactly two body rows, 「肢D1634」 first and 「肢D1644」 second, never swapped; confirm that the left card of panel 2 has the heading 「取下げは、申請と同じ方法」 with the tag 「肢D1634は、こちらの場面」 and the right card has the heading 「却下は、決定書を作成して交付」 with the tag 「肢D1644は、こちらの場面」, never swapped confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不動産登記法編2章_4コマ6_取下げは、申請と同じ方法で.png`
- 途中の版・不採用の版：`不動産登記法編2章_4コマ6_取下げは、申請と同じ方法で_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch2/prompt_4koma_PB-06_01_torisage-kyakka.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で2肢の場面（電子申請の取下げと、電子申請の却下の決定書）の違い、コマ2で取下げは申請と同じ方法・却下は決定書を作成して交付、コマ3で取下げは区分ごとに方法が決まるが却下にはその区分がないことが言える
- [ ] 工程C：構成表の全文言を記事（R03-Q04オ、R03-Q06オ）・法令DB（規則38条・39条）と突き合わせ済み
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方は small→none→faces→既定 で隣り合うコマが同じにならない
- [ ] 工程C：肝の確認：①電子申請の取下げは電子情報処理組織で、書面申請の取下げは書面の提出で（規則39条1項） ②却下は決定書を作成して交付（送付もできる。規則38条1項・2項） ③電子申請の決定書が書面で交付・送付される点は整理 ④D1634もD1644も×

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

## 改訂履歴（このファイルは `src/spec_4koma_PB-06_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-13 v01：新規作成（総合記事②不動産登記法編 第2章【PB-6】用。型4（複数肢の対比。コマ1は比較表）＋型3（理由のコマ）。外し方が逆の2肢を、取下げ（申請と同じ方法）と却下（決定書を作成して交付）で並べた）
