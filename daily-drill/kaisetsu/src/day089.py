def _k(*t, n=24):
    out = []
    for c in ''.join(t):
        if '一' <= c <= '龥' and c not in out:
            out.append(c)
    return out[:n]


_T1, _T2, _TOP = '登記が要る相手、', '要らない相手は？', '民法　不動産の物権変動と登記'
_cards = [
    dict(h='知っていた買主も「第三者」',
         ill='an isometric land plot. Two buyer figures stand beside it. The first buyer holds a contract but no stamp. The second buyer holds a contract and a round stamp labeled 「登記」 and is highlighted with a green glow. A green check mark sits beside the second buyer.',
         words=['登記'], tag='登記のある方が勝つ'),
    dict(h='時効完成後の買主とは登記の先後',
         ill='an isometric horizontal timeline. On the left a flag labeled 「時効完成」. Further right, a buyer figure holding a stamp labeled 「登記」 is highlighted with a green glow. A green check mark sits beside the buyer.',
         words=['時効完成', '登記'], tag='完成後は登記の先後'),
    dict(h='相続人には登記なしで対抗できる',
         ill='an isometric scene: a buyer figure holds a contract with a green glow, and behind a seller silhouette a smaller figure labeled 「相続人」 stands inside the same outline as the seller. There is no stamp anywhere. A green check mark sits beside the buyer.',
         words=['相続人'], tag='相続人は第三者でない'),
    dict(h='時効完成前の買主にも登記なしで',
         ill='an isometric horizontal timeline. On the left a buyer figure holding a stamp labeled 「登記」 stands before a flag labeled 「時効完成」 on the right. A long-time occupant figure beside the flag is highlighted with a green glow and holds no stamp. A green check mark sits beside the occupant.',
         words=['登記', '時効完成'], tag='完成前は当事者並み'),
    dict(h='共有者の持分は登記が必要',
         ill='an isometric land plot divided into three equal parts labeled by figures, with one figure on the left handing a part to a new figure holding a stamp labeled 「登記」. The two remaining co-owner figures stand on the other parts. A green check mark sits beside the stamp.',
         words=['登記'], tag='他の共有者は第三者'),
]

D = dict(
    catch='登記が要る相手と、要らない相手',
    intro='不動産を買ったとき、登記がなければ、だれに対して所有権を主張できないのかを問う問題です（民法177条）。民法177条は、登記をしなければ「第三者」に対抗できない、と定めています。そのため、だれが「第三者」に当たるのかが問題になります。この問題は、判例の趣旨に照らして正しいものの組合せを選びます。\n\nこの記事では、「第三者」に当たる人と当たらない人を、具体的な場面で分けていきましょう。',
    sections={
        'ア': ('先の売買を知っていただけの買主にも、登記がなければ対抗できない',
               '不動産に関する物権の得喪及び変更は、登記をしなければ、第三者に対抗することができません（民法177条）。判例の趣旨では、先の売買を知っていただけの買主（単純悪意者）も、この「第三者」に含まれます。\n\n問題文は、Bが登記なしでCに対抗できるとしているので、本肢は誤りです。\n\n**たとえば**、AさんがBさんに土地を売ったが登記が済んでいない間に、AさんがCさんにも同じ土地を売りました。Cさんが、先にBさんへの売買があったことを知っていただけなら、先に登記を備えたほうが勝ちます。'),
        'イ': ('時効完成後に買った人が登記を備えたときは、登記がなければ対抗できない',
               '取得時効が完成した後に、元の所有者から土地を買って登記を備えた人との関係は、二重譲渡と同じように、登記の先後で決まります（判例の趣旨）。\n\n問題文は、Cが登記なしでBに対抗できるとしているので、本肢は誤りです。\n\n**たとえば**、Cさんが長年占有して時効が完成した後、元の所有者Aさんが、同じ土地をBさんに売って登記もしました。Cさんが時効取得の登記をしていないなら、Cさんは、Bさんに時効による所有権の取得を対抗できません。'),
        'ウ': ('相続人には、登記なしで対抗できる',
               '相続人は、相続開始の時から、被相続人の財産に属した一切の権利義務を承継します（民法896条）。そのため、相続人は被相続人と同じ立場に立ち、買主とは当事者の関係になります。判例の趣旨では、相続人は「第三者」に当たりません。\n\n本肢は正しいといえます。\n\n**たとえば**、Aさんが土地をBさんに売ったあと、登記前に亡くなり、子のCさんが相続したとします。Bさんは、登記がなくても、Cさんに土地の所有権を主張できます。'),
        'エ': ('時効完成前に買って登記を備えた人には、登記なしで対抗できる',
               '時効が完成する前に元の所有者から土地を買い、登記を備えた人は、時効が完成した時点での所有者です。時効取得者から見て、当事者に類似する関係に立つので、「第三者」には当たりません（判例の趣旨）。時効取得者は、登記がなくても対抗できます。\n\n問題文は「登記を備えなければ対抗できない」としているので、本肢は誤りです。\n\n**たとえば**、Cさんが占有を続けている途中で、Aさんが土地をBさんに売って登記をしました。その後にCさんの時効が完成したなら、Cさんは、登記がなくてもBさんに所有権を主張できます。'),
        'オ': ('共有者から持分を買った人は、登記がなければ他の共有者に対抗できない',
               '共有者の一人から持分を買った人にとって、他の共有者は、民法177条の「第三者」に当たります（判例の趣旨）。そのため、持分を買った人は、持分の移転の登記を備えなければ、他の共有者に持分の取得を対抗できません。\n\n本肢は正しいといえます。\n\n**たとえば**、A・D・Eの3人の共有地で、AさんがFさんに持分を売りました。Fさんが持分の移転の登記を済ませていなければ、Fさんは、DさんとEさんに対して、自分が共有者になったと主張できません。'),
    },
    summary=[
        ('ア', '誤', '二重譲渡の買主が先の売買を知っていただけでも、先の買主は登記がなければ対抗できない'),
        ('イ', '誤', '時効完成後に買って登記を備えた人とは、登記の先後で決まる（登記なしでは対抗できない）'),
        ('ウ', '正', '相続人は「第三者」に当たらないので、買主は登記なしで対抗できる'),
        ('エ', '誤', '時効完成前に買って登記を備えた人には、時効取得者は登記なしで対抗できる'),
        ('オ', '正', '共有者から持分を買った人は、登記がなければ他の共有者に対抗できない'),
    ],
    summary_tail='ア・イ・エは、登記が必要かどうかを入れ替えた出題です。迷ったら、相手が「第三者」に当たるかどうかに戻って考えましょう。相続人や、時効完成前の買主は「第三者」に当たりません。',
    supplements=[
        '### 補足説明（ア・ウ・オ）：「第三者」に当たる人と当たらない人\n\n民法177条の「第三者」に当たるかどうかで、登記が必要かどうかが決まります（以下は判例の趣旨による整理です）。\n\n| 登記が必要な相手（第三者に当たる） | 登記が不要な相手（第三者に当たらない） |\n|---|---|\n| 先の売買を知っていただけの二重譲渡の買主（ア） | 相続人（ウ） |\n| 時効完成後に買って登記を備えた人（イ） | 時効完成前に買って登記を備えた人（エ） |\n| 共有者の一人から持分を買った場合の、他の共有者（オ） | 買主を害する目的で買った人（背信的悪意者） |\n\n**たとえば**、同じ土地を二重に買った人でも、先の売買を知っていただけなら「第三者」ですが、先の買主に嫌がらせをする目的で買ったような人は、「第三者」から除かれます。',
        '### 補足説明（イ・エ）：時効の完成の前か後かで、結論が変わる\n\n時効取得者Cさんと、元の所有者から土地を買ったBさんの関係は、Bさんが買って登記した時が、時効の完成の前か後かで変わります。\n\n- 時効の完成前にBさんが登記：Bさんは時効完成時の所有者。Cさんは、登記なしでBさんに対抗できる（エ）。\n- 時効の完成後にBさんが登記：二重譲渡と同じ。登記の先後で決まり、Cさんは登記がないとBさんに対抗できない（イ）。\n\n**たとえば**、時効が完成した日を境に、「完成した日より前に買った人」と「完成した日より後に買った人」を分けて考えます。同じ「買って登記した人」でも、結論が逆になります。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第89日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '民法177条と896条は、`note-articles/laws/` 配下の原文で確認しました。',
        '「判例の趣旨」とした各結論（単純悪意者、時効完成前後の買主、相続人、共有者の第三者性）は、判例によるもので、条文からは直接読み取れません。判例の原文は未確認です。過去問の解説記事の結論と照らして確認しています。',
        '補足説明の「背信的悪意者」は、第三者から除かれる類型の例として挙げたものです。この記事では判例の詳細（要件など）は扱っていません。',
    ],
    phrases=['知っていた買主も第三者です', '時効完成後の買主とは登記の先後です', '相続人には登記なしで対抗できます', '時効完成前の買主には登記は不要です', '持分の買主は登記が必要です'],
    header=dict(t1=_T1, t2=_T2, topic=_TOP, kanji='・'.join(_k(_T1, _T2, _TOP))),
    poster_intro='不動産の物権変動と登記を、「二重に売られたとき」（グループA：ア・イ）と「相続・時効完成前・共有」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='登記が要る相手を整理', sub='民法 第177条・第896条（毎日ドリル 第89日）',
        col_a='二重に売られたとき', col_b='相続と時効完成前と共有', n_a=2,
        cards=_cards,
        kanji=_k(*[c['h'] + c['tag'] + ''.join(c['words']) for c in _cards], '登記が要る相手を整理二重に売られたとき相続と時効完成前と共有', n=24)),
    nb_label='ア・ウ・オ肢とイ・エ肢', nb_intro='補足説明に合わせた2枚です。1枚目は、「第三者」に当たる人と当たらない人を左右の対比で示します。2枚目は、時効の完成の前に買った人と後に買った人を、時間の流れで示します。',
    notebooks=[
        dict(name='「第三者」に当たる人と当たらない人', args=dict(
            title='登記が要る相手、要らない相手', sub='民法177条の「第三者」（毎日ドリル 第89日 ア・ウ・オ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two sides must show OPPOSITE marks, not the same mark. The left side shows a red cross; the right side shows a green check mark. The two panel headers are different strings: 「第三者に当たる人」 on the left and 「第三者に当たらない人」 on the right; draw them in different accent colors (blue and gray) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 第三者に当たる人
Items (a plain list with a small icon beside each):
先の売買を知っていただけの二重譲渡の買主
時効完成後に買って登記を備えた人
共有者の一人から持分を買った場合の、他の共有者
Result badge with a red cross: 登記がないと対抗できない

RIGHT PANEL (gray accent):
Panel header: 第三者に当たらない人
Items (a plain list with a small icon beside each):
相続人
時効完成前に買って登記を備えた人
Result badge with a green check mark: 登記がなくても対抗できる""",
            callout='相手が「第三者」に当たるときは、登記がなければ対抗できません。\n相続人や、時効完成前に買って登記を備えた人は、「第三者」に当たらないので、登記がなくても対抗できます。',
            footer='民法177条、896条',
            kanji='・'.join(_k('第三者当先売買知二重譲渡買主時効完成後登記備共有持分他相続人対抗民法')), what='panels',
            check='confirm the two panel headers are different strings (第三者に当たる人 on the left and 第三者に当たらない人 on the right) and that the left panel shows a red cross while the right panel shows a green check mark, ')),
        dict(name='時効完成の前か後か', args=dict(
            title='時効の完成の前か後か', sub='時効取得者と、買って登記した人（毎日ドリル 第89日 イ・エ）',
            req='a timeline diagram',
            layout="""--- TIMELINE ---
Render as a clean flat-design horizontal timeline in the upper half, with two lanes stacked vertically. A common timeline axis runs left to right with two flags: the left flag labeled 占有の開始 with an icon of a person standing on a plot, and the right flag labeled 時効の完成 with an icon of a calendar page.
Upper lane (green accent), lane label: 時効の完成前に買って登記. A small icon of a buyer holding a stamp is placed to the LEFT of the right flag. Result label at the end of the lane: 時効取得者は登記なしで対抗できる.
Lower lane (blue accent), lane label: 時効の完成後に買って登記. A small icon of a buyer holding a stamp is placed to the RIGHT of the right flag. Result label at the end of the lane: 時効取得者は登記がないと対抗できない.
Use exactly these strings, and no others, for the labels. The two lane labels are different strings; draw them in different accent colors (green and blue).""",
            callout='時効の完成の前に買って登記した人は、完成した時点での所有者で、時効取得者とは当事者に類似する関係です。\n完成の後に買って登記した人とは、二重譲渡と同じように、登記の先後で決まります。',
            footer='民法177条',
            kanji='・'.join(_k('時効完成前後買登記占有開始取得者対抗二重譲渡先後当事者類似関係民法')), what='timeline',
            check='confirm the two lane labels are different strings in different accent colors and that the buyer icon is left of the 時効の完成 flag in the upper lane and right of it in the lower lane, ')),
    ],
)
