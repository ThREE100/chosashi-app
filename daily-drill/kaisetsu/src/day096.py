def kj(*texts, n=20):
    out = []
    for t in texts:
        for c in t:
            if '一' <= c <= '鿿' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='放棄は他の共有者へ、分割禁止は五年まで',
    intro='共有物の管理、費用の負担、持分の放棄、分割について問う問題です（民法252条・253条・255条・256条・258条）。この問題は、誤っている記述を選ぶ形式です。\n\nこの記事では、過半数で決められること、持分の放棄の行き先、分割をしない契約の期間を、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('3年以内の建物の賃借権は、持分の価格の過半数で設定できる',
               '共有物の管理に関する事項は、各共有者の持分の価格に従い、その過半数で決めます（民法252条1項）。建物の賃借権は、期間が3年を超えないものであれば、この方法で設定できます（同条4項3号）。\n\n本肢は正しいといえます。\n\n**たとえば**、3人が3分の1ずつ共有する建物を、2人の賛成（持分の価格で3分の2）で、3年間の約束で人に貸すことができます。3年を超える期間にする場合は、この方法では設定できません。'),
        'イ': ('持分を放棄すると、その持分は他の共有者のものになる',
               '共有者の一人が持分を放棄したとき、又は死亡して相続人がいないときは、その持分は、他の共有者に帰属します（民法255条）。\n\n問題文は、Cの持分が国庫に帰属するとしているので、本肢は誤りです。持分を放棄したCの持分は、AとBに帰属します。\n\n**たとえば**、3人で共有する土地で、Cさんが「もう要らない」と持分を放棄したとします。Cさんの持分は国のものにはならず、残るAさんとBさんのものになります。'),
        'ウ': ('費用を1年払わない共有者の持分は、償金を支払って取得できる',
               '各共有者は、持分に応じて、管理の費用を支払い、そのほか共有物に関する負担を負います（民法253条1項）。\n\n共有者が1年以内にこの義務を履行しないときは、他の共有者は、相当の償金を支払って、その人の持分を取得することができます（同条2項）。本肢は正しいといえます。\n\n**たとえば**、3人共有の土地の草刈りの費用のうち、Cさんが自分の分を1年間払わないままだったとします。Aさんは、相当の償金をCさんに支払って、Cさんの持分を取得することができます。'),
        'エ': ('協議ができないときも、裁判所に分割を請求できる',
               '共有物の分割について、共有者の間で協議が調わないとき、又は協議をすることができないときは、その分割を裁判所に請求できます（民法258条1項）。\n\n裁判所は、共有者に債務を負担させて、他の共有者の持分の全部又は一部を取得させる方法による分割も、命じることができます（同条2項2号）。本肢は正しいといえます。\n\n**たとえば**、共有者の一人の行方が分からず、話し合いができない場合でも、Aさんは分割を裁判所に請求できます。裁判所は、Aさんにお金を支払う債務を負担させて、BさんとCさんの持分を全部Aさんに取得させる、という分け方を命じることもできます。'),
        'オ': ('分割をしない契約は、5年を超えない期間に限る',
               '各共有者は、いつでも共有物の分割を請求できます。ただし、5年を超えない期間内は分割をしない旨の契約をすることができます（民法256条1項）。\n\nこの契約は更新できますが、その期間も、更新の時から5年を超えることはできません（同条2項）。問題文は、10年間分割をしない旨の契約をすることができるとしているので、本肢は誤りです。\n\n**たとえば**、兄弟3人で相続した土地を、「当分の間は分けずに持っておこう」と約束するとき、決められる期間は5年までです。5年を超える期間を定めることはできません。'),
    },
    summary=[
        ('ア', '正', '期間が3年を超えない建物の賃借権は、持分の価格の過半数で設定できる'),
        ('イ', '誤', '持分を放棄したときは、その持分は国庫ではなく、他の共有者に帰属する'),
        ('ウ', '正', '1年以内に管理の費用を払わない共有者の持分は、他の共有者が償金を支払って取得できる'),
        ('エ', '正', '協議ができないときも裁判所に分割を請求でき、債務を負担させて持分を取得させる方法も命じられる'),
        ('オ', '誤', '分割をしない旨の契約は、5年を超えない期間内に限られる'),
    ],
    summary_tail='イは「持分の帰属先」、オは「契約の期間」をすり替えた出題です。放棄した持分は他の共有者へ、分割をしない契約は5年まで、と覚えましょう。',
    supplements=[
        '### 補足説明（イ）：持分が他の共有者に移る2つの場面\n\n共有者の持分が他の共有者に移る場面には、手続の違うものがあります。\n\n- 持分の放棄（255条）：放棄すると、その持分は他の共有者に帰属します。\n- 費用の不払い（253条2項）：1年以内に払わないとき、他の共有者が相当の償金を支払って取得できます。\n\n**たとえば**、Cさんが自分から「持分は要らない」と放棄すれば、Cさんの持分はAさんとBさんのものになります。一方、Cさんが費用を払わないままの場合は、AさんがCさんに償金を支払って、Cさんの持分を取得します。',
        '### 補足説明（オ）：分割をしない契約の期間\n\n分割はいつでも請求できるのが原則ですが、分割をしない契約には、期間の上限があります（256条）。\n\n- 分割をしない旨の契約：5年を超えない期間内。\n- 契約の更新：できるが、更新の時から5年を超えられない。\n\n**たとえば**、令和8年4月に5年の契約をして、満了した令和13年4月に更新する場合、更新後に定められるのは、更新の時から5年までです。5年を超える長い契約を、一度に定めることはできません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第96日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、民法252条1項・4項、253条、255条、256条、258条は、`note-articles/laws/` 配下の原文で確認しました。',
        '具体例の人物と場面（兄弟3人の相続した土地、草刈りの費用など）は、理解のために設けた架空の例です。条文にない事実は断定していません。',
        'オの更新の例（令和8年4月に5年の契約をし、令和13年4月に更新）は、256条2項の文言から導いた一般的な整理です。',
    ],
    phrases=['三年以内の賃貸は過半数で決められます', '放棄した持分は他の共有者のものです', '費用を一年払わないと持分を取得されます', '協議ができなくても裁判所に請求できます', '分割しない契約は五年が上限です'],
    header=dict(t1='共有者の決まり、', t2='どこまで？', topic='民法　共有物の管理と分割', kanji=''),
    poster_intro='共有物の決まりを、「管理・負担・放棄」（グループA：ア・イ・ウ）と「分割」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='共有物の管理と分割を整理', sub='民法 第252条・第253条・第255条・第256条・第258条（毎日ドリル 第96日）',
        col_a='管理と負担と放棄', col_b='分割', n_a=3,
        cards=[
            dict(h='三年以内の建物賃貸は過半数で決める',
                 ill='an isometric apartment building with a key tag labeled 「三年以内」. Three owner figures stand in front; two of them raise their hands. A green check mark sits beside the building.',
                 words=['三年以内'], tag='過半数で設定可'),
            dict(h='放棄した持分は他の共有者のもの',
                 ill='a land plot divided into three parts with three owner figures. One figure walks away leaving a stamp labeled 「放棄」 on his part; arrows move that part toward the two remaining figures. A green check mark sits beside the two remaining figures.',
                 words=['放棄'], tag='他の共有者に帰属'),
            dict(h='費用を一年払わない人の持分は取得できる',
                 ill='a calendar page labeled 「一年」 beside an empty wallet held by one figure. Another figure hands a money bag to him and receives a piece of the land plot. A green check mark sits beside the receiving figure.',
                 words=['一年'], tag='償金を支払って取得'),
            dict(h='協議ができなくても裁判所に請求できる',
                 ill='an isometric courthouse with a balance scale in front, and a land plot split into parts on the scale. A sign on the courthouse is labeled 「裁判所」. A green check mark sits beside the courthouse.',
                 words=['裁判所'], tag='分割の請求ができる'),
            dict(h='分割しない契約は五年まで',
                 ill='a horizontal calendar strip with a green bracket labeled 「五年」 over it, and two figures shaking hands above the bracket. A green check mark sits beside the bracket.',
                 words=['五年'], tag='更新後も五年まで'),
        ],
        kanji=[]),
    nb_label='イ・オ肢', nb_intro='イ・オの補足説明に合わせた2枚です。1枚目は、持分が他の共有者に移る2つの場面を左右の対比で示します。2枚目は、分割をしない契約の期間を時間の流れで示します。',
    notebooks=[
        dict(name='持分が他の共有者に移る2つの場面', args=dict(
            title='持分が他の共有者に移る場面', sub='放棄と費用の不払い（毎日ドリル 第96日 イ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「持分の放棄」 on the left and 「費用の不払い」 on the right. Draw them large and in different accent colors (blue on the left, orange on the right) so they can never be confused or duplicated. Do not use any check mark or cross mark in this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 持分の放棄
Scene: a figure leaving a piece of a land plot behind, with arrows moving the piece to the two remaining figures.
Label under the scene: 他の共有者に帰属する

RIGHT PANEL (orange accent):
Panel header: 費用の不払い
Scene: a calendar page with a bracket, an empty wallet held by one figure, and another figure handing a money bag and receiving a piece of the land plot.
Label under the scene: 一年以内に払わないとき、償金を支払って取得できる
Use exactly these strings, and no others, for the labels.""",
            callout='持分の放棄は、持分が他の共有者に帰属します。\n費用の不払いは、他の共有者が相当の償金を支払って、その人の持分を取得できます。',
            footer='民法253条2項・255条', kanji=[], what='panels',
            check='confirm the two panel headers are different strings (持分の放棄 on the left and 費用の不払い on the right) drawn in different accent colors, ')),
        dict(name='分割をしない契約の期間', args=dict(
            title='分割をしない契約の期間', sub='契約と更新（毎日ドリル 第96日 オ）',
            req='a timeline diagram',
            layout="""--- TIMELINE ---
Render as a clean flat-design horizontal timeline with a common axis running left to right and three flags. Use exactly these strings, and no others, for the labels. Do not use any check mark or cross mark.
Flag 1 (left): 契約をした日. Flag 2 (middle): 契約の満了. Flag 3 (right): 更新の期間の満了.
Above the axis, between flag 1 and flag 2, a blue bracket labeled 五年を超えない期間内.
Above the axis, between flag 2 and flag 3, a green bracket labeled 更新の時から五年を超えない期間内.
Two small figures shaking hands near flag 1.""",
            callout='分割をしない旨の契約は、五年を超えない期間内に限られます。\n更新もできますが、更新の時から五年を超えることはできません。',
            footer='民法256条', kanji=[], what='timeline',
            check='confirm there are exactly three flags and two brackets with the given strings, ')),
    ],
)

_p = D['poster']
_p['kanji'] = kj(_p['title'], _p['sub'], _p['col_a'], _p['col_b'], *[c['h'] + c['tag'] + ''.join(c['words']) for c in _p['cards']])
D['header']['kanji'] = '・'.join(kj(D['header']['t1'], D['header']['t2'], D['header']['topic']))
for _nb in D['notebooks']:
    _a = _nb['args']
    _a['kanji'] = kj(_a['title'], _a['sub'], _a['callout'], _a['footer'])
