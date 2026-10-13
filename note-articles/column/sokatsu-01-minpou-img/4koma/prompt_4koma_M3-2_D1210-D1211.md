# D1210・D1211 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

- 肢：D1210・D1211（民法／物権変動・対抗要件、出典 H29-Q02イ・ウ）。正解＝D1210＝〇・D1211＝×。どちらも『登記なくして所有権を主張することができる』と言う肢だが、D1210は時効完成の前に登記を得た買主が相手なので登記は不要で〇、D1211は解除のあとに登記を得た第三者が相手なので登記が必要で×。誤解（一問一答での誤答の履歴は図に入れない。解除や時効の前後という時点の取り違えが推測される）。
- 記事：`note-articles/h29-mondai/q02-bukken-hendou.md` イ（登記後に時効が完成した占有者は、当事者に類似する関係にある買主に、登記なくして所有権を主張できる）とウ（解除後に現れた第三者とは対抗関係で、解除した者にも登記が必要）を、第三者が現れた時期で対比する。総合記事の【M3-2】と、時効完成の後の第三者は対抗関係（M1-6の整理）も添える
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】2肢とも文の骨組みが『…した場合、○○は、△△に対し、登記なくして当該土地の所有権を主張することができる』で同じに見える。D1211は解除という『戻る』感覚（解除したのだから自分のものに戻った）に乗せて、登記は要らないと思わせる。D1210は、買主が先に登記を備えたことに目を引かれて、登記を先に備えた買主が勝つと思わせる。実際は、第三者が現れた時期（解除のあと／時効完成の前）で結論が逆になる。
- 【受験者の勘違い・定着していない点】（推測）①『登記は先に備えた方が勝つ』という一般ルールを、解除にも時効にも同じように当てはめる（D1210で、先に登記した買主が勝つと考える）。②解除のあとに出てきた第三者を、解除前の当事者のように考えて、解除した売主は登記なしで主張できると考える（D1211）。③第三者が原因（解除・時効完成）の前に現れたのか、あとに現れたのかを、先に確かめる習慣がない。
- 【対比する制度】「解除のあとの第三者」⇔「完成の前に登記を得た買主」：解除のあとに現れた第三者とは対抗関係で、解除した売主も登記が要る。時効完成の前に登記を得た買主とは当事者に類似する関係で、占有者は登記なしで所有権を主張できる（結論が逆になる点）。
- 【型の選び方】型：型4（＋型3の理由）。理由…壁＝2肢は同じ問のイ・ウで、『登記なくして主張できる』という同じ言い方なのに、片方は〇、片方は×。別々の場面（日付が共通でない）なので、コマ1は時系列でなく2つの出来事の並びを左右のカードで見せる（型4の比較の形）。コマ2＝分かれ目の対比（解除のあと／時効完成の前。左右のカード）、コマ3＝『なぜ』を2枚の理由カード（上下）に分け、会話は罠の指摘に使う（型3の理由）、コマ4＝2肢の整理。単独版のD0520（取消し前）・D1209（順次譲渡）と重ならないよう、取消しは図に入れず、解除と時効の2つに絞った。
- 記事の範囲：H29-Q02イ（Ａの土地をＣが占有して取得時効が進行している途中で、土地がＡからＢへ譲渡されて登記も移った後に時効が完成した場合、ＣとＢは物権変動の当事者に類似する関係に立つ。Ｂは民法177条の第三者にあたらず、Ｃは登記なくして時効取得をＢに対抗できる）、H29-Q02ウ（解除のあとに土地を買って登記を備えた第三者Ｃが現れたとき、解除した売主Ａと第三者Ｃは対抗関係に立つ。Ｂを起点にＢ→Ａ〈解除による復帰的物権変動〉とＢ→Ｃの二重譲渡があったのと同じに扱われるため、Ａは登記を備えなければＣに対抗できない）。総合記事【M3-2】の中身の整理に同じ。
- extra_refs：条文は民法177条（法令DB note-articles/laws/minpou-1-soukyoku-bukken.md 第177条で原文確認済み）。図には条文番号を入れていない。時効完成の後に現れた第三者とは対抗関係（コマ2の帯）は、総合記事の【M1-6】（時効取得と登記）の整理による（元記事H21-Q01イ）。判例の立場で、条文に直接の定めはない。
- 図に入れないもの：同じ問のア（他人物売買）・エ（不法占拠者）・オ（登記申請を受任していた者）。解除の前に現れた第三者（民法545条1項ただし書）と取消し（D0520）は、肢の結論を決めないので入れない。
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない。肢により記号の役割が違う（Ｃは、D1211では解除のあとにＢから買った人、D1210では占有している人）ため、人物は文字ラベル『売主』『買主』『あとで買った人』『占有者』で示す。コマ1の左右のカードで紹介してから使う。
- 矢印の意味：矢印は使わない。コマ1は左右のカード（上から下に出来事の順）、コマ2は左右のカード、コマ3は上下2枚のカード。
- 配色：コマ1〜3は印（✓✕）を付けない（可否は文字で書く。肢の〇×と印の向きが重なって紛らわしくなるのを避ける）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠・濃紺の文字、リボンは濃紺の地に白文字、強調は黄色マーカーだけ。
- コマの使い方：コマ1＝small（左右のカードを横いっぱいに見せるので、キャラは小さく）、コマ2＝none（左右2枚のカードが主役。キャラも吹き出しもなし）、コマ3＝faces（左に上下2枚の理由カード、右に会話の縦並び。会話4つ＝顔4つ＝4行）、コマ4＝既定（暗記3点と結論）。
- コマごとに読者が言えること：コマ1＝2肢はどちらも売主が買主に売って登記を移した土地の話だが、片方は解除、片方は時効で、第三者の出てくる時期が違う。コマ2＝解除のあとの第三者とは対抗関係（売主も登記が要る）、時効完成の前に登記を得た買主には占有者は登記なしで主張できる。コマ3＝解除は二重譲渡のように扱われるから対抗関係、時効は占有者と買主が当事者に類似する関係だから登記が要らない。コマ4＝D1210は〇、D1211は×。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D1210・D1211～H29-Q02イ・ウ～

## note記事の冒頭文

売主が買主に土地を売って登記を移したあと、売主が契約を解除した場合と、占有者の取得時効が完成した場合を比べます。それぞれ、売主と占有者は、登記なしで所有権を主張できるのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（平成29年度　第2問　イ・ウ）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 第三者がいつ出たかで、登記の要否が逆 | 「いつ出たか」を黄色マーカー |
| コマ1 見出し | ラベル | ①　解除と時効、出来事の順 | — |
| コマ1 図 | 図・カード | 売主が買主に売り、買主に登記を移したあと / 肢D1211　解除 / 売主が、契約を解除する / 解除のあとに、買主があとで買った人に売る / あとで買った人に登記が移る / 売主は、登記なしで主張できる？ / 肢D1210　時効 / 占有者が、その土地を占有している / 買主に登記が移る（時効の完成の前） / あとで、占有者の取得時効が完成する / 占有者は、登記なしで主張できる？ | — |
| コマ1 | 藍子（左・先に話す） | どちらも登記なしで主張できますよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。第三者がいつ出たかを見るのよ | 「いつ出たか」 |
| コマ2 見出し | ラベル | ②　解除のあとか、完成の前か | — |
| コマ2 図 | 図・カード | 分かれ目 / 第三者が出てきたのは、原因のあとか前か / あとか前か / 解除のあとの第三者（肢D1211） / 売主と第三者は、対抗関係 / 先に登記をした方が勝つ / 売主も、登記が要る / 完成の前に登記を得た買主（肢D1210） / 占有者と買主は、当事者に類似 / 買主は、第三者にあたらない / 占有者は、登記なしで主張できる / 時効完成のあとに現れた第三者とは、対抗関係 | — |
| コマ3 見出し | ラベル | ③　なぜ、結論が逆になるのか | — |
| コマ3 図 | 図・カード | なぜ、解除のあとは対抗関係なのか / 買主から売主へ戻る動きと / 買主からあとで買った人への売却が / 二重譲渡のように扱われるから / なぜ、完成の前の買主は登記が要らないのか / 占有者と買主は、当事者に類似する関係 / だから、買主は第三者にあたらない | — |
| コマ3 | 藍子（左・1番目） | 解除したら、売主に戻るのでは？ | — |
| コマ3 | トリ先生（右・2番目） | 戻る動きと売却が、二重譲渡の形になるの | 「二重譲渡の形」 |
| コマ3 | 藍子（左・3番目） | 時効は、先に登記した買主が勝つのでは？ | — |
| コマ3 | トリ先生（右・4番目） | 買主は当事者に類似。登記は要らないのよ | 「当事者に類似」 |
| コマ4 見出し | ラベル | ④　2つの肢の答え | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | まず、第三者が出た時期を見ます！ | — |
| コマ4 | トリ先生（右・答える） | そう。解除のあとか、完成の前かよ | 「解除のあとか、完成の前か」 |
| コマ4 チェック欄 | 3項目（青✓） | 解除のあとの第三者とは対抗関係。解除した売主も登記が要る（D1211は×） / 時効完成の前に登記を得た買主には、占有者は登記なしで主張できる（D1210は〇） / 原因（解除・時効完成）に対して、第三者が出た時期を先に確かめる | — |
| 結論帯 | 1行目 | 解除のあとは登記が要る。完成の前は要らない | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1210・D1211　正解〇・×（H29-Q02イ・ウ） | — |

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

TITLE BANNER: text 「第三者がいつ出たかで、登記の要否が逆」 in large bold letters; the part 「いつ出たか」 has a yellow highlighter marker.

PANEL 1 (puzzled, curious mood; both characters appear SMALLER than in the other panels, only because this panel's diagram or text needs the room (each about 150 px tall; never below 110 px and never more than one third of the panel height; use the largest size in this range that still lets the diagram fill the panel), 藍子 at the lower left corner and トリ先生 at the lower right corner; 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　解除と時効、出来事の順」
- A wide diagram that fills the full panel width: two cards of the same size side by side, left and right, each with the same pale gray fill and a dark navy outline, each text at least 24 px high, with no check mark, no cross, and no arrow. A small dark navy tag 「売主が買主に売り、買主に登記を移したあと」 sits above the two cards.
- Left card: heading 「肢D1211　解除」, three lines in order from top to bottom 「売主が、契約を解除する」, 「解除のあとに、買主があとで買った人に売る」 and 「あとで買った人に登記が移る」, and a question line 「売主は、登記なしで主張できる？」.
- Right card: heading 「肢D1210　時効」, three lines in order from top to bottom 「占有者が、その土地を占有している」, 「買主に登記が移る（時効の完成の前）」 and 「あとで、占有者の取得時効が完成する」, and a question line 「占有者は、登記なしで主張できる？」.
- The two cards have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- 藍子 bubble (left, spoken first): 「どちらも登記なしで
主張できますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。第三者が
いつ出たかを見るのよ」 with the part 「いつ出たか」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　解除のあとか、完成の前か」
- A small dark navy tag 「分かれ目」 at the top left with a line beside it: 「第三者が出てきたのは、原因のあとか前か」, with the part 「あとか前か」 in a yellow highlighter marker.
- Two large cards of the same size side by side, left and right, each with the same pale gray fill, a dark navy outline, and a dark navy heading placed fully INSIDE the card, with no check mark, no cross, and no arrow anywhere in this panel. Only a small empty gap separates the two cards, with nothing drawn between them.
- Left card: heading 「解除のあとの第三者（肢D1211）」, three short body lines 「売主と第三者は、対抗関係」, 「先に登記をした方が勝つ」 and 「売主も、登記が要る」.
- Right card: heading 「完成の前に登記を得た買主（肢D1210）」, three short body lines 「占有者と買主は、当事者に類似」, 「買主は、第三者にあたらない」 and 「占有者は、登記なしで主張できる」.
- At the bottom, one wide dark navy band with white text 「時効完成のあとに現れた第三者とは、対抗関係」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ、結論が逆になるのか」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Two cards stacked from top to bottom, both the same size, each with the same pale gray fill, a dark navy outline, and a dark navy heading placed fully INSIDE the card, with no check mark and no cross. The two cards are separated only by a small empty gap, with nothing drawn between them.
- Top card: heading 「なぜ、解除のあとは対抗関係なのか」, three short body lines 「買主から売主へ戻る動きと」, 「買主からあとで買った人への売却が」 and 「二重譲渡のように扱われるから」.
- Bottom card: heading 「なぜ、完成の前の買主は登記が要らないのか」, two short body lines 「占有者と買主は、当事者に類似する関係」 and 「だから、買主は第三者にあたらない」.
- The two cards have clearly different texts; the texts are NOT identical.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「解除したら、
売主に戻るのでは？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「戻る動きと売却が、
二重譲渡の形になるの」 with the part 「二重譲渡の形」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「時効は、先に登記した
買主が勝つのでは？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「買主は当事者に類似。
登記は要らないのよ」 with the part 「当事者に類似」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　2つの肢の答え」
- 藍子 bubble (left, spoken first): 「まず、第三者が
出た時期を見ます！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。解除のあとか、
完成の前かよ」 with the part 「解除のあとか、完成の前か」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「解除のあとの第三者とは対抗関係。解除した売主も登記が要る（D1211は×）」, 「時効完成の前に登記を得た買主には、占有者は登記なしで主張できる（D1210は〇）」, 「原因（解除・時効完成）に対して、第三者が出た時期を先に確かめる」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「解除のあとは登記が要る。完成の前は要らない」 with a yellow highlighter marker.
- Line 2: 「問題D1210・D1211　正解〇・×（H29-Q02イ・ウ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 効, 占, 地, 売, 対, 張, 当, 抗, 渡, 登, 肢, 解, 記, 譲, 買 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the word 「第三者」 is spelled exactly like this everywhere (never 「時三者」); confirm that the smaller characters are drawn within the specified size range (they must not grow and squeeze the diagram, and must not be shrunk below the range) and that nothing but the given text appears above the heads of the pictograms; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panel 1, panel 2 and panel 3 contain no check mark and no cross anywhere, and that the only blue check marks in the whole image are the three in the checklist of panel 4; confirm that in panel 1 the LEFT card heading is 「肢D1211　解除」 and the RIGHT card heading is 「肢D1210　時効」, never swapped; confirm that in panel 2 the LEFT card heading is 「解除のあとの第三者（肢D1211）」 and the RIGHT card heading is 「完成の前に登記を得た買主（肢D1210）」, never swapped; confirm that in panel 3 the TOP card heading is 「なぜ、解除のあとは対抗関係なのか」 and the BOTTOM card heading is 「なぜ、完成の前の買主は登記が要らないのか」, never swapped confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 解除と時効のあと | 薄い黄色のマーカー |
| タイトル2行目 | 登記なしで言える？ | 「登記なしで言える？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D1210・D1211　H29-Q02イ・ウ | — |

### 見出し画像プロンプト本体

```text
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the two characters at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): follow the attached character-specification images exactly and do not redesign them. トリ先生 is the chubby bird teacher (round red glasses, blue shirt, red neckerchief), placed at the lower left of center. 藍子 is the young woman exam candidate (long wavy brown hair, pinstriped light-blue blouse with rolled sleeves, navy pencil skirt, no jacket), placed at the lower right of center. POSES ARE NOT FIXED: do not copy any pose from the attached images or from earlier header images; let each character take a free, natural pose of your own choosing that fits the topic and suits the character (for example standing, sitting, leaning, gesturing, or holding a small prop), and choose a different pose each time this image is generated. Keep both characters fully visible, with their faces clear of the title text, and keep 藍子's hairstyle exactly as in the attached images. Keep 藍子's human anatomy strictly correct: exactly one head, one torso, two arms (one left, one right) and two hands in total, each hand with exactly five fingers; never draw extra arms, hands, or fingers, floating or duplicated hands, arms not growing from the shoulders, or fused hands; check that every shoulder, elbow, and wrist connects naturally.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and the Arabic numeral 4; the only Latin letters and digits allowed are those in the subtitle exactly as written below. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it:
解除と時効のあと
Line 2 is larger; the phrase 登記なしで言える？ is red-orange and the rest is dark navy:
登記なしで言える？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D1210・D1211　H29-Q02イ・ウ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a wooden fence around a small plot of land with a blank paper contract beside it
Right side: a wall calendar with blank pages and a small registry book with a rubber stamp

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written (cartoon expression marks such as ！ and ？ beside the characters' faces are decoration, are allowed, and are not extra text); scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 解, 除, 時, 効, 登, 記, 言, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere. Never delete, redo, or regenerate anything because of an expression mark or a symbol beside a character; deliver the first image as it is.
```

### 見出し画像の検品
- [ ] 画像内の文字は、タイトル2行とサブタイトルだけ。文言が上の表と一字一句一致、簡体字・余計な文字なし
- [ ] トリ先生が左下、藍子が右下で向き合い、顔がタイトルに重ならない。藍子の髪型が参照画像どおり
- [ ] 左右のテーマの場面に文字がなく、タイトル・キャラより目立たない
- [ ] 背景が不透明（透過・チェッカーボードなし）、中央でトリミングしても主要要素が切れない

## 画像ファイル名（名づけルール）

ChatGPTで生成した画像は、保存するときに次の名前へ変更する（拡張子は生成された形式のまま：png・webp など）。`MANGA_RULES.md` の「画像ファイル名」に従う。

| 画像 | ファイル名 |
|---|---|
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D1210・D1211～H29-Q02イ・ウ～.png |
| 見出し画像（採用版） | 4コマ解説図解D1210・D1211～H29-Q02イ・ウ～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D1210・D1211～H29-Q02イ・ウ～_v01.png ／ 4コマ解説図解D1210・D1211～H29-Q02イ・ウ～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D1210-D1211_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で、2肢とも売主が買主に売って登記を移したあとの話で、D1211は解除のあとに買主から買った人、D1210は時効が完成する占有者が出てくると言える。コマ2で、解除のあとの第三者は対抗関係、時効完成の前に登記を得た買主には登記なしで主張できると言える。コマ3で、その理由（二重譲渡のように扱われる／当事者に類似する関係）が言える
- [ ] 工程C：肝の確認：①解除のあとに現れた第三者とは対抗関係で、解除した売主も登記が要る（D1211は×） ②時効完成の前に登記を得た買主には、占有者は登記なしで主張できる（D1210は〇） ③時効完成の後に現れた第三者とは対抗関係（帯） ④第三者が現れた時期を先に確かめる
- [ ] 工程C：構成表の全文言を記事（H29-Q02イ・ウ）と突き合わせ：『対抗関係』『二重譲渡のように扱われる』『復帰』『当事者に類似する関係』『第三者にあたらない』『登記なくして』。総合記事【M3-2】・【M1-6】の整理と一致。民法177条は法令DBで原文確認済み
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方が隣り合うコマで同じにならない（small→none→faces→既定）。コマ3の顔アイコンは、会話の数と同じ4つ。個人の演習結果・回答履歴は図に入れていない

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

## v01：新規作成（2026-10-13）。総合記事（民法編）【M3-2】用。型4＋型3の理由。解除と時効の2肢を『第三者が現れた時期』の軸で対比した。取消し（D0520）は既存の単独版があるので図に入れていない。ChatGPTでの画像生成・検品はまだ。

## 改訂履歴（このファイルは `manga_specs.py` から生成。直すときは設計データを直して再生成する）

- 2026-10-13 v01：初版（総合記事の図解・4コマの一括作成）
