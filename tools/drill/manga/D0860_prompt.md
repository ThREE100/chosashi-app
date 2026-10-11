# D0860 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

- 肢：D0860（不動産登記法／建物の認定・個数・種類構造床面積、出典 R05-Q17オ／H25-Q11イ）。正解＝×（誤った記述。不動産番号を申請情報の内容としたときは、家屋番号を申請情報の内容とすることを要しない）。誤解2回の出題で、〇（誤解）が1回、？（わからない）が2回、×（正解）が1回。
- 記事：`note-articles/r5-mondai/q17-kyouyoububun.md` R05-Q17オ（不動産番号を書けば、団地共用部分である旨の登記でも家屋番号は省略できる。令6条2項4号）と、同じ肢のH25-Q11イ（別表19項申請情報欄イ・令6条2項4号）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】問題文の『不動産番号を申請情報の内容とするときであっても、…家屋番号を申請情報の内容としなければならない』。『であっても』で、不動産番号を書く場合にも例外として家屋番号が要るように読ませ、『しなければならない』の言い切りで押し切る。別表19項申請情報欄イが建物の所在・地番・家屋番号を求めている事実も、『家屋番号は要る』という読みを後押しする。
- 【受験者の勘違い・定着していない点】（以下はすべて推測。根拠は回答履歴：同じ肢が2つの年度で出て、〇（誤解）が1回、？が2回、×が1回で、答えが安定していない）①別表19項申請情報欄イが家屋番号を個別に求めているので、不動産番号を書いても、別表が求める家屋番号まで省けるとは思わない。②令6条の『省略できる』を、令6条1項（令3条7号・8号の建物の表示）の話だけだと思い、令6条2項4号が別表19項イを名指しで省略できると定めている点が定着していない。③同じ問のア（分割の登記は分割前の家屋番号が要る・×）を先に解くと、『家屋番号は書くもの』という感覚が先に立つ。
- 【対比する制度】「不動産番号を書かないとき」⇔「不動産番号を書いたとき」：書かないときは、別表19項イの建物の所在・地番と家屋番号を申請情報に書く／書いたときは、建物の所在・地番と家屋番号を書かなくてよい（令6条2項4号）（同じ団地共用部分である旨の登記でも、番号を書いたかどうかで結論が逆になる点）。
- 【型の選び方】型：型2（第二案・押さえどころ）（＋型1の対比を押さえどころのカードに入れた混成）。理由…壁（初見の読者が引っかかる理解の壁）＝別表が家屋番号を個別に求めているのに、不動産番号を書くとその家屋番号まで省けるのはなぜか、どこまで省けるのかが見えない。誤答の型より、省略の範囲（令6条2項4号が別表19項イを名指ししている）が見えないことが問題なので、しくみ→書かない⇔書くの押さえどころ→読み方3ステップ→暗記3点の順に組んだ。回答履歴の誤りの向きが安定していない（〇・？・×・？）ので、『なぜ省けるか』より、『どの場面でどこまで省けるか』を先に言えるようにする。
- 記事の範囲：R05-Q17オ（不動産番号を書けば、土地なら所在・地番・地目・地積、建物なら所在・地番・家屋番号を省略できる〈令6条1項〉。団地共用部分である旨の登記〈令別表19項〉の申請情報欄イの建物の所在・地番・家屋番号も、不動産番号を書いたときは省略できる〈令6条2項4号〉。不動産番号は不動産識別事項〈規則34条2項〉）、H25-Q11イ（同じ結論。区分建物でない建物の場合の別表19項申請情報欄イ）。記事の『たとえば』（団地共用部分とする建物の不動産番号を申請書に書いておけば、家屋番号を重ねて書く必要はない）を使う。
- extra_refs：①不動産登記規則34条3項（令6条の省略は、他の登記所の管轄区域内にある不動産の事項については、不動産番号と併せてその登記所の表示を申請情報の内容としたときに限り適用する）は法令DB（note-articles/laws/fudousan-touki-kisoku-1.md、同 R6-0624-version）で確認した。肢の記事にはなく、コマ2の帯に『ただし書き』として入れる。②不動産番号が『不動産を識別するために必要な事項』であること（令6条1項本文）は法令DB（note-articles/laws/fudousan-touki-rei.md）で確認した。コマ2の『番号は建物を識別する』は、記事の『物件を一発で特定できる番号』と令6条本文（不動産を識別するために必要な事項）の言い方にそろえた。いずれも『記事にない整理』としてユーザーに伝える。
- 今回は図に入れないもの：①別表19項ロ（区分建物のとき）は令6条2項4号に挙がっていない（挙がっているのはイだけ）。肢が『区分建物でない建物』と限定しているので、コマ1の図に『区分建物でない』と書くにとどめ、ロの扱いは図で断定しない。②同じ問のア（D0859。分割の登記は分割前の家屋番号が要る・×）は、記事が『不動産番号を書かない場合』と明示していないので、図に入れない（図に置くと、分割の登記は不動産番号を書いても家屋番号が要る、と読めてしまうおそれがあり、記事の範囲を超える）。③規則34条4項（表題登記では不動産番号を書いても令3条7号・8号の事項は省けない）は、団地共用部分である旨の登記の肢とは別の場面なので入れない。④記事の『たとえば』の『12桁の番号』は、法令DBに桁数の規定がなく、図に入れない。
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない。建物・申請書は文字ラベルつきのアイコンで示す。
- 矢印の意味：矢印は使わない。コマ1は建物と申請書のカード、コマ2は左右のカード、コマ3は3枚のステップカード。
- 配色：コマ1〜3は印（✓✕）を付けない（要る・要らないは文字で書く）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠・濃紺の見出し、帯・リボンは濃紺の地に白文字、強調は黄色マーカーだけ。
- コマの使い方：コマ1＝side（キャラは通常の大きさ。図は中央に申請書を大きく）、コマ2＝none（書かない⇔書くのカード）、コマ3＝faces（左に3枚のステップカード、右に会話の縦並び。会話4つ＝顔4つ＝4行）、コマ4＝両方（暗記3点と結論）。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D0860～R05-Q17オ／H25-Q11イ～

## note記事の冒頭文

団地共用部分である旨の登記を、区分建物でない建物について申請します。その建物の不動産番号を申請情報に書いたときでも、建物の家屋番号まで書かなければならないのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（令和5年度　第17問　オ／平成25年度　第11問　イ）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 不動産番号を書けば、家屋番号は省略できる | 「家屋番号は省略できる」を黄色マーカー |
| コマ1 見出し | ラベル | ①　問いの事案 | — |
| コマ1 図 | 図・カード | 団地の建物 / 区分建物でない / 団地共用部分である旨の登記 / 不動産番号 / 書いた / 建物の所在・地番 / 家屋番号 / 別表19項イ / 不動産番号を書いても、家屋番号は要る？ | — |
| コマ1 | 藍子（左・先に話す） | 番号を書いても、家屋番号は要りますよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。番号を書いたかを見てごらん | 「番号を書いた」 |
| コマ2 見出し | ラベル | ②　書かないとき⇔書いたとき | — |
| コマ2 図 | 図・カード | 押さえどころ / 番号は建物を識別する。書いたかどうかで、書く事項が変わる / 書いたかどうか / 不動産番号を書かないとき / 別表19項イ / 建物の所在・地番と家屋番号を、申請情報に書く / 不動産番号を書いたとき / 令6条2項4号 / 建物の所在・地番と家屋番号は、書かなくてよい / ただし、他の登記所の不動産は、不動産番号と登記所の表示を併せて書く（規則34条3項） | — |
| コマ3 見出し | ラベル | ③　本番での読み方3ステップ | — |
| コマ3 図 | 図・カード | ステップ1　どの登記かを見る / 団地共用部分である旨の登記。区分建物でない建物 / ステップ2　不動産番号を書いたか / 令6条2項4号 / 書いたなら、建物の所在・地番と家屋番号は省ける / ステップ3　言い切りの語を見る / ひっかけ：であっても、しなければならない / この場面で、家屋番号を書かなければならないは誤り | — |
| コマ3 | 藍子（左・1番目） | であっても、とあるので要るのでは？ | — |
| コマ3 | トリ先生（右・2番目） | それが罠。番号があれば省けるのよ | 「番号があれば省ける」 |
| コマ3 | 藍子（左・3番目） | では、何が書かなくてよいんですか？ | — |
| コマ3 | トリ先生（右・4番目） | 建物の所在、地番、家屋番号よ | 「建物の所在、地番、家屋番号」 |
| コマ4 見出し | ラベル | ④　これだけ覚える | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 番号を書けば、家屋番号は省けるんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。書かなければならない、は誤りよ | 「書かなければならない」 |
| コマ4 チェック欄 | 3項目（青✓） | 不動産番号を書けば、建物の所在・地番と家屋番号は省ける（令6条2項4号） / 不動産番号を書かないなら、別表19項イの建物の所在・地番と家屋番号を書く / 番号を書いても家屋番号を書かなければならない、は× | — |
| 結論帯 | 1行目 | 不動産番号を書けば、家屋番号は省略できる | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0860　正解×（R05-Q17オ／H25-Q11イ） | — |

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

TITLE BANNER: text 「不動産番号を書けば、家屋番号は省略できる」 in large bold letters; the part 「家屋番号は省略できる」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　問いの事案」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center of the panel (about 56 percent of the panel width): on the left one flat low building icon labeled 「団地の建物」 with a small tag 「区分建物でない」; on the right one large white application-form card with a dark navy outline and the dark navy heading 「団地共用部分である旨の登記」.
- Inside the form card, three field rows of the same pale gray fill and a dark navy outline, each text at least 24 px high, with no check mark, no cross, and no arrow: row 1 「不動産番号」 with a small tag 「書いた」; row 2 「建物の所在・地番」; row 3 「家屋番号」. A thin dark navy bracket on the right side of rows 2 and 3 carries a small label 「別表19項イ」.
- A small question badge 「不動産番号を書いても、家屋番号は要る？」 sits at the top (a question badge only, with no check mark and no cross).
- 藍子 bubble (left, spoken first): 「番号を書いても、
家屋番号は
要りますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
番号を書いたかを
見てごらん」 with the part 「番号を書いた」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　書かないとき⇔書いたとき」
- A full-width concept diagram fills the whole panel, with a small dark navy tag 「押さえどころ」 at the top left and a line beside it: 「番号は建物を識別する。書いたかどうかで、書く事項が変わる」, with the part 「書いたかどうか」 in a yellow highlighter marker.
- Two large cards side by side, both exactly the same size and top-aligned, each with the same pale gray fill, a dark navy outline, and a dark navy heading placed fully INSIDE the card, separated by a tall plain dark navy divider line (no arrow), with no check mark and no cross. Left card, heading 「不動産番号を書かないとき」, small tag 「別表19項イ」, body 「建物の所在・地番と家屋番号を、申請情報に書く」. Right card, heading 「不動産番号を書いたとき」, small tag 「令6条2項4号」, body 「建物の所在・地番と家屋番号は、書かなくてよい」.
- At the bottom, one wide dark navy band with white text 「ただし、他の登記所の不動産は、不動産番号と登記所の表示を併せて書く（規則34条3項）」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　本番での読み方3ステップ」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three step cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a dark navy number badge, and a dark navy heading, with no check mark and no cross. The step cards are separated only by a small empty gap, with nothing drawn between them.
- Step card 1: heading 「ステップ1　どの登記かを見る」, body 「団地共用部分である旨の登記。区分建物でない建物」.
- Step card 2: heading 「ステップ2　不動産番号を書いたか」, small tag 「令6条2項4号」, body 「書いたなら、建物の所在・地番と家屋番号は省ける」.
- Step card 3: heading 「ステップ3　言い切りの語を見る」, a dark navy ribbon tag with large white text 「ひっかけ：であっても、しなければならない」, body 「この場面で、家屋番号を書かなければならないは誤り」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「であっても、
とあるので
要るのでは？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「それが罠。
番号があれば
省けるのよ」 with the part 「番号があれば省ける」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「では、何が
書かなくて
よいんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「建物の所在、
地番、家屋番号よ」 with the part 「建物の所在、地番、家屋番号」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　これだけ覚える」
- 藍子 bubble (left, spoken first): 「番号を書けば、
家屋番号は
省けるんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。書かなければ
ならない、は
誤りよ」 with the part 「書かなければならない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「不動産番号を書けば、建物の所在・地番と家屋番号は省ける（令6条2項4号）」, 「不動産番号を書かないなら、別表19項イの建物の所在・地番と家屋番号を書く」, 「番号を書いても家屋番号を書かなければならない、は×」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「不動産番号を書けば、家屋番号は省略できる」 with a yellow highlighter marker.
- Line 2: 「問題D0860　正解×（R05-Q17オ／H25-Q11イ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 号, 地, 建, 所, 押, 物, 番, 登, 規, 解, 記, 請 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that no triangle, chevron, arrow, or connector is drawn between the stacked step cards; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 不動産番号を書いたとき | 薄い黄色のマーカー |
| タイトル2行目 | 家屋番号は要る？ | 「要る？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D0860　R05-Q17オ／H25-Q11イ | — |

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
不動産番号を書いたとき
Line 2 is larger; the phrase 要る？ is red-orange and the rest is dark navy:
家屋番号は要る？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D0860　R05-Q17オ／H25-Q11イ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a cluster of low residential buildings on shared land with a blank house-number plate
Right side: an application form with a blank number tag attached and a rubber stamp beside a small registry book

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written (cartoon expression marks such as ！ and ？ beside the characters' faces are decoration, are allowed, and are not extra text); scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 不, 動, 産, 番, 号, 書, 家, 屋, 要, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere. Never delete, redo, or regenerate anything because of an expression mark or a symbol beside a character; deliver the first image as it is.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D0860～R05-Q17オ／H25-Q11イ～.png |
| 見出し画像（採用版） | 4コマ解説図解D0860～R05-Q17オ／H25-Q11イ～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D0860～R05-Q17オ／H25-Q11イ～_v01.png ／ 4コマ解説図解D0860～R05-Q17オ／H25-Q11イ～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0860_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で、団地共用部分である旨の登記を、区分建物でない建物について申請し、申請情報に不動産番号を書く場面だと言える。コマ2で、不動産番号を書かないなら建物の所在・地番と家屋番号を書き、書いたなら書かなくてよい（令6条2項4号）と言える。コマ3で、『であっても、しなければならない』が罠だと言える
- [ ] 工程C：肝の確認：①番号を書かないとき⇔書いたときで結論が逆 ②令6条2項4号が別表19項イを名指しで省略可としている ③肢の『家屋番号を書かなければならない』は×
- [ ] 工程C：構成表の全文言を記事と突き合わせ：『別表19項イ』『令6条2項4号』『建物の所在・地番と家屋番号』『不動産番号』『区分建物でない建物』（R05-Q17オ・H25-Q11イ）。『他の登記所』『登記所の表示』『規則34条3項』は記事になく、法令DBで確認した（extra_refs）。条文番号は令別表19項・令6条2項4号・規則34条3項のみ。
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方が隣り合うコマで同じにならない（side→none→faces→両方）。コマ3の会話4つが、ステップカードの文言と1対1で対応している

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

- 2026-10-11 v01：新規作成（一問一答で誤解・未習得が重なった肢。型は型2＋型1の対比。法令DBで令6条2項4号・規則34条3項を確認）
