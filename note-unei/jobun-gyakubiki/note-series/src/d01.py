"""第1回：分筆・合筆は「誰が」申請できるか（不動産登記法 第39条・第40条）"""
NO = 1
SLUG = 'bunpitsu-shinseinin'
TITLE = '分筆・合筆は「誰が」申請できるか'
LAWS = '不動産登記法 第39条・第40条'
L = '不動産登記法'

LEAD = [
    '図鑑で出た年度がいちばん多かった条文は、不動産登記法第39条（分筆又は合筆の登記）でした。平成17年度から令和8年度までの22年度分のうち、16年度で出ています。',
    '第39条が問うのは、ほぼ「**誰が申請できるか**」の一点です。買主、相続人、共有者の一人、抵当権者……と、立場を変えた人を次々に登場させて、「この人は分筆を申請できるか」を聞いてきます。あわせて、分筆と同時に抵当権などを消せる第40条も、同じ問題の中でよく出ます。',
    'この回では、第39条と第40条を、本試験で見るところに絞って読みます。',
]

POSTER = dict(
    title='分筆・合筆は誰が申請できるか',
    topics='申請人・共有・職権・分筆と権利の消滅',
    cards=[
        ('申請できる人', '所有者だけ', 'a plot of land divided by a dashed line, with a person holding a house-shaped name card standing on it; a buyer and a bank officer stand outside a fence'),
        ('共有の土地', '持分の過半数で', 'a pie chart split into three equal slices, two slices highlighted blue next to two people raising hands'),
        ('職権の分筆', 'しなければならない', 'a land plot where one part has turned into a parking lot, and a registrar with a stamp dividing it'),
        ('地図作成の職権', '異議がなければできる', 'a registrar drawing a map at a desk, with a small speech bubble showing no objection from the owner'),
        ('分筆と権利の消滅', '一方の土地だけ', 'a mortgaged land plot split into two; a chain-lock icon is removed from only one of the two plots'),
    ])

JOBUN = [
    dict(law=L, art='39',
         quotes=['分筆又は合筆の登記は、表題部所有者又は所有権の登記名義人以外の者は、申請することができない。',
                 '2. 登記官は、前項の申請がない場合であっても、一筆の土地の一部が別の地目となり、又は地番区域（地番区域でない字を含む。第四十一条第二号において同じ。）を異にするに至ったときは、職権で、その土地の分筆の登記をしなければならない。',
                 '3. 登記官は、第一項の申請がない場合であっても、第十四条第一項の地図を作成するため必要があると認めるときは、第一項に規定する表題部所有者又は所有権の登記名義人の異議がないときに限り、職権で、分筆又は合筆の登記をすることができる。'],
         points=['**第1項は「申請できる人」を絞る規定**です。表題部所有者か、所有権の登記名義人だけ。所有権の移転の登記をまだ受けていない買主、抵当権者、地上権者は、自分の名で分筆を申請できません（買主が代わりに申請する「代位」は第9回で扱います）。',
                 '**共有の土地は、持分の価格の過半数で**申請できます。分筆・合筆は、共有物の形や効用を大きく変えない変更（民法第251条第1項かっこ書き・第252条第1項）として扱われ、過半数の持分を持つ共有者が申請人になります。ちょうど半分は過半数ではありません。',
                 '**第2項と第3項は語尾が違います。** 一筆の一部が別の地目になったときの職権分筆は「しなければならない」。地図を作るための職権の分筆・合筆は「異議がないときに限り」「できる」。',
                 '第2項があっても、地目が変わったことの登記（地目変更）を所有者が申請しなくてよいわけではありません（第37条。第4回）。'],
         shi=[('H26-Q10-ウ', '表題部所有者から土地を買っただけの人は、売主の承諾があっても分筆を申請できない'),
              ('R03-Q11-ア', '所有権の移転の登記を受けていない買主は、分筆を申請できない'),
              ('H28-Q09-イ', '共有物分割禁止の定めがあっても、分筆の登記は申請できる'),
              ('R06-Q08-オ', '持分3分の1ずつの共有地は、全員でなくても、持分の価格の過半数を持つ共有者で申請できる'),
              ('R03-Q11-オ', '持分2分の1の共有者は、他方の承諾書を付けても一人では申請できない（半分は過半数ではない）'),
              ('H17-Q06-1', '仮差押えの登記がある土地の分筆に、仮差押債権者の承諾は要らない'),
              ('H29-Q14-オ', '地図作成のための職権合筆は、所有権の登記名義人に異議があればできない')],
         zu=dict(title='第39条の3つの項', sub='申請できる人・しなければならない・できる',
                 layout=('Three horizontal bands from top to bottom, each a rounded card with an icon on the left.\n'
                         'Band 1 (pale blue), label 「第1項　申請できる人」: inside, a blue-circle group of two person icons labeled 「表題部所有者」 and '
                         '「所有権の登記名義人」, and a red-cross group of three person icons labeled 「買主（移転の登記前）」「抵当権者」「地上権者」. '
                         'A small tag under the blue group: 「共有なら持分の過半数」.\n'
                         'Band 2 (pale beige), label 「第2項　職権で分筆」: icon of one land plot whose corner has become a parking lot; conclusion tag '
                         '「しなければならない」 in bold.\n'
                         'Band 3 (pale beige), label 「第3項　地図を作るための職権」: icon of a registrar drawing a map; a condition tag '
                         '「異議がないときに限り」 and a conclusion tag 「できる」.\n'
                         'At the bottom, a yellow sticky note: 「語尾と条件を入れ替えた肢が出る」.'),
                 footer='不動産登記法第39条、民法第251条・第252条')),
    dict(law=L, art='40',
         quotes=['登記官は、所有権の登記以外の権利に関する登記がある土地について分筆の登記をする場合において、当該分筆の登記の申請情報と併せて当該権利に関する登記に係る権利の登記名義人（当該権利に関する登記が抵当権の登記である場合において、抵当証券が発行されているときは、当該抵当証券の所持人又は裏書人を含む。）が当該権利を分筆後のいずれかの土地について消滅させることを承諾したことを証する情報が提供されたとき（当該権利を目的とする第三者の権利に関する登記がある場合にあっては、当該第三者が承諾したことを証する情報が併せて提供されたときに限る。）は、…当該承諾に係る土地について当該権利が消滅した旨を登記しなければならない。'],
         points=['分筆すると、抵当権などの権利は、原則として分筆後の土地の両方にそのまま残ります。**分筆するだけなら、抵当権者の承諾は要りません。**',
                 '第40条は、分筆と**同時に、分筆後の「いずれかの」土地について**権利を消したいときの近道です。権利者の承諾を証する情報を付けます。',
                 '**両方の土地から消すことはできません。** 「いずれかの土地について」だからです（両方から消すなら、それは抵当権の抹消です）。',
                 'その権利を目的とする**第三者の権利**（抵当権の上の転抵当など）があるときは、その第三者の承諾も要ります。'],
         shi=[
              ('R05-Q09-イ', '分筆後の2筆の両方について、抵当権を消滅させることはできない'),
              ('H23-Q08-ア', '抵当権を目的とする第三者の権利があるときは、その第三者の承諾も要る'),
              ('H22-Q18-エ', '差押えの登記は、承諾があっても分筆の手続の中では消せない'),
              ('R07-Q11-ウ', '仮登記の権利者が承諾すれば、分筆後の一方の土地にその仮登記は移らない')],
         zu=dict(title='分筆と一緒に権利を消す', sub='第40条の使いどころ',
                 layout=('Top: a land plot with a chain-lock icon labeled 「抵当権」, split by a dashed line into two plots labeled 「甲」 and 「乙」.\n'
                         'Below, two outcome rows:\n'
                         'Row 1 (pale beige), label 「分筆するだけ」: both plots keep the chain-lock icon; tag 「承諾は要らない」.\n'
                         'Row 2 (pale blue), label 「乙だけ消したい」: plot 乙 has the lock removed with a blue circle mark; two small document icons '
                         'labeled 「抵当権者の承諾」 and 「その上の第三者の承諾」.\n'
                         'Row 3 (pale red), label 「甲も乙も消したい」: both locks removed, with one red cross mark and the tag 「分筆ではできない」.\n'
                         'Bottom sticky note: 「いずれかの土地について」.'),
                 footer='不動産登記法第40条')),
]

MISTAKES = [
    dict(title='分筆に権利者の承諾が要ると思い込む',
         sub='承諾が出てくるのは、権利を消すときだけ',
         wrong='抵当権や仮差押えの登記がある土地を分筆するには、その権利者の承諾が要る。',
         right='分筆は所有者だけで申請できる。承諾が要るのは、分筆と同時に一方の土地の権利を消すとき（第40条）だけ。',
         steps=['肢が「分筆するだけ」か「分筆と同時に権利を消す」かを見分ける', '分筆するだけなら、権利は両方の土地に残るので承諾は要らない', '権利を消すなら、権利者と、その上の第三者の承諾が要る'],
         callout='「承諾を証する情報」という言葉を見たら、権利を消す話かどうかを先に確かめます。分筆そのものの要件ではありません。',
         footer='不動産登記法第39条第1項・第40条',
         shi=['H17-Q06-1']),
    dict(title='共有の土地は、全員でないと分筆できない？',
         sub='持分の価格の過半数で申請する',
         wrong='共有の土地の分筆は、共有者全員で申請するか、一人が他の全員の承諾書を付けて申請する。',
         right='持分の価格の過半数を持つ共有者が申請人になれば足りる。一人でも、その人の持分が過半数でなければ申請できない。',
         steps=['共有者の持分を足して、申請する人の持分の合計が過半数かを見る', '過半数なら、その人たちが申請人になる（全員でなくてよい）', 'ちょうど半分や、承諾書を付けただけの一人は申請できない'],
         callout='分筆・合筆は、共有物の形や効用を大きく変えない変更として、持分の価格の過半数で決めます（民法第251条第1項かっこ書き・第252条第1項）。古い年度の肢は、改正前の考え方で作られていることがあります。',
         footer='不動産登記法第39条第1項、民法第251条・第252条',
         shi=['R06-Q08-オ', 'R03-Q11-オ', 'H17-Q06-4']),
    dict(title='抵当権は、分筆後の両方の土地から消せる？',
         sub='「いずれかの土地について」の意味',
         wrong='抵当権者が承諾すれば、分筆後の甲土地からも乙土地からも抵当権を消せる。',
         right='第40条で消せるのは、分筆後の「いずれかの」土地だけ。両方から消すことはできない。',
         steps=['消したい土地が分筆後の一方か両方かを見る', '一方なら、権利者の承諾を証する情報で消せる', '両方なら、第40条では消せない'],
         callout='第40条は「分筆後のいずれかの土地について消滅させることを承諾したことを証する情報」と書いています。両方から消すと、分筆と関係のない抵当権の抹消になってしまいます。',
         footer='不動産登記法第40条',
         shi=['R05-Q09-イ']),
]

SUMMARY = [
    '分筆・合筆を申請できるのは、表題部所有者か所有権の登記名義人だけ（第39条第1項）。買主・抵当権者・地上権者は自分の名で申請できない。',
    '共有の土地は、持分の価格の過半数を持つ共有者が申請人になる。ちょうど半分は過半数ではない。',
    '職権の分筆は、一部が別の地目になったら「しなければならない」、地図作成のためなら「異議がないときに限り、できる」。',
    '分筆するだけなら権利者の承諾は要らない。分筆と同時に一方の土地の権利を消すときだけ、承諾を証する情報を付ける（第40条）。両方からは消せない。',
]
NEXT = '次回（第2回）は、合筆ができない場合を並べた第41条と、その例外を定める不動産登記規則第105条です。地役権・抵当権・信託の登記の「同一なら合筆できる」の範囲を整理します。'
NOTES = ['共有の土地の分筆・合筆を持分の価格の過半数で申請できる扱いは、令和5年4月1日施行の民法改正（第251条第1項かっこ書き・第252条第1項）と、それを受けた法務省の通達（令和5年3月28日民二第533号）によるものです（年度別記事 令和6年度 第8問の確認事項で原文を確認）。']

HEADER = dict(
    store='ブエノスアイレスの「エル・アテネオ・グランド・スプレンディッド」（劇場を改装した書店。赤いカーテンの舞台、金の装飾のバルコニー席、天井画）',
    scene=('A former grand theater turned into a bookstore: tiers of curved balconies lined with bookshelves, gold ornamental railings, '
           'a painted dome ceiling with soft clouds, and a stage at the back framed by heavy crimson curtains where a reading cafe sits. '
           'Warm amber light from many small lamps.'),
    pose='she sits sideways on a velvet chair in a theater box seat, one elbow resting on the gilded balcony railing, holding a folded land plan in her other hand.',
    face='a calm, thoughtful half-smile, eyes looking slightly upward as if working out who can file the application.',
    prop='a folded paper land plan with a dashed dividing line (no text).',
    pose_ja='劇場のボックス席の椅子に横向きに座り、手すりに肘をかけ、土地の図面を持つ',
    face_ja='少し上を見て考えている、落ち着いた微笑み',
    l1='条文の逆引き図鑑', l2='分筆と合筆の申請人', sub='第三十九条と第四十条')
