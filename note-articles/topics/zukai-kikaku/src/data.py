"""図解企画6本（土地の一生・用語の対比・添付情報・条文の読み方・解く順番・登記ストーリー）の元データ。
手で生成物を直さず、このデータを直して gen_prompts.py で作り直す。
fig の body 中の 「」 で囲んだ文字列が、そのまま画像に入れてよい文字（Words allowed）になる。
"""

TAGS = '#土地家屋調査士 #調査士試験 #不動産登記法 #資格勉強'

TOPICS = []


def topic(**kw):
    TOPICS.append(kw)


# ---------------------------------------------------------------- 01
topic(
    id='KZ_01', slug='01-tochi-tatemono-isshou',
    title='土地の一生・建物の一生〜登記が時間順に何を起こすかを、一本の線で眺める〜',
    media='note＋Instagram', motif='a winding path with small signposts and milestones, drawn simply',
    figs=[
        dict(key='zu01', title='土地の一生', size='1080x1800', body='''--- HEADER ---
Title (large, bold): 「土地の一生を一本の線で」 / subtitle band: 「登記が起こす出来事を時間順に」

--- BODY (one winding vertical path from top to bottom with four milestone cards on the path, and one side card branching off to the right after the first card) ---
 - Milestone card 1 (blue): heading 「表題登記」, line 「第36条　取得の日から一月以内」
 - Side card, pale orange, branching from card 1: heading 「所有権の保存」, line 「第74条　表題部所有者などが申請」
 - Milestone card 2 (blue): heading 「地目・地積の変更」, line 「第37条　変更の日から一月以内」
 - Milestone card 3 (blue): heading 「分筆・合筆」, line 「第39条　申請の期限の定めなし」, small tag 「合筆には制限がある　第41条」
 - Milestone card 4 (blue): heading 「滅失」, line 「第42条　滅失の日から一月以内」

--- FOOTER --- conclusion band: 「一月以内の登記と、期限の定めのない登記」'''),
        dict(key='zu02', title='建物の一生', size='1080x1900', body='''--- HEADER ---
Title (large, bold): 「建物の一生を一本の線で」 / subtitle band: 「順番は一例」

--- BODY (one winding vertical path from top to bottom with five milestone cards on the path, and one side card branching off to the right after the first card) ---
 - Milestone card 1 (blue): small text 「新築」, heading 「建物の表題登記」, line 「第47条　取得の日から一月以内」
 - Side card, pale orange, branching from card 1: heading 「所有権の保存」, line 「第74条　表題部所有者などが申請」
 - Milestone card 2 (blue): small text 「増築・用途や構造の変更」, heading 「表題部の変更」, line 「第51条　変更の日から一月以内」
 - Milestone card 3 (blue): heading 「分割・区分・合併」, line 「第54条　申請の期限の定めなし」, small tag 「合併には制限がある　第56条」
 - Milestone card 4 (blue): heading 「合体」, line 「第49条　合体の日から一月以内」
 - Milestone card 5 (blue): heading 「滅失」, line 「第57条　滅失の日から一月以内」

--- FOOTER --- conclusion band: 「一月以内の登記と、期限の定めのない登記」'''),
    ],
    header=dict(l1='土地と建物の', l2='一生を一本の線で', emph='一本の線', band='登記が時間順に起こすこと', sub='一月以内か、期限の定めなしか',
                scene_note='Left side: a small plot of land with a boundary line and a tiny signpost. Right side: a small house under construction with a scaffold and a calendar page with no numbers.',
                scene_ig='a small plot of land with a boundary line, a small house model, and a winding path with blank signposts'),
    captions=[
        ('A　カルーセル（表紙＋図2枚）', '''【土地の一生・建物の一生】登記は、いつ何を起こす？

土地や建物は、生まれてから無くなるまでに、いくつもの登記を経ます。それを一本の線に並べると、「期限のある登記」と「期限のない登記」がはっきり分かれます。

・土地：表題登記・地目や地積の変更・滅失は、一月以内（第36条・第37条・第42条）
・建物：表題登記・表題部の変更・合体・滅失も、一月以内（第47条・第51条・第49条・第57条）
・分筆・合筆や、建物の分割・区分・合併には、申請期限の定めがない
・所有権の保存は、表題部所有者などだけが申請できる（第74条）

一本の線で見ると、条文の位置関係が頭に入ります。保存して、見返してください。くわしくはプロフィールのリンクのnoteでどうぞ。

''' + TAGS),
        ('B　1枚目だけ（表紙）', '''土地にも建物にも「一生」がある。

生まれたとき（表題登記）から、無くなるとき（滅失）まで。登記が起こす出来事を、時間の順に一本の線で並べました。

次の投稿から、土地の一生・建物の一生を1枚ずつ見ていきます。

条文の位置は、プロフィールのリンクのnoteで確かめられます。

''' + TAGS),
    ],
)

# ---------------------------------------------------------------- 02
topic(
    id='KZ_02', slug='02-taihi-zukan',
    title='似た用語の対比図鑑〜分筆と分割、区分と分割、合体と合併、変更と更正をペアで比べる〜',
    media='Instagram（noteにも掲載）', motif='a pair of picture-book pages facing each other, drawn simply',
    figs=[
        dict(key='zu01', title='分筆・合筆と分割・合併', size='1080x1700', body='''--- HEADER ---
Title (large, bold): 「土地は筆、建物は個で数える」 / subtitle band: 「分筆・合筆と分割・合併」

--- BODY (a two-column comparison; left column header 「土地」 with a land plot icon, right column header 「建物」 with a house icon; two rows, each row has a row label on the left edge) ---
 - Row label 「分ける」:
   left cell: 「分筆」, line 「一筆の土地を二筆以上に分ける」, tag 「第39条」
   right cell: 「分割」, line 「附属建物を別の一個の建物にする」, tag 「第54条」
 - Row label 「つなぐ」:
   left cell: 「合筆」, line 「二筆以上の土地を一筆にする」, tag 「第39条・第41条」
   right cell: 「合併」, line 「他の建物の附属建物にする、または一個にする」, tag 「第54条・第56条」

--- FOOTER --- conclusion band: 「土地は一筆、建物は一個で登記記録をつくる」'''),
        dict(key='zu02', title='区分と分割、合体と合併', size='1080x1700', body='''--- HEADER ---
Title (large, bold): 「区分と分割、合体と合併」 / subtitle band: 「似ているが別の手続」

--- BODY (two comparison blocks stacked; each block has two cards side by side separated by a thin vertical divider line; all cards blue) ---
 - Block 1, cards:
   left card: heading 「建物の分割」, line 「附属建物を、別の一個の建物にする」
   right card: heading 「建物の区分」, line 「建物の部分を、区分建物にする」
   below the block, a small tag: 「どちらも第54条」
 - Block 2, cards:
   left card: heading 「合体」, line 「二以上の建物が一個の建物になった事実」, tag 「第49条　合体の日から一月以内」
   right card: heading 「合併」, line 「登記の手続で、附属建物にする、または一個にする」, tag 「第54条　申請の期限の定めなし」

--- FOOTER --- conclusion band: 「合体は事実、合併は手続」'''),
        dict(key='zu03', title='変更と更正、表題登記と所有権の保存', size='1080x1700', body='''--- HEADER ---
Title (large, bold): 「変更と更正、表題と保存」 / subtitle band: 「いつの誤りか、どの部分の最初か」

--- BODY (two comparison blocks stacked) ---
 - Block 1 (blue cards):
   left card: heading 「変更」, line 「登記したあとに、現実が変わった」, tag 「第37条・第51条　一月以内」
   right card: heading 「更正」, line 「登記したときから、内容が誤っていた」, tag 「第38条・第53条　期限の定めなし」
 - Block 2:
   left card (blue): heading 「表題登記」, line 「表題部に最初にされる登記」, tag 「第2条第20号」
   right card (pale orange): heading 「所有権の保存」, line 「権利部に最初にされる所有権の登記」, tag 「第74条」

--- FOOTER --- conclusion band: 「表題部は表示、権利部は権利」'''),
    ],
    header=dict(l1='似ている用語の', l2='対比図鑑', emph='対比', band='分筆と分割、合体と合併ほか', sub='混同しやすい組を二列で比べる',
                scene_note='Left side: an open picture book with two facing blank pages. Right side: two small blocks, one a plot of land and one a house, standing side by side.',
                scene_ig='an open picture book with two facing blank pages, and a small plot of land and a small house standing side by side'),
    captions=[
        ('A　カルーセル（表紙＋図3枚）', '''【似た用語の対比図鑑】分筆と分割、合体と合併、言い分けられますか？

不動産登記法には、名前は似ていても別の手続がたくさんあります。ペアにして比べると、違いが一目で分かります。

・分筆・合筆は土地、分割・合併は建物（第39条・第54条）
・分割は附属建物を別の建物に、区分は建物の部分を区分建物に（第54条）
・合体は事実、合併は登記の手続（第49条・第54条）
・変更は登記後に現実が変わった、更正は登記時から誤っていた
・表題登記は表題部の最初、所有権の保存は権利部の最初

3枚にまとめました。保存して見返してください。条文の位置は、プロフィールのリンクのnoteでどうぞ。

''' + TAGS),
        ('B-1　分筆・合筆と分割・合併（単発）', '''土地は「筆」、建物は「個」で数える。

土地を分けるのは「分筆」、つなぐのは「合筆」。建物を分けるのは「分割」、つなぐのは「合併」。同じ「分ける・つなぐ」でも、呼び名が土地と建物で違います（第39条・第54条）。

試験では、土地の問題に「分割」が出てきたり、建物の問題に「分筆」が出てきたりして、言葉のひっかけになります。まず対象が土地か建物かを見る習慣をつけましょう。

くわしくはプロフィールのリンクのnoteでどうぞ。

''' + TAGS),
        ('B-2　区分と分割、合体と合併（単発）', '''「区分」と「分割」、「合体」と「合併」。

・分割：附属建物を、別の一個の建物にする
・区分：建物の部分を、区分建物にする
・合体：二以上の建物が一個の建物になった事実。合体の日から一月以内（第49条）
・合併：登記の手続で、附属建物にする、または一個にする。申請の期限の定めなし（第54条）

合体は事実、合併は手続。この一言で、期限の有無の違いも思い出せます。

くわしくはプロフィールのリンクのnoteでどうぞ。

''' + TAGS),
        ('B-3　変更と更正、表題登記と所有権の保存（単発）', '''「変更」と「更正」の違いは、誤りがいつからあったか。

・変更：登記したあとに、現実が変わった（一月以内。第37条・第51条）
・更正：登記したときから、内容が誤っていた（期限の定めなし。第38条・第53条）

そして「表題登記」は表題部に最初にされる登記（第2条第20号）、「所有権の保存」は権利部に最初にされる所有権の登記（第74条）。表題部は表示、権利部は権利、と覚えると整理できます。

くわしくはプロフィールのリンクのnoteでどうぞ。

''' + TAGS),
    ],
)

# ---------------------------------------------------------------- 03
topic(
    id='KZ_03', slug='03-tenpu-jouhou-hayami',
    title='表示に関する登記の添付情報 早見図〜この登記には何を付けるか、令別表の項で一枚にする〜',
    media='note（Instagramにも掲載）', motif='a clipboard and paper clips, drawn simply',
    figs=[
        dict(key='zu01', title='土地の登記と添付情報', size='1080x1700', body='''--- HEADER ---
Title (large, bold): 「土地の登記に付ける情報」 / subtitle band: 「令別表で決まる」

--- BODY (a table with a blue header row and a first column of registration names; four attachment columns; each cell holds one mark) ---
 - Column headers: 「土地所在図」 「地積測量図」 「所有権証明情報」 「住所証明情報」
 - Row 「土地の表題登記」 with small tag 「令別表四の項」: 「○」 「○」 「○」 「○」
 - Row 「地目の変更・更正」 with small tag 「五の項」: 「－」 「－」 「－」 「－」
 - Row 「地積の変更・更正」 with small tag 「六の項」: 「－」 「○」 「－」 「－」
 - Row 「分筆」 with small tag 「八の項」: 「－」 「○」 「－」 「－」
 - Row 「合筆」 with small tag 「九の項」: 「－」 「－」 「－」 「－」
 - Legend under the table: 「○　別表に定めがある」 「－　通常は別表に定めがない」

--- FOOTER --- conclusion band: 「代理人が申請するなら代理権限証明情報も」'''),
        dict(key='zu02', title='建物の登記と添付情報', size='1080x1800', body='''--- HEADER ---
Title (large, bold): 「建物の登記に付ける情報」 / subtitle band: 「令別表で決まる」

--- BODY (a table with a blue header row and a first column of registration names; four attachment columns; each cell holds one mark) ---
 - Column headers: 「建物図面」 「各階平面図」 「所有権証明情報」 「住所証明情報」
 - Row 「建物の表題登記」 with small tag 「令別表十二の項」: 「○」 「○」 「○」 「○」
 - Row 「合体による登記等」 with small tag 「十三の項」: 「○」 「○」 「○」 「○」
 - Row 「表題部の変更・更正」 with small tag 「十四の項」: 「△」 「△」 「△」 「－」
 - Row 「分割・区分・合併」 with small tag 「十六の項」: 「○」 「○」 「－」 「－」
 - Row 「滅失」 with small tag 「別表に項なし」: 「－」 「－」 「－」 「－」
 - Legend under the table: 「○　別表に定めがある」 「△　変更の内容による」 「－　通常は別表に定めがない」

--- FOOTER --- conclusion band: 「代理人が申請するなら代理権限証明情報も」'''),
    ],
    header=dict(l1='表示の登記の', l2='添付情報早見図', emph='早見図', band='何の登記に何を付けるか', sub='令別表の項で決まる',
                scene_note='Left side: a clipboard with blank sheets and a few paper clips. Right side: a small stack of blank documents and a rubber stamp with no text.',
                scene_ig='a clipboard with blank sheets, paper clips, and a small stack of blank documents'),
    captions=[
        ('A　カルーセル（表紙＋図2枚）', '''【表示の登記の添付情報 早見図】この登記には、何を付ける？

土地や建物の表示に関する登記は、不動産登記令の別表で「何を付けるか」が項ごとに決まっています。一枚の表にすると、図面が要る登記と要らない登記が分かります。

・土地の表題登記：土地所在図・地積測量図・所有権証明情報・住所証明情報（別表四の項）
・地目の変更・更正：別表に個別の定めがない（五の項）
・分筆：分筆後の土地の地積測量図（八の項）
・建物の表題登記：建物図面・各階平面図・所有権証明情報・住所証明情報（十二の項）
・滅失：別表に項がない

2枚にまとめました。保存して見返してください。くわしくはプロフィールのリンクのnoteでどうぞ。

''' + TAGS),
        ('B-1　土地の登記（単発）', '''土地の登記に付ける情報、早見図です。

・表題登記（別表四の項）：土地所在図・地積測量図・所有権証明情報・住所証明情報
・地積の変更・更正（六の項）：地積測量図
・分筆（八の項）：分筆後の土地の地積測量図
・地目の変更・更正（五の項）と合筆（九の項）：別表に個別の定めがない

「別表に定めがない」は「何も要らない」という意味ではありません。代理人が申請するなら代理権限証明情報など、令第7条の一般の添付情報は別に要ります。

くわしくはプロフィールのリンクのnoteでどうぞ。

''' + TAGS),
        ('B-2　建物の登記（単発）', '''建物の登記に付ける情報、早見図です。

・表題登記（別表十二の項）と合体による登記等（十三の項）：建物図面・各階平面図・所有権証明情報・住所証明情報
・分割・区分・合併（十六の項）：建物図面と各階平面図
・表題部の変更・更正（十四の項）：床面積を変えるときは変更後の建物図面と各階平面図、など変更の内容による
・滅失：別表に項がない

表の見方に慣れると、図面が要る登記かどうかが一目で分かります。

くわしくはプロフィールのリンクのnoteでどうぞ。

''' + TAGS),
    ],
)

# ---------------------------------------------------------------- 04
topic(
    id='KZ_04', slug='04-joubun-no-yomikata',
    title='条文の読み方 図解〜「ただし書」「除き」「前項」「準用」「みなす」を、実際の条文で読み解く〜',
    media='note＋Instagram', motif='an open statute book with a magnifying glass, drawn simply',
    figs=[
        dict(key='zu01', title='本文とただし書', size='1080x1700', body='''--- HEADER ---
Title (large, bold): 「ただし書は、例外の合図」 / subtitle band: 「第25条を例に」

--- BODY (a statute-reading diagram; a large pale card in the middle split into two parts, upper part = main text, lower part = proviso, joined by a small down arrow) ---
 - Small tag above the card: 「第25条　申請の却下」
 - Upper part, tab 「本文」 (blue): 「登記官は、次の場合には却下しなければならない」
 - Lower part, tab 「ただし書」 (pale orange): 「補正できる不備を、期間内に補正したときは、この限りでない」
 - Left margin label on the upper part: 「原則」 ; left margin label on the lower part: 「例外」
 - Under the card, three small reading steps in a row: 「まず本文」 「次にただし書」 「例外に当たるか確かめる」

--- FOOTER --- conclusion band: 「この限りでない＝そこは適用しない」'''),
        dict(key='zu02', title='除きと次に掲げる', size='1080x1700', body='''--- HEADER ---
Title (large, bold): 「除きと次に掲げる」 / subtitle band: 「第16条と第41条を例に」

--- BODY (two statute cards stacked) ---
 - Card 1 (blue), tag 「第16条第1項」: sentence 「法令に別段の定めがある場合を除き、申請または嘱託がなければ、登記はできない」; below it two small boxes: 「原則　申請または嘱託が必要」 and 「除く　別段の定めがあるとき」
 - Card 2 (blue), tag 「第41条」: sentence 「次に掲げる合筆の登記は、することができない」; below it a short list of labeled boxes: 「一号　相互に接続していない土地」 「二号　地目または地番区域が異なる土地」 「三号　所有者が異なる土地」 and a small box 「ほか三つの号」
 - A small reading hint under card 2: 「号のどれかに当たれば、できない」

--- FOOTER --- conclusion band: 「除きは例外を外す、次に掲げるは号を読む」'''),
        dict(key='zu03', title='前項・準用・みなす', size='1080x1800', body='''--- HEADER ---
Title (large, bold): 「前項・準用・みなす」 / subtitle band: 「指す先を確かめる」

--- BODY (three statute cards stacked, each with an arrow icon pointing to the thing it refers to) ---
 - Card 1 (blue), tag 「第51条第2項」: phrase 「前項の登記事項について変更があった後に…」; small arrow label 「前項＝すぐ前の第1項」
 - Card 2 (blue), tag 「第54条第3項」: phrase 「第40条の規定は、権利の登記がある建物の分割・区分の登記をするときに準用する」; small arrow label 「準用＝同じ規定を当てはめる」; small caption 「第40条は分筆に伴う権利の消滅の登記」
 - Card 3 (pale orange), tag 「第19条第2項」: phrase 「その前後が明らかでないときは、同時にされたものとみなす」; small arrow label 「みなす＝事実と違っても、そう扱う」

--- FOOTER --- conclusion band: 「指す先の条文を、必ず開いて読む」'''),
    ],
    header=dict(l1='条文の読み方', l2='図解で読み解く', emph='読み解く', band='ただし書・準用・前項・みなす', sub='実際の条文を例にして',
                scene_note='Left side: a large open statute book and a magnifying glass. Right side: a small stack of books and a pen.',
                scene_ig='a large open statute book with a magnifying glass, and a small stack of books'),
    captions=[
        ('A　カルーセル（表紙＋図3枚）', '''【条文の読み方】「ただし書」「除き」「前項」「準用」「みなす」、読めていますか？

法律の条文には、読み方の「合図」になる言葉があります。実際の条文を例に、3枚で整理しました。

・ただし書は例外の合図。本文を読んでから、ただし書を確かめる（第25条）
・「除き」は例外を外す。「次に掲げる」は号を読む（第16条・第41条）
・「前項」はすぐ前の項、「準用」は同じ規定を当てはめる（第51条・第54条）
・「みなす」は事実と違っても、そう扱う（第19条）

指す先の条文を開いて読む習慣が、得点につながります。くわしくはプロフィールのリンクのnoteでどうぞ。

''' + TAGS),
        ('B-1　ただし書（単発）', '''「ただし書」は、例外の合図です。

第25条は、登記官は申請を却下しなければならない、と書いたあとに、ただし書でこう続けます。補正できる不備を、登記官が定めた期間内に補正したときは、この限りでない。

本文は原則、ただし書は例外。順に読めば、「補正すれば却下されない」と分かります。

くわしくはプロフィールのリンクのnoteでどうぞ。

''' + TAGS),
        ('B-2　準用・みなす（単発）', '''「準用」と「みなす」の読み方です。

・準用：第54条第3項は、第40条（分筆に伴う権利の消滅の登記）を、建物の分割・区分の登記に準用しています。指す先の条文を開いて、同じ規定を当てはめます。
・みなす：第19条第2項は、申請の前後が明らかでないとき、同時にされたものとみなします。事実と違っても、そう扱います。

読み解く鍵は、指す先を確かめることです。

くわしくはプロフィールのリンクのnoteでどうぞ。

''' + TAGS),
    ],
)

# ---------------------------------------------------------------- 05
topic(
    id='KZ_05', slug='05-kijutsu-tokujunban',
    title='記述式の「解く順番」図〜土地（第21問）と建物（第22問）、どこから手を付けるか〜',
    media='note（Instagramにも掲載）', motif='a stopwatch and an answer sheet with a pencil, drawn simply',
    figs=[
        dict(key='zu01', title='土地（第21問）の解く順番', size='1080x1800', body='''--- HEADER ---
Title (large, bold): 「土地の記述式　解く順番」 / subtitle band: 「座標の前にできることから」

--- BODY (a vertical staircase of seven steps from top to bottom, each step a rounded card; the first three steps are light blue, the middle two are pale yellow, the last two are pale orange) ---
 - Step 1: heading 「問と注を先に読む」, line 「注は系統ごとに仕分ける」
 - Step 2: heading 「時系列メモ」, line 「期限と所有者を書き出す」
 - Step 3: heading 「座標に左右されない欄」, line 「記述問題と申請書の一部を先に」
 - Step 4: heading 「点を順に出す」, line 「放射と交点の計算」
 - Step 5: heading 「面積と公差の判定」, line 「地積更正の要否」
 - Step 6: heading 「地積測量図」, line 「作図に使う時間を先に決める」
 - Step 7: heading 「見直し」, line 「検算と書き漏れ」

--- FOOTER --- conclusion band: 「手が止まったら、書ける欄へ戻る」'''),
        dict(key='zu02', title='建物（第22問）の解く順番', size='1080x1800', body='''--- HEADER ---
Title (large, bold): 「建物の記述式　解く順番」 / subtitle band: 「求積と作図に時間を残す」

--- BODY (a vertical staircase of seven steps from top to bottom, each step a rounded card; the first three steps are light blue, the middle two are pale yellow, the last two are pale orange) ---
 - Step 1: heading 「問とただし書きを先に読む」, line 「書き方の指示を見落とさない」
 - Step 2: heading 「事実関係と登記記録」, line 「時系列メモと申請の期限」
 - Step 3: heading 「登記記録を写す欄」, line 「写すだけの欄から埋める」
 - Step 4: heading 「求積」, line 「壁心か内法かを確かめる」
 - Step 5: heading 「作図」, line 「建物図面と各階平面図」
 - Step 6: heading 「問の穴埋め」, line 「最後に回すが、時間は残す」
 - Step 7: heading 「見直し」, line 「検算と書き漏れ」

--- FOOTER --- conclusion band: 「いちばん重いのは、求積と作図」'''),
    ],
    header=dict(l1='記述式の', l2='解く順番', emph='解く順番', band='土地と建物の型別に示す', sub='座標や求積の前にできること',
                scene_note='Left side: a stopwatch and an answer sheet with a pencil. Right side: a small stack of blank sheets and a calculator with no numbers on its screen.',
                scene_ig='a stopwatch, an answer sheet with a pencil, and a calculator with a blank screen'),
    captions=[
        ('A　カルーセル（表紙＋図2枚）', '''【記述式の「解く順番」】どこから手を付ける？

記述式は、手を付ける順番で結果が変わります。土地（第21問）と建物（第22問）で、型別に整理しました。

・土地：問と注 → 時系列メモ → 座標に左右されない欄 → 点を出す → 面積と公差 → 地積測量図 → 見直し
・建物：問とただし書き → 事実関係と登記記録 → 写す欄 → 求積 → 作図 → 問の穴埋め → 見直し

土地は座標の前にできることから、建物は求積と作図に時間を残す。手が止まったら、書ける欄へ戻りましょう。

保存して、過去問の演習前に見返してください。くわしくはプロフィールのリンクのnoteでどうぞ。

''' + TAGS),
        ('B-1　土地（第21問）（単発）', '''土地の記述式、解く順番です。

①問と注を読む　②時系列メモ　③座標に左右されない欄　④点を順に出す　⑤面積と公差　⑥地積測量図　⑦見直し

いきなり座標の計算に入らず、記述問題や申請書の一部など、座標に左右されない欄を先に書いておくと、手が止まったときの保険になります。

くわしくはプロフィールのリンクのnoteでどうぞ。

''' + TAGS),
        ('B-2　建物（第22問）（単発）', '''建物の記述式、解く順番です。

①問とただし書き　②事実関係と登記記録　③写す欄　④求積　⑤作図　⑥問の穴埋め　⑦見直し

いちばん重いのは、求積と作図です。穴埋めは短い知識問題なので最後に回しますが、その時間は必ず残しておきましょう。

くわしくはプロフィールのリンクのnoteでどうぞ。

''' + TAGS),
    ],
)

# ---------------------------------------------------------------- 06
topic(
    id='KZ_06', slug='06-ichinichi-no-touki-story',
    title='ある一日の登記ストーリー〜新築から建物の表題登記まで、トリ先生と藍子の四コマで追う〜',
    media='Instagram（リール・四コマ）＋note', motif='a small house, a map, and a government building drawn simply',
    figs=[],
    header=dict(l1='ある一日の', l2='登記ストーリー', emph='ストーリー', band='新築から表題登記まで', sub='トリ先生と藍子の四コマ',
                scene_note='Left side: a newly built small house with a blank signboard. Right side: a small government office building and a surveying tripod.',
                scene_ig='a newly built small house, a small government office building and a surveying tripod'),
    captions=[
        ('A　四コマ（フィードは3:4版、ストーリー・リールは9:16版）の投稿', '''【ある一日の登記ストーリー】新築した家は、いつ・誰が・どうやって登記される？

建物を新築したら、所有権を取得した日から一月以内に、建物の表題登記を申請します（第47条）。

①依頼人が調査士に相談
②調査士が現地を調査・測量し、建物図面と各階平面図をつくる
③法務局に申請（受付は第19条）
④登記官が必要に応じて調査し（第29条）、表題部に記録する（第11条）

四コマで、流れをつかんでください。保存して見返してください。くわしくはプロフィールのリンクのnoteでどうぞ。

''' + TAGS),
        ('B　リール（20秒）のキャプション', '''新築した家が登記されるまでを、20秒で。

相談 → 現地調査・測量 → 申請 → 登記官の調査と記録。
表題登記は、新築から一月以内（第47条）。

試験で問われるのは、この流れの「どこで何を根拠にするか」。四コマの画像版もあります。

くわしくはプロフィールのリンクのnoteでどうぞ。

''' + TAGS),
    ],
)
