# D1268・D1270・D0738 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②「直前期の苦手論点つぶし 不動産登記法編」の第3章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch3.md`）の、論点【PC-4】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PC-04_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D1268・D1270・D0738（不動産登記法／土地の表題・地目・地積、出典 H29-Q13イ・エ／H24-Q06ウ）。正解＝D1268＝〇（正しい記述）／D1270＝〇（正しい記述）／D0738＝×（誤った記述）。
- 記事：`note-articles/h29-mondai/q13-tochi-hyouji-touki.md` イ（一筆の一部が常時海面下に没したときは、地積に関する変更の登記）・エ（一筆の全部が河川区域内の土地になったときは、河川区域内の土地である旨の登記を嘱託）。ほか、H24-Q06ウ（h24-mondai/q06-chimoku-henkou.md。河川区域内の土地である旨の登記の抹消は、地目の変更の登記の前提でない）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】D1268は『一筆の一部が常時海面下に没する状態になった場合』と、土地が減る出来事を書き、滅失の登記に見せる。D1270は『嘱託する登記の目的』と書き、所有者が申請する登記と同じ並びで扱わせる。D0738は『河川区域内の土地である旨の登記のある土地』と『抹消をしなければ、地目の変更の登記を申請することはできない』を重ね、抹消が前提のように読ませる。
- 【受験者の勘違い・定着していない点】（推測）①土地の一部が沈んだだけで、滅失の登記と考える（一部は地積の変更、全部が滅失）。②河川区域内の土地である旨の登記も、所有者が申請するものと考える（河川管理者が嘱託する）。③地目の変更の前に、河川区域内の登記を抹消しなければならないと考える（要らない要件を足す）。
- 【対比する制度】「名義人が申請する登記」⇔「管理者が嘱託する登記」：土地の一部が常時海面下に没したときの地積に関する変更の登記や、全部が滅失したときの滅失の登記は、所有権の登記名義人などが申請する（法37条1項・法42条）／河川区域内の土地である旨の登記と、その抹消は、河川管理者が嘱託する（法43条2項・3項）（申請する人が逆になる点）。また「地積に関する変更の登記」⇔「滅失の登記」：一部が沈めば地積の変更、全部が滅失すれば滅失の登記。
- 【型の選び方】型：型4（複数肢の対比。コマ3の右に型5の整理カードを併用）。理由：3つの肢は日付のない別々の場面なので、コマ1は『肢／場面／肢の言い分』の比較表にした。コマ2は『名義人が申請する登記』と『管理者が嘱託する登記』の左右の対比。コマ3は、抹消が前提という思い込みを左（上＝✕・下＝✓）で正し、右に、地目変更と河川区域の登記の関係の整理カードを置いた。壁＝『河川区域の登記も、地目変更の前に所有者が片づけるもの』。
- コマごとに読者が言えること：コマ1＝3つの肢の場面（一部の海没、全部が河川区域内、河川区域内の登記のある土地の地目変更）。コマ2＝海没は名義人が申請（一部は地積の変更、全部は滅失）、河川区域内の登記は管理者が嘱託。コマ3＝地目変更に、河川区域内の登記の抹消が先という規定はない。コマ4＝D1268は〇、D1270は〇、D0738は×。
- 記事の範囲：H29-Q13イ・エ（法37条1項、法43条2項。一部が常時海面下に没したことが地積の変更に当たる点は、記事が先例〔昭33.4.11民事三発203号〕に基づくとする取扱い）、H24-Q06ウ（法43条1項〜3項。地目の変更の登記を河川区域内の登記の抹消の後に限る規定はない）。全部が滅失したときの滅失の登記は法42条（滅失の日から1か月以内）で、総合記事②の【PC-4】の整理。海没が一時的なとき（滅失の登記をしない）は、記事H29-Q13ウの別の論点なので、この本には入れない。『抹消を前提とする規定がない』は、記事の言い方にそろえた。
- extra_refs：不動産登記法37条1項（地目又は地積について変更があったときは、表題部所有者又は所有権の登記名義人は、その変更があった日から一月以内に、当該地目又は地積に関する変更の登記を申請しなければならない）、42条（土地が滅失したときは、表題部所有者又は所有権の登記名義人は、その滅失の日から一月以内に、当該土地の滅失の登記を申請しなければならない）、43条2項・3項（河川区域内の土地となったとき、またはならなくなったときは、河川管理者は、遅滞なく、その旨の登記又は抹消を登記所に嘱託しなければならない）は、法令DB note-articles/laws/fudousan-touki-hou.md で原文を確認。
- 対象外にした肢：D1041（電子申請の表題登記で、署名用電子証明書を住所を証する情報に代えられる・規則44条1項）は、『だれが、何の登記をするか』という軸と別の話題（添付情報）で、同じ論点の図解6の早見表で扱うため、この4コマには入れない。
- 登場人物：人型は使わず、土地と河川区域は文字のカードで示す。
- 矢印の意味：矢印は使わない。コマ1は表、コマ2は左右のカード、コマ3は上下のカードと整理カード。
- 配色：コマ1・2は印（✓✕）を付けない。コマ3の左は上＝✕、下＝✓の1個ずつ。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝small（3列の表が横いっぱいに要るので、キャラは小さく）、コマ2＝none（図が主役）、コマ3＝faces（左に上下2枚のカード、右に会話2つと整理カード）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。図解（prompt_infographic_PC-4.md）の5行の早見表とは重ねず、この4コマは『申請する登記と嘱託される登記の違い』と『抹消は前提でない』に絞った。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 海没は申請、河川区域は管理者の嘱託 | 「管理者の嘱託」を黄色マーカー |
| コマ1 見出し | ラベル | ①　3つの肢を並べる | — |
| コマ1 図 | 図・カード | 肢 / 場面 / 肢の言い分 / 肢D1268 / 一筆の一部が、常時海面下に没した / 地積に関する変更の登記を申請する / 肢D1270 / 一筆の全部が、河川区域内の土地になった / 河川区域内の土地である旨の登記を嘱託する / 肢D0738 / 河川区域内の土地の地目が変わった / 旨の登記を抹消するまで、地目変更は申請できない / 申請する / 嘱託する / だれが、どの登記をする？ | — |
| コマ1 | 藍子（左・先に話す） | 河川区域の登記は、抹消が先ですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。抹消は前提じゃないのよ | 「前提じゃない」 |
| コマ2 見出し | ラベル | ②　申請する登記と、嘱託される登記 | — |
| コマ2 図 | 図・カード | 土地の状況が変わったとき / 動く人も、登記も違う / 名義人が申請する登記 / 法37条1項・42条 / 一部が常時海面下に没したとき / 地積に関する変更の登記 / 全部が滅失したら、滅失の登記 / 管理者が嘱託する登記 / 法43条2項・3項 / 河川区域内の土地になったとき / 河川管理者が、遅滞なく嘱託 / 抹消も、河川管理者が嘱託 / 海没は申請、河川区域の登記は嘱託 | — |
| コマ3 見出し | ラベル | ③　抹消は前提になるのか | — |
| コマ3 図 | 図・カード | 抹消が先に要る / 肢D0738の言い分 / 抹消は前提にならない / 地目変更は、そのまま申請できる / 地目変更と河川区域の登記 / 地目変更の登記は、名義人が申請 / 河川区域内の旨の登記は、管理者が嘱託 / 地目変更を抹消の後に限る規定はない / ひっかけ：要らない要件を足す / 要らない要件 | — |
| コマ3 | 藍子（左・1番目） | 抹消されるまで、待つんですよね？ | — |
| コマ3 | トリ先生（右・2番目） | いいえ。別々の登記なのよ | 「別々の登記」 |
| コマ4 見出し | ラベル | ④　結論は〇・〇・× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 申請と嘱託を、分けて考えるんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。抹消は前提にならないのよ | 「前提にならない」 |
| コマ4 チェック欄 | 3項目（青✓） | 一部が常時海面下に没したら、地積に関する変更の登記を申請する（肢D1268は〇） / 全部が河川区域内の土地になったら、管理者がその旨の登記を嘱託する（肢D1270は〇） / 地目の変更は、河川区域内の旨の登記の抹消を待たずに申請できる（肢D0738は×） | — |
| 結論帯 | 1行目 | 海没は申請。河川区域は嘱託。抹消は前提でない | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1268・D1270・D0738　正解〇・〇・×（H29-Q13イ・エ／H24-Q06ウ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記法37条1項・42条・43条2項・3項。法令DB note-articles/laws/fudousan-touki-hou.md と照合済み。一部の海没が地積の変更に当たる点は、記事H29-Q13イの先例に基づく取扱い（図には条文番号〔法37条1項〕のみ載せた）。『抹消を地目変更の前提とする規定はない』は、記事H24-Q06ウの言い方にそろえた

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

TITLE BANNER: text 「海没は申請、河川区域は管理者の嘱託」 in large bold letters; the part 「管理者の嘱託」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear SMALLER than in the other panels, only because this panel's diagram or text needs the room (each about 150 px tall; never below 110 px and never more than one third of the panel height; use the largest size in this range that still lets the diagram fill the panel), 藍子 at the lower left corner and トリ先生 at the lower right corner; 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　3つの肢を並べる」
- A wide table that fills the full panel width. The header row is dark navy with white text and has three columns: 「肢」, 「場面」, 「肢の言い分」. The three body rows have the same pale gray fill and a dark navy outline, each text at least 24 px high, with no check mark, no cross, and no arrow.
- Body row 1: 「肢D1268」, 「一筆の一部が、常時海面下に没した」, 「地積に関する変更の登記を申請する」.
- Body row 2: 「肢D1270」, 「一筆の全部が、河川区域内の土地になった」, 「河川区域内の土地である旨の登記を嘱託する」.
- Body row 3: 「肢D0738」, 「河川区域内の土地の地目が変わった」, 「旨の登記を抹消するまで、地目変更は申請できない」.
- In the third column, the strings 「申請する」 and 「嘱託する」 differ by one word; copy each exactly as given and do not change one into the other.
- A small question badge 「だれが、どの登記をする？」 with a pale gray fill and a dark navy outline sits at the upper right of the table (a question badge only, with no check mark and no cross).
- 藍子 bubble (left, spoken first): 「河川区域の登記は、
抹消が先ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
抹消は前提
じゃないのよ」 with the part 「前提じゃない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　申請する登記と、嘱託される登記」
- A small dark navy tag 「土地の状況が変わったとき」 at the top left, with one line beside it: 「動く人も、登記も違う」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「名義人が申請する登記」, a small tag 「法37条1項・42条」, three body lines: 「一部が常時海面下に没したとき」, 「地積に関する変更の登記」, 「全部が滅失したら、滅失の登記」.
- Right card, heading 「管理者が嘱託する登記」, a small tag 「法43条2項・3項」, three body lines: 「河川区域内の土地になったとき」, 「河川管理者が、遅滞なく嘱託」, 「抹消も、河川管理者が嘱託」.
- Under the two cards, one wide dark navy band with large white text 「海没は申請、河川区域の登記は嘱託」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　抹消は前提になるのか」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 2 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 120 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 2 face icons and exactly 2 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.
- LEFT SIDE: two stacked cards of the same size, top and bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card, with no arrow and no connector. The cards are separated only by a small empty gap.
- Top card, heading 「抹消が先に要る」, body 「肢D0738の言い分」, and ONE red cross only at the bottom of this card (no check mark on this card).
- Bottom card, heading 「抹消は前提にならない」, body 「地目変更は、そのまま申請できる」, and ONE blue check mark only at the bottom of this card (no cross on this card).
- RIGHT SIDE, under the two speech bubbles (the two speech bubbles and their two faces stay at the top of the right side): one tall list card with a dark navy heading 「地目変更と河川区域の登記」, with the same pale gray fill and a dark navy outline, containing exactly three short rows, each with a small dark navy dot at its left end (NO digit and NO letter on the dots), with no arrow and no check mark and no cross: 「地目変更の登記は、名義人が申請」, 「河川区域内の旨の登記は、管理者が嘱託」, 「地目変更を抹消の後に限る規定はない」, with the third row highlighted with a yellow marker. Under the three rows, one small dark navy ribbon tag with white text 「ひっかけ：要らない要件を足す」, with the text 「要らない要件」 highlighted with a yellow marker.
- The list card is a part of the right side, and it is NOT a speech bubble. The left cards and the list card have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 2 in the conversation column; face icon at the LEFT end of its own row): 「抹消されるまで、
待つんですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 2 in the conversation column; face icon at the RIGHT end of its own row): 「いいえ。
別々の登記
なのよ」 with the part 「別々の登記」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇・〇・×」
- 藍子 bubble (left, spoken first): 「申請と嘱託を、
分けて考える
んですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
抹消は
前提にならない
のよ」 with the part 「前提にならない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「一部が常時海面下に没したら、地積に関する変更の登記を申請する（肢D1268は〇）」, 「全部が河川区域内の土地になったら、管理者がその旨の登記を嘱託する（肢D1270は〇）」, 「地目の変更は、河川区域内の旨の登記の抹消を待たずに申請できる（肢D0738は×）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「海没は申請。河川区域は嘱託。抹消は前提でない」 with a yellow highlighter marker.
- Line 2: 「問題D1268・D1270・D0738　正解〇・〇・×（H29-Q13イ・エ／H24-Q06ウ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 地, 登, 肢, 規, 解, 記, 請, 違 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the left comparison card has only a red cross and the right card only a blue check mark; confirm that the smaller characters are drawn within the specified size range (they must not grow and squeeze the diagram, and must not be shrunk below the range) and that nothing but the given text appears above the heads of the pictograms; confirm that the conversation column has exactly 2 face icons and exactly 2 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不登法第3章_4コマ4_海没は申請、河川区域は管理者の嘱託.png`
- 途中の版・不採用の版：`不登法第3章_4コマ4_海没は申請、河川区域は管理者の嘱託_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch3/prompt_4koma_PC-04_01_kaibotsu-kasen.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1の表で3つの肢の場面と言い分が言え、コマ2で名義人が申請する登記と管理者が嘱託する登記の違い、コマ3で地目変更に抹消が先という規定がないことが言える
- [ ] 工程C：構成表の全文言を記事（H29-Q13イ・エ、H24-Q06ウ）・法令DB（法37条・42条・43条）と突き合わせ済み。海没が一時的なとき・電子申請の住所証明は、この本の範囲外
- [ ] 工程C：コマ1・2に印がなく、コマ3の左は上＝✕・下＝✓の1個ずつ、コマ4だけ青✓。コマの使い方は small→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはコマ1だけ（表が横いっぱいに要るため）
- [ ] 工程C：肝の確認：①一部が常時海面下に没したら地積に関する変更の登記、全部が滅失したら滅失の登記（法37条1項・法42条） ②河川区域内の土地である旨の登記と抹消は河川管理者が嘱託（法43条2項・3項） ③地目の変更の登記は、河川区域内の登記の抹消を待たずに申請できる ④D1268は〇、D1270は〇、D0738は×

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

## 改訂履歴（このファイルは `src/spec_4koma_PC-04_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-13 v01：新規作成（総合記事②不動産登記法編 第3章【PC-4】用。型4（複数肢の対比。＋型5の整理カード）。3肢の場面の表、名義人が申請する登記と管理者が嘱託する登記の対比、抹消は前提でないことの整理カードを組んだ）
