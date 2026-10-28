D = dict(
    catch='合筆できるか、名義人と権利を見る',
    intro='土地の合筆の登記について、「どんな土地は合筆できないのか」と「だれが申請できるのか」を問う問題です（不動産登記法39条・41条、不動産登記規則105条）。\n\nこの記事では、合筆できない土地のルールと、その例外、そして申請できる人と登記官が自分で合筆できる場合を、具体的な場面で確認していきましょう。なお、この問題は「誤っているもの」を選ぶ問題です。',
    sections={
        'ア': ('名義人の顔ぶれが違えば、合筆できない',
               '表題部所有者又は所有権の登記名義人が相互に異なる土地の合筆の登記は、することができません（不動産登記法41条3号）。\n\n甲土地の登記名義人はA、乙土地はA及びBです。Aが両方に含まれていても、名義人は相互に異なります。本肢は正しいといえます。\n\n**たとえば**、甲土地はAさん一人の名義、隣の乙土地はAさんとBさんの共有名義だとします。Aさんが両方に関わっていても、名義人の顔ぶれが違うので、そのままでは合筆できません。'),
        'イ': ('同じ内容の担保権の登記なら、合筆できる',
               '所有権の登記以外の権利に関する登記がある土地の合筆は、原則としてできません（不動産登記法41条6号）。ただし、法務省令で定める登記は例外です。\n\n担保権の登記で、登記の目的、申請の受付の年月日及び受付番号、登記原因及びその日付が同一のものは、その例外に当たります（不動産登記規則105条2号）。本肢は正しいといえます。\n\n**たとえば**、同じ銀行から借りたお金のために、甲土地と乙土地に一つの申請で同じ抵当権の登記をしたとします。この場合は、合筆後の土地にも同じ抵当権を登記できるので、合筆することができます。'),
        'ウ': ('承役地の地役権の登記があっても、合筆できる',
               '承役地についてする地役権の登記も、合筆の制限の例外です（不動産登記規則105条1号）。\n\n問題文は「合筆の登記をすることができない」としていますが、承役地の地役権の登記があっても、ほかの要件を満たせば合筆できます。本肢は誤りです。\n\n**たとえば**、隣の土地の人が通る道として使っている甲土地（承役地）に、地役権の登記があるとします。この甲土地は、これに接続する乙土地と合筆できます。合筆のあとは、地役権の及ぶ範囲が地役権図面番号とともに記録されます（同規則107条2項・3項）。'),
        'エ': ('買っただけでは、合筆を申請できない',
               '分筆又は合筆の登記は、表題部所有者又は所有権の登記名義人以外の者は、申請することができません（不動産登記法39条1項）。\n\n甲土地の所有権の登記名義人はまだAなので、買ったBは申請人になれません。また、甲土地はA、乙土地はBが名義人で、名義人が相互に異なります（同法41条3号）。本肢は誤りです。\n\n**たとえば**、Bさんが、Aさん名義の甲土地を買ったばかりで、名義変更をしていないとします。Bさんは、自分名義の隣の乙土地と合筆したくても、先にAさんからBさんへの所有権の移転の登記を受けなければなりません。'),
        'オ': ('地図のための職権の合筆は、異議がないときに限る',
               '登記官は、申請がない場合でも、地図を作成するため必要があると認めるときは、表題部所有者又は所有権の登記名義人の異議がないときに限り、職権で分筆又は合筆の登記をすることができます（不動産登記法39条3項）。本肢は正しいといえます。\n\n**たとえば**、登記所が地図を整える作業の中で、隣り合う土地を一筆にまとめたほうがよいと考えたとします。所有者から異議が出ているときは、職権で合筆することはできません。「承諾があるとき」ではなく「異議がないとき」に限る点に注意しましょう。'),
    },
    summary=[
        ('ア', '正', '名義人が相互に異なる土地は、Aが共通していても合筆できない'),
        ('イ', '正', '登記の目的や受付などが同一の担保権の登記なら、合筆できる'),
        ('ウ', '誤', '承役地の地役権の登記は例外なので、あっても合筆できる'),
        ('エ', '誤', '買っただけのBは申請人になれず、先に所有権の移転の登記が必要'),
        ('オ', '正', '地図作成のための職権の合筆は、名義人の異議がないときに限る'),
    ],
    summary_tail='ウは「権利の登記があれば合筆できない」という原則の例外を見落とした出題、エは「実際の所有者」と「登記名義人」を入れ替えた出題です。合筆は、名義人と権利の登記の両方を見て判断しましょう。',
    supplements=[
        '### 補足説明（ウ）：合筆できない土地と、その例外\n\n合筆できない土地は、不動産登記法41条の各号で決まっています。\n\n| 合筆できない土地 | ポイント |\n|---|---|\n| 相互に接続していない土地 | 隣り合っていなければならない |\n| 地目又は地番区域が異なる土地 | 地目も地番区域も同じ必要がある |\n| 名義人が相互に異なる土地 | 顔ぶれが同じでなければならない |\n| 名義人が相互に持分を異にする土地 | 持分の割合も同じでなければならない |\n| 所有権の登記がない土地と、ある土地 | 登記の有無がそろっている必要がある |\n| 所有権以外の権利の登記がある土地 | 例外あり（下の例外） |\n\n最後の例外は、不動産登記規則105条が定めています。承役地の地役権の登記、登記の目的などが同一の担保権の登記、同一内容の信託の登記、同一の鉱害賠償登録に関する登記がある土地は、合筆できます。\n\n**たとえば**、通行のための地役権が付いた土地や、同じ抵当権が付いた隣り合う二つの土地は、ほかの要件を満たせば合筆できます。',
        '### 補足説明（エ・オ）：申請できる人と、登記官が自分でするとき\n\n合筆の登記は、申請によってするのが原則です。登記官が自分の判断（職権）でするのは、限られた場面だけです。\n\n- 申請：表題部所有者又は所有権の登記名義人だけが申請できます（不動産登記法39条1項）。\n- 職権：地図を作成するため必要があると認めるときに、表題部所有者又は所有権の登記名義人の異議がないときに限ってできます（同条3項）。\n\n**たとえば**、買ったばかりで名義変更をしていない人は申請できません。一方、登記所が地図づくりのために合筆するときは、名義人の異議がないことが条件になります。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第36日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法39条・41条、不動産登記規則105条・107条は、`note-articles/laws/` 配下の原文で確認しました。',
        '各肢の具体例（共有名義の隣地、同じ銀行の抵当権、通行のための地役権、買ったばかりの人）は、条文の文言をかみ砕いた一般的な説明で、個別の先例・通達の確認はしていません。',
        '補足説明（ウ）の表の「ポイント」の列は、41条各号の文言を言い換えた一般的な整理で、条文そのものではありません。',
    ],
    phrases=['名義人が違えば合筆できません', '同じ担保権なら合筆できます', '承役地の地役権は例外です', '申請できるのは登記名義人だけです', '職権の合筆は異議がないときだけ'],
    header=dict(t1='合筆できる土地、', t2='できない土地？', topic='不動産登記法　合筆の登記',
                kanji='合・筆・登・記・土・地'),
    poster_intro='合筆の登記を、「合筆できるかどうか」（グループA：ア・イ・ウ）と「申請する人と職権」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='合筆の登記を整理', sub='不動産登記法 第39条・第41条（毎日ドリル 第36日）',
        col_a='合筆できるかどうか', col_b='申請する人と職権', n_a=3,
        cards=[
            dict(h='名義人の顔ぶれが違えば合筆できない',
                 ill='two adjacent isometric land plots. The left plot carries a name tag labeled 「一人」 and the right plot carries a name tag labeled 「二人」. A padlock icon sits on the boundary line between them, and the merging arrow above is drawn in faded gray. No check mark and no cross mark on this card.',
                 words=['一人', '二人'], tag='名義人が違うと不可'),
            dict(h='同じ内容の担保権なら合筆できる',
                 ill='two adjacent isometric land plots, each with an identical small record sheet labeled 「抵当権」 beside it. A green arrow merges the two plots into one larger plot. A green check mark sits beside the merged plot.',
                 words=['抵当権'], tag='同一の担保権は例外'),
            dict(h='承役地の地役権があっても合筆できる',
                 ill='an isometric land plot with a narrow path strip across it and a small document labeled 「地役権」 beside the path. A green arrow merges this plot with the neighboring plot. A green check mark sits beside the merged plot.',
                 words=['地役権'], tag='承役地は例外'),
            dict(h='申請できるのは名義人だけ',
                 ill='a counter scene. A figure with a name tag labeled 「名義人」, highlighted with a green glow, submits a form at the counter. A second figure labeled 「買主」, drawn in faded gray, stands aside holding a rolled contract. A green check mark sits beside the first figure.',
                 words=['名義人', '買主'], tag='先に名義変更が必要'),
            dict(h='職権の合筆は異議がないときだけ',
                 ill='a registrar figure at a desk holding a map sheet labeled 「地図」, and an owner figure beside the desk giving a small nod and holding a note labeled 「異議なし」. A green check mark sits above the group.',
                 words=['地図', '異議なし'], tag='異議がないときに限る'),
        ],
        kanji='合・筆・名・義・人・担・保・権・同・地・役・承・申・請・先・変・更・職・異・議・図・買・主'.split('・')),
    nb_label='ウ・エ・オ肢', nb_intro='ウ・エ・オの補足説明に合わせた2枚です。1枚目は、合筆できない土地とその例外を左右の対比で示します。2枚目は、合筆を申請できる人と、登記官が職権でするときを左右の対比で示します。',
    notebooks=[
        dict(name='合筆できない土地と、その例外', args=dict(
            title='合筆できない土地と、その例外', sub='合筆の登記の制限（毎日ドリル 第36日 ウ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「合筆できない土地」 on the left and 「権利の登記があっても合筆できる」 on the right. Draw them large and in different accent colors (blue and green). Do not draw any check mark or cross mark on this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 合筆できない土地
Scene: six small rows stacked vertically, each with a small land plot icon and one of these exact labels: 接続していない | 地目や地番区域が違う | 名義人が違う | 持分が違う | 所有権の登記の有無が違う | 所有権以外の権利の登記がある

RIGHT PANEL (green accent):
Panel header: 権利の登記があっても合筆できる
Scene: two small rows stacked vertically, each with a small icon and one of these exact labels: 承役地の地役権の登記 | 同一の担保権の登記
Result badge: 規則で定める例外""",
            callout='所有権以外の権利の登記がある土地は、原則として合筆できません。\nただし、承役地の地役権の登記や、同一の担保権の登記などは例外で、合筆できます。',
            footer='不動産登記法41条、不動産登記規則105条',
            kanji='合・筆・土・地・目・名・義・人・持・分・所・有・権・登・記・承・役・担・保・規・則'.split('・'), what='panels',
            check='confirm the two panel headers are different strings in different accent colors, that the left panel has exactly six rows and the right panel exactly two rows, and that no check mark and no cross mark is drawn, ')),
        dict(name='合筆を申請できる人と、職権でするとき', args=dict(
            title='合筆はだれがするの？', sub='申請と職権（毎日ドリル 第36日 エ・オ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「申請できる人」 on the left and 「登記官が職権でするとき」 on the right. Draw them large and in different accent colors (blue and orange). Do not draw any check mark or cross mark on this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 申請できる人
Scene: an isometric scene of two figures at a counter with name tags: 表題部所有者 and 所有権の登記名義人. A third figure holding a contract, with a name tag 買っただけの人, stands aside in faded gray.
Result badge: この人たちだけ

RIGHT PANEL (orange accent):
Panel header: 登記官が職権でするとき
Scene: an isometric scene of a registrar figure at a desk holding a map sheet, with a note beside it labeled 地図を作成するため必要. An owner figure nods with a note labeled 異議がない.
Result badge: 異議がないときに限る""",
            callout='合筆の申請ができるのは、表題部所有者又は所有権の登記名義人だけです。\n登記官が職権でするときは、地図を作成するため必要で、名義人の異議がないときに限ります。',
            footer='不動産登記法39条',
            kanji='合・筆・申・請・表・題・部・所・有・者・権・登・記・名・義・人・買・職・異・議・地・図・作・成・必・要'.split('・'), what='panels',
            check='confirm the two panel headers are different strings in different accent colors, and that no check mark and no cross mark is drawn, ')),
    ],
)
