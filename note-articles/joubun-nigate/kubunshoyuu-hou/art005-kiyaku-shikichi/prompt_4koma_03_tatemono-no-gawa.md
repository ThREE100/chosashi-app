# D1278・D1368・D1796 4コマ解説図解 プロンプト（ChatGPT貼付用・v02）

> **このファイルについて**
>
> - 条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、区分所有法 第5条（規約敷地）の記事に差し込む4コマ（3本目）のプロンプトです。類似の誤解をまとめて、1本の4コマにしました。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`（mainブランチ））に従い、同フォルダの生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-09）。下の「作成時の品質ゲート」にある `tools/drill/manga/` のパスは、そのブランチ上のパスです。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D1278・D1368・D1796（不動産登記法／区分建物・敷地権・共用部分、出典 H29-Q15イ／H30-Q11⑦誤／R04-Q18イ）。正解＝D1278・D1368＝×（誤った記述）／D1796＝〇。
- 記事：`note-articles/r4-mondai/q18-shikichiken.md` R04-Q18イ（規約敷地になったら、建物の表題部の変更の登記を1か月以内に申請）を軸に、H29-Q15イ（申請することを要しない、は誤り）・H30-Q11⑦誤（敷地権である旨の登記は、申請ではなく職権）を対比
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【型の選び方】型：型4（複数肢の対比）＋型3（理由）。理由：3肢とも、規約敷地が生じた同じ場面から出ていて、誤りは『建物の側を、申請を要しないとする』（D1278）と『土地の側を、申請によるとする』（D1368）の2通りに分かれる。壁は、2つの登記のうち、どちらが申請でどちらが職権かが結びつかないことと、その理由が見えないこと。コマ1で3肢の言い分を並べ、コマ2で2つの登記を申請と職権に仕分け、コマ3で理由を示す。
- 【出題者のひっかけ】『規約により敷地とされた』『敷地権である旨の登記』と、土地の側の言葉で場面を書き、建物の側の登記が必要なことを見えにくくする（D1278は『申請することを要しない』、D1796は『申請しなければならない』と、同じ場面で逆の言い方）。D1368は『申請により』と書いて、登記官が職権でする登記を、申請でする登記に見せる（記事 R04-Q18イ、H29-Q15イ、H30-Q11⑦誤）。
- 【受験者の勘違い・定着していない点】規約敷地は土地の話だから建物の登記は要らない、と思う。または、土地の側の敷地権である旨の登記も申請で行うと思う。実際は、建物の側が表題部の変更の登記を申請し（法51条1項）、土地の側の敷地権である旨の登記は登記官が職権でする（法46条）。
- 【対比する制度】「建物の側」⇔「土地の側」：建物の側は、敷地権の表示をする表題部の変更の登記を、変更があった日から1か月以内に申請する／土地の側は、敷地権である旨の登記を、登記官が職権でする。同じ場面でも、申請か職権かが逆になる。
- 理由の出典：敷地権は建物の表題部の登記事項（法44条1項9号。記事 note_art005 の部品2）。登記事項に変更があれば、表題部所有者又は所有権の登記名義人が1か月以内に変更の登記を申請する（法51条1項。44条1項各号のうち第2号と第6号を除く）。土地の側は、表示に関する登記のうち敷地権について表題部に最初に登記をするときに、登記官が職権で敷地権である旨の登記をする（法46条）。
- D1796の単独版（申請人・期限・登記の4点の押さえどころ）とは切り口を変えた。この4コマは、3肢の言い分を並べて、誤りが2通りあることと、申請と職権を分ける理由を示す。
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない。建物・土地はアイコンと文字ラベルで示す。
- 矢印の意味：矢印は使わない。コマ1は縦に積んだカード、コマ2は左右のカード、コマ3は縦に積んだカード。
- 配色：コマ1〜3は印（✓✕）を付けない（申請・職権は文字で書く）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラの大きさ）：不必要に小さくしない。コマ1＝side（キャラは通常サイズで左右の端、図は中央に事案カード1枚と肢のカード3枚）、コマ2＝none（図が主役。左右の大きなカード）、コマ3＝faces（左に理由のカード3枚、右に会話4つの縦並び）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 建物の側は申請、土地の側は職権 | 「土地の側は職権」を黄色マーカー |
| コマ1 見出し | ラベル | ①　同じ場面の3つの言い分 | — |
| コマ1 図 | 図・カード | 規約で土地が敷地になり、敷地権が生じた / 肢D1796 / 建物の表題部の変更の登記を / 1か月以内に申請しなければならない / 肢D1278 / 申請することを要しない / 肢D1368 / 土地の敷地権である旨の登記を / 登記官が、申請によりする / 肢の言い分は、どこが違う？ | — |
| コマ1 | 藍子（左・先に話す） | どれも規約敷地の肢ですよね？ | — |
| コマ1 | トリ先生（右・答える） | 同じ場面でも、申請か職権かで分かれるのよ | 「申請か職権か」 |
| コマ2 見出し | ラベル | ②　申請する登記と、職権の登記 | — |
| コマ2 図 | 図・カード | 出題者のねらい / 同じ場面の2つの登記を、申請と職権に分けられるか / 建物の側 / 敷地権の表示をする、表題部の変更の登記 / 申請する。期限は変更から1か月以内 / 土地の側 / 敷地権である旨の登記 / 登記官が職権でする | — |
| コマ3 見出し | ラベル | ③　なぜ、そう分かれる？ | — |
| コマ3 図 | 図・カード | 建物の側は、申請する / 法44条1項9号・法51条1項 / 敷地権は、建物の表題部の登記事項 / 規約敷地で変われば、変更登記を申請 / 土地の側は、職権でされる / 法46条 / 建物の表題部に、敷地権を最初に登記する / そのとき登記官が、職権で土地に登記する / 分かれ目：申請の登記か、職権の登記か / たとえば / 駐車場だった土地が、規約で敷地になったら / 建物の所有者が、1か月以内に変更登記を申請 | — |
| コマ3 | 藍子（左・1番目） | 申請により、と読んでしまいました | — |
| コマ3 | トリ先生（右・2番目） | それが罠。土地の側は職権でするの | 「職権」 |
| コマ3 | 藍子（左・3番目） | 建物の側は、なぜ申請なんですか？ | — |
| コマ3 | トリ先生（右・4番目） | 建物の表題部の登記事項が変わるからよ | 「登記事項が変わる」 |
| コマ4 見出し | ラベル | ④　3肢の答え | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 建物は申請、土地は職権ですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。だから2肢は×、1肢が〇よ | 「2肢は×」 |
| コマ4 チェック欄 | 3項目（青✓） | 規約敷地が生じたら、建物の側が表題部の変更の登記を、変更から1か月以内に申請（法51条1項） / 土地の側の、敷地権である旨の登記は、登記官が職権でする（法46条） / D1796は〇、D1278は×（要しない）、D1368は×（申請により） | — |
| 結論帯 | 1行目 | 建物の側は申請、土地の側は職権 | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1278・D1368・D1796　正解×・×・〇（H29-Q15イ／H30-Q11⑦誤／R04-Q18イ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記法44条1項9号（敷地権の定義。敷地権は建物の表題部の登記事項）：記事 note_art005 の部品2、H30-Q11の記事で確認。法令DB note-articles/laws/fudousan-touki-hou.md 第44条第1項第9号の原文でも確認した
- 不動産登記法51条1項：44条1項各号（第2号及び第6号を除く）の登記事項に変更があったときは、変更があった日から1か月以内に変更の登記を申請する（法令DB fudousan-touki-hou.md 第51条第1項で確認）。9号は第2号・第6号に当たらないので、敷地権の変更も51条1項の対象になる。この『44条1項9号だから51条1項の対象』というつなぎは、記事（R04-Q18イ、H29-Q15イ）に直接の書き方はなく、条文の文言からの整理（ユーザーに伝える）
- 不動産登記法46条（法令DB fudousan-touki-hou.md 第46条で確認）：表示に関する登記のうち、区分建物に関する敷地権について表題部に最初に登記をするときは、登記官が、土地の登記記録について、職権で敷地権である旨の登記をする。コマ3の『表題部に最初に登記するとき登記官が土地に登記する』は、この条文の言い方そのまま。立法趣旨としては断定しない

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

TITLE BANNER: text 「建物の側は申請、土地の側は職権」 in large bold letters; the part 「土地の側は職権」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　同じ場面の3つの言い分」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center region: four SEPARATE cards stacked from top to bottom, with a small empty gap between them and no arrow anywhere, all with the same pale gray fill and a dark navy outline, and no check mark and no cross anywhere in this panel.
- Top card (a wide situation card, dark navy text): 「規約で土地が敷地になり、敷地権が生じた」.
- Card 2: a small dark navy tag 「肢D1796」 and two text lines: 「建物の表題部の変更の登記を」, 「1か月以内に申請しなければならない」.
- Card 3: a small dark navy tag 「肢D1278」 and two text lines: 「建物の表題部の変更の登記を」, 「申請することを要しない」.
- Card 4: a small dark navy tag 「肢D1368」 and two text lines: 「土地の敷地権である旨の登記を」, 「登記官が、申請によりする」.
- Above the diagram, a small question badge in a gray fill with dark navy text 「肢の言い分は、どこが違う？」 (a question badge only, with no check mark and no cross).
- The cards have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- 藍子 bubble (left, spoken first): 「どれも規約敷地の
肢ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「同じ場面でも、
申請か職権かで
分かれるのよ」 with the part 「申請か職権か」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　申請する登記と、職権の登記」
- A small dark navy tag 「出題者のねらい」 at the top left, with one line beside it: 「同じ場面の2つの登記を、申請と職権に分けられるか」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「建物の側」, a building icon, and two body lines: 「敷地権の表示をする、表題部の変更の登記」, 「申請する。期限は変更から1か月以内」.
- Right card, heading 「土地の側」, a land plot icon, and two body lines: 「敷地権である旨の登記」, 「登記官が職権でする」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ、そう分かれる？」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three stacked cards of the same size, from top to bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card, with no arrow, no connector, no check mark, and no cross. The cards are separated only by a small empty gap.
- Card 1, heading 「建物の側は、申請する」, a small dark navy tag 「法44条1項9号・法51条1項」, two body lines: 「敷地権は、建物の表題部の登記事項」, 「規約敷地で変われば、変更登記を申請」.
- Card 2, heading 「土地の側は、職権でされる」, a small dark navy tag 「法46条」, two body lines: 「建物の表題部に、敷地権を最初に登記する」, 「そのとき登記官が、職権で土地に登記する」, and under the body a dark navy ribbon tag with large white text 「分かれ目：申請の登記か、職権の登記か」.
- Card 3, heading 「たとえば」, two body lines: 「駐車場だった土地が、規約で敷地になったら」, 「建物の所有者が、1か月以内に変更登記を申請」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「申請により、と
読んでしまいました」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「それが罠。
土地の側は職権でするの」 with the part 「職権」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「建物の側は、
なぜ申請なんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「建物の表題部の
登記事項が変わるからよ」 with the part 「登記事項が変わる」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　3肢の答え」
- 藍子 bubble (left, spoken first): 「建物は申請、
土地は職権ですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。だから
2肢は×、1肢が〇よ」 with the part 「2肢は×」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「規約敷地が生じたら、建物の側が表題部の変更の登記を、変更から1か月以内に申請（法51条1項）」, 「土地の側の、敷地権である旨の登記は、登記官が職権でする（法46条）」, 「D1796は〇、D1278は×（要しない）、D1368は×（申請により）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「建物の側は申請、土地の側は職権」 with a yellow highlighter marker.
- Line 2: 「問題D1278・D1368・D1796　正解×・×・〇（H29-Q15イ／H30-Q11⑦誤／R04-Q18イ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 初, 号, 地, 建, 所, 権, 物, 登, 肢, 規, 解, 記, 請, 違 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`4コマ3_規約敷地は建物の側で申請.png`
- 途中の版・不採用の版：`4コマ3_規約敷地は建物の側で申請_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D1278-D1368-D1796_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で『同じ規約敷地の場面で、肢の言い分が、建物の側は申請する／しない、土地の側は申請による、と分かれている』、コマ2で『建物の側は申請、土地の側は職権』、コマ3で『敷地権は建物の表題部の登記事項なので建物の側が申請し、土地の側は表題部に最初に登記するときに登記官が付ける』が言える
- [ ] 工程C：肝の確認：①建物の側は、敷地権の表示をする表題部の変更の登記を、変更があった日から1か月以内に申請（法51条1項） ②土地の側の敷地権である旨の登記は、登記官が職権でする（法46条） ③D1796は〇、D1278は×（要しない）、D1368は×（申請により）
- [ ] 工程C：構成表の全文言を記事・法令DBと突き合わせ：『申請することを要しない』『申請により』『1か月以内』『表題部の登記事項』『職権』。記事にない整理（理由の言い方）は、条文の文言の範囲で、設計メモに書いてある
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラは、図や会話が入らないコマだけ小さくする（今回は小さくしたコマなし）

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

- 2026-10-09 v01：初版（条文別『苦手克服』シリーズの規約敷地用。規約敷地が生じたときの建物の側・土地の側の登記を問う3肢を1本にまとめた）
- 2026-10-11 v02：最新ルールで作り直し。D1796の単独版（申請人・期限・登記の4点）と重ならないよう、3肢の言い分を並べて誤りが2通りあること（建物の側を『要しない』、土地の側を『申請により』）を示す型4＋型3に変えた。同じ文が4回出ていた構成をやめ、コマ2は『何を・誰が』、コマ3は『なぜ』（敷地権は建物の表題部の登記事項／土地の側は表題部に最初に登記するとき登記官が付ける）に役割を分けた。コマ1のキャラは通常サイズ（side）。
