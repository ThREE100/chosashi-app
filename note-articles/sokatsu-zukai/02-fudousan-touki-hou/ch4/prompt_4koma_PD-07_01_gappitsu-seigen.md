# D1153・D1752・D0749 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②不動産登記法編 第4章「土地の分筆・合筆・地積更正」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch4.md`）の、論点【PD-7】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PD-07_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D1153・D1752・D0749（不動産登記法／土地の分筆・合筆・地積更正、出典 H28-Q10ウ／R04-Q09ア／H24-Q08エ）。正解＝D1153＝×（誤った記述）／D1752＝〇（正しい記述）／D0749＝×（誤った記述）。
- 記事：`note-articles/h28-mondai/q10-gappitsu.md` ウ（保安林であることは、法41条の制限事由にない。指定の解除を待たずに合筆できる）。ほか、R04-Q09ア（r4-mondai/q09-gappitsu.md。使用貸借権は登記できない権利なので、法41条6号の「所有権以外の権利に関する登記がある土地」に当たらない）、H24-Q08エ（h24-mondai/q08-gappitsu.md。表題登記のみの土地と所有権の登記がある土地は、名義人が同じでも法41条5号により合筆できない）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】D1153は『保安林としての指定が解除されない限り』と、解除という具体的な手続まで書いて、保安林の指定が制限事由であるかのように見せる。D1752は『第三者に使用貸借されている』と、権利が付いている土地に見せる（前提に『所有権の登記名義人が同一』『他の制限事由は考慮しない』とある）。D0749は『同じ者が表題部所有者／所有権の登記名義人』と名義人の一致だけを並べ、所有権の登記の有無の違いを見落とさせる。
- 【受験者の勘違い・定着していない点】（推測）①特別な指定（保安林）や、土地を貸していることがあれば、合筆の制限になるはずだと考える（D1153・D1752）。②使用貸借も権利だから、『所有権以外の権利に関する登記』に当たると考える。使用貸借は登記できない権利で、登記がないことが決め手（D1752）。③名義人が同じなら合筆できると考え、所有権の登記がない土地とある土地は合筆できない（法41条5号）ことが結びついていない（D0749）。
- 【対比する制度】「条文に挙がる事由」⇔「条文にない事情」：所有権の登記がない土地と所有権の登記がある土地の合筆は法41条5号に挙がる事由で、名義人が同じでも合筆できない／保安林の指定や登記できない使用貸借は法41条のどの号にも当たらない事情で、あっても合筆できる（結論が逆になる点）。
- 【型の選び方】型：型4（複数肢の対比。＋型3の理由説明）。理由：3つの肢は共通の日付のない別々の場面なので、コマ1は『肢／場面／肢の言い分』の比較表にした。コマ2は『条文に挙がる事由』と『条文にない事情』の左右の対比。コマ3は、なぜ制限になる・ならないが分かれるかの理由を3枚のカード（印なし）で示し、右に藍子の罠の語（使用貸借・名義人が同じ）と、トリ先生の指摘の会話を置いた。壁＝『目立つ事情があれば制限になるはず、名義人が同じなら足りるはず』。法41条の6つの号の一覧は、図解8とD0940の4コマ（型5）にあるので、この4コマには入れない。
- コマごとに読者が言えること：コマ1＝保安林・使用貸借・所有権の登記の有無の3つの場面と、肢の言い分。コマ2＝制限になるのは条文に挙がる事由（5号）だけで、保安林の指定と登記できない使用貸借は条文にない事情。コマ3＝保安林は条文に挙がらない／使用貸借は登記できず6号に当たらない／所有権の登記がない土地とある土地は5号で不可、の理由。コマ4＝D1153は×、D1752は〇、D0749は×。
- 記事の範囲：H28-Q10ウ（保安林であること自体は、法41条の制限事由に含まれない）、R04-Q09ア（使用貸借権は登記できない権利なので、乙土地は『所有権以外の権利に関する登記がある土地』に当たらず、合筆できる）、H24-Q08エ（法41条5号：所有権の登記がある土地とない土地は合筆できない。名義人が同じでも、権利部の状態が異なる）。
- 対象外にした肢：D1946（現況の地目が違う場合）は、記事が『現況の扱いは実務の取扱いによる整理』とするため、条文だけで説明できるこの4コマには入れず、図解8で扱う。D1753（敷地権である旨の登記）は【PD-8】の既存の4コマ。
- extra_refs：不動産登記法41条（一 相互に接続していない土地 二 地目又は地番区域が相互に異なる土地 三 表題部所有者又は所有権の登記名義人が相互に異なる土地 四 持分を相互に異にする土地 五 所有権の登記がない土地と所有権の登記がある土地 六 所有権の登記以外の権利に関する登記がある土地）は、法令DB note-articles/laws/fudousan-touki-hou.md 第41条で原文を確認した。図に入れるのは5号と6号だけ。保安林が条文にないことは、41条の各号に保安林がないことの確認による（記事もその書き方）。
- 登場人物：人型は使わず、土地は文字のカードで示す（A・Bの文字は使わない。名義人は『同じ者』と書く）。
- 矢印の意味：矢印は使わない。コマ1は表、コマ2は左右のカード、コマ3は左の縦3枚のカードと右の会話。
- 配色：コマ1〜3は印（✓✕）を付けない。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝small（3列の表が横いっぱいに要るので、キャラは小さく）、コマ2＝none（図が主役）、コマ3＝faces（左に縦3枚のカード、右に会話4つの縦並び）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 条文にない事情は、合筆の制限にならない | 「条文にない事情」を黄色マーカー |
| コマ1 見出し | ラベル | ①　3つの肢を並べる | — |
| コマ1 図 | 図・カード | 肢 / 場面 / 肢の言い分 / 肢D1153 / 甲・乙の地目が、いずれも保安林 / 指定が解除されないと、合筆できない / 肢D1752 / 乙土地が、第三者に使用貸借されている / 使用貸借があっても、合筆できる / 肢D0749 / 甲は表題登記のみ。乙には同じ者の所有権の登記 / 名義人が同じなら、合筆できる / 合筆できない / 合筆できる / 合筆の登記を申請できる？ | — |
| コマ1 | 藍子（左・先に話す） | 保安林や貸地なら、制限ですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。条文に挙がるかを見なさい | 「条文に挙がるか」 |
| コマ2 見出し | ラベル | ②　挙がる事由と、挙がらない事情 | — |
| コマ2 図 | 図・カード | 合筆の制限 / 分かれ目は、条文に挙がるかどうか / 条文に挙がる事由 / 法41条5号 / 所有権の登記がない土地と、ある土地 / 名義人が同じでも、合筆できない / 条文にない事情 / 法41条のどの号にもない / 保安林の指定、登記できない使用貸借 / あっても、合筆できる / 合筆できる | — |
| コマ3 見出し | ラベル | ③　なぜ、そう分かれる？ | — |
| コマ3 図 | 図・カード | 保安林が制限にならない理由 / 保安林の指定は、法41条の事由に挙がっていない / 使用貸借が制限にならない理由 / 登記できないので、法41条6号の登記がある土地に当たらない / 名義人が同じでも不可の理由 / 所有権の登記がない土地とある土地は、法41条5号で合筆できない | — |
| コマ3 | 藍子（左・1番目） | 使用貸借も、権利ですよね？ | — |
| コマ3 | トリ先生（右・2番目） | 登記できない権利は、6号に当たらないのよ | 「6号に当たらない」 |
| コマ3 | 藍子（左・3番目） | 名義人が同じなら、足りますよね？ | — |
| コマ3 | トリ先生（右・4番目） | 登記の有無も見なさい。それが罠よ | 「登記の有無」 |
| コマ4 見出し | ラベル | ④　結論は×と〇と× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 条文に挙がるかを見ればいいんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。挙がらない事情は気にしないのよ | 「気にしない」 |
| コマ4 チェック欄 | 3項目（青✓） | 保安林の指定は法41条に挙がらず、解除を待たずに合筆できる（肢D1153は×） / 登記できない使用貸借は6号に当たらず、合筆できる（肢D1752は〇） / 所有権の登記がない土地とある土地は、名義人が同じでも合筆できない（肢D0749は×） | — |
| 結論帯 | 1行目 | 保安林・使用貸借は制限でない。登記の有無は制限 | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1153・D1752・D0749　正解×・〇・×（H28-Q10ウ／R04-Q09ア／H24-Q08エ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記法41条5号・6号（法令DB note-articles/laws/fudousan-touki-hou.md 第41条）：五 所有権の登記がない土地と所有権の登記がある土地との合筆の登記、六 所有権の登記以外の権利に関する登記がある土地（法務省令で定めるものがある土地を除く。）の合筆の登記。1号〜4号は図に入れない。保安林は41条の各号にない

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

TITLE BANNER: text 「条文にない事情は、合筆の制限にならない」 in large bold letters; the part 「条文にない事情」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear SMALLER than in the other panels, only because this panel's diagram or text needs the room (each about 150 px tall; never below 110 px and never more than one third of the panel height; use the largest size in this range that still lets the diagram fill the panel), 藍子 at the lower left corner and トリ先生 at the lower right corner; 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　3つの肢を並べる」
- A wide table that fills the full panel width. The header row is dark navy with white text and has three columns: 「肢」, 「場面」, 「肢の言い分」. The three body rows have the same pale gray fill and a dark navy outline, each text at least 24 px high, with no check mark, no cross, and no arrow.
- Body row 1: 「肢D1153」, 「甲・乙の地目が、いずれも保安林」, 「指定が解除されないと、合筆できない」.
- Body row 2: 「肢D1752」, 「乙土地が、第三者に使用貸借されている」, 「使用貸借があっても、合筆できる」.
- Body row 3: 「肢D0749」, 「甲は表題登記のみ。乙には同じ者の所有権の登記」, 「名義人が同じなら、合筆できる」.
- In the third column, row 1 says that the plots CANNOT be merged (「合筆できない」) while rows 2 and 3 say that they CAN (「合筆できる」); copy each exactly as given and do not change one into the other.
- A small question badge 「合筆の登記を申請できる？」 with a pale gray fill and a dark navy outline sits at the upper right of the table (a question badge only, with no check mark and no cross).
- 藍子 bubble (left, spoken first): 「保安林や貸地なら、
制限ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
条文に挙がるかを
見なさい」 with the part 「条文に挙がるか」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　挙がる事由と、挙がらない事情」
- A small dark navy tag 「合筆の制限」 at the top left, with one line beside it: 「分かれ目は、条文に挙がるかどうか」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「条文に挙がる事由」, a small tag 「法41条5号」, two body lines: 「所有権の登記がない土地と、ある土地」, 「名義人が同じでも、合筆できない」.
- Right card, heading 「条文にない事情」, a small tag 「法41条のどの号にもない」, two body lines: 「保安林の指定、登記できない使用貸借」, 「あっても、合筆できる」, with the text 「合筆できる」 highlighted with a yellow marker.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ、そう分かれる？」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- LEFT SIDE: three stacked reason cards of the same size, from top to bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card and one or two short body lines, with no arrow, no connector, no check mark, and no cross. The cards are separated only by a small empty gap.
- Card 1, heading 「保安林が制限にならない理由」, body 「保安林の指定は、法41条の事由に挙がっていない」.
- Card 2, heading 「使用貸借が制限にならない理由」, body 「登記できないので、法41条6号の登記がある土地に当たらない」.
- Card 3, heading 「名義人が同じでも不可の理由」, body 「所有権の登記がない土地とある土地は、法41条5号で合筆できない」.
- The three cards have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「使用貸借も、
権利ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「登記できない権利は、
6号に当たらない
のよ」 with the part 「6号に当たらない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「名義人が同じなら、
足りますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「登記の有無も
見なさい。
それが罠よ」 with the part 「登記の有無」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は×と〇と×」
- 藍子 bubble (left, spoken first): 「条文に挙がるかを
見ればいいんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。挙がらない
事情は気にしない
のよ」 with the part 「気にしない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「保安林の指定は法41条に挙がらず、解除を待たずに合筆できる（肢D1153は×）」, 「登記できない使用貸借は6号に当たらず、合筆できる（肢D1752は〇）」, 「所有権の登記がない土地とある土地は、名義人が同じでも合筆できない（肢D0749は×）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「保安林・使用貸借は制限でない。登記の有無は制限」 with a yellow highlighter marker.
- Line 2: 「問題D1153・D1752・D0749　正解×・〇・×（H28-Q10ウ／R04-Q09ア／H24-Q08エ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 保, 号, 地, 当, 所, 権, 無, 登, 肢, 解, 記, 請 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the word 「第三者」 is spelled exactly like this everywhere (never 「時三者」); confirm that the smaller characters are drawn within the specified size range (they must not grow and squeeze the diagram, and must not be shrunk below the range) and that nothing but the given text appears above the heads of the pictograms; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不動産登記法編4章_4コマ3_条文にない事情は、合筆の制限にならない.png`
- 途中の版・不採用の版：`不動産登記法編4章_4コマ3_条文にない事情は、合筆の制限にならない_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch4/prompt_4koma_PD-07_01_gappitsu-seigen.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1の表で3つの肢の場面と言い分が言え、コマ2で制限になる事由とならない事情の対比、コマ3でその理由が言える
- [ ] 工程C：構成表の全文言を記事（H28-Q10ウ、R04-Q09ア、H24-Q08エ）・法令DB（法41条）と突き合わせ済み。『実務の取扱い』とされる現況の地目（D1946）と敷地権である旨の登記（D1753）は入れていない
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方は small→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはコマ1だけ（表が横いっぱいに要るため）
- [ ] 工程C：肝の確認：①合筆の制限になるのは法41条に挙がる事由だけ ②保安林の指定は挙がっていない（肢D1153は×） ③使用貸借は登記できず、6号の登記がある土地に当たらない（肢D1752は〇） ④所有権の登記がない土地とある土地は、名義人が同じでも5号で不可（肢D0749は×）

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

## 改訂履歴（このファイルは `src/spec_4koma_PD-07_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-13 v01：新規作成（総合記事②不動産登記法編 第4章【PD-7】用。型4の複数肢の対比＋型3の理由説明。制限にならない事情〔保安林・登記できない使用貸借〕と、制限になる事由〔法41条5号〕の対比に絞った。D1946〔現況の地目〕は実務の取扱いを含むため図解8で扱う）
