D = dict(
    catch='登記記録の編成と保存期間の数字',
    intro='登記記録の編成、滅失と回復、閉鎖した登記記録の保存期間、職権による登記、副登記記録について問う問題です（不動産登記法13条・16条・28条、不動産登記規則4条・9条・28条・30条）。\n\nこの記事では、甲区と乙区の使い分け、保存期間の年数、副登記記録の位置づけを、具体的な場面で確認していきましょう。問題は、正しい記述の組合せを選ぶ形です。',
    sections={
        'ア': ('地上権の設定の登記は、乙区に記録される',
               '権利部は、甲区と乙区に分かれています。甲区には所有権に関する登記の登記事項を、乙区には所有権以外の権利に関する登記の登記事項を記録します（不動産登記規則4条4項）。\n\n地上権は所有権以外の権利なので、乙区に記録されます。問題文は「甲区に記録される」としているので、本肢は誤りです。\n\n**たとえば**、甲土地の所有者はAさんで、Bさんがその土地に地上権の設定を受けたとします。Aさんの所有権の登記は甲区、Bさんの地上権の登記は乙区に載ります。'),
        'イ': ('登記記録が滅失したら、登記官が報告し、法務大臣が回復を命ずる',
               '登記官は、登記記録が滅失したときは、速やかにその状況を調査して、その登記官を監督する法務局又は地方法務局の長に報告しなければなりません（不動産登記規則30条1項）。\n\nまた、法務大臣は、登記官に対し、一定の期間を定めて、登記記録の回復に必要な処分を命ずることができます（不動産登記法13条）。\n\n本肢は正しいといえます。\n\n**たとえば**、災害で登記所の登記記録の一部が失われたとします。まず登記官が状況を調べて法務局の長に報告し、法務大臣が回復のための処分を命じる、という順になります。'),
        'ウ': ('建物の閉鎖登記記録の保存期間は、三十年間',
               '閉鎖した登記記録の保存期間は、土地と建物で違います。土地に関する閉鎖登記記録は閉鎖した日から五十年間、建物に関する閉鎖登記記録は閉鎖した日から三十年間です（不動産登記規則28条4号・5号）。\n\n問題文は、取り壊された建物の閉鎖登記記録を「五十年間」としているので、本肢は誤りです。\n\n**たとえば**、取り壊した建物の滅失の登記で閉鎖された登記記録は、閉鎖から三十年間保存されます。一方、土地の登記記録が閉鎖されたときは、五十年間です。'),
        'エ': ('登記は申請か嘱託が原則だが、表示に関する登記は職権でもできる',
               '登記は、法令に別段の定めがある場合を除き、当事者の申請又は官庁若しくは公署の嘱託がなければ、することができません（不動産登記法16条1項）。その別段の定めの一つが、表示に関する登記は登記官が職権ですることができるという規定です（同法28条）。\n\n本肢は正しいといえます。\n\n**たとえば**、新築された建物の表題登記は、所有者の申請だけでなく、登記官が職権ですることもできます。'),
        'オ': ('副登記記録に記録した事項は、登記記録に記録した事項とみなされる',
               '登記官は、登記簿に記録した登記記録によって登記の事務を行うことができないときは、副登記記録によって事務を行うことができます。この場合、副登記記録に記録した事項は、登記記録に記録した事項とみなされます（不動産登記規則9条2項）。\n\n問題文は「みなされない」としているので、本肢は誤りです。\n\n**たとえば**、機器の故障で登記記録が使えない間も、副登記記録を使って登記の事務を続けられます。そこに記録した事項は、正式な登記記録の事項として扱われ、元の記録が使えるようになったら直ちに登記記録に記録されます（同条3項）。'),
    },
    summary=[
        ('ア', '誤', '甲区は所有権に関する登記、乙区は所有権以外の権利に関する登記。地上権は乙区に記録される'),
        ('イ', '正', '登記記録の滅失は、登記官が法務局の長に報告し、法務大臣が回復の処分を命ずることができる'),
        ('ウ', '誤', '建物に関する閉鎖登記記録の保存期間は三十年間（五十年間は土地）'),
        ('エ', '正', '登記は申請か嘱託が原則だが、表示に関する登記は登記官が職権ですることもできる'),
        ('オ', '誤', '副登記記録に記録した事項は、登記記録に記録した事項とみなされる'),
    ],
    summary_tail='アは「甲区と乙区の取り違え」、ウは「土地と建物の年数の取り違え」、オは「みなされる」を「みなされない」にした出題です。区の使い分けと保存期間は、組にして覚えましょう。',
    supplements=[
        '### 補足説明（ア）：甲区と乙区の使い分け\n\n登記記録の権利部は、記録する内容によって甲区と乙区に分かれます（不動産登記規則4条4項）。\n\n- 甲区：所有権に関する登記（所有権の保存、移転など）。\n- 乙区：所有権以外の権利に関する登記（地上権、抵当権、賃借権など）。\n\n**たとえば**、住宅ローンを組んで家を買った場合、買主の所有権の移転の登記は甲区、銀行の抵当権の設定の登記は乙区に載ります。所有者の名前を見たいときは甲区、借金や地上権などの負担を見たいときは乙区を見ます。',
        '### 補足説明（ウ）：閉鎖登記記録の保存期間\n\n閉鎖した登記記録の保存期間は、不動産の種類で変わります（不動産登記規則28条）。\n\n- 土地に関する閉鎖登記記録：閉鎖した日から五十年間。\n- 建物に関する閉鎖登記記録：閉鎖した日から三十年間。\n- 閉鎖していない登記記録：永久。\n\n**たとえば**、同じ年に、取り壊された建物の登記記録と、閉鎖された土地の登記記録があるとします。建物の記録は三十年間、土地の記録は五十年間、保存されます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第21日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法13条、16条、28条、不動産登記規則4条、9条、28条、30条は、`note-articles/laws/` 配下の原文で確認しました。',
        'ウの具体例（取り壊された建物と閉鎖された土地の登記記録）は、保存期間の違いを比べるために挙げたものです。閉鎖の原因ごとの取扱いは確認していません。',
        'イ・エ・オの具体例（災害、新築建物の表題登記、機器の故障）は、条文の文言から導いた一般的な説明です。副登記記録を使う具体的な場面は、条文には書かれていません。',
    ],
    phrases=['地上権は乙区に記録されます', '回復を命じるのは法務大臣です', '建物の閉鎖記録は三十年間です', '表示の登記は職権でもできます', '副登記記録の事項は登記記録とみなされます'],
    header=dict(t1='甲区か乙区か、', t2='保存は何年？', topic='不動産登記法　登記記録と登記簿',
                kanji='甲・乙・区・保・存・年・登・記・録・簿'),
    poster_intro='登記記録と登記簿に関する決まりを、「登記記録の編成と回復」（グループA：ア・イ）と「保存・職権・副登記記録」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='登記記録と保存期間を整理', sub='不動産登記法・不動産登記規則（毎日ドリル 第21日）',
        col_a='登記記録の編成と回復', col_b='保存・職権・副登記記録', n_a=2,
        cards=[
            dict(h='地上権は乙区に記録される',
                 ill='an isometric record sheet divided into two sections. The upper section is labeled 「甲区」 and holds a line for ownership. The lower section is labeled 「乙区」 and holds a highlighted line labeled 「地上権」. A green check mark sits beside the lower section.',
                 words=['甲区', '乙区', '地上権'], tag='所有権以外は乙区'),
            dict(h='滅失は報告し、回復は大臣が命ずる',
                 ill='a damaged record sheet with a torn corner, a registry officer figure handing a report sheet to a figure labeled 「法務局の長」, and a second figure labeled 「法務大臣」 holding an order sheet. A green check mark sits beside the minister figure.',
                 words=['法務局の長', '法務大臣'], tag='報告と回復の命令'),
            dict(h='建物の閉鎖記録は三十年間',
                 ill='a stack of closed record folders with a small house icon labeled 「建物」, and a calendar page labeled 「三十年間」 beside the stack. A green check mark sits beside the calendar.',
                 words=['建物', '三十年間'], tag='建物は三十年'),
            dict(h='表示の登記は職権でもできる',
                 ill='a registry officer figure pressing a round stamp labeled 「職権」 onto a record sheet labeled 「表示」. A green check mark sits beside the stamp.',
                 words=['職権', '表示'], tag='申請がなくても可'),
            dict(h='副登記記録の事項は登記記録とみなす',
                 ill='two stacked record sheets. The front sheet is labeled 「登記記録」 and the sheet behind it is labeled 「副登記記録」. A green equals sign sits between the two sheets.',
                 words=['登記記録', '副登記記録'], tag='登記記録の事項とみなす'),
        ],
        kanji='地・上・権・甲・乙・区・滅・失・法・務・局・長・大・臣・建・物・閉・鎖・年・間・表・示・職・副・登・記・録・事・項'.split('・')),
    nb_label='ア・ウ肢', nb_intro='ア・ウの補足説明に合わせた2枚です。1枚目は、甲区と乙区に記録される内容を左右の対比で示します。2枚目は、登記記録の保存期間を表で整理します。',
    notebooks=[
        dict(name='甲区と乙区の使い分け', args=dict(
            title='甲区と乙区、何を記録する？', sub='権利部の2つの区（毎日ドリル 第21日 ア）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings, 「甲区」 on the left and 「乙区」 on the right. Draw them in different accent colors (blue and orange) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 甲区
Scene: an isometric scene of a record sheet with two small stacked icons, each followed by a label: a house with a key and the label 所有権の保存, a seller handing a deed document to a buyer with the label 所有権の移転.
Result badge: 所有権に関する登記

RIGHT PANEL (orange accent):
Panel header: 乙区
Scene: an isometric scene of a record sheet with three small stacked icons, each followed by a label: a house with a lock-shaped stamp and the label 抵当権, a land plot with a pillar and the label 地上権, a house with a rental sign and the label 賃借権.
Result badge: 所有権以外の権利に関する登記""",
            callout='権利部の甲区には、所有権に関する登記を記録します。\n乙区には、地上権、抵当権、賃借権など、所有権以外の権利に関する登記を記録します。',
            footer='不動産登記規則4条4項',
            kanji='甲・乙・区・所・有・権・保・存・移・転・抵・当・地・上・賃・借・登・記'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (甲区 on the left and 乙区 on the right) drawn in different accent colors, ')),
        dict(name='閉鎖登記記録の保存期間', args=dict(
            title='登記記録、何年保存される？', sub='閉鎖した登記記録の保存期間（毎日ドリル 第21日 ウ）',
            req='a table',
            layout="""--- TABLE ---
Render as a clean table with 2 columns and 3 data rows, plus a header row. The column headers are exactly: 登記記録 / 保存期間. Each row has a small isometric icon beside the first cell.
Row 1: first cell 土地に関する閉鎖登記記録 (icon: a land plot with a closed folder); second cell 閉鎖した日から五十年間.
Row 2: first cell 建物に関する閉鎖登記記録 (icon: a house with a closed folder); second cell 閉鎖した日から三十年間.
Row 3: first cell 閉鎖していない登記記録 (icon: an open record sheet); second cell 永久.
Use exactly these strings, and no others, for the cell text. The three 保存期間 cells are different strings; draw each of them in a different accent color (blue, orange and green).""",
            callout='閉鎖した登記記録の保存期間は、土地が五十年間、建物が三十年間です。\n取り壊された建物の閉鎖登記記録は、五十年間ではなく、三十年間です。',
            footer='不動産登記規則28条',
            kanji='土・地・建・物・閉・鎖・登・記・保・存・期・間・永・久・五・十・三・年・日'.split('・'), what='table',
            check='confirm the table has exactly 2 columns and 3 data rows, and confirm the three cells in the 保存期間 column are different strings drawn in different accent colors, ')),
    ],
)
