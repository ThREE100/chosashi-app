D = dict(
    catch='地目の変更日は、許可の日ではない',
    intro='地目の認定と、地目の変更の登記を問う問題です（不動産登記法37条、不動産登記事務取扱手続準則68条・69条）。地目とは、土地の主な使い道による分類のことで、田、畑、宅地、雑種地などがあります。\n\nこの記事では、変更の登記の原因となる日、申請する人と期間、高圧線の下の土地の地目、数回変わったときの申請の仕方を、具体的な場面で確かめていきましょう。',
    sections={
        'ア': ('原因の日付は、許可の日ではなく、現況が変わった日',
               '地目は、土地の現況と利用目的に重点を置いて定めます（不動産登記事務取扱手続準則68条）。地目の変更の登記は「変更があった日」から一月以内に申請するもので（不動産登記法37条1項）、この日は、土地の現況が実際に変わった日です。\n\n問題文は、農地法の許可を受けた6月1日を原因の日付としているので、本肢は誤りです。\n\n**たとえば**、6月1日に農地転用の許可を受けても、土地は畑のままです。8月1日に造成工事が終わって住宅の敷地になった日に、はじめて地目が変わったといえます。'),
        'イ': ('地目の変更の登記を申請するのは、所有権の登記名義人',
               '地目の変更があったときに、変更の登記を申請しなければならないのは、表題部所有者又は所有権の登記名義人です（不動産登記法37条1項）。\n\n本肢は正しいといえます。現況を変えたのが地上権者のBであっても、申請する人はAです。\n\n**たとえば**、地上権を持つBさんが山林を切り開いて建物の敷地にした場合でも、土地の持ち主である所有権の登記名義人のAさんが、地目を山林から宅地に変える登記を申請します。'),
        'ウ': ('変更の後に名義人となった人は、自分の登記の日から数える',
               '地目の変更があった後に所有権の登記名義人となった者は、その所有権の登記があった日から一月以内に、変更の登記を申請しなければなりません（不動産登記法37条2項）。\n\n本肢は正しいといえます。Bさんの一月は、変更の日からではなく、Bさんの所有権の登記があった日から数えます。\n\n**たとえば**、畑が宅地に変わったあと、その登記がされないまま、BさんがAさんから土地を買って所有権の移転の登記を受けたとします。Bさんは、その移転の登記の日から一月以内に、地目の変更の登記を申請します。'),
        'エ': ('居宅の敷地になっている土地は、高圧線の下でも宅地',
               '雑種地とされるのは、高圧線の下の土地で、他の目的に使用することができない区域です（不動産登記事務取扱手続準則69条13号）。建物の敷地とその維持や効用に必要な土地は、宅地です（同準則68条3号）。\n\n問題文の甲土地は、居宅の敷地として使われているので、雑種地ではなく宅地です。本肢は誤りです。\n\n**たとえば**、上空に高圧線が通っていても、その下に家が建って暮らしている土地は、宅地です。雑種地になるのは、高圧線があるために他の使い方ができない区域です。'),
        'オ': ('数回変わっていても、登記記録上の地目から一度に申請できる',
               '地目が田から雑種地、雑種地から宅地へと、何度も変わっていても、変更の登記は、登記記録上の地目から現在の地目への変更として、一度に申請することができます。途中の地目を一つずつ登記する必要はありません。\n\n問題文は「雑種地への変更の登記をした後でなければ、宅地への変更の登記を申請できない」としているので、本肢は誤りです。\n\n**たとえば**、登記記録上は田のままの土地が、実際には雑種地を経て宅地になっていた場合、田から宅地への変更として、一度に申請します。'),
    },
    summary=[
        ('ア', '誤', '地目の変更の原因の日付は、許可の日ではなく、現況が実際に変わった日である'),
        ('イ', '正', '地目の変更の登記を申請するのは、現況を変えた人ではなく、所有権の登記名義人である'),
        ('ウ', '正', '変更の後に名義人となった者の一月は、自分の所有権の登記があった日から数える'),
        ('エ', '誤', '居宅の敷地として使われている土地は、高圧線の下でも宅地である'),
        ('オ', '誤', '数回変わっていても、登記記録上の地目から現在の地目へ、一度に申請できる'),
    ],
    summary_tail='アは「許可の日」と「現況が変わった日」、エは「高圧線の下」と「建物の敷地」の取り違えを誘う出題です。地目は、書類上の日付ではなく、土地の実際の使い道で決まる、と覚えましょう。',
    supplements=[
        '### 補足説明（ア）：許可の日と、現況が変わった日\n\n農地を宅地にするときは、農地法の許可と、実際の工事という二つの出来事があります。地目の変更の原因の日付になるのは、後者です。\n\n- 農地転用の許可を受けた日：まだ土地は畑のままです。登記原因の日付にはなりません。\n- 造成工事が終わり、住宅の敷地となった日：現況が変わった日です。これが地目の変更の原因の日付で、ここから一月以内に申請します。\n\n**たとえば**、6月1日に許可を受け、8月1日に造成が終わって住宅の敷地にしたなら、原因の日付は8月1日です。申請は、8月1日から一月以内にします。',
        '### 補足説明（エ）：高圧線の下の土地は、使い方で決まる\n\n高圧線の下にある土地でも、使い方によって地目は変わります。\n\n- 高圧線の下で、他の目的に使用することができない区域：雑種地です（準則69条13号）。\n- 建物の敷地として使われている土地：宅地です（準則68条3号）。\n\n**たとえば**、上空を高圧線が通っていても、そこに居宅が建ち、庭や通路も含めて住まいとして使われていれば、その土地は宅地です。高圧線があるというだけで、雑種地になるわけではありません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第57日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法37条1項・2項、不動産登記事務取扱手続準則68条・69条は、`note-articles/laws/` 配下の原文で確認しました。',
        'アの「原因の日付は、現況が変わった日」は、37条1項の「変更があった日」と準則68条（現況と利用目的に重点を置く）から導いた説明です。農地法の許可の日を原因の日付にしないという個別の取扱いの原文は、手元の法令集には収録がなく、未確認です。',
        'オの「登記記録上の地目から一度に申請できる」という取扱いは、条文の文言ではなく登記実務の取扱いで、原文は未確認です。',
    ],
    phrases=['地目の変更日は、許可の日ではありません', '申請するのは、所有権の登記名義人です', '後から名義人になれば、自分の登記の日から', '居宅の敷地なら、高圧線の下でも宅地です', '何度変わっても、一度に変更できます'],
    header=dict(t1='地目が変わった日は、', t2='いつになる？', topic='不動産登記法　地目の変更', kanji='登・記・毎・地・目・変・更'),
    poster_intro='地目の変更の登記を、「申請の仕方」（グループA：ア・イ・ウ）と「地目の認定と手順」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='地目の変更の登記を整理', sub='不動産登記法 第37条と準則 第68条・第69条（毎日ドリル 第57日）',
        col_a='申請の仕方', col_b='地目の認定と手順', n_a=3,
        cards=[
            dict(h='原因の日付は現況が変わった日',
                 ill='a horizontal timeline. On the left a flag labeled 「許可」 drawn in gray; further right a flag labeled 「工事完了」 drawn in green with an icon of a house on a plot. A green check mark sits above the green flag.',
                 words=['許可', '工事完了'], tag='現況が変わった日'),
            dict(h='申請するのは所有権の登記名義人',
                 ill='an owner figure at a desk, holding a form, highlighted with a green glow and carrying a name tag labeled 「所有者」. In the background a faded gray figure with a land plot stands aside. A green check mark sits beside the owner.',
                 words=['所有者'], tag='申請人は名義人'),
            dict(h='あとから名義人になれば自分の登記の日から',
                 ill='a horizontal timeline. On the left a flag labeled 「変更」; further right a second flag labeled 「自分の登記」. A green bracket labeled 「一月以内」 starts at the second flag and extends to the right.',
                 words=['変更', '自分の登記', '一月以内'], tag='起算日は自分の登記'),
            dict(h='居宅の敷地なら高圧線の下でも宅地',
                 ill='an isometric house on a land plot with a high-voltage power line stretching above it. A sign beside the house is labeled 「宅地」. A green check mark sits beside the sign.',
                 words=['宅地'], tag='敷地は宅地'),
            dict(h='何度変わっても一度に変更できる',
                 ill='three small land plot icons in a row labeled 「田」, 「雑種地」 and 「宅地」, with one long green arrow skipping directly from the first to the third. A green check mark sits beside the arrow.',
                 words=['田', '雑種地', '宅地'], tag='一度に申請'),
        ],
        kanji='許・可・工・事・完・了・所・有・者・変・更・自・分・登・記・一・月・以・内・居・宅・敷・地・高・圧・線・雑・種・田'.split('・')),
    nb_label='ア・エ肢', nb_intro='ア・エの補足説明に合わせた2枚です。1枚目は、許可の日と現況が変わった日を時間の流れで示します。2枚目は、高圧線の下の土地が雑種地になる場合と宅地になる場合を、左右の対比で示します。',
    notebooks=[
        dict(name='許可の日と、現況が変わった日', args=dict(
            title='原因の日付は、どの日？', sub='地目の変更の登記の原因の日付（毎日ドリル 第57日 ア）',
            req='a timeline diagram',
            layout="""--- TIMELINE ---
Render as a clean flat-design horizontal timeline in the upper half. A common timeline axis runs left to right with two flags: the left flag labeled 農地転用の許可 (with an icon of a stamped permit paper beside a field) and the right flag labeled 造成工事が完了 (with an icon of a house on a plot of land).
Under the left flag, a result badge in gray with a red cross: 原因の日付ではない
Under the right flag, a result badge in green with a green check mark: 原因の日付
A green bracket starting at the right flag and extending to the right, labeled 一月以内に申請
The two flag labels are different strings; draw them in different accent colors (gray and green). Use exactly these strings, and no others, for the labels.""",
            callout='地目の変更の原因の日付は、許可を受けた日ではなく、土地の現況が実際に変わった日です。\nこの日から一月以内に、変更の登記を申請します。',
            footer='不動産登記法三十七条一項、不動産登記事務取扱手続準則六十八条',
            kanji='登・記・地・目・変・更・農・転・用・許・可・造・成・工・事・完・了・原・因・日・付・申・請'.split('・'), what='timeline',
            check='confirm the left flag carries a red cross and the right flag carries a green check mark, and that the two flag labels are different strings in different accent colors, ')),
        dict(name='高圧線の下の土地は、使い方で決まる', args=dict(
            title='高圧線の下は、雑種地？', sub='高圧線の下の土地の地目（毎日ドリル 第57日 エ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「他の目的に使えない区域」 on the left and 「居宅の敷地」 on the right. Draw them in different accent colors (gray and blue). The two result badges are also different strings: 「雑種地」 and 「宅地」.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (gray accent):
Panel header: 他の目的に使えない区域
Scene: an isometric scene of an empty plot of land under a high-voltage power line, with no building on it.
Result badge with a green check mark: 雑種地

RIGHT PANEL (blue accent):
Panel header: 居宅の敷地
Scene: an isometric scene of a house with a garden under a high-voltage power line.
Result badge with a green check mark: 宅地""",
            callout='高圧線の下の土地が雑種地になるのは、他の目的に使用することができない区域です。\n居宅の敷地として使われている土地は、高圧線の下でも宅地です。',
            footer='不動産登記事務取扱手続準則六十八条・六十九条',
            kanji='地・目・雑・種・宅・他・的・使・区・域・居・敷・高・圧・線'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (他の目的に使えない区域 on the left and 居宅の敷地 on the right) and the two result badges read 雑種地 on the left and 宅地 on the right, ')),
    ],
)
