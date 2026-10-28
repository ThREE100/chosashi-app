D = dict(
    catch='分筆の申請人は登記名義人、買主は代位',
    intro='土地の分筆の登記について、だれが申請できるのか、登記官が職権でするのはどんなときか、抵当権はどうなるのか、分筆後の地番はどう付くのか、を問う問題です（不動産登記法39条・40条）。\n\nこの問題は、誤っている肢の組合せを選ぶ形式です。申請人の範囲と、職権でできる条件を、具体的な場面で確かめていきましょう。',
    sections={
        'ア': ('土地の一部の買主は、自分では分筆を申請できない',
               '分筆の登記は、表題部所有者又は所有権の登記名義人以外の者は、申請することができません（不動産登記法39条1項）。\n\n問題文は、買主Bが、Aに代位することなく、自ら申請できるとしているので、本肢は誤りです。土地の一部を買っただけのBは、まだ所有権の登記名義人ではありません。Bが申請するには、Aに代位して申請する方法を取ります。\n\n**たとえば**、広い土地の一部だけを買ったBが、その部分を別の土地として登記してほしいと考えても、自分の名前で分筆の登記を申請することはできません。売主Aに代位して申請するか、Aに申請してもらうことになります。'),
        'イ': ('一部が別の地目になったら、登記官が職権で分筆する',
               '登記官は、一筆の土地の一部が別の地目となったときは、申請がなくても、職権で、その土地の分筆の登記をしなければなりません（不動産登記法39条2項）。\n\n本肢は正しいといえます。\n\n**たとえば**、宅地として登記されている土地の一部が、駐車場として使われるようになったとします。所有者が分筆の登記を申請しなくても、登記官は、一つの土地には一つの地目という考え方から、その部分を職権で分筆します。'),
        'ウ': ('地図のための職権分筆は、異議がないときに限る',
               '登記官は、地図を作成するため必要があると認めるときは、表題部所有者又は所有権の登記名義人の異議がないときに限り、職権で、分筆又は合筆の登記をすることができます（不動産登記法39条3項）。\n\n問題文は、Aが異議を述べている場合でも職権で分筆できるとしているので、本肢は誤りです。\n\n**たとえば**、法務局が地図を整えるために土地の分け方を直したいと考えても、所有者Aが「反対です」と述べているなら、職権で分筆することはできません。'),
        'エ': ('乙土地の抵当権を消滅させる承諾があれば、付記登記で記録する',
               '抵当権の登記がある土地を分筆するとき、抵当権者が、分筆後の乙土地について抵当権を消滅させることを承諾した情報が、分筆の申請情報と併せて提供されたとします。この場合、乙土地について抵当権が消滅した旨が登記されます（不動産登記法40条）。\n\nその記録の方法は、乙土地の登記記録には抵当権の登記を転写せず、分筆後の甲土地の登記記録の抵当権の登記に、付記登記で「乙土地について消滅した」旨を記録するものです（不動産登記規則104条2項）。本肢は正しいといえます。\n\n**たとえば**、銀行の抵当権が付いた甲土地から一部を乙土地として分筆して売るとき、銀行が「乙土地は抵当権から外してよい」と承諾すれば、乙土地の登記記録には抵当権が載りません。'),
        'オ': ('支号のある土地を分筆すると、最終の支号に続けて付ける',
               '本番に支号のある土地を分筆する場合は、その一筆には従来の地番を残し、他の各筆には、本番の最終の支号に続けて順次支号を付けて地番を定めます（不動産登記事務取扱手続準則67条1項4号ただし書）。\n\n本肢は正しいといえます。5番から5番1〜5番8が分筆されているので、本番（5番）の最終の支号は8です。5番3を3筆に分けると、一筆は従来の5番3のまま、残る二筆は5番9と5番10になります。\n\n**たとえば**、5番3の土地をさらに分けるときに、「5番3の1」「5番3の2」のような地番にはしません。支号の支号は用いない決まりがあるからです（同項9号）。'),
    },
    summary=[
        ('ア', '誤', '土地の一部の買主は、所有権の登記名義人ではないので、自ら分筆を申請できず、売主に代位して申請する'),
        ('イ', '正', '一筆の土地の一部が別の地目となったときは、登記官が職権で分筆の登記をしなければならない'),
        ('ウ', '誤', '地図を作成するための職権による分筆は、登記名義人の異議がないときに限りできる'),
        ('エ', '正', '乙土地の抵当権を消滅させる承諾があれば、乙土地には転写せず、甲土地の抵当権の登記に付記登記で記録する'),
        ('オ', '正', '支号のある土地の分筆では、一筆に従来の地番を残し、他は本番の最終の支号に続けて付ける'),
    ],
    summary_tail='アは「だれが申請するか」、ウは「異議がないときに限る」という条件を外した出題です。申請は名義人、職権分筆は場面ごとに条件が違う、と分けて覚えましょう。',
    supplements=[
        '### 補足説明（ア）：分筆の登記を申請できる人\n\n分筆の登記は、申請できる人が限られています（不動産登記法39条1項）。\n\n- 申請できる人：表題部所有者又は所有権の登記名義人。\n- 申請できない人：土地の一部を買っただけの買主など、それ以外の人。\n\n買主は、自分の名前では申請できません。売主に代位して（売主に代わって）申請する方法を取ります。\n\n**たとえば**、Aの土地の東半分をBが買う契約をしたとします。東半分を別の土地として登記するための分筆は、Bが自分では申請できません。Aに代位してBが申請するか、Aに申請してもらいます。',
        '### 補足説明（イ・ウ）：登記官が職権で分筆する二つの場面\n\n登記官は、申請がなくても職権で分筆の登記をすることがあります。ただし、場面によって「しなければならない」場合と、「異議がないときに限りできる」場合に分かれます。\n\n- 一筆の土地の一部が別の地目となったとき（又は地番区域を異にするに至ったとき）：職権で分筆の登記をしなければならない（39条2項）。\n- 地図を作成するため必要があると認めるとき：登記名義人の異議がないときに限り、職権で分筆又は合筆の登記をすることができる（同条3項）。\n\n**たとえば**、宅地の一部が駐車場になっていれば、所有者が申請しなくても、登記官は分筆しなければなりません。一方、地図を整えるための分筆は、所有者が「反対です」と述べればできません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第116日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法39条1項〜3項・40条、不動産登記規則104条1項・2項、不動産登記事務取扱手続準則67条1項4号・9号は、`note-articles/laws/` 配下の原文で確認しました。',
        'アの「買主は売主に代位して申請する」、イの「一つの土地には一つの地目という考え方」は、条文からの一般的な整理です。代位の根拠条文や個別の先例は、この記事では確認していません。',
        '具体例（土地の東半分を買う買主、駐車場になった宅地、銀行の抵当権、5番3の分筆）は、条文の文言を日常の場面に置き換えた説明です。',
    ],
    phrases=['分筆は登記名義人が申請します', '買主は売主に代位して申請します', '一部が別の地目なら職権で分筆です', '地図のための職権分筆は異議なしのとき', '支号の支号は使わず最終の支号に続けます'],
    header=dict(t1='分筆は、だれが？', t2='どう進む？', topic='不動産登記法　分筆の登記',
                kanji='分・筆・登・記・毎・進'),
    poster_intro='分筆の登記を、「申請と職権」（グループA：ア・イ・ウ）と「権利の消滅と地番」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='分筆の登記を整理', sub='不動産登記法 第39条・第40条（毎日ドリル 第116日）',
        col_a='分筆の申請と職権', col_b='権利の消滅と地番', n_a=3,
        cards=[
            dict(h='買主は代位して分筆を申請',
                 ill='an isometric land plot split by a dashed line. An owner figure carrying a name tag labeled 「登記名義人」 holds a form. A buyer figure behind the owner has a thin arrow into the owner figure, with a small tag labeled 「代位」 on the arrow. A green check mark sits beside the owner.',
                 words=['登記名義人', '代位'], tag='買主は代位で申請'),
            dict(h='一部が別の地目なら登記官が分筆',
                 ill='an isometric land plot whose right part has turned into a parking lot. A registry official figure stamps a stamp labeled 「分筆」 on a record sheet. A green check mark sits beside the official.',
                 words=['分筆'], tag='申請がなくても職権で'),
            dict(h='地図のための職権分筆は異議なしのとき',
                 ill='a map sheet on a table with several land plots. A registry official figure and an owner figure face each other, and the owner holds a small card labeled 「異議なし」. A green check mark sits beside the owner.',
                 words=['異議なし'], tag='異議がなければ可能'),
            dict(h='乙土地は抵当権から外れる',
                 ill='two record sheets side by side. The left sheet is labeled 「甲土地」 and carries a note line with a small stamp labeled 「消滅」. The right sheet is labeled 「乙土地」 and has a blank rights section. A green check mark sits beside the right sheet.',
                 words=['甲土地', '乙土地', '消滅'], tag='付記登記で記録'),
            dict(h='支号は最終の支号に続ける',
                 ill='a land plot split into three parts, labeled 「5番3」, 「5番9」 and 「5番10」 from left to right. A green check mark sits beside the plot.',
                 words=['5番3', '5番9', '5番10'], tag='最終の支号に続ける'),
        ],
        kanji='分・筆・申・請・登・記・名・義・人・代・位・職・権・異・議・甲・乙・消・滅・番・支・号'.split('・')),
    nb_label='ア・イ・ウ肢', nb_intro='ア・イ・ウの補足説明に合わせた2枚です。1枚目は、分筆の登記を申請できる人と、できない人を左右の対比で示します。2枚目は、登記官が職権で分筆する二つの場面を整理します。',
    notebooks=[
        dict(name='分筆の登記を申請できる人、できない人', args=dict(
            title='分筆を申請できるのは？', sub='分筆の登記の申請人（毎日ドリル 第116日 ア）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two sides must show OPPOSITE marks, not the same mark. The left side shows a green check mark; the right side shows a red cross. The two panel headers are different strings: 「所有権の登記名義人」 on the left and 「土地の一部の買主」 on the right; draw them in different accent colors (blue and gray) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 所有権の登記名義人
Scene: an isometric scene of an owner figure at a desk, applying with a form for dividing a land plot by a dashed line.
Result badge with a green check mark: 自分で申請できる

RIGHT PANEL (gray accent):
Panel header: 土地の一部の買主
Scene: a buyer figure standing beside half of a land plot, holding a form but not touching the desk. A small arrow from the buyer toward the owner is labeled 代位.
Result badge with a red cross: 自分の名前では申請できない""",
            callout='分筆の登記を申請できるのは、表題部所有者又は所有権の登記名義人です。\n土地の一部の買主は、自分の名前では申請できず、売主に代位して申請します。',
            footer='不動産登記法39条1項',
            kanji='分・筆・登・記・所・有・権・名・義・人・買・主・申・請・代・位'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (所有権の登記名義人 on the left and 土地の一部の買主 on the right) and that the left panel shows a green check mark while the right panel shows a red cross, ')),
        dict(name='登記官が職権で分筆する二つの場面', args=dict(
            title='職権で分筆するのは、どんなとき？', sub='職権による分筆の登記（毎日ドリル 第116日 イ・ウ）',
            req='a two-row comparison table',
            layout="""--- TABLE ---
Render as a clean flat-design table with two rows and two columns, with a header row. Header row: 場面 | 職権での分筆.
Row 1 (green accent), left cell: an icon of a land plot whose part has turned into a parking lot, with the label 一部が別の地目になったとき. Right cell: a stamp icon with the label 申請がなくても、しなければならない.
Row 2 (blue accent), left cell: an icon of a map sheet with several plots, with the label 地図を作成するため必要なとき. Right cell: an icon of an owner figure holding a card, with the label 異議がないときに限り、できる.
Use exactly these strings, and no others. The two right cells are different strings; draw them in different accent colors (green and blue).""",
            callout='一部が別の地目になったときは、申請がなくても、登記官は職権で分筆しなければなりません。\n地図を作成するための職権分筆は、登記名義人の異議がないときに限り、することができます。',
            footer='不動産登記法39条2項・3項',
            kanji='場・面・職・権・分・筆・一・部・別・地・目・申・請・図・作・成・必・要・異・議'.split('・'), what='table',
            check='confirm there are exactly two data rows and that the two right cells are different strings in different accent colors, ')),
    ],
)
