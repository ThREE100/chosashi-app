D = dict(
    catch='筆界特定の申請、却下、調査委員',
    intro='筆界特定について、「だれが申請できるか」「どんなときに申請が却下されるか」「どんな人は筆界調査委員になれないか」を問う問題です（不動産登記法123条・131条・132条・134条、不動産登記規則208条）。\n\nこの記事では、各肢の「例外」や「かっこ書き」に注目して、具体的な場面で確認していきましょう。問題は、誤っている記述の組合せを選ぶ形です。',
    sections={
        'ア': ('相続の登記がまだでも、相続人は筆界特定を申請できる',
               '土地の所有権登記名義人等は、その土地と隣接する土地との筆界について、筆界特定の申請をすることができます（不動産登記法131条1項）。所有権登記名義人等には、所有権の登記名義人の相続人その他の一般承継人も含まれます（同法123条5号）。\n\n本肢は正しいといえます。\n\n**たとえば**、父が亡くなって子が土地を相続したものの、名義の変更はまだ済んでいないとします。この子も、隣の土地との境をはっきりさせたいときは、自分で筆界特定を申請できます。'),
        'イ': ('地方公共団体の申請は、地図に表示されない筆界に限られる',
               '地方公共団体は、その区域内の対象土地の所有権登記名義人等のいずれかの同意を得たときは、筆界特定の申請をすることができます。ただし、その筆界は、14条1項の地図に表示されないものに限られます（不動産登記法131条2項）。\n\n問題文は、筆界が地図に表示されているものでも申請できるとしているので、本肢は誤りです。\n\n**たとえば**、市が道路の整備のため、隣り合う土地の境を確認したいとします。その境が地図にきちんと載っているときは、市は申請できません。地図に載っていない境なら、土地の所有者の一人の同意を得て申請できます。'),
        'ウ': ('訴えを却下した判決が確定しても、筆界特定の申請は却下されない',
               '筆界特定の申請が却下される場合の一つが、対象土地の筆界について、すでに筆界の確定を求める訴えに係る判決が確定しているときです。ただし、訴えを不適法として却下した判決は除かれています（不動産登記法132条1項6号）。\n\n訴えを不適法として却下した判決は、筆界の位置を判断していません。問題文は、この判決を理由に申請を却下するとしているので、本肢は誤りです。\n\n**たとえば**、境の確定を求める訴えが、訴えの形に不備があるとして却下されたとします。境は裁判所に判断されていないので、その後に隣の所有者がした筆界特定の申請は、この理由では却下されません。'),
        'エ': ('対象土地の一方が共通なら、一つの申請情報で複数の申請ができる',
               '対象土地の一つを共通にする複数の筆界特定の申請は、一つの筆界特定申請情報によってすることができます（不動産登記規則208条）。\n\n本肢は正しいといえます。\n\n**たとえば**、甲土地が、東の乙土地と南の丙土地の両方に隣接しているとします。甲土地を共通にして、乙土地との筆界と丙土地との筆界の特定を、一つの申請でまとめて求められます。'),
        'オ': ('関係土地の抵当権者は、筆界調査委員に指定できない',
               '筆界調査委員には、対象土地や関係土地の所有権の登記名義人のほか、所有権以外の権利の登記名義人も、指定することができません（不動産登記法134条2項1号）。\n\n関係土地とは、対象土地以外の土地で、対象となる筆界上の点を含む他の筆界で、対象土地の一方または双方と接するものです（同法123条4号）。丁土地は、これに当たります。本肢は正しいといえます。\n\n**たとえば**、丁土地に抵当権の登記を受けている銀行Eは、甲土地と乙土地の筆界を調べる筆界調査委員には指定できません。調査をする人が、関係する土地の権利者であってはならないからです。'),
    },
    summary=[
        ('ア', '正', '相続人その他の一般承継人も所有権登記名義人等に含まれ、相続の登記がまだでも筆界特定を申請できる'),
        ('イ', '誤', '地方公共団体が申請できるのは、地図に表示されない筆界に限られる'),
        ('ウ', '誤', '訴えを不適法として却下した判決は、却下事由の確定判決から除かれる'),
        ('エ', '正', '対象土地の一つを共通にする複数の申請は、一つの筆界特定申請情報でできる'),
        ('オ', '正', '関係土地の所有権以外の権利の登記名義人は、筆界調査委員に指定できない'),
    ],
    summary_tail='イは「かっこ書きの見落とし」、ウは「確定判決の範囲」を取り違えた出題です。筆界特定は、申請できる人と、却下の理由を、例外とセットで確認しましょう。',
    supplements=[
        '### 補足説明（イ）：筆界特定を申請できる人\n\n筆界特定の申請人は、大きく2つに分けて整理できます。\n\n- 土地の所有権登記名義人等：自分の土地と隣の土地との筆界について、申請できる（131条1項）。相続人などの一般承継人を含む（123条5号）。\n- 地方公共団体：所有権登記名義人等の一人の同意を得て、地図に表示されない筆界についてだけ、申請できる（131条2項）。\n\n**たとえば**、同じ筆界でも、土地の所有者は自分の判断で申請できますが、市が申請するには、土地の所有者の同意と、その筆界が地図にないこと、の両方が必要です。',
        '### 補足説明（ウ）：判決が出ていても却下されない場合\n\n筆界を確定する訴えの判決が確定しているときは、筆界特定の申請は却下されます（132条1項6号）。ただし、訴えを不適法として却下した判決は、筆界の位置を判断したものではないので、この却下事由から除かれます。\n\n**たとえば**、境の位置を裁判所が判断した判決が確定した後に筆界特定を申請すると、却下されます。訴えの形が整っていないとして裁判所が審理に入らなかった場合は、境がまだ判断されていないので、筆界特定を申請できます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第17日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法123条、131条、132条、134条、不動産登記規則208条は、`note-articles/laws/` 配下の原文で確認しました。',
        'イの具体例（市の道路整備）、ウの具体例（訴えの形に不備がある場合）、オの具体例（銀行Eが指定できない理由）は、条文の文言から導いた一般的な説明です。個別の運用・先例の確認はしていません。',
        'オの「調査をする人が関係する土地の権利者であってはならない」という説明は、134条2項各号の趣旨の一般的な整理です。',
    ],
    phrases=['相続の登記前でも筆界特定は申請できます', '市の申請は地図にない筆界だけです', '訴えを却下した判決は却下事由ではありません', '共通の土地があれば一つの申請でできます', '関係土地の抵当権者は委員になれません'],
    header=dict(t1='筆界特定の申請、', t2='誰ができる？', topic='不動産登記法　筆界特定の申請',
                kanji='筆・界・特・定・申・請・登・記'),
    poster_intro='筆界特定の申請と手続を、「申請できる人」（グループA：ア・イ）と「却下と手続」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='筆界特定の申請と却下を整理', sub='不動産登記法 第131条・第132条・第134条（毎日ドリル 第17日）',
        col_a='申請できる人', col_b='却下と手続', n_a=2,
        cards=[
            dict(h='相続人も筆界特定を申請できる',
                 ill='a person figure carrying a name tag labeled 「相続人」 holding a form labeled 「筆界特定」, standing beside two neighboring land plots with a dotted boundary line between them. A green check mark sits beside the figure.',
                 words=['相続人', '筆界特定'], tag='相続登記の前でも可'),
            dict(h='市の申請は地図にない筆界だけ',
                 ill='a city hall building on the left and two land plots on the right. A map sheet labeled 「地図」 beside the plots shows no boundary line between the two plots. A green check mark sits beside the plots.',
                 words=['地図'], tag='地図にない筆界だけ'),
            dict(h='訴え却下の判決なら申請できる',
                 ill='a courthouse building with a document labeled 「訴え却下」 in front of it, and a thin arrow pointing to a form labeled 「筆界特定」. A green check mark sits beside the form.',
                 words=['訴え却下', '筆界特定'], tag='却下事由に当たらない'),
            dict(h='共通の土地があれば一つの申請で',
                 ill='three land plots in a row, with the middle plot touching both of the others. One single form labeled 「筆界特定」 covers both boundary lines. A green check mark sits beside the form.',
                 words=['筆界特定'], tag='対象土地が共通'),
            dict(h='関係土地の抵当権者は委員になれない',
                 ill='a faded gray person figure carrying a name tag labeled 「抵当権者」 standing beside a land plot, and a surveyor figure with a tripod in front of the plot. No check mark and no cross mark on this card.',
                 words=['抵当権者'], tag='委員に指定できない'),
        ],
        kanji='筆・界・特・定・申・請・相・続・人・地・図・訴・却・下・共・通・抵・当・権・者・委・員・指'.split('・')),
    nb_label='イ・ウ肢', nb_intro='イ・ウの補足説明に合わせた2枚です。1枚目は、筆界特定を申請できる人を左右の対比で示します。2枚目は、確定判決の種類と、筆界特定の申請が却下されるかどうかを左右の対比で示します。',
    notebooks=[
        dict(name='筆界特定を申請できる人', args=dict(
            title='筆界特定を申請できる人は？', sub='所有権登記名義人等と地方公共団体（毎日ドリル 第17日 イ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings, 「所有権登記名義人等」 on the left and 「地方公共団体」 on the right. Draw them in different accent colors (blue and green) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 所有権登記名義人等
Scene: an isometric scene of two person figures beside two neighboring land plots; one carries a name tag 「相続人」. Both hold a form.
Result badge: 自分で申請できる

RIGHT PANEL (green accent):
Panel header: 地方公共団体
Scene: an isometric scene of a city hall building and two land plots. Two small condition tags are attached to the building: 「同意」 and 「地図にない筆界」.
Result badge: 二つの条件がそろえば申請できる""",
            callout='土地の所有権登記名義人等は、相続人などの一般承継人も含めて、自分で申請できます。\n地方公共団体は、所有権登記名義人等の同意を得て、地図に表示されない筆界についてだけ申請できます。',
            footer='不動産登記法123条5号、131条',
            kanji='所・有・権・登・記・名・義・人・地・方・公・共・団・体・自・分・申・請・図・界・相・続・同・意・件'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (所有権登記名義人等 on the left and 地方公共団体 on the right) drawn in different accent colors, ')),
        dict(name='確定判決の種類と却下', args=dict(
            title='判決が出ていたら、却下される？', sub='確定判決の種類による違い（毎日ドリル 第17日 ウ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings, 「筆界を判断した判決」 on the left and 「訴えを却下した判決」 on the right. Draw them in different accent colors (orange and blue) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (orange accent):
Panel header: 筆界を判断した判決
Scene: an isometric courthouse with a judge's gavel and a document showing two land plots with a solid boundary line between them.
Result badge: 申請は却下される

RIGHT PANEL (blue accent):
Panel header: 訴えを却下した判決
Scene: an isometric courthouse with a closed door and a document showing two land plots with a dotted boundary line between them.
Result badge: 申請は却下されない""",
            callout='筆界の確定を求める訴えの判決が確定していると、筆界特定の申請は却下されます。\nただし、訴えを不適法として却下した判決は、筆界を判断していないので、却下の理由になりません。',
            footer='不動産登記法132条1項6号',
            kanji='筆・界・判・断・決・訴・却・下・申・請・確・定・適・法'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (筆界を判断した判決 on the left and 訴えを却下した判決 on the right) drawn in different accent colors, ')),
    ],
)
