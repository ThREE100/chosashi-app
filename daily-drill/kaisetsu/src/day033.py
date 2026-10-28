D = dict(
    catch='代襲相続の原因に、放棄は含まれない',
    intro='相続人の範囲、代襲相続、法定相続分、遺産分割の効力、相続の承認・放棄の期間を問う問題です（民法887条・889条・899条の2・900条・909条・915条・939条）。今回は、誤っているものの組合せを選びます。\n\nこの記事では、放棄した人の子は代襲できるのか、兄弟姉妹の相続分の計算、再代襲の有無、そして三箇月の数え始めを、具体的な場面で確認します。',
    sections={
        'ア': ('相続の放棄をしても、その子は代襲しない',
               '代襲相続が起きるのは、相続人となるべき子が、相続の開始以前に死亡したとき、欠格に当たるとき、廃除されたときです（民法887条2項）。相続の放棄は、この原因に入っていません。放棄をした者は、初めから相続人とならなかったものとみなされます（民法939条）。\n\n本肢は条文のとおりで、正しい記述です。\n\n**たとえば**、Aが亡くなり、子Bが相続を放棄したとします。Bに子Cがいても、CはBに代わってAの相続人になることはありません。'),
        'イ': ('父だけが同じ弟の相続分は、兄の半分になる',
               '配偶者と兄弟姉妹が相続人のとき、配偶者の相続分は4分の3、兄弟姉妹の相続分は4分の1です（民法900条3号）。父母の一方だけが同じ兄弟姉妹の相続分は、父母の双方が同じ兄弟姉妹の2分の1です（同条4号ただし書）。\n\n問題文は、Dの相続分を8分の1としています。これは兄弟姉妹の2人で等分した場合の数字で、4号ただし書を見落としています。本肢は誤りです。\n\n**たとえば**、全体を12とすると、配偶者Bが9、兄Cが2、弟Dが1になります。Dは12分の1です。'),
        'ウ': ('兄弟姉妹の相続では、再代襲は起きない',
               '兄弟姉妹が相続人になる場合に準用されるのは、代襲を定める887条2項だけです（民法889条2項）。再代襲を定める887条3項は準用されません。\n\n本肢は条文のとおりで、正しい記述です。\n\n**たとえば**、Aに子も親も配偶者もおらず、兄Bも、Bの子Cも先に亡くなっていたとします。Cの子Dは、Aの相続人になりません。兄弟姉妹の場合は、甥や姪の代で止まります。'),
        'エ': ('遺産分割は相続開始にさかのぼるが、超える部分は登記が必要',
               '遺産の分割は、相続開始の時にさかのぼって効力を生じます（民法909条本文）。ただし、法定相続分を超える部分は、登記などの対抗要件を備えなければ、第三者に対抗できません（民法899条の2第1項）。\n\n本肢は条文のとおりで、正しい記述です。\n\n**たとえば**、子BとCが共同相続した土地を、Bが単独で取得すると協議したとします。法定相続分は2分の1ずつなので、Bは、超える2分の1の部分について、登記をしないと第三者に対抗できません。'),
        'オ': ('三箇月は、相続の開始を知った時から数える',
               '相続人は、自己のために相続の開始があったことを知った時から3箇月以内に、単純承認、限定承認又は放棄をしなければなりません（民法915条1項本文）。\n\n問題文は、死亡の日から3箇月にあたる7月1日までとしているので、本肢は誤りです。Bが死亡を知ったのは5月10日ですから、そこから数えます。\n\n**たとえば**、4月1日に亡くなったことを、5月10日になって初めて知った相続人は、5月10日から3箇月以内、つまり8月10日ごろまでに決めればよいことになります。'),
    },
    summary=[
        ('ア', '正', '相続の放棄は代襲の原因ではない。放棄した者の子は代襲しない'),
        ('イ', '誤', '父のみ同じ弟の相続分は兄の2分の1で、8分の1ではなく12分の1'),
        ('ウ', '正', '兄弟姉妹の代襲は子の一代限り。再代襲は起きない'),
        ('エ', '正', '遺産分割は相続開始にさかのぼるが、法定相続分を超える部分は登記がないと第三者に対抗できない'),
        ('オ', '誤', '三箇月は、死亡の日ではなく、自己のために相続の開始があったことを知った時から数える'),
    ],
    summary_tail='今回は誤っているものを選ぶ問題なので、イとオが正解です。イは兄弟姉妹の相続分の半分ルールの見落とし、オは三箇月の数え始めの取り違えです。',
    supplements=[
        '### 補足説明（ア・ウ）：代襲相続の原因と、再代襲の範囲\n\n代襲相続には、原因と範囲の決まりがあります。\n\n- 代襲の原因：相続の開始以前の死亡、欠格、廃除の3つ。相続の放棄は含まれない（民法887条2項、939条）。\n- 子の場合：孫が代襲し、孫も先に亡くなっていればひ孫が再代襲する（民法887条3項）。\n- 兄弟姉妹の場合：甥・姪が代襲するが、再代襲はない（民法889条2項）。\n\n**たとえば**、放棄をした子の子は代襲しません。兄弟姉妹では、甥や姪がすでに亡くなっていても、その子は相続人になりません。',
        '### 補足説明（イ）：配偶者と兄弟姉妹の相続分の計算\n\n配偶者と兄弟姉妹が相続人のとき、相続分は次の順で求めます。\n\n- 配偶者が4分の3、兄弟姉妹全体で4分の1（民法900条3号）。\n- 兄弟姉妹の中では、父母の双方が同じ者を1、父母の一方だけが同じ者を2分の1の割合にする（同条4号ただし書）。\n- 兄Cが1、弟Dが2分の1なので、4分の1を2対1に分ける。Cは6分の1、Dは12分の1。\n\n**たとえば**、全体を12に分けると、配偶者が9、Cが2、Dが1になります。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第33日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、民法887条2項・3項、889条2項、899条の2第1項、900条3号・4号ただし書、909条、915条1項、939条は、`note-articles/laws/` 配下の原文で確認しました。',
        'この問題は「誤っているものの組合せ」を選ぶ問題です。各肢の本文の「正しい記述です」は、肢の記述が条文どおりであることを指します。',
        'オの「8月10日ごろ」は、民法の期間の計算（初日を算入しない）に基づく一般的な目安で、民法140条・143条の原文までは今回確認していません。',
    ],
    phrases=['相続の放棄は代襲の原因ではありません', '父だけが同じ弟の相続分は兄の半分です', '兄弟姉妹の相続に再代襲はありません', '遺産分割でも超える部分は登記が必要です', '三箇月は知った時から数えます'],
    header=dict(t1='相続人はだれ？', t2='いつまでに決める？', topic='民法　相続',
                kanji='相・続・決・毎'),
    poster_intro='相続の決まりを、「相続人と相続分」（グループA：ア・イ・ウ）と「遺産分割と期間」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='相続の決まりを整理', sub='民法887条から939条まで（毎日ドリル 第33日）',
        col_a='相続人と相続分', col_b='遺産分割と期間', n_a=3,
        cards=[
            dict(h='放棄した人の子は代襲しない',
                 ill='a family tree fragment with a parent figure at the top, a child figure in the middle labeled 「放棄」 and drawn faded, and a grandchild figure at the bottom drawn faded and separated from the parent by a dotted gap. A green check mark sits beside the gap.',
                 words=['放棄'], tag='代襲は起きない'),
            dict(h='父だけ同じ弟は兄の半分',
                 ill='a pie divided into two slices: a large slice labeled 「兄」 and a slice half its size labeled 「弟」. A green check mark sits beside the pie.',
                 words=['兄', '弟'], tag='兄の2分の1'),
            dict(h='兄弟姉妹は甥姪の代で止まる',
                 ill='a family tree fragment with a sibling figure at the top, a nephew figure in the middle, and a grandnephew figure at the bottom drawn faded and cut off by a barrier line. The nephew figure is labeled 「甥姪」. A green check mark sits beside the nephew figure.',
                 words=['甥姪'], tag='再代襲はなし'),
            dict(h='遺産分割でも超える部分は登記が必要',
                 ill='a land plot with a boundary half in blue and half in green. The green half carries a stamp labeled 「登記」. A heir figure stands next to the green half. A green check mark sits beside the stamp.',
                 words=['登記'], tag='対抗には登記'),
            dict(h='三箇月は知った時から数える',
                 ill='a horizontal timeline. On the left a flag labeled 「死亡」; further right a second flag labeled 「知った」. A green bracket labeled 「三箇月」 starts at the second flag and extends to the right. The part of the timeline before the second flag is drawn in gray with no bracket.',
                 words=['死亡', '知った', '三箇月'], tag='起算日は知った時'),
        ],
        kanji='放・棄・兄・弟・甥・姪・登・記・死・亡・知・三・箇・月'.split('・')),
    nb_label='ア・ウ・イ肢', nb_intro='ア・ウとイの補足説明に合わせた2枚です。1枚目は、代襲相続の原因と範囲を早見表にします。2枚目は、配偶者と兄弟姉妹が相続人のときの相続分を、分け方の図で示します。',
    notebooks=[
        dict(name='代襲相続の原因と、再代襲の範囲', args=dict(
            title='代襲相続と再代襲', sub='民法887条と889条（毎日ドリル 第33日 ア・ウ）',
            req='a table',
            layout="""--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Two columns and three data rows. The header row has the column names. Each data row has a small isometric icon at the left of its first cell (a family tree with a faded parent for the first row, a child figure with a grandchild figure for the second row, a sibling figure with a nephew figure for the third row). Use exactly these strings, and no others:
Header row: 場面 | 代襲の範囲
Row 1: 相続の放棄 | 代襲の原因ではない
Row 2: 子の場合 | 孫が代襲し、再代襲もある
Row 3: 兄弟姉妹の場合 | 甥姪が代襲し、再代襲はない
Draw the three right-hand cells in three different accent colors (orange, green and blue) because they are three different strings.""",
            callout='相続の放棄は代襲の原因になりません。放棄した人の子は代襲しません。\n子の場合は再代襲がありますが、兄弟姉妹の場合は甥姪の代で止まります。',
            footer='民法887条、889条、939条',
            kanji='代・襲・相・続・放・棄・孫・甥・姪・兄・弟・姉・妹'.split('・'), what='table',
            check='confirm the table has exactly 2 columns and 3 data rows, confirm the three right-hand cells are in three different accent colors, ')),
        dict(name='配偶者と兄弟姉妹の相続分の計算', args=dict(
            title='相続分を、順に分ける', sub='民法900条（毎日ドリル 第33日 イ）',
            req='a vertical flow diagram',
            layout="""--- FLOW ---
Render as a clean flat-design vertical flow in three steps, connected by small downward arrows with no text.
Step 1 (blue accent): header 配偶者と兄弟姉妹. Content: a bar split into two parts: a large part labeled 配偶者 4分の3 and a small part labeled 兄弟姉妹 4分の1.
Step 2 (green accent): header 兄弟姉妹の中で分ける. Content: two figures, a tall one labeled 兄 (written as 父母の双方が同じ in small text) with the ratio 2, and a short one labeled 弟 (written as 父のみが同じ in small text) with the ratio 1.
Step 3 (orange accent): header 相続分. Content: a bar of twelve equal cells: nine cells labeled 配偶者, two cells labeled 兄, and one cell labeled 弟.
Use exactly these strings, and no others, for the labels.""",
            callout='兄弟姉妹の相続分は、父母の双方が同じ者を1、父母の一方だけが同じ者を2分の1として分けます。\n全体を12に分けると、配偶者が9、兄が2、弟が1です。',
            footer='民法900条3号、4号',
            kanji='配・偶・者・兄・弟・姉・妹・相・続・分・父・母'.split('・'), what='flow',
            check='confirm there are exactly three steps connected by arrows and the final bar has twelve cells (nine, two and one), ')),
    ],
)
