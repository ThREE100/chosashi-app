def kj(*ss, n=14):
    out = []
    for s in ss:
        for c in s:
            if '一' <= c <= '龥' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='兄弟姉妹の代襲は一代、放棄は代襲しない',
    intro='相続について、「だれが相続人になるか」「どれだけ受け取るか」「遺言や遺産分割にどんな制限があるか」を問う問題です（民法887条・889条・900条・908条・939条・1023条）。\n\nこの記事では、代襲相続が起きる場面と起きない場面、半血の兄弟姉妹の相続分、遺言と生前処分の関係、遺産分割を禁じる期間を、具体的な場面で確認していきましょう。この問題は「正しいもの」の組合せを選ぶ形式です。',
    sections={
        'ア': ('兄弟姉妹の代襲は、その子までで止まる',
               '兄弟姉妹が相続人となる場合の代襲は、被相続人の兄弟姉妹の子までです。民法889条2項は、子の代襲を定めた887条2項だけを準用しており、その先の代襲を定めた887条3項は準用していません。\n\n問題文は、兄の子Cが先に死亡した場合に、Cの子Dが相続人になるとしています。この点が条文と違うので、本肢は誤りです。\n\n**たとえば**、独身で子も親もいない人が亡くなり、兄が相続人になるはずだったところ、兄はすでに他界していたとします。この場合は、兄の子（おいやめい）が代わりに相続人となります。しかし、その子も先に亡くなっていたとき、さらにその子（兄の孫）が代わって相続人になることはありません。'),
        'イ': ('相続の放棄は、代襲の原因にならない',
               '代襲が起こるのは、子が相続の開始以前に死亡したとき、相続欠格に当たるとき、廃除によって相続権を失ったときに限られます（民法887条2項）。相続の放棄は、この中に入っていません。\n\n放棄をした人は、その相続については初めから相続人とならなかったものとみなされます（同法939条）。問題文は、放棄をしたBの子Cが代襲するとしているので、本肢は誤りです。\n\n**たとえば**、亡くなった父に借金が多く、子Bが家庭裁判所で相続の放棄をしたとします。Bには子Cがいますが、Cが父の相続人として借金を引き継ぐことにはなりません。Bの相続権がCへ移るのではなく、Bが初めから相続人でなかったことになるからです。'),
        'ウ': ('半血の兄弟姉妹の相続分は、全血の二分の一',
               '配偶者と兄弟姉妹が相続人であるときは、配偶者が4分の3、兄弟姉妹が合わせて4分の1です（民法900条3号）。\n\n兄弟姉妹が数人いるときは等分しますが、父母の一方だけを同じくする兄弟姉妹の相続分は、父母の双方を同じくする兄弟姉妹の半分です（同条4号ただし書）。\n\n本肢では、兄C（父母の双方が同じ）と弟D（父だけが同じ）の相続分を2対1で分けます。兄弟姉妹の合計4分の1は12分の3ですから、Cが12分の2、Dが12分の1です。本肢は正しいといえます。\n\n**たとえば**、遺産が1200万円だとすると、配偶者が900万円、Cが200万円、Dが100万円です。Dの取り分は、Cの半分になります。'),
        'エ': ('遺言の後に売却したら、その部分の遺言は撤回したものとみなされる',
               '遺言が、遺言の後にされた生前処分その他の法律行為と抵触するときは、抵触する部分について、遺言を撤回したものとみなします（民法1023条2項）。\n\n本肢は正しいといえます。\n\n**たとえば**、「甲土地をBに遺贈する」と遺言した人が、その後に生前に甲土地をCへ売ってしまったとします。この場合、甲土地についての遺言は撤回したものとみなされ、Bは甲土地を遺贈で取得することができません。'),
        'オ': ('遺言で遺産分割を禁じられるのは、五年を超えない期間',
               '被相続人は、遺言で、相続開始の時から5年を超えない期間を定めて、遺産の分割を禁じることができます（民法908条1項）。\n\n問題文は、7年間の禁止がその期間のとおり効力を生ずるとしています。5年を超える期間を定めた点が条文と違うので、本肢は誤りです。\n\n**たとえば**、父が遺言に「私が死んでから7年間は、遺産を分けてはならない」と書いたとしても、遺言で禁じることができる期間は5年を超えないものに限られます。7年という定めを、そのまま有効な禁止期間として扱うことはできません。'),
    },
    summary=[
        ('ア', '誤', '兄弟姉妹の代襲は、その子までで、兄弟姉妹の孫には及ばない'),
        ('イ', '誤', '相続の放棄は代襲の原因ではなく、放棄をした人の子は代襲しない'),
        ('ウ', '正', '父母の一方だけを同じくする兄弟姉妹の相続分は、双方を同じくする兄弟姉妹の二分の一'),
        ('エ', '正', '遺言の後の生前処分が遺言と抵触するときは、その部分の遺言は撤回したものとみなされる'),
        ('オ', '誤', '遺言で遺産分割を禁じられるのは、相続開始の時から五年を超えない期間'),
    ],
    summary_tail='アは代襲の範囲、イは代襲の原因、オは期間の数字がひっかけでした。「子の代襲は孫、ひ孫と続くが、兄弟姉妹の代襲は子まで」「放棄は代襲の原因ではない」「遺言による分割禁止は五年まで」と整理しましょう。',
    supplements=[
        '### 補足説明（ア・イ）：代襲相続が起こる場面と、起こらない場面\n\n相続人となるはずの人が相続の開始以前に亡くなっていたとき、その子が代わりに相続人になることを代襲相続といいます。ただし、どこまで代襲できるかは、だれが相続人かで違います。\n\n| 場面 | 代襲相続 | 根拠 |\n|---|---|---|\n| 被相続人の子が相続人 | 子、孫、ひ孫と続けて代襲できる | 887条2項・3項 |\n| 被相続人の兄弟姉妹が相続人 | その子（おいやめい）までで止まる | 889条2項 |\n| 相続人が相続の放棄をした | 代襲は起こらない（初めから相続人でなかったことになる） | 939条 |\n\n代襲が起こる原因は、相続の開始以前の死亡、相続欠格、廃除の三つです（887条2項）。\n\n**たとえば**、亡くなった人の子が先に死亡していれば、その子の子（孫）が代襲します。孫も先に死亡していれば、さらにその子（ひ孫）へと続きます。一方、亡くなった人の兄が先に死亡していれば兄の子までですが、その子も先に死亡していても、兄の孫は代襲しません。',
        '### 補足説明（オ）：遺産分割を止められる期間\n\n遺産の分割を止める方法は、だれが決めるかで条文が分かれています。\n\n| 決める人 | 期間 | 根拠 |\n|---|---|---|\n| 被相続人（遺言） | 相続開始の時から5年を超えない期間 | 908条1項 |\n| 共同相続人（契約） | 5年以内の期間を定める。更新もできるが、終期は相続開始の時から10年を超えられない | 908条2項・3項 |\n\n**たとえば**、父が遺言で分割を禁じるなら、相続開始の時から5年までです。これに対し、きょうだいが話し合って「しばらく分けない」と契約するときは、5年以内の期間を定め、更新しても相続開始の時から10年が限度です。「10年」は共同相続人の契約の終期の限度であり、遺言による禁止の限度ではありません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第75日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、民法887条、889条、900条、908条、939条、1023条は、`note-articles/laws/` 配下の原文で確認しました。',
        'エの具体例（遺贈の後に売却したときBが遺贈を受けられないこと）は、1023条2項の文言から導いた一般的な説明です。個別の判例の確認はしていません。',
        'オの具体例は、908条1項の「5年を超えない期間」の文言からの説明です。5年を超える期間を定めた遺言の効力の細かい扱い（期間が短縮されるかどうかなど）は、条文からは確認できないため、記事では断定していません。',
    ],
    phrases=['兄弟姉妹の代襲は子までです', '放棄をしても代襲は起きません', '半血の兄弟姉妹は二分の一です', '売ってしまえば遺言は撤回扱い', '遺言で分割を禁じるのは五年まで'],
    header=dict(t1='相続人はだれで、', t2='いくら？いつまで？', topic='民法　相続',
                kanji='相・続・人・民・法・毎'),
    poster_intro='相続のルールを、「相続人と相続分」（グループA：ア・イ・ウ）と「遺言と遺産分割」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='相続のルールを整理', sub='民法 第887条・第889条・第900条・第908条・第1023条（毎日ドリル 第75日）',
        col_a='相続人と相続分', col_b='遺言と遺産分割', n_a=3,
        cards=[
            dict(h='兄弟姉妹の代襲は子まで',
                 ill='a simple family diagram. On the left a deceased person figure; next to it a brother figure and the brother\'s child figure, enclosed together by a green bracket labeled 「子まで」. The brother\'s grandchild figure stands outside the bracket, drawn in pale gray with a thin dashed outline.',
                 words=['子まで'], tag='孫には及ばない'),
            dict(h='放棄は代襲の原因ではない',
                 ill='a parent figure, a child figure and the child\'s own child figure in a row. The child figure holds a document labeled 「放棄」. The grandchild figure is drawn in pale gray with a thin dashed outline and stands apart from a small inheritance chest on the right.',
                 words=['放棄'], tag='子は代襲しない'),
            dict(h='半血の兄弟姉妹は二分の一',
                 ill='two horizontal bars side by side: a long bar labeled 「両方が同じ」 and a bar exactly half as long labeled 「一方だけ同じ」. A green check mark sits beside the bars.',
                 words=['両方が同じ', '一方だけ同じ'], tag='相続分は半分'),
            dict(h='売ったら遺言は撤回扱い',
                 ill='a will document on the left, a house in the middle, and a seller figure handing a house key to a buyer figure on the right. A round stamp labeled 「撤回」 sits on the will. A green check mark sits beside the stamp.',
                 words=['撤回'], tag='抵触する部分だけ'),
            dict(h='遺言で分割を禁じるのは五年まで',
                 ill='a calendar strip with five equal blocks in a row. A green bracket above spans all five blocks and is labeled 「五年まで」. A will document sits above the bracket.',
                 words=['五年まで'], tag='遺言の上限は五年'),
        ],
        kanji=kj('兄弟姉妹代襲子放棄半血二分遺言撤回五年禁割', n=24)),
    nb_label='ア・イ・オ肢', nb_intro='ア・イ・オの補足説明に合わせた2枚です。1枚目は、代襲相続が起こる場面と起こらない場面を表で示します。2枚目は、遺産分割を止められる期間を、遺言と契約で左右に対比します。',
    notebooks=[
        dict(name='代襲相続が起こる場面と、起こらない場面', args=dict(
            title='代襲相続は、どこまで？', sub='民法887条・889条・939条（毎日ドリル 第75日 ア・イ）',
            req='a comparison table',
            layout="""--- TABLE ---
Render as a clean flat-design table with a header row and three body rows, in rounded panel style. Each body row carries a small family-diagram icon at the left edge.
Header row (blue accent), three column headers: 場面 | 代襲相続 | 根拠
Row 1: 子が相続人 | 子、孫、ひ孫と続けて代襲できる | 887条
Row 2: 兄弟姉妹が相続人 | その子までで止まる | 889条
Row 3: 相続の放棄をした | 代襲は起こらない | 939条
Use exactly these strings, and no others. Do not use check marks or cross marks.""",
            callout='兄弟姉妹の代襲は、その子までで止まります。\n相続の放棄は代襲の原因ではなく、放棄をした人は初めから相続人でなかったものとみなされます。',
            footer='民法887条・889条・939条',
            kanji=kj('代襲相続子孫兄弟姉妹放棄', n=14), what='table',
            check='confirm the table has exactly three body rows and that no check mark or cross mark appears, ')),
        dict(name='遺産分割を止められる期間', args=dict(
            title='遺産分割を止められる期間', sub='民法908条（毎日ドリル 第75日 オ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「遺言で禁じる」 on the left and 「共同相続人の契約」 on the right. Draw them large and in different accent colors (blue on the left, green on the right) so they can never be confused or duplicated. Do not use check marks or cross marks.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 遺言で禁じる
Scene: an isometric scene of a will document on a desk with a calendar strip of five blocks.
Rows of text:
決める人: 被相続人
期間: 相続開始の時から五年を超えない期間

RIGHT PANEL (green accent):
Panel header: 共同相続人の契約
Scene: an isometric scene of several siblings figures shaking hands over a contract sheet, with a calendar strip behind them.
Rows of text:
決める人: 共同相続人
期間: 五年以内の期間を定める
更新: できる。ただし、終期は相続開始の時から十年まで""",
            callout='遺言で遺産分割を禁じられるのは、相続開始の時から五年を超えない期間です。\n十年は、共同相続人が契約で定める場合の終期の限度で、遺言の限度ではありません。',
            footer='民法908条1項・2項・3項',
            kanji=kj('遺言禁共同相続人契約被期間更新', n=14), what='panels',
            check='confirm the two panel headers are different strings (遺言で禁じる on the left and 共同相続人の契約 on the right) drawn in different accent colors, ')),
    ],
)
