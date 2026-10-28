def _k(*t, n=24):
    out = []
    for c in ''.join(t):
        if '一' <= c <= '龥' and c not in out:
            out.append(c)
    return out[:n]


_T1, _T2, _TOP = '建物を合併するとき、', '記録はどうなる？', '不動産登記法　建物の合併と区分'
_cards = [
    dict(h='賃借権があると合併できない',
         ill='two isometric houses side by side, each with a record sheet attached that carries a line labeled 「賃借権」. A thin arrow tries to join the two houses but is stopped by a small barrier between them. A green check mark sits beside the barrier.',
         words=['賃借権'], tag='内容が同じでも合併できない'),
    dict(h='附属合併は二通りの言葉で記録する',
         ill='two isometric record sheets. The smaller sheet on the left carries a tag labeled 「に合併」 and is stamped closed. The larger sheet on the right carries a tag labeled 「を合併」. A thin arrow runs from the left sheet to the right sheet. A green check mark sits beside the right sheet.',
         words=['に合併', 'を合併'], tag='合併される側と、する側'),
    dict(h='合併後の家屋番号は上位のもの',
         ill='an isometric scene of two houses on the left with two house number plates, joined by an arrow into one larger house on the right. The upper plate is highlighted with a green glow and labeled 「上位」. A green check mark sits beside the larger house.',
         words=['上位'], tag='相当でなければ他の番号も可'),
    dict(h='附属合併は離れていても合併できる',
         ill='an isometric scene of a main building on the left and a smaller building on the right, separated by an open space. A thin dotted line labeled 「主従」 connects the two buildings. A green check mark sits beside the dotted line.',
         words=['主従'], tag='区分合併は接続が必要'),
    dict(h='非区分の建物の区分は新しい登記記録',
         ill='an isometric record sheet on the left stamped with a round stamp labeled 「閉鎖」, and two new clean record sheets on the right connected to it by arrows. A green check mark sits beside the two new sheets.',
         words=['閉鎖'], tag='区分前の記録は閉鎖する'),
]

D = dict(
    catch='附属合併の記録と、合併できる条件',
    intro='建物の合併の登記と区分の登記について、できる場合・できない場合と、登記記録にどう記録されるのかを問う問題です（不動産登記法56条、不動産登記規則129条・131条、不動産登記事務取扱手続準則79条・86条・98条）。この問題は、正しいものの組合せを選びます。\n\nこの記事では、合併の登記の制限、附属合併の記録の言葉、区分の登記で登記記録がどうなるかを、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('賃借権の登記があると、内容が同じでも合併の登記はできない',
               '所有権等の登記以外の権利に関する登記がある建物の合併の登記は、することができません（不動産登記法56条5号）。\n\n例外として、合併後の登記記録に登記できるのは、同一の担保権の登記と、登記事項が同一の信託の登記だけです（不動産登記規則131条）。賃借権は、この例外に含まれていません。\n\n問題文は、賃借権の登記が同一なら合併できるとしているので、本肢は誤りです。\n\n**たとえば**、甲建物にも乙建物にも、同じ内容の賃借権の設定の登記があったとしても、甲建物と乙建物の合併の登記はできません。同一の担保権（抵当権など）であれば、合併できる場合があります。'),
        'イ': ('附属合併では、合併される建物に「に合併」、合併する建物に「を合併」と記録する',
               '甲建物を乙建物の附属建物とする附属合併の登記では、甲建物の登記記録の表題部の原因及びその日付欄に「何番に合併」と記録します。乙建物の登記記録の表題部の原因及びその日付欄には「何番を合併」と記録します（不動産登記事務取扱手続準則98条1項・2項）。\n\n本肢は正しいといえます。\n\n**たとえば**、家屋番号5番の乙建物に、家屋番号6番の甲建物を附属建物として合併する場合、甲建物の登記記録には「5番に合併」、乙建物の登記記録には「6番を合併」と記録されます。'),
        'ウ': ('合併後の家屋番号は、原則として、上位のもの',
               '建物の合併の登記をする場合には、合併前の建物の家屋番号のうち上位のものをもって、合併後の家屋番号とします。上位の家屋番号によることが相当でない場合は、他の番号を用いて差し支えありません（不動産登記事務取扱手続準則79条9号）。\n\n問題文は「下位のもの」としているので、本肢は誤りです。\n\n**たとえば**、家屋番号が「7番の1」の建物と「7番の2」の建物を合併するときは、原則として、上位の「7番の1」が合併後の家屋番号になります。'),
        'エ': ('区分建物でも、主従の関係があれば、接続していなくても附属合併ができる',
               '附属合併ができない場合は、合併しようとする建物が主たる建物と附属建物の関係にないときです（不動産登記事務取扱手続準則86条1号）。建物が互いに接続していないことが理由で合併できなくなるのは、区分合併の場合です（同条2号）。\n\n本肢は正しいといえます。\n\n**たとえば**、区分建物である乙建物（居宅）と、離れて建つ区分建物である甲建物（物置）が、主たる建物と附属建物の関係にあるなら、接続していなくても、甲建物を乙建物の附属建物とする合併の登記ができます。'),
        'オ': ('区分建物でない建物を区分するときは、区分後の各建物に新しく登記記録を作る',
               '登記官は、区分建物でない甲建物を区分して甲建物と乙建物とする建物の区分の登記をするときは、区分後の各建物について新たに登記記録を作成します。区分前の甲建物の登記記録は、閉鎖します（不動産登記規則129条1項・2項）。\n\n問題文は、乙建物についてだけ新たに登記記録を作り、甲建物の登記記録をそのまま用いるとしているので、本肢は誤りです。\n\n**たとえば**、1棟の建物を2つに区分するとき、元の1つの登記記録は閉鎖され、区分後の2つの建物に新しい登記記録が作られます。'),
    },
    summary=[
        ('ア', '誤', '賃借権の登記がある建物は、内容が同じでも合併の登記ができない（例外は同一の担保権など）'),
        ('イ', '正', '附属合併では、合併される建物に「に合併」、合併する建物に「を合併」と記録する'),
        ('ウ', '誤', '合併後の家屋番号は、原則として上位のもの（下位ではない）'),
        ('エ', '正', '附属合併は主従の関係があればよく、接続していなくてもできる'),
        ('オ', '誤', '区分建物でない建物を区分するときは、区分後の各建物に新しく登記記録を作り、区分前の記録は閉鎖する'),
    ],
    summary_tail='アは「担保権」と「賃借権」、ウは「上位」と「下位」、オは「新たに作る登記記録の範囲」を入れ替えた出題です。附属合併と区分合併、区分建物と非区分建物の区分を、それぞれ分けて整理しましょう。',
    supplements=[
        '### 補足説明（ア）：合併の登記ができない場合と、その例外\n\n法56条は、合併の登記ができない場合を5つ定めています。\n\n| 号 | 合併の登記ができない場合 |\n|---|---|\n| 1号 | 共用部分である旨の登記などがある建物 |\n| 2号 | 表題部所有者又は所有権の登記名義人が互いに異なる建物 |\n| 3号 | 表題部所有者又は所有権の登記名義人の持分が互いに異なる建物 |\n| 4号 | 所有権の登記がない建物と、ある建物 |\n| 5号 | 所有権等の登記以外の権利に関する登記がある建物（例外あり） |\n\n5号の例外は、規則131条で、同一の担保権の登記（登記の目的、受付の年月日及び受付番号、登記原因及びその日付が同一のもの）と、登記事項が同一の信託の登記に限られます。\n\n**たとえば**、同じ内容の抵当権が両方の建物に付いていれば合併できる場合がありますが、同じ内容の賃借権が付いていても、合併はできません。',
        '### 補足説明（オ）：建物の区分の登記で、登記記録がどうなるか\n\n建物の区分の登記は、区分する建物が区分建物かどうかで、登記記録の扱いが違います（規則129条）。\n\n| 区分する建物 | 登記記録の扱い | 根拠 |\n|---|---|---|\n| 区分建物でない建物（甲を甲と乙に区分） | 区分後の各建物に新たに登記記録を作り、区分前の甲の登記記録は閉鎖する | 1項・2項 |\n| 区分建物である建物（甲を甲と乙に区分） | 乙についてだけ新たに登記記録を作る。甲の登記記録は、残余部分の建物の記録として残る | 3項・4項 |\n\n**たとえば**、マンションの一室を2つに区分するときは、新しくできる部屋の登記記録だけを新たに作ります。一方、一戸建てのような区分建物でない建物を2つに区分するときは、両方とも新しい登記記録になります。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第94日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法56条、不動産登記規則129条・131条、不動産登記事務取扱手続準則79条9号・86条・98条は、`note-articles/laws/` 配下の原文で確認しました。',
        'イの具体例は、準則98条の「何番に合併」「何番を合併」の言葉に沿って作った例です。附属合併で、どちらの建物の家屋番号が残るのかは、この記事では扱っていません。',
        'オの補足説明の「甲の登記記録は、残余部分の建物の記録として残る」は、規則129条4項（甲建物の登記記録の表題部に残余部分の建物の表題部の登記事項などを記録する）に基づく整理です。',
    ],
    phrases=['賃借権があると合併できません', '附属合併はに合併とを合併です', '合併後の家屋番号は上位のものです', '附属合併は離れていてもできます', '非区分の建物の区分は新しい記録です'],
    header=dict(t1=_T1, t2=_T2, topic=_TOP, kanji='・'.join(_k(_T1, _T2, _TOP))),
    poster_intro='建物の合併と区分の登記を、「合併の制限と記録」（グループA：ア・イ・ウ）と「接続の要否と区分の登記」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='建物の合併と区分を整理', sub='不動産登記法 第56条、規則 第129条・第131条、準則 第79条・第86条・第98条（毎日ドリル 第94日）',
        col_a='合併の制限と記録', col_b='接続の要否と区分の登記', n_a=3,
        cards=_cards,
        kanji=_k(*[c['h'] + c['tag'] + ''.join(c['words']) for c in _cards], '建物の合併と区分を整理合併の制限と記録接続の要否と区分の登記', n=24)),
    nb_label='ア・オ肢', nb_intro='ア・オの補足説明に合わせた2枚です。1枚目は、合併の登記ができない場合と例外を表で整理します。2枚目は、区分建物でない建物と区分建物の区分の登記で、登記記録の扱いがどう違うかを左右の対比で示します。',
    notebooks=[
        dict(name='合併の登記ができない場合と例外', args=dict(
            title='合併の登記ができない場合', sub='不動産登記法56条（毎日ドリル 第94日 ア）',
            req='a five-row table with an exception box',
            layout="""--- TABLE ---
A table with five rows. Each row has the item on the left and a short note on the right. Rows 1 to 4 use a blue accent. Row 5 uses an orange accent and is highlighted.
Row 1: 共用部分である旨の登記などがある建物
Row 2: 表題部所有者又は所有権の登記名義人が互いに異なる建物
Row 3: 表題部所有者又は所有権の登記名義人の持分が互いに異なる建物
Row 4: 所有権の登記がない建物と、ある建物
Row 5: 所有権等の登記以外の権利に関する登記がある建物

--- EXCEPTION BOX (green accent, placed under row 5) ---
Box header: 合併できる例外（規則131条）
Items:
同一の担保権の登記
登記事項が同一の信託の登記
Beside the box, a small isometric icon of two houses with the same mortgage sheet attached. A separate small note, in gray: 賃借権は例外に入らない
Do not use check marks or crosses.""",
            callout='所有権等の登記以外の権利に関する登記がある建物は、合併できません。例外は、同一の担保権の登記と、登記事項が同一の信託の登記だけです。\n賃借権は、内容が同じでも例外に入りません。',
            footer='不動産登記法56条、不動産登記規則131条',
            kanji='・'.join(_k('合併登記共用部分表題部所有者名義人持分異所有権担保権信託賃借権例外同一不動産法規則')), what='table',
            check='confirm that rows 1 to 4 are drawn in blue and row 5 in orange, that the exception box is drawn in green, and that the sentence 賃借権は例外に入らない is copied verbatim, ')),
        dict(name='建物の区分の登記と登記記録', args=dict(
            title='区分の登記で登記記録はどうなる？', sub='不動産登記規則129条（毎日ドリル 第94日 オ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「区分建物でない建物を区分」 on the left and 「区分建物を区分」 on the right; draw them in different accent colors (blue and green) so they can never be confused or duplicated. Do not use check marks or crosses.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 区分建物でない建物を区分
Scene: one record sheet labeled 「甲」 at the top, with arrows going down to two new record sheets labeled 「甲」 and 「乙」. The top sheet carries a round stamp labeled 「閉鎖」.
Rule text: 区分後の各建物に新たに登記記録を作り、区分前の登記記録は閉鎖する

RIGHT PANEL (green accent):
Panel header: 区分建物を区分
Scene: one record sheet labeled 「甲」 remains in place, and an arrow leads to one new record sheet labeled 「乙」.
Rule text: 乙についてだけ新たに登記記録を作る。甲の登記記録は残る""",
            callout='区分建物でない建物を区分するときは、区分後の両方に新しい登記記録を作り、区分前の記録は閉鎖します。\n区分建物を区分するときは、新しくできる乙だけに新しい登記記録を作り、甲の記録は残ります。',
            footer='不動産登記規則129条1項から4項',
            kanji='・'.join(_k('区分建物登記記録新閉鎖甲乙残不動産規則')), what='panels',
            check='confirm the two panel headers are different strings (区分建物でない建物を区分 on the left and 区分建物を区分 on the right) and that the labels 甲 and 乙 are copied verbatim, ')),
    ],
)
