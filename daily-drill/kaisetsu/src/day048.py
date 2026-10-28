D = dict(
    catch='まとめて申請できる場合と、添付情報の省略',
    intro='登記を申請するときの「申請情報」と「添付情報」の作り方を問う問題です（不動産登記令4条・7条、不動産登記規則35条〜37条）。何をまとめて申請できるのか、添付する書類はいつまで有効か、同時に申請するときは共通の書類をどうするかを確かめます。\n\nこの問題は、誤っている記述の組合せを選ぶ形です。誤りの肢は、申請できないと言い切ったり、省略できないと言い切ったりしています。',
    sections={
        'ア': ('登記事項証明書は、作成後三月以内のもの',
               '法人が会社法人等番号を提供しない場合は、代表者の資格を証する登記事項証明書を提供します。この登記事項証明書は、その作成後三月以内のものでなければなりません（不動産登記規則36条1項・2項）。\n\n本肢は正しい記述です。\n\n**たとえば**、株式会社が土地の登記を申請するとき、会社法人等番号を書かない代わりに登記事項証明書を付けるなら、半年前に取った古いものは使えません。直近三月以内に取ったものを用意します。'),
        'イ': ('地目の変更と分筆は、一の申請情報でできる',
               '申請情報は、登記の目的及び登記原因に応じ、一の不動産ごとに作成するのが原則です（不動産登記令4条）。ただし、同一の不動産について申請する表題部の変更の登記と、土地の分筆の登記は、一の申請情報で申請することができます（不動産登記規則35条7号）。\n\n問題文は、これらを一の申請情報によって申請することはできないとしているので、本肢は誤りです。\n\n**たとえば**、畑だった土地の一部を駐車場にして、地目の変更の登記と、その部分を切り分ける分筆の登記をするときは、まとめて一通の申請で足ります。'),
        'ウ': ('相続人が申請するときは、相続を証する情報が必要',
               '相続人などの一般承継人が、不動産登記法30条により表示に関する登記を申請するときは、相続その他の一般承継があったことを証する市町村長、登記官その他の公務員が職務上作成した情報を提供しなければなりません（不動産登記令7条1項4号）。\n\n本肢は正しい記述です。\n\n**たとえば**、土地の所有者Aが亡くなり、相続人のBが地目の変更の登記を申請するときは、BがAの相続人であることを示す戸籍の謄本などを添付します。'),
        'エ': ('同時に申請するときは、共通の添付情報は一つでよい',
               '同一の登記所に同時に二以上の申請をする場合に、各申請に共通する添付情報があるときは、その添付情報は、一の申請の申請情報と併せて提供すれば足ります（不動産登記規則37条1項）。\n\n問題文は、各申請の申請情報と併せてそれぞれ提供しなければならないとしているので、本肢は誤りです。\n\n**たとえば**、同じ依頼者の代理人が、甲土地の分筆の登記と乙土地の地目の変更の登記を同時に申請します。委任状が共通なら、委任状は一方に付ければ足ります。'),
        'オ': ('目的と原因と日付が同じなら、複数の土地を一通で',
               '同一の登記所の管轄区域内にある二以上の不動産について申請する登記の目的並びに登記原因及びその日付が同一であるときは、一の申請情報で申請することができます（不動産登記令4条ただし書）。\n\n本肢は正しい記述です。\n\n**たとえば**、隣り合う甲土地と乙土地が、同じ日に畑から宅地になったとします。どちらも地目の変更の登記で、原因も日付も同じなので、一通の申請で済ませられます。'),
    },
    summary=[
        ('ア', '正', '会社法人等番号を提供しない法人の登記事項証明書は、作成後三月以内のものでなければならない'),
        ('イ', '誤', '地目の変更の登記と分筆の登記は、一の申請情報で申請することができる'),
        ('ウ', '正', '相続人が表示に関する登記を申請するときは、相続を証する公務員作成の情報を提供する'),
        ('エ', '誤', '同時に申請する場合の共通の添付情報は、一の申請の申請情報と併せて提供すれば足りる'),
        ('オ', '正', '目的と原因と日付が同一なら、同じ登記所の複数の不動産を一の申請情報で申請できる'),
    ],
    summary_tail='イとエは、できる場合を「できない」「そのつど必要」と言い切らせる出題です。申請は不動産ごとが原則ですが、例外として一つにまとめられる場面があります。',
    supplements=[
        '### 補足説明（イ）：一の申請情報で申請できる場合\n\n申請情報は、一の不動産ごとに作るのが原則です。例外として、まとめられる場合が決まっています。\n\n| 場面 | まとめられるか | 根拠 |\n|---|---|---|\n| 同じ不動産の地目の変更と分筆 | まとめられる | 規則35条7号 |\n| 同じ不動産の表題部の変更の登記が二つ以上 | まとめられる | 規則35条6号 |\n| 二以上の土地で、目的と原因と日付が同一 | まとめられる | 令4条ただし書 |\n\n**たとえば**、一つの土地について、地目の変更の登記と分筆の登記をする場合は、まとめて一通で足ります。',
        '### 補足説明（エ）：同時に申請するときの添付情報\n\n同じ登記所に、同時に複数の申請をするときの、共通の添付情報の扱いです（不動産登記規則37条）。\n\n- 共通する添付情報は、一の申請の申請情報と併せて提供すれば足りる（1項）。\n- その場合、他の申請の申請情報には、併せて提供した旨を書く（2項）。\n\n**たとえば**、甲土地の分筆と乙土地の地目の変更を同時に申請し、委任状が共通なら、委任状は甲土地の申請に付けます。乙土地の申請には、「委任状は甲土地の申請に添付した」と書きます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第48日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記令4条・7条1項4号、不動産登記規則35条6号・7号、36条1項・2項、37条1項・2項は、`note-articles/laws/` 配下の原文で確認しました。',
        'ア・ウ・エ・オの具体例（半年前の登記事項証明書、戸籍の謄本、委任状の共通化）は、条文の言葉を場面に置き換えた例です。戸籍の謄本が相続を証する情報の代表例であることは、条文からの一般的な整理です。',
        'エの補足説明にある、他の申請の申請情報に「添付した旨」を書く点は、規則37条2項の文言に基づきます。書き方の文例は、場面を思い描くための例です。',
    ],
    phrases=['登記事項証明書は三月以内のものです', '地目の変更と分筆は一通でできます', '相続人は相続を証する情報を付けます', '共通の添付情報は一つでいいんです', '同じ目的と原因なら一通で申請できます'],
    header=dict(t1='申請書は、', t2='まとめられる？', topic='不動産登記　申請と添付情報',
                kanji='申・請・添・付・情・報'),
    poster_intro='登記の申請情報と添付情報を、「法人の証明書と申請のまとめ方」（グループA：ア・イ）と「相続人・共通の添付・複数の土地」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='申請情報と添付情報を整理', sub='不動産登記令と不動産登記規則（毎日ドリル 第48日）',
        col_a='法人の証明書と申請のまとめ方', col_b='相続人と共通の添付と複数の土地', n_a=2,
        cards=[
            dict(h='登記事項証明書は三月以内のもの',
                 ill='a company building on the left and a certificate sheet in the center labeled 「登記事項証明書」. A calendar page beside the sheet is labeled 「三月以内」. A green check mark sits beside the calendar page.',
                 words=['登記事項証明書', '三月以内'], tag='作成後三月以内'),
            dict(h='地目の変更と分筆は一通でできる',
                 ill='a single application sheet in the center, with two small icons stacked on it: a field turning into a parking lot, and a land plot split by a line. A round stamp labeled 「一通」 sits beside the sheet. A green check mark sits beside the stamp.',
                 words=['一通'], tag='同一の不動産'),
            dict(h='相続人の申請は相続を証する情報を添付',
                 ill='an isometric scene of an heir figure at a desk holding a form, with a family record sheet labeled 「戸籍」 clipped to the form. A green check mark sits beside the family record sheet.',
                 words=['戸籍'], tag='相続を証する情報'),
            dict(h='共通の添付情報は一つでよい',
                 ill='two application sheets side by side, with a single power-of-attorney sheet labeled 「委任状」 attached to the left one and a thin dotted arrow pointing from the right sheet to it. A green check mark sits beside the power-of-attorney sheet.',
                 words=['委任状'], tag='併せて提供すれば足りる'),
            dict(h='目的と原因と日付が同じなら一通',
                 ill='two neighboring land plots on the left, both turning from a field into a house lot, and a single application sheet on the right labeled 「同じ日」. A thin arrow joins the plots to the sheet. A green check mark sits beside the sheet.',
                 words=['同じ日'], tag='複数の土地も一通'),
        ],
        kanji='登・記・事・項・証・明・書・三・月・以・内・変・更・分・筆・相・続・戸・籍・共・通・委・任・状・同・日'.split('・')),
    nb_label='イ・エ肢', nb_intro='イ・エの補足説明に合わせた2枚です。1枚目は、一の申請情報でまとめられる場面を表で示します。2枚目は、同時に申請するときの共通の添付情報の扱いを、図で示します。',
    notebooks=[
        dict(name='一の申請情報でまとめられる場面', args=dict(
            title='一通でまとめられるのは？', sub='一の申請情報で申請できる場合（毎日ドリル 第48日 イ）',
            req='a table diagram',
            layout="""--- TABLE ---
Render as a clean flat-design table in the upper half, with three rows and two columns, and a small isometric icon at the left of each row.
Column headers: 場面 | まとめられるか
Row 1 (blue accent), icon: a field turning into a parking lot beside a land plot split by a line. Cells: 同じ不動産の地目の変更と分筆 | まとめられる
Row 2 (green accent), icon: a record sheet with two corrected lines. Cells: 同じ不動産の表題部の変更の登記が二つ以上 | まとめられる
Row 3 (orange accent), icon: two neighboring land plots under one sheet. Cells: 二つ以上の土地で、目的と原因と日付が同一 | まとめられる
Use exactly these strings, and no others, for the table text. Each row has its own accent color so the three rows are never confused or duplicated.""",
            callout='申請情報は、一の不動産ごとに作るのが原則です。\nただし、同じ不動産の地目の変更と分筆は、一の申請情報で申請できます。',
            footer='不動産登記令4条、不動産登記規則35条',
            kanji='地・目・変・更・分・筆・表・題・部・土・同・原・因・日・付'.split('・'), what='table',
            check='confirm the three rows carry three different scene strings in different accent colors, ')),
        dict(name='同時に申請するときの共通の添付情報', args=dict(
            title='共通の書類は、どう出す？', sub='添付情報の省略（毎日ドリル 第48日 エ）',
            req='a flow diagram',
            layout="""--- FLOW ---
Render as a clean flat-design diagram in the upper half. Two application sheets are placed side by side: the left sheet carries the header 甲土地の分筆の登記の申請, and the right sheet carries the header 乙土地の地目の変更の登記の申請.
A single power-of-attorney sheet labeled 委任状 is clipped to the left sheet only (blue accent).
On the right sheet, a small note box (green accent) carries the text: 委任状は甲土地の申請に添付した. A thin dotted arrow runs from the note box to the power-of-attorney sheet.
Under the diagram, a banner with a green check mark: 共通の添付情報は、一の申請と併せて提供すれば足りる
Use exactly these strings, and no others, for the labels.""",
            callout='同じ登記所に同時に複数の申請をするときは、共通の添付情報を一の申請に付ければ足ります。\n他の申請の申請情報には、併せて提供した旨を書きます。',
            footer='不動産登記規則37条',
            kanji='甲・乙・土・地・分・筆・変・更・登・記・申・請・委・任・状・添・付・共・通・情・報'.split('・'), what='diagram',
            check='confirm the power-of-attorney sheet is attached to the left sheet only and the right sheet carries only the note box, ')),
    ],
)
