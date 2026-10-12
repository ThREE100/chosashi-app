# D0995 4コマ解説図解 プロンプト（ChatGPT貼付用・v02）

- 肢：D0995（不動産登記法／建物の分割・合併・合体・滅失・変更、出典 H26-Q17オ）。正解＝〇（正しい記述）。誤解登記記録の住所が古いままでは次の登記を申請できないので、先に住所の変更の登記が要ると考える（合体による登記等では、変更を証する情報で足りることを見落とす）。
- 記事：`note-articles/h26-mondai/q17-gattai-touki.md` オ（住所変更証明情報があれば、前提の住所変更登記を経ずに合体登記等を申請できる）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】問題文が『住所に変更があった場合でも』と書き、登記記録の住所が古いままという状況を強調する。前の登記記録を最新にしてから次の登記に進むという感覚に乗せ、変更を証する情報で足りることを見落とさせる。
- 【受験者の勘違い・定着していない点】（推測）①登記名義人の住所が変わっていれば、まず住所の変更の登記が要ると覚えている。②建物の合併の登記（名義人の表示が一致しないと先に変更登記が必要）と混同する。③『変更があった事実』と『変更の登記を経ること』が別物であることが結びついていない。
- 【対比する制度】「合体による登記等」⇔「建物の合併の登記」：合体による登記等は、変更があったことを証する情報を添付すれば住所の変更の登記は不要（記事H26-Q17オ）／合併の登記は、名義人の表示が一致しないと同一人と扱われず、変更証明書等では足りず先に住所の変更の登記が必要（記事R04-Q16オ）（結論が逆になる点）。v02で、分かれ目を『名義人が同一であることが要件か』に整理し、建物の分割・土地の分筆（要件でない＝不要）と土地の合筆（要件＝必要）、表題部所有者と所有権の登記名義人（考え方は同じ）まで広げた（ユーザー指示。条文に直接書かれていない結論は、登記実務の整理として使う）。
- 【型の選び方】型：型5（整理カード併用。型3の理由説明・型1の思い込みと組み合わせ）。理由が『名義人が同一であることが要件かどうか』の整理なので、コマ3の右側は会話1往復（表題登記と所有権の登記の違い）と、合体・分割・分筆・合併・合筆の5つの整理カードにした。コマ1で思い込みを出し、コマ2で合体と合併を左右に並べ、コマ3の左を『要件が同一人か』の理由の上下カードにした。
- 記事の範囲：H26-Q17オ。記事は『この取扱いを直接定めた条文は確認できておらず、登記実務の取扱いによる理解』と書く。比較に使う合併の側は別の記事（R04-Q16オ。同じく先例に基づく実務の取扱い）。図では条番号で断定せず、『実務の取扱い』と書く。不動産登記令9条は記事が参考として触れるだけなので図に入れない。
- extra_refs：R04-Q16オ（note-articles/r4-mondai/q16-tatemono-gappei.md）：合併に係る建物の所有権の登記名義人の表示が一致していないときは、同一人とは取り扱われず、変更証明書等を提供して申請することもできない（条文に明記がなく、先例に基づく実務の取扱い）。この肢の記事ではなく別の記事の結論なので、ユーザーに伝える。
- v02の拡張（ユーザー指示）：①なぜ合体は不要で合併は必要か＝合併は『表題部所有者又は所有権の登記名義人が相互に異ならない』ことが要件（法56条2号。土地は法41条3号）で、住所が古いと同一人と言えない／合体は合体後の建物を新たに表題登記するもので（法49条）、合体前の登記は抹消され、所有者が違っても申請でき、同一人かを確かめる要件がない。②建物の分割・土地の分筆は、同じ名義人の1つの登記記録を分けるだけで、同一人かを確かめる場面がないので、変更を証する情報で足りる。土地の合筆は合併と同じで先に変更登記。③表題部所有者と所有権の登記名義人：法56条2号・41条3号は『表題部所有者又は所有権の登記名義人』を並べて同一人を求めるので、考え方は同じ（違うのは誰が申請するか＝法49条1項各号）。②③の分割・分筆・合筆の結論は、記事にも法令DBにも直接の記述がなく、登記実務の整理（ユーザーに伝える）。コマ3は右側が会話1往復（顔2つ）と5つの整理カード（型5。この肢のコマ3の右の会話は4つではなく2つ）。
- 登場人物：人型は使わず、建物・土地・登記は文字のカードで示す。
- 矢印の意味：矢印は使わない。コマ1は図（カード）、コマ2は左右のカード、コマ3は上下のカード。
- 配色：コマ1・2は印（✓✕）を付けない。コマ3は上＝✕、下＝✓の1個ずつ。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝side、コマ2＝none（図が主役）、コマ3＝faces（左に上下2枚のカード、右に会話4つの縦並び）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D0995～H26-Q17オ～

## note記事の冒頭文

合体前の建物の所有権の登記名義人の住所に変更がありましたが、登記記録の住所はそのままです。住所の変更の登記をしないで、変更があったことを証する情報を添付して、合体による登記等を申請できるのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（平成26年度　第17問　オ）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 合体では、住所変更の登記なしで申請できる | 「登記なしで申請できる」を黄色マーカー |
| コマ1 見出し | ラベル | ①　住所が古いままなら、先に変更登記？ | — |
| コマ1 図 | 図・カード | 合体前の建物の名義人が、引っ越した / 登記記録の住所は、古いまま / 住所変更の登記をせず、合体による登記等を申請したい / 申請できる？ | — |
| コマ1 | 藍子（左・先に話す） | 住所が古いなら、先に変更登記ですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。事実と登記は別物よ | 「事実と登記は別物」 |
| コマ2 見出し | ラベル | ②　なぜ、合体は不要で合併は必要？ | — |
| コマ2 図 | 図・カード | 分かれ目は、同一人かを確かめる必要があるか / 住所が古いままのとき / 合体による登記等 / 法49条 / 合体後は、新しく表題登記 / 現在の住所を証する情報を添付 / 所有者が違っても申請できる / 建物の合併の登記 / 法56条2号 / 名義人が同一であることが要件 / 住所が古いと、同一人と言えない / 先に住所変更の登記が必要 / この肢は、同一人かを問わない合体 | — |
| コマ3 見出し | ラベル | ③　分割・分筆・合筆は？ | — |
| コマ3 図 | 図・カード | 要件が同一人（合併・合筆） / 住所が古いと同一人と言えない。先に変更登記 / 要件が同一人でない（合体・分割・分筆） / 現在の住所を証する情報で足りる / 住所が古いままのとき、変更登記は？ / 建物の合体　不要 / 建物の分割　不要 / 土地の分筆　不要 / 建物の合併　先に変更登記 / 土地の合筆　先に変更登記 / 分かれ目は、要件が同一人か | — |
| コマ3 | 藍子（左・1番目） | 表題登記と所有権の登記で違いますか？ | — |
| コマ3 | トリ先生（右・2番目） | 違わないの。条文は両方を並べるのよ | 「両方を並べる」 |
| コマ4 見出し | ラベル | ④　結論は〇 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 合体は、同一人かを問わないんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。できると書けば〇よ | 「できると書けば〇」 |
| コマ4 チェック欄 | 3項目（青✓） | 合併・合筆は、同一人が要件。先に住所変更の登記 / 合体・分割・分筆は、同一人が要件でない。証する情報で足りる / 表題部所有者でも所有権の登記名義人でも、考え方は同じ | — |
| 結論帯 | 1行目 | 合体による登記等は、変更を証する情報があれば申請できる | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0995　正解〇（H26-Q17オ） | — |

## 記事に無い条文（ユーザー指示で追加）

- R04-Q16オ（別の記事 note-articles/r4-mondai/q16-tatemono-gappei.md）の結論：合併に係る建物の所有権の登記名義人の表示が一致していないときは、同一人とは取り扱われず、変更証明書等を提供して申請することもできないとされる。条文に明記がなく、先例に基づく実務の取扱い
- H26-Q17オの結論（合体による登記等では、変更を証する情報で足りる）も、記事は『直接定めた条文は確認できておらず、登記実務の取扱いによる理解』と書く。2つの結論が逆になること自体は、2つの記事の記述から言えるが、条文で対比できるわけではない（ユーザーに伝える）

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

TITLE BANNER: text 「合体では、住所変更の登記なしで申請できる」 in large bold letters; the part 「登記なしで申請できる」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　住所が古いままなら、先に変更登記？」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: three SEPARATE cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a small dark navy dot at its left end (NO number, NO digit, NO letter on the dots, so that they cannot be confused with the circled panel numbers), and one dark navy text line. Do NOT draw any arrow anywhere in this panel and do NOT connect the cards; they are separated only by a small empty gap.
- Card 1: 「合体前の建物の名義人が、引っ越した」. Card 2: 「登記記録の住所は、古いまま」. Card 3: 「住所変更の登記をせず、合体による登記等を申請したい」.
- At the top, a small question badge in a gray fill with dark navy text 「申請できる？」 (a question badge only, with no check mark and no cross).
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, spoken first): 「住所が古いなら、
先に変更登記
ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
事実と登記は
別物よ」 with the part 「事実と登記は別物」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　なぜ、合体は不要で合併は必要？」
- A small dark navy tag 「分かれ目は、同一人かを確かめる必要があるか」 at the top left, with one line beside it: 「住所が古いままのとき」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross. Both headings and all body text use one single dark navy color, with emphasis only by a yellow marker.
- Left card, heading 「合体による登記等」, a small tag 「法49条」, three body lines: 「合体後は、新しく表題登記」, 「現在の住所を証する情報を添付」, 「所有者が違っても申請できる」.
- Right card, heading 「建物の合併の登記」, a small tag 「法56条2号」, three body lines: 「名義人が同一であることが要件」, 「住所が古いと、同一人と言えない」, 「先に住所変更の登記が必要」.
- Under the two cards, one wide dark navy band with large white text 「この肢は、同一人かを問わない合体」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　分割・分筆・合筆は？」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 2 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 120 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 2 face icons and exactly 2 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.
- LEFT SIDE: two stacked cards of the same size, top and bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card, with no arrow and no connector. The cards are separated only by a small empty gap.
- Top card, heading 「要件が同一人（合併・合筆）」, body 「住所が古いと同一人と言えない。先に変更登記」, and ONE red cross only at the bottom of this card (no check mark on this card).
- Bottom card, heading 「要件が同一人でない（合体・分割・分筆）」, body 「現在の住所を証する情報で足りる」, and ONE blue check mark only at the bottom of this card (no cross on this card).
- RIGHT SIDE, under the two speech bubbles (the two speech bubbles and their two faces stay at the top of the right side): one tall list card with a dark navy heading 「住所が古いままのとき、変更登記は？」, with the same pale gray fill and a dark navy outline, containing exactly five short rows, each with a small dark navy dot at its left end (NO digit and NO letter on the dots, so that they cannot be confused with the circled panel numbers), with no arrow and no check mark and no cross: 「建物の合体　不要」, 「建物の分割　不要」, 「土地の分筆　不要」, 「建物の合併　先に変更登記」, 「土地の合筆　先に変更登記」. The row 「建物の合体　不要」 is highlighted with a yellow marker. Under the five rows, one small dark navy ribbon tag with white text 「分かれ目は、要件が同一人か」.
- The list card is a part of the right side, and it is NOT a speech bubble. The left cards and the list card have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 2 in the conversation column; face icon at the LEFT end of its own row): 「表題登記と
所有権の登記で
違いますか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 2 in the conversation column; face icon at the RIGHT end of its own row): 「違わないの。
条文は両方を
並べるのよ」 with the part 「両方を並べる」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇」
- 藍子 bubble (left, spoken first): 「合体は、
同一人かを問わない
んですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。できると
書けば〇よ」 with the part 「できると書けば〇」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「合併・合筆は、同一人が要件。先に住所変更の登記」, 「合体・分割・分筆は、同一人が要件でない。証する情報で足りる」, 「表題部所有者でも所有権の登記名義人でも、考え方は同じ」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「合体による登記等は、変更を証する情報があれば申請できる」 with a yellow highlighter marker.
- Line 2: 「問題D0995　正解〇（H26-Q17オ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 号, 地, 建, 所, 権, 物, 登, 肢, 解, 記, 証, 請, 違, 録 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the left comparison card has only a red cross and the right card only a blue check mark; confirm that the word 「合体」 is spelled exactly like this everywhere (never 「合併」); confirm that the conversation column has exactly 2 face icons and exactly 2 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 住所が変わったら | 薄い黄色のマーカー |
| タイトル2行目 | 変更登記は先？ | 「先？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D0995　H26-Q17オ | — |

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
住所が変わったら
Line 2 is larger; the phrase 先？ is red-orange and the rest is dark navy:
変更登記は先？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D0995　H26-Q17オ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a small moving truck beside a house with a blank address plate, no text
Right side: two small building icons merging into one building with a document sheet, no text

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written (cartoon expression marks such as ！ and ？ beside the characters' faces are decoration, are allowed, and are not extra text); scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 住, 所, 変, 更, 登, 記, 先, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere. Never delete, redo, or regenerate anything because of an expression mark or a symbol beside a character; deliver the first image as it is.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D0995～H26-Q17オ～.png |
| 見出し画像（採用版） | 4コマ解説図解D0995～H26-Q17オ～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D0995～H26-Q17オ～_v01.png ／ 4コマ解説図解D0995～H26-Q17オ～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0995_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で問いの場面、コマ2で結論が分かれる2つの場面の対比、コマ3で理由、が言える
- [ ] 工程C：構成表の全文言を記事・法令DBと突き合わせ済み。出題当時と今の言い方の違いは入れていない
- [ ] 工程C：コマ1・2に印がなく、コマ3は上＝✕・下＝✓の1個ずつ、コマ4だけ青✓の暗記3点。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない
- [ ] 工程C：肝の確認：①合体前の建物の所有権の登記名義人の住所に変更があっても、変更があったことを証する情報を添付すれば、住所の変更の登記をせず合体による登記等を申請できる②『変更があった事実』と『変更の登記を経ること』は別③この取扱いを直接定めた条文は確認できず、登記実務の取扱い（記事）④合併の登記は、名義人の表示が一致しないと先に住所変更の登記が必要（R04-Q16オ。実務の取扱い）⑤肢D0995は『住所の変更の登記をすることなく…申請することができる』なので〇⑥v02：合併・合筆は名義人が同一が要件なので先に変更登記、合体・分割・分筆は要件でないので不要（分割・分筆・合筆は登記実務の整理）⑦表題部所有者と所有権の登記名義人で考え方は同じ（法56条2号・41条3号が両方を並べる）

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

## 改訂履歴（このファイルは `manga_specs.py` から生成。直すときは設計データを直して再生成する）

- 2026-10-12 v01：新規作成（型3の理由説明＋型1の思い込み。合体による登記等と建物の合併の登記の対比と、事実と登記は別物という理由に絞った）
- 2026-10-12 v01の画像を検品：本文・台詞・チェック欄・フッターは構成表と一致、キャラの位置と顔の数（4つ）もよし。軽微な点：コマ2のカードの見出しが青と緑、結論の文字が両方赤で、色が意味を持つように見える（カードは同じ薄い灰色・濃紺の枠にそろえ、強調は黄色マーカーだけにする規則に反する）
- 2026-10-12 v02：ユーザー指示。なぜ合体は不要で合併は必要か（同一人かを確かめる要件の有無。法56条2号・法49条）、建物の分割・土地の分筆（要件でないので不要）・土地の合筆（要件なので必要）、表題部所有者と所有権の登記名義人（考え方は同じ）まで広げた。コマ3を型5（整理カード併用）にし、右側に5つの整理カードを置いた。コマ2のカードは同じ色にそろえた。条文に直接書かれていない結論は登記実務の整理（ユーザーに伝える）
