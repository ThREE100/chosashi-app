D = dict(
    catch='変更は一月以内、更正は所有者だけ',
    intro='土地の表題部に関する登記について、「いつまでに」「だれが」申請するのかを問う問題です（不動産登記法37条・38条・42条）。地目や地積が変わったとき（変更）と、最初から誤っていたとき（更正）では、申請できる人の決まり方が違います。\n\nこの記事では、一月以内の期限がいつから数えられるのかと、更正の登記を申請できる人を、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('地目が変わったら、変更の日から一月以内に申請する',
               '地目又は地積について変更があったときは、表題部所有者又は所有権の登記名義人は、その変更があった日から一月以内に、変更の登記を申請しなければなりません（不動産登記法37条1項）。\n\n本肢は正しいといえます。\n\n**たとえば**、畑として使っていた土地を造成して駐車場にした場合、地目は畑から雑種地に変わります。その造成が終わって使い方が変わった日から一月以内に、所有者が地目の変更の登記を申請します。'),
        'イ': ('土地がなくなったら、滅失の日から一月以内に申請する',
               '土地が滅失したときは、表題部所有者又は所有権の登記名義人は、その滅失の日から一月以内に、土地の滅失の登記を申請しなければなりません（不動産登記法42条）。\n\n本肢は正しいといえます。\n\n**たとえば**、海に面した土地が波に削られて海に沈み、土地としてなくなってしまった場合は、その滅失の日から一月以内に、所有者が滅失の登記を申請します。'),
        'ウ': ('変更の後に名義人となった者は、自分の登記の日から数える',
               '地目又は地積について変更があった後に表題部所有者又は所有権の登記名義人となった者は、その者に係る表題部所有者についての更正の登記又は所有権の登記があった日から一月以内に、変更の登記を申請しなければなりません（不動産登記法37条2項）。\n\n問題文は「その変更があった日から」としていますが、変更の後に名義人になった者の一月は、変更の日ではなく、自分に係る登記があった日から数えます。本肢は誤りです。\n\n**たとえば**、3月1日に畑が駐車場に変わり、4月10日に買主が所有権の移転の登記を受けた場合、買主の一月は、3月1日からではなく、登記を受けた4月10日から数えます。'),
        'エ': ('地積の更正の登記は、所有者と名義人しか申請できない',
               '地積は、土地の表示に関する登記の登記事項です（不動産登記法34条1項4号）。地積に関する更正の登記は、表題部所有者又は所有権の登記名義人以外の者は、申請することができません（同法38条）。\n\n本肢は正しいといえます。\n\n**たとえば**、測量したら、登記記録の面積が実際と違っていたとします。このとき、隣の土地の所有者や、土地を借りている人が、自分で地積の更正の登記を申請することはできません。申請できるのは、土地の所有者などに限られます。'),
        'オ': ('地目の更正の登記も、所有者と名義人しか申請できない',
               '地目も、土地の表示に関する登記の登記事項です（不動産登記法34条1項3号）。地目に関する更正の登記も、38条により、表題部所有者又は所有権の登記名義人以外の者は、申請することができません。\n\n問題文は「それ以外の者であっても、申請することができる」としているので、本肢は誤りです。\n\n**たとえば**、土地を借りている人が「登記記録の地目が実際と違う」と気づいても、自分で更正の登記を申請することはできません。土地の所有者に申請してもらうことになります。'),
    },
    summary=[
        ('ア', '正', '地目の変更があったときは、変更の日から一月以内に変更の登記を申請する'),
        ('イ', '正', '土地が滅失したときは、滅失の日から一月以内に滅失の登記を申請する'),
        ('ウ', '誤', '変更の後に名義人となった者の一月は、変更の日ではなく、自分に係る登記があった日から数える'),
        ('エ', '正', '地積の更正の登記は、表題部所有者又は所有権の登記名義人以外の者は申請できない'),
        ('オ', '誤', '地目の更正の登記も、表題部所有者又は所有権の登記名義人以外の者は申請できない'),
    ],
    summary_tail='ウは「一月をいつから数えるか」、オは「だれが申請できるか」を入れ替えた出題です。変更の登記は期限の起算日、更正の登記は申請人の範囲、と分けて覚えましょう。',
    supplements=[
        '### 補足説明（ウ）：一月の数え始めは、人によって違う\n\n地目や地積の変更の登記は、だれが申請するかによって、一月の数え始めが変わります。\n\n- 変更があったときの名義人：変更があった日から一月以内（37条1項）。\n- 変更の後に名義人となった者：自分に係る登記があった日から一月以内（37条2項）。\n\n**たとえば**、3月1日に地目が変わり、4月10日に買主が所有権の移転の登記を受けたとします。売主は3月1日から一月以内ですが、買主は4月10日から一月以内です。買主にとっては、買う前に起きた変更について、自分が名義人になった日から数え始める、ということです。',
        '### 補足説明（エ・オ）：更正の登記を申請できる人は、決まっている\n\n38条は、土地の所在（34条1項1号）、地目（同項3号）、地積（同項4号）に関する更正の登記を、表題部所有者又は所有権の登記名義人以外の者は申請できないと定めています。\n\n**たとえば**、登記記録の地目や地積が実際と違っているとき、隣の土地の所有者や、土地を借りている人は、間違いに気づいても自分で申請することはできません。土地の所有者に申請してもらうことになります。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第2日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、法34条1項、37条1項・2項、38条、42条は、`note-articles/laws/` 配下の原文で確認しました。',
        'ウの具体例（売主と買主の起算日の違い）は、37条1項・2項の文言から導いた一般的な説明で、個別の先例・通達の確認はしていません。',
        '更正の登記を申請できない人の例（隣地の所有者、土地を借りている人）は、38条の「表題部所有者又は所有権の登記名義人以外の者」の具体例として挙げたものです。',
    ],
    phrases=['変更は、変更の日から一月以内です', '土地がなくなったら滅失の登記です', '買主の一月は自分の登記の日から', '地積の更正は所有者しかできません', '地目の更正も所有者だけの申請です'],
    header=dict(t1='一月はいつから？', t2='だれが申請する？', topic='不動産登記法　土地の表題部',
                left='a small blank calendar page on the desk, beside a steaming cup of coffee',
                right='a land plot sheet and a pencil on the desk',
                pose="One hand on her chin in a thinking pose, the other hand holding a small blank calendar page; a focused, slightly puzzled expression with raised eyebrows.",
                kanji='登・記・毎・表・題・部'),
    poster_intro='土地の表題部の登記を、「一月以内の申請」（グループA：ア・イ・ウ）と「更正の登記の申請人」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='土地の表題部の登記を整理', sub='不動産登記法 第37条・第38条・第42条（毎日ドリル 第2日）',
        col_a='一月以内の申請', col_b='更正の登記の申請人', n_a=3,
        cards=[
            dict(h='地目が変わったら一月以内',
                 ill='an isometric scene of a field on the left turning into a parking lot on the right, with a thin arrow between them. A calendar page labeled 「一月以内」 sits above the arrow. A green check mark sits beside the parking lot.',
                 words=['一月以内'], tag='変更の日から'),
            dict(h='土地がなくなったら滅失の登記',
                 ill='an isometric coastal land plot on the left, partly sinking into the sea on the right, drawn as a plot outline fading into the water. A stamp labeled 「滅失」 sits beside the plot. A green check mark sits beside the stamp.',
                 words=['滅失'], tag='滅失の日から'),
            dict(h='あとから名義人になったら自分の登記から',
                 ill='a horizontal timeline. On the left a flag labeled 「変更」; further right a second flag labeled 「自分の登記」. A green bracket labeled 「一月以内」 starts at the second flag and extends to the right. The part of the timeline before the second flag is drawn in gray with no bracket.',
                 words=['変更', '自分の登記', '一月以内'], tag='起算日は自分の登記'),
            dict(h='地積の更正は所有者だけが申請',
                 ill='an isometric land plot with a measuring tape along one side. An owner figure at a desk, holding a form, is highlighted with a green glow and carries a name tag labeled 「所有者」. A green check mark sits beside the owner.',
                 words=['所有者'], tag='申請人は限定'),
            dict(h='地目の更正も所有者だけ',
                 ill='a record sheet labeled 「地目」 with one line corrected by a pencil, and a round stamp labeled 「更正」 beside it. An owner figure carrying a name tag 「所有者」 holds the sheet and is highlighted with a green glow. A faded gray figure with no tag stands aside in the background. A green check mark sits beside the owner.',
                 words=['地目', '更正', '所有者'], tag='申請人は限定'),
        ],
        kanji='地・目・変・更・滅・失・積・正・所・有・者・登・記・名・義・人・月・以・内・自・分'.split('・')),
    nb_label='ウ・エ・オ肢', nb_intro='ウ・エ・オの補足説明に合わせた2枚です。1枚目は、一月の数え始めが人によって違うことを、時間の流れで示します。2枚目は、更正の登記を申請できる人と、できない人を左右の対比で示します。',
    notebooks=[
        dict(name='一月の数え始めは、人によって違う', args=dict(
            title='一月の数え始めは、いつ？', sub='地目と地積の変更の登記（毎日ドリル 第2日 ウ）',
            req='a timeline diagram',
            layout="""--- TIMELINE ---
Render as a clean flat-design horizontal timeline in the upper half, with two lanes stacked vertically. A common timeline axis runs left to right with two flags: the left flag labeled 3月1日 with an icon of a field turning into a parking lot, and the right flag labeled 4月10日 with an icon of a deed document being handed to a buyer figure.
Upper lane (blue accent), lane label: 売主（変更があったときの名義人）. A blue bracket starts at the left flag and extends to the right, labeled 変更の日から一月以内.
Lower lane (green accent), lane label: 買主（変更の後に名義人となった者）. A green bracket starts at the right flag and extends to the right, labeled 自分の登記の日から一月以内.
Use exactly these strings, and no others, for the labels. The two bracket labels are different strings; draw them in different accent colors (blue and green).""",
            callout='変更の後に名義人となった者は、変更があった日ではなく、自分に係る登記があった日から一月以内に申請します。\n買う前に起きた変更でも、数え始めは自分の登記の日です。',
            footer='不動産登記法37条1項・2項',
            kanji='登・記・変・更・売・買・名・義・人・月・以・内'.split('・'), what='timeline',
            check='confirm the two lanes have different bracket labels in different accent colors, ')),
        dict(name='更正の登記を申請できる人、できない人', args=dict(
            title='更正の登記を申請できるのは？', sub='地目と地積の更正（毎日ドリル 第2日 エ・オ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two sides must show OPPOSITE marks, not the same mark. The left side shows a green check mark; the right side shows a red cross. The two panel headers are different strings: 「所有者」 on the left and 「それ以外の人」 on the right; draw them in different accent colors (blue and gray) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 所有者
Scene: an isometric scene of an owner figure at a desk, applying with a form for a corrected record sheet labeled 「地目」 and 「地積」.
Result badge with a green check mark: 申請できる

RIGHT PANEL (gray accent):
Panel header: それ以外の人
Scene: two faceless figures standing beside a land plot: one with a name tag 「隣地の所有者」, one with a name tag 「土地を借りている人」. Neither holds a form.
Result badge with a red cross: 申請できない""",
            callout='地目や地積の更正の登記は、表題部所有者又は所有権の登記名義人以外の者は、申請することができません。\n間違いに気づいても、隣の土地の所有者や、土地を借りている人は、自分では申請できません。',
            footer='不動産登記法34条1項、38条',
            kanji='登・記・更・正・地・目・積・所・有・者・申・請・隣・借'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (所有者 on the left and それ以外の人 on the right) and that the left panel shows a green check mark while the right panel shows a red cross, ')),
    ],
)
