# D0573・D0574・D0575・D1983 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②不動産登記法編 第6章「建物の分割・分棟・合併」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch6.md`）の、論点【PF1-4】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PF1-4_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D0573・D0574・D0575・D1983（不動産登記法／建物の分割・合併・合体・滅失・変更、出典 H22-Q13ウ・エ・オ／R06-Q16エ）。正解＝D0573＝×（誤った記述）／D0574＝×（誤った記述）／D0575＝〇（正しい記述）／D1983＝×（誤った記述）。
- 記事：`note-articles/h22-mondai/q13-bunmune.md` ウ・エ・オ（H22：分棟の登記は表題部の変更の登記。課税されない。抹消＋表題登記を一の申請情報でする決まりはない。分棟と分割は一の申請情報にできる）。ほか、R06-Q16エ（r6-mondai/q16-tatemono-bunkatsu-gappei.md。分棟による表題部の変更の登記と分割の登記は、一の申請情報で申請できる）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】4肢とも『分棟』を扱う。D0574は『表題部の抹消の登記と表題登記を一の申請情報によってしなければならない』と、分棟を滅失と新築のように手続を決めつける。D0573は『所有権の登記がある建物の…登録免許税を納付しなければならない』と、所有権の登記があることから課税を匂わせる。D1983は『表題部の変更の登記と建物の分割の登記とは、一の申請情報により申請することができない』と、目的の違う登記は別々に申請するという感覚に乗せる。正しいD0575（分棟と分割は一の申請情報にできる）を、見落とさせる。
- 【受験者の勘違い・定着していない点】（推測）①分棟を、前の建物を消して新しく登記し直すものと考える（D0574）。②所有権の登記がある建物の登記だから課税されると考え、分割・合併が課税されることと混同する（D0573）。③目的の違う登記は別々に申請と考え、一括できる例外（規則35条7号）を思い出せない（D1983・D0575）。④分棟だけでは主である建物と附属建物のままで、別個の建物にするには分割の登記も要ることが定着していない。
- 【対比する制度】「分棟の登記」⇔「分割の登記」：分棟の登記は、1棟の建物を主である建物と附属建物にする表題部の変更の登記で、表示に関する登記なので課税されない／分割の登記は、附属建物を別個の建物にする登記で、分棟の後に主従のない2棟にするには必要（別の登記だが一の申請情報にできる。結論が逆に見える点）。
- 【型の選び方】型：型4（4肢の比較表。型5の整理カード併用）。理由：4肢は同じ『分棟』の裏表だが、問いの角度（申請の組み立て・課税・分割との一括）が別々なので、コマ1は『場面／問われていること』の比較表にした。結論は『分棟は表題部の変更』という1つの理解から全部導けるので、コマ3の右側は会話1往復と、分棟の登記の押さえどころ4つの整理カードにした。コマ2は『分棟の登記』と『分割の登記』の左右の対比。壁＝『分棟を滅失と新築のように考える』『目的が違えば別々の申請と考える』。
- コマごとに読者が言えること：コマ1＝4つの肢は、分棟の登記の申請の組み立て・課税・分割との一括を問うている。コマ2＝分棟は表題部の変更（主である建物と附属建物にする）、分割は別個の建物にする別の登記。コマ3＝分棟の押さえどころは、表題部の変更・抹消＋表題登記の組ではない・課税なし・分割と一括できるの4つ。コマ4＝D0573・D0574・D1983は×、D0575は〇。
- 記事の範囲：H22-Q13ウ・エ・オ（分棟は表題部の変更の登記。表示に関する登記は原則として登録免許税が課されない。抹消＋表題登記を一の申請情報でする決まりはなく、規則35条の各号にも挙がらない。分棟後の2棟を別個の建物にするなら分棟の登記と分割の登記を一の申請情報にできる）、R06-Q16エ（分棟による表題部の変更の登記をすると、主である建物と附属建物の扱いになるので、主従のない2棟にするには分割の登記も要る。この2つは特別に一の申請情報で申請できる）。分割の登記に課税されるかどうかは、これらの記事にないので図に入れなかった。
- extra_refs：規則35条7号（同一の不動産について申請する二以上の登記が、不動産の表題部の登記事項に関する変更の登記又は更正の登記及び建物の分割の登記…であるとき）は法令DB note-articles/laws/fudousan-touki-kisoku-1.md で原文を確認。H22-Q13エの記事に『35条の6号・7号』として出る。図の『規則35条7号』はこの文言の短い言い換え。
- 登場人物：人型は使わず、建物・登記は文字のカードで示す。
- 矢印の意味：矢印は使わない。コマ1は2列の比較表、コマ2は左右のカード、コマ3は左に上下2枚のカード・右に整理カード。
- 配色：コマ1・2は印（✓✕）を付けない。コマ3の左は上＝✕、下＝✓の1個ずつ。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、帯・リボンは濃紺（白文字）、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝side、コマ2＝none（図が主役）、コマ3＝faces（左に上下2枚のカード、右に会話2つと整理カード）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 分棟は表題部の変更で、分割と一括できる | 「表題部の変更」を黄色マーカー |
| コマ1 見出し | ラベル | ①　分棟の登記、4つの問い | — |
| コマ1 図 | 図・カード | 分棟の登記は、どう扱う？ / 場面 / 問われていること / 申請の組み立て / 抹消と表題登記を一の申請情報で？ / 登録免許税 / 所有権の登記があれば納付？ / 別個の建物にする / 分棟と分割を一の申請情報に？ / 2棟とも主である建物 / 変更と分割は一の申請情報にできない？ | — |
| コマ1 | 藍子（左・先に話す） | 分棟は、消して登記し直すんですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。分棟は表題部の変更よ | 「表題部の変更」 |
| コマ2 見出し | ラベル | ②　分棟の登記と、分割の登記 | — |
| コマ2 図 | 図・カード | 1棟の建物を2棟にしたとき / 2つの登記は、別の登記 / 分棟の登記 / 表題部の変更の登記 / 1棟を主である建物と附属建物にする / 表示に関する登記なので、課税なし / 分割の登記 / 別個の建物にする登記 / 附属建物を別の1個の建物にする / 分棟の後に主従をなくすなら必要 / 別の登記でも、一の申請情報にできる | — |
| コマ3 見出し | ラベル | ③　分棟の押さえどころは4つ | — |
| コマ3 図 | 図・カード | 分棟は、消して新しく登記し直す / 抹消と表題登記を一の申請情報でする / 分棟は、表題部の変更の登記 / 抹消と表題登記の組という決まりはない / 分棟の登記の押さえどころ / 表題部の変更の登記 / 抹消と表題登記の組ではない / 表示の登記なので課税なし / 分割と一の申請情報にできる / 別個の建物にするなら、分割も要る | — |
| コマ3 | 藍子（左・1番目） | 目的が違うのに、まとめていいんですか？ | — |
| コマ3 | トリ先生（右・2番目） | 同一の不動産なら、35条7号の例外よ | 「35条7号」 |
| コマ4 見出し | ラベル | ④　結論は×・×・〇・× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 分棟は表題部の変更なんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。課税もなく、分割とも一括よ | 「一括」 |
| コマ4 チェック欄 | 3項目（青✓） | 分棟の登記は表題部の変更の登記で、抹消と表題登記を一の申請情報でする決まりはない / 表示に関する登記なので、所有権の登記がある建物でも登録免許税はかからない / 2棟を別個の建物とするなら、分棟の登記と分割の登記は一の申請情報でできる | — |
| 結論帯 | 1行目 | 分棟は表題部の変更。分割とは一の申請情報にできる | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0573・D0574・D0575・D1983　正解×・×・〇・×（H22-Q13ウ・エ・オ／R06-Q16エ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記規則35条7号（一の申請情報によって申請することができる場合）。法令DB note-articles/laws/fudousan-touki-kisoku-1.md と照合済み。H22-Q13エの記事に『6号・7号』として出る

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

TITLE BANNER: text 「分棟は表題部の変更で、分割と一括できる」 in large bold letters; the part 「表題部の変更」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　分棟の登記、4つの問い」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: a small question badge 「分棟の登記は、どう扱う？」 at the top (a question badge only, with no check mark and no cross), and under it a two-column table with a dark navy header row (white text) 「場面」 and 「問われていること」, and exactly four body rows with the same pale gray fill and a dark navy outline, each text at least 24 px high, with no check mark, no cross, and no arrow anywhere.
- Body row 1: 「申請の組み立て」, 「抹消と表題登記を一の申請情報で？」.
- Body row 2: 「登録免許税」, 「所有権の登記があれば納付？」.
- Body row 3: 「別個の建物にする」, 「分棟と分割を一の申請情報に？」.
- Body row 4: 「2棟とも主である建物」, 「変更と分割は一の申請情報にできない？」.
- The rows have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- 藍子 bubble (left, spoken first): 「分棟は、消して
登記し直すんですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
分棟は
表題部の変更よ」 with the part 「表題部の変更」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　分棟の登記と、分割の登記」
- A small dark navy tag 「1棟の建物を2棟にしたとき」 at the top left, with one line beside it: 「2つの登記は、別の登記」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「分棟の登記」, a small tag 「表題部の変更の登記」, two body lines: 「1棟を主である建物と附属建物にする」, 「表示に関する登記なので、課税なし」.
- Right card, heading 「分割の登記」, a small tag 「別個の建物にする登記」, two body lines: 「附属建物を別の1個の建物にする」, 「分棟の後に主従をなくすなら必要」.
- Under the two cards, one wide dark navy band with large white text 「別の登記でも、一の申請情報にできる」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　分棟の押さえどころは4つ」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 2 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 120 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 2 face icons and exactly 2 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.
- LEFT SIDE: two stacked cards of the same size, top and bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card, with no arrow and no connector. The cards are separated only by a small empty gap.
- Top card, heading 「分棟は、消して新しく登記し直す」, body 「抹消と表題登記を一の申請情報でする」, and ONE red cross only at the bottom of this card (no check mark on this card).
- Bottom card, heading 「分棟は、表題部の変更の登記」, body 「抹消と表題登記の組という決まりはない」, and ONE blue check mark only at the bottom of this card (no cross on this card).
- RIGHT SIDE, under the two speech bubbles (the two speech bubbles and their two faces stay at the top of the right side): one tall list card with a dark navy heading 「分棟の登記の押さえどころ」, with the same pale gray fill and a dark navy outline, containing exactly four short rows, each with a small dark navy dot at its left end (NO digit and NO letter on the dots), with no arrow and no check mark and no cross: 「表題部の変更の登記」, 「抹消と表題登記の組ではない」, 「表示の登記なので課税なし」, 「分割と一の申請情報にできる」. The row 「分割と一の申請情報にできる」 is highlighted with a yellow marker. Under the four rows, one small dark navy ribbon tag with white text 「別個の建物にするなら、分割も要る」.
- The list card is a part of the right side, and it is NOT a speech bubble. The left cards and the list card have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 2 in the conversation column; face icon at the LEFT end of its own row): 「目的が違うのに、
まとめていいんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 2 in the conversation column; face icon at the RIGHT end of its own row): 「同一の不動産なら、
35条7号の例外よ」 with the part 「35条7号」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は×・×・〇・×」
- 藍子 bubble (left, spoken first): 「分棟は
表題部の変更
なんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。課税もなく、
分割とも一括よ」 with the part 「一括」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「分棟の登記は表題部の変更の登記で、抹消と表題登記を一の申請情報でする決まりはない」, 「表示に関する登記なので、所有権の登記がある建物でも登録免許税はかからない」, 「2棟を別個の建物とするなら、分棟の登記と分割の登記は一の申請情報でできる」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「分棟は表題部の変更。分割とは一の申請情報にできる」 with a yellow highlighter marker.
- Line 2: 「問題D0573・D0574・D0575・D1983　正解×・×・〇・×（H22-Q13ウ・エ・オ／R06-Q16エ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 号, 建, 所, 押, 権, 物, 登, 解, 記, 請, 違, 録 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the left comparison card has only a red cross and the right card only a blue check mark; confirm that the word 「まとめて」 is spelled exactly like this everywhere (never 「まとかて」); confirm that the conversation column has exactly 2 face icons and exactly 2 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panel 1 and panel 2 contain no check mark and no cross anywhere, that panel 3 has exactly one red cross (on the top-left card) and exactly one blue check mark (on the bottom-left card), and that the only other blue check marks in the whole image are the three in the checklist of panel 4; confirm that the table of panel 1 has exactly four body rows in the order 申請の組み立て, 登録免許税, 別個の建物にする, 2棟とも主である建物; confirm that the left card of panel 2 has the heading 「分棟の登記」 and the right card has the heading 「分割の登記」, never swapped confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不登法編6章_4コマ4_分棟は表題部の変更で、分割と一括できる.png`
- 途中の版・不採用の版：`不登法編6章_4コマ4_分棟は表題部の変更で、分割と一括できる_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch6/prompt_4koma_PF1-4_01_bunmune.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で4つの問い（申請の組み立て・課税・分割との一括）、コマ2で分棟の登記と分割の登記の違い、コマ3で分棟の押さえどころ4つが言える
- [ ] 工程C：構成表の全文言を記事（H22-Q13ウ・エ・オ、R06-Q16エ）・法令DBと突き合わせ済み。分割の登記の課税は記事にないので入れていない
- [ ] 工程C：コマ1・2に印がなく、コマ3の左は上＝✕・下＝✓の1個ずつ、コマ4だけ青✓。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない
- [ ] 工程C：肝の確認：①分棟の登記は表題部の変更の登記 ②抹消＋表題登記を一の申請情報でする決まりはない ③表示に関する登記なので登録免許税はかからない ④別個の建物にするなら分棟の登記と分割の登記は一の申請情報にできる ⑤D0573・D0574・D1983は×、D0575は〇

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

## 改訂履歴（このファイルは `src/spec_4koma_PF1-4_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-13 v01：新規作成（総合記事②不動産登記法編 第6章【PF1-4】【PF1-6】用。型4（4肢の比較表）＋型5（整理カード）。分棟は表題部の変更の登記という1つの理解から、抹消＋表題登記の組ではない・課税なし・分割と一括できるを導く構成にした）
