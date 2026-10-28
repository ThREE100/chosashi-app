D = dict(
    catch='管轄がまたがるとき、除斥の範囲',
    intro='登記所の管轄がまたがる場合や移る場合、登記官の除斥について問う問題です（不動産登記法6条・10条、不動産登記規則40条、不動産登記事務取扱手続準則4条・5条）。\n\nこの記事では、「またがる」と「移る」の違い、除斥される範囲を、具体的な場面で確認していきましょう。問題は、正しい記述の組合せを選ぶ形です。',
    sections={
        'ア': ('増築で別の区域にまたがっても、管轄はもとの登記所のまま',
               '甲登記所で登記されている建物が、増築や附属建物の新築によって、乙登記所の管轄区域にまたがることになった場合でも、その建物の管轄登記所は甲登記所のままです（不動産登記事務取扱手続準則5条）。\n\n本肢は正しいといえます。\n\n**たとえば**、甲登記所の区域にある建物を、区域の境の向こう側へ広げる増築をしたとします。この建物の登記事務は、これまでどおり甲登記所が扱います。'),
        'イ': ('離婚した元の配偶者が申請人でも、登記官は登記できない',
               '登記官又はその配偶者若しくは四親等内の親族（配偶者又は四親等内の親族であった者を含みます）が登記の申請人であるときは、その登記官は、その登記をすることができません（不動産登記法10条）。\n\n問題文は、5年前に離婚した元の配偶者が申請人のときも登記できるとしているので、本肢は誤りです。\n\n**たとえば**、登記官Xが5年前に離婚していても、元の配偶者は「配偶者であった者」に当たります。元の配偶者が申請人の建物の表題登記は、Xはすることができません。'),
        'ウ': ('四親等内の親族が会社を代表して申請するときも、登記できない',
               '登記官の配偶者又は四親等内の親族が、申請人を代表して申請するときも、その登記官は登記をすることができません（不動産登記法10条後段）。\n\n本肢のBは、登記官Xのおい（三親等）で、申請人の株式会社を代表して申請しています。Xは、その登記をすることができません。本肢は正しいといえます。\n\n**たとえば**、申請人が会社で、登記官本人とは何の関係もなくても、会社の代表者がおいやめいにあたる場合は、除斥の対象になります。'),
        'エ': ('指定の前に申請を受けた登記所は、事件を移送する',
               '不動産が二以上の登記所の管轄区域にまたがる場合、管轄登記所が指定されるまでの間は、そのうちの一つの登記所に登記の申請ができます（不動産登記法6条3項）。\n\nその後、他の登記所が管轄登記所に指定されたときは、申請を受けた登記所の登記官は、事件を指定された登記所に移送します（不動産登記規則40条1項）。\n\n問題文は「却下しなければならない」としているので、本肢は誤りです。\n\n**たとえば**、甲乙二つの登記所にまたがる土地の分筆を、乙登記所に申請した後、甲登記所が管轄登記所に指定されたとします。乙登記所は申請を却下せず、事件を甲登記所に移します。'),
        'オ': ('えい行移転で全体が別の区域に移れば、移転先の登記所が取り扱う',
               '表題登記がある建物が、えい行移転（建物を取り壊さずに他の土地へ移すこと）によって、甲登記所の管轄区域から乙登記所の管轄区域に移動した場合、不動産所在事項に関する変更の登記は、乙登記所が管轄登記所として取り扱います（不動産登記事務取扱手続準則4条1項）。\n\n問題文は「甲登記所が取り扱う」としているので、本肢は誤りです。\n\n**たとえば**、建物を丸ごと別の土地へ引いて移し、新しい場所が乙登記所の区域だったときは、移った先の乙登記所が取り扱います。'),
    },
    summary=[
        ('ア', '正', '増築などで別の登記所の区域にまたがっても、管轄登記所はもとの甲登記所のまま'),
        ('イ', '誤', '10条の除斥には、配偶者であった者も含まれるので、離婚した元の配偶者が申請人でも登記できない'),
        ('ウ', '正', '四親等内の親族が申請人を代表して申請するときも、登記官は登記できない'),
        ('エ', '誤', '指定の前に申請を受けた登記所は、却下ではなく、指定された登記所に事件を移送する'),
        ('オ', '誤', '建物が全体として別の区域に移動したときは、移転先の乙登記所が取り扱う'),
    ],
    summary_tail='イは「かっこ書きの見落とし」、エは「却下と移送のすり替え」、オは「またがる場合と移る場合の取り違え」の出題です。管轄は、またがるのか、移るのかを見分けましょう。',
    supplements=[
        '### 補足説明（イ・ウ）：登記官が登記できない範囲\n\n登記官は、自分に近い人が関わる登記をすることができません（不動産登記法10条）。範囲は次のとおりです。\n\n- 登記官本人が申請人であるとき。\n- 登記官の配偶者又は四親等内の親族が申請人であるとき（元の配偶者や元の親族も含む）。\n- 登記官の配偶者又は四親等内の親族が、申請人を代表して申請するとき。\n\n**たとえば**、申請人が会社でも、その代表取締役が登記官のおいなら、登記官はその登記ができません。おいは三親等なので、四親等内に入ります。',
        '### 補足説明（ア・エ・オ）：管轄がまたがる、移る、指定される\n\n管轄に関わる3つの場面は、結論が違います。\n\n- 増築などで別の区域にまたがる：もとの登記所のまま（準則5条）。\n- えい行移転で全体が別の区域に移る：移転先の登記所（準則4条1項）。\n- 管轄登記所の指定前に申請し、後から別の登記所が指定された：指定された登記所に移送（規則40条1項）。\n\n**たとえば**、広げるだけなら「もとのまま」、丸ごと動けば「移った先」、申請先が後から変わるなら「指定された登記所へ移送」です。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第23日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法6条、10条、不動産登記規則40条、不動産登記事務取扱手続準則4条、5条は、`note-articles/laws/` 配下の原文で確認しました。',
        'ウの具体例（会社の代表者が登記官のおいにあたる場合）は、10条後段の文言をかみ砕いた説明です。親等の数え方（おいは三親等）は民法の一般的な整理で、民法の条文は確認していません。',
        'ア・エ・オの具体例（増築、分筆の申請先、建物の引き移し）は、条文の文言から導いた一般的な説明です。個別の運用・先例の確認はしていません。',
    ],
    phrases=['増築でまたがってももとの登記所です', '離婚した元の配偶者も除斥の対象です', '親族が代表して申請しても除斥です', '指定前の申請は移送され、却下されません', 'えい行移転で移れば移転先が取り扱います'],
    header=dict(t1='管轄はどこ？', t2='除斥されるのは？', topic='不動産登記法　登記所と登記官',
                kanji='管・轄・除・斥・登・記・所・官'),
    poster_intro='登記所と登記官に関する決まりを、「管轄と除斥」（グループA：ア・イ・ウ）と「移送と移転」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='登記所と登記官を整理', sub='不動産登記法第6条と第10条ほか（毎日ドリル 第23日）',
        col_a='管轄と除斥', col_b='移送と移転', n_a=3,
        cards=[
            dict(h='増築で区域をまたいでも管轄は変わらない',
                 ill='a house extended across a dotted line that divides two district areas. A small office building labeled 「甲登記所」 on the left side is highlighted with a green glow. A green check mark sits beside the office building.',
                 words=['甲登記所'], tag='もとの登記所のまま'),
            dict(h='離婚した元の配偶者も除斥の対象',
                 ill='a registry officer figure on the left and a second person figure on the right, with a thin broken ring icon between them. A tag labeled 「除斥」 is attached to the registry officer figure. A green check mark sits beside the tag.',
                 words=['除斥'], tag='配偶者であった者を含む'),
            dict(h='親族が代表して申請しても除斥',
                 ill='a registry officer figure on the left and a company building on the right with a representative figure in front of it carrying a name tag labeled 「代表取締役」 and holding a form. A thin line connects the officer figure to the representative figure. A green check mark sits beside the line.',
                 words=['代表取締役'], tag='四親等内の親族が代表'),
            dict(h='指定前の申請は指定された登記所へ移送',
                 ill='a file folder moving along a thin arrow from a small office building labeled 「乙登記所」 on the left to a second office building labeled 「甲登記所」 on the right. A green check mark sits beside the second office building.',
                 words=['乙登記所', '甲登記所'], tag='却下ではなく移送'),
            dict(h='全体が移れば移転先の登記所が管轄',
                 ill='a house on rollers being pulled across a dotted line that divides two district areas, from the left area to the right area. A small office building labeled 「乙登記所」 on the right side is highlighted with a green glow. A green check mark sits beside it.',
                 words=['乙登記所'], tag='移った先の登記所'),
        ],
        kanji='増・築・区・域・登・記・所・除・斥・配・偶・者・親・族・代・表・移・送・指・定・転'.split('・')),
    nb_label='ア・イ・ウ・エ・オ肢', nb_intro='補足説明に合わせた2枚です。1枚目は、登記官が登記できない範囲を表で整理します。2枚目は、管轄に関わる3つの場面を表で整理します。',
    notebooks=[
        dict(name='登記官が登記できない範囲', args=dict(
            title='登記官が登記できないのは？', sub='除斥される範囲（毎日ドリル 第23日 イ・ウ）',
            req='a table',
            layout="""--- TABLE ---
Render as a clean table with 2 columns and 3 data rows, plus a header row. The column headers are exactly: 登記官との関係 / 具体例. Each row has a small isometric icon beside the first cell.
Row 1: first cell 配偶者であった者を含む (icon: a broken ring); second cell 離婚した元の配偶者.
Row 2: first cell 四親等内の親族 (icon: a family tree-shaped set of three person figures connected by lines); second cell おい（三親等）.
Row 3: first cell 申請人を代表して申請 (icon: a person figure holding a form in front of a company building); second cell 会社の代表者がおい.
Use exactly these strings, and no others, for the cell text. The three 具体例 cells are different strings; draw each of them in a different accent color (blue, green and orange).""",
            callout='登記官は、自分の配偶者や四親等内の親族が申請人であるとき、登記ができません。\n元の配偶者や元の親族も含まれ、親族が申請人を代表して申請する場合も同じです。',
            footer='不動産登記法10条',
            kanji='登・記・官・関・係・配・偶・者・四・親・等・内・族・申・請・人・代・表・具・体・例・会・社'.split('・'), what='table',
            check='confirm the table has exactly 2 columns and 3 data rows, and confirm the three cells in the 具体例 column are different strings drawn in different accent colors, ')),
        dict(name='管轄がまたがる、移る、指定される', args=dict(
            title='管轄は、どう変わる？', sub='またがる、移る、指定される（毎日ドリル 第23日 ア・エ・オ）',
            req='a table',
            layout="""--- TABLE ---
Render as a clean table with 2 columns and 3 data rows, plus a header row. The column headers are exactly: 場面 / 取扱い. Each row has a small isometric icon beside the first cell.
Row 1: first cell 増築で別の区域にまたがる (icon: a house extended across a dotted line); second cell もとの登記所のまま.
Row 2: first cell えい行移転で全体が移る (icon: a house on rollers); second cell 移転先の登記所.
Row 3: first cell 指定の前に申請して後から指定 (icon: a file folder with an arrow); second cell 指定された登記所に移送.
Use exactly these strings, and no others, for the cell text. The three 取扱い cells are different strings; draw each of them in a different accent color (blue, green and orange).""",
            callout='増築などで区域をまたいでも、管轄はもとの登記所のままです。\nえい行移転で全体が移れば移転先の登記所が取り扱い、指定の前に申請を受けた登記所は、指定された登記所に事件を移送します。',
            footer='準則4条1項、5条、不動産登記規則40条1項',
            kanji='増・築・区・域・登・記・所・移・転・全・体・指・定・申・請・場・面・取・扱・送'.split('・'), what='table',
            check='confirm the table has exactly 2 columns and 3 data rows, and confirm the three cells in the 取扱い column are different strings drawn in different accent colors, ')),
    ],
)
