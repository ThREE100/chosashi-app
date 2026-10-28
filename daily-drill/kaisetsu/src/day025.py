D = dict(
    catch='地目は土地の使い方で決まる',
    intro='土地の「地目」（土地の使い道を表す区分）について、変更の登記の申請と、地目の決め方を問う問題です（不動産登記法37条、不動産登記事務取扱手続準則69条）。正しいものの組合せを選びます。\n\nこの記事では、あとから所有者になった人の一月の数え方と、テニスコート、農具小屋、石油タンク、火葬場といった施設の敷地が、宅地になるのか雑種地になるのかを、具体的な場面で確認します。',
    sections={
        'ア': ('地目が変わったあとに買った人は、自分の登記から一月',
               '地目又は地積について変更があった後に所有権の登記名義人となった者は、その者に係る所有権の登記があった日から一月以内に、変更の登記を申請しなければなりません（不動産登記法37条2項）。\n\n本肢は正しいといえます。\n\n**たとえば**、3月1日に畑が宅地に変わったあと、4月10日に買主が所有権の移転の登記を受けたとします。買主の一月は、3月1日からではなく、登記を受けた4月10日から数えます。'),
        'イ': ('宅地に接続していないテニスコートは、雑種地',
               'テニスコートの敷地は、宅地に接続するものは宅地とし、その他は雑種地とします（準則69条9号）。\n\n問題文は「宅地に接続していない」テニスコートを宅地としているので、本肢は誤りです。\n\n**たとえば**、住宅の庭に続いているテニスコートの敷地は宅地です。これに対し、住宅から離れた場所にある、独立したテニスコートの敷地は雑種地になります。'),
        'ウ': ('畑の中でも、永久的設備の農具小屋の敷地は宅地',
               '耕作地の区域内にある農具小屋等の敷地は、その建物が永久的設備と認められるものに限り、宅地とします（準則69条3号）。\n\n本肢は正しいといえます。\n\n**たとえば**、畑のまん中に、しっかりした基礎のある農具小屋が建っているとします。小屋の敷地の部分は、周りが畑でも、宅地になります。永久的設備と認められない小屋は、この規定では宅地とされません。'),
        'エ': ('石油タンクの敷地は、宅地',
               'ガスタンク敷地又は石油タンク敷地は、宅地とします（準則69条10号）。\n\n問題文は、石油タンクが建物に当たらないことを理由に雑種地としていますが、タンクが建物かどうかと、敷地の地目は別の話です。本肢は誤りです。\n\n**たとえば**、石油を貯蔵するタンクが置かれた土地は、タンクそのものは建物として扱われませんが、その敷地の地目は宅地です。'),
        'オ': ('火葬場は、建物があれば構内全部が宅地',
               '火葬場は、構内に建物の設備があるときは構内全部を宅地とし、建物の設備がないときは雑種地とします（準則69条12号）。\n\n問題文は「建物の敷地の部分だけを宅地」としているので、本肢は誤りです。\n\n**たとえば**、建物のほかに駐車場や植え込みがある火葬場でも、構内に建物の設備があれば、構内の全部がひとまとまりで宅地になります。建物がなければ、全体が雑種地です。'),
    },
    summary=[
        ('ア', '正', '地目の変更のあとに所有権の登記名義人となった者は、自分の所有権の登記があった日から一月以内に申請する'),
        ('イ', '誤', '宅地に接続していないテニスコートの敷地は、宅地ではなく雑種地'),
        ('ウ', '正', '耕作地の中の農具小屋の敷地は、永久的設備と認められる建物に限り宅地'),
        ('エ', '誤', '石油タンクの敷地は、雑種地ではなく宅地'),
        ('オ', '誤', '火葬場は、建物の設備があれば、建物の敷地の部分だけでなく構内全部が宅地'),
    ],
    summary_tail='イは「接続しているかどうか」、エは「建物かどうかと地目は別」、オは「構内全部か一部か」を取り違えさせる出題です。施設ごとに、宅地になる条件を確かめましょう。',
    supplements=[
        '### 補足説明（イ・ウ・オ）：宅地になる条件は、施設ごとに決まっている\n\n準則69条は、施設ごとに「どんなときに宅地になるか」を定めています。条件を見落とすと、結論を取り違えます。\n\n- テニスコート：宅地に接続していれば宅地、接続していなければ雑種地。\n- 火葬場：構内に建物の設備があれば構内全部が宅地、なければ雑種地。\n- 耕作地の中の農具小屋：永久的設備と認められる建物に限り、その敷地が宅地。\n\n**たとえば**、同じテニスコートでも、庭続きなら宅地、離れていれば雑種地です。「施設の名前」だけでなく「条件」まで読むことが大切です。',
        '### 補足説明（エ）：建物かどうかと、地目は別の話\n\n石油タンクは、建物としては取り扱われません（準則77条1項2号ア）。しかし、石油タンクの敷地の地目は、宅地です（準則69条10号）。\n\n**たとえば**、「タンクは建物ではないから、敷地は宅地ではない」と考えるのは誤りです。建物かどうかを決める基準と、土地の地目を決める基準は、別々に定められています。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第25日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、法37条2項は `note-articles/laws/` 配下の原文で、準則69条3号・9号・10号・12号、同77条1項2号ア、同82条は準則の原文で確認しました。',
        'ウの「永久的設備と認められない小屋は、この規定では宅地とされない」は、準則69条3号の文言（永久的設備と認められるものに限る）からの一般的な整理です。',
        '各具体例（庭続きのテニスコート、基礎のある農具小屋など）は、条文の文言を日常の場面に置き換えた説明で、個別の事例の判断ではありません。',
    ],
    phrases=['あとから買った人は自分の登記から数えます', '離れたテニスコートは雑種地です', '畑の中の農具小屋は条件つきで宅地です', '石油タンクの敷地は宅地になります', '火葬場は建物があれば構内全部が宅地です'],
    header=dict(t1='地目は、', t2='どう決まる？', topic='不動産登記法　地目の認定',
                kanji='地・目・決・毎・登・記・認・定'),
    poster_intro='地目と変更の登記を、「申請の期限と宅地の判断」（グループA：ア・イ・ウ）と「大きな施設の敷地」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='地目の決め方を整理', sub='不動産登記法37条と準則69条（毎日ドリル 第25日）',
        col_a='期限と宅地の判断', col_b='大きな施設の敷地', n_a=3,
        cards=[
            dict(h='あとから買った人は自分の登記から',
                 ill='a horizontal timeline. On the left a flag labeled 「地目の変更」; further right a second flag labeled 「自分の登記」. A green bracket labeled 「一月以内」 starts at the second flag and extends to the right. The part of the timeline before the second flag is drawn in gray with no bracket.',
                 words=['地目の変更', '自分の登記', '一月以内'], tag='起算日は自分の登記'),
            dict(h='離れたテニスコートは雑種地',
                 ill='an isometric house with a yard on the left, and on the right a tennis court standing alone, clearly separated from the house by a gap. A sign beside the separate court is labeled 「雑種地」. A green check mark sits beside the sign.',
                 words=['雑種地'], tag='接続しなければ雑種地'),
            dict(h='畑の中の農具小屋の敷地は宅地',
                 ill='a green field with a sturdy small shed on a concrete base in the middle. The ground under the shed is highlighted and carries a label 「宅地」, while the surrounding field carries a label 「畑」. A green check mark sits beside the shed.',
                 words=['宅地', '畑'], tag='永久的設備なら宅地'),
            dict(h='石油タンクの敷地は宅地',
                 ill='an isometric oil storage tank standing on a land plot, with the plot outline highlighted and a label 「宅地」 on the ground. A green check mark sits beside the plot.',
                 words=['宅地'], tag='タンクの敷地も宅地'),
            dict(h='火葬場は建物があれば構内全部が宅地',
                 ill='an isometric walled compound containing one building and an open yard. The whole compound, building and yard together, is filled with one uniform color and carries a label 「宅地」. A green check mark sits beside the compound.',
                 words=['宅地'], tag='構内全部が宅地'),
        ],
        kanji='地・目・変・更・登・記・雑・種・宅・畑・農・具・小・屋・石・油・葬・構'.split('・')),
    nb_label='イ・ウ・エ・オ肢', nb_intro='イ・ウ・エ・オの補足説明に合わせた2枚です。1枚目は、施設ごとに宅地になる条件を早見表にします。2枚目は、建物かどうかと地目が別の話であることを左右の対比で示します。',
    notebooks=[
        dict(name='施設ごとの、宅地になる条件', args=dict(
            title='宅地になる条件は、施設ごと', sub='地目の認定（毎日ドリル 第25日 イ・ウ・オ）',
            req='a table',
            layout="""--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Three columns and five data rows. The header row has the column names. Each data row has a small isometric icon at the left of its first cell (a tennis court for rows 1 and 2, a compound with a chimney building for rows 3 and 4, a small shed in a field for row 5). Use exactly these strings, and no others:
Header row: 施設 | 条件 | 地目
Row 1: テニスコート | 宅地に接続している | 宅地
Row 2: テニスコート | 宅地に接続していない | 雑種地
Row 3: 火葬場 | 構内に建物の設備がある | 構内全部が宅地
Row 4: 火葬場 | 構内に建物の設備がない | 雑種地
Row 5: 耕作地の中の農具小屋 | 永久的設備と認められる | 敷地は宅地
The condition cells 「宅地に接続している」 (Row 1) and 「宅地に接続していない」 (Row 2) differ by one word and are different strings; draw them in different accent colors (green and orange). In the same way, draw 「構内に建物の設備がある」 (Row 3) in green and 「構内に建物の設備がない」 (Row 4) in orange.""",
            callout='同じ施設でも、条件しだいで宅地になったり雑種地になったりします。\n施設の名前だけでなく、「接続しているか」「建物の設備があるか」まで読んで、結論を決めます。',
            footer='不動産登記事務取扱手続準則69条',
            kanji='地・目・宅・雑・種・接・続・条・件・施・設'.split('・'), what='table',
            check='confirm the table has exactly 3 columns and 5 data rows, confirm the paired condition cells that differ by one word are in different accent colors, ')),
        dict(name='建物かどうかと、地目は別の話', args=dict(
            title='建物かどうかと、地目は別', sub='石油タンクの敷地（毎日ドリル 第25日 エ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「建物の認定」 on the left and 「地目の認定」 on the right. Draw them in different accent colors (blue and green). Neither panel uses a cross mark; no cross mark anywhere.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 建物の認定
Scene: an isometric oil storage tank standing alone, without any house roof around it.
Result badge: 建物ではない

RIGHT PANEL (green accent):
Panel header: 地目の認定
Scene: the same oil storage tank standing on a land plot whose ground is highlighted and labeled 「宅地」.
Result badge with a green check mark: 敷地は宅地""",
            callout='石油タンクは建物としては扱われませんが、その敷地の地目は宅地です。\n「建物ではないから宅地ではない」と考えるのは誤りです。',
            footer='不動産登記事務取扱手続準則69条10号',
            kanji='建・物・認・定・地・目・宅・敷・石・油'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (建物の認定 on the left and 地目の認定 on the right) in different accent colors and that no cross mark appears anywhere, ')),
    ],
)
