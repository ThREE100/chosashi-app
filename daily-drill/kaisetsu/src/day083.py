def kj(*ss, n=14):
    out = []
    for s in ss:
        for c in s:
            if '一' <= c <= '龥' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='専有部分と敷地の権利は一体',
    intro='マンションなどの区分建物では、部屋（専有部分）と、建物が建っている土地を使う権利（敷地利用権）を別々に処分できるのでしょうか。\n\n敷地権とは何か、その割合の決め方、そして敷地権である旨の登記と抵当権の扱いを問う問題です（区分所有法22条・14条、不動産登記法46条、不動産登記規則119条・123条）。\n\nこの記事では、分離処分の禁止、単独所有の場合、敷地権の登記の記録事項、割合の基準、建物の表題部の変更で新たに敷地権の登記をするときの抵当権の扱いを確認していきましょう。この問題は「正しいもの」の組合せを選ぶ形式です。',
    sections={
        'ア': ('土地の持分を数人で持つなら、部屋と分けて処分できない',
               '敷地利用権が数人で有する所有権その他の権利である場合には、区分所有者は、その有する専有部分とその専有部分に係る敷地利用権とを分離して処分することができません。ただし、規約に別段の定めがあるときは別です（区分所有法22条1項）。\n\n甲土地の共有持分は、数人で有する所有権です。規約に別段の定めがなければ、Aは専有部分と共有持分を分離して処分できません。本肢は正しいといえます。\n\n**たとえば**、AとBが共有する土地にマンションを建てて、それぞれ部屋を持っているとします。Aが、自分の部屋だけを売って、土地の共有持分は自分に残す、ということはできません。'),
        'イ': ('土地を単独で所有している場合も、分離処分はできない',
               '分離処分の禁止は、敷地利用権が「数人で」有する権利の場合だけではありません。建物の専有部分の全部を所有する人の敷地利用権が、単独で有する所有権その他の権利である場合にも、準用されます（区分所有法22条3項）。\n\n問題文は、乙土地の所有権は数人で有する権利ではないから、規約に別段の定めがなくても、専有部分と分けて処分できるとしています。3項を見落としているので、本肢は誤りです。\n\n**たとえば**、C株式会社が、自社の土地に区分建物からなる建物を新築して、すべての専有部分を所有しているとします。規約に別段の定めがなければ、Cは専有部分と土地の所有権を別々に売ることはできません。'),
        'ウ': ('敷地権の登記は土地にも記録され、一部の建物なら家屋番号も載る',
               '登記官は、区分建物に関する敷地権について表題部に最初に登記をするときは、職権で、敷地権の目的である土地の登記記録に、敷地権である旨の登記をします（不動産登記法46条）。\n\nその敷地権が一棟の建物に属する一部の建物についての敷地権であるときは、その一部の建物の家屋番号も、土地の登記記録の権利部の相当区に記録します（不動産登記規則119条1項4号）。本肢は正しいといえます。\n\n**たとえば**、101号室だけの敷地権になっている土地なら、土地の登記記録に「101号室の家屋番号」が記録されます。'),
        'エ': ('敷地利用権の割合は、床面積の割合が基本で、価格ではない',
               '区分所有者が数個の専有部分を所有するときは、各専有部分に係る敷地利用権の割合は、専有部分の床面積の割合によるのが基本です（区分所有法22条2項、14条）。\n\n規約で異なる割合を定めているときは、その割合によります。\n\n問題文は、Dが各専有部分の価格に応じて定めた割合によるとしています。所有者が価格に応じて自由に決める仕組みではないので、本肢は誤りです。\n\n**たとえば**、101号室が60平方メートル、102号室が40平方メートルなら、規約で別の割合を決めていない限り、敷地利用権の割合は6対4を基本とします。部屋の値段の高い安いで割合が決まるわけではありません。'),
        'オ': ('目的等が同一の抵当権なら、土地側の登記が職権で抹消される',
               '建物の表題部の変更の登記で新たに敷地権の登記をした場合、建物に特定担保権（抵当権など）の登記があるときは、原則として、その登記に建物のみに関する旨を付記します。\n\nただし、登記の目的、申請の受付の年月日及び受付番号並びに登記原因及びその日付が、敷地権について土地にされた特定担保権の登記と同一であるときは、この付記はしません（不動産登記規則123条1項）。\n\n付記をしない場合は、登記官は職権で、土地の側の特定担保権の登記を抹消します（同条2項）。問題文は、同一の場合でも付記をしなければならないとしているので、本肢は誤りです。\n\n**たとえば**、建物と土地に、同じ日に同じ原因で受け付けた同じ抵当権の登記があるときは、建物に「建物のみに関する旨」を付記せず、土地側の抵当権の登記が抹消されます。'),
    },
    summary=[
        ('ア', '正', '敷地利用権が数人で有する権利なら、規約に別段の定めがない限り、専有部分と分離して処分できない'),
        ('イ', '誤', '専有部分の全部を所有する人の敷地利用権が単独所有でも、分離処分の禁止が準用される'),
        ('ウ', '正', '敷地権が一部の建物についてのものなら、土地の登記記録にその建物の家屋番号も記録する'),
        ('エ', '誤', '数個の専有部分の敷地利用権の割合は、床面積の割合が基本で、所有者が価格に応じて定めるものではない'),
        ('オ', '誤', '目的等が同一の抵当権の登記があるときは、付記をせず、土地側の登記を職権で抹消する'),
    ],
    summary_tail='イは「単独所有の例外の見落とし」、エは「基準のすり替え」、オは「付記が要らない場合」がひっかけでした。「専有部分と敷地の権利は一体」という原則から、登記の記録のしかたまで順に確認しましょう。',
    supplements=[
        '### 補足説明（イ）：分離処分の禁止が働く場面\n\n分離処分の禁止は、敷地利用権の持ち方によらず、広く働きます（区分所有法22条）。\n\n| 場面 | 分離処分 | 根拠 |\n|---|---|---|\n| 敷地利用権が数人で有する所有権その他の権利 | できない（規約に別段の定めがあれば別） | 1項 |\n| 専有部分の全部を所有する人の敷地利用権が単独で有する権利 | できない（1項・2項を準用） | 3項 |\n| 規約に別段の定めがある | その定めによる | 1項ただし書 |\n\n**たとえば**、1社が土地もマンション全体も持っている新築の段階でも、規約に別段の定めがなければ、部屋と土地は別々に売れません。「数人で持っていないから自由」という考えは、3項で否定されています。',
        '### 補足説明（オ）：新たに敷地権の登記をするときの抵当権の扱い\n\n建物の表題部の変更の登記で新たに敷地権の登記をしたとき、建物の特定担保権の登記の扱いは、土地の側の登記と同一かどうかで変わります（不動産登記規則123条）。\n\n| 建物と土地の抵当権の登記 | 登記官がすること |\n|---|---|\n| 登記の目的、受付の年月日及び受付番号、登記原因及びその日付が同一 | 付記はしない。職権で土地側の登記を抹消する（2項） |\n| 同一ではない | 建物の登記に、建物のみに関する旨を付記する（1項本文） |\n\n**たとえば**、同じ日に、同じ抵当権設定契約で、建物と土地の両方に抵当権が登記されていたなら、敷地権の登記後は建物の登記に一本化され、土地側が抹消されます。日付などが違うと、建物の登記に「建物のみに関する旨」が付記されます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第83日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、区分所有法14条・22条、不動産登記法46条、不動産登記規則119条・123条は、`note-articles/laws/` 配下の原文で確認しました。',
        'エの具体例（60平方メートルと40平方メートルで6対4）は、14条1項（床面積の割合）を数字で置き換えた説明です。実際には14条3項により壁の内側線で囲まれた部分の面積で測るため、数字は説明のための単純化です。',
        'オの一本化の説明（目的等が同一なら建物の登記に一本化される）は、規則123条1項ただし書・2項の結果を平易に言い換えたもので、条文の文言そのものではありません。',
    ],
    phrases=['部屋と土地の持分は別々に売れません', '一人で全部屋を持っていても同じです', '敷地権の登記は土地にも載ります', '土地の割合は床面積で決まります', '同じ抵当権なら土地側が消えます'],
    header=dict(t1='部屋と土地は、', t2='別々に売れる？', topic='区分所有法　敷地権',
                kanji='部・屋・土・地・区・分・所・有・法・毎'),
    poster_intro='敷地権を、「分離処分の禁止」（グループA：ア・イ）と「登記の記録と割合」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='敷地権を整理', sub='区分所有法 第22条と不動産登記法 第46条（毎日ドリル 第83日）',
        col_a='分離処分の禁止', col_b='登記の記録と割合', n_a=2,
        cards=[
            dict(h='部屋と土地の持分は一体',
                 ill='a condominium room unit connected by a chain to a pie-slice-shaped share of a land plot, so that the room and the share form one inseparable set.',
                 words=[], tag='分離して処分できない'),
            dict(h='単独所有でも一体',
                 ill='a single company figure holding the whole condominium building and the land beneath it, with a chain linking the building and the land.',
                 words=[], tag='全部を所有する人も'),
            dict(h='敷地権は土地の登記にも載る',
                 ill='a land record sheet with a stamp labeled 「敷地権」 and a small door icon with a house number plate beside the stamp.',
                 words=['敷地権'], tag='家屋番号も記録'),
            dict(h='土地の割合は床面積の割合',
                 ill='two rooms of different sizes on the left and a land pie chart on the right divided in the same proportions as the two floor areas.',
                 words=[], tag='規約で別も定められる'),
            dict(h='同じ抵当権なら土地側が消える',
                 ill='a building record sheet and a land record sheet, each with an identical mortgage line labeled 「抵当権」. The mortgage line on the land sheet is lightly faded, with an eraser beside it.',
                 words=['抵当権'], tag='職権で抹消'),
        ],
        kanji=kj('部屋土地持分一体単独所有敷地権登記割合床面積抵当権', n=24)),
    nb_label='イ・オ肢', nb_intro='イ・オの補足説明に合わせた2枚です。1枚目は、分離処分が禁止される場面を表で示します。2枚目は、新たに敷地権の登記をするときの抵当権の扱いを、左右で対比します。',
    notebooks=[
        dict(name='分離処分の禁止が働く場面', args=dict(
            title='部屋と土地は、いつ一体？', sub='区分所有法22条（毎日ドリル 第83日 イ）',
            req='a comparison table',
            layout="""--- TABLE ---
Render as a clean flat-design table with a header row and three body rows, in rounded panel style. Each body row carries a small icon at the left edge (several owners sharing a land plot, one company figure holding a building and land, a document labeled 規約).
Header row (blue accent), three column headers: 場面 | 分離処分 | 根拠
Row 1: 敷地利用権を数人で有する | できない | 第一項
Row 2: 専有部分の全部を所有する人が単独で有する | できない | 第三項
Row 3: 規約に別段の定めがある | その定めによる | 第一項ただし書
Use exactly these strings, and no others. Do not use check marks or cross marks.""",
            callout='敷地利用権を単独で有する場合でも、専有部分の全部を所有する人には、分離処分の禁止が準用されます。\n「数人で持っていないから自由」ではありません。',
            footer='区分所有法22条1項・3項',
            kanji=kj('場面分離処分敷地利用権数人専有部分所有規約', n=16), what='table',
            check='confirm the table has exactly three body rows and that no check mark or cross mark appears, ')),
        dict(name='新たに敷地権の登記をするときの抵当権', args=dict(
            title='抵当権の登記は、どうなる？', sub='不動産登記規則123条（毎日ドリル 第83日 オ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「目的等が同一」 on the left and 「同一でない」 on the right. Draw them large and in different accent colors (blue on the left, green on the right) so they can never be confused or duplicated. Do not use check marks or cross marks.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 目的等が同一
Scene: an isometric building record sheet and a land record sheet side by side, each with an identical mortgage line, with the land sheet's line fading away.
Rows of text:
建物の登記: 付記はしない
土地の登記: 職権で抹消する

RIGHT PANEL (green accent):
Panel header: 同一でない
Scene: an isometric building record sheet with a small tag attached to its mortgage line, beside a land record sheet whose mortgage line stays.
Rows of text:
建物の登記: 建物のみに関する旨を付記する
土地の登記: そのまま""",
            callout='建物と土地の抵当権の登記の目的等が同一のときは、付記をせず、土地の側の登記を職権で抹消します。\n同一でないときは、建物の登記に建物のみに関する旨を付記します。',
            footer='不動産登記規則123条1項・2項',
            kanji=kj('目的同一建物土地登記付記職権抹消抵当', n=16), what='panels',
            check='confirm the two panel headers are different strings (目的等が同一 on the left and 同一でない on the right) drawn in different accent colors, ')),
    ],
)
