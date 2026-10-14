# D0577・D0770 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②「直前期の苦手論点つぶし 不動産登記法編」第2章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch2.md`）の、論点【PB-3】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PB-03_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D0577・D0770（不動産登記法／建物の表示（添付情報）、出典 H22-Q14イ／H24-Q12オ）。正解＝D0577＝×（誤った記述）／D0770＝×（誤った記述）。
- 記事：`note-articles/h22-mondai/q14-tatemono-tenpu.md` イ（H22：管轄区域外の敷地の土地は、不動産番号だけでは登記事項証明書を省略できない。令別表12の項添付情報欄ヘ（3）・令6条）。ほか、H24-Q12オ（h24-mondai/q12-tatemono-tenpu.md。敷地権の発生による建物の表題部の変更の登記は、他の登記所の管轄区域内の土地に限って登記事項証明書を提供する。令別表15の項添付情報欄ホ（2））
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】2肢とも×だが、外し方が逆である。D0577は『不動産番号を提供すれば、登記事項証明書を提供する必要はない』と、番号による省略（令6条）という別の制度を持ち込んで、管轄区域外の土地の証明書まで省けると思わせる。D0770は『管轄区域内にあるときであっても…提供しなければならない』と、『他の登記所の管轄区域内にあるとき』という限定を落として、常に要ると言い切る。
- 【受験者の勘違い・定着していない点】（推測）①不動産番号は何でも省略できる番号だと考える（実際は申請情報の一部の省略用で、添付情報の登記事項証明書の代わりにならない）。②敷地権に関わる登記なら、土地の登記事項証明書は常に要ると考える。③令別表12の項と15の項に共通する『他の登記所の管轄区域内にあるとき』という限定を読み落とす。
- 【対比する制度】「他の登記所の管轄区域内にある土地」⇔「同じ登記所の管轄区域内にある土地」：敷地権の目的である土地が他の登記所の管轄区域内にあるときは、その土地の登記事項証明書を提供する（令別表12の項ヘ（3）・15の項ホ（2））／同じ登記所の管轄区域内にある土地なら、登記事項証明書は要らない（結論が逆になる点）。
- 【型の選び方】型：型4（複数肢の対比。コマ1は比較表）。理由：2肢は別々の登記（区分建物の表題登記と、敷地権の発生による変更の登記）で共通の日付がなく、どちらも×だが外し方が逆で、読者は自分で並べ直せない。コマ1＝2肢の比較表（肢／登記と土地／肢の言い分）、コマ2＝分かれ目の左右のカード、コマ3＝不動産番号と登記事項証明書の役割の違いを理由のカード3枚で、コマ4＝2肢とも×の整理。壁＝『番号を出せば省ける』と『常に要る』の両極。
- コマごとに読者が言えること：コマ1＝2肢は、土地の所在（管轄区域外／同じ管轄区域内）と肢の言い分が違う。コマ2＝要るのは、他の登記所の管轄区域内にある土地だけ。コマ3＝不動産番号は申請情報の省略用で、登記事項証明書の代わりにならない。同じ管轄なら要らない。コマ4＝D0577もD0770も×。
- 記事の範囲：H22-Q14イ（令別表12の項添付情報欄ヘ（3）、令6条）、H24-Q12オ（令別表15の項添付情報欄ホ（2））。2つの項が同じ『他の登記所の管轄区域内にあるとき』の限定を置いていることは、令別表の原文（note-articles/laws/fudousan-touki-rei-betsuhyou.md）で確認した。
- extra_refs：令別表12の項添付情報欄ヘ（3）『敷地権の目的である土地が他の登記所の管轄区域内にあるときは、当該土地の登記事項証明書』、令別表15の項添付情報欄ホ（2）『敷地権の目的である土地が他の登記所の管轄区域内にあるときは、当該土地の登記事項証明書』（ホは『イ及びニの場合』の限定つき）、令6条（不動産識別事項を申請情報の内容としたときは、申請情報の一部を省略できる）は、法令DBで原文を確認した。
- 登場人物：人型は使わず、登記所・土地は文字のカードで示す。
- 矢印の意味：矢印は使わない。コマ1は表、コマ2は左右のカード、コマ3は縦3枚のカード。
- 配色：コマ1〜3は印（✓✕）を付けない。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、帯・リボンは濃紺（白文字）、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝small（表が横いっぱいに要るので、キャラは小さく。約150px）、コマ2＝none（図が主役）、コマ3＝faces（左に理由のカード3枚、右に会話4つの縦並び）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 敷地の証明書は、管轄外の土地だけ | 「管轄外の土地だけ」を黄色マーカー |
| コマ1 見出し | ラベル | ①　2つの肢は、土地の所在が違う | — |
| コマ1 図 | 図・カード | 肢 / 登記と敷地の土地 / 肢の言い分 / 肢D0577 / 区分建物の表題登記。敷地の土地は、管轄区域外 / 不動産番号を提供すれば、土地の登記事項証明書は要らない / 肢D0770 / 敷地権の発生による変更の登記。敷地の土地は、同じ管轄区域内 / それでも、土地の登記事項証明書を提供しなければならない | — |
| コマ1 | 藍子（左・先に話す） | 番号を出せば、証明書は省けますよね？ | — |
| コマ1 | トリ先生（右・答える） | どちらの肢も×よ。外し方が逆なの | 「外し方が逆」 |
| コマ2 見出し | ラベル | ②　要るのは、管轄外の土地だけ | — |
| コマ2 図 | 図・カード | 敷地権の目的である土地 / 土地の所在で、結論が分かれる / 他の登記所の管轄区域内にある土地 / その土地の登記事項証明書を提供する / 不動産番号では、省けない / 肢D0577は、こちらの場面 / 同じ登記所の管轄区域内にある土地 / その土地の登記事項証明書は、要らない / 敷地権発生の変更の登記でも同じ / 肢D0770は、こちらの場面 / どちらの登記でも、要るのは左の場面だけ | — |
| コマ3 見出し | ラベル | ③　不動産番号は、証明書の代わりではない | — |
| コマ3 図 | 図・カード | 不動産番号は、申請情報の省略用 / 土地の所在・地番・地目・地積などを / 書かずに済む（令6条） / 登記事項証明書は、添付情報 / ひっかけ：番号を出せば、証明書も不要 / 管轄外の土地の状況を / 確かめるための書類 / 同じ管轄なら、要らない / 敷地権発生の変更の登記でも、 / 他の登記所の土地に限る | — |
| コマ3 | 藍子（左・1番目） | 番号を出せば、証明書は要りませんよね？ | — |
| コマ3 | トリ先生（右・2番目） | それが罠。番号は申請情報の省略用よ | 「それが罠」 |
| コマ3 | 藍子（左・3番目） | 同じ管轄なら、証明書は要りますか？ | — |
| コマ3 | トリ先生（右・4番目） | 要らないわ。管轄外の土地だけよ | 「管轄外の土地だけ」 |
| コマ4 見出し | ラベル | ④　結論は×と× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | どちらの肢も、×なんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。外し方が逆でも、×は×よ | 「×は×」 |
| コマ4 チェック欄 | 3項目（青✓） | 管轄区域外の敷地の土地は、登記事項証明書を提供する（令別表12の項） / 不動産番号は申請情報の省略用で、証明書の代わりにならない（令6条） / 敷地権発生の変更の登記は、他の登記所の土地に限る（令別表15の項） | — |
| 結論帯 | 1行目 | 登記事項証明書が要るのは、管轄外の敷地の土地だけ | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0577・D0770　正解×・×（H22-Q14イ／H24-Q12オ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記令別表12の項添付情報欄ヘ（3）・同15の項添付情報欄ホ（2）（敷地権の目的である土地が他の登記所の管轄区域内にあるときは、当該土地の登記事項証明書）、同6条（不動産識別事項を申請情報の内容としたとき、申請情報の一部を省略できる）。法令DB note-articles/laws/fudousan-touki-rei-betsuhyou.md・fudousan-touki-rei.md と照合済み

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

TITLE BANNER: text 「敷地の証明書は、管轄外の土地だけ」 in large bold letters; the part 「管轄外の土地だけ」 has a yellow highlighter marker.

PANEL 1 (curious, puzzled mood; both characters appear SMALLER than in the other panels, only because this panel's diagram or text needs the room (each about 150 px tall; never below 110 px and never more than one third of the panel height; use the largest size in this range that still lets the diagram fill the panel), 藍子 at the lower left corner and トリ先生 at the lower right corner; 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　2つの肢は、土地の所在が違う」
- A wide table that fills the full panel width. The header row is dark navy with white text and has three columns: 「肢」, 「登記と敷地の土地」, 「肢の言い分」. The two body rows have the same pale gray fill and a dark navy outline, each text at least 24 px high, with no check mark, no cross, and no arrow.
- Body row 1: 「肢D0577」, 「区分建物の表題登記。敷地の土地は、管轄区域外」, 「不動産番号を提供すれば、土地の登記事項証明書は要らない」.
- Body row 2: 「肢D0770」, 「敷地権の発生による変更の登記。敷地の土地は、同じ管轄区域内」, 「それでも、土地の登記事項証明書を提供しなければならない」.
- The two rows have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- 藍子 bubble (left, spoken first): 「番号を出せば、
証明書は省けます
よね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「どちらの肢も×よ。
外し方が逆なの」 with the part 「外し方が逆」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　要るのは、管轄外の土地だけ」
- A small dark navy tag 「敷地権の目的である土地」 at the top left, with one line beside it: 「土地の所在で、結論が分かれる」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「他の登記所の管轄区域内にある土地」, two body lines: 「その土地の登記事項証明書を提供する」, 「不動産番号では、省けない」, and a small dark navy tag 「肢D0577は、こちらの場面」.
- Right card, heading 「同じ登記所の管轄区域内にある土地」, two body lines: 「その土地の登記事項証明書は、要らない」, 「敷地権発生の変更の登記でも同じ」, and a small dark navy tag 「肢D0770は、こちらの場面」.
- Under the two cards, one wide dark navy band with large white text 「どちらの登記でも、要るのは左の場面だけ」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　不動産番号は、証明書の代わりではない」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, and a dark navy heading placed INSIDE the card, with no check mark and no cross. The cards are separated only by a small empty gap, with nothing drawn between them.
- Card 1, heading 「不動産番号は、申請情報の省略用」, two body lines 「土地の所在・地番・地目・地積などを」 and 「書かずに済む（令6条）」.
- Card 2, heading 「登記事項証明書は、添付情報」, a dark navy ribbon tag with large white text 「ひっかけ：番号を出せば、証明書も不要」, two body lines 「管轄外の土地の状況を」 and 「確かめるための書類」.
- Card 3, heading 「同じ管轄なら、要らない」, two body lines 「敷地権発生の変更の登記でも、」 and 「他の登記所の土地に限る」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「番号を出せば、
証明書は要り
ませんよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「それが罠。
番号は申請情報の
省略用よ」 with the part 「それが罠」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「同じ管轄なら、
証明書は
要りますか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「要らないわ。
管轄外の土地
だけよ」 with the part 「管轄外の土地だけ」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は×と×」
- 藍子 bubble (left, spoken first): 「どちらの肢も、
×なんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
外し方が逆でも、
×は×よ」 with the part 「×は×」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「管轄区域外の敷地の土地は、登記事項証明書を提供する（令別表12の項）」, 「不動産番号は申請情報の省略用で、証明書の代わりにならない（令6条）」, 「敷地権発生の変更の登記は、他の登記所の土地に限る（令別表15の項）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「登記事項証明書が要るのは、管轄外の敷地の土地だけ」 with a yellow highlighter marker.
- Line 2: 「問題D0577・D0770　正解×・×（H22-Q14イ／H24-Q12オ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 代, 号, 地, 建, 所, 権, 物, 番, 登, 肢, 解, 記, 証, 請, 違 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the smaller characters are drawn within the specified size range (they must not grow and squeeze the diagram, and must not be shrunk below the range) and that nothing but the given text appears above the heads of the pictograms; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panel 1, panel 2 and panel 3 contain no check mark and no cross anywhere, and that the only blue check marks in the whole image are the three in the checklist of panel 4; confirm that the table in panel 1 has exactly two body rows, 「肢D0577」 first and 「肢D0770」 second, never swapped; confirm that the left card of panel 2 has the heading 「他の登記所の管轄区域内にある土地」 with the tag 「肢D0577は、こちらの場面」 and the right card has the heading 「同じ登記所の管轄区域内にある土地」 with the tag 「肢D0770は、こちらの場面」, never swapped confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不動産登記法編2章_4コマ3_敷地の証明書は、管轄外の土地だけ.png`
- 途中の版・不採用の版：`不動産登記法編2章_4コマ3_敷地の証明書は、管轄外の土地だけ_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch2/prompt_4koma_PB-03_01_kankatsugai-shoumeisho.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で2肢の登記と土地の所在の違い、コマ2で要るのは他の登記所の管轄区域内にある土地だけ、コマ3で不動産番号は登記事項証明書の代わりにならないことが言える
- [ ] 工程C：構成表の全文言を記事（H22-Q14イ、H24-Q12オ）・法令DB（令別表12の項・15の項、令6条）と突き合わせ済み
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方は small→none→faces→既定 で隣り合うコマが同じにならない
- [ ] 工程C：肝の確認：①敷地権の目的である土地が他の登記所の管轄区域内にあるときは、その土地の登記事項証明書を提供する ②不動産番号は申請情報の一部の省略用で、証明書の代わりにならない ③敷地権発生の変更登記でも、要るのは他の登記所の土地に限る ④D0577もD0770も×

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

## 改訂履歴（このファイルは `src/spec_4koma_PB-03_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-13 v01：新規作成（総合記事②不動産登記法編 第2章【PB-3】用。型4（複数肢の対比。コマ1は比較表）。外し方が逆の2肢を、土地の所在（管轄外／同じ管轄）で並べた）
