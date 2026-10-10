# D1996 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

- 肢：D1996（不動産登記法／筆界特定・境界、出典 R06-Q19イ）。正解＝〇（正しい記述）。誤解2026-10-05・10-08・10-09・10-10の4回とも×と答えて誤答。
- 記事：`note-articles/r6-mondai/q19-hikkai-tokutei.md` イ（表題登記がない土地の所有者は、所有権を有することを証する情報の提供が必要）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】問題文は『表題登記がない甲土地』『甲土地の所有権を有することを証する情報』『提供しなければならない』と、登記の有無と義務を言い切る。同じ問のア（1点だけ接する）・エ（双方に表題登記がない）では『申請できない』が正解になるため、『表題登記がない』という語から『できない側の話』と読ませる。さらに、隣の乙土地には表題登記があるので、証明は乙の記録で足りると思わせる（証するのは甲の所有権）。
- 【受験者の勘違い・定着していない点】①本人が所有者なのに、所有権を証明する書類まで要るはずがないと考える。②登記記録で所有者が分かる土地（所有権の登記名義人・表題部所有者）と、記録に載らない土地（所有者）を区別せず、すべて同じ扱いと覚える。③乙に登記があるから、申請の場面全体で記録を使えると取り違える（所有権を証するのは申請人の土地＝甲）。（①〜③は、回答履歴から立てた推測。D1996は4回とも×。同じ問のD1995・D1998は〇、D1997は×で正解しているので、『表題登記がない土地は申請できない』という対象土地の要件の誤解ではなく、申請人の側の添付情報を取り違えている形と推測する）
- 【対比する制度】「表題登記がある土地」⇔「表題登記がない土地」：表題登記がある土地は、申請人（所有権の登記名義人・表題部所有者）が登記記録で確認できる。表題登記がない土地は、申請人（所有者）が記録に載らないので、所有権を有することを証する情報を自分で提供する（結論が逆になる点）。
- 【型の選び方】型：型3（第三案・理由説明）。理由：結論の〇だけを覚えても、『なぜ表題登記がない土地だけ所有権の証明が要るのか』が分からないと、同じ問のウ（一部取得者は取得を証する情報）などで崩れる。理由は『登記記録で所有者を確認できるか』の1点に絞り、コマ2の上下ではなく左右の対比カード、コマ3の3ステップで『証するのは甲の所有権』を読み取らせる。型1の流れ（思い込み→理由→読み方→結論）を保ち、対比カードの印は付けない。
- 初見の読者が引っかかる理解の壁：本人が所有者なのに、なぜ所有権の証明が要るのか分からない。壁を越える材料は、記事の『表題登記がある土地であれば登記記録から所有者を確認できますが、未登記の土地では申請適格を裏付ける必要がある』と、法123条5号の三区分（所有権の登記名義人／表題部所有者／所有者）。
- 記事の範囲：イ（申請人が表題登記のない土地の所有者であるときは、所有権を有することを証する情報を提供。表題登記がある土地は登記記録から所有者を確認できる。権利証や売買契約書の例）／規則209条1項4号（記事冒頭の確認欄に記載あり）。
- extra_refs：不動産登記法123条5号（所有権登記名義人等＝所有権の登記がある土地は所有権の登記名義人、所有権の登記がない一筆の土地は表題部所有者、表題登記がない土地は所有者）、同法123条1号（筆界の定義。表題登記がある一筆の土地とこれに隣接する他の土地〈表題登記がない土地を含む〉との間）、同法131条1項（土地の所有権登記名義人等が筆界特定の申請をすることができる）を note-articles/laws/fudousan-touki-hou.md で確認した。不動産登記規則209条1項4号（申請人が表題登記がない土地の所有者であるとき、当該土地の所有権を有することを証する情報）は note-articles/laws/fudousan-touki-kisoku-2.md で確認した。いずれも記事の結論と一致し、記事にない整理は『法123条5号の三区分で申請人を並べる』点と『乙に表題登記があるので対象土地になる』点（法123条1号）。
- 同系統で今回は図に入れない肢：D1995（ア・〇、1点のみで接する土地は対象にならない）、D1997（ウ・×、一部取得者は取得を証する情報〈規則209条1項5号〉を出せば、対象筆界に接していなくても申請できる）、D1998（エ・〇、双方に表題登記がない土地は対象にならない）、D1999（オ・×、筆界確定訴訟が係属中でも申請できる）。同じ問の肢は、コマ3のステップ1で乙に表題登記がある点だけ触れる。
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない。甲土地・乙土地は土地のブロックと文字ラベル、申請人は文字ラベルのタグで示す。
- 矢印の意味：矢印は使わない。コマ1は2つの土地を並べた図、コマ2は左右のカード、コマ3は3枚のステップカード。
- 配色：コマ1〜3は印（✓✕）を付けない（要る・載っていない等は文字で書く）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方：コマ1＝side（キャラが左右の端、図は中央。2つの土地の並置）、コマ2＝既定（通常キャラ・台詞2つ。左右のカードと下の帯）、コマ3＝faces（左に3枚のステップカード、右に会話4つ＝顔4つ＝4行）、コマ4＝既定（暗記3点と結論）。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D1996～R06-Q19イ～

## note記事の冒頭文

表題登記がない甲土地の所有者が、隣の表題登記がある乙土地との間の筆界について、筆界特定を申請します。このとき甲土地の所有者は、甲土地の所有権を有することを証する情報を提供しなければならないのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（令和6年度　第19問　イ）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 表題登記がない土地は、所有権の証明が要る | 「所有権の証明が要る」を黄色マーカー |
| コマ1 見出し | ラベル | ①　未登記の甲と登記済みの乙 | — |
| コマ1 図 | 図・カード | 筆界 / 甲土地 / 表題登記がない / 乙土地 / 表題登記がある / 申請人：甲土地の所有者 / 所有権を有することを証する情報は要る？ | — |
| コマ1 | 藍子（左・先に話す） | 本人が所有者なら、証明は要りませんよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。登記の有無が分かれ目よ | 「登記の有無」 |
| コマ2 見出し | ラベル | ②　登記記録で所有者が分かるか | — |
| コマ2 図 | 図・カード | 表題登記がある土地 / 法123条5号 / 申請人：所有権の登記名義人など / 登記記録から所有者を確認できる / 表題登記がない土地 / 申請人：その土地の所有者 / 登記記録に載っていない / 申請適格を裏付ける　所有権を有することを証する情報 / 規則209条1項4号 | — |
| コマ2 | 藍子（左・先に話す） | 登記がない土地だと、何が違うんですか？ | — |
| コマ2 | トリ先生（右・答える） | 記録で所有者を確認できないのよ | 「記録で所有者を確認できない」 |
| コマ3 見出し | ラベル | ③　本番での読み方3ステップ | — |
| コマ3 図 | 図・カード | ステップ1　乙の登記を見る / 乙に表題登記があるので、筆界特定はできる / ステップ2　申請人の土地を見る / 申請人は甲の所有者。甲は登記記録に載らない / ステップ3　証する情報を探す / ひっかけ：証するのは乙でなく甲の所有権 / 甲の所有権を有することを証する情報を提供 | — |
| コマ3 | 藍子（左・1番目） | 所有者本人なのに、証明が要るんですか？ | — |
| コマ3 | トリ先生（右・2番目） | それが罠。甲は記録に載らないのよ | 「甲は記録に載らない」 |
| コマ3 | 藍子（左・3番目） | 乙に登記があれば、省けますか？ | — |
| コマ3 | トリ先生（右・4番目） | 省けないわ。証するのは甲の所有権よ | 「甲の所有権」 |
| コマ4 見出し | ラベル | ④　肢の答えは〇 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 未登記の甲は、自分で示すんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。証する情報を忘れないことよ | 「証する情報」 |
| コマ4 チェック欄 | 3項目（青✓） | 表題登記がない土地の所有者は、所有権を有することを証する情報を提供する / 表題登記がある土地は、登記記録から所有者を確認できる / 証するのは甲の所有権。D1996は〇（提供しなければならない） | — |
| 結論帯 | 1行目 | 未登記の甲は、所有権の証明が要る | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1996　正解〇（R06-Q19イ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記法123条1号・5号、131条1項（note-articles/laws/fudousan-touki-hou.md）
- 不動産登記規則209条1項4号（note-articles/laws/fudousan-touki-kisoku-2.md）

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

TITLE BANNER: text 「表題登記がない土地は、所有権の証明が要る」 in large bold letters; the part 「所有権の証明が要る」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　未登記の甲と登記済みの乙」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- Two plot-of-land blocks side by side in the center, both exactly the same size, separated by a thin plain line labeled 「筆界」 (no arrow). Left block, label 「甲土地」, with a small dark navy tag 「表題登記がない」. Right block, label 「乙土地」, with a small dark navy tag 「表題登記がある」. The two tags are NOT identical.
- Under the left block, a dark navy ribbon with large white text 「申請人：甲土地の所有者」.
- At the top, a small question badge in a gray fill with dark navy text 「所有権を有することを証する情報は要る？」 (a question badge only, with no check mark and no cross).
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, spoken first): 「本人が所有者なら、
証明は要りませんよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
登記の有無が
分かれ目よ」 with the part 「登記の有無」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (藍子 puzzled, トリ先生 explaining with a wing-pointer; 藍子's hands: one hand touches her chin and the other holds the clipboard at her side (two hands in total)):
- Label tab: 「②　登記記録で所有者が分かるか」
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「表題登記がある土地」, small tag 「法123条5号」, two body lines: 「申請人：所有権の登記名義人など」, 「登記記録から所有者を確認できる」.
- Right card, heading 「表題登記がない土地」, small tag 「法123条5号」, two body lines: 「申請人：その土地の所有者」, 「登記記録に載っていない」.
- Under the two cards, one wide dark navy band with large white text 「申請適格を裏付ける　所有権を有することを証する情報」 and a small tag 「規則209条1項4号」 at its right end.
- The two cards have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, spoken first): 「登記がない土地だと、
何が違うんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「記録で所有者を
確認できないのよ」 with the part 「記録で所有者を確認できない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　本番での読み方3ステップ」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three step cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a dark navy number badge, and a dark navy heading, with no check mark and no cross. The step cards are separated only by a small empty gap, with nothing drawn between them.
- Step card 1: heading 「ステップ1　乙の登記を見る」, body 「乙に表題登記があるので、筆界特定はできる」.
- Step card 2: heading 「ステップ2　申請人の土地を見る」, body 「申請人は甲の所有者。甲は登記記録に載らない」.
- Step card 3: heading 「ステップ3　証する情報を探す」, a dark navy ribbon tag with large white text 「ひっかけ：証するのは乙でなく甲の所有権」, body 「甲の所有権を有することを証する情報を提供」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「所有者本人なのに、
証明が要るんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「それが罠。
甲は記録に
載らないのよ」 with the part 「甲は記録に載らない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「乙に登記があれば、
省けますか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「省けないわ。
証するのは
甲の所有権よ」 with the part 「甲の所有権」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　肢の答えは〇」
- 藍子 bubble (left, spoken first): 「未登記の甲は、
自分で示すんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
証する情報を
忘れないことよ」 with the part 「証する情報」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「表題登記がない土地の所有者は、所有権を有することを証する情報を提供する」, 「表題登記がある土地は、登記記録から所有者を確認できる」, 「証するのは甲の所有権。D1996は〇（提供しなければならない）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「未登記の甲は、所有権の証明が要る」 with a yellow highlighter marker.
- Line 2: 「問題D1996　正解〇（R06-Q19イ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two very small characters are drawn as specified and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 号, 地, 所, 権, 無, 番, 登, 肢, 規, 解, 記, 証, 認, 請, 違, 録 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that no triangle, chevron, arrow, or connector is drawn between the stacked step cards; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 表題登記がない甲土地 | 薄い黄色のマーカー |
| タイトル2行目 | 証明書類は要る？ | 「要る？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D1996　R06-Q19イ | — |

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
表題登記がない甲土地
Line 2 is larger; the phrase 要る？ is red-orange and the rest is dark navy:
証明書類は要る？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D1996　R06-Q19イ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: two adjoining plots of land separated by a thin boundary line, one with a blank signpost board
Right side: a blank document sheet and a rubber stamp beside a small registry book

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 表, 題, 登, 記, 甲, 土, 地, 証, 明, 書, 類, 要, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D1996～R06-Q19イ～.png |
| 見出し画像（採用版） | 4コマ解説図解D1996～R06-Q19イ～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D1996～R06-Q19イ～_v01.png ／ 4コマ解説図解D1996～R06-Q19イ～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D1996_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で『甲は表題登記がなく、乙はある。甲の所有者が筆界特定を申請する』、コマ2で『登記記録で所有者が分かるか否かの違い』、コマ3で『証するのは甲の所有権』が言える
- [ ] 工程C：肝の確認：①表題登記がない土地の所有者は所有権を有することを証する情報を提供する（規則209条1項4号） ②表題登記がある土地は登記記録で所有者を確認できる（法123条5号の三区分） ③肢D1996は〇
- [ ] 工程C：構成表の全文言を記事と突き合わせ：『表題登記がない』『所有権を有することを証する情報』『登記記録から所有者を確認できる』『申請適格』（図では申請する資格＝申請人の土地の所有者と言い換えず、記事の語『申請適格』を使う）
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

- 2026-10-10 v01：新規作成（一問一答で4回続けて×と誤答。型は型3。理由＝登記記録で所有者を確認できるか）
