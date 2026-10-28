D = dict(
    catch='牧場は牧場、畑の小屋は宅地',
    intro='土地の地目をどう決めるかを問う問題です（不動産登記事務取扱手続準則69条）。建物が建っていても、その敷地がいつも宅地になるわけではなく、土地がある区域や建物の使い道によって地目が変わります。\n\nこの記事では、牧場地域内の畜舎、畑の中の農具小屋、プール、高圧線の下の土地を順に確かめます。あわせて、地目の変更の登記原因の日付が、いつの日になるのかも整理します。',
    sections={
        'ア': ('牧場地域内の畜舎の敷地は、すべて牧場',
               '牧畜のために使用する建物の敷地、牧草栽培地及び林地等で牧場地域内にあるものは、すべて牧場とします（不動産登記事務取扱手続準則69条4号）。永久的設備と認められる建物でも、宅地にはなりません。\n\n問題文は「宅地とする」としているので、本肢は誤りです。永久的設備の建物に限って宅地とするのは、耕作地の区域内の農具小屋等の場合（同条3号）で、これと取り違えた出題です。\n\n**たとえば**、牧場地域の中に、牛を飼うための頑丈な畜舎を建てたとします。その畜舎の敷地は、宅地ではなく牧場です。畜舎がどれほど立派な建物でも、牧場地域内の牧畜用の建物の敷地は、すべて牧場として扱います。'),
        'イ': ('畑の中の農具小屋は、永久的設備なら宅地',
               '耕作地の区域内にある農具小屋等の敷地は、その建物が永久的設備と認められるものに限り、宅地とします（不動産登記事務取扱手続準則69条3号）。\n\n本肢は正しいといえます。\n\n**たとえば**、畑の真ん中に、農具をしまうための頑丈な小屋を建てた場合、その小屋の敷地は宅地になります。簡単に動かせる仮設の小屋のように、永久的設備と認められないときは、宅地にはなりません。'),
        'ウ': ('宅地に接続するプールの敷地は、宅地',
               'テニスコート又はプールについては、宅地に接続するものは宅地とし、その他は雑種地とします（不動産登記事務取扱手続準則69条9号）。\n\n本肢は正しいといえます。「プールなら雑種地」と覚えていると誤りやすい点です。\n\n**たとえば**、自宅の庭の続きに家族用のプールを設けた場合、その敷地は宅地です。自宅とは離れた別の土地に設けたプールなら、その敷地は雑種地になります。'),
        'エ': ('高圧線の下で雑種地になるのは、使えない区域だけ',
               '高圧線の下の土地のうち、雑種地とするのは「他の目的に使用することができない区域」です（不動産登記事務取扱手続準則69条13号）。\n\n問題文は、居宅が建っている土地を、高圧線の下にあるというだけで雑種地としているので、本肢は誤りです。居宅の敷地として使われている土地は、他の目的に使用できない区域ではなく、宅地です。\n\n**たとえば**、高圧線の下で、建物も建てられず何にも使えない部分は雑種地です。同じ高圧線の下でも、居宅を建てて暮らしている部分は、宅地になります。'),
        'オ': ('地目変更の日付は、許可の日ではなく現況が変わった日',
               '地目の変更の登記は、土地の現況が変わったことを公示する登記です。そのため、登記原因の日付は、農地法の許可があった日ではなく、現況が実際に変わった日になります（実務上の扱いによります）。\n\n問題文は、許可を受けた3月1日を日付としているので、本肢は誤りです。建物の敷地として利用を始めた6月1日が日付です。\n\n**たとえば**、畑の土地について3月1日に許可を受け、造成工事を経て、6月1日に建物の敷地として使い始めたとします。登記原因の日付は、許可の日の3月1日ではなく、使い始めた6月1日です。'),
    },
    summary=[
        ('ア', '誤', '牧場地域内の牧畜用の建物の敷地は、永久的設備の建物でも、すべて牧場とする'),
        ('イ', '正', '耕作地の区域内の農具小屋等の敷地は、永久的設備と認められるものに限り宅地とする'),
        ('ウ', '正', '宅地に接続するプールの敷地は宅地とし、その他は雑種地とする'),
        ('エ', '誤', '高圧線の下で雑種地とするのは、他の目的に使用することができない区域に限られる'),
        ('オ', '誤', '地目変更の登記原因の日付は、許可の日ではなく、現況が変わった日である'),
    ],
    summary_tail='アは「牧場」と「宅地」、エは「使えない区域に限る」という範囲、オは「許可の日」と「現況が変わった日」を入れ替えた出題です。地目は、建物があるかどうかではなく、区域と使い道で決まると覚えておきましょう。',
    supplements=[
        '### 補足説明（ア）：同じ「建物の敷地」でも、区域によって地目が変わる\n\n建物の敷地が、すべて宅地になるわけではありません。どの区域の中にあるかで、地目の決まり方が違います（不動産登記事務取扱手続準則69条）。\n\n- 牧場地域内の、牧畜のために使用する建物の敷地：永久的設備と認められる建物でも、すべて牧場（4号）。\n- 耕作地の区域内の農具小屋等の敷地：永久的設備と認められるものに限り、宅地（3号）。\n\n**たとえば**、牧場地域の畜舎は、頑丈でも敷地は牧場です。畑の中の農具小屋は、頑丈な（永久的設備の）ものなら敷地は宅地、仮設のものなら宅地にはなりません。',
        '### 補足説明（オ）：地目変更の日付は、許可の日でも工事の日でもない\n\n畑を宅地にする場合、時間の流れの中には、いくつかの節目があります。\n\n- 農地法の許可を受けた日：許可があっただけで、現況はまだ畑。\n- 造成工事をしている間：現況はまだ宅地になっていない。\n- 建物の敷地として利用を始めた日：現況が宅地に変わった日。\n\n登記原因の日付になるのは、最後の「現況が宅地に変わった日」です（実務上の扱いによります）。\n\n**たとえば**、3月1日に許可を受け、造成工事をして、6月1日に建物の敷地として使い始めたなら、登記原因の日付は6月1日です。一月以内の申請の期限も、この日から数えます（不動産登記法37条1項）。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第115日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記事務取扱手続準則69条3号・4号・9号・13号と、不動産登記法37条1項は、`note-articles/laws/` 配下の原文で確認しました。',
        'オの「登記原因の日付は、農地法の許可の日ではなく、現況が変わった日」は、条文には書かれていない実務上の扱いで、条文からの一般的な整理です。先例・通達の原文は未確認です。',
        'ア・イ・ウ・エ・オの具体例（畜舎、農具小屋、庭のプール、高圧線の下の居宅、許可から利用開始までの流れ）は、条文の文言を日常の場面に置き換えた説明で、個別の先例の確認はしていません。',
    ],
    phrases=['牧場地域の建物の敷地は牧場です', '畑の中の農具小屋は宅地になることも', '自宅に接続するプールは宅地です', '高圧線の下でも居宅の敷地は宅地です', '地目変更の日は現況が変わった日です'],
    header=dict(t1='この敷地の地目は、', t2='何になる？', topic='不動産登記　地目の認定',
                kanji='地・目・敷・不・動・産・登・記・認・定・毎'),
    poster_intro='地目の認定を、「建物やプールの敷地」（グループA：ア・イ・ウ）と「雑種地の範囲と変更の日付」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='地目の認定と変更の日付を整理', sub='不動産登記事務取扱手続準則 第69条（毎日ドリル 第115日）',
        col_a='建物やプールの敷地', col_b='雑種地の範囲と日付', n_a=3,
        cards=[
            dict(h='牧場地域内の畜舎の敷地は牧場',
                 ill='an isometric pasture area with a sturdy barn building on a green field, and a small signpost beside the barn labeled 「牧場」. A green check mark sits beside the signpost.',
                 words=['牧場'], tag='敷地はすべて牧場'),
            dict(h='畑の中の頑丈な農具小屋は宅地',
                 ill='an isometric crop field with rows of plants and a sturdy tool shed in the middle. The ground under the shed is outlined in warm beige, and a small signpost beside it is labeled 「宅地」. A green check mark sits beside the signpost.',
                 words=['宅地'], tag='永久的設備なら宅地'),
            dict(h='自宅につながるプールの敷地は宅地',
                 ill='an isometric house with a garden and a small swimming pool directly next to it, both inside one shared outline. A small signpost beside the pool is labeled 「宅地」. A green check mark sits beside the signpost.',
                 words=['宅地'], tag='接続すれば宅地'),
            dict(h='雑種地は使えない区域だけ',
                 ill='an isometric land plot crossed by overhead high-voltage power lines on a tower. The empty strip directly under the lines is outlined and carries a small signpost labeled 「雑種地」. A house sits on the other part of the plot, with a small signpost labeled 「宅地」. A green check mark sits beside the house.',
                 words=['雑種地', '宅地'], tag='使えない区域だけ雑種地'),
            dict(h='地目変更の日は現況が変わった日',
                 ill='a horizontal timeline. On the left a faded gray flag labeled 「許可」; further right a bright green flag labeled 「利用開始」 with a house under construction turning into a finished house. A green check mark sits beside the right flag.',
                 words=['許可', '利用開始'], tag='現況が変わった日'),
        ],
        kanji='牧・場・宅・地・雑・種・高・圧・線・許・可・利・用・開・始・接・続'.split('・')),
    nb_label='ア・オ肢', nb_intro='ア・オの補足説明に合わせた2枚です。1枚目は、牧場地域内と耕作地の区域内の違いを左右の対比で示します。2枚目は、地目変更の登記原因の日付が、いつの日になるのかを時間の流れで示します。',
    notebooks=[
        dict(name='牧場地域内と耕作地の区域内の違い', args=dict(
            title='建物の敷地の地目は、区域で決まる', sub='牧場地域内と耕作地の区域内（毎日ドリル 第115日 ア）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「牧場地域内」 on the left and 「耕作地の区域内」 on the right. Draw them in different accent colors (green and blue) so they can never be confused or duplicated. Do not draw any check mark or cross mark in this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (green accent):
Panel header: 牧場地域内
Scene: an isometric pasture with a sturdy barn building and a small signpost beside it labeled 牧場.
Result badge: 永久的設備でも、すべて牧場

RIGHT PANEL (blue accent):
Panel header: 耕作地の区域内
Scene: an isometric crop field with a sturdy tool shed beside a small signpost labeled 宅地, and a faded flimsy temporary shed with no signpost.
Result badge: 永久的設備に限り宅地""",
            callout='牧場地域内の牧畜用の建物の敷地は、永久的設備の建物でも、すべて牧場です。\n永久的設備の建物に限って宅地になるのは、耕作地の区域内の農具小屋等です。',
            footer='不動産登記事務取扱手続準則69条3号・4号',
            kanji='牧・場・耕・作・地・域・内・永・久・的・設・備・宅・登・記'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (牧場地域内 on the left and 耕作地の区域内 on the right) drawn in different accent colors, and that no check mark or cross mark appears, ')),
        dict(name='地目変更の登記原因の日付', args=dict(
            title='地目変更の日付は、いつの日？', sub='畑から宅地への地目変更（毎日ドリル 第115日 オ）',
            req='a timeline diagram',
            layout="""--- TIMELINE ---
Render as a clean flat-design horizontal timeline with three flags from left to right.
Left flag labeled 3月1日, with an icon of an approval stamp and the label 農地法の許可. Below it, a faded gray tag labeled 日付ではない.
Middle flag with an icon of an excavator and the label 造成工事.
Right flag labeled 6月1日, with an icon of a house on a plot and the label 建物の敷地として利用開始. Below it, a bright green tag with a calendar icon labeled 登記原因の日付.
Use exactly these strings, and no others, for the labels. The gray tag and the green tag are different strings; draw them in different colors.""",
            callout='地目の変更の登記原因の日付は、農地法の許可があった日ではなく、現況が実際に変わった日です。\n建物の敷地として利用を始めた日が、登記原因の日付になります。',
            footer='不動産登記法37条1項',
            kanji='農・地・法・許・可・造・成・工・事・建・物・敷・利・用・開・始・登・記・原・因・日・付'.split('・'), what='timeline',
            check='confirm the gray tag and the green tag are different strings in different colors, and that the green tag sits under the right flag, ')),
    ],
)
