# D1633 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、不動産登記令 第13条と調査士報告方式の取扱いを主役にした4コマ（1本目）のプロンプトです。条文の中身が1枚で言えるように組み、構成表（文言の正本）を含みます。関連する肢（D1633）は、条文のどこで誤りやすいかを示す材料として使っています。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（ブランチ `claude/kind-bell-y3f106` の `tools/drill/manga/`）に従い、同ブランチの生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-10）。下の「作成時の品質ゲート」にある `tools/drill/manga/` のパスは、そのブランチ上のパスです。設計データは `src/spec_4koma_01.py` にあります。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。


- 肢：D1633（不動産登記法／申請総論（申請情報・添付情報・代理・却下取下・還付・電子申請・登記識別情報）、出典 R03-Q04エ）。正解＝×（誤った記述。調査士報告方式なら、委任状原本の提示は省略できる）。誤解の原因は、条文の原則（令13条2項の提示）と、通達による取扱い（報告方式）を区別できず、省略できないと読む。
- 記事：`note-articles/r3-mondai/q04-denshi-shinsei.md` R03-Q04エ（調査士報告方式なら、委任状原本の提示は省略できる。令13条2項の提示の原則に対する、通達による取扱い）を軸に、不動産登記令第13条の1項・2項と、R06-Q05（報告方式の対象は委任状、対象外は承諾書）を対比
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】肢は『当該委任状原本の提示を省略することはできない』と言い切る。令13条2項は『登記官が定めた相当の期間内に書面を提示しなければならない』と書いてあるので、条文を覚えている受験者ほど『条文が提示を求めているのだから、省略できない』と読む。しかし省略の定めは条文になく、通達による取扱い（調査士報告方式）で認められている。条文の原則と通達の取扱いの二層を、肢は1つに混ぜて問うている。
- 【受験者の勘違い・定着していない点】①条文（令13条2項の提示）と、条文にない通達による取扱い（報告方式）が別の層であることを区別できず、条文に書いてあることがすべてだと考える。②令13条1項のかっこ書き（申請人又はその代表者若しくは代理人が作成したものを除く）を見て、申請人側の書面である委任状は特則の外だと考え、報告方式でも別扱いだと思い込む。しかし、報告方式でどの書面が対象になるかの仕分けは、かっこ書きではなく通達による取扱いで決まる。③対象かどうかの軸が『第三者の承諾を証する書面かどうか』であることが定着しておらず、委任状と承諾書を同じ扱いにしてしまう。④『省略することはできない』という否定の言い切りを、厳しい側＝安全側と感じて〇と判断しやすい。
- 【対比する制度】「条文の原則」⇔「通達による取扱い」：令13条2項は、相当の期間内に書面を提示するのが条文の原則／調査士報告方式は、通達による取扱いで、提示を原則として求めない（結論が逆になる点）。あわせて、報告方式の中でも「承諾書」（第三者の承諾を証する書面。対象外で提示が必要）⇔「委任状」（代理人の権限を証する書面。対象で提示は原則不要）で結論が逆になる。
- 【型の選び方】型：型2（しくみ図→押さえどころ→対象と対象外→暗記3点。＋型1の対比）。理由…壁（初見の読者が引っかかる理解の壁）＝条文は提示を求めているのに、なぜ省略できるのか、何が条文で何が通達なのか、どの書面が省略できる側なのかが見えない。肢の言い切りだけを覚えるのでなく、コマ2で『条文の層』と『通達の層』の二層を1枚で見せ、コマ3で対象と対象外の仕分けを見せる構成にした。
- 記事の範囲：R03-Q04エ（調査士報告方式の内容、令13条2項の原則に対する法務省の通達による特例、条文に省略の定めはない）。不動産登記令第13条の条文の抜粋は、法令DB note-articles/laws/fudousan-touki-rei.md の第13条（表示に関する登記の添付情報の特則）で確かめた。1項＝電子申請の表示に関する登記で、添付情報が書面に記載されているとき、その情報を電磁的記録に記録したものを添付情報とすることができる（作成した者による電子署名が必要）。かっこ書き＝申請人又はその代表者若しくは代理人が作成したもの並びに土地所在図、地積測量図、地役権図面、建物図面及び各階平面図を除く。2項＝前項の場合に、申請人は登記官が定めた相当の期間内に、登記官に書面を提示しなければならない。
- extra_refs：対比『委任状は対象、承諾書は対象外』と、判断の軸『第三者の許可・同意・承諾を証する情報かどうか』は、肢の記事（R03-Q04エ）になく、R06-Q05の記事（note-articles/r6-mondai/q05-chousashi-houkoku-houshiki.md。イ＝委任状は対象、ウ＝工事完了引渡証明書は対象、エ・オ＝承諾書は対象外、ア＝地役権設定の範囲を証する書面は承諾書と同じ対象外の側）から取った。令13条1項・2項・かっこ書きの文言は法令DB（note-articles/laws/fudousan-touki-rei.md 第13条）。通達の番号は記事間で表記が揃わず、原文も法令DBにないので、図には入れず『通達による取扱い』とだけ書く。不動産登記規則第93条ただし書（登記官は、調査士が作成した不動産の調査に関する報告があるときなどは、実地調査をしなくてよい）は法令DB（fudousan-touki-kisoku-1.md）で確かめたが、規則93条は実地調査の省略の規定で、令13条2項の提示の省略の根拠ではないので、図には入れない（混同を避けるため）。いずれも肢の記事にない整理で、ユーザーに『記事にない整理』と伝える。
- 記事間の食い違いの疑い（図には入れない）：R06-Q05の記事が自ら指摘しているとおり、令13条1項のかっこ書きは『申請人又はその代表者若しくは代理人が作成したもの』を除いており、委任状は一見この除外に当たるのに、通達の仕分けでは報告方式の対象とされる。この関係を説明する資料は確認できていない。図は『仕分けは条文でなく通達による』とだけ書き、かっこ書きと通達の関係の理由づけは断定しない。また、兄弟肢D1632の記事は、かっこ書きにより申請人が作成した委任状はスキャンしても申請人自身の電子署名が必要と説明する（報告方式でない場合の話）。本図とは矛盾しない。
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない。『申請人』『調査士』を人型タグ、『登記所』を建物アイコンでコマ1で紹介してから使う。『承諾書』『委任状』は書面と名称のラベルで、人物としては描かない。
- 矢印の意味：矢印はコマ1の1本だけ（調査士から登記所へ『電子申請で提供する』）。申請人と調査士の間は矢印のない細い線。コマ2は上下2段の層で、矢印なし（小さなラベルのみ）、コマ3・4も矢印なし。
- 配色：コマ1・2は印（✓✕）を付けない。コマ3は左（承諾書など：提示が必要）＝赤✕1つ、右（委任状など：提示は原則不要）＝青✓1つ。この✓✕は『報告方式で原本の提示が要るか』の意味で、肢の〇×とは別（肢の〇×はコマ4で示す）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、リボン・帯は濃紺の地に白文字、強調は黄色マーカーだけ。
- コマの使い方：コマ1＝side（キャラは通常の大きさ。図は中央）、コマ2＝none（条文の層と通達の層の二層図だけ）、コマ3＝faces（左に2枚のカードとリボン、右に会話の縦並び。会話4つ＝顔4つ＝4行）、コマ4＝既定（両方。暗記3点と結論）。先行版（肢中心。委任状と承諾書の仕分けが中心）と矛盾する主張は書かない。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D1633～R03-Q04エ～

## note記事の冒頭文

電子申請で土地の合筆の登記を申請するとき、令13条2項は書面の提示を求めています。調査士報告方式で申請しても、委任状の原本の提示は省略できないのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（令和3年度　第4問　エ）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 提示は条文の原則、報告方式は通達で省略 | 「報告方式は通達で省略」を黄色マーカー |
| コマ1 見出し | ラベル | ①　問いの事案 | — |
| コマ1 図 | 図・カード | 申請人 / 調査士 / 登記所 / 委任状（原本） / ①　電子申請で提供する / スキャンした委任状、調査士の電子署名、調査に関する報告 / 委任状の原本の提示は、省略できない？ | — |
| コマ1 | 藍子（左・先に話す） | 条文は提示を求めるので、無理ですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。条文と通達を分けて見るのよ | 「条文と通達を分けて」 |
| コマ2 見出し | ラベル | ②　条文の層と通達の層 | — |
| コマ2 図 | 図・カード | 出題者のねらい / 条文の原則と、通達の取扱いを見分ける / 令13条（条文） / 条文の原則 / 1項 / 書面は、電磁的記録にして添付できる / 1項かっこ書き / 申請人・代表者・代理人の作成物と図面は除く / 2項 / 相当の期間内に、登記官へ書面を提示 / 2項の提示について / 調査士報告方式 / 通達による取扱い / 電子署名と調査の報告を添えれば、 / 提示を原則として求めない / どの書面が対象かの仕分けも、条文ではなく通達による | — |
| コマ3 見出し | ラベル | ③　対象と対象外の仕分け | — |
| コマ3 図 | 図・カード | 対象外 / 承諾にかかわる書面 / 承諾書（表題部所有者・抵当権者） / 地役権設定の範囲を証する書面 / 提示が必要 / 対象 / 承諾を証するものではない / 委任状（代理人の権限を証する） / 工事完了引渡証明書 / 提示は原則不要 / ひっかけ：省略することはできない、という言い切り | — |
| コマ3 | 藍子（左・1番目） | 委任状は、申請人側の書面ですよね？ | — |
| コマ3 | トリ先生（右・2番目） | 仕分けは通達の話。承諾を証するかよ | 「承諾を証するか」 |
| コマ3 | 藍子（左・3番目） | では、承諾書はどちらの側ですか？ | — |
| コマ3 | トリ先生（右・4番目） | 対象外よ。承諾書は提示が必要なの | 「対象外」 |
| コマ4 見出し | ラベル | ④　結論は× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 省略できない、は×なんですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。条文と通達を分けて覚えるのよ | 「条文と通達を分けて」 |
| コマ4 チェック欄 | 3項目（青✓） | 令13条2項の提示は条文の原則。報告方式は通達による取扱い / 調査士報告方式なら、委任状の原本の提示を省略できる / 承諾にかかわる書面は対象外。原本の提示が必要 | — |
| 結論帯 | 1行目 | 提示は条文の原則、報告方式は通達で省略できる | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1633　正解×（R03-Q04エ） | — |

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

TITLE BANNER: text 「提示は条文の原則、報告方式は通達で省略」 in large bold letters; the part 「報告方式は通達で省略」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　問いの事案」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A relation diagram in the center of the panel, laid out ONE row from left to right: one faceless pictogram tag in light gray-blue labeled 「申請人」, one faceless pictogram tag in light gray-blue labeled 「調査士」, and one flat registry-office building icon labeled 「登記所」.
- Between 「申請人」 and 「調査士」, one plain thin dark navy line with no arrowhead and a small label 「委任状（原本）」.
- One dark navy arrow from 「調査士」 to 「登記所」 labeled 「①　電子申請で提供する」 (this arrow means submitting the application information, not a sale and not a payment).
- Under the arrow, a white card with a dark navy outline: 「スキャンした委任状、調査士の電子署名、調査に関する報告」.
- A small question badge 「委任状の原本の提示は、省略できない？」 sits at the top (a question badge only, with no check mark and no cross).
- 藍子 bubble (left, spoken first): 「条文は提示を求める
ので、無理ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
条文と通達を分けて
見るのよ」 with the part 「条文と通達を分けて」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　条文の層と通達の層」
- A full-width two-layer diagram fills the whole panel, with a small dark navy tag 「出題者のねらい」 at the top left and a line beside it: 「条文の原則と、通達の取扱いを見分ける」.
- UPPER LAYER: one wide card with the same pale gray fill, a dark navy outline, and the dark navy heading 「令13条（条文）」 with a small dark navy tag 「条文の原則」. Inside it, three small white rows stacked from top to bottom, each with a dark navy heading and one body line. Row 1: heading 「1項」, body 「書面は、電磁的記録にして添付できる」. Row 2: heading 「1項かっこ書き」, body 「申請人・代表者・代理人の作成物と図面は除く」. Row 3: heading 「2項」, body 「相当の期間内に、登記官へ書面を提示」.
- Between the two layers, one small plain dark navy label 「2項の提示について」 (a label only, with no arrow).
- LOWER LAYER: one wide card with the same pale gray fill, a dark navy outline, and the dark navy heading 「調査士報告方式」 with a small dark navy tag 「通達による取扱い」. Body two lines: 「電子署名と調査の報告を添えれば、」 and 「提示を原則として求めない」.
- At the bottom, one wide dark navy band with white text 「どの書面が対象かの仕分けも、条文ではなく通達による」.
- There is no check mark and no cross anywhere in this panel.

PANEL 3 (surprised then convinced mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　対象と対象外の仕分け」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.
- Two cards side by side, both exactly the same size and top-aligned, with the same pale gray fill, a dark navy outline, and a dark navy heading placed fully INSIDE the card.
- Left card, heading 「対象外」, small tag 「承諾にかかわる書面」, two body lines 「承諾書（表題部所有者・抵当権者）」 and 「地役権設定の範囲を証する書面」, then the line 「提示が必要」, with ONE red cross only (no check mark on this card).
- Right card, heading 「対象」, small tag 「承諾を証するものではない」, two body lines 「委任状（代理人の権限を証する）」 and 「工事完了引渡証明書」, then the line 「提示は原則不要」, with ONE blue check mark only (no cross on this card).
- Under the two cards, one dark navy ribbon with large white text 「ひっかけ：省略することはできない、という言い切り」.
- The two cards have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「委任状は、申請人側の
書面ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「仕分けは通達の話。
承諾を証するかよ」 with the part 「承諾を証するか」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「では、承諾書は
どちらの側ですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「対象外よ。承諾書は
提示が必要なの」 with the part 「対象外」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は×」
- 藍子 bubble (left, spoken first): 「省略できない、は
×なんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。
条文と通達を分けて
覚えるのよ」 with the part 「条文と通達を分けて」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「令13条2項の提示は条文の原則。報告方式は通達による取扱い」, 「調査士報告方式なら、委任状の原本の提示を省略できる」, 「承諾にかかわる書面は対象外。原本の提示が必要」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「提示は条文の原則、報告方式は通達で省略できる」 with a yellow highlighter marker.
- Line 2: 「問題D1633　正解×（R03-Q04エ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two very small characters are drawn as specified and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 代, 地, 対, 当, 所, 承, 抵, 権, 渡, 無, 物, 登, 解, 記, 証, 請, 諾, 録, 間 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the left comparison card has only a red cross and the right card only a blue check mark; confirm that the word 「原則」 is spelled exactly like this everywhere (never 「思則」); confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 電子申請の委任状 | 薄い黄色のマーカー |
| タイトル2行目 | 原本の提示は要る？ | 「要る？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D1633　R03-Q04エ | — |

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
電子申請の委任状
Line 2 is larger; the phrase 要る？ is red-orange and the rest is dark navy:
原本の提示は要る？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D1633　R03-Q04エ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a laptop showing an online filing screen beside a small document scanner
Right side: a blank power-of-attorney sheet and a small report paper with a rubber stamp

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 電, 子, 申, 請, 委, 任, 状, 原, 本, 提, 示, 要, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D1633～R03-Q04エ～.png |
| 見出し画像（採用版） | 4コマ解説図解D1633～R03-Q04エ～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D1633～R03-Q04エ～_v01.png ／ 4コマ解説図解D1633～R03-Q04エ～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D1633_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で、申請人・調査士・登記所の関係と、電子申請で何を提供するか（スキャンした委任状、調査士の電子署名、調査に関する報告）が言える。コマ2で、令13条は1項で書面を電磁的記録にして添付でき、2項で書面を提示するのが条文の原則であり、報告方式はその提示を原則として求めない通達による取扱いだと言える。コマ3で、承諾を証する書面は対象外で提示が必要、委任状は対象で提示は原則不要と言える
- [ ] 工程C：肝の確認：①条文の原則（2項の提示）と通達の取扱い（報告方式）で結論が逆 ②報告方式の中でも、承諾書（対象外）と委任状（対象）で結論が逆 ③肢の『省略することはできない』は、委任状が対象なので×
- [ ] 工程C：構成表の全文言を記事・法令DBと突き合わせ：『令13条』『1項』『2項』『登記官が定めた相当の期間内に書面を提示する』『申請人又はその代表者若しくは代理人が作成したもの並びに土地所在図等の図面を除く』（法令DB令第13条）、『調査士報告方式』『通達による取扱い』（R03-Q04エ）、『代理人の権限を証する書面』『承諾にかかわる書面』『対象外』（R06-Q05）。通達番号・規則93条は図に入れていない
- [ ] 工程C：コマ1・2に印がなく、コマ3は左赤✕・右青✓、コマ4だけ青✓の暗記3点。コマの使い方が隣り合うコマで同じにならない（side→none→faces→両方）

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

- 2026-10-10 v01：新規作成（条文を主役にした版。不動産登記令第13条の1項・かっこ書き・2項と、通達による調査士報告方式の二層構造、対象と対象外の仕分け。型2＋型1の対比）
