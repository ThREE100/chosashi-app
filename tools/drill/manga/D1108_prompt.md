# D1108 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

- 肢：D1108（民法／時効・条件期限、出典 H28-Q01ウ）。正解＝〇（正しい記述）。誤解2026-10-03に×と答えて誤答、2026-10-05・10-11は？（わからない）で未習得。
- 記事：`note-articles/h28-mondai/q01-shoumetsujikou.md` ウ（訴えの取下げは、権利が確定することなく裁判上の請求が終了した場合にあたり、終了の時から6か月は時効の完成が猶予される）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】問題文は『その訴えが取り下げられたときにおいても』と、取下げの場面を最初から前に出す。取り下げたのだから訴えの効力は消える、と読ませる。さらに『催告として』『時効の中断の効力』という出題当時の言い方で、いまの完成猶予・更新のどちらの話かを見えにくくしている。
- 【受験者の勘違い・定着していない点】（推測：回答履歴は×のあと？が2回。最初の×は『取り下げたら効力は残らない』と読んだ形、その後の？は、残るとすれば何が残るのかが整理できていない形と考える）①訴えを取り下げたら、時効を止めた効果も全部なくなる、と考える。②確定判決で権利が確定した場合は新たに進行する（更新）と覚えていて、取り下げて確定しなかった場合は何が残るのか（6か月の完成猶予だけ）が頭にない。③『催告として』という出題当時の言い方が、いまの条文のどの規定にあたるのかが結びつかない。
- 【対比する制度】「確定判決で権利が確定」⇔「訴えの取下げ」：どちらも裁判上の請求が終わる場面だが、確定判決で権利が確定したときは、終了の時から時効が新たに進行を始める（147条2項）。訴えの取下げで権利が確定することなく終了したときは、終了の時から6か月は時効が完成しないだけ（147条1項柱書のかっこ書）。結論が逆になるのは、新たに進行するかどうか。
- 【型の選び方】型：型3（第三案・理由説明）＋型1の対比。理由：初見の読者が引っかかる壁は『取り下げたのに、なぜ時効の完成が猶予されるのか』（取り下げたら全部なくなると思う）。1肢が3回、×と？で定まらないので、結論の暗記より、『取下げは権利が確定せずに終了した場合にあたるから、条文どおり6か月は猶予される』という理由と、確定判決の場合（新たに進行）との違いが読み取れる構成を優先した。コマ2で二つの場合を左右に並べ、コマ3で理由を示す。
- 記事の範囲：H28-Q01ウ（147条1項柱書のかっこ書。確定判決又はこれと同一の効力を有するものによって権利が確定することなく事由が終了したときは、終了の時から6か月を経過するまで時効は完成しない。訴えの取下げはこれにあたる。たとえば：和解交渉がまとまりそうで訴えを取り下げても、取り下げた時から6か月以内に改めて裁判上の請求などをすれば、時効の完成を防げる）。記事末尾の改題メモ：出題当時の肢は『催告として時効の中断の効力』という判例法理（裁判上の催告）で、令和2年の民法改正で147条1項柱書のかっこ書として明文化された。結論（正しい記述）は変わらない。『中断』は改正で完成猶予と更新に分かれた（記事のエの注記も同じ）。
- extra_refs：①民法147条1項・2項の原文は法令DB note-articles/laws/minpou-1-soukyoku-bukken.md の第147条で確認した（1項かっこ書＝確定せずに終了した場合は終了の時から6か月。2項＝確定したときは終了の時から新たに進行）。確定判決の場合の147条2項は同じ記事のイの解説にもある。②『取下げでは新たに進行を始めない（更新にはならない）』は、147条2項が『権利が確定したとき』に限っていることからの条文の読みで、記事のウには明記がなく、記事にない整理（ユーザーに伝える）。コマ4の3点目はこれに沿って『取下げは猶予だけ』と書いた。③『中断は、今の言い方で完成猶予と更新』は、記事のエの注記と改題メモの言い方に合わせた。
- 兄弟肢：D1106（ア・×：再度の催告では新たな完成猶予は生じない。150条2項）、D1107（イ・〇：確定判決で新たに進行。147条2項）、D1109（エ・×：一部弁済は承認）、D1110（オ・〇：時効完成後の承認）。このうちイ（D1107）は本肢と同じ147条で結論が逆になる相手なので対比に使った。ア（150条）は、肢の『催告として』の語と混ざりやすいが、本肢の6か月は147条1項の話で、150条の催告の話ではないため、図には入れない（条文番号の混在を避ける）。
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない（lead1の問いかけだけ問題文どおり）。訴え・期日・期間はカードと文字ラベル。
- 矢印の意味：矢印は使わない。コマ1は番号つきの縦3枚の別カード（時系列は順番に並べるだけ）、コマ2は左右のカード、コマ3は上下2枚のカード。
- 配色：コマ1・2は印（✓✕）を付けない。コマ3は上のカード（取り下げたら効力は消える）＝赤✕1つ、下のカード（取下げでも6か月は猶予）＝青✓1つ。コマ4の暗記3点は青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方：コマ1＝side（キャラが左右の端、図は中央に縦3枚のカードと疑問バッジ）、コマ2＝none（図が主役。左右のカードと帯）、コマ3＝faces（左に上下2枚のカードと『たとえば』の帯、右に会話4つの縦並び）、コマ4＝既定（両方）。隣り合うコマで同じ見せ方が続かない。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D1108～H28-Q01ウ～

## note記事の冒頭文

ＡがＢに貸金返還請求の訴えを提起し、その後その訴えを取り下げました。訴訟手続でのＡの権利行使の意思の表示は、取り下げたときにおいても、Ｂに対する催告として時効の中断の効力を有するのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（平成28年度　第1問　ウ）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 訴えを取り下げても、6か月は時効が完成しない | 「6か月は時効が完成しない」を黄色マーカー |
| コマ1 見出し | ラベル | ①　取り下げた後は、どうなる？ | — |
| コマ1 図 | 図・カード | 返還期日を経過 / 貸金返還請求の訴えを提起 / 訴えを取り下げた（判決は出ていない） / 取り下げた後も、効力は残る？ / 中断は、今の言い方で完成猶予と更新 | — |
| コマ1 | 藍子（左・先に話す） | 取り下げたら、効力は残らないのでは？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。取下げの後が肝なのよ | 「取下げの後」 |
| コマ2 見出し | ラベル | ②　確定したときと、取下げのとき | — |
| コマ2 図 | 図・カード | 出題者のねらい / 取下げで終わりか、6か月残るかを見分けさせる / 確定判決で権利が確定したとき / 時効は新たに進行を始める / （147条2項） / 訴えの取下げで終了したとき / 終了の時から6か月は / 時効は完成しない / 民法147条1項柱書のかっこ書 / 催告としての効力は出題当時の判例の言い方 / 今は147条1項柱書のかっこ書に明文化 | — |
| コマ3 見出し | ラベル | ③　なぜ、6か月は猶予される？ | — |
| コマ3 図 | 図・カード | 取り下げたら、効力は消える / 訴えをやめたので / 時効への効力も消える / ひっかけ：取り下げられたときにおいても / 取下げ後も、6か月は猶予 / 権利が確定せずに終了した場合にあたる / だから終了の時から6か月は完成しない / たとえば：和解のために取り下げても / 取下げの時から6か月以内に / 改めて裁判上の請求などをすれば防げる | — |
| コマ3 | 藍子（左・1番目） | 判決が出ていないのに、猶予が残るんですか？ | — |
| コマ3 | トリ先生（右・2番目） | それが罠。確定せず終了なら6か月猶予よ | 「6か月猶予」 |
| コマ3 | 藍子（左・3番目） | 催告として、とは何のことですか？ | — |
| コマ3 | トリ先生（右・4番目） | 出題当時は判例の言い方。今は条文よ | 「今は条文」 |
| コマ4 見出し | ラベル | ④　結論は〇 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 取り下げても、6か月は守られるんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。この肢は〇よ。6か月以内が勝負よ | 「6か月以内が勝負」 |
| コマ4 チェック欄 | 3項目（青✓） | 訴えを取り下げても、終了の時から6か月は時効が完成しない / 6か月以内に改めて裁判上の請求などをすれば、完成を防げる / 判決で確定すれば新たに進行。取下げは猶予だけ | — |
| 結論帯 | 1行目 | 取下げ後も、終了の時から6か月は時効が完成しない | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1108　正解〇（H28-Q01ウ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 民法147条1項柱書のかっこ書・同条2項（法令DB note-articles/laws/minpou-1-soukyoku-bukken.md 第147条）：1項＝事由が終了する（確定判決又は確定判決と同一の効力を有するものによって権利が確定することなくその事由が終了した場合にあっては、その終了の時から六箇月を経過する）までの間は、時効は完成しない。2項＝前項の場合において確定判決又は確定判決と同一の効力を有するものによって権利が確定したときは、事由が終了した時から新たにその進行を始める。1項は記事のウ、2項は記事のイの解説にあり、記事の範囲内
- 取下げでは新たに進行しない（更新にはならない）：147条2項が『権利が確定したとき』に限っていることからの条文の読み。記事のウには明記がなく、記事にない整理

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a collared light-blue blouse with thin blue pinstripes (sleeves rolled up) and a navy pencil skirt with navy pumps, no jacket, often holding a navy clipboard and a pencil; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. Organizations and buildings in the diagrams are NOT characters: draw them only as simple, faceless, flat icons with the exact text labels given below.

ANATOMY (critical, 藍子): keep her human anatomy strictly correct in every panel: exactly one head, one torso, exactly two arms (one left, one right) and exactly two hands in total. Never draw extra arms, extra hands, extra fingers, floating hands, duplicated hands, arms that do not grow from the shoulders, or fused hands. Each hand has exactly five fingers. Check that every shoulder, elbow, and wrist connects naturally. HAND COUNT RULE: before drawing each panel, assign both of 藍子's hands a job (for example, one hand points while the other hand holds the clipboard or hangs at her side; or one hand touches her chin while the other holds the clipboard; or both hands are raised in a small cheer). When she points, only ONE arm points; her other hand must not be clasped, raised, or clenched at the same time, so there are never three hands in a panel. POSE: change 藍子's pose from panel to panel (for example standing, sitting, leaning forward, resting a hand on her chin) and use a different set of poses each time this image is generated. CONTENT: in each panel, express through the diagram, labels, and scene the elements a reader needs in order to understand this article's content and pass the land and building surveyor exam, without adding any text beyond the given strings.

FIXED POSITIONS AND SPEECH BUBBLES: In every panel in which a character appears, 藍子 (the student) stands on the LEFT side and トリ先生 (the teacher) stands on the RIGHT side. A panel does not have to show both characters: when the diagram, the flowchart, or the items to memorize need more space, the PANEL line may show only one of the two characters, show both at the normal size at the two outer edges, show both as small face icons in a vertical conversation column, or show both very small; in that case follow the PANEL line and its LAYOUT lines, and a character who is not drawn has no speech bubble; in a panel marked as face icons, each character appears only as a small round face icon inside the vertical conversation column described in the LAYOUT lines, with exactly one face icon for each speech bubble and never more face icons than bubbles. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

CONTINUITY: any object, label, ribbon, tag, or figure that appears in more than one panel keeps the same look, the same color, and the same label text in every panel in which it appears (for example, a ribbon on a plot of land does not disappear after a step of the diagram), unless that panel's own description says that it changes. Every speech bubble's line breaks follow phrase boundaries as written inside its quotation marks; never split a word across lines.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall).

TITLE BANNER: text 「訴えを取り下げても、6か月は時効が完成しない」 in large bold letters; the part 「6か月は時効が完成しない」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　取り下げた後は、どうなる？」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: three SEPARATE numbered cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a dark navy number badge, and one dark navy text line. Do NOT draw any arrow anywhere in this panel and do NOT connect the cards; they are separated only by a small empty gap.
- Card 1: 「返還期日を経過」. Card 2: 「貸金返還請求の訴えを提起」. Card 3: 「訴えを取り下げた（判決は出ていない）」.
- At the top, a small question badge in a gray fill with dark navy text 「取り下げた後も、効力は残る？」 (a question badge only, with no check mark and no cross).
- At the bottom, one small white card with a dark navy outline: 「中断は、今の言い方で完成猶予と更新」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, spoken first): 「取り下げたら、
効力は残らないのでは？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
取下げの後が
肝なのよ」 with the part 「取下げの後」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　確定したときと、取下げのとき」
- A small dark navy tag 「出題者のねらい」 at the top left, with one line beside it: 「取下げで終わりか、6か月残るかを見分けさせる」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「確定判決で権利が確定したとき」, two body lines: 「時効は新たに進行を始める」, 「（147条2項）」.
- Right card, heading 「訴えの取下げで終了したとき」, two body lines: 「終了の時から6か月は」, 「時効は完成しない」, and a small tag 「民法147条1項柱書のかっこ書」.
- Under the two cards, one wide dark navy band with white text in two lines: 「催告としての効力は出題当時の判例の言い方」 and 「今は147条1項柱書のかっこ書に明文化」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ、6か月は猶予される？」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Two stacked cards of the same size, top and bottom, with no arrow and no connector between them, and a wide example strip under them.
- Top card, with a dark navy heading 「取り下げたら、効力は消える」, two body lines 「訴えをやめたので」 and 「時効への効力も消える」, and ONE red cross only (no check mark on this card); a dark navy ribbon tag under the body, with large white text, reads 「ひっかけ：取り下げられたときにおいても」.
- Bottom card, with a dark navy heading 「取下げ後も、6か月は猶予」, two body lines 「権利が確定せずに終了した場合にあたる」 and 「だから終了の時から6か月は完成しない」, and ONE blue check mark only (no cross on this card).
- Example strip under the two cards, in three short lines: 「たとえば：和解のために取り下げても」, 「取下げの時から6か月以内に」, 「改めて裁判上の請求などをすれば防げる」.
- The two cards have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「判決が出ていないのに、
猶予が残るんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「それが罠。確定せず
終了なら6か月猶予よ」 with the part 「6か月猶予」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「催告として、とは
何のことですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「出題当時は判例の言い方。
今は条文よ」 with the part 「今は条文」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇」
- 藍子 bubble (left, spoken first): 「取り下げても、
6か月は守られるんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。この肢は〇よ。
6か月以内が勝負よ」 with the part 「6か月以内が勝負」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「訴えを取り下げても、終了の時から6か月は時効が完成しない」, 「6か月以内に改めて裁判上の請求などをすれば、完成を防げる」, 「判決で確定すれば新たに進行。取下げは猶予だけ」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「取下げ後も、終了の時から6か月は時効が完成しない」 with a yellow highlighter marker.
- Line 2: 「問題D1108　正解〇（H28-Q01ウ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two very small characters are drawn as specified and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 効, 当, 権, 肢, 解, 請, 過, 還 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 訴えを取り下げたら | 薄い黄色のマーカー |
| タイトル2行目 | 時効はどうなる？ | 「どうなる？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D1108　H28-Q01ウ | — |

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
訴えを取り下げたら
Line 2 is larger; the phrase どうなる？ is red-orange and the rest is dark navy:
時効はどうなる？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D1108　H28-Q01ウ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a stack of court document sheets being slid back into a folder, beside a small hourglass, no text
Right side: a small wall calendar with a few days circled and a blank document sheet, no text

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 訴, 取, 下, 時, 効, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D1108～H28-Q01ウ～.png |
| 見出し画像（採用版） | 4コマ解説図解D1108～H28-Q01ウ～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D1108～H28-Q01ウ～_v01.png ／ 4コマ解説図解D1108～H28-Q01ウ～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D1108_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で『返還期日を過ぎ、訴えを提起し、取り下げた（判決は出ていない）。取り下げた後も効力は残るか』、コマ2で『判決で確定すれば新たに進行、取下げは終了から6か月は完成しないだけ』、コマ3で『取下げは権利が確定せずに終了した場合にあたるから6か月猶予』が言える
- [ ] 工程C：肝の確認：①取下げは権利が確定することなく終了した場合にあたる（147条1項柱書のかっこ書）ので、終了の時から6か月は時効が完成しない ②その6か月以内に改めて裁判上の請求などが要る ③確定判決で権利が確定すれば新たに進行する（147条2項）のと対比 ④肢D1108は〇
- [ ] 工程C：構成表の全文言を記事・法令DBと突き合わせ：『権利が確定せずに終了』『終了の時から6か月』『時効は完成しない』『新たに進行』『出題当時の判例の説明』『今は条文に書かれている』『中断は完成猶予と更新』。記事にない整理（取下げでは新たに進行しない）は設計メモに残した
- [ ] 工程C：コマ1・2に印がなく、コマ3で上のカードが赤✕・下のカードが青✓、コマ4だけ青✓の暗記3点。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない

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

- 2026-10-11 v01：新規作成（一問一答で×・？・？と定まらない肢。型3＋型1の対比）
