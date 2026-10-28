def kj(*ss, n=14):
    out = []
    for s in ss:
        for c in s:
            if '一' <= c <= '龥' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='家屋番号は「5番の1」、床面積は内側線',
    intro='建物の家屋番号の定め方、床面積の測り方、敷地権である旨の登記、河川区域内の土地の登記について問う問題です（不動産登記法43条・46条、不動産登記規則115条、不動産登記事務取扱手続準則79条）。この問題は、正しいものを選ぶ形です。\n\nこの記事では、家屋番号の「支号」の書き方、区分建物の床面積の測り方、河川区域内の土地が滅失したときの嘱託を、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('一筆の土地に二個の建物があれば、「5番の1」「5番の2」',
               '一筆の土地の上に二個以上の建物が存する場合の家屋番号は、敷地の地番と同一の番号に1、2の支号を付して、「5番の1」「5番の2」の例により定めます（不動産登記事務取扱手続準則79条2号）。\n\n問題文は「5番1」「5番2」の例としています。「5番1」は、土地を分筆したときの地番の書き方であり、家屋番号の書き方ではありません。本肢は誤りです。\n\n**たとえば**、地番が5番の土地に母屋と離れの二個の建物があるときは、家屋番号は「5番の1」「5番の2」となります。'),
        'イ': ('区分建物の床面積は、壁の内側線で測る',
               '建物の床面積は、各階ごとに壁その他の区画の中心線で囲まれた部分の面積で定めますが、区分建物については、壁その他の区画の内側線で囲まれた部分の面積で定めます（不動産登記規則115条）。\n\n本肢は、中心線で測ると52.38平方メートル、内側線で測ると49.76平方メートルの区分建物なので、登記されるのは内側線で測った49.76平方メートルです。本肢は正しいといえます。\n\n**たとえば**、マンションの一室の広さは、壁の厚みの真ん中までではなく、部屋の内側の壁面から壁面までで測ります。'),
        'ウ': ('二筆にまたがる建物は、床面積の多い土地の地番と同じ番号',
               '二筆以上の土地にまたがって一個の建物が存する場合は、附属建物がないときは、床面積の多い部分の存する敷地の地番と同一の番号で定めます（不動産登記事務取扱手続準則79条3号）。\n\n本肢は、床面積の多い部分が6番の土地の上にあるので、家屋番号は6番と同一の番号です。5番ではありません。本肢は誤りです。\n\n**たとえば**、5番と6番にまたがる建物で、床面積の多い部分が6番側にあれば、家屋番号は「6番」となります。地番の若い5番ではありません。'),
        'エ': ('敷地権について最初に登記したら、土地に「敷地権である旨」を登記する',
               '登記官は、区分建物に関する敷地権について表題部に最初に登記をするときは、その敷地権の目的である土地の登記記録に、職権で、所有権などが敷地権である旨の登記をしなければなりません（不動産登記法46条）。\n\n本肢は正しいといえます。\n\n**たとえば**、新築のマンションの区分建物に敷地権が登記されたときは、その敷地である土地の登記記録に、「この土地の所有権は敷地権である」という趣旨の登記が、登記官によって職権でされます。'),
        'オ': ('河川区域内の土地の一部が滅失したら、地積の変更を嘱託する',
               '河川区域内の土地の一部が滅失したときは、河川管理者は、遅滞なく、その土地の地積に関する変更の登記を登記所に嘱託しなければなりません（不動産登記法43条6項）。\n\n問題文は、分筆の登記と、分筆後の土地の滅失の登記を嘱託するとしています。本肢は誤りです。\n\n**たとえば**、河川区域内の土地の一部が川に削られてなくなったときは、河川管理者が、残った土地の面積に直す登記を嘱託します。土地を分けて、なくなった部分だけを滅失させるわけではありません。'),
    },
    summary=[
        ('ア', '誤', '一筆の土地に二個の建物があるときの家屋番号は、「5番の1」「5番の2」の例による'),
        ('イ', '正', '区分建物の床面積は、壁その他の区画の内側線で囲まれた部分で定める'),
        ('ウ', '誤', '二筆にまたがる建物の家屋番号は、床面積の多い部分の存する土地の地番と同一の番号'),
        ('エ', '正', '敷地権について表題部に最初に登記するときは、土地の登記記録に敷地権である旨を職権で登記する'),
        ('オ', '誤', '河川区域内の土地の一部が滅失したときは、地積に関する変更の登記を嘱託する'),
    ],
    summary_tail='アは「5番の1」と「5番1」の書き方の取り違え、ウは「地番の若い方」という思い込み、オは全部滅失と一部滅失の取り違えを突いた出題です。この問題は正しいものを選ぶ形なので、正解はイとエの組合せになります。',
    supplements=[
        '### 補足説明（ア・ウ）：家屋番号は、敷地の地番をもとに定める\n\n家屋番号は、敷地の地番と同一の番号を基本としますが、建物の数や敷地の数によって決め方が変わります（不動産登記事務取扱手続準則79条）。\n\n| 場面 | 家屋番号の決め方 |\n|---|---|\n| 一筆の土地に一個の建物 | 敷地の地番と同一の番号 |\n| 一筆の土地に二個以上の建物 | 地番に1、2の支号を付けて「5番の1」「5番の2」 |\n| 二筆以上にまたがる一個の建物（附属建物なし） | 床面積の多い部分の存する土地の地番と同一の番号 |\n\n**たとえば**、5番の土地に建物が二つあれば「5番の1」「5番の2」、5番と6番にまたがる建物で6番側の床面積が多ければ「6番」です。',
        '### 補足説明（オ）：河川区域内の土地の登記は、河川管理者が嘱託する\n\n河川区域内の土地について、河川管理者が登記所に嘱託する内容は、場面ごとに決まっています（不動産登記法43条）。\n\n| 場面 | 嘱託する登記 | 条文 |\n|---|---|---|\n| 土地の全部が滅失した | 土地の滅失の登記 | 5項 |\n| 土地の一部が滅失した | 地積に関する変更の登記 | 6項 |\n| 土地の一部が河川区域内の土地となった、又はならなくなった | その旨の登記又は抹消の嘱託に伴い、分筆の登記を代わって嘱託できる | 2項から4項まで |\n\n**たとえば**、河川の流れで土地の全部がなくなれば滅失の登記、一部がなくなれば地積の変更の登記を、河川管理者が嘱託します。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第14日（朝）　択一」とし、note の引用の出典欄は空欄にします。この問題は「正しいものの組合せ」を選ぶ形です。',
        '各肢の根拠のうち、不動産登記法43条2項から6項まで、46条、不動産登記規則112条1項・115条、不動産登記事務取扱手続準則79条は、`note-articles/laws/` 配下の原文で確認しました。',
        'アの「5番1は土地を分筆したときの地番の書き方」は、準則79条2号の例示（家屋番号は「5番の1」、地番が「6番1」であれば「6番1の1」）からの整理で、分筆後の地番の書き方そのものの条文は確認していません。',
        'イ・エ・オの具体例（マンションの一室の測り方、新築マンションの敷地権、川に削られた土地）は、条文をかみ砕いた一般的な例です。',
    ],
    phrases=['家屋番号は「5番の1」と書きます', '区分建物は内側線で測ります', '床面積の多い土地の番号になります', '敷地権は土地にも登記されます', '一部滅失は地積の変更の嘱託です'],
    header=dict(t1='家屋番号と床面積、', t2='どう決まる？', topic='不動産登記法　建物の登記事項',
                kanji='家・屋・番・号・床・面・積・毎'),
    poster_intro='建物の登記事項を、「家屋番号と床面積」（グループA：ア・イ・ウ）と「敷地権と河川区域」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='建物の登記事項を整理', sub='不動産登記法 第43条・第46条、規則 第115条、準則 第79条（毎日ドリル 第14日）',
        col_a='家屋番号と床面積', col_b='敷地権と河川区域', n_a=3,
        cards=[
            dict(h='一筆に二個の建物は「5番の1」「5番の2」',
                 ill='an isometric single land plot with two small buildings on it, each with a number plate in front. The plates read 「5番の1」 and 「5番の2」. A green check mark sits beside the plates.',
                 words=['5番の1', '5番の2'], tag='支号を付ける'),
            dict(h='区分建物の床面積は内側線で測る',
                 ill='a floor plan of a single apartment room with a measuring line drawn along the inside faces of the walls. A label beside the line reads 「内側線」. A green check mark sits beside the line.',
                 words=['内側線'], tag='壁の内側から内側'),
            dict(h='二筆にまたがる建物は床面積の多い土地の番号',
                 ill='an isometric building straddling two land plots drawn side by side. The larger part of the building sits on the right plot, which is highlighted with a green glow. A number plate in front of the right plot reads 「6番」. A green check mark sits beside the plate.',
                 words=['6番'], tag='多い方の地番'),
            dict(h='敷地権は土地の登記記録にも登記される',
                 ill='an isometric apartment building above a land plot with a registry record sheet. A registry officer figure stamps the record sheet with a stamp labeled 「敷地権」. A green check mark sits beside the stamp.',
                 words=['敷地権'], tag='登記官が職権で'),
            dict(h='河川区域内の土地の一部滅失は地積の変更',
                 ill='an isometric land plot beside a river, with one edge washed away by the water. A river manager figure holds a form labeled 「地積変更」. A green check mark sits beside the form.',
                 words=['地積変更'], tag='河川管理者が嘱託'),
        ],
        kanji=kj('家屋番号支号区分建物床面積内側線二筆敷地権河川区域滅失')),
    nb_label='ア・ウ・オ肢', nb_intro='ア・ウ・オの補足説明に合わせた2枚です。1枚目は、家屋番号の決め方を場面ごとに整理します。2枚目は、河川区域内の土地について河川管理者が嘱託する登記を整理します。',
    notebooks=[
        dict(name='家屋番号の決め方', args=dict(
            title='家屋番号は、どう決める？', sub='準則79条（毎日ドリル 第14日 ア・ウ）',
            req='a three-row table-like diagram',
            layout="""IMPORTANT: the three row headers are different strings. Draw them in three different accent colors (blue, green, orange) so they can never be confused or duplicated. Do not draw any cross mark or check mark in this image.

--- THREE ROWS ---
Three horizontal rounded rows stacked vertically, each with a left header box, an icon and a right result box.

ROW 1 (blue accent): header 一筆に一個の建物
Icon: one land plot with one building and a number plate.
Result box: 敷地の地番と同一の番号

ROW 2 (green accent): header 一筆に二個以上の建物
Icon: one land plot with two buildings and two number plates.
Result box: 5番の1、5番の2のように支号を付ける

ROW 3 (orange accent): header 二筆にまたがる一個の建物
Icon: a building straddling two land plots, with the larger part on the right plot.
Result box: 床面積の多い部分の存する土地の地番と同一の番号""",
            callout='一筆の土地に二個以上の建物があるときは、地番に支号を付けて「5番の1」「5番の2」のように定めます。\n二筆にまたがる建物は、床面積の多い部分の存する土地の地番と同一の番号です。',
            footer='不動産登記事務取扱手続準則79条',
            kanji=kj('一筆個建物敷地地番番号支号二筆床面積'), what='table',
            check='confirm the three row headers are three different strings drawn in three different colors, and that no check mark or cross mark appears anywhere, ')),
        dict(name='河川区域内の土地の嘱託', args=dict(
            title='河川区域内の土地が滅失したら？', sub='不動産登記法43条（毎日ドリル 第14日 オ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「全部が滅失」 on the left and 「一部が滅失」 on the right. Draw them large and in different accent colors (orange on the left, blue on the right) so they can never be confused or duplicated. Do not draw any cross mark or check mark in this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (orange accent):
Panel header: 全部が滅失
Scene: an isometric land plot beside a river completely washed away, and a river manager figure holding a form.
Text row: 土地の滅失の登記を嘱託（5項）

RIGHT PANEL (blue accent):
Panel header: 一部が滅失
Scene: an isometric land plot beside a river with one edge washed away, and a river manager figure holding a form.
Text row: 地積に関する変更の登記を嘱託（6項）""",
            callout='河川区域内の土地の全部が滅失したときは、土地の滅失の登記を嘱託します。\n一部が滅失したときは、分筆ではなく、地積に関する変更の登記を嘱託します。',
            footer='不動産登記法43条5項・6項',
            kanji=kj('河川区域土地全部一部滅失登記嘱託地積変更'), what='panels',
            check='confirm the two panel headers are different strings drawn in different accent colors, and that no check mark or cross mark appears anywhere, ')),
    ],
)
