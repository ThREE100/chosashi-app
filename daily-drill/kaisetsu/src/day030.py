D = dict(
    catch='合併できる抵当権、閉鎖される登記記録',
    intro='建物の合併・分割・区分の登記について、合併の制限の例外、附属合併の記録、一の申請情報で申請できる場合、区分の登記の記録を問う問題です（不動産登記法56条、不動産登記規則35条・129条・131条・132条）。正しいものの組合せを選びます。\n\nこの記事では、抵当権があるときに建物の合併ができる場合、附属合併でどちらの登記記録が残るか、区分の登記で従前の登記記録がどうなるかを、具体的な場面で確認します。',
    sections={
        'ア': ('同じ内容の抵当権が両方にあるなら、合併できる',
               '所有権等の登記以外の権利に関する登記がある建物の合併は、原則としてできません（不動産登記法56条5号）。ただし、担保権の登記で、登記の目的、申請の受付の年月日及び受付番号、並びに登記原因及びその日付が同一のものは、合併後の建物の登記記録に登記できるので、合併の制限に当たりません（不動産登記規則131条1号）。\n\n本肢は正しいといえます。\n\n**たとえば**、同じ銀行のために、同じ日に同じ受付番号で、同じ原因による抵当権が甲建物と乙建物の両方に登記されているなら、甲建物を乙建物の附属建物とする合併の登記を申請できます。'),
        'イ': ('抵当権が片方だけにあるときは、合併できない',
               '一方の建物にだけ抵当権の登記があるときは、規則131条の「同一のもの」に当たらないので、合併の登記はできません（不動産登記法56条5号）。\n\n問題文は、甲建物にだけ抵当権がある場合でも合併の登記を申請できるとしているので、本肢は誤りです。\n\n**たとえば**、甲建物だけが銀行の抵当に入っていて、乙建物には抵当権がないとします。この状態のまま、2棟を1個の建物にまとめる合併の登記はできません。'),
        'ウ': ('附属合併では、主である乙建物の登記記録に記録し、甲を閉鎖する',
               '甲建物を乙建物の附属建物とする附属合併では、登記官は、乙建物の登記記録の表題部に、附属合併後の建物の表題部の登記事項と、甲建物を合併した旨を記録します。そして、甲建物の登記記録は、閉鎖します（不動産登記規則132条1項・3項）。\n\n問題文は、甲建物の登記記録に合併後の事項を記録し、乙建物の登記記録を閉鎖するとしているので、甲と乙が逆です。本肢は誤りです。\n\n**たとえば**、小さな物置（甲）を母屋（乙）の附属建物にまとめるなら、母屋の登記記録が残り、物置の登記記録は閉鎖されます。'),
        'エ': ('分割と合併は、一の申請情報で申請できる',
               '甲建物の附属建物を分割して、これを乙建物の附属建物としようとする場合には、建物の分割の登記と建物の合併の登記を、一の申請情報で申請できます（不動産登記規則35条2号）。\n\n本肢は正しいといえます。\n\n**たとえば**、同じ持ち主Aの甲建物にある附属建物（離れ）を切り離し、同じ持ち主Aの乙建物の附属建物として付け替えたいとします。この付け替えは、1つの申請書でまとめて申請できます。'),
        'オ': ('区分建物でない建物を区分すると、従前の登記記録は閉鎖する',
               '区分建物でない甲建物を区分して甲建物と乙建物にするときは、区分後の各建物について新たに登記記録を作成し、区分前の登記記録は閉鎖します（不動産登記規則129条1項・2項）。\n\n問題文は、甲建物には従前の登記記録が用いられるとしているので、本肢は誤りです。従前の登記記録を残して使うのは、区分建物である甲建物を区分する場合です（同条3項・4項）。\n\n**たとえば**、一戸建ての住宅を2つに区分したときは、2つとも新しい登記記録になり、もとの登記記録は閉鎖されます。'),
    },
    summary=[
        ('ア', '正', '抵当権の登記の目的、受付、原因が同一なら、合併の制限に当たらない'),
        ('イ', '誤', '抵当権の登記が片方の建物にしかないときは、合併の登記はできない'),
        ('ウ', '誤', '附属合併では、主である乙建物の登記記録に記録し、附属建物となる甲建物の登記記録を閉鎖する'),
        ('エ', '正', '附属建物の分割と、他の建物への合併は、一の申請情報で申請できる'),
        ('オ', '誤', '区分建物でない建物の区分では、区分後の各建物に新しい登記記録を作り、従前のものは閉鎖する'),
    ],
    summary_tail='イは「同一のもの」という例外の当てはめの誤り、ウは甲と乙の入れ替え、オは区分建物かどうかの取り違えです。合併の制限は例外の条件を、記録は「どの登記記録に残るか」を確かめましょう。',
    supplements=[
        '### 補足説明（ア・イ）：抵当権があるとき、合併できる場合とできない場合\n\n建物に所有権以外の権利の登記があると、合併は原則できません。ただし、担保権の登記で次の3つが同一なら、例外的に合併できます（不動産登記規則131条1号）。\n\n- 登記の目的。\n- 申請の受付の年月日及び受付番号。\n- 登記原因及びその日付。\n\n**たとえば**、甲乙の両方に、同じ日に同じ受付番号で、同じ原因の抵当権が登記されていれば合併できます。片方にしかない、または受付番号が違うなら、合併できません。',
        '### 補足説明（ウ）：附属合併で、残る登記記録と閉鎖される登記記録\n\n附属合併では、「主」になる建物の登記記録が残り、「附属」になる建物の登記記録は閉鎖されます（不動産登記規則132条）。\n\n- 主になる乙建物：表題部に、合併後の建物の表題部の登記事項と、甲建物を合併した旨を記録する。\n- 附属建物になる甲建物：表題部に、乙建物に合併した旨と、従前の表題部の登記事項を抹消する記号を記録し、登記記録を閉鎖する。\n\n**たとえば**、物置（甲）を母屋（乙）の附属建物にまとめたら、母屋の登記記録だけが残ります。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第30日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法56条5号、不動産登記規則35条2号・129条1項から4項まで・131条1号・132条1項・3項は、`note-articles/laws/` 配下の原文で確認しました。',
        'エの一の申請情報は、不動産登記令4条ただし書に基づき規則35条が定める場合の一つです。令4条ただし書の条文自体は、この記事の作成では確認していません。',
        '各具体例（同じ銀行の抵当権、物置と母屋、一戸建ての区分など）は、条文の文言を日常の場面に置き換えた説明で、個別の事例の判断ではありません。',
    ],
    phrases=['同じ内容の抵当権なら合併できます', '片方だけの抵当権では合併できません', '附属合併では主である建物の記録が残ります', '附属建物の付け替えは一つの申請でできます', '区分すると新しい登記記録を作ります'],
    header=dict(t1='合併・区分で、', t2='登記記録は？', topic='不動産登記法　建物の合併と区分',
                kanji='合・併・区・分・登・記・毎'),
    poster_intro='建物の合併・分割・区分の登記を、「合併の制限と附属合併」（グループA：ア・イ・ウ）と「申請と区分の記録」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='建物の合併と区分を整理', sub='不動産登記法56条と不動産登記規則35条から132条まで（毎日ドリル 第30日）',
        col_a='合併の制限と附属合併', col_b='申請と区分の記録', n_a=3,
        cards=[
            dict(h='同じ抵当権なら合併できる',
                 ill='two isometric buildings, labeled 「甲建物」 and 「乙建物」, each carrying an identical small lock-shaped stamp on its wall, with an equals sign between the two stamps. A green arrow joins the two buildings into one. A green check mark sits beside the arrow.',
                 words=['甲建物', '乙建物'], tag='同一なら合併可'),
            dict(h='抵当権が片方だけなら合併できない',
                 ill='two isometric buildings, labeled 「甲建物」 and 「乙建物」. Only the left building carries a lock-shaped stamp on its wall, and the right building has none. A gray arrow between them is blocked by a small barrier. No check mark and no cross mark on this card.',
                 words=['甲建物', '乙建物'], tag='片方だけは不可'),
            dict(h='附属合併は主である建物の記録が残る',
                 ill='two record sheets, the left labeled 「甲建物」 drawn faded with a closed-folder icon on it, and the right labeled 「乙建物」 drawn bright and thick with the merged contents. A green arrow points from the left sheet to the right sheet. A green check mark sits beside the right sheet.',
                 words=['甲建物', '乙建物'], tag='主の記録が残る'),
            dict(h='附属建物の付け替えは一つの申請',
                 ill='an isometric annex building moving by a curved green arrow from the left main building to the right main building, with one single form stapled above the arrow labeled 「一の申請情報」. A green check mark sits beside the form.',
                 words=['一の申請情報'], tag='分割と合併を一括'),
            dict(h='区分すると新しい登記記録を作る',
                 ill='one isometric house on the left dividing into two houses on the right through a dotted line, with two fresh record sheets under the two houses and an old record sheet at the far left drawn faded with a closed-folder icon. A green check mark sits beside the two new sheets.',
                 words=[], tag='従前の記録は閉鎖'),
        ],
        kanji='合・併・甲・乙・建・物・抵・当・権・附・属・申・請・情・報・区・分'.split('・')),
    nb_label='ア・イ・ウ肢', nb_intro='ア・イ・ウの補足説明に合わせた2枚です。1枚目は、抵当権があるとき合併できる場合とできない場合を左右の対比で示します。2枚目は、附属合併で残る登記記録と閉鎖される登記記録を対比で示します。',
    notebooks=[
        dict(name='抵当権があるとき、合併できる場合とできない場合', args=dict(
            title='抵当権があっても合併できる？', sub='建物の合併の制限（毎日ドリル 第30日 ア・イ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two sides must show OPPOSITE marks, not the same mark. The left side shows a green check mark; the right side shows a red cross. The two panel headers are different strings: 「両方に同じ抵当権」 on the left and 「片方だけに抵当権」 on the right; draw them in different accent colors (blue and gray) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 両方に同じ抵当権
Scene: an isometric scene of two buildings, 甲建物 and 乙建物, each carrying an identical lock-shaped stamp; between the stamps, a small equals sign.
Result badge with a green check mark: 合併できる

RIGHT PANEL (gray accent):
Panel header: 片方だけに抵当権
Scene: an isometric scene of two buildings, 甲建物 with a lock-shaped stamp and 乙建物 without any stamp.
Result badge with a red cross: 合併できない""",
            callout='抵当権があっても、登記の目的、受付の年月日と受付番号、登記原因とその日付が同一なら、合併できます。\n片方の建物にしかない抵当権は、同一とは言えないので、合併できません。',
            footer='不動産登記法56条5号、不動産登記規則131条',
            kanji='合・併・抵・当・権・建・物・甲・乙・登・記'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (両方に同じ抵当権 on the left and 片方だけに抵当権 on the right) and that the left panel shows a green check mark while the right panel shows a red cross, ')),
        dict(name='附属合併で残る登記記録と閉鎖される登記記録', args=dict(
            title='附属合併で、どちらが残る？', sub='附属合併の登記（毎日ドリル 第30日 ウ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: neither panel uses a cross mark; no cross mark anywhere. The two panel headers differ by one character, 「附属建物になる甲」 and 「主になる乙」; they are NOT the same string. Draw them in different accent colors (gray and blue) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (gray accent):
Panel header: 附属建物になる甲
Scene: an isometric scene of a small shed with a record sheet beside it drawn faded, with a closed-folder icon on the sheet.
Result badge: 登記記録を閉鎖

RIGHT PANEL (blue accent):
Panel header: 主になる乙
Scene: an isometric scene of a main house with a thick record sheet beside it, labeled with the merged contents.
Result badge with a green check mark: 合併後の事項を記録""",
            callout='附属合併では、主になる乙建物の登記記録に合併後の事項を記録します。\n附属建物になる甲建物の登記記録は、乙建物に合併した旨を記録して閉鎖します。',
            footer='不動産登記規則132条',
            kanji='附・属・合・併・主・登・記・閉・鎖・甲・乙'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (附属建物になる甲 on the left and 主になる乙 on the right) in different accent colors and that no cross mark appears anywhere, ')),
    ],
)
