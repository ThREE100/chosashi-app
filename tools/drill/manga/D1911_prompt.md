# D1911 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

- 肢：D1911（民法／物権変動・対抗要件、出典 R06-Q02ア）。正解＝×（誤った記述）。誤解〇と答えて誤解が3回（2026-10-04・10-05・10-11）。10-06だけ×で正解。
- 記事：`note-articles/r6-mondai/q02-taikouyouken.md` R06-Q02ア「ＡＣ間の売買の時点でＡＢ間の売買についてＣが悪意であったときは、Ｂは登記なしでＣに対抗できる」は誤り。単純悪意者も177条の第三者に含まれる。除外される主な者（当事者本人・包括承継人・前主後主・不法占拠者・背信的悪意者）は、同じ記事と note-articles/topics/taikouyouken-daisansha-5ruikei.md の整理
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】問題文は『ＡＢ間の売買についてＣが悪意であったとき』としか書かず、背信的悪意者とは書いていない。『悪意＝事情を知って買った＝ずるい買い方』と読み替えさせ、『ずるい人は保護されないから、Ｂは登記なしで対抗できる』と思わせる。ひっかけの根拠は問題文の『悪意であったとき』。
- 【受験者の勘違い・定着していない点】①『知っていて買った悪意者は保護に値しない』という道徳的な感覚で判断する。②悪意（事情を知っていただけ）と背信的悪意（自由競争の範囲を逸脱し、もっぱら相手を害する目的で買い受ける）を同じものと見て、線引きが見えていない。③第三者から除外される者（背信的悪意者など）が具体的に決まっていることを覚えていないため、『悪意』が除外の一つのように見える。（①〜③は、回答履歴から立てた推測。3回とも〇と答えて誤解で、10-06だけ×と答えて正解している。結論を理由なく暗記した回だけ当たり、直感に戻ると〇に戻る形。同じ問の兄弟肢のうち、同じ誤りの相手は『ずるい人は保護されない』という感覚で、兄弟肢D1912〈買受人〉・D1914〈相続人〉ではない）
- 【対比する制度】「単純悪意」⇔「背信的悪意」：単純悪意（事情を知っていただけ）は自由な取引の範囲内にとどまるので第三者に含まれ、Ｂは登記がなければ対抗できない。背信的悪意（自由競争の範囲を逸脱し、もっぱら相手を害する目的で買い受ける）は第三者から除外され、Ｂは登記なしで対抗できる（結論が逆になる点）。
- 【型の選び方】型：型3（第三案・理由説明）に型2のしくみ図（第三者から除外される主な者の一覧）を足した混成。理解の壁＝『知って買ったずるい人が、なぜ第三者として保護されるのか』が分からず、悪意と背信的悪意の線引きが見えない。3回〇と答えて誤解しているので、結論の暗記ではなく理由（知っていただけは自由な取引の範囲内）が読み取れる構成にした。コマ1＝事案と思い込み、コマ2＝除外される主な者の一覧と、この肢のＣの置き場所、コマ3＝理由の対比（単純悪意⇔背信的悪意）、コマ4＝結論。
- 記事の範囲：R06-Q02ア（単純悪意者も177条の第三者に含まれ、Ｂは登記がなければ対抗できない。『知っていた』というだけでは自由な取引の範囲内にとどまり、信義則に反するとまではいえない）。除外される主な者は肢アの記事の本文と、topics記事の記述（記事は『5つに限られる』と書くが、不動産登記法第5条にも登記がないことを主張できない第三者の定めがあるため、図では『主なもの』と書き、『限られる』『だけ』とは書かない）。背信的悪意者の定義は肢アの記事の『自由競争の範囲を逸脱してもっぱら相手を害する目的で買い受けるような』を使う。
- 登場人物：Ａ（売主）・Ｂ（先に買った人）・Ｃ（あとで買った人）の3人。全員コマ1の図で紹介してから使う。ピクトグラムは全員同じ色。
- 矢印の意味：矢印は使わない。コマ1は人型の一列とカード、コマ2は一覧のカードと帯、コマ3は上下2枚のカードとリボン。
- 配色：コマ1〜3は印（✓✕）を付けない（対抗できる・できないは文字で書く）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方：コマ1＝side（キャラは通常の大きさで左右の端。図は中央）、コマ2＝tori（トリ先生だけ。一覧が主役）、コマ3＝faces（左に上下2枚のカードとリボン、右に会話の縦並び。会話4つ＝顔4つ＝4行）、コマ4＝既定（暗記3点と結論）。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D1911～R06-Q02ア～

## note記事の冒頭文

ＡがＢに甲土地を売った後、登記がされないうちに、ＡがＣにも甲土地を売りました。ＣはＡＢ間の売買を知っていました。Ｂは、登記がなくてもＣに所有権の取得を対抗できるのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（令和6年度　第2問　ア）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 悪意だけでは、登記なしで対抗できない | 「登記なしで対抗できない」を黄色マーカー |
| コマ1 見出し | ラベル | ①　ＡがＢとＣに売った事案 | — |
| コマ1 図 | 図・カード | Ａ / Ｂ / Ｃ / 売主 / 先に買った人 / あとで買った人 / 先に / ＡがＢに売った / Ｂは登記をしていない / あとで / ＡがＣにも売った / Ｃは、ＡＢ間の売買を知っていた（悪意） / 悪意 / Ｂは、登記なしでＣに対抗できる？ | — |
| コマ1 | 藍子（左・先に話す） | 知っていて買ったなら、登記なしで勝てますよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。悪意の中身を見なさい | 「悪意の中身」 |
| コマ2 見出し | ラベル | ②　第三者から除外される者の主なもの | — |
| コマ2 図 | 図・カード | 出題者のねらい / 第三者から除外される者を、言えるか / 第三者から除外される者（主なもの） / 当事者本人 / 包括承継人（相続人など） / 前主・後主の関係にある者 / 不法占拠者 / 背信的悪意者 / 肢D1914はここ / この肢のＣ / 知っていただけ（単純悪意） / 上の5つには入らない / 入らなければ、原則どおり第三者に含まれる | — |
| コマ2 | トリ先生（右・答える） | 悪意だけでは、除外されないのよ | 「除外されない」 |
| コマ3 見出し | ラベル | ③　なぜ、悪意でも第三者なのか | — |
| コマ3 図 | 図・カード | 単純悪意（知っていただけ） / 自由な取引の範囲内にとどまる / 信義則に反するとまではいえない / 第三者に含まれる / 背信的悪意（害する目的） / 自由競争の範囲を逸脱する / もっぱら相手を害する目的で買い受ける / 第三者から除外される / ひっかけ：悪意であったとき | — |
| コマ3 | 藍子（左・1番目） | 知っていたのに、勝てないんですか？ | — |
| コマ3 | トリ先生（右・2番目） | 知っていただけなら、自由な取引の範囲内よ | 「自由な取引の範囲内」 |
| コマ3 | 藍子（左・3番目） | ではＣが除外されるのは、どんなときですか？ | — |
| コマ3 | トリ先生（右・4番目） | もっぱら害する目的の背信的悪意者のときよ | 「背信的悪意者」 |
| コマ4 見出し | ラベル | ④　結論は× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 悪意だけでは、足りないんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。背信的悪意かどうかを見るのよ | 「背信的悪意」 |
| コマ4 チェック欄 | 3項目（青✓） | 知っていただけの悪意者も、177条の第三者に含まれる / 背信的悪意者など第三者から除外される者には、登記なしで対抗できる / Ｃが悪意でも、Ｂは登記がなければ対抗できない（D1911は×） | — |
| 結論帯 | 1行目 | 悪意だけでは、Ｂは登記なしで対抗できない | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1911　正解×（R06-Q02ア） | — |

## 記事に無い条文（ユーザー指示で追加）

- 民法第177条（法令DB note-articles/laws/minpou-1-soukyoku-bukken.md で原文を確認）：不動産に関する物権の得喪及び変更は、不動産登記法その他の登記に関する法律の定めるところに従いその登記をしなければ、第三者に対抗することができない。条文は『第三者』とだけ書き、善意などの限定は書いていない。図には条文番号を入れていない。
- R06-Q02エ（肢D1914。note-articles/r6-mondai/q02-taikouyouken.md の同じ記事）：相続人は被相続人を包括承継するので、Ｂは登記なしで対抗できる。コマ2の一覧で『包括承継人（相続人など）』の行に『肢D1914はここ』のタグを付けるのに使った。新しい整理は足していない。
- 除外される者の5類型と『入らなければ原則どおり第三者に含まれる』は、肢アの記事の本文と note-articles/topics/taikouyouken-daisansha-5ruikei.md の記述。ただし記事の『5つに限られる』は、不動産登記法第5条（詐欺又は強迫によって登記の申請を妨げた第三者、他人のために登記を申請する義務を負う第三者は、登記がないことを主張できない。法令DB note-articles/laws/fudousan-touki-hou.md で確認）と食い違う疑いがあるので、図では『主なもの』とし、法第5条は図に入れない。判例の事件番号も図に入れない。

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

TITLE BANNER: text 「悪意だけでは、登記なしで対抗できない」 in large bold letters; the part 「登記なしで対抗できない」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　ＡがＢとＣに売った事案」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center region (about 56 percent of the panel width), with no arrow, no check mark, and no cross. Three faceless person pictograms stand in ONE row from left to right, all the same size and all in the same single light gray-blue color, each with a dark navy name tag: 「Ａ」, 「Ｂ」, 「Ｃ」. Under the row, three small dark navy labels, one under each person: 「売主」 under Ａ, 「先に買った人」 under Ｂ, 「あとで買った人」 under Ｃ.
- Under the labels, two white cards with dark navy outlines stacked top to bottom with a small empty gap, each with a dark navy heading placed inside the card. Top card, heading 「先に」, body 「ＡがＢに売った」 and 「Ｂは登記をしていない」. Bottom card, heading 「あとで」, body 「ＡがＣにも売った」 and 「Ｃは、ＡＢ間の売買を知っていた（悪意）」, the part 「悪意」 with a yellow highlighter marker.
- A small question badge 「Ｂは、登記なしでＣに対抗できる？」 with a pale gray fill and a dark navy outline sits at the top of the center region (a question badge only, with no check mark and no cross).
- 藍子 bubble (left, spoken first): 「知っていて買ったなら、
登記なしで勝てますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
悪意の中身を見なさい」 with the part 「悪意の中身」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (calm, explaining mood; ONLY トリ先生 appears in this panel (no 藍子), standing at the right and smaller than usual, so that the diagram or the items to memorize can be drawn large):
- Label tab: 「②　第三者から除外される者の主なもの」
- A concept diagram fills the center-left region, with no arrow, no check mark, and no cross. At the top left, a small dark navy tag 「出題者のねらい」 and, beside it, one line 「第三者から除外される者を、言えるか」.
- Below, two cards side by side, top-aligned, both with the same pale gray fill, a dark navy outline, and a dark navy heading placed fully inside the card. Left card (wider), heading 「第三者から除外される者（主なもの）」, five body lines, each at least 24 px high: 「当事者本人」, 「包括承継人（相続人など）」, 「前主・後主の関係にある者」, 「不法占拠者」, 「背信的悪意者」, the part 「背信的悪意者」 with a yellow highlighter marker; a small dark navy tag 「肢D1914はここ」 sits at the right end of the line 「包括承継人（相続人など）」.
- Right card (narrower), heading 「この肢のＣ」, two body lines: 「知っていただけ（単純悪意）」, 「上の5つには入らない」.
- At the bottom, one wide dark navy band with large white text 「入らなければ、原則どおり第三者に含まれる」.
- The two cards have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- トリ先生 bubble (right, spoken as the answer): 「悪意だけでは、
除外されないのよ」 with the part 「除外されない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ、悪意でも第三者なのか」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Two cards stacked from top to bottom, both the same size, each with a pale gray fill, a dark navy outline, and a dark navy heading placed fully inside the card, with no check mark and no cross. The two cards are separated only by a small empty gap, with nothing drawn between them.
- Top card, heading 「単純悪意（知っていただけ）」, two body lines: 「自由な取引の範囲内にとどまる」, 「信義則に反するとまではいえない」, and a small dark navy tag 「第三者に含まれる」.
- Bottom card, heading 「背信的悪意（害する目的）」, two body lines: 「自由競争の範囲を逸脱する」, 「もっぱら相手を害する目的で買い受ける」, and a small dark navy tag 「第三者から除外される」.
- Under the two cards, a dark navy ribbon tag with large white text 「ひっかけ：悪意であったとき」, the same size as the card body text.
- The two cards have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「知っていたのに、
勝てないんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「知っていただけなら、
自由な取引の範囲内よ」 with the part 「自由な取引の範囲内」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「ではＣが除外されるのは、
どんなときですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「もっぱら害する目的の
背信的悪意者のときよ」 with the part 「背信的悪意者」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は×」
- 藍子 bubble (left, spoken first): 「悪意だけでは、
足りないんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。背信的悪意かどうかを
見るのよ」 with the part 「背信的悪意」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「知っていただけの悪意者も、177条の第三者に含まれる」, 「背信的悪意者など第三者から除外される者には、登記なしで対抗できる」, 「Ｃが悪意でも、Ｂは登記がなければ対抗できない（D1911は×）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「悪意だけでは、Ｂは登記なしで対抗できない」 with a yellow highlighter marker.
- Line 2: 「問題D1911　正解×（R06-Q02ア）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two very small characters are drawn as specified and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 占, 売, 対, 当, 承, 抗, 登, 肢, 解, 記, 買, 間 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the word 「原則」 is spelled exactly like this everywhere (never 「思則」); confirm that the word 「第三者」 is spelled exactly like this everywhere (never 「時三者」); confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 知っていて買った人に | 薄い黄色のマーカー |
| タイトル2行目 | 登記なしで対抗できる？ | 「対抗できる？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D1911　R06-Q02ア | — |

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
知っていて買った人に
Line 2 is larger; the phrase 対抗できる？ is red-orange and the rest is dark navy:
登記なしで対抗できる？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D1911　R06-Q02ア
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a plot of land with a blank signboard and a small house key lying beside it
Right side: an open registry book with blank form fields, a rubber stamp, and a small balance scale

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 知, 買, 人, 登, 記, 対, 抗, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D1911～R06-Q02ア～.png |
| 見出し画像（採用版） | 4コマ解説図解D1911～R06-Q02ア～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D1911～R06-Q02ア～_v01.png ／ 4コマ解説図解D1911～R06-Q02ア～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D1911_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1の図で、ＡがＢとＣに二重に売り、Ｂは未登記、Ｃは事情を知っていた（悪意）という事案と、問われているのが『Ｂは登記なしでＣに対抗できるか』であることが言える
- [ ] 工程C：肝の確認：①第三者から除外される主な者は、当事者本人・包括承継人・前主後主・不法占拠者・背信的悪意者 ②知っていただけの単純悪意者はどれにも当てはまらず第三者に含まれる ③自由競争の範囲を逸脱しもっぱら相手を害する目的の背信的悪意者だけが除外される ④したがって本肢は×
- [ ] 工程C：構成表の全文言を記事と突き合わせ：『単純悪意者』『自由競争の範囲』『もっぱら相手を害する目的』『背信的悪意者』『第三者』『信義則に反するとまではいえない』『原則どおり第三者に含まれる』（肢アの記事、topics記事）。法令DBで民法177条の原文を確認済み
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方が隣り合うコマで同じにならない（side→tori→faces→既定）。判例の事件番号・丸数字⑤は図に入れていない

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

- 2026-10-11 v01：新規作成（一問一答で〇と答えて3回誤解した肢。型は型3＋型2の一覧。悪意と背信的悪意の対比を、除外される5つの一覧と理由の対比カードで示した）
