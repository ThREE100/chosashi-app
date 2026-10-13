# D0507 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事③「直前期の苦手論点つぶし 土地家屋調査士法編」（`note-articles/column/sokatsu-03-chousashi-hou.md`）の、論点【C1-2】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_C1-2_02.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D0507（土地家屋調査士法／調査士会・資格・その他、出典 H21-Q20イ）。正解＝×（誤った記述）。
- 記事：`note-articles/h21-mondai/q20-kekkaku-jiyuu.md` イ（司法書士の業務禁止を受けたBも、3年を経過していれば『資格を有しない』とはいえない）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】肢が『懲戒処分により司法書士の業務を禁止された』と書き、司法書士の業務禁止が欠格事由に列挙されている（法5条8号）ことを思い出させて、『資格を有しない』と答えさせる。同時に、処分の日（平成17年4月1日）と判定の日（平成21年4月1日）の2つの日付を示し、『処分の日から3年を経過しない者』という期間の限定を数えさせる。
- 【受験者の勘違い・定着していない点】（推測）①欠格事由に列挙されていれば、いつまでも資格を有しないと考える。②『3年を経過しない者』という期間の限定を読み落とす。③欠格事由の期間がどの号にあるのか（多くは3年）が定着していない。
- 【対比する制度】「欠格事由に列挙されている」⇔「処分の日から3年を経過しない者」：司法書士法による業務の禁止は、欠格事由に列挙されている（法5条8号）／ただし、処分の日から3年を経過すれば、当たらなくなる（結論が逆になる点）。リストに載っているかと、今も当たるかは別である。
- 【型の選び方】型：型5（整理カード併用。型3の理由と組み合わせ）。理由：結論の理由が『列挙されていて、かつ3年の期間内か』の2段階で、他の号にも同じ形があるので、コマ3の右側は会話1往復と、『3年で外れる欠格事由』の整理カードにした。コマ1で2つの日付を出し、コマ2で『載っている』と『3年を経過しない者』の左右の対比。壁＝『載っている＝ずっと資格がない』という短絡。
- コマごとに読者が言えること：コマ1＝平成17年4月1日に司法書士の業務禁止、平成21年4月1日現在、資格を有しないか。コマ2＝司法書士の業務禁止は欠格事由に載っているが、処分の日から3年を経過しない者だけが当たる。コマ3＝3年の限定は8号だけでなく、1号・4号〜7号にもある。コマ4＝この肢は4年が過ぎているので資格を有し、D0507は×。
- 記事の範囲：H21-Q20イ（法5条8号）。『処分の日などから3年で外れる欠格事由』の整理（1号・4号〜8号）は、総合記事③の【C1-2】の整理（法令DBで原文を確認）。日付は肢の本文（平成17年4月1日・平成21年4月1日）どおりに書いた。
- extra_refs：法5条1号（拘禁刑以上の刑に処せられ、その執行を終わり、又は執行を受けることがなくなつてから三年を経過しない者）、4号（公務員で懲戒免職の処分の日から三年）、5号（第四十二条の規定により業務の禁止の処分の日から三年）、6号（測量法の規定により登録の抹消の処分の日から三年）、7号（建築士法の規定により免許の取消しの処分の日から三年）、8号（司法書士法第四十七条の規定により業務の禁止の処分の日から三年）、2号（未成年者）、3号（破産手続開始の決定を受けて復権を得ない者）は法令DB note-articles/laws/chousashi-hou.md で原文を確認。
- 登場人物：人型は使わず、日付と処分は文字のカードで示す。
- 矢印の意味：矢印は使わない。コマ1は縦3枚のカード、コマ2は左右のカード、コマ3は上下のカードと整理カード。
- 配色：コマ1・2は印（✓✕）を付けない。コマ3の左は上＝✕、下＝✓の1個ずつ。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝side、コマ2＝none（図が主役）、コマ3＝faces（左に上下2枚のカード、右に会話2つと整理カード）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 業務禁止も、3年たてば欠格事由から外れる | 「3年たてば」を黄色マーカー |
| コマ1 見出し | ラベル | ①　業務を禁止された人は、資格がない？ | — |
| コマ1 図 | 図・カード | 平成17年4月1日　司法書士の業務の禁止の処分 / 平成21年4月1日　現在 / 調査士となる資格を有しない？ / 懲戒処分の日から、何年たっている？ | — |
| コマ1 | 藍子（左・先に話す） | 業務禁止になった人は、資格がないですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。載っているのと今当たるのは別よ | 「今当たるのは別」 |
| コマ2 見出し | ラベル | ②　載っているが、3年で外れる | — |
| コマ2 図 | 図・カード | 土地家屋調査士法5条8号 / 欠格事由は、期間つき / 欠格事由に列挙されている / 法5条8号 / 司法書士法による / 業務の禁止の処分を受けた者 / 処分の日から3年を経過しない者 / 同号の限定 / 3年を経過すれば、 / 欠格事由に当たらなくなる / この肢は、処分の日から4年たっている | — |
| コマ3 見出し | ラベル | ③　3年で外れる欠格事由 | — |
| コマ3 図 | 図・カード | 業務禁止を受けたので、今も資格がない / 肢D0507の言い分 / 3年を経過しているので、資格を有する / 処分の日から4年たっている / 3年で外れる欠格事由（法5条） / 1号　刑の執行の終了などから3年 / 4号　公務員の懲戒免職から3年 / 5号　調査士の業務禁止から3年 / 6号　測量法の登録抹消から3年 / 7号　建築士法の免許取消しから3年 / 8号　司法書士の業務禁止から3年 / 2号（未成年）・3号（破産）に3年はない | — |
| コマ3 | 藍子（左・1番目） | ほかの欠格事由も、3年で外れますか？ | — |
| コマ3 | トリ先生（右・2番目） | 多くはそう。8号は、その1つよ | 「8号は、その1つ」 |
| コマ4 見出し | ラベル | ④　結論は× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 3年たてば、資格を有するんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。期間を数えるのが決め手よ | 「期間を数える」 |
| コマ4 チェック欄 | 3項目（青✓） | 司法書士の業務禁止は、欠格事由に列挙されている（法5条8号） / ただし、処分の日から3年を経過しない者に限られる / 肢D0507は4年が過ぎているので、資格を有しないとはいえない | — |
| 結論帯 | 1行目 | 業務禁止も、処分の日から3年たてば欠格事由から外れる | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0507　正解×（H21-Q20イ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 土地家屋調査士法5条（欠格事由）1号〜8号。1号は『執行を終わり、又は執行を受けることがなくなつてから三年』、4号〜8号は『その処分の日から三年を経過しない者』。2号は未成年者、3号は破産手続開始の決定を受けて復権を得ない者で、3年の限定はない。法令DB note-articles/laws/chousashi-hou.md と照合済み

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

TITLE BANNER: text 「業務禁止も、3年たてば欠格事由から外れる」 in large bold letters; the part 「3年たてば」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　業務を禁止された人は、資格がない？」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: three SEPARATE cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a small dark navy dot at its left end (NO number, NO digit, NO letter on the dots, so that they cannot be confused with the circled panel numbers), and one dark navy text line. Do NOT draw any arrow anywhere in this panel and do NOT connect the cards; they are separated only by a small empty gap.
- Card 1: 「平成17年4月1日　司法書士の業務の禁止の処分」. Card 2: 「平成21年4月1日　現在」. Card 3: 「調査士となる資格を有しない？」.
- At the top, a small question badge in a gray fill with dark navy text 「懲戒処分の日から、何年たっている？」 (a question badge only, with no check mark and no cross).
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, spoken first): 「業務禁止になった人は、
資格が
ないですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
載っているのと
今当たるのは別よ」 with the part 「今当たるのは別」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　載っているが、3年で外れる」
- A small dark navy tag 「土地家屋調査士法5条8号」 at the top left, with one line beside it: 「欠格事由は、期間つき」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「欠格事由に列挙されている」, a small tag 「法5条8号」, two body lines: 「司法書士法による」, 「業務の禁止の処分を受けた者」.
- Right card, heading 「処分の日から3年を経過しない者」, a small tag 「同号の限定」, two body lines: 「3年を経過すれば、」, 「欠格事由に当たらなくなる」.
- Under the two cards, one wide dark navy band with large white text 「この肢は、処分の日から4年たっている」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　3年で外れる欠格事由」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 2 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 120 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 2 face icons and exactly 2 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.
- LEFT SIDE: two stacked cards of the same size, top and bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card, with no arrow and no connector. The cards are separated only by a small empty gap.
- Top card, heading 「業務禁止を受けたので、今も資格がない」, body 「肢D0507の言い分」, and ONE red cross only at the bottom of this card (no check mark on this card).
- Bottom card, heading 「3年を経過しているので、資格を有する」, body 「処分の日から4年たっている」, and ONE blue check mark only at the bottom of this card (no cross on this card).
- RIGHT SIDE, under the two speech bubbles (the two speech bubbles and their two faces stay at the top of the right side): one tall list card with a dark navy heading 「3年で外れる欠格事由（法5条）」, with the same pale gray fill and a dark navy outline, containing exactly six short rows, each with a small dark navy dot at its left end (NO digit and NO letter on the dots), with no arrow and no check mark and no cross: 「1号　刑の執行の終了などから3年」, 「4号　公務員の懲戒免職から3年」, 「5号　調査士の業務禁止から3年」, 「6号　測量法の登録抹消から3年」, 「7号　建築士法の免許取消しから3年」, 「8号　司法書士の業務禁止から3年」, with the sixth row highlighted with a yellow marker. Under the six rows, one small dark navy ribbon tag with white text 「2号（未成年）・3号（破産）に3年はない」.
- The list card is a part of the right side, and it is NOT a speech bubble. The left cards and the list card have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 2 in the conversation column; face icon at the LEFT end of its own row): 「ほかの欠格事由も、
3年で外れ
ますか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 2 in the conversation column; face icon at the RIGHT end of its own row): 「多くはそう。
8号は、
その1つよ」 with the part 「8号は、その1つ」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は×」
- 藍子 bubble (left, spoken first): 「3年たてば、
資格を有する
んですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
期間を数えるのが
決め手よ」 with the part 「期間を数える」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「司法書士の業務禁止は、欠格事由に列挙されている（法5条8号）」, 「ただし、処分の日から3年を経過しない者に限られる」, 「肢D0507は4年が過ぎているので、資格を有しないとはいえない」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「業務禁止も、処分の日から3年たてば欠格事由から外れる」 with a yellow highlighter marker.
- Line 2: 「問題D0507　正解×（H21-Q20イ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 号, 地, 建, 当, 登, 肢, 解, 過, 録, 間 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the left comparison card has only a red cross and the right card only a blue check mark; confirm that the conversation column has exactly 2 face icons and exactly 2 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`調査士法編_4コマ4_業務禁止も、3年たてば欠格事由から外れる.png`
- 途中の版・不採用の版：`調査士法編_4コマ4_業務禁止も、3年たてば欠格事由から外れる_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/03-chousashi-hou/prompt_4koma_C1-2_02_kekkaku-3nen.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で2つの日付（処分と判定）、コマ2で『欠格事由に載っている』と『3年を経過しない者だけが当たる』の対比、コマ3で3年で外れる号の整理が言える
- [ ] 工程C：構成表の全文言を記事（H21-Q20イ）・法令DBと突き合わせ済み。出題当時と今の言い方の違いは入れていない（日付は肢の本文どおり）
- [ ] 工程C：コマ1・2に印がなく、コマ3の左は上＝✕・下＝✓の1個ずつ、コマ4だけ青✓。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない
- [ ] 工程C：肝の確認：①司法書士の業務禁止は欠格事由に列挙されている（法5条8号） ②ただし、処分の日から3年を経過しない者に限られる ③平成17年4月1日から平成21年4月1日までは4年で、3年を経過している ④したがって資格を有しないとはいえない ⑤D0507は×

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

## 改訂履歴（このファイルは `src/spec_4koma_C1-2_02.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-13 v01：新規作成（総合記事③土地家屋調査士法編【C1-2】用。型5（整理カード併用）。欠格事由に列挙されているかと、今も当たるかの対比と、3年で外れる欠格事由の整理に絞った）
