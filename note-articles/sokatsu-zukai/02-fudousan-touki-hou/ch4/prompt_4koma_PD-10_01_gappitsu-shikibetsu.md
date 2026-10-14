# D1051・D1052 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②不動産登記法編 第4章「土地の分筆・合筆・地積更正」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch4.md`）の、論点【PD-10】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PD-10_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D1051・D1052（不動産登記法／土地の分筆・合筆・地積更正、出典 H27-Q09イ／H27-Q09ウ）。正解＝D1051＝〇（正しい記述）／D1052＝×（誤った記述）。
- 記事：`note-articles/h27-mondai/q09-gappitsu.md` イ（委任による代理人が登記識別情報の通知を受けるには、特別の委任が必要。なければ受けられない）。ウ（登記識別情報を提供できない理由は、申請情報の内容とすれば足り、理由を証する情報は不要）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】D1051は『特別の委任を受けていないときは、通知を受けることができない』と、正しい結論を言い切る。代理人に頼んだのだから通知も当然に受け取れる、と思っている受験者には『受けることができない』が言い過ぎに見え、×にしたくなる。D1052は『理由を申請情報の内容とするときは、その理由を証する情報を提供しなければならない』と、書くだけで足りるところに、証明まで求める。提供できない事情があるなら証拠が要る、という日常の感覚に乗って、〇にしたくなる。どちらも『登記識別情報』の話なので、同じ向きの扱いに見える。
- 【受験者の勘違い・定着していない点】（推測）①委任して申請を任せたのだから、合筆後の新しい登記識別情報の通知も代理人が受け取れると考える（D1051）。②通知を受ける権限は、申請の代理権とは別に特別の委任が必要だ、という区別が結びついていない。③登記識別情報を提供できない理由には、証明する書類が要ると考える（D1052）。④『提供する』場面と『通知を受ける』場面を混ぜ、どちらにも同じ厳しさが要ると考える。
- 【対比する制度】「合筆後に通知を受ける」⇔「提供できないとき」：通知を代理人が受けるには、受けることができる旨の特別の委任が要り、なければ受けられない／提供できない理由は申請情報の内容とすれば足り、理由を証する情報は要らない（厳しさの向きが逆になる点）。
- 【型の選び方】型：型4（2肢の対比。型3の理由コマを組み合わせる）。理由：2つの肢は同じ合筆の申請の中の、通知を受ける場面と提供できない場面という別の場面で、正しい扱いが『特別の委任という手間が要る』と『証明という手間は要らない』で逆向きになる。コマ1は2つの肢の言い分の表、コマ2は『通知を受ける』『提供できない』の左右の対比、コマ3は2つの肢の言い分のカード（〇と×）と、なぜそうなるかの会話。壁＝『代理人は通知も当然に受けられる／提供できない理由には証拠が要る、という日常感覚』。
- コマごとに読者が言えること：コマ1＝合筆のとき、代理人が通知を受けられるか、提供できない理由に証明が要るかを問う2つの肢。コマ2＝通知を代理人が受けるには特別の委任が要る、提供できない理由は書けば足りて証明は要らない。コマ3＝D1051の言い分は正しく、D1052の言い分は誤り。通知の受領は代理権に含まれず、提供できない理由は書くだけ。コマ4＝D1051は〇、D1052は×。
- 記事の範囲：H27-Q09イ（不動産登記規則62条2項。委任による代理人が通知を受けるには、登記識別情報の通知を受けることができる旨の特別の委任が必要。なければ受けられない）、H27-Q09ウ（不動産登記令3条12号。提供できない正当な理由があるときは、その理由〔不通知、失効、失念など〕を申請情報の内容とすれば足り、理由を証する情報まで提供する必要はない）。記事は、所有権の登記がある土地の合筆では、いずれか一筆の所有権の登記名義人の登記識別情報を提供する点（令8条）も述べているが、2つの肢の決め手ではないので、図は『提供する』の語にとどめ、令8条の中身には踏み込まない。『理由を証する情報は要らない』は、令3条12号が理由を申請情報の内容とだけ定めている点からの記事の整理で、証明を求める条文が見当たらない、という扱いで書く。
- extra_refs：不動産登記規則62条2項（登記識別情報の通知を受けるための特別の委任を受けた代理人がある場合には、登記識別情報の通知は、当該代理人に対してするものとする）、不動産登記令3条12号（不動産登記法22条ただし書の規定により登記識別情報を提供することができないときは、当該登記識別情報を提供することができない理由）は、法令DB note-articles/laws/fudousan-touki-kisoku-1.md・fudousan-touki-rei.md で原文を確認。
- 登場人物：当事者の人型は使わず、事情は文字のカードと表で示す。
- 矢印の意味：矢印は使わない。コマ1は表、コマ2は左右のカード、コマ3は左の上下2枚のカードと右の会話。
- 配色：コマ1・2は印（✓✕）を付けない。コマ3の左は上＝✓、下＝✕の1個ずつ（上の肢D1051の言い分は正しい記述、下の肢D1052の言い分は誤った記述）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝small（表が横いっぱいに要るので、キャラは小さく）、コマ2＝none（図が主役）、コマ3＝faces（左に上下2枚の言い分のカード、右に会話4つの縦並び）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 通知は特別の委任、理由は書くだけ | 「特別の委任」を黄色マーカー |
| コマ1 見出し | ラベル | ①　代理人は、通知も受けられる？ | — |
| コマ1 図 | 図・カード | 肢 / 場面 / 肢の言い分 / 肢D1051 / 代理人が合筆を申請。特別の委任はない / 通知を受けることができない / 肢D1052 / 登記識別情報を提供できない / 理由を証する情報も提供する / 何が必要になる？ | — |
| コマ1 | 藍子（左・先に話す） | 代理人なら、通知も受け取れますよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。そこに落とし穴があるわよ | 「落とし穴」 |
| コマ2 見出し | ラベル | ②　通知を受ける側と提供できない側 | — |
| コマ2 図 | 図・カード | 合筆の登記識別情報 / 場面で、必要なものが違う / 合筆後に通知を受ける / 代理人が受けるとき / 特別の委任が必要 / なければ受けられない / 提供できないとき / 失念、失効など / 理由は申請情報に書けば足りる / 理由を証する情報は要らない | — |
| コマ3 見出し | ラベル | ③　なぜ、そう分かれる？ | — |
| コマ3 図 | 図・カード | 肢D1051の言い分 / 特別の委任がなければ、通知を受けられない / 肢D1052の言い分 / 理由を証する情報も提供する | — |
| コマ3 | 藍子（左・1番目） | 委任したのに、通知は別なんですか？ | — |
| コマ3 | トリ先生（右・2番目） | ええ。通知を受ける委任は、別に要るの | 「別に要る」 |
| コマ3 | 藍子（左・3番目） | 提供できない理由は、証明が要る？ | — |
| コマ3 | トリ先生（右・4番目） | いいえ。理由を書けば足りるのよ | 「書けば足りる」 |
| コマ4 見出し | ラベル | ④　結論は〇と× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 通知は委任、理由は書くだけなんですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。証明までは要らないのよ | 「証明までは要らない」 |
| コマ4 チェック欄 | 3項目（青✓） | 代理人が通知を受けるには、特別の委任が必要（肢D1051は〇） / 提供できない理由は、申請情報に書けば足りる（肢D1052は×） / 提供できない理由を証する情報は、要らない | — |
| 結論帯 | 1行目 | 通知は特別の委任。提供できない理由は書くだけ | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1051・D1052　正解〇・×（H27-Q09イ／H27-Q09ウ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記規則62条2項、不動産登記令3条12号。法令DB note-articles/laws/fudousan-touki-kisoku-1.md・fudousan-touki-rei.md と照合済み。令8条（所有権の登記がある土地の合筆では、いずれか一筆の名義人の登記識別情報を提供）は、2つの肢の決め手ではないので図に入れていない

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

TITLE BANNER: text 「通知は特別の委任、理由は書くだけ」 in large bold letters; the part 「特別の委任」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear SMALLER than in the other panels, only because this panel's diagram or text needs the room (each about 150 px tall; never below 110 px and never more than one third of the panel height; use the largest size in this range that still lets the diagram fill the panel), 藍子 at the lower left corner and トリ先生 at the lower right corner; 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　代理人は、通知も受けられる？」
- A wide table that fills the full panel width. The header row is dark navy with white text and has three columns: 「肢」, 「場面」, 「肢の言い分」. The two body rows have the same pale gray fill and a dark navy outline, each text at least 24 px high, with no check mark, no cross, and no arrow.
- Body row 1: 「肢D1051」, 「代理人が合筆を申請。特別の委任はない」, 「通知を受けることができない」.
- Body row 2: 「肢D1052」, 「登記識別情報を提供できない」, 「理由を証する情報も提供する」.
- In the third column, the two strings differ; copy each exactly as given and do not change one into the other.
- A small question badge 「何が必要になる？」 with a pale gray fill and a dark navy outline sits at the upper right of the table (a question badge only, with no check mark and no cross).
- 藍子 bubble (left, spoken first): 「代理人なら、
通知も受け取れ
ますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
そこに落とし穴が
あるわよ」 with the part 「落とし穴」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　通知を受ける側と提供できない側」
- A small dark navy tag 「合筆の登記識別情報」 at the top left, with one line beside it: 「場面で、必要なものが違う」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「合筆後に通知を受ける」, a small tag 「代理人が受けるとき」, two body lines: 「特別の委任が必要」, 「なければ受けられない」, with the text 「特別の委任が必要」 highlighted with a yellow marker.
- Right card, heading 「提供できないとき」, a small tag 「失念、失効など」, two body lines: 「理由は申請情報に書けば足りる」, 「理由を証する情報は要らない」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ、そう分かれる？」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- LEFT SIDE: two stacked cards of the same size, top and bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card and one short body line, with no arrow and no connector. The cards are separated only by a small empty gap.
- Top card, heading 「肢D1051の言い分」, body 「特別の委任がなければ、通知を受けられない」, and ONE blue check mark only at the bottom of this card (no cross on this card).
- Bottom card, heading 「肢D1052の言い分」, body 「理由を証する情報も提供する」, and ONE red cross only at the bottom of this card (no check mark on this card).
- The two cards have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「委任したのに、
通知は別なんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「ええ。通知を受ける
委任は、別に要るの」 with the part 「別に要る」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「提供できない理由は、
証明が要る？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「いいえ。
理由を書けば
足りるのよ」 with the part 「書けば足りる」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇と×」
- 藍子 bubble (left, spoken first): 「通知は委任、
理由は書くだけ
なんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。
証明までは
要らないのよ」 with the part 「証明までは要らない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「代理人が通知を受けるには、特別の委任が必要（肢D1051は〇）」, 「提供できない理由は、申請情報に書けば足りる（肢D1052は×）」, 「提供できない理由を証する情報は、要らない」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「通知は特別の委任。提供できない理由は書くだけ」 with a yellow highlighter marker.
- Line 2: 「問題D1051・D1052　正解〇・×（H27-Q09イ／H27-Q09ウ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 代, 効, 登, 肢, 解, 記, 証, 請, 違 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the smaller characters are drawn within the specified size range (they must not grow and squeeze the diagram, and must not be shrunk below the range) and that nothing but the given text appears above the heads of the pictograms; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panel 1 and panel 2 contain no check mark and no cross anywhere, that the only red cross in the whole image is the one at the bottom of the bottom-left card of panel 3 and the only blue check marks are the one at the bottom of the top-left card of panel 3 and the three in the checklist of panel 4; confirm that the left card of panel 2 has the heading 「合筆後に通知を受ける」 and the right card has the heading 「提供できないとき」, never swapped; confirm that the rows of the table in panel 1 are in the order 肢D1051, 肢D1052, never swapped; confirm that the top card of panel 3 is 肢D1051の言い分 and the bottom card is 肢D1052の言い分, never swapped confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不動産登記法編4章_4コマ10_通知は特別の委任、理由は書くだけ.png`
- 途中の版・不採用の版：`不動産登記法編4章_4コマ10_通知は特別の委任、理由は書くだけ_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch4/prompt_4koma_PD-10_01_gappitsu-shikibetsu.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1の表で、2つの肢が『代理人は通知を受けられるか』『提供できない理由に証明が要るか』を問うていること、コマ2で通知を受ける場面と提供できない場面の違い、コマ3で理由（通知の受領は代理権と別／提供できない理由は書くだけ）が言える
- [ ] 工程C：構成表の全文言を記事（H27-Q09イ・ウ）・法令DB（規則62条2項、令3条12号）と突き合わせ済み。記事が令3条12号から整理している『証明は要らない』は断定せず、書くだけで足りる、の形にとどめた
- [ ] 工程C：コマ1・2に印がなく、コマ3の左は上＝✓・下＝✕の1個ずつ、コマ4だけ青✓。コマの使い方は small→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはコマ1だけで、表のためのもの
- [ ] 工程C：肝の確認：①委任による代理人が通知を受けるには、受けることができる旨の特別の委任が要る ②特別の委任がなければ、代理人は通知を受けられない ③提供できない理由は、申請情報の内容とすれば足り、証明する情報は要らない ④肢D1051は〇、D1052は×

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

## 改訂履歴（このファイルは `src/spec_4koma_PD-10_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-13 v01：新規作成（総合記事②不動産登記法編 第4章【PD-10】用。型4（2肢の対比）＋型3の理由コマ。合筆の登記識別情報について、通知を代理人が受ける場面と、提供できない場面の対比に絞った。令8条の提供の中身は入れていない）
