D = dict(
    catch='分割は名義人が申請、合併には制限あり',
    intro='建物の分割の登記と建物の合併の登記について、だれが申請できるのか、どんなときに合併できないのか、合併の後に登記記録がどうなるのか、を問う問題です（不動産登記法54条・56条、不動産登記規則131条・132条）。\n\nこの問題は、誤っている肢の組合せを選ぶ形式です。合併できない場合の「原則」と「例外」に注意して確かめていきましょう。',
    sections={
        'ア': ('附属建物だけの買主は、自分では分割を申請できない',
               '建物の分割の登記は、表題部所有者又は所有権の登記名義人以外の者は、申請することができません（不動産登記法54条1項1号）。\n\n問題文は、買主Bが、Aに代位することなく、自ら申請できるとしているので、本肢は誤りです。物置だけを買ったBは、まだ所有権の登記名義人ではありません。Bが申請するには、Aに代位して申請する方法を取ります。\n\n**たとえば**、母屋と物置をまとめて登記しているAから、Bが物置だけを買ったとします。物置を切り離す分割の登記は、Bが自分の名前では申請できません。Aが申請するか、BがAに代位して申請します。'),
        'イ': ('名義人が相互に異なる建物は、合併できない',
               '表題部所有者又は所有権の登記名義人が相互に異なる建物の合併の登記は、することができません（不動産登記法56条2号）。\n\n本肢は正しいといえます。Aが単独で所有する甲建物と、AとBが共有する乙建物とでは、所有権の登記名義人が相互に異なります。\n\n**たとえば**、父A名義の建物と、父Aと子Bの共有名義の建物を、一つにまとめたいと思っても、名義人が違うままでは合併の登記はできません。'),
        'ウ': ('同一内容の抵当権の登記なら、合併の制限に当たらない',
               '所有権等の登記以外の権利に関する登記（抵当権の登記など）がある建物は、原則として、合併の登記ができません（不動産登記法56条5号）。\n\nただし、担保権の登記で、登記の目的、申請の受付の年月日及び受付番号並びに登記原因及びその日付が同一のものは、合併後の建物の登記記録に登記できるので、制限に当たりません（不動産登記規則131条1号）。本肢は正しいといえます。\n\n**たとえば**、甲建物と乙建物に、同じ日に同じ申請で、同一内容の抵当権が設定されていたとします。この場合は、抵当権の登記があっても、甲建物を乙建物に合併できます。'),
        'エ': ('所有権の登記がない建物とは、同一人でも合併できない',
               '所有権の登記がない建物と、所有権の登記がある建物との合併の登記は、することができません（不動産登記法56条4号）。\n\n問題文は、名義人が同一人Aであれば申請できるとしているので、本肢は誤りです。表題部所有者と所有権の登記名義人が同一人でも、この制限は変わりません。\n\n**たとえば**、新築して表題登記だけをした甲建物を、所有権の登記がある乙建物に合併したいときは、先に甲建物について所有権の保存の登記をする必要があります。'),
        'オ': ('附属合併では、乙に記録し、甲の記録は閉鎖する',
               '甲建物を乙建物の附属建物とする附属合併の登記をするときは、乙建物の登記記録の表題部に、附属合併後の建物の表題部の登記事項と、家屋番号何番の建物を合併した旨を記録します（不動産登記規則132条1項）。\n\n甲建物の登記記録の表題部には、家屋番号何番の建物に合併した旨と、従前の建物の表題部の登記事項を抹消する記号を記録し、その登記記録を閉鎖します（同条3項）。本肢は正しいといえます。\n\n**たとえば**、物置の甲建物を、母屋の乙建物の附属建物にまとめた場合、合併後の内容は乙建物の登記記録に載ります。物置だった甲建物の登記記録は、閉鎖されます。'),
    },
    summary=[
        ('ア', '誤', '建物の分割の登記は、登記名義人しか申請できず、附属建物だけの買主は自ら申請できない'),
        ('イ', '正', '所有権の登記名義人が相互に異なる建物は、合併の登記ができない'),
        ('ウ', '正', '登記の目的、受付、原因が同一の担保権の登記があるだけなら、合併の制限に当たらない'),
        ('エ', '誤', '所有権の登記がない建物と、ある建物とは、名義人が同一人でも合併できない'),
        ('オ', '正', '附属合併では乙の登記記録に合併後の内容を記録し、甲の登記記録は閉鎖する'),
    ],
    summary_tail='アは「だれが申請するか」、エは「同一人ならよい」と考えさせる出題です。ウは例外の見落としを誘います。合併の制限は、原則とその例外をセットで覚えておきましょう。',
    supplements=[
        '### 補足説明（ア）：建物の分割の登記とは、どんな登記か\n\n建物の分割の登記は、表題登記がある建物の附属建物を、その建物の登記記録から切り離して、登記記録上別の一個の建物にする登記です（不動産登記法54条1項1号）。\n\n- 分割の前：母屋（主である建物）と物置（附属建物）が、一つの登記記録に載っている。\n- 分割の後：母屋と物置が、それぞれ別の一個の建物として登記される。\n\n申請できるのは、表題部所有者又は所有権の登記名義人だけです。\n\n**たとえば**、母屋と物置をまとめて登記しているAから、Bが物置だけを買う場合、物置を切り離す登記は、Aが申請するか、BがAに代位して申請します。',
        '### 補足説明（イ・ウ・エ）：建物の合併ができない場合\n\n建物の合併の登記は、次のような場合にはすることができません（不動産登記法56条）。\n\n- 共用部分である旨の登記などがある建物（1号）。\n- 表題部所有者又は所有権の登記名義人が相互に異なる建物（2号）：イの場合。\n- 名義人の持分が相互に異なる建物（3号）。\n- 所有権の登記がない建物と、ある建物（4号）：エの場合。同一人でもできない。\n- 所有権等の登記以外の権利に関する登記がある建物（5号）：ただし、登記の目的、受付、原因が同一の担保権の登記は例外で、合併できる（ウの場合）。\n\n**たとえば**、名義人が違う建物は合併できず、新築したばかりで所有権の登記がない建物は、先に所有権の保存の登記が必要です。抵当権の登記がある建物は、原則としてできませんが、同じ内容の抵当権なら例外にあたります。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第120日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法54条1項1号・56条1号〜5号、不動産登記規則131条1号・132条1項・3項は、`note-articles/laws/` 配下の原文で確認しました。',
        'アの「買主は売主に代位して申請する」、エの「先に所有権の保存の登記をする」は、条文からの一般的な整理です。代位の根拠条文や個別の先例は、この記事では確認していません。',
        '具体例（母屋と物置、父と子の建物、同一内容の抵当権、新築したばかりの建物）は、条文の文言を日常の場面に置き換えた仮の設定です。',
    ],
    phrases=['分割の登記は名義人が申請します', '名義人が違う建物は合併できません', '同一の抵当権なら合併できます', '所有権の登記がない建物は合併不可です', '附属合併の後は甲の記録を閉鎖します'],
    header=dict(t1='分割と合併、', t2='できる条件は？', topic='不動産登記法　建物の分割と合併',
                kanji='分・割・合・併・建・物・登・記・毎'),
    poster_intro='建物の分割と合併を、「分割の申請人と合併の制限」（グループA：ア・イ・ウ）と「所有権の登記と合併後の記録」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='建物の分割と合併を整理', sub='不動産登記法 第54条・第56条（毎日ドリル 第120日）',
        col_a='分割の申請人と合併の制限', col_b='所有権の登記と合併後の記録', n_a=3,
        cards=[
            dict(h='分割は名義人か代位で申請',
                 ill='an isometric main house with an attached storage shed, separated by a dashed line. An owner figure carrying a name tag labeled 「登記名義人」 holds a form. A buyer figure has a thin arrow into the owner figure, with a small tag labeled 「代位」 on the arrow. A green check mark sits beside the owner.',
                 words=['登記名義人', '代位'], tag='買主は代位で申請'),
            dict(h='名義人が違う建物は合併できない',
                 ill='two buildings. The left building has one owner figure with a name tag labeled 「単有」, and the right building has two owner figures with a name tag labeled 「共有」. A merge arrow between the buildings is stopped by a barrier. No check mark and no cross mark on this card.',
                 words=['単有', '共有'], tag='名義人が違うと不可'),
            dict(h='同一内容の抵当権なら合併できる',
                 ill='two buildings, each with an identical record sheet labeled 「抵当権」 and matching stamps, merging into one building. A green check mark sits beside the merged building.',
                 words=['抵当権'], tag='登記の内容が同一なら可'),
            dict(h='所有権の登記がない建物とは合併不可',
                 ill='a building with a nearly blank record sheet labeled 「表題のみ」 next to a building with a record sheet carrying an owner stamp labeled 「所有権」. A barrier stands between the two buildings. No check mark and no cross mark on this card.',
                 words=['表題のみ', '所有権'], tag='先に保存の登記が必要'),
            dict(h='附属合併では甲の記録を閉鎖',
                 ill='a building labeled 「甲」 being attached to a main building labeled 「乙」 as a shed. The record sheet of 乙 gains a new entry, and the record sheet of 甲 carries a stamp labeled 「閉鎖」 and is being filed away. A green check mark sits beside the 乙 record sheet.',
                 words=['甲', '乙', '閉鎖'], tag='乙に記録、甲は閉鎖'),
        ],
        kanji='分・割・名・義・人・代・位・合・併・抵・当・権・所・有・単・共・表・題・閉・鎖'.split('・')),
    nb_label='ア・イ・ウ・エ肢', nb_intro='ア、イ・ウ・エの補足説明に合わせた2枚です。1枚目は、建物の分割を申請できる人と、できない人を左右の対比で示します。2枚目は、建物の合併ができる場合とできない場合を3つの例で整理します。',
    notebooks=[
        dict(name='建物の分割を申請できる人、できない人', args=dict(
            title='建物の分割を申請できるのは？', sub='建物の分割の登記の申請人（毎日ドリル 第120日 ア）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two sides must show OPPOSITE marks, not the same mark. The left side shows a green check mark; the right side shows a red cross. The two panel headers are different strings: 「所有権の登記名義人」 on the left and 「附属建物だけの買主」 on the right; draw them in different accent colors (blue and gray) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 所有権の登記名義人
Scene: an isometric scene of an owner figure at a desk, applying with a form to separate a storage shed from a main house, the two joined by a dashed line.
Result badge with a green check mark: 自分で申請できる

RIGHT PANEL (gray accent):
Panel header: 附属建物だけの買主
Scene: a buyer figure standing beside a storage shed, holding a form but not touching the desk. A small arrow from the buyer toward the owner is labeled 代位.
Result badge with a red cross: 自分の名前では申請できない""",
            callout='建物の分割の登記を申請できるのは、表題部所有者又は所有権の登記名義人です。\n附属建物だけの買主は、自分の名前では申請できず、売主に代位して申請します。',
            footer='不動産登記法54条1項1号',
            kanji='建・物・分・割・登・記・所・有・権・名・義・人・附・属・買・主・申・請・代・位'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (所有権の登記名義人 on the left and 附属建物だけの買主 on the right) and that the left panel shows a green check mark while the right panel shows a red cross, ')),
        dict(name='建物の合併ができる場合とできない場合', args=dict(
            title='建物の合併、できる？ できない？', sub='建物の合併の制限（毎日ドリル 第120日 イ・ウ・エ）',
            req='a three-row table',
            layout="""IMPORTANT: Row 1 and Row 2 show a red cross, and Row 3 shows a green check mark. The three result cells are different strings; do not repeat or copy a result cell.

--- TABLE ---
Render as a clean flat-design table with three data rows and two columns, with a header row. Header row: 場合 | 合併の登記.
Row 1 (orange accent): left cell with a building labeled 単有 and a building labeled 共有, and the label 名義人が相互に異なる; right cell with a red cross and the label できない.
Row 2 (orange accent): left cell with a blank record sheet and a stamped record sheet, and the label 所有権の登記がない建物とある建物; right cell with a red cross and the label 同一人でもできない.
Row 3 (green accent): left cell with two buildings carrying identical mortgage record sheets, and the label 登記の目的、受付、原因が同一の抵当権; right cell with a green check mark and the label できる.
Use exactly these strings, and no others.""",
            callout='名義人が相互に異なる建物や、所有権の登記がない建物との合併は、できません。\n抵当権の登記がある場合も原則としてできませんが、登記の目的、受付、原因が同一の担保権の登記は例外です。',
            footer='不動産登記法56条、不動産登記規則131条',
            kanji='場・合・併・登・記・名・義・人・相・互・異・所・有・権・建・物・同・一・抵・当・受・付・原・因'.split('・'), what='table',
            check='confirm there are exactly three data rows, that Row 1 and Row 2 show a red cross and Row 3 shows a green check mark, and that the three result cells are different strings, ')),
    ],
)
