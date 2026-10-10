# D1596・D1728・D2023 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、不動産登記規則 第28条・第28条の2（保存期間）を主役にした4コマ（1本目）のプロンプトです。条文の中身が1枚で言えるように組み、構成表（文言の正本）を含みます。関連する肢（D1596・D1728・D2023）は、条文のどこで誤りやすいかを示す材料として使っています。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（ブランチ `claude/kind-bell-y3f106` の `tools/drill/manga/`）に従い、同ブランチの生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-10）。下の「作成時の品質ゲート」にある `tools/drill/manga/` のパスは、そのブランチ上のパスです。設計データは `src/spec_4koma_01.py` にあります。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。


- 肢：D1596・D1728・D2023（不動産登記法／登記制度・総則（保存期間）、出典 R02-Q17イ／R04-Q04イ／R07-Q05ア）。正解＝D1596＝〇・D1728＝×・D2023＝×（D1728は『30年間』が誤り。正しくは5年間。D2023は『永久』が誤り。正しくは閉鎖した日から50年間）。誤解の原因（一般論）：保存期間の肢で、年数と数え始めの日が情報ごとに違うことが定着していない形（条文の号ごとの当てはめができていない）。
- 記事：`note-articles/r2-mondai/q17-tatemono-messhitsu.md` 不動産登記規則第28条（1号・4号・5号・9号・10号）と第28条の2（6号）の保存期間を軸に、R02-Q17イ（建物の滅失の登記の申請情報・添付情報は受付の日から30年間。規則28条9号）、R04-Q04イ（法定相続情報一覧図つづり込み帳は作成の年の翌年から5年間。規則28条の2第6号）、R07-Q05ア（土地に関する閉鎖登記記録は閉鎖した日から50年間。規則28条）を対比
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】規則第28条・第28条の2は、情報の種類ごとに号を分けて、数え始めの日と年数を別々に定めている。出題者は、そのうちの年数だけを入れ替える（法定相続情報一覧図つづり込み帳に、申請情報の『30年間』をそのまま持ち込む。土地の閉鎖登記記録に、閉鎖前の登記記録の『永久』を持ち込む）。保存期間の肢は、数字が『30年』で並ぶものが多いので、どれも30年に見える。
- 【受験者の勘違い・定着していない点】①『保存期間はどれも30年』という印象で、情報の種類を読まずに年数を決める。②『登記記録は大事だから、閉鎖した後も永久』と考える。永久なのは閉鎖前の登記記録で、閉鎖すると土地は50年、建物は30年の年数が付くことが定着していない。③『滅失の登記の書類は特別な扱いではないか』と疑う。表示に関する登記の申請情報・添付情報は、滅失の登記も含めて受付の日から30年間で一律。④数え始めの日が、閉鎖した日・受付の日・作成の年の翌年と違うことを区別していない。
- 【対比する制度】「閉鎖前の登記記録」⇔「土地の閉鎖登記記録」：閉鎖前の登記記録は永久。土地の閉鎖登記記録は閉鎖した日から50年間（建物の閉鎖登記記録は30年間）。永久という結論が、閉鎖の前後で変わる。もう1組は「申請情報」⇔「法定相続情報一覧図つづり込み帳」：表示に関する登記の申請情報及び添付情報は受付の日から30年間。つづり込み帳は作成の年の翌年から5年間。数え始めの日と年数が、情報の種類で違う。
- 【型の選び方】型：型2（＋型4の対比）。理由…壁＝『規則第28条・第28条の2は、情報の種類ごとに数え始めの日と年数を号で分けているのに、どれも30年に見えて、号ごとの当てはめができていない』。条文の側から1枚で言えるように、コマ1で『何の情報か・いつから・何年か』の3点セットを示し、コマ2で6つの号を並べた当てはめ表（印なし）、コマ3で読み方3ステップ、コマ4で暗記3点と3つの肢の〇×にした。保存期間の年数は条文が号で定めているだけで、記事にも条文にも『なぜその年数か』の理由はないので、理由コマ（型3）は作らず、当てはめの手順を理由代わりにした。
- 記事の範囲：R02-Q17イ（表示に関する登記の申請情報及び添付情報は受付の日から30年間。建物の滅失の登記もこれに含まれる。規則28条9号）、R04-Q04イ（法定相続情報一覧図つづり込み帳は作成の年の翌年から5年間。規則28条の2第6号）、R07-Q05ア（土地に関する閉鎖登記記録は閉鎖した日から50年間。永久ではない。規則28条）、R04-Q04ア（土地の閉鎖登記記録50年間は28条4号、建物の閉鎖登記記録30年間は28条5号）、R04-Q04オ（表示に関する登記の申請情報及び添付情報は28条9号、権利に関する登記は同条10号。いずれも受付の日から30年間）。
- extra_refs：①『閉鎖前の登記記録は永久』は不動産登記規則28条1号（法令DB note-articles/laws/fudousan-touki-kisoku-1.md の第二十八条第一号で確認。『登記記録（閉鎖登記記録を除く。）永久』）。3肢の記事に直接は書かれていないが、R07-Q05アの記事の『永久ではありません』の裏返しとして置く。②4号・5号・9号・10号と第28条の2第6号の文言も同ファイルで原文を確認した（4号『土地に関する閉鎖登記記録　閉鎖した日から五十年間』、5号『建物に関する閉鎖登記記録　閉鎖した日から三十年間』、9号『表示に関する登記の申請情報及びその添付情報…受付の日から三十年間』、10号『権利に関する登記の申請情報及びその添付情報…受付の日から三十年間』、28条の2第6号『法定相続情報一覧図つづり込み帳　作成の年の翌年から五年間』）。③9号・10号のかっこ書（申請書類つづり込み帳につづり込まれたものは電磁的記録に記録して保存した日から三十年間）は、図には入れない。いずれも『条文の号で6行を並べる整理』は記事にないので、ユーザーに『記事にない整理』と伝える。
- 記事・バンク・条文の確認：肢（D1728）の文は『作成の年の翌年から30年間』で、起算点は条文どおり。×の理由は起算点ではなく『30年間』という年数で、記事・条文（規則28条の2第6号）は5年間。食い違いはなく、図は条文どおり『5年間』と書く。ただし、第28条の2は帳簿ごとに年数が違い（第3号は同じ5年間、第4号は3年間、第2号・第5号は1年間）、第1号（登記簿保存簿など）は『作成の日から三十年間』で『翌年から』でもない。図に『帳簿は5年』のように一般化して書かず、法定相続情報一覧図つづり込み帳だけを書く。
- 同系統で今回は図に入れない肢：D1727（土地の閉鎖登記記録を30年とする。×）、D1729（閉鎖した各階平面図は閉鎖した日から30年間。〇。第13号）、D1730（筆界特定書以外の手続記録は送付を受けた年の翌年から30年間。〇。規則235条）、D1731（書面申請の申請書は受付の日から30年間。〇。9号）、D2024（閉鎖した建物所在図は永久。〇。3号）、D2025（建物の合併の登記の申請情報は永久でなく30年。×。9号）、D2026（筆界特定書は永久。〇）、D2027（閉鎖した地積測量図は30年。×。13号）。今回は、条文の号の構造が言えるように6行（1・4・5・9・10号と28条の2第6号）に絞った。
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない。書類・帳簿・登記簿はアイコンと文字ラベルで示す。肢のID（D####）は図に載せない（結論帯の問題番号だけ）。
- 矢印の意味：矢印は使わない。コマ1は3枚のカード、コマ2は表、コマ3は3枚のステップカード。
- 配色：コマ1〜3は印（✓✕）を付けない（年数は文字で書く）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方：コマ1＝side（通常サイズのキャラが左右の端、図は中央）、コマ2＝none（6行の当てはめ表が主役。キャラも吹き出しもなし）、コマ3＝faces（左に3枚のカード、右に会話の縦並び。会話4つ＝顔4つ＝4行）、コマ4＝既定（暗記3点と結論）。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D1596・D1728・D2023～R02-Q17イ／R04-Q04イ／R07-Q05ア～

## note記事の冒頭文

登記所が保存する情報には、種類ごとに保存期間が定められています。閉鎖した登記記録、登記の申請情報、法定相続情報一覧図つづり込み帳は、それぞれいつから何年間保存されるのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（令和2年度　第17問　イ／令和4年度　第4問　イ／令和7年度　第5問　ア）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 保存期間は、情報ごとに起算点と年数が違う | 「起算点と年数が違う」を黄色マーカー |
| コマ1 見出し | ラベル | ①　保存期間の肢が問う3点 | — |
| コマ1 図 | 図・カード | 保存期間の肢は、3点を問う / ①　何の情報か / 登記記録／申請情報／帳簿 / ②　いつから数えるか / 閉鎖した日／受付の日／作成の年の翌年 / ③　何年間か / 永久／50年間／30年間／5年間 | — |
| コマ1 | 藍子（左・先に話す） | 保存期間は、どれも30年ですよね？ | — |
| コマ1 | トリ先生（右・答える） | そこが罠。情報ごとに違うのよ | 「情報ごとに違う」 |
| コマ2 見出し | ラベル | ②　規則の号ごとに、起算点と年数 | — |
| コマ2 図 | 図・カード | 規則の号 / 保存される情報 / 数え始め / 保存期間 / 28条1号 / 閉鎖前の登記記録 / なし / 永久 / 28条4号 / 土地の閉鎖登記記録 / 閉鎖した日から / 50年間 / 28条5号 / 建物の閉鎖登記記録 / 30年間 / 28条9号 / 表示に関する登記の申請情報・添付情報 / 受付の日から / 28条10号 / 権利に関する登記の申請情報・添付情報 / 28条の2第6号 / 法定相続情報一覧図つづり込み帳 / 作成の年の翌年から / 5年間 | — |
| コマ3 見出し | ラベル | ③　本番での読み方3ステップ | — |
| コマ3 図 | 図・カード | ステップ1　何の情報かを見る / 登記記録か、申請情報か、帳簿か / ステップ2　登記記録は閉鎖の前後 / 閉鎖前は永久。閉鎖後は土地50年、建物30年 / ステップ3　起算点と年数を当てはめる / ひっかけ：全部30年に見える / 30年は申請情報（滅失の登記も）。つづり込み帳は5年 | — |
| コマ3 | 藍子（左・1番目） | 閉鎖した記録は永久ですよね？ | — |
| コマ3 | トリ先生（右・2番目） | それが罠。永久は閉鎖前よ | 「永久は閉鎖前」 |
| コマ3 | 藍子（左・3番目） | 滅失の登記の書類は何年ですか？ | — |
| コマ3 | トリ先生（右・4番目） | 表示の登記だから受付から30年 | 「受付から30年」 |
| コマ4 見出し | ラベル | ④　3つの肢の答え | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | つづり込み帳は、5年なんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。号ごとに当てはめるのよ | 「号ごとに当てはめる」 |
| コマ4 チェック欄 | 3項目（青✓） | 閉鎖前の登記記録は永久。閉鎖後は土地50年、建物30年（閉鎖後の土地を永久とするのは×） / 申請情報・添付情報は受付の日から30年。建物の滅失の登記も同じ（これは〇） / 法定相続情報一覧図つづり込み帳は作成の年の翌年から5年（30年とするのは×） | — |
| 結論帯 | 1行目 | 保存期間は、情報ごとに起算点と年数が違う | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1596・D1728・D2023　正解〇・×・×（R02-Q17イ／R04-Q04イ／R07-Q05ア） | — |

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

TITLE BANNER: text 「保存期間は、情報ごとに起算点と年数が違う」 in large bold letters; the part 「起算点と年数が違う」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　保存期間の肢が問う3点」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- One slim card at the top, same pale gray fill and dark navy outline, one line 「保存期間の肢は、3点を問う」.
- Below it, ONE vertical column of three cards, all exactly the same size, each with the same pale gray fill and a dark navy outline, each with a dark navy number badge and a dark navy heading placed fully INSIDE the card, each text at least 24 px high, with no check mark, no cross, and no arrow. The cards are separated only by a small empty gap.
- Card 1: heading 「①　何の情報か」, body 「登記記録／申請情報／帳簿」.
- Card 2: heading 「②　いつから数えるか」, body 「閉鎖した日／受付の日／作成の年の翌年」.
- Card 3: heading 「③　何年間か」, body 「永久／50年間／30年間／5年間」.
- The three cards have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- 藍子 bubble (left, spoken first): 「保存期間は、
どれも30年ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そこが罠。
情報ごとに違うのよ」 with the part 「情報ごとに違う」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (calm, focused mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　規則の号ごとに、起算点と年数」
- A wide table that fills the full panel width. The header row is dark navy with white text and has four columns: 「規則の号」, 「保存される情報」, 「数え始め」, 「保存期間」. The six body rows have the same pale gray fill and a dark navy outline, each text at least 24 px high, with no check mark, no cross, and no arrow.
- Body row 1: 「28条1号」, 「閉鎖前の登記記録」, 「なし」, 「永久」.
- Body row 2: 「28条4号」, 「土地の閉鎖登記記録」, 「閉鎖した日から」, 「50年間」.
- Body row 3: 「28条5号」, 「建物の閉鎖登記記録」, 「閉鎖した日から」, 「30年間」.
- Body row 4: 「28条9号」, 「表示に関する登記の申請情報・添付情報」, 「受付の日から」, 「30年間」.
- Body row 5: 「28条10号」, 「権利に関する登記の申請情報・添付情報」, 「受付の日から」, 「30年間」.
- Body row 6: 「28条の2第6号」, 「法定相続情報一覧図つづり込み帳」, 「作成の年の翌年から」, 「5年間」.
- The rows have clearly different texts; the texts are NOT identical, so copy each character exactly as given.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　本番での読み方3ステップ」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three step cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a dark navy number badge, and a dark navy heading, with no check mark and no cross. The step cards are separated only by a small empty gap, with nothing drawn between them.
- Step card 1: heading 「ステップ1　何の情報かを見る」, body 「登記記録か、申請情報か、帳簿か」.
- Step card 2: heading 「ステップ2　登記記録は閉鎖の前後」, body 「閉鎖前は永久。閉鎖後は土地50年、建物30年」.
- Step card 3: heading 「ステップ3　起算点と年数を当てはめる」, a dark navy ribbon tag with large white text 「ひっかけ：全部30年に見える」, body 「30年は申請情報（滅失の登記も）。つづり込み帳は5年」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「閉鎖した記録は
永久ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「それが罠。
永久は閉鎖前よ」 with the part 「永久は閉鎖前」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「滅失の登記の書類は
何年ですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「表示の登記だから
受付から30年」 with the part 「受付から30年」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　3つの肢の答え」
- 藍子 bubble (left, spoken first): 「つづり込み帳は、
5年なんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。号ごとに
当てはめるのよ」 with the part 「号ごとに当てはめる」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「閉鎖前の登記記録は永久。閉鎖後は土地50年、建物30年（閉鎖後の土地を永久とするのは×）」, 「申請情報・添付情報は受付の日から30年。建物の滅失の登記も同じ（これは〇）」, 「法定相続情報一覧図つづり込み帳は作成の年の翌年から5年（30年とするのは×）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「保存期間は、情報ごとに起算点と年数が違う」 with a yellow highlighter marker.
- Line 2: 「問題D1596・D1728・D2023　正解〇・×・×（R02-Q17イ／R04-Q04イ／R07-Q05ア）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two very small characters are drawn as specified and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 保, 号, 地, 建, 当, 権, 物, 番, 登, 肢, 規, 解, 記, 請, 違, 録, 間 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that no triangle, chevron, arrow, or connector is drawn between the stacked step cards; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 登記の保存期間 | 薄い黄色のマーカー |
| タイトル2行目 | 全部30年？ | 「全部30年？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D1596・D1728・D2023　R02-Q17イ／R04-Q04イ／R07-Q05ア | — |

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
登記の保存期間
Line 2 is larger; the phrase 全部30年？ is red-orange and the rest is dark navy:
全部30年？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D1596・D1728・D2023　R02-Q17イ／R04-Q04イ／R07-Q05ア
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: stacked archive shelves with blank binders and a small calendar
Right side: a blank document sheet beside a small registry book and a rubber stamp

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 登, 記, 保, 存, 期, 間, 全, 部, 年, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D1596・D1728・D2023～R02-Q17イ／R04-Q04イ／R07-Q05ア～.png |
| 見出し画像（採用版） | 4コマ解説図解D1596・D1728・D2023～R02-Q17イ／R04-Q04イ／R07-Q05ア～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D1596・D1728・D2023～R02-Q17イ／R04-Q04イ／R07-Q05ア～_v01.png ／ 4コマ解説図解D1596・D1728・D2023～R02-Q17イ／R04-Q04イ／R07-Q05ア～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D1596-D1728-D2023_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で『何の情報か・いつから数えるか・何年間か』の3点を読む問いだと分かり、コマ2の表で6つの号の組み合わせが言える
- [ ] 工程C：肝の確認：①閉鎖前の登記記録は永久、土地の閉鎖登記記録は閉鎖した日から50年間、建物は30年間 ②表示に関する登記も権利に関する登記も、申請情報・添付情報は受付の日から30年間（建物の滅失の登記も含む） ③法定相続情報一覧図つづり込み帳は作成の年の翌年から5年間 ④『土地の閉鎖登記記録は永久』は×、『つづり込み帳は翌年から30年間』は×、『滅失の登記の申請情報は受付の日から30年間』は〇
- [ ] 工程C：構成表の全文言を、記事と法令DB（規則28条1・4・5・9・10号、28条の2第6号）に突き合わせ：『受付の日から30年間』『閉鎖した日から50年間』『閉鎖した日から30年間』『作成の年の翌年から5年間』『永久』『建物の滅失の登記も含む』。号の番号は原文で確認できた6つだけを図に入れた
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方が隣り合うコマで同じにならない（side→none→faces→既定）。コマ4のチェックに、3つの肢の〇×を別に示す

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

- 2026-10-10 v01：新規作成（条文版。先に作った肢中心の版と別に、不動産登記規則第28条・第28条の2の号ごとの起算点と年数を1枚で言える構成にした。型は型2＋型4の対比）
