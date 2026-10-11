# D1949 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

- 肢：D1949（不動産登記法／土地の分筆・合筆・地積更正、出典 R06-Q09オ）。正解＝〇（正しい記述）。誤解2026-10-04・10-05・10-11の3回×と答えて誤答（10-06だけ〇で正解）。
- 記事：`note-articles/r6-mondai/q09-gappitsu-touki.md` オ（承役地についてする地役権の登記がある甲土地に、地役権の登記がない乙土地を合筆するときは、地役権設定の範囲を申請情報の内容としなければならない）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】問題文は『承役地についてする地役権の登記がある甲土地』に『地役権の登記がない乙土地』を合筆する場面を示し、『地役権設定の範囲を申請情報の内容としなければならない』と言い切る。①地役権の登記がある土地は合筆できない（法41条6号）と思わせ、申請の話そのものを成り立たないと読ませる。②令別表9の項申請情報欄ロの『合筆後の土地の一部であるとき』という条件を肢は書いていない。その条件は『乙土地に地役権の登記がない』という一句に隠れている（乙に地役権がなければ、合筆後に地役権が及ぶのは必ず元の甲土地の部分＝一部になる）。③『申請情報』と『添付情報』（範囲を証する情報・地役権図面）の取り違えを誘う。
- 【受験者の勘違い・定着していない点】①地役権の登記がある土地は合筆できないと覚え、承役地の地役権が規則105条1号の例外であることが定着していない。②承役地と要役地を取り違える（承役地＝負担を受ける側は合筆できる、要役地＝利益を受ける側は例外に入らず合筆できない）。③合筆しても地役権は全部に及ぶと考え、乙に地役権がないと一部になる、という前提がない。④範囲は添付情報（地役権者が作成した情報・地役権図面）で足りると考え、申請情報にも書くことを落とす。（①〜④は回答履歴から立てた推測。D1949は4回中3回×。同じ問のD1945・D1947・D1949（正）とD1946・D1948（誤）の中で、地役権の肢だけを繰り返し外していることから、『合筆の制限（41条）の例外』と『範囲の記載』の2点のどちらかが定着していないと推測する。記事には誤答の理由は書かれていない）
- 【対比する制度】「承役地の地役権」⇔「要役地の地役権」：承役地についてする地役権の登記がある土地は、規則105条1号の例外で合筆できる（そのとき、合筆後の土地の一部になるなら範囲を申請情報に書く）。要役地の地役権の登記がある土地は、規則105条に挙がらず、合筆できない（結論が逆になる点）。
- 【型の選び方】型：型3（＋型4の対比、型2のしくみ図）。理由：結論の〇だけでなく、『なぜ範囲を書くのか』（乙に地役権がないと合筆後は一部になる）が分からないと、分筆の肢（令別表8の項ロ）や、両方に地役権がある肢で崩れる。コマ2に承役地⇔要役地の対比カード、コマ3に合筆のあとの図と理由、コマ4で申請情報と添付情報を分ける。
- 初見の読者が引っかかる理解の壁：地役権の登記がある土地は合筆できないはずなのに、なぜ範囲を書いて申請できるのか／乙に地役権がないのに、なぜ範囲を書くのかが見えない。壁を越える材料は、記事の『合筆後の土地のどの部分に地役権が及ぶのかを明確にするため』と、同系統の肢D1039（H27-Q06オ）の記事の『地役権のない土地と合筆すると、合筆後の一筆のうち、もとの地役権のある土地の部分だけに地役権が及ぶ』。
- 記事の範囲：R06-Q09オ（承役地に地役権があり、地役権のない土地を合筆するときは、地役権設定の範囲を申請情報の内容としなければならない。令別表9の項申請情報欄ロ。『添付情報』ではなく『申請情報』であることは、記事の確認事項で訂正済み）。
- extra_refs：①不動産登記法41条6号（所有権の登記以外の権利に関する登記がある土地は、法務省令で定めるものを除き合筆できない）と、不動産登記規則105条1号（承役地についてする地役権の登記は、合筆後の土地の登記記録に登記することができる）は、note-articles/laws/fudousan-touki-hou.md・fudousan-touki-kisoku-1.md で原文を確認した（同系統の肢D1151〈H28-Q10ア〉・D0748〈H24-Q08ウ〉の記事にもある）。②令別表9の項（申請情報欄ロ：地役権設定の範囲、添付情報欄：範囲を証する地役権者が作成した情報又は裁判を証する情報、及び地役権図面）は note-articles/laws/fudousan-touki-rei-betsuhyou.md で確認した。③要役地の地役権の登記がある土地は例外に入らず合筆できない、という整理は、D1560（R02-Q10エ・×）の記事 note-articles/r2-mondai/q10-gappitsu-seigen.md とD0251（H19-Q10ア・×）の記事 note-articles/h19-mondai/q10-gappitsu.md による（承役地は地役権の負担を受ける側、要役地は利益を受ける側、という言い方もH19の記事）。この③と『乙に地役権がないと合筆後は元の甲の部分だけに及ぶ』（H27-Q06オの記事）は、D1949の記事にない整理なので、ユーザーに『記事にない整理』として伝える。
- 同系統で今回は図に入れない肢：D1151（H28-Q10ア・〇。同じ内容を『合筆後の土地の一部であるとき』という条件つきで書く）、D0748（H24-Q08ウ・×。承役地の地役権があれば合筆できないとする誤り）、D1560（R02-Q10エ・×）、D0251（H19-Q10ア・×）、D1039（H27-Q06オ・〇）、D0647（H23-Q08イ・〇）。コマ2で承役地と要役地だけ使う。
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない。甲土地・乙土地は土地のブロックと文字ラベルで示す。地役権が及ぶ部分は、濃紺の斜線の塗りで示す（色は意味を持たせない）。
- 矢印の意味：矢印は使わない。コマ1は2つの土地を並べた図、コマ2は左右のカード、コマ3は合筆のあとの1枚の図。
- 配色：コマ1〜3は印（✓✕）を付けない（合筆できる・できないは文字で書く）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方：コマ1＝side（キャラが左右の端、図は中央。2つの土地の並置）、コマ2＝既定（通常キャラ・台詞2つ。左右のカードと下の帯）、コマ3＝faces（左に合筆のあとの図、右に会話4つ＝顔4つ＝4行）、コマ4＝既定（暗記3点と結論）。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D1949～R06-Q09オ～

## note記事の冒頭文

承役地についてする地役権の登記がある甲土地に、地役権の登記がない乙土地を合筆します。このとき、地役権設定の範囲を申請情報として書くことになるのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（令和6年度　第9問　オ）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 承役地は合筆できる。範囲は申請情報に | 「範囲は申請情報に」を黄色マーカー |
| コマ1 見出し | ラベル | ①　承役地の甲に、乙を合筆する | — |
| コマ1 図 | 図・カード | 甲土地 / 承役地の地役権の登記がある / 乙土地 / 地役権の登記がない / 甲土地に乙土地を合筆する / 地役権設定の範囲は、申請情報に書く？ | — |
| コマ1 | 藍子（左・先に話す） | 地役権つきの土地は、合筆できませんよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。承役地は例外よ | 「承役地は例外」 |
| コマ2 見出し | ラベル | ②　承役地と要役地は、結論が逆 | — |
| コマ2 図 | 図・カード | 承役地の地役権 / 肢D1949はこちら / 地役権の負担を受ける側の土地 / 例外（規則105条1号）で合筆できる / 要役地の地役権 / この問いには登場しない / 地役権の利益を受ける側の土地 / 例外に入らず、合筆できない / 原則：所有権以外の権利の登記がある土地は合筆できない / 法第41条第6号 | — |
| コマ2 | 藍子（左・先に話す） | 承役地と要役地で、何が違うんですか？ | — |
| コマ2 | トリ先生（右・答える） | 合筆の例外は、承役地だけなのよ | 「承役地だけ」 |
| コマ3 見出し | ラベル | ③　合筆のあとは、一部だけ | — |
| コマ3 図 | 図・カード | 合筆のあと（1筆） / 元の甲土地　地役権が及ぶ / 元の乙土地　及ばない / ひっかけ：乙土地には地役権の登記がない / 一部になるので、申請情報に地役権設定の範囲を書く / 令別表9の項 | — |
| コマ3 | 藍子（左・1番目） | 合筆できても、範囲は書かないのでは？ | — |
| コマ3 | トリ先生（右・2番目） | そこが罠。乙には地役権がないのよ | 「乙には地役権がない」 |
| コマ3 | 藍子（左・3番目） | 地役権がないと、何が変わりますか？ | — |
| コマ3 | トリ先生（右・4番目） | 及ぶのは一部だけ。範囲を特定するのよ | 「一部だけ」 |
| コマ4 見出し | ラベル | ④　肢の答えは〇 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 合筆はできて、範囲も書くんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。一部になるから範囲を書くのよ | 「範囲を書く」 |
| コマ4 チェック欄 | 3項目（青✓） | 承役地の地役権は合筆の例外。要役地は合筆できない / 乙に地役権がなければ一部になる。範囲は申請情報に書く / 範囲を証する情報と地役権図面は添付情報。D1949は〇 | — |
| 結論帯 | 1行目 | 承役地の合筆は、地役権の範囲を書く | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1949　正解〇（R06-Q09オ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記法41条6号（note-articles/laws/fudousan-touki-hou.md）
- 不動産登記規則105条1号（note-articles/laws/fudousan-touki-kisoku-1.md）
- 不動産登記令別表9の項（note-articles/laws/fudousan-touki-rei-betsuhyou.md）

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

TITLE BANNER: text 「承役地は合筆できる。範囲は申請情報に」 in large bold letters; the part 「範囲は申請情報に」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　承役地の甲に、乙を合筆する」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- Two plot-of-land blocks side by side in the center, both exactly the same size, separated by a thin plain line (no arrow). Left block, label 「甲土地」, with a small dark navy tag 「承役地の地役権の登記がある」. Right block, label 「乙土地」, with a small dark navy tag 「地役権の登記がない」. The two tags are NOT identical.
- Under the two blocks, a dark navy ribbon with large white text 「甲土地に乙土地を合筆する」.
- At the top, a small question badge in a gray fill with dark navy text 「地役権設定の範囲は、申請情報に書く？」 (a question badge only, with no check mark and no cross).
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, spoken first): 「地役権つきの土地は、
合筆できませんよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
承役地は
例外よ」 with the part 「承役地は例外」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (藍子 puzzled, トリ先生 explaining with a wing-pointer; 藍子's hands: one hand touches her chin and the other holds the clipboard at her side (two hands in total)):
- Label tab: 「②　承役地と要役地は、結論が逆」
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「承役地の地役権」, small tag 「肢D1949はこちら」, two body lines: 「地役権の負担を受ける側の土地」, 「例外（規則105条1号）で合筆できる」.
- Right card, heading 「要役地の地役権」, small tag 「この問いには登場しない」, two body lines: 「地役権の利益を受ける側の土地」, 「例外に入らず、合筆できない」.
- Under the two cards, one wide dark navy band with large white text 「原則：所有権以外の権利の登記がある土地は合筆できない」 and a small tag 「法第41条第6号」 at its right end.
- The two cards have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, spoken first): 「承役地と要役地で、
何が違うんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「合筆の例外は、
承役地だけなのよ」 with the part 「承役地だけ」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　合筆のあとは、一部だけ」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- One large card at the top with the same pale gray fill and a dark navy outline, with its dark navy heading 「合筆のあと（1筆）」 placed fully INSIDE the card. Inside the card, one wide land block made of two parts joined side by side. The left part (the former 甲土地) is filled with dark navy diagonal stripes and has the label 「元の甲土地　地役権が及ぶ」 above it. The right part (the former 乙土地) has a plain pale gray fill and has the label 「元の乙土地　及ばない」 above it. The two labels are NOT identical.
- Under the card, a dark navy ribbon tag with large white text 「ひっかけ：乙土地には地役権の登記がない」.
- Under the ribbon, one wide band of the same pale gray fill and dark navy outline with dark navy text 「一部になるので、申請情報に地役権設定の範囲を書く」 and a small tag 「令別表9の項」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「合筆できても、
範囲は書かない
のでは？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「そこが罠。
乙には地役権が
ないのよ」 with the part 「乙には地役権がない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「地役権がないと、
何が変わりますか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「及ぶのは
一部だけ。範囲を
特定するのよ」 with the part 「一部だけ」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　肢の答えは〇」
- 藍子 bubble (left, spoken first): 「合筆はできて、
範囲も書くんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。一部になるから
範囲を書くのよ」 with the part 「範囲を書く」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「承役地の地役権は合筆の例外。要役地は合筆できない」, 「乙に地役権がなければ一部になる。範囲は申請情報に書く」, 「範囲を証する情報と地役権図面は添付情報。D1949は〇」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「承役地の合筆は、地役権の範囲を書く」 with a yellow highlighter marker.
- Line 2: 「問題D1949　正解〇（R06-Q09オ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 号, 地, 所, 承, 権, 登, 肢, 規, 解, 記, 証, 請, 違 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the word 「原則」 is spelled exactly like this everywhere (never 「思則」); confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 地役権つきの甲土地 | 薄い黄色のマーカー |
| タイトル2行目 | 範囲は書く？ | 「書く？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D1949　R06-Q09オ | — |

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
地役権つきの甲土地
Line 2 is larger; the phrase 書く？ is red-orange and the rest is dark navy:
範囲は書く？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D1949　R06-Q09オ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: two adjoining plots of land, one with a faint striped strip along its edge
Right side: a blank map sheet and a rubber stamp beside a small registry book

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written (cartoon expression marks such as ！ and ？ beside the characters' faces are decoration, are allowed, and are not extra text); scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 役, 権, 甲, 土, 範, 囲, 書, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere. Never delete, redo, or regenerate anything because of an expression mark or a symbol beside a character; deliver the first image as it is.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D1949～R06-Q09オ～.png |
| 見出し画像（採用版） | 4コマ解説図解D1949～R06-Q09オ～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D1949～R06-Q09オ～_v01.png ／ 4コマ解説図解D1949～R06-Q09オ～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D1949_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で『承役地の地役権がある甲に、ない乙を合筆する』、コマ2で『承役地は合筆できる・要役地はできない』、コマ3で『合筆のあとは元の甲の部分だけに地役権が及ぶ＝一部だから範囲を書く』が言える
- [ ] 工程C：肝の確認：①承役地の地役権は合筆の制限の例外（規則105条1号） ②乙に地役権がなければ、合筆後は一部になるので、地役権設定の範囲を申請情報に書く（令別表9の項ロ） ③範囲を証する情報と地役権図面は添付情報 ④肢D1949は〇
- [ ] 工程C：構成表の全文言を記事・法令DBと突き合わせ：『承役地』『要役地』『合筆できる』『地役権設定の範囲』『申請情報』『添付情報』『規則105条1号』『令別表9の項』『法第41条第6号』。要役地の整理は記事にない（D1560・D0251の記事）旨を設計メモに書いてある
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方が隣り合うコマで同じにならない（side→既定→faces→既定）

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

- 2026-10-11 v01：新規作成（一問一答で4回中3回×と誤答。型は型3＋型4の対比。理由＝乙に地役権がないと合筆後は一部になる。対比＝承役地の地役権⇔要役地の地役権）
