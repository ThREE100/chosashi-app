def kj(*ss, n=14):
    out = []
    for s in ss:
        for c in s:
            if '一' <= c <= '龥' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='表題部所有者の変更はできず、更正に承諾',
    intro='表示に関する登記の申請人について、相続人が申請できる場合、表題部所有者を変えたいとき、表題部所有者や持分が誤っていたときの手続きを問う問題です（不動産登記法30条・32条・33条）。この問題は、正しいものを選ぶ形です。\n\nこの記事では、「相続人が申請できる範囲」と、「変更はできないが更正はできる」という考え方を、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('名義人が亡くなったら、相続人が滅失の登記を申請できる',
               '表題部所有者又は所有権の登記名義人が表示に関する登記の申請人となることができる場合に、その名義人について相続があったときは、相続人は、その登記を申請することができます（不動産登記法30条）。\n\n建物の滅失の登記が、名義人の死亡前の取り壊しによるものであっても、共同相続人の一人から申請できる、という取扱いです。本肢は正しいといえます。\n\n**たとえば**、父A名義の古い家が、父の生前に取り壊されたのに、滅失の登記がされていなかったとします。子の一人であるBが、他の兄弟の同意を待たずに、滅失の登記を申請できます。'),
        'イ': ('共同相続人の一人が申請するなら、自分の相続を示せば足りる',
               '共同相続人の一人が、30条により表示に関する登記を申請するときは、申請人自身が相続人であることを示せば足り、共同相続人全員についての相続の情報までは求められません、という取扱いです。\n\n問題文は、B及びCの全員についてAの相続があったことを証する情報を提供しなければならないとしています。本肢は誤りです。\n\n**たとえば**、父Aの子B、Cのうち、Bだけが申請するときは、Bが相続人であることを示す書類を出せば足ります。Cの分まで、そろえる必要はありません。'),
        'ウ': ('表題部所有者の変更の登記は、そのままではできない',
               '表題部所有者又はその持分についての変更は、その不動産について所有権の保存の登記をした後に、所有権の移転の登記の手続をするのでなければ、登記することができません（不動産登記法32条）。\n\n問題文は、BがAからBへの表題部所有者の変更の登記を申請できるとしています。本肢は誤りです。\n\n**たとえば**、Aが表題部所有者として載っている土地をBが買い受けたときは、まずAが所有権の保存の登記をして、そのうえでAからBへ所有権の移転の登記をします。'),
        'エ': ('真の所有者は、表題部所有者の承諾があれば更正の登記を申請できる',
               '不動産の所有者と表題部所有者とが異なるときの更正の登記は、不動産の所有者以外の者は申請できません（不動産登記法33条1項）。所有者が申請するには、表題部所有者の承諾が必要です（同条2項）。\n\n本肢は正しいといえます。\n\n**たとえば**、新築した真の所有者はBなのに、登記記録の表題部所有者がAと載っていたとします。Aの承諾があれば、Bは、表題部所有者をBに直す更正の登記を申請できます。'),
        'オ': ('持分の更正は、持分が減る共有者の承諾がなければできない',
               '表題部所有者である共有者の持分についての更正の登記は、その共有者以外の者は申請できません（不動産登記法33条3項）。共有者が申請するときは、更正によって持分が変わる他の共有者の承諾が必要です（同条4項）。\n\n問題文は、Bの承諾がなくても申請できるとしています。本肢は誤りです。\n\n**たとえば**、AとBの持分が2分の1ずつと記録されているのを、Aが3分の2、Bが3分の1に直す場合、Bの持分が減るので、Bの承諾が必要です。'),
    },
    summary=[
        ('ア', '正', '名義人が亡くなったときは、相続人が滅失の登記を申請できる'),
        ('イ', '誤', '共同相続人の一人が申請するときは、全員の相続を示す必要はなく、自分が相続人であることを示せば足りる'),
        ('ウ', '誤', '表題部所有者の変更の登記はできず、所有権の保存の登記をして、移転の登記をする'),
        ('エ', '正', '真の所有者は、表題部所有者の承諾があれば、表題部所有者の更正の登記を申請できる'),
        ('オ', '誤', '持分の更正の登記は、持分が変わる他の共有者の承諾が必要'),
    ],
    summary_tail='ウは「変更」と「更正」の取り違え、オは「承諾が必要」という条件を外した出題です。この問題は正しいものを選ぶ形なので、正解はアとエの組合せになります。',
    supplements=[
        '### 補足説明（ウ）：表題部所有者を買主に直接変えることはできない\n\n不動産を買い受けても、買主を表題部所有者にする変更の登記はできません。権利の移転は、次の流れで登記します。\n\n1. 表題部所有者が、所有権の保存の登記をする（74条1項1号）。\n2. 保存の登記をした名義人から買主へ、所有権の移転の登記をする。\n\n**たとえば**、Aが表題部所有者として載っている土地を、Bが買ったとします。登記記録の表題部の「A」を「B」に書き換えるのではなく、Aの名義で保存の登記をしたうえで、AからBへの移転の登記をします。',
        '### 補足説明（エ・オ）：更正の登記の申請人と、承諾が必要な人\n\n表題部所有者についての更正の登記には、誰が申請し、誰の承諾が要るかが決まっています。\n\n| 更正の内容 | 申請できる人 | 承諾が必要な人 | 条文 |\n|---|---|---|---|\n| 表題部所有者の更正 | 不動産の所有者 | 表題部所有者 | 33条1項・2項 |\n| 共有者の持分の更正 | 表題部所有者である共有者 | 持分が変わる他の共有者 | 33条3項・4項 |\n\n**たとえば**、所有者が違うときは、真の所有者が申請し、今載っている表題部所有者が承諾します。持分が違うときは、共有者の一人が申請し、持分が変わる共有者が承諾します。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第13日（朝）　択一」とし、note の引用の出典欄は空欄にします。この問題は「正しいものの組合せ」を選ぶ形です。',
        '各肢の根拠のうち、不動産登記法30条、32条、33条1項から4項まで、74条1項1号は、`note-articles/laws/` 配下の原文で確認しました。',
        'ア（死亡前に取り壊された建物の滅失の登記を共同相続人の一人が申請できること）とイ（共同相続人の一人が申請するとき、全員分の相続を証する情報までは要らないこと）は、先例の取扱いに基づく内容です。先例の原文は手元にないため、番号は書かず、原文は未確認です。年度別解説記事の整理と同じ結論であることのみ確認しました。',
        'ウの「Aが所有権の保存の登記をし、AからBへ所有権の移転の登記をする」は、32条の文言と74条1項1号からの整理です。具体例は、条文をかみ砕いた一般的な例です。',
    ],
    phrases=['相続人は表示の登記を申請できます', '一人の申請なら自分の相続を示せば足ります', '表題部所有者は変更できません', '真の所有者は承諾を得て更正できます', '持分の更正には他の共有者の承諾です'],
    header=dict(t1='表題部所有者は、', t2='どう直す？', topic='不動産登記法　表示に関する登記の申請人',
                kanji='表・題・部・所・有・者・登・記・毎'),
    poster_intro='表示に関する登記の申請人を、「相続人の申請」（グループA：ア・イ）と「表題部所有者と持分の直し方」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='表示に関する登記の申請人を整理', sub='不動産登記法 第30条・第32条・第33条（毎日ドリル 第13日）',
        col_a='相続人の申請', col_b='表題部所有者と持分', n_a=2,
        cards=[
            dict(h='名義人が亡くなったら、相続人が申請できる',
                 ill='a demolished old house shown as a pile of materials, and an heir figure holding a form labeled 「滅失」 stepping forward. A faded portrait of the deceased owner hangs on the wall behind. A green check mark sits beside the heir figure.',
                 words=['滅失'], tag='相続人が申請'),
            dict(h='共同相続人の一人は自分の相続を示す',
                 ill='two heir figures standing side by side, one holding a family document and a form, highlighted with a green glow. The other figure stands aside with empty hands. A label above the first figure reads 「自分」. A green check mark sits beside the document.',
                 words=['自分'], tag='全員分は要らない'),
            dict(h='表題部所有者の変更はできない',
                 ill='a record sheet with a name plate. A buyer figure holds a new name plate but a thin barrier stands between the buyer and the record sheet. Beside it, a route of two steps: a stamp labeled 「保存」 and then a stamp labeled 「移転」. A green check mark sits beside the two-step route.',
                 words=['保存', '移転'], tag='保存の後に移転'),
            dict(h='真の所有者は承諾を得て更正できる',
                 ill='a record sheet with the wrong owner name plate, a true owner figure holding a corrected name plate, and the recorded owner figure giving a consent sheet. A label above the consent sheet reads 「承諾」. A green check mark sits beside the consent sheet.',
                 words=['承諾'], tag='表題部所有者の承諾'),
            dict(h='持分の更正は他の共有者の承諾が必要',
                 ill='a pie chart divided into two slices being corrected, and two co-owner figures. One figure holds a form, and the other gives a consent sheet. A label above the consent sheet reads 「承諾」. A green check mark sits beside the consent sheet.',
                 words=['承諾'], tag='持分が変わる人の承諾'),
        ],
        kanji=kj('相続人滅失自分保存移転承諾表題部所有者更正持分')),
    nb_label='ウ・エ・オ肢', nb_intro='ウ・エ・オの補足説明に合わせた2枚です。1枚目は、表題部所有者を買主に直接変えられないことを流れで示します。2枚目は、更正の登記で誰が申請し誰が承諾するのかを整理します。',
    notebooks=[
        dict(name='買主への権利の移転の流れ', args=dict(
            title='買主に名義を移すには？', sub='不動産登記法32条（毎日ドリル 第13日 ウ）',
            req='a step-by-step flow diagram',
            layout="""--- FLOW ---
A clean flat-design vertical flow with three steps connected by downward arrows.

Step 1 (blue box): 表題部所有者がAのまま、Bが買い受ける
Icon: a record sheet with the name plate A, and a buyer figure with a contract.

Step 2 (blue box): Aが所有権の保存の登記をする
Icon: a stamp being pressed onto the record sheet.

Step 3 (green box): AからBへ所有権の移転の登記をする
Icon: a name plate being handed from the seller figure to the buyer figure.

At the right side of Step 1, a small side note in a gray rounded box: 表題部所有者をBに変える登記は、できない""",
            callout='表題部所有者の変更は、そのままでは登記できません。\n所有権の保存の登記をした後に、所有権の移転の登記をする流れになります。',
            footer='不動産登記法32条、74条1項',
            kanji=kj('表題部所有者買所有権保存登記移転'), what='flow',
            check='confirm that the three steps are connected by downward arrows and that the gray side note reads 表題部所有者をBに変える登記は、できない, ')),
        dict(name='更正の登記の申請人と承諾', args=dict(
            title='更正の登記は、誰が申請し誰が承諾？', sub='不動産登記法33条（毎日ドリル 第13日 エ・オ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「表題部所有者の更正」 on the left and 「持分の更正」 on the right. Draw them large and in different accent colors (blue on the left, green on the right) so they can never be confused or duplicated. Do not draw any cross mark or check mark in this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 表題部所有者の更正
Scene: an isometric scene of a true owner figure holding a form, and the recorded owner figure holding a consent sheet.
Text rows:
申請できる人: 不動産の所有者
承諾が必要な人: 表題部所有者

RIGHT PANEL (green accent):
Panel header: 持分の更正
Scene: an isometric scene of one co-owner figure holding a form, and another co-owner figure holding a consent sheet.
Text rows:
申請できる人: 表題部所有者である共有者
承諾が必要な人: 持分が変わる他の共有者""",
            callout='表題部所有者の更正は、真の所有者が表題部所有者の承諾を得て申請します。\n持分の更正は、共有者が、持分が変わる他の共有者の承諾を得て申請します。',
            footer='不動産登記法33条1項から4項まで',
            kanji=kj('表題部所有者更正持分共有者申請承諾不動産'), what='panels',
            check='confirm the two panel headers are different strings drawn in different accent colors, and that no check mark or cross mark appears anywhere, ')),
    ],
)
