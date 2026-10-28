def _kj(*texts, n=22):
    out = []
    for c in ''.join(texts):
        if '一' <= c <= '龥' and c not in out:
            out.append(c)
    return out[:n]


_P = dict(
    title='合筆の登記の制限を整理', sub='不動産登記法 第41条（毎日ドリル 第111日）',
    col_a='地役権と賃借権', col_b='名義人と担保権', n_a=3,
    cards=[
        dict(h='承役地の地役権は、要役地が別でも合筆できる',
             ill='two neighboring land plots each carrying a small gate icon, with a thin arrow from each plot to a different faraway plot behind it. A dotted line joins the two near plots into one. A green check mark sits beside the joined plots.',
             words=[], tag='承役地は例外'),
        dict(h='要役地どうしは、合筆の例外にならない',
             ill='two neighboring land plots each labeled 「要役地」, and a closed padlock sitting on the dotted line between them. A green check mark sits beside the padlock.',
             words=['要役地'], tag='登記があれば制限'),
        dict(h='登記のない賃借権は、合筆の妨げにならない',
             ill='two neighboring land plots, one with a tenant figure holding a lease paper, and an empty record sheet beside it. A dotted line joins the two plots into one. A green check mark sits beside the empty record sheet.',
             words=[], tag='登記がなければ制限なし'),
        dict(h='名義人が違うなら、合筆できない',
             ill='two neighboring land plots, each with a name tag labeled 「名義人」 in a different color, and a closed padlock on the dotted line between them. A green check mark sits beside the padlock.',
             words=['名義人'], tag='先に相続の登記を'),
        dict(h='担保権は、全部同じなら合筆できる',
             ill='two neighboring land plots each carrying an identical stamp labeled 「抵当権」 with a matching receipt slip beside it. A dotted line joins the two plots into one. A green check mark sits beside the stamps.',
             words=['抵当権'], tag='受付も原因も同じ'),
    ],
)
_P['kanji'] = _kj(_P['title'], _P['sub'], _P['col_a'], _P['col_b'], *[c['h'] + ''.join(c['words']) + c['tag'] for c in _P['cards']])

_N1 = dict(
    title='権利の登記と、合筆できるか', sub='規則105条の例外（毎日ドリル 第111日 ア・イ・ウ・オ）',
    req='a comparison table',
    layout="""IMPORTANT: this is a four-row table with two columns. The two column headers 「権利」 and 「合筆の扱い」 are different strings. Draw the 「権利」 column in blue and the 「合筆の扱い」 column in green so that they cannot be confused. This image uses no check marks and no cross marks.

--- TABLE ---
Row 1: 承役地の地役権 | 要役地が違っても合筆できる
Row 2: 要役地の側 | 例外にならない
Row 3: 担保権 | 目的と受付と原因が全部同じなら合筆できる
Row 4: 登記のない賃借権 | 合筆の妨げにならない
Use exactly these strings, and no others.""",
    callout='所有権の登記以外の権利の登記がある土地は、原則として合筆できません。例外は、承役地の地役権と、内容が全部同じ担保権などです。\n登記がされていない賃借権は、登記記録に現れないので、合筆の妨げになりません。',
    footer='不動産登記法41条6号、不動産登記規則105条',
    what='table',
    check='confirm the table has exactly four rows and two columns with the exact strings, ')
_N2 = dict(
    title='相続の登記を先に済ませる', sub='名義人が違う土地の合筆（毎日ドリル 第111日 エ）',
    req='a flow diagram',
    layout="""--- FLOW ---
Render as a clean flat-design flow with four steps in a row from left to right, joined by thin arrows.
Step 1 (blue accent): two neighboring plots with name tags in two different colors, with the label: 名義人が違う
Step 2 (orange accent): a family figure holding a form beside a house model, with the label: 相続の登記を申請
Step 3 (green accent): the two plots with name tags in the same color, with the label: 名義人がそろう
Step 4 (green accent): the two plots joined into one, with the label: 合筆の登記ができる
Use exactly these strings, and no others. This image uses no check marks and no cross marks.""",
    callout='相続があっても、相続による所有権の移転の登記をしなければ、登記記録の名義人は変わりません。\n名義人が違うままでは合筆できないので、先に相続の登記をして名義人をそろえます。',
    footer='不動産登記法41条3号',
    what='flow',
    check='confirm there are exactly four steps in a row with the exact strings and no check marks or cross marks, ')
for _n in (_N1, _N2):
    _n['kanji'] = _kj(_n['title'], _n['sub'], _n['layout'].split('--- ')[-1], _n['callout'], _n['footer'])

D = dict(
    catch='合筆できるかは、登記記録で決まる',
    intro='合筆の登記ができるかどうかを問う問題です（不動産登記法41条、不動産登記規則105条）。条文は、合筆できない場合を並べています。ここでは、地役権、賃借権、名義人、担保権の登記がある場合が出題されています。\n\nこの記事では、「登記記録の上で何が記録されているか」で結論が決まることを、具体的な場面で確認していきましょう。この問題は、正しい肢の組合せを選ぶ形です。',
    sections={
        'ア': ('承役地の地役権は、要役地が別でも合筆できる',
               '所有権の登記以外の権利に関する登記がある土地は、原則として合筆できません（不動産登記法41条6号）。ただし、承役地についてする地役権の登記は、例外として、合筆後の土地の登記記録に登記できるものとされています（不動産登記規則105条1号）。\n\n甲土地も乙土地も承役地で、要役地が別々でも、この例外に当たります。本肢は正しいといえます。\n\n**たとえば**、甲土地は丙土地のために通行を認める承役地、乙土地は丁土地のために通行を認める承役地だとします。要役地が違っていても、甲と乙を合筆できます。'),
        'イ': ('要役地の側には、合筆の例外がない',
               '規則105条1号の例外は、「承役地についてする」地役権の登記だけです。要役地の側には、この例外は及びません。\n\n問題文は、甲土地と乙土地がどちらも要役地で、丙土地を承役地とする地役権の登記の内容が同じだから合筆できるとしています。要役地には例外がないので、本肢は誤りです。\n\nなお、登記の目的、受付の年月日と番号、原因とその日付が同じであることが要件になるのは、担保権の登記です（同条2号）。\n\n**たとえば**、甲と乙がどちらも、丙土地を通るための権利を持つ要役地だとしても、それだけでは合筆できません。'),
        'ウ': ('登記されていない賃借権は、合筆の妨げにならない',
               '合筆が制限されるのは、所有権の登記以外の権利に関する「登記がある」土地です（不動産登記法41条6号）。\n\n建物所有を目的とする賃借権が設定されていても、その賃借権の登記がされていないなら、登記記録には現れません。合筆の妨げにならないので、本肢は正しいといえます。\n\n**たとえば**、乙土地をBが借りて家を建てていても、賃借権の登記がされていなければ、所有者Aは甲土地と乙土地を合筆できます。'),
        'エ': ('相続の登記が済んでいなければ、名義人は違うままで、合筆できない',
               '所有権の登記名義人が相互に異なる土地は、合筆できません（不動産登記法41条3号）。名義人が同じかどうかは、登記記録の上の名義人で判断します。\n\n乙土地の名義人が亡くなった父Bのままなら、子Aがすでに相続していても、登記記録の上では甲土地（A）と乙土地（B）で名義人が違います。相続を証する情報を提供するだけでは足りず、本肢は誤りです。\n\n**たとえば**、Aは、先に乙土地について相続による所有権の移転の登記をして、名義人をAにそろえます。そのうえで合筆の登記を申請します。'),
        'オ': ('担保権は、受付も原因も全部同じでなければ、例外にならない',
               '担保権の登記が合筆の例外になるのは、登記の目的、申請の受付の年月日及び受付番号、登記原因及びその日付が、すべて同じ場合です（不動産登記規則105条2号）。\n\n問題文は、同じ債権を担保していても、受付の年月日と受付番号が異なるとしています。目的と原因が同じでも、受付が違えば例外になりません。本肢は誤りです。\n\n**たとえば**、甲土地と乙土地に、同じ債権を担保する抵当権がそれぞれあっても、受付の日や番号が違えば、そのままでは合筆できません。'),
    },
    summary=[
        ('ア', '正', '承役地についてする地役権の登記は例外で、要役地が別々でも合筆できる'),
        ('イ', '誤', '例外は承役地の地役権だけで、要役地の側には及ばない。目的や受付が同じことが要件なのは担保権'),
        ('ウ', '正', '登記がされていない賃借権は、登記記録に現れないので、合筆の妨げにならない'),
        ('エ', '誤', '相続の登記をして名義人をそろえなければ合筆できず、相続を証する情報の提供では足りない'),
        ('オ', '誤', '担保権の登記は、目的と受付と原因がすべて同じでなければ、合筆の例外にならない'),
    ],
    summary_tail='イは「承役地」と「要役地」、オは「全部同じ」という条件を外した出題です。合筆の制限は、登記記録に何が記録されているかで考えましょう。',
    supplements=[
        '### 補足説明（イ・オ）：合筆の制限の例外は、権利によって要件が違う\n\n所有権の登記以外の権利の登記がある土地は、原則として合筆できません。例外は次のとおりです（規則105条）。\n\n- 承役地の地役権：要役地が違っても合筆できる（1号）。\n- 担保権：目的、受付の年月日と番号、原因とその日付が全部同じ（2号）。\n- 要役地の側：例外にならない。\n- 登記のない賃借権：制限の対象外（法41条6号は「登記がある」土地）。\n\n**たとえば**、同じ抵当権でも、受付の日が違えば例外になりません。一方、承役地の地役権は、要役地が違っても、そのまま合筆できます。',
        '### 補足説明（エ）：名義人は、登記記録の上でそろえる\n\n合筆できるかどうかを決める名義人は、登記記録の上の名義人です。\n\n- 乙土地の名義人が亡くなった父のまま：甲土地の名義人（子）と違う。合筆できない。\n- 相続による所有権の移転の登記をして、名義人が子になった：名義人がそろう。合筆できる。\n\n**たとえば**、遺産分割で乙土地を子が相続すると決まっていても、登記記録の名義人が父のままなら、合筆の登記は申請できません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第111日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法41条、不動産登記規則105条は、`note-articles/laws/` 配下の原文で確認しました。',
        'イの「要役地の側には例外が及ばない」、ウの「登記のない賃借権は登記記録に現れない」、エの「相続を証する情報の提供では足りない」という結論は、条文の文言からの一般的な整理です。登記先例の原文は手元になく、未確認です。',
        '各肢の具体例（通行のための地役権、家を建てる賃借権など）は、条文の適用場面をイメージするための例で、個別の事案の確認はしていません。',
    ],
    phrases=['承役地の地役権は合筆の例外です', '要役地の側には例外がありません', '登記のない賃借権は妨げになりません', '名義人が違うなら合筆できません', '担保権は全部同じなら合筆できます'],
    header=dict(t1='合筆できるのは、', t2='どんなとき？', topic='不動産登記法　合筆の制限',
                kanji='・'.join(_kj('合筆できるのはどんなとき', '不動産登記法合筆の制限', '毎', n=8))),
    poster_intro='合筆の登記の制限を、「地役権と賃借権」（グループA：ア・イ・ウ）と「名義人と担保権」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=_P,
    nb_label='イ・エ・オ肢', nb_intro='イ・エ・オの補足説明に合わせた2枚です。1枚目は、権利の登記と合筆できるかどうかを表で整理します。2枚目は、名義人が違う土地を合筆するまでの手順を示します。',
    notebooks=[
        dict(name='権利の登記と、合筆できるか', args=_N1),
        dict(name='相続の登記を先に済ませる', args=_N2),
    ],
)
