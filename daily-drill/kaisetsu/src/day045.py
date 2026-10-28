D = dict(
    catch='壊しても附属建物が残れば変更の登記',
    intro='建物がなくなったとき、その建物を移したときの登記を、まとめて問う問題です（不動産登記法57条、不動産登記事務取扱手続準則85条・101条・102条）。同じ「取り壊した」でも、建物が全部なくなるのか、附属建物が残るのかで、する登記が変わります。\n\nこの記事では、「滅失の登記」と「主たる建物の滅失による変更の登記」の違いと、建物を動かしたときの扱いを、具体的な場面で確認します。この問題は、正しい記述の組合せを選ぶ形です。',
    sections={
        'ア': ('主たる建物だけ壊すと、滅失ではなく変更の登記',
               '附属建物がある主たる建物が滅失したときは、表題部の登記事項に関する変更の登記をします。主たる建物の表示欄には、主たる建物となるべき附属建物の種類、構造及び床面積を記録します（不動産登記事務取扱手続準則102条）。\n\n建物そのものは附属建物として残っているので、甲建物全体の滅失の登記にはなりません。本肢は正しいといえます。\n\n**たとえば**、同じ敷地に母屋の居宅と倉庫が建っていて、居宅だけを取り壊したとします。倉庫は残るので、倉庫が新しい主たる建物として登記記録に書き直されます。'),
        'イ': ('滅失の登記では、附属建物の欄に日付を書かない',
               '建物の滅失の登記をする場合に、その建物の登記記録に附属建物があるときでも、附属建物の表示欄の原因及びその日付欄には、何も記録しません（不動産登記事務取扱手続準則101条）。\n\n問題文は、附属建物の欄にも取壊しの日付を記録しなければならないとしているので、本肢は誤りです。\n\n**たとえば**、母屋と倉庫をまとめて取り壊して、建物全体の滅失の登記をするときは、倉庫の欄に取壊しの日付を書き入れる必要はありません。主たる建物の欄に書いた原因と日付で、全体の滅失が示されます。'),
        'ウ': ('そのまま動かすのは、滅失と新築ではなく所在の変更',
               '建物をえい行移転した場合は、建物の所在の変更として取り扱います（不動産登記事務取扱手続準則85条2項）。えい行移転とは、建物を壊さず、そのままの状態で別の場所へ引いて動かすことです。\n\n問題文は、滅失の登記と移転後の建物の表題登記を申請するとしているので、本肢は誤りです。これは、建物を解体して移す場合（同条1項）の扱いです。\n\n**たとえば**、道路の拡幅のために、家を壊さずにそのまま奥へ引いて下げたときは、別の建物になったのではなく、同じ建物の所在が変わっただけです。表題部の所在を直す変更の登記をします。'),
        'エ': ('解体して建て直せば、元の建物は滅失する',
               '建物を解体移転した場合は、既存の建物が滅失し、新たな建物が建築されたものとして取り扱います（不動産登記事務取扱手続準則85条1項）。建物が滅失したときは、所有者は、滅失の日から一月以内に滅失の登記を申請しなければなりません（不動産登記法57条）。\n\n材料が同じで、種類、構造及び床面積が同じでも、元の建物と新しい建物は同じ建物として扱われません。本肢は正しいといえます。\n\n**たとえば**、古い家を解体し、その木材を使って別の土地に同じ間取りの家を建てたとします。元の家は滅失の登記、新しい家は表題登記が必要です。'),
        'オ': ('一棟が全部なくなれば、所有者の一人から申請できる',
               '区分建物が属する一棟の建物が全部なくなったときの滅失の登記は、区分建物の所有者のうちの一人から申請できる、という取扱いがあります。この点は、不動産登記法57条に書かれたものではありません。\n\n問題文は、所有者全員が共同してしなければならないとしているので、本肢は誤りです。\n\n**たとえば**、所有者が3人いるマンションが火事で全焼したとします。3人がそろわなくても、そのうちの一人が一棟の滅失の登記を申請できます。'),
    },
    summary=[
        ('ア', '正', '附属建物がある主たる建物が滅失したときは、滅失ではなく表題部の変更の登記をする'),
        ('イ', '誤', '建物の滅失の登記では、附属建物の表示欄の原因及びその日付欄には何も記録しない'),
        ('ウ', '誤', 'えい行移転は所在の変更として扱い、滅失の登記と表題登記は不要'),
        ('エ', '正', '解体移転は、既存の建物が滅失し、新たな建物が建築されたものとして扱う'),
        ('オ', '誤', '一棟の建物の滅失の登記は、区分建物の所有者の一人から申請できる'),
    ],
    summary_tail='アとイは、同じ「取り壊し」でも、附属建物が残るかどうかで記録のしかたが変わる点を取り違えさせる出題です。ウとエは、「壊さずに動かす」か「解体して移す」かが分かれ道です。',
    supplements=[
        '### 補足説明（イ）：滅失の登記と、主たる建物の滅失による変更の登記\n\nどちらも「取り壊した」ときの登記ですが、附属建物の欄の扱いが違います。\n\n| | 建物全体の滅失の登記 | 主たる建物の滅失による変更の登記 |\n|---|---|---|\n| 場面 | 主たる建物も附属建物もなくなる | 主たる建物だけがなくなり、附属建物が残る |\n| 主たる建物の欄 | 滅失の原因と日付 | 滅失の原因と日付を書き、残った附属建物の種類、構造及び床面積に書き直す |\n| 附属建物の欄 | 何も記録しない（準則101条） | 「主たる建物に変更」と記録する（準則102条） |\n\n**たとえば**、居宅と倉庫のうち居宅だけを壊したときは右の列、居宅も倉庫も壊したときは左の列です。倉庫が残るかどうかで見分けます。',
        '### 補足説明（ウ）：解体して移す場合と、そのまま動かす場合\n\n建物を別の場所へ移すときは、壊すかどうかで扱いが分かれます（準則85条）。\n\n- 解体移転（1項）：元の建物は滅失し、新しい建物が建築されたものとする。滅失の登記と表題登記をする。\n- えい行移転（2項）：同じ建物の所在が変わったものとする。所在を直す変更の登記をする。\n\n**たとえば**、家をばらして別の土地で組み立て直せば、新しく建てたのと同じ扱いになります。家を丸ごと引いて動かせば、建物は一つのままで、場所だけが変わった扱いになります。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第45日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法57条と、不動産登記事務取扱手続準則85条（1項・2項）・101条・102条は、`note-articles/laws/` 配下の原文で確認しました。',
        'オ（所有者の異なる区分建物が属する一棟の建物の滅失の登記は、所有者の一人から申請できる）は、条文に書かれたものではなく、先例の取扱いによります。先例の原文は手元にないため未確認で、本文には番号を書いていません。公開前に確認してください。',
        'ウのえい行移転の意味（建物を壊さず、そのままの状態で別の場所へ動かすこと）は、準則85条2項の文言からの一般的な整理です。ウの道路の拡幅の例は、場面を思い描くための例です。',
    ],
    phrases=['居宅だけ壊しても変更の登記です', '滅失の登記は附属建物の欄が空白です', '壊さず動かせば所在の変更です', '解体して建て直せば滅失と新築です', '一棟の滅失は一人から申請できます'],
    header=dict(t1='壊したら、', t2='滅失？変更？', topic='不動産登記　建物の滅失',
                kanji='壊・滅・失・変・更・建・物・登・記'),
    poster_intro='建物の滅失とその関連の登記を、「滅失の登記の記録のしかた」（グループA：ア・イ）と「移転と一棟の滅失」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='建物の滅失と関連の登記を整理', sub='不動産登記法 第57条ほか（毎日ドリル 第45日）',
        col_a='滅失の登記の記録', col_b='移転と一棟の滅失', n_a=2,
        cards=[
            dict(h='居宅だけ壊すと変更の登記',
                 ill='an isometric site with a main house drawn faded and crossed out on the left, and a small warehouse standing on the right. A thin arrow runs from the warehouse to a record sheet labeled 「主たる建物」. A green check mark sits beside the record sheet.',
                 words=['主たる建物'], tag='倉庫が主たる建物に'),
            dict(h='滅失の登記は附属建物の欄が空白',
                 ill='a record sheet with two rows labeled 「主たる建物」 and 「附属建物」. A round stamp labeled 「滅失」 sits on the first row. The second row is left blank. A green check mark sits beside the blank row.',
                 words=['主たる建物', '附属建物', '滅失'], tag='附属建物の欄は記録不要'),
            dict(h='壊さず動かせば所在の変更',
                 ill='an isometric house resting on wooden rollers, being pulled from one land plot to the neighboring plot, with a dotted outline showing the old position. A small sign beside the house is labeled 「所在の変更」. A green check mark sits beside the sign.',
                 words=['所在の変更'], tag='えい行移転'),
            dict(h='解体して建て直せば滅失と新築',
                 ill='on the left, a pile of timber beams where a house used to stand, with a stamp labeled 「滅失」. On the right, a new house of the same shape on another land plot, with a stamp labeled 「新築」. A thin arrow runs from the timber to the new house. A green check mark sits beside the new house.',
                 words=['滅失', '新築'], tag='元の建物は滅失'),
            dict(h='一棟の滅失は所有者の一人から申請',
                 ill='an isometric apartment building that has burned down to its outline, and three owner figures standing in front of it. One of the figures steps forward holding a form labeled 「滅失」. A green check mark sits beside the figure who steps forward.',
                 words=['滅失'], tag='全員でなくてよい'),
        ],
        kanji='滅・失・壊・主・建・物・附・属・所・在・変・更・新・築・棟・有・者・申・請'.split('・')),
    nb_label='イ・ウ肢', nb_intro='イ・ウの補足説明に合わせた2枚です。1枚目は、建物全体の滅失の登記と、主たる建物の滅失による変更の登記を、附属建物の欄の扱いで対比します。2枚目は、解体移転とえい行移転の違いを左右の対比で示します。',
    notebooks=[
        dict(name='滅失の登記と、主たる建物の滅失による変更の登記', args=dict(
            title='附属建物の欄の記録は、どう違う？', sub='滅失の登記と変更の登記（毎日ドリル 第45日 イ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings. The left header is 建物全体の滅失の登記 and the right header is 主たる建物の滅失による変更の登記. Draw them in different accent colors (blue on the left and green on the right) so they can never be confused or duplicated. Neither panel uses a cross mark.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 建物全体の滅失の登記
Scene: an isometric scene of a main house and a warehouse that are both crossed out. Below it, a small record sheet with two rows: the row 主たる建物 carries a stamp 滅失, and the row 附属建物 is blank.
Result badge: 附属建物の欄は何も記録しない

RIGHT PANEL (green accent):
Panel header: 主たる建物の滅失による変更の登記
Scene: an isometric scene of a main house that is crossed out and a warehouse that is still standing. Below it, a small record sheet with two rows: the row 主たる建物 shows the warehouse as the new main building, and the row 附属建物 carries the words 主たる建物に変更.
Result badge: 附属建物の欄に「主たる建物に変更」と記録""",
            callout='同じ「取り壊した」でも、附属建物が残るかどうかで登記が変わります。\n全部なくなれば附属建物の欄は空白、附属建物が残れば、その欄に「主たる建物に変更」と記録します。',
            footer='不動産登記事務取扱手続準則101条・102条',
            kanji='滅・失・変・更・建・物・登・記・属・取・壊・欄・録'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (建物全体の滅失の登記 on the left and 主たる建物の滅失による変更の登記 on the right) in different accent colors, ')),
        dict(name='解体移転とえい行移転の違い', args=dict(
            title='壊して移す？そのまま動かす？', sub='解体移転とえい行移転（毎日ドリル 第45日 ウ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings. The left header is 解体移転 and the right header is えい行移転. Draw them in different accent colors (orange on the left and blue on the right) so they can never be confused or duplicated. Neither panel uses a cross mark.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (orange accent):
Panel header: 解体移転
Scene: an isometric scene of a house taken apart into beams on one land plot, and a new house built from the beams on another land plot.
Result badge: 滅失の登記と表題登記

RIGHT PANEL (blue accent):
Panel header: えい行移転
Scene: an isometric scene of one house on wooden rollers being pulled from one land plot to another, drawn as the same house with a dotted outline of the old position.
Result badge: 所在の変更の登記""",
            callout='建物を壊して移せば、元の建物は滅失し、新しい建物が建ったものとして扱われます。\n壊さずにそのまま動かしたときは、同じ建物の所在が変わっただけです。',
            footer='不動産登記事務取扱手続準則85条',
            kanji='解・体・移・転・滅・失・登・記・表・題・所・在・変・更'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (解体移転 on the left and えい行移転 on the right) in different accent colors, ')),
    ],
)
