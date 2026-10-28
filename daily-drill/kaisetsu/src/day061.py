D = dict(
    catch='完成の前か後かで、登記の要否が変わる',
    intro='不動産の取得時効を問う問題です（民法145条・162条・177条・187条）。取得時効とは、他人の土地を自分のものとして長く占有し続けた人が、その所有権を取得する制度です。この問題は、判例の趣旨に照らして**正しいもの**の組合せを選びます。\n\nこの記事では、時効の完成の前に現れた買主と後に現れた買主の違い、占有の足し算、時効の援用、土地の一部の時効取得を、具体的な場面で確かめていきましょう。',
    sections={
        'ア': ('完成前に現れた買主には、登記がなくても主張できる',
               '時効が完成する前に、元の所有者から土地を買って登記を受けた第三者に対しては、時効を取得した人は、登記がなくても、所有権の取得を主張することができます（判例）。\n\n本肢は正しいといえます。完成前の買主は、時効によって所有権を失う側の当事者と同じ立場にあるので、取得した人との間に、先に登記をした方が勝つという関係は生じません。\n\n**たとえば**、Aさんが20年の占有を続けている途中で、持ち主のBさんが土地をCさんに売り、登記もしたとします。その後に20年が経ったときは、AさんはCさんに対して、登記がなくても、時効による取得を主張できます。'),
        'イ': ('完成後に現れた買主とは、先に登記をした方が勝つ',
               '不動産に関する物権の得喪は、登記をしなければ、第三者に対抗することができません（民法177条）。時効が完成した後に、元の所有者から土地を買って登記を受けた第三者に対しては、時効を取得した人も、登記をしなければ対抗できません（判例）。\n\n問題文は、完成した後に買ったCに対して、登記なしで主張できるとしているので、本肢は誤りです。\n\n**たとえば**、Aさんの取得時効が完成した後に、持ち主のBさんが土地をCさんに売り、Cさんが先に登記をしてしまったら、Aさんは登記がないと、Cさんに所有権を主張できません。'),
        'ウ': ('前の占有者の占有を足すと、悪意という欠点も引き継ぐ',
               '前の占有者の占有を併せて主張する場合には、その瑕疵（欠点）も承継します（民法187条2項）。Aは、土地がB所有であることを知っていたので悪意です。Aの占有を併せて主張すると、悪意が引き継がれるので、必要な期間は20年です（民法162条1項）。\n\n問題文のAの3年とCの7年を足しても10年で、20年に足りません。また、Cの7年だけでは、善意無過失の10年（同条2項）にも足りません。本肢は誤りです。\n\n**たとえば**、「自分の分は7年だが、前の人の3年を足せば10年になる」と数えたくなりますが、前の人が悪意だと、足した分の期間も20年が必要になります。'),
        'エ': ('共同相続人の一人は、自分の相続分の範囲で援用できる',
               '時効は、当事者が援用しなければ、裁判所がこれによって裁判をすることができません（民法145条）。共同相続人の一人は、自己の相続分に応じた範囲でのみ、被相続人の取得時効を援用することができ、土地の全部について援用することはできません（判例）。\n\n問題文は「甲土地の全部について、取得時効を援用することができる」としているので、本肢は誤りです。\n\n**たとえば**、亡くなった父の占有で時効が完成していた土地を、兄弟二人が2分の1ずつ相続したとします。兄は、自分の2分の1の範囲で援用でき、全部を自分のものにすることはできません。'),
        'オ': ('一筆の土地の一部だけでも、時効で取得できる',
               '一筆の土地の一部だけを占有してきた場合でも、その部分について、時効により所有権を取得することができます（判例）。\n\n本肢は正しいといえます。\n\n**たとえば**、隣の土地の一部を、自分の庭の続きとして20年間、平穏かつ公然に使ってきたとします。この場合、その使ってきた一部分について、所有権を取得できます。登記をするときは、その部分を分筆してから、所有権の移転の登記をする流れになります。'),
    },
    summary=[
        ('ア', '正', '時効の完成前に現れた買主には、登記がなくても、時効による取得を主張できる'),
        ('イ', '誤', '時効の完成後に現れた買主には、先に登記をした方が勝つので、登記がないと主張できない'),
        ('ウ', '誤', '前の占有者の占有を足すと、悪意も承継するので、20年が必要で、3年＋7年では足りない'),
        ('エ', '誤', '共同相続人の一人が援用できるのは、自己の相続分の範囲に限られる'),
        ('オ', '正', '一筆の土地の一部だけの占有でも、その部分を時効で取得できる'),
    ],
    summary_tail='アとイは、買主が現れたのが時効の完成の前か後か、という一点だけが違います。ウは占有を足すときの欠点の引継ぎ、エは援用の範囲を問う出題でした。',
    supplements=[
        '### 補足説明（ア・イ）：買主が現れたのが、完成の前か後か\n\n同じように見える二つの場面で、結論が分かれます（民法177条、判例）。\n\n- 時効の完成前に買主が現れた：時効を取得した人は、登記がなくても主張できます。\n- 時効の完成後に買主が現れた：二重譲渡に似た関係になり、先に登記をした方が勝ちます。\n\n**たとえば**、Aさんの占有が続いている間に、持ち主のBさんがCさんに売った場合は、Cさんは時効の完成前の買主です。時効が完成した後に売った場合は、完成後の買主です。分かれ目は、売った日が時効の完成の前か後か、だけです。',
        '### 補足説明（ウ）：占有を足すときは、期間と欠点の引継ぎに注意\n\n占有者が替わったときは、自分の占有だけを主張することも、前の占有者の占有を足して主張することもできます（民法187条1項）。ただし、足すときは、前の占有者の欠点も一緒に引き継ぎます（同条2項）。\n\n- 自分の占有だけを主張：Cは、善意無過失で占有を始めたので、10年。\n- Aの占有を足して主張：Aが悪意なので、20年。\n\n**たとえば**、Aが3年、Cが7年占有したなら、10年分あるように見えます。しかし、Cだけなら10年に足りず、Aの分を足すなら20年が必要で、どちらでも時効は完成していません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第61日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、民法145条・162条・177条・187条は、`note-articles/laws/` 配下の原文で確認しました。',
        'ア、イ、エ、オの結論は判例の趣旨によるもので、判例そのものの原文は手元になく、未確認です。本文には判例の番号は書いていません。',
        'ウでCの占有を「善意無過失」としたのは、問題文の「過失なく信じた」という設定に基づく説明です。具体例（兄弟の相続など）は、条文と判例の趣旨をかみ砕いた一般的な説明です。',
    ],
    phrases=['完成の前なら、登記なしで主張できます', '完成の後なら、先に登記をした方が勝ちます', '占有を足すと、悪意も引き継ぎます', '援用できるのは、自分の相続分までです', '土地の一部だけでも、時効で取得できます'],
    header=dict(t1='時効の前か後か、', t2='それが分かれ目！', topic='民法　不動産の取得時効',
                kanji='毎・時・効・不・動・産・取・得'),
    poster_intro='取得時効を、「第三者との関係」（グループA：ア・イ）と「期間と範囲」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='不動産の取得時効を整理', sub='民法 第145条・第162条・第177条・第187条（毎日ドリル 第61日）',
        col_a='第三者との関係', col_b='期間と範囲', n_a=2,
        cards=[
            dict(h='完成前の買主には登記なしで主張できる',
                 ill='a horizontal timeline. On the left a flag labeled 「買主が現れる」; further right a flag labeled 「時効の完成」. A green check mark sits above the first flag, with a small house icon beside it.',
                 words=['買主が現れる', '時効の完成'], tag='完成の前'),
            dict(h='完成後の買主とは先に登記した方が勝つ',
                 ill='a horizontal timeline. On the left a flag labeled 「時効の完成」; further right a flag labeled 「買主が現れる」. A registration stamp labeled 「登記」 is held up by a buyer figure beside the second flag. A green check mark sits beside the stamp.',
                 words=['時効の完成', '買主が現れる', '登記'], tag='完成の後'),
            dict(h='占有を足すと悪意も引き継ぐ',
                 ill='two stacked bars: a short gray bar labeled 「前の占有者」 and a green bar labeled 「自分」 continuing it. A green bracket labeled 「二十年」 spans both bars. A green check mark sits beside the bracket.',
                 words=['前の占有者', '自分', '二十年'], tag='欠点も引き継ぐ'),
            dict(h='共同相続人は相続分の範囲で援用',
                 ill='a land plot divided into two halves, one half highlighted with a green glow and labeled 「相続分」 and the other faded in gray. A heir figure stands beside the highlighted half. A green check mark sits beside the figure.',
                 words=['相続分'], tag='相続分の範囲'),
            dict(h='土地の一部だけでも時効取得できる',
                 ill='two neighboring land plots; a small strip of the neighbor plot next to the first one is highlighted with a green glow, and a figure with a garden bench stands on the strip. A green check mark sits beside the strip.',
                 words=[], tag='一部でも取得'),
        ],
        kanji='買・主・現・時・効・完・成・前・後・登・記・占・有・者・自・分・二・十・年・相・続・範・囲'.split('・')),
    nb_label='ア・イ・ウ肢', nb_intro='ア・イ・ウの補足説明に合わせた2枚です。1枚目は、買主が現れた時期による違いを時間の流れで示します。2枚目は、占有を足したときの期間の違いを示します。',
    notebooks=[
        dict(name='買主が現れたのが、完成の前か後か', args=dict(
            title='買主が現れたのは、いつ？', sub='取得時効と登記（毎日ドリル 第61日 ア・イ）',
            req='a timeline diagram',
            layout="""--- TIMELINE ---
Render as a clean flat-design horizontal timeline in the upper half, with two lanes stacked vertically. A common timeline axis runs left to right with one flag in the middle labeled 時効の完成 (with an icon of a calendar page).
Upper lane (green accent), lane label: 完成の前に買主が現れた. A buyer figure with a house icon stands to the left of the middle flag. At the right end, a result badge with a green check mark: 登記なしで主張できる
Lower lane (orange accent), lane label: 完成の後に買主が現れた. A buyer figure with a house icon stands to the right of the middle flag, holding a registration stamp labeled 登記. At the right end, a result badge with a green check mark: 先に登記した方が勝つ
The two lane labels are different strings; draw them in different accent colors (green and orange). Use exactly these strings, and no others, for the labels.""",
            callout='買主が現れたのが、時効の完成の前なら、登記がなくても主張できます。\n完成の後なら、先に登記をした方が勝つ関係なので、登記がないと主張できません。',
            footer='民法百七十七条',
            kanji='時・効・完・成・前・後・買・主・登・記・主・張・先・勝'.split('・'), what='timeline',
            check='confirm the two lanes carry different lane labels in different accent colors and that the buyer figure is left of the flag in the upper lane and right of the flag in the lower lane, ')),
        dict(name='占有を足したときの期間', args=dict(
            title='占有を足すと、何年必要？', sub='占有の承継と欠点の引継ぎ（毎日ドリル 第61日 ウ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「自分の占有だけ」 on the left and 「前の人の占有を足す」 on the right. Draw them in different accent colors (blue and orange). Both panels end with the same red cross, because neither reaches the required length.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 自分の占有だけ
Scene: a bar labeled 七年 on a timeline, with a goal marker labeled 十年 at its right that the bar does not reach.
Note: 善意無過失なら十年
Result badge with a red cross: 足りない

RIGHT PANEL (orange accent):
Panel header: 前の人の占有を足す
Scene: two connected bars labeled 三年 and 七年 on a timeline, with a goal marker labeled 二十年 at its right that the bars do not reach.
Note: 悪意も引き継ぐので二十年
Result badge with a red cross: 足りない""",
            callout='前の占有者の占有を足して主張するときは、その欠点も引き継ぎます。\n前の占有者が悪意なら、足した場合は二十年が必要で、三年と七年の合計では足りません。',
            footer='民法百六十二条・百八十七条',
            kanji='占・有・善・意・無・過・失・悪・年・足・引・継'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (自分の占有だけ on the left and 前の人の占有を足す on the right), that the left goal marker reads 十年 and the right goal marker reads 二十年, and that both panels end with a red cross, ')),
    ],
)
