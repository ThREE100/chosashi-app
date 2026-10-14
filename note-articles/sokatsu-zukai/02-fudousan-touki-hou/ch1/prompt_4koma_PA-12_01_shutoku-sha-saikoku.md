# D0944・D1325 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②「直前期の苦手論点つぶし 不動産登記法編」第1章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch1.md`）の、論点【PA-12】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PA-12_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D0944・D1325（不動産登記法／申請総論（申請義務と登記官の催告）、出典 H26-Q07ウ／H30-Q05ア）。正解＝D0944＝〇（正しい記述）／D1325＝〇（正しい記述）。
- 記事：`note-articles/h26-mondai/q07-shinsei-gimu.md` ウ（H26：表題登記のない土地を売買で取得した買主にも、取得の日から1か月以内の表題登記の申請義務がある。法36条）。ほか、ア（h30-mondai/q05-tokikan-chousa.md。申請すべき事項で申請のないものを発見しても、直ちに職権で登記せず、まず申請義務のある者に催告する。準則63条1項）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】D0944は『Aが表題登記を申請することなくBに売却し、Bが所有権を取得した』という場面で、登記をしていないのは売主Aなのだから、申請するのもAだと読ませる。D1325は『申請をすべき事項で申請のないものを発見した』場面で、表示に関する登記は登記官が職権でもできる（法28条）という知識を思い出させ、『直ちに職権でその登記をすることなく』を誤りに見せる。どちらも、言い切りの向きを疑いたくなる書き方になっている。
- 【受験者の勘違い・定着していない点】（推測）①申請義務は、登記をしていない元の所有者にあると考え、新たに所有権を取得した者に義務が及ぶことが結びつかない。②表示に関する登記は職権でもできるので、申請がなければ登記官が自分でやってしまうと考える。③『職権でできる』ことと『直ちに職権でする』ことを同じに扱い、申請義務のある事項ではまず催告するという順番を知らない。
- 【対比する制度】「元の所有者だけ」⇔「取得した者にも」：元の所有者だけに義務があるという思い込みでは×にしてしまうが、表題登記のない土地の所有権を取得した者にも、取得の日から1か月以内の申請義務がある（法36条。結論が逆になる点）。「直ちに職権で登記」⇔「まず催告」：職権でもできるからと直ちに登記するのではなく、申請義務のある事項で申請のないものは、まず申請義務のある者に催告する（準則63条1項。結論が逆になる点）。
- 【型の選び方】型：型4（複数肢の対比。型5の整理カードを併用）。理由：2肢は別々の場面で共通の日付はないので、コマ1は肢と場面と肢の言い分の比較表にした。コマ2は『論点／思い込み／正しい整理』の2行の表で、二つの思い込みを同じ形で対比し、コマ3は左に✕✓の上下2枚のカード、右に会話1往復と、義務の整理カード（誰が・いつまでに・申請がなければ）を置いた。壁＝『元の所有者だけが義務を負う』『職権でできるから直ちに登記する』という二つの思い込み。
- コマごとに読者が言えること：コマ1＝2つの肢は、表題登記のない土地を買った者に申請義務があるか、申請のないものを見つけた登記官がどうするかを問うている。コマ2＝義務は取得した者にもあり、申請がないときは直ちに職権で登記せずまず催告する。コマ3＝思い込みは二つとも誤りで、取得者にも義務があり、登記官は先に催告する。コマ4＝D0944もD1325も〇。
- 記事の範囲：H26-Q07ウ（法36条）、H30-Q05ア（準則63条1項）、総合記事②第1章【PA-12】の整理（取得者にも義務がある・表示に関する登記は職権でもできる〔法28条〕が、申請義務のある事項で申請のないものはまず催告する）。準則63条1項は、登記官の取扱いを定めた準則の規定（実務の取扱い）であり、法律が催告を定めているわけではないので、図でもそのように添えた。なぜ直ちに職権でしないのかの理由は条文に書かれていないので、図には理由を入れていない。D1491（法51条1項の変更登記の義務）は既存の4コマがあるので入れていない。
- extra_refs：不動産登記法36条（新たに生じた土地又は表題登記がない土地の所有権を取得した者は、その所有権の取得の日から一月以内に、表題登記を申請しなければならない）、28条（表示に関する登記は、登記官が、職権ですることができる）、164条1項（36条などの規定による申請をすべき義務がある者が正当な理由がないのにその申請を怠ったときは、十万円以下の過料）、不動産登記事務取扱手続準則63条1項（登記官は、法36条などの規定による申請をすべき事項で申請のないものを発見した場合には、直ちに職権でその登記をすることなく、申請の義務がある者に登記の申請を催告するものとする）は、法令DB note-articles/laws/fudousan-touki-hou.md・fudousan-touki-jimu-junsoku.md で原文を確認。
- 登場人物：当事者の人型は使わず、売った元の所有者（甲）と買った取得者（乙）は文字のカードと表で示す。コマ1の表で甲・乙を紹介してから使う。
- 矢印の意味：矢印は使わない。コマ1は表、コマ2は表、コマ3は上下のカードと整理カード。
- 配色：コマ1・2は印（✓✕）を付けない。コマ3の左は上＝✕、下＝✓の1個ずつ。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝small（表が横いっぱいに要るので、キャラは小さく）、コマ2＝none（図が主役）、コマ3＝faces（左に上下2枚のカード、右に会話2つと整理カード）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。
- 肢は、カードの小タグ・整理カード・チェック欄に『肢D0944』『肢D1325』と肢IDで示す（試験の問の記号『ウ』『ア』は図に使わない）。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 取得者にも義務、まず催告 | 「まず催告」を黄色マーカー |
| コマ1 見出し | ラベル | ①　買った人の義務と、登記官の対応 | — |
| コマ1 図 | 図・カード | 肢 / 場面 / 肢の言い分 / 肢D0944 / 表題登記のない土地を、甲が乙に売った / 買った乙も、1か月以内に表題登記を申請する / 肢D1325 / 申請すべき事項で、申請がない / 登記官は、直ちに職権で登記せず、催告する / 誰に義務？ 申請がなければ？ | — |
| コマ1 | 藍子（左・先に話す） | 義務は、売った人だけですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。登記官も、職権とは限らないわよ | 「職権とは限らない」 |
| コマ2 見出し | ラベル | ②　二つの思い込みと、正しい整理 | — |
| コマ2 図 | 図・カード | 申請義務の整理 / 思い込みと、正しい整理 / 論点 / 思い込み / 正しい整理 / 申請義務を負う人 / 元の所有者だけ / 取得した者にも義務がある（法36条） / 取得した者にも / 申請がないとき / 直ちに職権で登記 / まず催告する（準則63条1項・実務の取扱い） / まず催告 / 表示に関する登記は、職権でもできる（法28条） | — |
| コマ3 見出し | ラベル | ③　義務は取得者にも、先に催告 | — |
| コマ3 図 | 図・カード | 義務は元の所有者だけ。見つけたら直ちに職権で登記 / 二つの思い込み / 取得者にも義務。申請がなければ、まず催告 / 肢D0944・肢D1325の言い分 / 申請義務の整理 / 誰が：土地の所有権を取得した者（肢D0944） / いつまでに：取得の日から1か月以内 / 申請がなければ：直ちに登記せず、まず催告（肢D1325） / ひっかけ：元の所有者だけ・直ちに職権で / 元の所有者だけ | — |
| コマ3 | 藍子（左・1番目） | 見つけたら、登記官がすぐ登記しますよね？ | — |
| コマ3 | トリ先生（右・2番目） | いいえ。義務のある人へ、まず催告よ | 「まず催告」 |
| コマ4 見出し | ラベル | ④　結論は〇と〇 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 取得者にも義務で、先に催告なんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。職権でできても、順番があるのよ | 「順番がある」 |
| コマ4 チェック欄 | 3項目（青✓） | 表題登記のない土地を取得した者にも、取得の日から1か月以内の申請義務がある（肢D0944は〇） / 申請のないものを見つけても、直ちに職権で登記せず、まず催告する（肢D1325は〇） / 表示に関する登記は職権でもできる（法28条）が、先に催告する | — |
| 結論帯 | 1行目 | 取得者にも申請義務。申請がなければまず催告 | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0944・D1325　正解〇・〇（H26-Q07ウ／H30-Q05ア） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記法36条・28条・164条1項、不動産登記事務取扱手続準則63条1項。法令DB note-articles/laws/fudousan-touki-hou.md・fudousan-touki-jimu-junsoku.md と照合済み

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

TITLE BANNER: text 「取得者にも義務、まず催告」 in large bold letters; the part 「まず催告」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear SMALLER than in the other panels, only because this panel's diagram or text needs the room (each about 150 px tall; never below 110 px and never more than one third of the panel height; use the largest size in this range that still lets the diagram fill the panel), 藍子 at the lower left corner and トリ先生 at the lower right corner; 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　買った人の義務と、登記官の対応」
- A wide table that fills the full panel width. The header row is dark navy with white text and has three columns: 「肢」, 「場面」, 「肢の言い分」. The two body rows have the same pale gray fill and a dark navy outline, each text at least 24 px high, with no check mark, no cross, and no arrow.
- Body row 1: 「肢D0944」, 「表題登記のない土地を、甲が乙に売った」, 「買った乙も、1か月以内に表題登記を申請する」.
- Body row 2: 「肢D1325」, 「申請すべき事項で、申請がない」, 「登記官は、直ちに職権で登記せず、催告する」.
- In the third column, the two strings differ; copy each exactly as given and do not change one into the other.
- A small question badge 「誰に義務？ 申請がなければ？」 with a pale gray fill and a dark navy outline sits at the upper right of the table (a question badge only, with no check mark and no cross).
- 藍子 bubble (left, spoken first): 「義務は、売った人
だけですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
登記官も、職権とは
限らないわよ」 with the part 「職権とは限らない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　二つの思い込みと、正しい整理」
- A small dark navy tag 「申請義務の整理」 at the top left, with one line beside it: 「思い込みと、正しい整理」.
- A wide table in the center that fills the full panel width. The header row is dark navy with white text and has three columns: 「論点」, 「思い込み」, 「正しい整理」. The two body rows have the same pale gray fill and a dark navy outline, each text at least 24 px high, with no check mark, no cross, and no arrow.
- Body row 1: 「申請義務を負う人」, 「元の所有者だけ」, 「取得した者にも義務がある（法36条）」, with the string 「取得した者にも」 highlighted with a yellow marker.
- Body row 2: 「申請がないとき」, 「直ちに職権で登記」, 「まず催告する（準則63条1項・実務の取扱い）」, with the string 「まず催告」 highlighted with a yellow marker.
- Under the table, one dashed dark navy outlined note card with one line: 「表示に関する登記は、職権でもできる（法28条）」.
- The cells of the second and third columns have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　義務は取得者にも、先に催告」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 2 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 120 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 2 face icons and exactly 2 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.
- LEFT SIDE: two stacked cards of the same size, top and bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card, with no arrow and no connector. The cards are separated only by a small empty gap.
- Top card, heading 「義務は元の所有者だけ。見つけたら直ちに職権で登記」, body 「二つの思い込み」, and ONE red cross only at the bottom of this card (no check mark on this card).
- Bottom card, heading 「取得者にも義務。申請がなければ、まず催告」, body 「肢D0944・肢D1325の言い分」, and ONE blue check mark only at the bottom of this card (no cross on this card).
- RIGHT SIDE, under the two speech bubbles (the two speech bubbles and their two faces stay at the top of the right side): one tall list card with a dark navy heading 「申請義務の整理」, with the same pale gray fill and a dark navy outline, containing exactly three short rows, each with a small dark navy dot at its left end (NO digit and NO letter on the dots), with no arrow and no check mark and no cross: 「誰が：土地の所有権を取得した者（肢D0944）」, 「いつまでに：取得の日から1か月以内」, 「申請がなければ：直ちに登記せず、まず催告（肢D1325）」. Under the three rows, one small dark navy ribbon tag with white text 「ひっかけ：元の所有者だけ・直ちに職権で」, with the text 「元の所有者だけ」 highlighted with a yellow marker.
- The list card is a part of the right side, and it is NOT a speech bubble. The left cards and the list card have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 2 in the conversation column; face icon at the LEFT end of its own row): 「見つけたら、
登記官がすぐ
登記しますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 2 in the conversation column; face icon at the RIGHT end of its own row): 「いいえ。
義務のある人へ、
まず催告よ」 with the part 「まず催告」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇と〇」
- 藍子 bubble (left, spoken first): 「取得者にも義務で、
先に催告
なんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
職権でできても、
順番があるのよ」 with the part 「順番がある」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「表題登記のない土地を取得した者にも、取得の日から1か月以内の申請義務がある（肢D0944は〇）」, 「申請のないものを見つけても、直ちに職権で登記せず、まず催告する（肢D1325は〇）」, 「表示に関する登記は職権でもできる（法28条）が、先に催告する」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「取得者にも申請義務。申請がなければまず催告」 with a yellow highlighter marker.
- Line 2: 「問題D0944・D1325　正解〇・〇（H26-Q07ウ／H30-Q05ア）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 地, 売, 対, 所, 権, 番, 登, 肢, 解, 記, 請, 買 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the left comparison card has only a red cross and the right card only a blue check mark; confirm that the smaller characters are drawn within the specified size range (they must not grow and squeeze the diagram, and must not be shrunk below the range) and that nothing but the given text appears above the heads of the pictograms; confirm that the conversation column has exactly 2 face icons and exactly 2 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panel 1 and panel 2 contain no check mark and no cross anywhere, that the only red cross in the whole image is the one at the bottom of the top-left card of panel 3 and the only blue check marks are the one at the bottom of the bottom-left card of panel 3 and the three in the checklist of panel 4; confirm that the columns of the table in panel 2 are in the order 論点, 思い込み, 正しい整理, never swapped; confirm that the rows of the table in panel 1 are in the order 肢D0944, 肢D1325, never swapped confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不登法編1_4コマ12_取得者にも義務、まず催告.png`
- 途中の版・不採用の版：`不登法編1_4コマ12_取得者にも義務、まず催告_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch1/prompt_4koma_PA-12_01_shutoku-sha-saikoku.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1の表で、2つの肢が買った者の申請義務と、申請のないものを見つけた登記官の対応を問うていること、コマ2で二つの思い込みと正しい整理、コマ3で取得者にも義務があり先に催告することが言える
- [ ] 工程C：構成表の全文言を記事（H26-Q07ウ、H30-Q05ア、総合記事②第1章【PA-12】）・法令DB（法36条・28条・164条1項、準則63条1項）と突き合わせ済み。催告の理由は条文にないので図に入れず、準則63条1項は実務の取扱いと添えた。元の所有者に義務がないとは書いていない（『元の所有者だけ』を誤りとするにとどめた）
- [ ] 工程C：コマ1・2に印がなく、コマ3の左は上＝✕・下＝✓の1個ずつ、コマ4だけ青✓。コマの使い方は small→none→faces→既定 で隣り合うコマが同じにならない
- [ ] 工程C：肝の確認：①表題登記のない土地の所有権を取得した者は、取得の日から1か月以内に申請義務を負う ②表示に関する登記は職権でもできるが、申請のないものを見つけても直ちに職権で登記せず、まず催告する ③D0944・D1325はいずれも〇

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

## 改訂履歴（このファイルは `src/spec_4koma_PA-12_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-14 v01：新規作成（総合記事②不動産登記法編 第1章【PA-12】用。型4に型5の整理カードを併用。取得者にも申請義務があること、申請のないものは直ちに職権で登記せずまず催告することの二つの思い込みを、同じ形の表で対比し、義務の整理カードを組んだ。D1491は既存の4コマがあるので入れていない）
