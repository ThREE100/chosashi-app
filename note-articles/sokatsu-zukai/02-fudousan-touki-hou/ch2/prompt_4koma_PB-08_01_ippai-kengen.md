# D1529・D1530・D1531 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②「直前期の苦手論点つぶし 不動産登記法編」第2章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch2.md`）の、論点【PB-8】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PB-08_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D1529・D1530・D1531（不動産登記法／申請総論（申請情報・添付情報・代理・却下取下・還付・電子申請・登記識別情報）、出典 R02-Q04イ・ウ・エ）。正解＝D1529＝〇（正しい記述）／D1530＝×（誤った記述）／D1531＝×（誤った記述）。
- 記事：`note-articles/r2-mondai/q04-dairiken-han-i.md` イ・ウ・エ（R2：委任状が「登記申請に関する一切の権限」とだけ書かれ、特別の委任を受けていない代理人は、登録免許税の還付金の受領、電子申請での登記識別情報の提供〔暗号化〕、電子申請での登記識別情報の通知の受領〔復号〕のいずれもできない。いずれも実務上の取扱い）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】3肢とも前提は同じ（委任状は『一切の権限』とだけ書かれ、特別の委任を受けていない）で、肢の言い分の向きだけを変える。イは『還付金を受領することができない』と否定の形で書き（正しい記述なので〇）、ウ・エは『提供することができる』『通知を受けることができる』と肯定の形で書く（どちらも誤りなので×）。『一切の権限』という広い言葉で、何でも代理できそうに見せる。
- 【受験者の勘違い・定着していない点】（推測）①『一切の権限』なら、申請に関する行為は全部できると考える。②還付金の受領は金銭の受領で、登記申請とは別の行為であることが定着していない。③電子申請での登記識別情報の提供は暗号化、通知の受領は復号を伴い、それぞれ別の特別の委任が要ることが定着していない（暗号化と復号の取り違えも起こりうる）。④肢が『できない』の否定形か『できる』の肯定形かに引きずられて、〇×を逆に置く。
- 【対比する制度】「一切の権限だけ」⇔「特別の委任も受けている」：委任状が「一切の権限」とだけ書かれているときは、還付金の受領・登記識別情報の暗号化・復号はできない／それぞれについて特別の委任を受けていれば、できる（結論が逆になる点。いずれも実務上の取扱いによる整理）。
- 【型の選び方】型：型4（複数肢の対比。コマ1は比較表）。理由：3肢は行為が違う（還付金の受領／登記識別情報の提供／通知の受領）うえに、肢の言い分の向き（できない／できる）が違い、読者は自分で並べ直せない。コマ1＝3肢の比較表（肢／行為／肢の言い分）、コマ2＝分かれ目の左右のカード（一切の権限だけ／特別の委任も受けている）、コマ3＝行為ごとに特別の委任が要る理由のカード3枚、コマ4＝〇・×・×の整理。壁＝『一切の権限なら何でもできる』という思い込み、および言い分の向きに引きずられた〇×の置き違い。
- コマごとに読者が言えること：コマ1＝3肢は、行為と言い分の向きが違う（イだけ『できない』、ウ・エは『できる』）。コマ2＝一切の権限だけでは、この3つはできない。特別の委任を受けていれば、できる。コマ3＝還付金は金銭の受領で、登記識別情報の提供は暗号化・通知の受領は復号を伴うから、それぞれ特別の委任が要る。コマ4＝D1529は〇、D1530とD1531は×。
- 記事の範囲：R2-Q04イ・ウ・エ（記事 note-articles/r2-mondai/q04-dairiken-han-i.md）と、総合記事第2章【PB-8】。『登記識別情報の暗号化に関する一切の権限』『登記識別情報の復号に関する一切の権限』『登記に係る登録免許税の還付金を受領すること』の特別の委任は、いずれも実務上の取扱い（先例）による整理で、条文には明記がない。図には『実務上の取扱い』と添えた。
- extra_refs：不動産登記規則62条2項（登記識別情報の通知を受けるための特別の委任を受けた代理人がある場合には、登記識別情報の通知は、当該代理人に対してする）は、法令DB note-articles/laws/fudousan-touki-kisoku-1.md で原文を確認した。通知の受領に関する特別の委任の条文上の手がかりで、総合記事【PB-8】が通知の受領と対応づけている。
- 登場人物：人型は使わず、委任状・行為は文字のカードで示す。
- 矢印の意味：矢印は使わない。コマ1は表、コマ2は左右のカード、コマ3は縦3枚のカード。
- 配色：コマ1〜3は印（✓✕）を付けない。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、帯・リボンは濃紺（白文字）、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝small（表が横いっぱいに要るので、キャラは小さく。約150px）、コマ2＝none（図が主役）、コマ3＝faces（左に理由のカード3枚、右に会話4つの縦並び）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 「一切の権限」でも、別の委任が要る | 「別の委任が要る」を黄色マーカー |
| コマ1 見出し | ラベル | ①　3つの肢は、行為と言い分の向きが違う | — |
| コマ1 図 | 図・カード | 肢 / 行為 / 肢の言い分 / 肢D1529 / 登録免許税の還付金の受領 / 還付金を受領することができない / 肢D1530 / 電子申請での登記識別情報の提供 / 登記識別情報を提供することができる / 肢D1531 / 電子申請での登記識別情報の通知の受領 / ファイルに記録する方法で通知を受けることができる | — |
| コマ1 | 藍子（左・先に話す） | 一切の権限なら、どれもできますよね？ | — |
| コマ1 | トリ先生（右・答える） | そこが罠。言い分の向きにも注意よ | 「言い分の向き」 |
| コマ2 見出し | ラベル | ②　一切の権限だけでは、できない | — |
| コマ2 図 | 図・カード | 実務上の取扱い / 委任状の書き方で、結論が分かれる / 一切の権限だけ / 還付金の受領・暗号化・復号は、できない / 3肢の前提は、この場面 / 肢D1529・D1530・D1531は、こちらの場面 / 特別の委任も受けている / 還付金の受領・暗号化・復号も、できる / それぞれの特別の委任が要る / 一切の権限だけでは、この3つはできない | — |
| コマ3 見出し | ラベル | ③　行為ごとに、特別の委任が要る | — |
| コマ3 図 | 図・カード | 肢D1529 / 還付金の受領は、金銭の受領 / 登記申請とは別の重要な行為 / 「還付金を受領すること / 肢D1530 / 登記識別情報の提供は、暗号化 / 電子申請で暗号化して提供する / 「暗号化 / 肢D1531 / 通知の受領は、復号 / ひっかけ：言い分は「できる / 電子申請で通知を受けて復号する / 「復号 | — |
| コマ3 | 藍子（左・1番目） | 暗号化と復号は、同じ委任でいいですか？ | — |
| コマ3 | トリ先生（右・2番目） | 別々よ。提供が暗号化、通知が復号よ | 「提供が暗号化、通知が復号」 |
| コマ3 | 藍子（左・3番目） | 還付金は、なぜ別の委任なんですか？ | — |
| コマ3 | トリ先生（右・4番目） | 金銭の受領は、申請とは別の行為だからよ | 「別の行為」 |
| コマ4 見出し | ラベル | ④　結論は〇と×と× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 3つとも、特別の委任がないとできないんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。肢の向きに惑わされないでね | 「肢の向き」 |
| コマ4 チェック欄 | 3項目（青✓） | 還付金の受領には、特別の委任が要る（肢D1529は〇） / 電子申請の登記識別情報の提供は、暗号化の特別の委任が要る（肢D1530は×） / 電子申請の通知の受領は、復号の特別の委任が要る（肢D1531は×） | — |
| 結論帯 | 1行目 | 「一切の権限」だけでは、還付金・暗号化・復号はできない | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1529・D1530・D1531　正解〇・×・×（R02-Q04イ・ウ・エ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記規則62条2項（登記識別情報の通知を受けるための特別の委任を受けた代理人がある場合には、登記識別情報の通知は、当該代理人に対してする）。法令DB note-articles/laws/fudousan-touki-kisoku-1.md と照合済み。還付金の受領・暗号化・復号の特別の委任は、条文に明記はなく、実務上の取扱い

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

TITLE BANNER: text 「「一切の権限」でも、別の委任が要る」 in large bold letters; the part 「別の委任が要る」 has a yellow highlighter marker.

PANEL 1 (curious, puzzled mood; both characters appear SMALLER than in the other panels, only because this panel's diagram or text needs the room (each about 150 px tall; never below 110 px and never more than one third of the panel height; use the largest size in this range that still lets the diagram fill the panel), 藍子 at the lower left corner and トリ先生 at the lower right corner; 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　3つの肢は、行為と言い分の向きが違う」
- A wide table that fills the full panel width. The header row is dark navy with white text and has three columns: 「肢」, 「行為」, 「肢の言い分」. The three body rows have the same pale gray fill and a dark navy outline, each text at least 24 px high, with no check mark, no cross, and no arrow.
- Body row 1: 「肢D1529」, 「登録免許税の還付金の受領」, 「還付金を受領することができない」.
- Body row 2: 「肢D1530」, 「電子申請での登記識別情報の提供」, 「登記識別情報を提供することができる」.
- Body row 3: 「肢D1531」, 「電子申請での登記識別情報の通知の受領」, 「ファイルに記録する方法で通知を受けることができる」.
- The three rows have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- 藍子 bubble (left, spoken first): 「一切の権限なら、
どれもできますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そこが罠。
言い分の向きにも
注意よ」 with the part 「言い分の向き」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　一切の権限だけでは、できない」
- A small dark navy tag 「実務上の取扱い」 at the top left, with one line beside it: 「委任状の書き方で、結論が分かれる」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「一切の権限だけ」, two body lines: 「還付金の受領・暗号化・復号は、できない」, 「3肢の前提は、この場面」, and a small dark navy tag 「肢D1529・D1530・D1531は、こちらの場面」.
- Right card, heading 「特別の委任も受けている」, two body lines: 「還付金の受領・暗号化・復号も、できる」, 「それぞれの特別の委任が要る」.
- Under the two cards, one wide dark navy band with large white text 「一切の権限だけでは、この3つはできない」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　行為ごとに、特別の委任が要る」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, and a dark navy heading placed INSIDE the card, with no check mark and no cross. The cards are separated only by a small empty gap, with nothing drawn between them.
- Card 1, a small dark navy tag 「肢D1529」, heading 「還付金の受領は、金銭の受領」, two body lines 「登記申請とは別の重要な行為」 and 「「還付金を受領すること」の特別の委任」.
- Card 2, a small dark navy tag 「肢D1530」, heading 「登記識別情報の提供は、暗号化」, two body lines 「電子申請で暗号化して提供する」 and 「「暗号化」の特別の委任が要る」.
- Card 3, a small dark navy tag 「肢D1531」, heading 「通知の受領は、復号」, a dark navy ribbon tag with large white text 「ひっかけ：言い分は「できる」でも×」, two body lines 「電子申請で通知を受けて復号する」 and 「「復号」の特別の委任が要る」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「暗号化と復号は、
同じ委任で
いいですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「別々よ。
提供が暗号化、
通知が復号よ」 with the part 「提供が暗号化、通知が復号」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「還付金は、
なぜ別の委任
なんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「金銭の受領は、
申請とは別の
行為だからよ」 with the part 「別の行為」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇と×と×」
- 藍子 bubble (left, spoken first): 「3つとも、
特別の委任が
ないとできない
んですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
肢の向きに
惑わされないでね」 with the part 「肢の向き」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「還付金の受領には、特別の委任が要る（肢D1529は〇）」, 「電子申請の登記識別情報の提供は、暗号化の特別の委任が要る（肢D1530は×）」, 「電子申請の通知の受領は、復号の特別の委任が要る（肢D1531は×）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「「一切の権限」だけでは、還付金・暗号化・復号はできない」 with a yellow highlighter marker.
- Line 2: 「問題D1529・D1530・D1531　正解〇・×・×（R02-Q04イ・ウ・エ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 号, 権, 登, 肢, 解, 記, 請, 違, 還, 録 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the smaller characters are drawn within the specified size range (they must not grow and squeeze the diagram, and must not be shrunk below the range) and that nothing but the given text appears above the heads of the pictograms; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panel 1, panel 2 and panel 3 contain no check mark and no cross anywhere, and that the only blue check marks in the whole image are the three in the checklist of panel 4; confirm that the table in panel 1 has exactly three body rows, 「肢D1529」 first, 「肢D1530」 second and 「肢D1531」 third, never reordered; confirm that the left card of panel 2 has the heading 「一切の権限だけ」 and the right card has the heading 「特別の委任も受けている」, never swapped; confirm that the three cards of panel 3 are in the order 「肢D1529」, 「肢D1530」, 「肢D1531」 confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不動産登記法編2章_4コマ8_「一切の権限」でも、別の委任が要る.png`
- 途中の版・不採用の版：`不動産登記法編2章_4コマ8_「一切の権限」でも、別の委任が要る_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch2/prompt_4koma_PB-08_01_ippai-kengen.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で3肢の行為と言い分の向きの違い、コマ2で一切の権限だけでは3つともできないこと、コマ3で行為ごとに特別の委任が要る理由が言える
- [ ] 工程C：構成表の全文言を記事（R2-Q04イ・ウ・エ）・総合記事【PB-8】・法令DB（規則62条2項）と突き合わせ済み。『実務上の取扱い』の注記を入れた
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方は small→none→faces→既定 で隣り合うコマが同じにならない
- [ ] 工程C：肝の確認：①一切の権限だけでは、還付金の受領・登記識別情報の提供（暗号化）・通知の受領（復号）はできない ②それぞれについて特別の委任を受けていれば、できる ③提供は暗号化、通知の受領は復号 ④D1529は〇、D1530・D1531は×（言い分の向きに惑わされない）

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

## 改訂履歴（このファイルは `src/spec_4koma_PB-08_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-13 v01：新規作成（総合記事②不動産登記法編 第2章【PB-8】用。型4（複数肢の対比。コマ1は比較表）。言い分の向きが違う3肢を、委任状が『一切の権限』だけか特別の委任も受けているかで並べた。いずれも実務上の取扱いと注記した）
