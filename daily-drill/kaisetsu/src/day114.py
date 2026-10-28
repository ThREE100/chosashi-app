def _kj(*texts, n=22):
    out = []
    for c in ''.join(texts):
        if '一' <= c <= '龥' and c not in out:
            out.append(c)
    return out[:n]


_P = dict(
    title='筆界特定の手続を整理', sub='不動産登記法 第136条・第146条・第148条（毎日ドリル 第114日）',
    col_a='測量と費用の負担', col_b='期日の場所と判決', n_a=3,
    cards=[
        dict(h='立会いの機会を与えれば、測量できる',
             ill='a surveyor figure with a tripod on a land plot, and a notice letter flying toward two neighbor figures. One neighbor figure stands present, and the other is drawn as a faded empty outline. A green check mark sits beside the tripod.',
             words=[], tag='来なくても測量できる'),
        dict(h='同じ側の申請人は、持分の割合で負担',
             ill='a land plot labeled 「甲土地」 with two owner figures of different sizes, and a round pie chart split into a large part and a small part matching the owners. A green check mark sits beside the pie chart.',
             words=['甲土地'], tag='持分の割合で分ける'),
        dict(h='両側の申請人は、半分ずつから分ける',
             ill='two neighboring land plots labeled 「甲土地」 and 「乙土地」, a round pie chart split into two equal halves, and the half on the 「甲土地」 side divided again into two parts. One owner stands at the 「乙土地」 half and two owners stand at the 「甲土地」 half. A green check mark sits beside the pie chart.',
             words=['甲土地', '乙土地'], tag='半分は持分で分ける'),
        dict(h='意見聴取の期日は、現地でも開ける',
             ill='a registry officer figure holding a folder and standing on a land plot beside a boundary stake, with a registry building drawn small and faded in the background. A green check mark sits beside the officer.',
             words=[], tag='適当と認める場所'),
        dict(h='判決と食い違う範囲だけ、効力を失う',
             ill='a boundary line between two plots drawn in three segments. The middle segment is highlighted in orange and the two outer segments stay blue. A gavel icon sits above the middle segment. A green check mark sits beside the outer segments.',
             words=[], tag='抵触する範囲だけ'),
    ],
)
_P['kanji'] = _kj(_P['title'], _P['sub'], _P['col_a'], _P['col_b'], *[c['h'] + ''.join(c['words']) + c['tag'] for c in _P['cards']])

_N1 = dict(
    title='筆界特定の費用は、どう分ける？', sub='手続費用の負担（毎日ドリル 第114日 イ・ウ）',
    req='a comparison table',
    layout="""IMPORTANT: this is a three-row table with two columns. The two column headers 「申請人の組合せ」 and 「負担の割合」 are different strings. Draw the 「申請人の組合せ」 column in blue and the 「負担の割合」 column in green so that they cannot be confused. This image uses no check marks and no cross marks.

--- TABLE ---
Row 1: 甲土地側に一人、乙土地側に一人 | 等しい割合
Row 2: 甲土地側の共有者二人だけ | 持分の割合
Row 3: 乙土地側に一人、甲土地側に二人 | 乙土地側が半分、甲土地側は残りの半分を持分で分ける
Use exactly these strings, and no others.""",
    callout='申請人の全員が対象土地の一方の側にいるときは、持分の割合で負担します。等しい割合になるのは、両側に一人ずつのときです。\n三人以上で、両側にいるときは、まず半分ずつに分け、二人以上の側は、その半分を持分で分けます。',
    footer='不動産登記法146条2項から4項',
    what='table',
    check='confirm the table has exactly three rows and two columns with the exact strings, ')
_N2 = dict(
    title='判決と食い違う区間だけ、効力を失う', sub='筆界確定訴訟の判決との関係（毎日ドリル 第114日 オ）',
    req='a diagram',
    layout="""IMPORTANT: this image uses opposite marks. A green check mark sits at the segments that keep their effect and a red cross sits at the segment that loses its effect. The two segment labels 「効力は残る」 and 「効力を失う」 are different strings; draw them in different colors (blue and orange).

--- DIAGRAM ---
A horizontal boundary line between two neighboring plots, drawn in three consecutive segments from left to right.
Left segment (blue): a label below it: 判決と同じ区間, and a result label with a green check mark: 効力は残る
Middle segment (orange): a label below it: 判決と違う区間, and a result label with a red cross: 効力を失う
Right segment (blue): a label below it: 判決と同じ区間, and a result label with a green check mark: 効力は残る
Above the line, a small gavel icon with no text.
Use exactly these strings, and no others.""",
    callout='筆界特定は、筆界確定訴訟の判決と抵触する範囲だけで、効力を失います。\n判決と同じ区間の筆界特定は、そのまま効力が残ります。全部が失効するわけではありません。',
    footer='不動産登記法148条',
    what='diagram',
    check='confirm the three segments carry the exact labels, that the two outer segments carry green check marks and the middle segment carries a red cross, ')
for _n in (_N1, _N2):
    _n['kanji'] = _kj(_n['title'], _n['sub'], _n['layout'].split('--- ')[-1], _n['callout'], _n['footer'])

D = dict(
    catch='立会いは機会を与えれば足りる',
    intro='筆界特定の手続について、誤っているものを選ぶ問題です（不動産登記法136条・146条・148条、不動産登記規則222条）。測量の立会い、手続費用の負担、意見聴取等の期日の場所、筆界確定訴訟の判決との関係が出題されています。\n\nこの記事では、条文の細かい数字や範囲を、具体的な場面で確認していきましょう。この問題は、誤っている肢の組合せを選ぶ形です。',
    sections={
        'ア': ('立会いの機会を与えれば、立ち会わなくても測量できる',
               '筆界調査委員は、対象土地の測量や実地調査をするときは、あらかじめ日時と場所を申請人や関係人に通知して、立ち会う機会を与えなければなりません（不動産登記法136条1項）。求められているのは、立ち会う機会を与えることです。\n\n機会を与えたのに関係人が来なかったとしても、測量はできます。本肢は正しいといえます。\n\n**たとえば**、筆界調査委員が測量の日時と場所を通知したのに、関係人Bが当日来なかったとします。この場合でも、測量を行うことができます。'),
        'イ': ('同じ側の申請人だけなら、持分の割合で負担する',
               '申請人が二人以上いて、その全員が対象土地の一方の土地の所有権登記名義人等であるときは、各申請人は、持分の割合に応じて手続費用を負担します（不動産登記法146条3項）。\n\n問題文は、甲土地の共有者C（3分の2）とD（3分の1）だけが申請人なので、持分の割合で負担します。等しい割合とする本肢は、誤りです。\n\n**たとえば**、手続費用が6万円なら、Cが4万円、Dが2万円を負担します。等しい割合で負担するのは、申請人が二人で、甲土地側と乙土地側に一人ずつ分かれる場合です。'),
        'ウ': ('両側にいる三人なら、半分ずつから持分で分ける',
               '申請人が三人以上で、対象土地の両側にいるときは、一人の側の申請人は手続費用の2分の1を負担します。二人以上の側の各申請人は、2分の1について持分の割合で負担します（不動産登記法146条4項）。\n\nEは2分の1、甲土地側のCは2分の1の3分の2で3分の1、Dは2分の1の3分の1で6分の1です。本肢は正しいといえます。\n\n**たとえば**、手続費用が6万円なら、Eが3万円、Cが2万円、Dが1万円です。'),
        'エ': ('意見聴取等の期日は、現地でも開ける',
               '意見聴取等の期日は、法務局又は地方法務局、対象土地の所在地を管轄する登記所のほか、筆界特定登記官が適当と認める場所で開きます（不動産登記規則222条）。庁舎に限る決まりではありません。\n\n本肢は正しいといえます。\n\n**たとえば**、現地で境界の位置を確かめながら話を聞いたほうが分かりやすい事案では、登記官が適当と認める現地で期日を開くこともできます。'),
        'オ': ('判決と食い違う範囲だけ、効力を失う',
               '筆界特定がされた後、同じ筆界について筆界確定訴訟の判決が確定したときは、筆界特定は、その判決と抵触する範囲で効力を失います（不動産登記法148条）。\n\n問題文は、判決と筆界特定が一部の区間だけ異なる場合に、筆界特定の全部が失効するとしています。失効するのは抵触する範囲だけなので、本肢は誤りです。\n\n**たとえば**、筆界の線の三つの区間のうち、真ん中の区間だけが判決と食い違うとします。効力を失うのはその区間だけで、両側の区間の筆界特定は、そのまま効力が残ります。'),
    },
    summary=[
        ('ア', '正', '立ち会う機会を与えれば足り、関係人が立ち会わなくても、筆界調査委員は測量できる'),
        ('イ', '誤', '申請人の全員が同じ側の土地の登記名義人なら、等しい割合ではなく、持分の割合で費用を負担する'),
        ('ウ', '正', '両側にいる三人なら、一人の側が2分の1を負担し、二人の側は残りの2分の1を持分で分ける'),
        ('エ', '正', '意見聴取等の期日は、庁舎のほか、筆界特定登記官が適当と認める場所（現地を含む）で開ける'),
        ('オ', '誤', '判決と抵触する範囲だけで効力を失い、全部が失効するのではない'),
    ],
    summary_tail='イは「負担の割合」、オは「効力を失う範囲」をすり替えた出題です。費用の割合は申請人の組合せで、失効の範囲は抵触する部分で決まります。',
    supplements=[
        '### 補足説明（イ・ウ）：筆界特定の費用は、申請人の組合せで分け方が決まる\n\n手続費用の負担は、申請人がどの土地の側にいるかで決まります（不動産登記法146条）。\n\n- 申請人が二人で、両側に一人ずつ：等しい割合（2項）。\n- 申請人の全員が一方の側：持分の割合（3項）。\n- 三人以上で両側にいる：一人の側は2分の1、二人以上の側は2分の1を持分で分ける（4項）。\n\n**たとえば**、甲土地の共有者C（3分の2）とD（3分の1）と、乙土地のEが申請人なら、Eが2分の1、Cが3分の1、Dが6分の1です。C・Dだけが申請人なら、Cが3分の2、Dが3分の1です。',
        '### 補足説明（オ）：判決と食い違う部分だけが失効する\n\n筆界確定訴訟の判決が確定すると、判決と抵触する範囲だけで、筆界特定の効力が失われます（不動産登記法148条）。\n\n- 判決と食い違う区間：筆界特定は効力を失う。\n- 判決と同じ区間：筆界特定は、そのまま効力が残る。\n\n**たとえば**、筆界の一部の区間だけ、判決と筆界特定の位置がずれたとします。効力を失うのはずれた区間だけで、残りの区間の筆界特定は有効なままです。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第114日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法136条、146条、148条、不動産登記規則222条は、`note-articles/laws/` 配下の原文で確認しました。',
        'エの「現地も含まれる」という点は、規則222条の「適当と認める場所」の解釈に関する登記実務の取扱い（先例）で、先例の原文は手元になく、未確認です。本文では、条文の文言から庁舎に限らないことを説明しました。',
        'イ・ウの手続費用の金額（6万円）は、割合を分かりやすくするための仮の例で、実際の費用ではありません。エの具体例（現地で話を聞く場合）は、一般的な説明で、個別の運用の確認はしていません。',
    ],
    phrases=['立会いは機会を与えれば足ります', '同じ側の申請人は持分の割合で負担します', '両側の三人なら半分を持分で分けます', '期日は現地で開くこともできます', '失効するのは判決と食い違う範囲だけです'],
    header=dict(t1='筆界特定の費用は、', t2='どう分ける？', topic='不動産登記法　筆界特定の手続',
                kanji='・'.join(_kj('筆界特定の費用はどう分ける', '不動産登記法筆界特定の手続', '毎', n=8))),
    poster_intro='筆界特定の手続を、「測量と費用の負担」（グループA：ア・イ・ウ）と「期日の場所と判決」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=_P,
    nb_label='イ・ウ・オ肢', nb_intro='イ・ウ・オの補足説明に合わせた2枚です。1枚目は、筆界特定の手続費用の分け方を、申請人の組合せごとに表で整理します。2枚目は、判決と食い違う区間だけで筆界特定が効力を失うことを、図で示します。',
    notebooks=[
        dict(name='筆界特定の費用は、どう分ける？', args=_N1),
        dict(name='判決と食い違う区間だけ、効力を失う', args=_N2),
    ],
)
