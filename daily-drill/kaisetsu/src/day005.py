def kj(*ss, n=14):
    out = []
    for s in ss:
        for c in s:
            if '一' <= c <= '龥' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='職権の分筆は、異議がないときに限る',
    intro='土地の分筆の登記について、「だれが申請できるのか」「登記官が自分で分筆できるのはどんなときか」「抵当権があるときはどうなるのか」を問う問題です（不動産登記法39条・40条）。\n\nこの記事では、登記官が職権で分筆する二つの場面の違いと、抵当権を分筆後の一部の土地から外すときの条件を、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('分筆や合筆を申請できるのは、所有者と名義人だけ',
               '分筆又は合筆の登記は、表題部所有者又は所有権の登記名義人以外の者は、申請することができません（不動産登記法39条1項）。\n\n本肢は正しいといえます。\n\n**たとえば**、隣の土地の所有者や、土地を借りている人が「この土地を二つに分けたほうがよい」と考えても、自分で分筆の登記を申請することはできません。申請できるのは、その土地の所有者などに限られます。'),
        'イ': ('地番区域をまたぐようになったら、登記官が職権で分筆する',
               '登記官は、申請がない場合であっても、一筆の土地の一部が別の地目となり、又は地番区域を異にするに至ったときは、職権で、その土地の分筆の登記をしなければなりません（不動産登記法39条2項）。\n\n本肢は正しいといえます。\n\n**たとえば**、一筆の土地の途中に地番区域の境目ができてしまい、一つの地番では表せなくなったとします。このときは、所有者の申請を待たずに、登記官が地番区域ごとに土地を分けます。'),
        'ウ': ('地図を作るための職権の分筆や合筆は、異議がないときに限る',
               '登記官は、申請がない場合であっても、地図を作成するため必要があると認めるときは、表題部所有者又は所有権の登記名義人の異議がないときに限り、職権で、分筆又は合筆の登記をすることができます（不動産登記法39条3項）。\n\n問題文は「異議の有無にかかわらず」としていますが、条文は「異議がないときに限り」です。本肢は誤りです。\n\n**たとえば**、法務局が地図を整えるために、ある土地を分けたいと考えたとします。所有者が反対しているのに、登記官が勝手に分筆することはできません。'),
        'エ': ('抵当権の登記名義人が承諾したら、消滅の登記をしなければならない',
               '所有権の登記以外の権利に関する登記がある土地について分筆の登記をする場合に、その権利を分筆後のいずれかの土地について消滅させることを承諾したことを証する情報が提供されたときは、登記官は、権利が消滅した旨を登記しなければなりません（不動産登記法40条）。\n\n本肢は正しいといえます。\n\n**たとえば**、銀行の抵当権がついた土地の一部だけを売りたいとき、銀行が「売る部分からは抵当権を外してよい」と承諾した書類を出せば、売る部分の登記記録から抵当権が消えます。'),
        'オ': ('抵当権を目的とする第三者の権利があれば、その人の承諾も必要',
               '40条のかっこ書きは、その権利を目的とする第三者の権利に関する登記がある場合は、その第三者が承諾したことを証する情報も併せて提供されたときに限る、と定めています（不動産登記法40条）。\n\n問題文は、第三者の承諾がなくても消滅の登記をしなければならないとしています。本肢は誤りです。\n\n**たとえば**、銀行の抵当権に、さらに別の人の権利の登記（転抵当など）がついているとします。このときは、銀行の承諾だけでなく、その別の人の承諾も出さなければ、抵当権を外す登記はされません。'),
    },
    summary=[
        ('ア', '正', '分筆や合筆は、表題部所有者又は所有権の登記名義人以外の者は申請できない'),
        ('イ', '正', '一筆の土地の一部が地番区域を異にするに至ったときは、登記官が職権で分筆する'),
        ('ウ', '誤', '地図を作成するための職権の分筆や合筆は、異議がないときに限ってできる'),
        ('エ', '正', '抵当権の登記名義人が消滅を承諾したことを証する情報が提供されたら、消滅の登記をしなければならない'),
        ('オ', '誤', '抵当権を目的とする第三者の権利に関する登記があるときは、その第三者の承諾を証する情報も併せて提供されたときに限る'),
    ],
    summary_tail='ウは「異議がないときに限る」という条件を外した出題、オは「第三者の承諾も必要」という例外を外した出題です。職権の分筆は「しなければならない場合」と「異議がなければできる場合」を分け、抵当権の消滅は「承諾の連鎖」をたどりましょう。',
    supplements=[
        '### 補足説明（ウ）：職権の分筆は、二つの場面で性格が違う\n\n登記官が申請なしで分筆をする場面は、39条に二つあります。\n\n| | 39条2項 | 39条3項 |\n|---|---|---|\n| きっかけ | 一部が別の地目になった、又は地番区域を異にするに至った | 地図を作成するため必要がある |\n| 登記官の義務 | しなければならない | することができる |\n| 所有者の異議 | 関係しない | 異議がないときに限る |\n\n**たとえば**、一筆の土地の一部が地番区域を異にするに至ったときは、所有者の気持ちに関係なく、登記官が分筆します。これに対し、地図を整えるための分筆や合筆は、所有者に異議がなければ行うことができる、という扱いです。',
        '### 補足説明（オ）：抵当権を外すには、承諾が順番に必要になる\n\n分筆の登記と一緒に、抵当権を分筆後の一部の土地から外すには、承諾を証する情報を出します（不動産登記法40条）。\n\n- 抵当権の登記名義人の承諾：いつも必要。\n- その抵当権を目的とする第三者の権利の登記がある場合は、その第三者の承諾：併せて必要。\n\n**たとえば**、A銀行の抵当権に、別の人Bの権利の登記がついている土地を分筆するとします。Aの承諾だけでは足りず、Bの承諾も出して初めて、承諾に係る土地から抵当権が消える登記がされます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第5日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法39条1項から3項まで、40条は、`note-articles/laws/` 配下の原文で確認しました。',
        'イの具体例（地番区域の境目ができる場面）は、39条2項の文言から導いた一般的な説明で、実際にどのような場面で起こるかの運用までは確認していません。',
        'エ・オの具体例（売る部分だけ抵当権を外す、転抵当）は、40条の文言をかみ砕いた一般的な説明です。転抵当が「抵当権を目的とする第三者の権利」の例になることは、条文の文言からの整理で、先例の確認はしていません。',
    ],
    phrases=['分筆を申請できるのは所有者だけです', '地番区域をまたいだら職権で分筆です', '地図づくりの職権は異議なしに限ります', '抵当権は承諾があれば外せます', '第三者の承諾も一緒に必要なんです'],
    header=dict(t1='職権の分筆って、', t2='いつできる？', topic='不動産登記法　土地の分筆',
                kanji='職・権・分・筆・毎'),
    poster_intro='土地の分筆の登記を、「申請と職権の分筆」（グループA：ア・イ・ウ）と「分筆に伴う抵当権の消滅」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='土地の分筆の登記を整理', sub='不動産登記法 第39条・第40条（毎日ドリル 第5日）',
        col_a='申請と職権の分筆', col_b='抵当権の消滅', n_a=3,
        cards=[
            dict(h='分筆の申請は所有者と名義人だけ',
                 ill='an isometric land plot with a dotted line splitting it into two parts. An owner figure at a desk, holding a form, is highlighted with a green glow and carries a name tag labeled 「所有者」. A faded gray neighbor figure with no tag stands aside. A green check mark sits beside the owner.',
                 words=['所有者'], tag='申請人は限定'),
            dict(h='地番区域をまたいだら職権で分筆',
                 ill='an isometric land plot crossed by a thick boundary line between two districts. A registry officer figure carries a name tag labeled 「登記官」 and splits the plot along the boundary line. A green check mark sits beside the officer.',
                 words=['登記官'], tag='申請がなくても'),
            dict(h='地図づくりの職権は異議がないとき',
                 ill='an isometric land plot with a map sheet beside it. An owner figure raises a friendly open hand with a green check mark, and a registry officer figure labeled 「登記官」 is splitting the plot. The scene shows consent, with no argument.',
                 words=['登記官'], tag='異議がないときに限る'),
            dict(h='抵当権の登記名義人が承諾したら外せる',
                 ill='an isometric land plot split into two parts. A bank figure carrying a name tag 「抵当権者」 hands a signed consent sheet to a registry officer. On one of the two parts a lock-shaped stamp is lifting away. A green check mark sits beside the consent sheet.',
                 words=['抵当権者'], tag='承諾で消滅の登記'),
            dict(h='第三者の権利があれば、その人の承諾も',
                 ill='two consent sheets stacked in a row, side by side with two figures. The left figure carries a name tag 「抵当権者」 and the right figure carries a name tag 「第三者」. Both hold signed sheets with a green check mark above them.',
                 words=['抵当権者', '第三者'], tag='承諾は両方'),
        ],
        kanji=kj('分筆申請所有者地番区域職権登記官異議抵当権承諾第三者')),
    nb_label='ウ・オ肢', nb_intro='ウ・オの補足説明に合わせた2枚です。1枚目は、職権の分筆の二つの場面を左右の対比で示します。2枚目は、抵当権を外すための承諾の流れを示します。',
    notebooks=[
        dict(name='職権の分筆は、二つの場面で違う', args=dict(
            title='職権の分筆は、いつできる？', sub='不動産登記法39条2項と3項（毎日ドリル 第5日 ウ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「39条2項」 on the left and 「39条3項」 on the right. Draw them large and in different accent colors (blue on the left, green on the right) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 39条2項
Scene: an isometric land plot crossed by a boundary line between two districts, with a registry officer figure splitting it.
Rows of text:
きっかけ: 地番区域を異にするに至った
登記官: しなければならない
所有者の異議: 関係しない

RIGHT PANEL (green accent):
Panel header: 39条3項
Scene: an isometric land plot with a map sheet beside it, and a registry officer figure waiting beside an owner figure who gives a friendly open hand.
Rows of text:
きっかけ: 地図を作成するため必要がある
登記官: することができる
所有者の異議: 異議がないときに限る""",
            callout='地図を作成するための職権の分筆や合筆は、所有者又は名義人の異議がないときに限り、することができます。\n異議の有無にかかわらず分筆できるわけではありません。',
            footer='不動産登記法39条2項・3項',
            kanji=kj('職権分筆地番区域異議所有者登記官'), what='panels',
            check='confirm the two panel headers are different strings (39条2項 on the left and 39条3項 on the right) drawn in different accent colors, ')),
        dict(name='抵当権を外すための承諾の流れ', args=dict(
            title='抵当権を外すには、誰の承諾？', sub='分筆に伴う権利の消滅の登記（毎日ドリル 第5日 オ）',
            req='a step-by-step flow diagram',
            layout="""--- FLOW ---
A clean flat-design vertical flow with three steps connected by downward arrows.

Step 1 (blue box): 分筆の申請
Icon: a land plot split into two parts.

Step 2 (green box, two figures side by side): 承諾を証する情報を一緒に出す
Left figure with a name tag: 抵当権の登記名義人
Right figure with a dotted outline and a name tag: 第三者（その権利を目的とする権利の登記がある場合）
Both figures hold signed sheets with a green check mark.

Step 3 (green box): 承諾に係る土地から、権利が消滅した旨を登記する
Icon: a lock-shaped stamp lifting away from one of the two land plots.""",
            callout='抵当権を外すには、抵当権の登記名義人の承諾を証する情報を提供します。\nその抵当権を目的とする第三者の権利に関する登記があるときは、その第三者の承諾を証する情報も、併せて提供されたときに限ります。',
            footer='不動産登記法40条',
            kanji=kj('抵当権分筆承諾第三者登記名義人'), what='flow',
            check='confirm that the three steps are connected by downward arrows and that the second step shows both the mortgagee figure and the dotted third-party figure, ')),
    ],
)
