# D1242・D1246・D1639 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②「直前期の苦手論点つぶし 不動産登記法編」第2章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch2.md`）の、論点【PB-5】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PB-05_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D1242・D1246・D1639（不動産登記法／申請総論（申請情報・添付情報・代理・却下取下・還付・電子申請・登記識別情報）、出典 H29-Q08ア・オ／R03-Q05オ）。正解＝D1242＝〇（正しい記述）／D1246＝×（誤った記述）／D1639＝×（誤った記述）。
- 記事：`note-articles/h29-mondai/q08-denshi-shinsei.md` ア（H29：申請情報には、申請人等が電子署名を行う。令12条1項）・オ（H29：スキャンした書面でも、登記官が定めた相当の期間内に原本を提示しなければならない。令13条2項）。ほか、R03-Q05オ（r3-mondai/q05-tenpu-jouhou.md。登記事項証明書の提供に代えて送信するのは、登記情報の送信を受けるために必要な情報〔実務では照会番号など〕であって、不動産番号ではない。令11条、令6条）。章の記事 note-articles/column/sokatsu-02-fudousan-touki-hou-ch2.md 【PB-5】
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】3肢とも電子申請の場面で、言い分の向きが揃わない。D1242は『電子署名を行わなければならない』と正しい約束事をそのまま問い（〇）、D1246は『当該書面を登記官に提示する必要はない』と、スキャンしたことで原本の提示が要らなくなったように見せる（×）。D1639は『不動産番号を送信しなければならない』と、令6条の不動産番号を令11条の登記事項証明書の代わりに入れ替える（×）。
- 【受験者の勘違い・定着していない点】（推測）①電子申請は紙をやめる制度だから、スキャンして送った時点で書面はもう見せなくてよいと広げて考える（令13条2項は、相当の期間内に登記官へ書面を提示すると定める）。②登記事項証明書の代わりには、不動産番号を送ればよいと考える（令11条が定めるのは登記情報の送信を受けるために必要な情報で、不動産番号は令6条の別の制度）。③電子申請は紙の押印がなくなる分、申請情報の署名も要らないように感じる（令12条1項で申請人等の電子署名が必要）。
- 【対比する制度】「電子でも省けない」⇔「電子で代えられる」：申請情報への電子署名（令12条1項）と、スキャンした書面のあとの原本提示（令13条2項）は、電子申請でも省けない／登記事項証明書の提供は、登記情報の送信を受けるために必要な情報（実務では照会番号など）で代えられるが、不動産番号は代わりにならない（令11条と令6条。結論が逆になる点）。
- 【型の選び方】型：型4（複数肢の対比。コマ1は比較表）に型5（整理カード併用）を組み合わせる。理由：3肢は電子申請の別々の場面（申請情報／スキャンした書面／登記事項証明書）で共通の日付がなく、言い分の向きも揃わず、読者は『電子で済むもの』と『電子でも要るもの』を自分で並べ直せない。コマ1＝3肢の比較表（肢／電子申請で扱うもの／肢の言い分）、コマ2＝『電子でも省けない』と『電子で代えられる』の左右のカード、コマ3＝左は肢の言い分（✕）と正しい整理（✓）の上下カード、右は会話1往復と、不動産番号と証明書の代わりの整理カード、コマ4＝〇・×・×の整理。壁＝『電子申請なら書面も番号も全部オンラインで足りる』という思い込み。
- コマごとに読者が言えること：コマ1＝3肢は、扱うもの（申請情報・スキャンした書面・登記事項証明書）と言い分が違う。コマ2＝署名と原本の提示は電子でも省けず、証明書は情報で代えられるが不動産番号ではない。コマ3＝スキャンしても原本は提示する。不動産番号は申請情報の省略用で、証明書の代わりは登記情報の送信を受けるための情報。コマ4＝D1242は〇、D1246とD1639は×。
- 記事の範囲：H29-Q08ア・オ、R03-Q05オ（記事 note-articles/h29-mondai/q08-denshi-shinsei.md、note-articles/r3-mondai/q05-tenpu-jouhou.md）と、総合記事第2章【PB-5】。条文の文言は法令DB（note-articles/laws/fudousan-touki-rei.md）の令6条・11条・12条・13条で確認した。『照会番号など』は条文に書かれておらず、令11条の『必要な情報』の実務上の中身（登記情報提供サービスの照会番号等）なので、図には『実務では』と添えて断定を避けた。令13条1項の対象（申請人等が作成した書面と各種図面を除く）と調査士報告方式の特例（D0586・D1633は既存の4コマ）は、この図に入れない。
- extra_refs：不動産登記令12条1項（申請情報への電子署名）・13条2項（スキャンした書面を登記官が定めた相当の期間内に提示）・11条（登記事項証明書の提供に代えて、登記情報の送信を受けるために必要な情報を送信）・6条（申請情報の一部の省略。不動産番号）は、法令DBで原文を確認した。なお、問題バンクのD1246の根拠欄は『不動産登記規則（原本の提示が必要）』と書かれているが、提示を定めるのは法令DBの令13条2項で、図には令13条2項を記載した。
- 登場人物：人型は使わず、申請情報・書面・番号は文字のカードで示す。
- 矢印の意味：矢印は使わない。コマ1は表、コマ2は左右のカード、コマ3は上下のカードと整理カード。
- 配色：コマ1・2は印（✓✕）を付けない。コマ3の左は上＝✕、下＝✓の1個ずつ。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、帯・リボンは濃紺（白文字）、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝small（表が横いっぱいに要るので、キャラは小さく。約150px）、コマ2＝none（図が主役）、コマ3＝faces（左に上下2枚のカード、右に会話2つと整理カード）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 電子でも、署名と原本は省けない | 「署名と原本」を黄色マーカー |
| コマ1 見出し | ラベル | ①　3つの肢は、電子申請で扱うものが違う | — |
| コマ1 図 | 図・カード | 肢 / 電子申請で扱うもの / 肢の言い分 / 肢D1242 / 申請情報 / 申請人等は、電子署名を行わなければならない / 肢D1246 / スキャンした書面 / 書面を登記官に提示する必要はない / 肢D1639 / 登記事項証明書 / 代えて、不動産番号を送信しなければならない | — |
| コマ1 | 藍子（左・先に話す） | 電子申請なら、全部ネットで済みますよね？ | — |
| コマ1 | トリ先生（右・答える） | そこが罠。署名も原本も番号も別々よ | 「別々」 |
| コマ2 見出し | ラベル | ②　電子でも省けないものと、電子で代えられるもの | — |
| コマ2 図 | 図・カード | 電子申請の約束事 / 扱うもので、電子で済むかが分かれる / 電子でも省けない / 令12条1項・13条2項 / 申請情報への電子署名 / スキャンした書面の、あとの原本の提示 / 肢D1242・肢D1246は、こちらの場面 / 電子で代えられる / 令11条 / 登記事項証明書は、送信する情報で代える / 不動産番号は、代わりにならない / 肢D1639は、こちらの場面 / 署名と原本の提示は、電子でも省けない | — |
| コマ3 見出し | ラベル | ③　スキャンしても、原本は見せる | — |
| コマ3 図 | 図・カード | スキャンすれば、提示は不要 / 肢D1246の言い分 / スキャンしても、原本を提示 / 登記官が定めた相当の期間内に（令13条2項） / 不動産番号と証明書の代わり / 令6条：不動産番号は、申請情報の省略用 / 令11条：証明書の代わりは、送信を受ける情報 / 実務では、照会番号など / 不動産番号は、証明書の代わりにならない / 肢D1639は、不動産番号を送る言い分 | — |
| コマ3 | 藍子（左・1番目） | 不動産番号を送れば、証明書の代わりですよね？ | — |
| コマ3 | トリ先生（右・2番目） | 役割が別なの。送るのは照会番号等よ | 「照会番号等」 |
| コマ4 見出し | ラベル | ④　結論は〇と×と× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 署名も原本も、電子申請でも必要なんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。証明書の代わりは番号じゃないわよ | 「番号じゃない」 |
| コマ4 チェック欄 | 3項目（青✓） | 電子申請では、申請情報に電子署名をする（肢D1242は〇） / スキャンした書面も、あとで原本を提示する（肢D1246は×） / 証明書の代わりは照会番号等で、不動産番号ではない（肢D1639は×） | — |
| 結論帯 | 1行目 | 電子申請でも、署名と原本の提示は省けない | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1242・D1246・D1639　正解〇・×・×（H29-Q08ア・オ／R03-Q05オ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記令12条1項（申請人又はその代表者若しくは代理人は、申請情報に電子署名を行わなければならない）・13条2項（申請人は、登記官が定めた相当の期間内に、登記官に書面を提示しなければならない）・11条（登記事項証明書の提供に代えて、登記情報の送信を受けるために必要な情報を送信）・6条（申請情報の一部の省略）。法令DB note-articles/laws/fudousan-touki-rei.md と照合済み。『照会番号』は条文にない実務上の呼び方

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

TITLE BANNER: text 「電子でも、署名と原本は省けない」 in large bold letters; the part 「署名と原本」 has a yellow highlighter marker.

PANEL 1 (curious, puzzled mood; both characters appear SMALLER than in the other panels, only because this panel's diagram or text needs the room (each about 150 px tall; never below 110 px and never more than one third of the panel height; use the largest size in this range that still lets the diagram fill the panel), 藍子 at the lower left corner and トリ先生 at the lower right corner; 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　3つの肢は、電子申請で扱うものが違う」
- A wide table that fills the full panel width. The header row is dark navy with white text and has three columns: 「肢」, 「電子申請で扱うもの」, 「肢の言い分」. The three body rows have the same pale gray fill and a dark navy outline, each text at least 24 px high, with no check mark, no cross, and no arrow.
- Body row 1: 「肢D1242」, 「申請情報」, 「申請人等は、電子署名を行わなければならない」.
- Body row 2: 「肢D1246」, 「スキャンした書面」, 「書面を登記官に提示する必要はない」.
- Body row 3: 「肢D1639」, 「登記事項証明書」, 「代えて、不動産番号を送信しなければならない」.
- The three rows have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- 藍子 bubble (left, spoken first): 「電子申請なら、
全部ネットで
済みますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そこが罠。
署名も原本も番号も
別々よ」 with the part 「別々」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　電子でも省けないものと、電子で代えられるもの」
- A small dark navy tag 「電子申請の約束事」 at the top left, with one line beside it: 「扱うもので、電子で済むかが分かれる」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「電子でも省けない」, a small tag 「令12条1項・13条2項」, two body lines: 「申請情報への電子署名」, 「スキャンした書面の、あとの原本の提示」, and a small dark navy tag 「肢D1242・肢D1246は、こちらの場面」.
- Right card, heading 「電子で代えられる」, a small tag 「令11条」, two body lines: 「登記事項証明書は、送信する情報で代える」, 「不動産番号は、代わりにならない」, and a small dark navy tag 「肢D1639は、こちらの場面」.
- Under the two cards, one wide dark navy band with large white text 「署名と原本の提示は、電子でも省けない」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　スキャンしても、原本は見せる」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 2 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 120 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 2 face icons and exactly 2 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.
- LEFT SIDE: two stacked cards of the same size, top and bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card, with no arrow and no connector. The cards are separated only by a small empty gap.
- Top card, heading 「スキャンすれば、提示は不要」, body 「肢D1246の言い分」, and ONE red cross only at the bottom of this card (no check mark on this card).
- Bottom card, heading 「スキャンしても、原本を提示」, body 「登記官が定めた相当の期間内に（令13条2項）」, and ONE blue check mark only at the bottom of this card (no cross on this card).
- RIGHT SIDE, under the two speech bubbles (the two speech bubbles and their two faces stay at the top of the right side): one tall list card with a dark navy heading 「不動産番号と証明書の代わり」, with the same pale gray fill and a dark navy outline, containing exactly four short rows, each with a small dark navy dot at its left end (NO digit and NO letter on the dots), with no arrow and no check mark and no cross: 「令6条：不動産番号は、申請情報の省略用」, 「令11条：証明書の代わりは、送信を受ける情報」, 「実務では、照会番号など」, 「不動産番号は、証明書の代わりにならない」, with the second and third rows highlighted with a yellow marker. Under the four rows, one small dark navy ribbon tag with white text 「肢D1639は、不動産番号を送る言い分」.
- The list card is a part of the right side, and it is NOT a speech bubble. The left cards and the list card have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 2 in the conversation column; face icon at the LEFT end of its own row): 「不動産番号を
送れば、証明書の
代わりですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 2 in the conversation column; face icon at the RIGHT end of its own row): 「役割が別なの。
送るのは
照会番号等よ」 with the part 「照会番号等」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇と×と×」
- 藍子 bubble (left, spoken first): 「署名も原本も、
電子申請でも
必要なんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
証明書の代わりは
番号じゃないわよ」 with the part 「番号じゃない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「電子申請では、申請情報に電子署名をする（肢D1242は〇）」, 「スキャンした書面も、あとで原本を提示する（肢D1246は×）」, 「証明書の代わりは照会番号等で、不動産番号ではない（肢D1639は×）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「電子申請でも、署名と原本の提示は省けない」 with a yellow highlighter marker.
- Line 2: 「問題D1242・D1246・D1639　正解〇・×・×（H29-Q08ア・オ／R03-Q05オ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 代, 号, 当, 番, 登, 肢, 解, 記, 証, 請, 違, 間 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the left comparison card has only a red cross and the right card only a blue check mark; confirm that the smaller characters are drawn within the specified size range (they must not grow and squeeze the diagram, and must not be shrunk below the range) and that nothing but the given text appears above the heads of the pictograms; confirm that the conversation column has exactly 2 face icons and exactly 2 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panel 1 and panel 2 contain no check mark and no cross anywhere, that panel 3 has exactly one red cross (on the top-left card) and exactly one blue check mark (on the bottom-left card) and no other mark, and that the only blue check marks outside panel 3 are the three in the checklist of panel 4; confirm that the table in panel 1 has exactly three body rows, 「肢D1242」 first, 「肢D1246」 second and 「肢D1639」 third, never reordered; confirm that the left card of panel 2 has the heading 「電子でも省けない」 with the tag 「肢D1242・肢D1246は、こちらの場面」 and the right card has the heading 「電子で代えられる」 with the tag 「肢D1639は、こちらの場面」, never swapped confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不動産登記法編2章_4コマ5_電子でも、署名と原本は省けない.png`
- 途中の版・不採用の版：`不動産登記法編2章_4コマ5_電子でも、署名と原本は省けない_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch2/prompt_4koma_PB-05_01_denshi-shomei-genpon.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で3肢が扱うものと言い分の違い、コマ2で電子でも省けないもの（署名・原本の提示）と電子で代えられるもの（証明書）、コマ3でスキャンしても原本は提示することと不動産番号が証明書の代わりにならないことが言える
- [ ] 工程C：構成表の全文言を記事（H29-Q08ア・オ、R03-Q05オ）・総合記事【PB-5】・法令DB（令6条・11条・12条・13条）と突き合わせ済み。『照会番号など』には『実務では』の注記を入れた
- [ ] 工程C：コマ1・2に印がなく、コマ3の左は上＝✕・下＝✓の1個ずつ、コマ4だけ青✓。コマの使い方は small→none→faces→既定 で隣り合うコマが同じにならない
- [ ] 工程C：肝の確認：①申請情報には申請人等が電子署名をする（令12条1項） ②スキャンした書面でも、相当の期間内に原本を登記官に提示する（令13条2項） ③登記事項証明書の代わりは登記情報の送信を受けるための情報で、不動産番号は令6条の別の制度 ④D1242は〇、D1246・D1639は×

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

## 改訂履歴（このファイルは `src/spec_4koma_PB-05_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-14 v01：新規作成（総合記事②不動産登記法編 第2章【PB-5】用。型4（複数肢の対比。コマ1は比較表）に型5（整理カード併用）を組み合わせた。電子申請の署名・スキャンした書面の原本の提示・登記事項証明書の代わり（不動産番号との区別）を、『電子でも省けない』と『電子で代えられる』で整理した。照会番号は実務上の呼び方と注記した）
