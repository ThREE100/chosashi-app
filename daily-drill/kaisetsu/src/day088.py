def _k(*t, n=24):
    out = []
    for c in ''.join(t):
        if '一' <= c <= '龥' and c not in out:
            out.append(c)
    return out[:n]


_T1, _T2, _TOP = '申請できるのは誰か、', '費用はどう分ける？', '不動産登記法　筆界特定'
_cards = [
    dict(h='筆界特定は単独で申請できる',
         ill='an isometric scene of two neighboring land plots separated by a boundary line, the left plot labeled 「甲土地」 and the right plot labeled 「乙土地」. A figure standing on the left plot holds an application form alone, while a figure on the right plot stands aside with empty hands. A green check mark sits beside the figure with the form.',
         words=['甲土地', '乙土地'], tag='相手との共同は不要'),
    dict(h='市の申請は地図にない筆界だけ',
         ill='an isometric city hall building on the left with a figure holding an application form. In the middle a map sheet labeled 「地図」 is shown with one boundary line drawn on it, and a second boundary line drawn separately outside the map sheet is highlighted with a green glow. A green check mark sits beside the highlighted line.',
         words=['地図'], tag='所有者の同意が必要'),
    dict(h='筆界確定の判決後は却下',
         ill='an isometric courthouse desk with a gavel and a document labeled 「判決」. Beside it an application form is stamped with a round stamp labeled 「却下」. A green check mark sits beside the stamp.',
         words=['判決', '却下'], tag='確定した判決があるとき'),
    dict(h='費用は両側の申請人で等分',
         ill='an isometric scene of two figures standing on either side of a boundary line between two plots, each holding one half of a receipt that was split in two equal halves. A label 「等しい割合」 sits above the receipt. A green check mark sits beside the receipt.',
         words=['等しい割合'], tag='甲乙の二人なら等分'),
    dict(h='確定判決と抵触すれば失効',
         ill='an isometric page labeled 「筆界特定」 with a boundary line drawn on it. A second page labeled 「判決」 is laid over it, and the part of the first page that overlaps with the second page is drawn faded and gray. A green check mark sits beside the overlapping part.',
         words=['筆界特定', '判決'], tag='抵触する範囲で失効'),
]

D = dict(
    catch='申請は単独で、費用は等しく負担',
    intro='筆界特定について、だれが申請できるのか、どんなときに却下されるのか、費用はどう分担するのか、そして裁判との関係はどうなるのかを問う問題です（不動産登記法131条・132条・146条・148条）。この問題は、誤っているものの組合せを選びます。\n\nこの記事では、筆界特定を申請できる人の範囲と、費用の分担のしかたを、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('筆界特定は、隣の土地の所有者と共同しなくても、単独で申請できる',
               '土地の所有権登記名義人等は、その土地と隣接する他の土地との筆界について、筆界特定の申請をすることができます（不動産登記法131条1項）。相手方である隣地の所有者と共同で申請する必要はありません。\n\n本肢は正しいといえます。\n\n**たとえば**、甲土地の所有者Aさんが、隣の乙土地との境がはっきりしないと感じたとき、乙土地の所有者Bさんと話し合って一緒に申請しなくても、Aさん一人で筆界特定を申請できます。Bさんは、申請があったことを関係人として通知されます（同法133条1項1号）。'),
        'イ': ('地方公共団体が申請できるのは、地図に表示されない筆界に限られる',
               '地方公共団体は、その区域内の対象土地の所有権登記名義人等のうちいずれかの者の同意を得たときは、筆界特定を申請できます。ただし、申請できるのは、法14条1項の地図に表示されない筆界に限られます（不動産登記法131条2項のかっこ書）。\n\n問題文は、地図に表示されている筆界についても申請できるとしているので、本肢は誤りです。\n\n**たとえば**、A市が、市内の土地の所有者の一人の同意を得て筆界特定を申請しようとしても、その筆界が地図に表示されているものであれば、申請できません。'),
        'ウ': ('筆界を確定した判決があるときは、筆界特定の申請は却下される',
               '対象土地の筆界について、すでに民事訴訟の手続により筆界の確定を求める訴えに係る判決が確定しているときは、筆界特定登記官は、理由を付した決定で、申請を却下しなければなりません（不動産登記法132条1項6号）。訴えを不適法として却下した判決は、これに当たりません。\n\n本肢は正しいといえます。\n\n**たとえば**、甲土地と乙土地の筆界について、すでに裁判で筆界を確定する判決が確定している場合、その筆界について改めて筆界特定を申請しても、却下されます。'),
        'エ': ('申請人が両側の土地の所有者の2人なら、費用は等しい割合で負担する',
               '申請人が2人で、その一人が対象土地の一方の所有権登記名義人等、もう一人が他方の所有権登記名義人等であるときは、各申請人は、等しい割合で手続費用を負担します（不動産登記法146条2項）。\n\n問題文は「地積の割合に応じて負担する」としているので、本肢は誤りです。土地の広さは関係ありません。\n\n**たとえば**、広い甲土地のCさんと、狭い乙土地のDさんが一緒に申請したとき、費用は半分ずつです。広い土地の所有者が多く払うわけではありません。'),
        'オ': ('筆界特定の後に筆界確定の判決が確定したら、抵触する範囲で効力を失う',
               '筆界特定がされた後、その筆界について筆界の確定を求める訴えに係る判決が確定したときは、その筆界特定は、判決と抵触する範囲において、効力を失います（不動産登記法148条）。\n\n本肢は正しいといえます。\n\n**たとえば**、筆界特定で示された筆界の位置と、後から確定した判決の筆界の位置が食い違っている場合、その食い違う範囲については、判決が優先され、筆界特定は効力を失います。'),
    },
    summary=[
        ('ア', '正', '筆界特定は、隣の土地の所有権登記名義人等と共同しなくても、単独で申請できる'),
        ('イ', '誤', '地方公共団体が申請できるのは、地図に表示されない筆界に限られる'),
        ('ウ', '正', '筆界を確定した判決が確定しているときは、筆界特定の申請は却下される'),
        ('エ', '誤', '申請人が両側の土地の所有者の2人なら、費用は等しい割合で負担する（地積の割合ではない）'),
        ('オ', '正', '筆界特定の後に筆界確定の判決が確定したら、抵触する範囲で効力を失う'),
    ],
    summary_tail='イは「地図に表示されない筆界に限る」というかっこ書き、エは「等しい割合」と「地積の割合」を入れ替えた出題です。申請できる人と費用の分担は、条文の項ごとに分けて整理しましょう。',
    supplements=[
        '### 補足説明（エ）：手続費用の負担は、申請人の組合せで決まる\n\n筆界特定の手続費用は、申請人が負担します（146条1項）。申請人が複数いるときの分担は、次の表のとおりです。\n\n| 申請人の組合せ | 負担の割合 | 根拠 |\n|---|---|---|\n| 2人で、一人ずつが両側の土地の所有者 | 等しい割合 | 146条2項 |\n| 2人以上で、全員が一方の土地の所有者 | 持分の割合 | 146条3項 |\n| 3人以上で、両側の土地に所有者がいる | 各土地側で2分の1ずつ。同じ土地側が2人以上なら、その中で持分の割合 | 146条4項 |\n\n**たとえば**、甲土地のCさんと乙土地のDさんが申請すれば半分ずつです。甲土地のCさん・Eさんの共有者2人と乙土地のDさんの3人で申請すれば、まず甲側と乙側で半分ずつに分け、甲側の半分はCさんとEさんが持分の割合で分けます。',
        '### 補足説明（イ）：筆界特定を申請できる人は、2通り\n\n筆界特定を申請できるのは、次の2通りです（131条）。\n\n- 土地の所有権登記名義人等（1項）：単独で申請できる。\n- 地方公共団体（2項）：対象土地の所有権登記名義人等のうちいずれかの者の同意を得たとき。申請できるのは、法14条1項の地図に表示されない筆界に限る。\n\n「所有権登記名義人等」とは、所有権の登記がある土地なら所有権の登記名義人、所有権の登記がない土地なら表題部所有者、表題登記がない土地なら所有者をいい、その相続人その他の一般承継人を含みます（123条5号）。\n\n**たとえば**、所有者のAさんが亡くなり、相続人のFさんがまだ名義を変えていなくても、相続人であるFさんは、所有権登記名義人等に含まれます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第88日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法123条5号、131条1項・2項、132条1項6号、133条1項、146条1項から4項、148条は、`note-articles/laws/` 配下の原文で確認しました。',
        'イの「地図に表示されている筆界は申請できない」理由（すでに筆界が明確だから、など）は、条文には書かれていないため、記事では理由を説明していません。',
        '補足説明の相続人の例は、123条5号の「相続人その他の一般承継人を含む」という文言に沿って作った例です。',
    ],
    phrases=['筆界特定は単独で申請できます', '市の申請は地図にない筆界だけです', '確定判決があれば申請は却下です', '両側の二人なら費用は等しい割合です', '確定判決と抵触すれば効力を失います'],
    header=dict(t1=_T1, t2=_T2, topic=_TOP, kanji='・'.join(_k(_T1, _T2, _TOP))),
    poster_intro='筆界特定の手続を、「申請と却下」（グループA：ア・イ・ウ）と「費用と裁判との関係」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='筆界特定の決まりを整理', sub='不動産登記法 第131条・第132条・第146条・第148条（毎日ドリル 第88日）',
        col_a='申請と却下', col_b='費用と裁判との関係', n_a=3,
        cards=_cards,
        kanji=_k(*[c['h'] + c['tag'] + ''.join(c['words']) for c in _cards], '筆界特定の決まりを整理申請と却下費用と裁判との関係', n=24)),
    nb_label='イ・エ肢', nb_intro='イ・エの補足説明に合わせた2枚です。1枚目は、筆界特定を申請できる人の2通りを左右の表で示します。2枚目は、手続費用の負担を申請人の組合せごとに表で整理します。',
    notebooks=[
        dict(name='筆界特定を申請できる人', args=dict(
            title='筆界特定を申請できる人', sub='不動産登記法131条（毎日ドリル 第88日 イ）',
            req='a two-column table',
            layout="""--- TWO-COLUMN TABLE ---
Two panels side by side (left and right), same height. The two panel headers are different strings; draw them in different accent colors (blue on the left, green on the right). Keep every item exactly as written. Do not use check marks or crosses.

LEFT PANEL (blue accent):
Panel header: 所有権登記名義人等
Items (a plain list, one per row):
単独で申請できる
隣の土地の所有者との共同は不要
所有権の登記がある土地は所有権の登記名義人
所有権の登記がない土地は表題部所有者
表題登記がない土地は所有者

RIGHT PANEL (green accent):
Panel header: 地方公共団体
Items (a plain list, one per row):
所有権登記名義人等のうち、いずれかの者の同意が必要
申請できるのは、地図に表示されない筆界に限る""",
            callout='地方公共団体が申請できるのは、土地の所有権登記名義人等の同意を得たときで、しかも地図に表示されない筆界に限られます。\n地図に表示されている筆界については、地方公共団体は申請できません。',
            footer='不動産登記法123条5号、131条',
            kanji='・'.join(_k('所有権登記名義人等地方公共団体筆界特定申請単独共同隣土地表題部所有者同意地図表示不動産登記法')), what='panels',
            check='confirm the two panel headers are different strings (所有権登記名義人等 on the left and 地方公共団体 on the right) and that both lists are copied verbatim, ')),
        dict(name='手続費用の負担', args=dict(
            title='手続費用はどう分ける？', sub='不動産登記法146条（毎日ドリル 第88日 エ）',
            req='a three-row table',
            layout="""--- TABLE ---
A table with three rows. Each row has a scene on the left and the rule on the right, connected by a thin arrow. The three rule boxes are drawn in three different accent colors (blue, green, orange).
Row 1: scene 「申請人が二人。甲土地の所有者と乙土地の所有者が一人ずつ」 (two figures on either side of a boundary line) → 等しい割合
Row 2: scene 「申請人の全員が、一方の土地の所有者」 (three figures standing on the same plot) → 持分の割合
Row 3: scene 「申請人が三人以上。両側の土地に所有者がいる」 (two figures on one plot and one figure on the other plot) → 各土地側で二分の一ずつ。同じ土地側が二人以上なら、その中で持分の割合""",
            callout='広い土地か狭い土地かは、費用の分担には関係しません。\n両側の土地の所有者が一人ずつ申請するときは、等しい割合です。',
            footer='不動産登記法146条2項から4項',
            kanji='・'.join(_k('手続費用負担申請人二人土地所有者等割合持分全員一方三人両側各二分同')), what='table',
            check='confirm the three rule boxes are drawn in three different accent colors and that the rule strings are copied verbatim, ')),
    ],
)
