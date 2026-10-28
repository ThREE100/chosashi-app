def kj(*ss, n=14):
    out = []
    for s in ss:
        for c in s:
            if '一' <= c <= '龥' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='変更は全員、管理は過半数、保存は単独',
    intro='共有の土地について、使う・変える・管理するときに、だれの同意が必要かを問う問題です（民法249条・251条・252条）。Aの持分は2分の1、Bは4分の1、Cは4分の1という設定で、持分の価格の計算もからみます。\n\nこの記事では、共有物の行為を「変更」「管理」「保存」に分け、それぞれ全員の同意・過半数・単独のどれで足りるのかを、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('持分を超えて使うと、他の共有者に対価を償還する',
               '共有物を使用する共有者は、別段の合意がある場合を除き、他の共有者に対し、自己の持分を超える使用の対価を償還する義務を負います（民法249条2項）。\n\n本肢は正しいといえます。\n\n**たとえば**、3人で共有する土地の全部を、Aが一人で自分の駐車場として使っているとします。他の共有者との間に別段の合意がなければ、Aは持分を超えて使った分の対価を、BとCに償還しなければなりません。'),
        'イ': ('著しい変更は、持分の多少ではなく、全員の同意が必要',
               '各共有者は、他の共有者の同意を得なければ、共有物に変更（形状又は効用の著しい変更を伴わないものを除く）を加えることができません（民法251条1項）。\n\n問題文は、AとBの持分を合わせると4分の3だからCの同意がなくてもよい、としています。本肢は誤りです。\n\n**たとえば**、山林や畑を大きく造成して、土地の形や使い道が大きく変わる工事をするときは、持分が多くても、共有者全員の同意が必要です。Cが反対していれば、Aは造成工事をすることができません。'),
        'ウ': ('持分の価格が2分の1では、過半数にならない',
               '共有物の管理に関する事項は、各共有者の持分の価格に従い、その過半数で決します（民法252条1項）。過半数とは、半分を超えることです。\n\nAの持分は2分の1で、半分ちょうどなので、過半数ではありません。Aの賛成だけで決めることはできないため、本肢は誤りです。\n\n**たとえば**、Aが賛成し、BとCが反対した場合、賛成した持分は2分の1、反対した持分も2分の1です。同数で、過半数に届かないので、使い方は決まりません。'),
        'エ': ('保存行為は、各共有者が単独でできる',
               '各共有者は、管理に関する事項を決める方法にかかわらず、保存行為をすることができます（民法252条5項）。\n\n本肢は正しいといえます。\n\n**たとえば**、共有の土地の境にある塀が倒れそうになっているときに、Cが一人で修理をすることは、A、B、Cの意見がまとまっていなくてもできます。壊れそうな物を守るための行為だからです。'),
        'オ': ('土地の賃借権は、5年以内なら過半数で設定できる',
               '共有者は、管理に関する事項として、共有物に賃借権を設定することができます。建物の所有を目的としない土地の賃借権は、5年を超えない期間であれば、持分の価格の過半数で設定できます（民法252条1項・4項2号）。\n\n本肢は、AとBで持分の4分の3を持ち、期間は4年なので、正しいといえます。\n\n**たとえば**、更地を月極駐車場として貸すために、期間4年の賃借権を設定するとします。5年を超えていないので、AとBの賛成で足ります。'),
    },
    summary=[
        ('ア', '正', '持分を超えて共有物を使った共有者は、他の共有者に対し、別段の合意がなければ、使用の対価を償還する'),
        ('イ', '誤', '形状又は効用の著しい変更は、持分の価格の合計ではなく、他の共有者全員の同意が必要'),
        ('ウ', '誤', '管理に関する事項は持分の価格の過半数で決め、2分の1は過半数に当たらない'),
        ('エ', '正', '保存行為は、各共有者が単独でできる'),
        ('オ', '正', '土地の賃借権は、5年を超えない期間であれば、持分の価格の過半数で設定できる'),
    ],
    summary_tail='イは「変更」を「管理」の扱いにした出題、ウは「半分ちょうど」を過半数と数えた出題です。変更は全員、管理は過半数（半分を超えること）、保存は単独、と三段階で整理しましょう。',
    supplements=[
        '### 補足説明（イ・ウ）：共有物の行為は、三段階で整理する\n\n共有物にする行為は、だれの同意が必要かで、次の三つに分かれます。\n\n| 行為 | 必要な同意 | 条文 |\n|---|---|---|\n| 変更（形状又は効用の著しい変更） | 他の共有者全員の同意 | 251条1項 |\n| 管理 | 持分の価格の過半数 | 252条1項 |\n| 保存 | 各共有者が単独で | 252条5項 |\n\n**たとえば**、土地を大きく造成するのは「変更」、駐車場として貸すのは「管理」、倒れそうな塀を直すのは「保存」です。同じ共有の土地でも、行為の重さによって必要な同意が変わります。',
        '### 補足説明（ウ）：「過半数」は、持分の価格で数える\n\nAは2分の1、Bは4分の1、Cは4分の1の共有で、賛成した人の持分を足して、半分を超えるかどうかを見ます。\n\n| 賛成した人 | 持分の合計 | 過半数か |\n|---|---|---|\n| Aだけ | 2分の1 | 超えない |\n| AとB | 4分の3 | 超える |\n| AとC | 4分の3 | 超える |\n| BとC | 2分の1 | 超えない |\n\n**たとえば**、人数ではAが1人、BとCが2人ですが、数えるのは持分の価格です。BとCが組んでも2分の1にとどまり、過半数にはなりません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第8日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、民法249条2項、251条1項、252条1項・4項2号・5項は、`note-articles/laws/` 配下の原文で確認しました。',
        'ウの「過半数とは半分を超えること」は、252条1項の「持分の価格に従い、その過半数で決する」からの一般的な整理です。',
        'エの具体例（倒れそうな塀の修理）、オの具体例（月極駐車場）は、条文の文言をかみ砕いた一般的な例で、個別の判断は確認していません。',
    ],
    phrases=['持分を超えて使えば対価を払います', '著しい変更は全員の同意が必要です', '半分ちょうどは過半数ではありません', '保存行為は一人でできるんです', '5年以内の賃借権は過半数で足ります'],
    header=dict(t1='共有の土地、', t2='だれの同意が必要？', topic='民法　共有物の使用と管理',
                kanji='共・有・同・意・民・法'),
    poster_intro='共有の土地の行為を、「使用と変更」（グループA：ア・イ）と「管理と保存」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='共有の土地の行為を整理', sub='民法 第249条・第251条・第252条（毎日ドリル 第8日）',
        col_a='使用と変更', col_b='管理と保存', n_a=2,
        cards=[
            dict(h='持分を超えて使うと対価を償還',
                 ill='an isometric land plot used as a parking lot by one figure, with coins flowing from that figure toward two other figures standing beside the plot. A green check mark sits beside the coins.',
                 words=[], tag='別段の合意がなければ'),
            dict(h='著しい変更は全員の同意が必要',
                 ill='an isometric scene of a land plot being graded by a small excavator. Three figures stand beside it, and all three raise a hand with a green check mark above each hand. A label above the group reads 「全員」.',
                 words=['全員'], tag='持分の多少は関係ない'),
            dict(h='管理は持分の価格の過半数で決める',
                 ill='a balance scale. On the left pan, two figures stand together with a block reading 「過半数」. On the right pan, a single figure with a smaller block. The left pan is lower. A green check mark sits beside the scale.',
                 words=['過半数'], tag='半分を超える'),
            dict(h='保存行為は各共有者が単独でできる',
                 ill='a fallen-over wall being repaired by one figure alone with a hammer, while two other figures stand far away. A label above the repair scene reads 「単独」. A green check mark sits beside the repaired wall.',
                 words=['単独'], tag='一人でもできる'),
            dict(h='土地の賃借権は5年以内なら過半数',
                 ill='an isometric empty land plot used as a monthly parking lot, with a lease document and a calendar page. The calendar page is labeled 「5年以内」. Two figures with a larger block stand beside the plot. A green check mark sits beside the calendar.',
                 words=['5年以内'], tag='過半数で足りる'),
        ],
        kanji=kj('共有持分償還全員過半数単独年以内賃借権変更管理保存同意')),
    nb_label='イ・ウ肢', nb_intro='イ・ウの補足説明に合わせた2枚です。1枚目は、共有物の行為を三段階で整理します。2枚目は、持分の価格で過半数を数える方法を示します。',
    notebooks=[
        dict(name='共有物の行為は三段階', args=dict(
            title='変更・管理・保存は、何が必要？', sub='民法251条・252条（毎日ドリル 第8日 イ・ウ）',
            req='a three-row table-like diagram',
            layout="""IMPORTANT: the three row headers are different strings: 「変更」, 「管理」 and 「保存」. Draw them large in three different accent colors (orange, blue, green) so they can never be confused or duplicated. Do not draw any cross mark or check mark in this image.

--- THREE ROWS ---
Three horizontal rounded rows stacked vertically, each with a left header, an icon and a right result box.

ROW 1 (orange accent): header 変更
Icon: a land plot being graded by a small excavator.
Result box: 他の共有者全員の同意

ROW 2 (blue accent): header 管理
Icon: a land plot used as a parking lot.
Result box: 持分の価格の過半数

ROW 3 (green accent): header 保存
Icon: a fallen-over wall being repaired.
Result box: 各共有者が単独で""",
            callout='共有物の形状や効用を著しく変える変更は、他の共有者全員の同意が必要です。\n管理に関する事項は持分の価格の過半数、保存行為は各共有者が単独でできます。',
            footer='民法251条1項、252条1項・5項',
            kanji=kj('変更管理保存共有者全員同意持分価格過半数単独'), what='table',
            check='confirm the three row headers are three different strings drawn in three different colors, and that no check mark or cross mark appears anywhere, ')),
        dict(name='過半数は持分の価格で数える', args=dict(
            title='過半数は、持分の価格で数える', sub='共有者の持分と賛成の組合せ（毎日ドリル 第8日 ウ）',
            req='a table-like diagram',
            layout="""--- SHARE BAR ---
At the top, one wide horizontal bar split into three segments: 
A (half of the bar, blue), labeled A 2分の1; B (a quarter, green), labeled B 4分の1; C (a quarter, orange), labeled C 4分の1.
A vertical dotted line marks the center of the bar, labeled 半分.

--- FOUR COMBINATIONS ---
Below the bar, four rows, each showing which segments are highlighted and the result text:
Row 1: highlight only A. Result text: 2分の1 半分ちょうど
Row 2: highlight A and B. Result text: 4分の3 半分を超える
Row 3: highlight A and C. Result text: 4分の3 半分を超える
Row 4: highlight B and C. Result text: 2分の1 半分ちょうど

Use a green outline around the rows whose result is 半分を超える.""",
            callout='過半数とは、半分を超えることです。\n持分の価格が2分の1のAだけでは、半分ちょうどで過半数にならず、Aと、BまたはCのどちらかが賛成すれば過半数になります。',
            footer='民法252条1項',
            kanji=kj('過半数持分価格賛成半分超'), what='table',
            check='confirm the top bar has three segments with the labels given, and that exactly two rows have a green outline, ')),
    ],
)
