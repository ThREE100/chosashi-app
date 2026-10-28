D = dict(
    catch='代位できるのは、前提として必要なときだけ',
    intro='他人に代わってする登記の申請（代位による申請）と、相続人による表示に関する登記の申請を問う問題です（不動産登記法30条・48条、不動産登記令3条・7条、不動産登記規則183条）。\n\nどんな場面なら他人に代わって申請できるのか、申請後の通知や添付する情報はどうなるのかを確かめます。この問題は、正しい記述の組合せを選ぶ形です。',
    sections={
        'ア': ('仮処分を得た人は、前提となる分筆を代位して申請できる',
               '土地の一部について処分禁止の仮処分の登記をするには、その一部を独立した一筆にする分筆の登記が前提として必要です。そこで、仮処分命令を得た人は、所有権の登記名義人に代わって、分筆の登記を申請できるという取扱いがあります。\n\n代位して申請するときは、代位原因を証する情報を提供します（不動産登記令7条1項3号）。仮処分命令の正本が、これにあたります。本肢は正しい記述です。\n\n**たとえば**、Aの土地の東半分についてBが仮処分命令を得たとします。Bは、東半分を切り分ける分筆の登記を、Aに代わって申請できます。'),
        'イ': ('地役権者は、分筆を代位して申請できない',
               '地役権は、承役地の一部についても設定できます。地役権の登記には、地役権設定の目的及び範囲が登記されるためです（不動産登記法80条1項2号）。土地を分筆しなくても、地役権の設定の登記は受けられます。\n\nそのため、分筆が前提として必要とはいえず、地役権者が代位して分筆の登記を申請することはできません。本肢は誤りです。\n\n**たとえば**、Aの土地の一部を通路として通らせてもらう権利をBが得たとします。Bは、土地を分筆しなくても、通路にあたる範囲を示して地役権の登記を受けられます。'),
        'ウ': ('新築した区分建物の所有者は、既存の建物の変更も申請できる',
               '表題登記がある建物（区分建物を除く）に接続して区分建物が新築されたときは、その区分建物の表題登記を、既存の建物の表題部の変更の登記と併せて申請しなければなりません（不動産登記法48条3項）。\n\nこの場合、新築した区分建物の所有者は、既存の建物の表題部所有者に代わって、表題部の変更の登記を申請できます（同条4項）。\n\n本肢は正しい記述です。\n\n**たとえば**、Bの建物に接続してAが区分建物を新築し、全体が区分建物の関係になったとします。Aは、Bに代わって、Bの建物の表題部の変更の登記も申請できます。'),
        'エ': ('代位による登記が完了したら、代位された本人に通知する',
               '民法423条その他の法令の規定により他人に代わってする申請に基づく登記を完了したときは、登記官は、その他人に対して、登記が完了した旨を通知しなければなりません（不動産登記規則183条1項2号）。\n\n問題文は、申請人であるBに登記完了証を交付すれば足り、Aに通知することを要しないとしているので、本肢は誤りです。\n\n**たとえば**、BがAに代わって分筆の登記を申請したときは、登記が完了した旨が、代位された側のAにも通知されます。'),
        'オ': ('相続人が申請するときは、相続を証する情報も必要',
               '表題部所有者の相続人は、不動産登記法30条により、表示に関する登記を申請できます。申請情報には、相続人である旨を書きます（不動産登記令3条10号）。\n\nさらに、相続その他の一般承継があったことを証する市町村長、登記官その他の公務員が職務上作成した情報を、添付情報として提供しなければなりません（同令7条1項4号）。\n\n問題文は、この情報を提供することを要しないとしているので、本肢は誤りです。\n\n**たとえば**、亡くなった父の名義の建物の種類を、子が変更の登記で直すときは、子であることを示す戸籍の謄本などを添付します。'),
    },
    summary=[
        ('ア', '正', '土地の一部の仮処分を得た人は、前提となる分筆の登記を代位して申請できる'),
        ('イ', '誤', '地役権は土地の一部にも設定できるので、地役権者は分筆の登記を代位して申請できない'),
        ('ウ', '正', '区分建物の新築者は、既存の建物の所有者に代わって、その表題部の変更の登記を申請できる'),
        ('エ', '誤', '代位による登記を完了したら、登記官は代位された本人に完了を通知する'),
        ('オ', '誤', '相続人が申請するときは、申請情報に相続人である旨を書き、相続を証する情報も提供する'),
    ],
    summary_tail='アとイは、前提として分筆が必要かどうかで分かれます。エは通知の相手、オは添付情報の見落としを狙った出題です。代位や相続人の申請は、通知と添付情報までセットで覚えましょう。',
    supplements=[
        '### 補足説明（イ）：代位して分筆を申請できる場合、できない場合\n\n代位して分筆の登記を申請できるのは、自分の登記をするために、分筆が前提として必要なときです。\n\n| 場面 | 分筆が前提として必要か | 代位して分筆を申請できるか |\n|---|---|---|\n| 土地の一部の処分禁止の仮処分 | 必要（一部だけでは登記できない） | できる |\n| 土地の一部の地役権の設定 | 不要（範囲を示して登記できる） | できない |\n\n**たとえば**、土地の東半分だけに仮処分の登記をするには、東半分が独立した一筆になっていないといけません。地役権は、一部の範囲を示して登記できるので、分筆は要りません。',
        '### 補足説明（エ・オ）：代位申請の通知と、相続人による申請の添付情報\n\n代位による申請と相続人による申請では、手続のどこかに追加の決まりがあります。\n\n| 場面 | 追加の決まり | 根拠 |\n|---|---|---|\n| 代位による申請の登記が完了した | 代位された本人に完了を通知する | 規則183条1項2号 |\n| 代位して申請する | 代位原因を証する情報を提供する | 令7条1項3号 |\n| 相続人が表示に関する登記を申請する | 申請情報に相続人である旨を書く | 令3条10号 |\n| 同上 | 相続を証する公務員作成の情報を提供する | 令7条1項4号 |\n\n**たとえば**、BがAに代わって申請したときは、完了後にAへ通知が届きます。子が亡父の名義で申請するときは、相続を示す書類が必要です。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第53日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法30条・48条3項・4項・80条1項2号、不動産登記令3条10号・7条1項3号・4号、不動産登記規則183条1項は、`note-articles/laws/` 配下の原文で確認しました。',
        'ア（土地の一部の仮処分を得た人が分筆を代位できる）とイ（地役権者は分筆を代位できない）は、条文に直接書かれたものではなく、先例の取扱いと代位の考え方に基づきます。先例の原文は手元にないため未確認で、本文には番号を書いていません。公開前に確認してください。',
        'イについて、地役権が土地の一部にも設定できる点は、法80条1項2号（地役権設定の目的及び範囲を登記する）からの一般的な整理です。具体例（通路の地役権、東半分の仮処分）は、場面を思い描くための例です。',
    ],
    phrases=['仮処分の前提の分筆は代位できます', '地役権は分筆しなくても登記できます', '新築した人が既存の建物も申請できます', '代位した登記は本人に通知されます', '相続人の申請には相続の書類がいります'],
    header=dict(t1='代わりに申請、', t2='どこまで？', topic='不動産登記　代位による申請',
                kanji='代・位・申・請・登・記'),
    poster_intro='代位による申請と相続人による申請を、「代位して申請できるか」（グループA：ア・イ・ウ）と「通知と添付情報」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='代位による申請を整理', sub='不動産登記法 第30条と第48条ほか（毎日ドリル 第53日）',
        col_a='代位して申請できるか', col_b='通知と添付情報', n_a=3,
        cards=[
            dict(h='仮処分を得た人は分筆を代位できる',
                 ill='an isometric land plot whose east half is shaded and has a boundary line drawn through it. A creditor figure holds a sheet labeled 「仮処分」 and a thin arrow points from the sheet to the shaded half. A green check mark sits beside the sheet.',
                 words=['仮処分'], tag='前提として必要'),
            dict(h='地役権者は分筆を代位できない',
                 ill='an isometric land plot with a narrow path drawn across part of it, with no dividing line. A signboard beside the path is labeled 「地役権」. A green check mark sits beside the unsplit plot.',
                 words=['地役権'], tag='分筆しなくても登記可'),
            dict(h='新築した人が既存の建物も申請できる',
                 ill='an existing building connected by a short corridor to a newly built unit. A sheet labeled 「表題部の変更」 is held up by the owner of the new unit. A green check mark sits beside the sheet.',
                 words=['表題部の変更'], tag='併せて申請する'),
            dict(h='代位の完了は本人に通知される',
                 ill='a registry officer figure sending a notice sheet labeled 「通知」 toward an owner figure who stands in the background. A green check mark sits beside the notice sheet.',
                 words=['通知'], tag='代位された人に通知'),
            dict(h='相続人の申請には相続の書類が必要',
                 ill='an heir figure at a desk holding a form with a family record sheet labeled 「戸籍」 clipped to it. A green check mark sits beside the family record sheet.',
                 words=['戸籍'], tag='相続を証する情報'),
        ],
        kanji='仮・処・分・地・役・権・表・題・部・変・更・通・知・戸・籍'.split('・')),
    nb_label='イ・エ・オ肢', nb_intro='イ・エ・オの補足説明に合わせた2枚です。1枚目は、代位して分筆を申請できる場合とできない場合を左右の対比で示します。2枚目は、代位申請の通知と相続人による申請の添付情報を、表で整理します。',
    notebooks=[
        dict(name='代位して分筆を申請できる場合、できない場合', args=dict(
            title='分筆は、代位で申請できる？', sub='土地の一部と代位による分筆（毎日ドリル 第53日 イ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two sides must show OPPOSITE marks, not the same mark. The left side shows a green check mark; the right side shows a red cross. The two panel headers are different strings: 一部の仮処分 on the left and 一部の地役権 on the right; draw them in different accent colors (blue and orange) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 一部の仮処分
Scene: an isometric scene of a land plot whose half is shaded with a dividing line, and a creditor figure holding a sheet labeled 仮処分.
Result badges (stacked): 分筆が前提として必要 | 代位して分筆を申請できる
The result uses a green check mark.

RIGHT PANEL (orange accent):
Panel header: 一部の地役権
Scene: an isometric scene of a land plot with a narrow path across it and no dividing line.
Result badges (stacked): 範囲を示して登記できる | 代位して分筆は申請できない
The result uses a red cross.""",
            callout='自分の登記をするために分筆が前提として必要なときだけ、代位して分筆を申請できます。\n地役権は土地の一部の範囲を示して登記できるので、分筆は前提になりません。',
            footer='不動産登記法80条1項2号',
            kanji='一・部・仮・処・分・地・役・権・範・囲・示・登・記・代・位・筆・申・請'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (一部の仮処分 on the left and 一部の地役権 on the right) and that the left panel shows a green check mark while the right panel shows a red cross, ')),
        dict(name='代位申請の通知と相続人の添付情報', args=dict(
            title='通知と添付情報の決まり', sub='代位による申請と相続人による申請（毎日ドリル 第53日 エ・オ）',
            req='a table diagram',
            layout="""--- TABLE ---
Render as a clean flat-design table in the upper half, with four rows and two columns, and a small isometric icon at the left of each row.
Column headers: 場面 | 追加の決まり
Row 1 (blue accent), icon: a notice sheet sent to an owner figure. Cells: 代位による申請の登記が完了した | 代位された本人に完了を通知する
Row 2 (green accent), icon: a creditor figure holding a court order sheet. Cells: 代位して申請する | 代位原因を証する情報を提供する
Row 3 (orange accent), icon: an heir figure at a desk. Cells: 相続人が表示に関する登記を申請する | 申請情報に相続人である旨を書く
Row 4 (gray accent), icon: a family record sheet. Cells: 同上 | 相続を証する公務員作成の情報を提供する
Use exactly these strings, and no others, for the table text. Each row has its own accent color so the rows are never confused or duplicated.""",
            callout='代位による申請が完了すると、登記官は代位された本人に完了を通知します。\n相続人が申請するときは、相続人である旨を書き、相続を証する情報も提供します。',
            footer='不動産登記規則183条、不動産登記令3条・7条',
            kanji='場・面・追・加・決・代・位・申・請・登・記・完・了・通・知・相・続・原・因・証・情・報・表・示・書・提・供'.split('・'), what='table',
            check='confirm the four rows carry four different condition strings in different accent colors, ')),
    ],
)
