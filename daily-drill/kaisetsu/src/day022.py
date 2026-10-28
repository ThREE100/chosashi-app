D = dict(
    catch='筆界は合意では動かない',
    intro='筆界の意味、筆界特定の関係土地、筆界特定の事務を行う人について問う問題です（不動産登記法123条〜125条、不動産登記規則211条）。\n\nこの記事では、「筆界とは何か」と「筆界特定は誰が行うのか」を、具体的な場面で確認していきましょう。問題は、誤っている記述の組合せを選ぶ形です。',
    sections={
        'ア': ('表題登記がない土地どうしの境は、筆界ではない',
               '筆界とは、表題登記がある一筆の土地と、これに隣接する他の土地（表題登記がない土地を含みます）との間で、一筆の土地が登記された時にその境を構成するものとされた二以上の点と、それらを結ぶ直線をいいます（不動産登記法123条1号）。\n\n表題登記がある土地が一つも関わらない境は、ここでいう筆界に当たりません。本肢は正しいといえます。\n\n**たとえば**、まだ表題登記のされていない山林どうしが隣り合っていても、その境は、不動産登記法上の筆界ではありません。どちらか一方に表題登記があれば、筆界になります。'),
        'イ': ('筆界上の点で対象土地に接する土地は、関係土地に当たる',
               '関係土地とは、対象土地以外の土地で、筆界特定の対象となる筆界上の点を含む他の筆界で、対象土地の一方または双方と接するものをいいます（不動産登記法123条4号）。\n\n甲土地と乙土地の筆界A－Bについて、丙土地が点Bを端点とする筆界B－Cで乙土地と接しているときは、丙土地は関係土地に当たります。本肢は正しいといえます。\n\n**たとえば**、甲土地と乙土地の境の端の点で、乙土地が丙土地にも接している場合です。この丙土地の所有者も、筆界特定の手続に関係する人になります。'),
        'ウ': ('所有者どうしが合意しても、筆界は動かない',
               '筆界は、一筆の土地が登記された時にその境を構成するものとされた点と直線です（不動産登記法123条1号）。所有者どうしが合意して境界標を新しく置いても、筆界がその線に移るわけではありません。\n\n問題文は「合意した線となる」としているので、本肢は誤りです。\n\n**たとえば**、隣り合う所有者が話し合って、新しい線に境界標を設けたとします。それでも、登記上の筆界は元のままです。合意した線に合わせたいときは、分筆や合筆の登記などを使います。'),
        'エ': ('筆界特定の書面申請は、管轄の登記所を経由してできる',
               '筆界特定の事務は、対象土地の所在地を管轄する法務局又は地方法務局がつかさどります（不動産登記法124条1項）。筆界特定の書面申請は、対象土地の所在地を管轄する登記所を経由してすることができます（不動産登記規則211条9項）。\n\n本肢は正しいといえます。\n\n**たとえば**、法務局が遠い場所にある場合でも、土地の近くの登記所に申請書を出すことで、そこから法務局に届けてもらえます。'),
        'オ': ('筆界特定登記官を指定するのは、法務大臣ではなく、法務局の長',
               '筆界特定は、筆界特定登記官が行います。筆界特定登記官は、登記官のうちから、法務局又は地方法務局の長が指定する者です（不動産登記法125条）。\n\n問題文は「法務大臣が指定する」としているので、本肢は誤りです。\n\n**たとえば**、ある法務局で筆界特定の申請があったとき、その法務局の長が、所属する登記官の中から、その事件を担当する筆界特定登記官を指定します。'),
    },
    summary=[
        ('ア', '正', '表題登記がない土地どうしの境は、筆界に当たらない（どちらか一方に表題登記があれば筆界）'),
        ('イ', '正', '筆界上の点を含む他の筆界で対象土地と接する土地は、関係土地に当たる'),
        ('ウ', '誤', '所有者どうしが境について合意しても、筆界は合意した線にならない'),
        ('エ', '正', '筆界特定の書面申請は、対象土地の所在地を管轄する登記所を経由してできる'),
        ('オ', '誤', '筆界特定登記官を指定するのは、法務大臣ではなく、法務局又は地方法務局の長'),
    ],
    summary_tail='ウは「合意で筆界が動く」という思い込み、オは「指定する人のすり替え」の出題です。筆界は登記された時の境で、所有者の合意では変わらないことを押さえましょう。',
    supplements=[
        '### 補足説明（ウ）：筆界と、所有者どうしの合意\n\n筆界と、所有者どうしが合意した境は、別のものです。\n\n- 筆界：一筆の土地が登記された時にその境を構成するものとされた点と、それらを結ぶ直線。所有者の合意では動かない（123条1号）。\n- 所有者どうしの合意：当事者間の取り決め。合意した線に筆界を合わせたいときは、分筆や合筆の登記などを使う。\n\n**たとえば**、隣人どうしが、ブロック塀を建てた線を「境」と決めたとしても、登記上の筆界は、元の土地が登記された時の線のままです。',
        '### 補足説明（オ）：筆界特定で、だれが何をするか\n\n筆界特定では、役割ごとに担当が決まっています。\n\n- 筆界特定の事務：対象土地の所在地を管轄する法務局又は地方法務局がつかさどる（124条1項）。\n- 筆界特定をする人：筆界特定登記官（125条）。\n- 筆界特定登記官を指定する人：法務局又は地方法務局の長（125条）。\n\n**たとえば**、法務大臣は筆界特定登記官を指定しません。指定は、その事件を扱う法務局又は地方法務局の長がします。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第22日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法123条、124条、125条、不動産登記規則211条は、`note-articles/laws/` 配下の原文で確認しました。',
        'ウの「合意した線に合わせたいときは、分筆や合筆の登記などを使う」という説明は、筆界と所有者の合意が別のものであることからの一般的な整理で、条文からは確認していません。',
        '各肢の具体例（未登記の山林、境界標の設置、遠方の登記所からの申請など）は、条文の文言から導いた一般的な説明です。個別の運用・先例の確認はしていません。',
    ],
    phrases=['表題登記のない土地どうしは筆界ではありません', '端の点で接する土地は関係土地です', '合意しても筆界は動きません', '書面申請は登記所を経由できます', '筆界特定登記官を指定するのは法務局の長です'],
    header=dict(t1='筆界は合意で', t2='動かない？', topic='不動産登記法　筆界と筆界特定',
                kanji='筆・界・合・意・動・特・定・登・記'),
    poster_intro='筆界と筆界特定を、「筆界の意味」（グループA：ア・イ・ウ）と「筆界特定の事務」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='筆界と筆界特定を整理', sub='不動産登記法 第123条〜第125条（毎日ドリル 第22日）',
        col_a='筆界の意味', col_b='筆界特定の事務', n_a=3,
        cards=[
            dict(h='表題登記がない土地どうしは筆界でない',
                 ill='two neighboring land plots. The left plot has a record sheet labeled 「表題登記」 attached to it. The right plot has no sheet. A dotted line between them is the boundary. A green check mark sits beside the dotted line.',
                 words=['表題登記'], tag='一方に表題登記が必要'),
            dict(h='筆界上の点で接する土地は関係土地',
                 ill='three land plots meeting around one boundary point marked with a small stake. A tag labeled 「関係土地」 is attached to the third plot, which touches the stake. A green check mark sits beside the third plot.',
                 words=['関係土地'], tag='端の点で接する土地'),
            dict(h='合意しても筆界は動かない',
                 ill='two owner figures shaking hands, with a new boundary stake placed on a line between them drawn in faded gray. The original dotted line is highlighted in bold and labeled 「筆界」. A green check mark sits beside the original line.',
                 words=['筆界'], tag='所有者の合意で動かない'),
            dict(h='書面申請は登記所を経由できる',
                 ill='an applicant figure handing a form to a small office counter labeled 「登記所」, with a thin arrow leading to a larger building labeled 「法務局」. A green check mark sits beside the arrow.',
                 words=['登記所', '法務局'], tag='登記所を経由して提出'),
            dict(h='筆界特定登記官は長が指定する',
                 ill='a person figure carrying a name tag labeled 「法務局の長」 pointing at a registry officer figure carrying a name tag labeled 「筆界特定登記官」, who holds a form. A green check mark sits beside the registry officer figure.',
                 words=['法務局の長', '筆界特定登記官'], tag='指定するのは長'),
        ],
        kanji='表・題・登・記・土・地・筆・界・関・係・合・意・動・書・面・経・由・特・定・官・長・指'.split('・')),
    nb_label='ウ・オ肢', nb_intro='ウ・オの補足説明に合わせた2枚です。1枚目は、筆界と所有者どうしの合意の違いを左右の対比で示します。2枚目は、筆界特定で担当する人を表で整理します。',
    notebooks=[
        dict(name='筆界と、所有者どうしの合意', args=dict(
            title='筆界は、合意で動くの？', sub='筆界と合意した境の違い（毎日ドリル 第22日 ウ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings, 「筆界」 on the left and 「合意した境」 on the right. Draw them in different accent colors (blue and orange) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 筆界
Scene: an isometric scene of two neighboring land plots with a bold dotted line between them and a record sheet beside the plots labeled 「登記された時」.
Result badge: 合意では動かない

RIGHT PANEL (orange accent):
Panel header: 合意した境
Scene: an isometric scene of two owner figures shaking hands beside a new boundary stake placed on a different line between the same two plots.
Result badge: 筆界はそのまま""",
            callout='筆界は、一筆の土地が登記された時にその境を構成するものとされた点と、それらを結ぶ直線です。\n所有者どうしが境について合意しても、筆界が合意した線に移ることはありません。',
            footer='不動産登記法123条1号',
            kanji='筆・界・合・意・境・登・記・動・所・有・者'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (筆界 on the left and 合意した境 on the right) drawn in different accent colors, ')),
        dict(name='筆界特定で、だれが何をするか', args=dict(
            title='筆界特定、だれが何をする？', sub='事務を行う庁と指定する人（毎日ドリル 第22日 オ）',
            req='a table',
            layout="""--- TABLE ---
Render as a clean table with 2 columns and 3 data rows, plus a header row. The column headers are exactly: 役割 / 担当. Each row has a small isometric icon beside the first cell.
Row 1: first cell 筆界特定の事務をつかさどる (icon: a government building); second cell 法務局又は地方法務局.
Row 2: first cell 筆界特定をする人 (icon: a registry officer figure with a form); second cell 筆界特定登記官.
Row 3: first cell 筆界特定登記官を指定する人 (icon: a person figure pointing at another figure); second cell 法務局又は地方法務局の長.
Use exactly these strings, and no others, for the cell text. The three 担当 cells are different strings; draw each of them in a different accent color (blue, green and orange).""",
            callout='筆界特定登記官を指定するのは、法務大臣ではなく、法務局又は地方法務局の長です。\n筆界特定登記官は、登記官のうちから指定されます。',
            footer='不動産登記法124条1項、125条',
            kanji='筆・界・特・定・事・務・法・局・長・官・登・記・役・割・担・当・指'.split('・'), what='table',
            check='confirm the table has exactly 2 columns and 3 data rows, and confirm the three cells in the 担当 column are different strings drawn in different accent colors, ')),
    ],
)
