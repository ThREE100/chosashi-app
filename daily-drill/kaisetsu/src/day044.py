D = dict(
    catch='更正できるのは所有者、承諾が必要',
    intro='土地や建物の表題部に載っている「表題部所有者」の更正や変更を問う問題です（不動産登記法32条・33条、不動産登記令別表の二の項・三の項）。この問題は「誤っているもの」を選びます。\n\nこの記事では、表題部所有者を直す更正を申請できる人、承諾が必要な人、売買があったときの手続、承諾書の代わりになる情報を、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('真の所有者が、表題部所有者の承諾を得て更正を申請する',
               '不動産の所有者と表題部所有者が異なる場合の更正の登記は、不動産の所有者以外の者は申請できません（不動産登記法33条1項）。\n\nそして、所有者は、表題部所有者の承諾があるときでなければ、申請できません（同条2項）。真の所有者Bが、表題部所有者Aの承諾を得て申請するという本肢は、正しいといえます。\n\n**たとえば**、登記上の表題部所有者はAさんですが、本当の所有者はBさんだとします。Bさんは、Aさんの承諾を得たうえで、表題部所有者をBさんに直す更正の登記を申請します。'),
        'イ': ('登記されている表題部所有者は、単独で更正を申請できない',
               '表題部所有者についての更正の登記を申請できるのは、不動産の所有者だけです（不動産登記法33条1項）。登記されている表題部所有者は、申請人になれません。Aの役割は、承諾をする側です（同条2項）。\n\n問題文は「Aが…単独で、表題部所有者をBとする更正の登記を申請することができる」としているので、本肢は誤りです。\n\n**たとえば**、自分の名義で登記されているAさんが、本当の所有者はBさんだと気づいたとします。Aさんは、自分では更正を申請できません。Bさんが申請するのを承諾する立場になります。'),
        'ウ': ('売買による表題部所有者の変更は、保存の登記から始める',
               '表題部所有者の変更は、所有権の保存の登記をした後に、所有権の移転の登記の手続でするのでなければ、登記することができません（不動産登記法32条）。\n\n問題文のBは「表題部所有者をAからBとする変更の登記」を申請できるとしていますが、そのような登記はできません。本肢は誤りです。\n\n**たとえば**、表題登記だけがされた建物の表題部所有者Aさんが、建物をBさんに売ったとします。Bさんは、表題部所有者を書き換えることはできません。まずA名義で所有権の保存の登記をして、そのうえでAさんからBさんへの所有権の移転の登記をします。'),
        'エ': ('共有者の持分の更正には、他の共有者の承諾を証する情報が要る',
               '表題部所有者である共有者の持分についての更正の登記は、共有者だけが申請できます（不動産登記法33条3項）。更正する共有者は、その更正によって持分を更正することになる他の共有者の承諾がなければ、申請できません（同条4項）。\n\nそのため、申請のときは、承諾を証する他の共有者が作成した情報を提供します（不動産登記令別表の三の項添付情報欄）。本肢は正しいといえます。\n\n**たとえば**、AさんとBさんが共有者として登記されていて、持分が誤っていたとします。Aさんが持分の更正を申請するときは、持分が変わるBさんの承諾書を添えます。'),
        'オ': ('承諾書の代わりに、裁判があったことを証する情報でもよい',
               '表題部所有者についての更正の登記の添付情報には、表題部所有者の承諾を証する、表題部所有者が作成した情報があります。この情報は、表題部所有者に対抗することができる裁判があったことを証する情報でも代えられます（不動産登記令別表の二の項添付情報欄ハ）。本肢は正しいといえます。\n\n**たとえば**、Aさんが承諾してくれないとき、Bさんは、Aさんに対抗できる裁判があったことを証する情報を提供して、更正を申請することができます。あわせて、Bさんが所有権を有することを証する情報（同欄イ）と、Bさんの住所を証する情報（同欄ロ）も提供します。'),
    },
    summary=[
        ('ア', '正', '真の所有者が、表題部所有者の承諾を得て、表題部所有者の更正を申請する'),
        ('イ', '誤', '登記されている表題部所有者は、単独で更正を申請できず、承諾をする側である'),
        ('ウ', '誤', '売買による表題部所有者の変更は、保存の登記をしたうえで、移転の登記でする'),
        ('エ', '正', '持分の更正には、持分が変わる他の共有者の承諾を証する情報が必要'),
        ('オ', '正', '表題部所有者の承諾を証する情報は、対抗できる裁判があったことを証する情報でも代えられる'),
    ],
    summary_tail='イは「申請する人」と「承諾する人」、ウは「更正」と「変更」を入れ替えた出題です。表題部所有者の登記が間違っているのか、あとから代わったのかを、まず見分けましょう。',
    supplements=[
        '### 補足説明（イ）：更正を申請する人と、承諾する人\n\n表題部所有者に関する更正の登記は、次のように、申請する人と承諾する人が決まっています。\n\n| 更正の内容 | 申請できる人 | 承諾が必要な人 |\n|---|---|---|\n| 表題部所有者そのものの更正（所有者が異なる） | 不動産の所有者（不動産登記法33条1項） | 表題部所有者（同条2項） |\n| 共有者の持分の更正 | その共有者（同条3項） | 持分が更正されることになる他の共有者（同条4項） |\n\n**たとえば**、登記上の表題部所有者Aさんが、承諾する人です。Aさん自身が更正を申請する人にはなれません。持分の更正でも、申請するのは共有者の一人で、承諾するのは持分が変わる他の共有者です。',
        '### 補足説明（ウ）：更正と変更は、別の登記\n\n更正と変更は、登記の誤りの理由が違います。法律の定義は、次のとおりです。\n\n| 登記 | 場面 | 手続 |\n|---|---|---|\n| 更正の登記 | 登記事項に錯誤又は遺漏があった場合（不動産登記法2条16号） | 所有者が、表題部所有者の承諾を得て申請する（同法33条） |\n| 変更の登記 | 登記事項に変更があった場合（同法2条15号） | 表題部所有者の変更は、所有権の保存の登記をした後、移転の登記でする（同法32条） |\n\n**たとえば**、最初から登記の所有者が違っていたのが更正、あとから売買で所有者が代わったのが変更、と考えます。売買は変更に当たるので、保存の登記から移転の登記へと進みます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第44日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法2条15号・16号、32条、33条、不動産登記令別表の二の項・三の項は、`note-articles/laws/` 配下の原文で確認しました。',
        '各肢の具体例（AとBの所有者の食い違い、売られた建物、持分が誤っている共有者、承諾しないA）は、条文の文言をかみ砕いた一般的な説明で、個別の先例・通達の確認はしていません。',
        '補足説明（ウ）の「最初から違っていたのが更正、あとから代わったのが変更」という説明は、法2条15号・16号の定義からの一般的な整理です。ウの「Bさんは表題部所有者を書き換えられない」という点は、32条の文言から導いた説明です。',
    ],
    phrases=['更正を申請できるのは真の所有者です', '登記されている名義人は承諾する側です', '売買は保存の登記から移転の登記です', '持分の更正は他の共有者の承諾が必要です', '承諾の代わりに裁判の情報も使えます'],
    header=dict(t1='表題部所有者の更正、', t2='だれが申請する？', topic='不動産登記法　表題部所有者',
                kanji='表・題・部・所・有・者'),
    poster_intro='表題部所有者の登記を、「表題部所有者の更正」（グループA：ア・イ）と「変更・持分の更正・添付情報」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='表題部所有者の登記を整理', sub='不動産登記法 第32条・第33条（毎日ドリル 第44日）',
        col_a='表題部所有者の更正', col_b='変更と持分の更正と添付情報', n_a=2,
        cards=[
            dict(h='真の所有者が承諾を得て更正',
                 ill='an owner figure with a name tag labeled 「所有者」, highlighted with a green glow, holding a form at a counter, with a second figure with a name tag labeled 「表題部所有者」 beside it holding a signed paper labeled 「承諾」. A green check mark sits beside the form.',
                 words=['所有者', '表題部所有者', '承諾'], tag='申請人は真の所有者'),
            dict(h='登記されている名義人は単独で更正できない',
                 ill='a counter scene. A figure with a name tag labeled 「表題部所有者」, drawn in faded gray, stands at the counter with empty hands. A second figure with a name tag labeled 「所有者」, highlighted with a green glow, holds a form. A green check mark sits beside the second figure.',
                 words=['表題部所有者', '所有者'], tag='申請できるのは所有者'),
            dict(h='売却による変更は保存の登記から',
                 ill='a horizontal flow of three small icons: a house with a round stamp labeled 「保存」, then an arrow with a deed document labeled 「移転」, then a buyer figure holding the house. A green check mark sits beside the buyer.',
                 words=['保存', '移転'], tag='保存から移転の順'),
            dict(h='持分の更正は他の共有者の承諾が必要',
                 ill='two co-owner figures standing beside a pie chart of a land plot divided into two shares labeled 「持分」. One figure holds a signed paper labeled 「承諾」 and passes it to the other. A green check mark sits beside the paper.',
                 words=['持分', '承諾'], tag='共有者の承諾'),
            dict(h='承諾書の代わりに裁判の情報も使える',
                 ill='a signed paper labeled 「承諾」 on the left, a small equal sign in the middle, and a judge gavel with a scroll labeled 「裁判」 on the right. A green check mark sits beside the equal sign.',
                 words=['承諾', '裁判'], tag='裁判の証明でも可'),
        ],
        kanji='所・有・者・表・題・部・承・諾・更・正・保・存・移・転・持・分・共・裁・判・申・請'.split('・')),
    nb_label='イ・ウ肢', nb_intro='イ・ウの補足説明に合わせた2枚です。1枚目は、更正を申請する人と承諾する人を整理します。2枚目は、更正と変更の違いを左右の対比で示します。',
    notebooks=[
        dict(name='更正を申請する人と、承諾する人', args=dict(
            title='更正を申請するのは、だれ？', sub='表題部所有者の更正（毎日ドリル 第44日 イ）',
            req='a two-row table diagram',
            layout="""--- TABLE ---
Render as a clean flat-design table with two rows stacked vertically, each row with a small icon on the left, a blue label cell, a green cell for the person who applies, and an orange cell for the person who consents. The column titles are drawn in a thin header band above the rows: 更正の内容 | 申請できる人 | 承諾が必要な人.
Row 1 icon: a record sheet with an owner name line. Label cell: 表題部所有者の更正. Applicant cell: 不動産の所有者. Consent cell: 表題部所有者
Row 2 icon: a pie chart divided into shares. Label cell: 共有者の持分の更正. Applicant cell: その共有者. Consent cell: 持分が変わる他の共有者
Use exactly these strings, and no others. Do not draw any check mark or cross mark.""",
            callout='表題部所有者の更正を申請できるのは不動産の所有者で、登記されている表題部所有者は承諾をする側です。\n持分の更正では、申請するのは共有者の一人、承諾するのは持分が変わる他の共有者です。',
            footer='不動産登記法33条',
            kanji='更・正・申・請・表・題・部・所・有・者・承・諾・持・分・共・不・動・産'.split('・'), what='table',
            check='confirm there are exactly two table rows with three columns each, and that no check mark and no cross mark is drawn, ')),
        dict(name='更正と変更の違い', args=dict(
            title='更正と変更は別の登記', sub='表題部所有者の誤りの理由（毎日ドリル 第44日 ウ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「更正」 on the left and 「変更」 on the right. Draw them very large and in different accent colors (blue and orange) so they can never be confused or swapped. Do not draw any check mark or cross mark on this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 更正
Scene: an isometric scene of a record sheet whose owner line shows a wrong person, with a pencil correcting it. A small caption: 登記事項に錯誤又は遺漏があった
Result badge: 所有者が承諾を得て申請

RIGHT PANEL (orange accent):
Panel header: 変更
Scene: an isometric scene of a house passing from a seller figure to a buyer figure, followed by a small stamp. A small caption: 登記事項に変更があった
Result badge: 保存の登記のあと移転の登記""",
            callout='最初から登記が間違っていたのが更正、あとから所有者が代わったのが変更です。\n売買による表題部所有者の変更は、所有権の保存の登記をしたうえで、移転の登記でします。',
            footer='不動産登記法2条15号・16号、32条、33条',
            kanji='更・正・変・錯・誤・遺・漏・所・有・者・承・諾・保・存・移・転・登・記'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (更正 on the left and 変更 on the right) in very different accent colors, and that no check mark and no cross mark is drawn, ')),
    ],
)
