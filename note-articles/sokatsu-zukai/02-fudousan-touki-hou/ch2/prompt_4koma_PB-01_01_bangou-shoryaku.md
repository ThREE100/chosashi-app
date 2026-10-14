# D0947・D1233 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②「直前期の苦手論点つぶし 不動産登記法編」第2章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch2.md`）の、論点【PB-1】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PB-01_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D0947・D1233（不動産登記法／申請総論（申請情報・添付情報）、出典 H26-Q08ア／H29-Q06イ）。正解＝D0947＝〇（正しい記述）／D1233＝×（誤った記述）。
- 記事：`note-articles/h29-mondai/q06-shinsei-jouhou.md` イ（H29：会社法人等番号を提供しても代表者の氏名は申請情報に書く。令3条2号。省略できるのは添付情報のほうで、申請情報の記載事項とは別物）。ほか、H26-Q08ア（h26-mondai/q08-tenpu-jouhou.md。番号を有する法人は番号を提供すれば代表者の資格を証する情報の提供を要しない。令7条1項1号イ。出題当時の文言を現行法に合わせた改題）。章の記事 note-articles/column/sokatsu-02-fudousan-touki-hou-ch2.md 【PB-1】
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】2肢とも『会社法人等番号を有する法人』が『番号を提供したとき』という同じ前提で、省略の対象だけを入れ替えている。D0947は代表者の資格を証する情報（添付情報）の提供を要しないと問い（〇）、D1233は代表者の氏名（申請情報の内容）を記載することを要しないと問う（×）。『番号を出せば代表者の件は全部省ける』という広い読みに乗せる。
- 【受験者の勘違い・定着していない点】（推測）①番号の提供で省けるものの範囲を広げ、添付情報（資格を証する情報）と申請情報の記載事項（代表者の氏名）を同じ棚に入れる（令3条は申請情報の内容、令7条は添付情報で、条が違う）。②逆に、番号を出しても結局は別の書類が要ると慎重に読みすぎる（令7条1項1号イは、番号の提供そのものが添付情報）。
- 【対比する制度】「代表者の資格を証する情報」⇔「代表者の氏名」：番号を提供したとき、代表者の資格を証する情報（添付情報）は提供を要しない（令7条1項1号イ）／代表者の氏名（申請情報）は、番号を提供しても申請情報の内容として書く（令3条2号）（結論が逆になる点）。
- 【型の選び方】型：型3（理由のコマ）に型5（整理カード併用）を組み合わせる。理由：2肢は同じ前提（番号の提供）で結論が逆（〇と×）だが、読者に欠けているのは『なぜ氏名だけが省けないのか』という理由で、結論の暗記だけでは別の肢（支配人・住所など）で崩れる。理由＝省けるのは令7条の添付情報の側、令3条2号の申請情報は別の条で定められている、という置き場の違いで、短い3行にまとめられるので、コマ3の右側を整理カードにする。壁＝『番号で代表者の件は全部省ける』という広い読み。コマ1＝2肢の比較表（肢／番号を提供したときの対象／肢の言い分）、コマ2＝『番号の提供で足りる添付情報』と『番号を出しても書く申請情報』の左右のカード、コマ3＝左に✕✓の1個ずつ（理由）、右に会話1往復と『番号の提供と代表者』の整理カード、コマ4＝2肢の整理。
- コマごとに読者が言えること：コマ1＝2肢はどちらも番号を提供したときの話だが、省くと言っているものが代表者の資格を証する情報と代表者の氏名で違う。コマ2＝番号の提供で足りるのは添付情報（令7条1項1号イ）、代表者の氏名は申請情報（令3条2号）。コマ3＝番号が代わるのは添付情報の側で、氏名は令3条2号が別に定める申請情報。コマ4＝D0947は〇、D1233は×。
- 記事の範囲：H29-Q06イ（令3条2号。番号を提供しても代表者の氏名は申請情報に書く）、H26-Q08ア（令7条1項1号イ。番号を提供すれば代表者の資格を証する情報は不要）。章の記事【PB-1】の『省略できるのは添付情報、省略できないのは申請情報の記載事項』という二層の整理と矛盾しない。D0947はバンク上『現行法に合わせた改題』（出題当時は規則36条1項2号の登記所基準）なので、図は現行の令7条1項1号イに合わせ、出題当時の文言は入れない。
- 条文に明記のない整理：『申請情報と添付情報の二層』は、令3条（申請情報の内容）と令7条（添付情報）が別の条に置かれていることからの整理で、条文が『省略できるのは添付情報だけ』と書いているわけではない。図でも『令7条の添付情報』『令3条2号の申請情報』と条を添え、『禁止』『明記』とは書かない。コマ3下のカードは、令3条2号が代表者の氏名を申請情報の内容と定めている、という事実の言い換え。
- extra_refs：不動産登記令3条2号（申請人が法人であるときは、その代表者の氏名）、同7条1項1号イ（会社法人等番号を有する法人にあっては、当該法人の会社法人等番号）・ロ（イに規定する法人以外の法人にあっては、当該法人の代表者の資格を証する情報）は、法令DB note-articles/laws/fudousan-touki-rei.md の原文で確認した。
- 登場人物：人型は使わず、条文・情報は文字のカードで示す。
- 矢印の意味：矢印は使わない。コマ1は表、コマ2は左右のカード、コマ3は上下2枚のカードと整理カード。
- 配色：コマ1・2は印（✓✕）を付けない。コマ3の左は上＝✕、下＝✓の1個ずつ（肢D1233の言い分と、正しい整理）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、帯・リボンは濃紺（白文字）、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝small（表が横いっぱいに要るので、キャラは小さく。約150px）、コマ2＝none（図が主役）、コマ3＝faces（左に上下2枚のカード、右に会話2つと整理カード）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 番号で省けるのは添付情報だけ | 「添付情報だけ」を黄色マーカー |
| コマ1 見出し | ラベル | ①　どちらの肢も、番号を提供したときの話 | — |
| コマ1 図 | 図・カード | 肢 / 省くと言うもの / 肢の言い分 / 肢D0947 / 代表者の資格を証する情報 / 番号を提供したときは、提供を要しない / 肢D1233 / 代表者の氏名 / 番号を提供したときは、申請情報の内容とすることを要しない | — |
| コマ1 | 藍子（左・先に話す） | 番号を出せば、代表者の件は全部省けますよね？ | — |
| コマ1 | トリ先生（右・答える） | 全部ではないの。肢D1233は×よ | 「全部ではない」 |
| コマ2 見出し | ラベル | ②　省けるのは添付情報、書くのは申請情報 | — |
| コマ2 図 | 図・カード | 会社法人等番号を提供したとき / 省くものによって、結論が分かれる / 番号の提供で足りる / 令7条1項1号イ / 代表者の資格を証する情報 / 添付情報の側 / 肢D0947は、こちらの場面 / 番号を出しても書く / 令3条2号 / 法人の代表者の氏名 / 申請情報の側 / 肢D1233は、こちらの場面 / 省けるのは添付情報。申請情報は書く | — |
| コマ3 見出し | ラベル | ③　なぜ氏名は省けないのか | — |
| コマ3 図 | 図・カード | 番号を出せば、代表者の氏名も要らない / 肢D1233の言い分 / 番号が代わるのは、添付情報の側 / 氏名は、令3条2号の申請情報の内容 / 番号の提供と、代表者 / 番号を持つ法人は、番号を提供する / 資格を証する情報は、提供を要しない / 代表者の氏名は、申請情報に書く / 肢D0947は上から2つ目、肢D1233は一番下 | — |
| コマ3 | 藍子（左・1番目） | なぜ、氏名だけは省けないのですか？ | — |
| コマ3 | トリ先生（右・2番目） | 条が違うの。氏名は申請情報よ | 「申請情報」 |
| コマ4 見出し | ラベル | ④　結論は〇と× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 省けるのは、添付情報のほうなんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。氏名は、番号でも書くのよ | 「番号でも書く」 |
| コマ4 チェック欄 | 3項目（青✓） | 番号を提供すれば、代表者の資格を証する情報は不要（肢D0947は〇） / 代表者の氏名は、番号を提供しても申請情報に書く（肢D1233は×） / 先に、申請情報か添付情報かを見分ける（令3条と令7条） | — |
| 結論帯 | 1行目 | 番号で省けるのは添付情報。代表者の氏名は書く | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0947・D1233　正解〇・×（H26-Q08ア／H29-Q06イ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記令3条2号（申請人が法人であるときは、その代表者の氏名）、同7条1項1号イ・ロ（申請人が法人であるときの添付情報：会社法人等番号を有する法人は番号、それ以外の法人は代表者の資格を証する情報）。法令DB note-articles/laws/fudousan-touki-rei.md と照合済み（『申請情報と添付情報の二層』は条の置き場所からの整理）

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

TITLE BANNER: text 「番号で省けるのは添付情報だけ」 in large bold letters; the part 「添付情報だけ」 has a yellow highlighter marker.

PANEL 1 (curious, puzzled mood; both characters appear SMALLER than in the other panels, only because this panel's diagram or text needs the room (each about 150 px tall; never below 110 px and never more than one third of the panel height; use the largest size in this range that still lets the diagram fill the panel), 藍子 at the lower left corner and トリ先生 at the lower right corner; 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　どちらの肢も、番号を提供したときの話」
- A wide table that fills the full panel width. The header row is dark navy with white text and has three columns: 「肢」, 「省くと言うもの」, 「肢の言い分」. The two body rows have the same pale gray fill and a dark navy outline, each text at least 24 px high, with no check mark, no cross, and no arrow.
- Body row 1: 「肢D0947」, 「代表者の資格を証する情報」, 「番号を提供したときは、提供を要しない」.
- Body row 2: 「肢D1233」, 「代表者の氏名」, 「番号を提供したときは、申請情報の内容とすることを要しない」.
- The two rows have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- 藍子 bubble (left, spoken first): 「番号を出せば、
代表者の件は
全部省けますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「全部ではないの。
肢D1233は×よ」 with the part 「全部ではない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　省けるのは添付情報、書くのは申請情報」
- A small dark navy tag 「会社法人等番号を提供したとき」 at the top left, with one line beside it: 「省くものによって、結論が分かれる」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「番号の提供で足りる」, a small tag 「令7条1項1号イ」, two body lines: 「代表者の資格を証する情報」, 「添付情報の側」, and a small dark navy tag 「肢D0947は、こちらの場面」.
- Right card, heading 「番号を出しても書く」, a small tag 「令3条2号」, two body lines: 「法人の代表者の氏名」, 「申請情報の側」, and a small dark navy tag 「肢D1233は、こちらの場面」.
- Under the two cards, one wide dark navy band with large white text 「省けるのは添付情報。申請情報は書く」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ氏名は省けないのか」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 2 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 120 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 2 face icons and exactly 2 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.
- LEFT SIDE: two stacked cards of the same size, top and bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card, with no arrow and no connector. The cards are separated only by a small empty gap.
- Top card, heading 「番号を出せば、代表者の氏名も要らない」, body 「肢D1233の言い分」, and ONE red cross only at the bottom of this card (no check mark on this card).
- Bottom card, heading 「番号が代わるのは、添付情報の側」, body 「氏名は、令3条2号の申請情報の内容」, and ONE blue check mark only at the bottom of this card (no cross on this card).
- RIGHT SIDE, under the two speech bubbles (the two speech bubbles and their two faces stay at the top of the right side): one tall list card with a dark navy heading 「番号の提供と、代表者」, with the same pale gray fill and a dark navy outline, containing exactly three short rows, each with a small dark navy dot at its left end (NO digit and NO letter on the dots), with no arrow and no check mark and no cross: 「番号を持つ法人は、番号を提供する」, 「資格を証する情報は、提供を要しない」, 「代表者の氏名は、申請情報に書く」, with the second and third rows highlighted with a yellow marker. Under the three rows, one small dark navy ribbon tag with white text 「肢D0947は上から2つ目、肢D1233は一番下」.
- The list card is a part of the right side, and it is NOT a speech bubble. The left cards and the list card have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 2 in the conversation column; face icon at the LEFT end of its own row): 「なぜ、氏名だけは
省けないのですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 2 in the conversation column; face icon at the RIGHT end of its own row): 「条が違うの。
氏名は申請情報よ」 with the part 「申請情報」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇と×」
- 藍子 bubble (left, spoken first): 「省けるのは、
添付情報の
ほうなんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
氏名は、番号でも
書くのよ」 with the part 「番号でも書く」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「番号を提供すれば、代表者の資格を証する情報は不要（肢D0947は〇）」, 「代表者の氏名は、番号を提供しても申請情報に書く（肢D1233は×）」, 「先に、申請情報か添付情報かを見分ける（令3条と令7条）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「番号で省けるのは添付情報。代表者の氏名は書く」 with a yellow highlighter marker.
- Line 2: 「問題D0947・D1233　正解〇・×（H26-Q08ア／H29-Q06イ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 代, 号, 番, 肢, 解, 証, 請, 違 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the left comparison card has only a red cross and the right card only a blue check mark; confirm that the smaller characters are drawn within the specified size range (they must not grow and squeeze the diagram, and must not be shrunk below the range) and that nothing but the given text appears above the heads of the pictograms; confirm that the conversation column has exactly 2 face icons and exactly 2 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panel 1 and panel 2 contain no check mark and no cross anywhere, that panel 3 has exactly one red cross (on the top-left card) and exactly one blue check mark (on the bottom-left card) and no other mark, and that the only blue check marks outside panel 3 are the three in the checklist of panel 4; confirm that the table in panel 1 has exactly two body rows, 「肢D0947」 first and 「肢D1233」 second, never swapped; confirm that the left card of panel 2 has the heading 「番号の提供で足りる」 with the tag 「肢D0947は、こちらの場面」 and the right card has the heading 「番号を出しても書く」 with the tag 「肢D1233は、こちらの場面」, never swapped confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不動産登記法編2章_4コマ1_番号で省けるのは添付情報だけ.png`
- 途中の版・不採用の版：`不動産登記法編2章_4コマ1_番号で省けるのは添付情報だけ_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch2/prompt_4koma_PB-01_01_bangou-shoryaku.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で2肢がどちらも番号を提供したときの話なのに省くものが違う、コマ2で番号の提供で足りるのは添付情報で代表者の氏名は申請情報、コマ3でなぜ氏名が省けないか（条が違う）が言える
- [ ] 工程C：構成表の全文言を記事（H29-Q06イ、H26-Q08ア）・法令DB（令3条2号、令7条1項1号イ・ロ）と突き合わせ済み
- [ ] 工程C：コマ1・2に印がなく、コマ3の左は上＝✕・下＝✓の1個ずつ、コマ4だけ青✓。コマの使い方は small→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない
- [ ] 工程C：肝の確認：①番号を持つ法人は番号を提供すれば代表者の資格を証する情報は不要（令7条1項1号イ） ②代表者の氏名は番号を提供しても申請情報に書く（令3条2号） ③省けるのは添付情報、書くのは申請情報 ④D0947は〇、D1233は×

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

## 改訂履歴（このファイルは `src/spec_4koma_PB-01_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-14 v01：新規作成（総合記事②不動産登記法編 第2章【PB-1】用。型3（理由のコマ）に型5（整理カード併用）を組み合わせた。同じ会社法人等番号の提供で、省ける添付情報（代表者の資格を証する情報）と省けない申請情報（代表者の氏名）を、令7条と令3条の置き場所で整理した）
