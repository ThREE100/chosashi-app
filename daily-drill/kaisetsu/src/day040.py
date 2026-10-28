D = dict(
    catch='登記なしで対抗できる相手は限られる',
    intro='不動産の物権変動について、「所有権はいつ移るのか」と「登記がなければ主張できない相手（民法177条の第三者）はだれか」を問う問題です（民法176条・177条）。判例の考え方に沿って、誤っているものを選びます。\n\nこの記事では、登記がなくても勝てる相手と、登記がないと負けてしまう相手の違いを、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('知っていただけの買主にも、登記がなければ対抗できない',
               '不動産の売買で買主が所有権の取得を主張するには、登記が必要です（民法177条）。二重に売られた場合は、先に登記をした方が勝ちます。\n\n判例は、売買があったことを知っていただけの買主（単純悪意者）も、177条の「第三者」に当たるとしています。そのため、Bは登記がなければ、Cに対抗できません。\n\n問題文は「登記を備えなくても対抗できる」としているので、本肢は誤りです。\n\n**たとえば**、AさんがBさんに土地を売ったあと、同じ土地をCさんにも売ったとします。Cさんが「Bさんに売ったらしい」と知っていただけなら、Bさんは登記を先に受けなければ、Cさんに勝てません。'),
        'イ': ('不法占拠者には、登記がなくても明渡しを請求できる',
               '判例は、何の権原もなく不動産を占拠している者は、177条の「第三者」に当たらないとしています。登記がないことを主張する正当な利益がないからです。\n\nそのため、買主のBは、登記がなくても、不法占拠者のCに明渡しを請求できます。本肢は正しいといえます。\n\n**たとえば**、買ったばかりの土地に、無断で車を止めている人がいたとします。名義変更をまだしていなくても、買主はその人に出ていくよう求めることができます。'),
        'ウ': ('解除のあとの第三者との関係は、先に登記をした方が勝つ',
               '売買を解除したあとに、買主から土地を買った第三者が現れた場合、判例は、解除した売主と第三者の関係を対抗関係としています。\n\nBを起点に、B→A（解除による所有権の復帰）とB→Cの二重譲渡があったのと同じに考えます。そのため、Aは登記を備えなければ、Cに対抗できません。\n\n問題文は「登記がなくても主張できる」としているので、本肢は誤りです。\n\n**たとえば**、Aさんが土地をBさんに売って登記も移し、その後に代金未払いを理由に契約を解除したとします。Bさんがその解除のあとに土地をCさんへ転売し、登記もCさんに移った場合、Aさんは「解除したから自分のものだ」と言うだけでは足りず、先に登記を取り戻していなければ、Cさんに負けます。'),
        'エ': ('他の共有者も、持分を譲り受けた人にとっては第三者',
               '判例は、共有者の一人から持分を譲り受けた者にとって、他の共有者は177条の「第三者」に当たるとしています。そのため、持分の譲受人は登記がなければ、他の共有者に持分の取得を対抗できません。本肢は正しいといえます。\n\n**たとえば**、A・B・Cが共有する土地で、AさんがDさんに自分の持分を売ったのに登記をしていないとします。DさんはBさんやCさんに対して、持分が自分のものになったと当然には主張できません。共有仲間だからといって、登記が不要になるわけではありません。'),
        'オ': ('他人の土地の売買では、売主が取得した時に買主に移る',
               '物権の移転は、当事者の意思表示だけで効力を生じます（民法176条）。特約がなければ、売買の契約をした時に移るのが原則です。\n\nただし、他人の物の売買では、売主がその物の所有権を取得した時に、買主に所有権が移るというのが判例の立場です。AからBへの移転の登記がされた時ではありません。本肢は正しいといえます。\n\n**たとえば**、BさんがAさん所有の土地を、あとで買い取ってからCさんに渡す約束で売ったとします。BさんがAさんから土地を買って自分のものにした時に、土地はCさんのものになります。'),
    },
    summary=[
        ('ア', '誤', '売買を知っていただけの買主（単純悪意者）にも、登記がなければ対抗できない'),
        ('イ', '正', '不法占拠者は第三者に当たらないので、登記がなくても明渡しを請求できる'),
        ('ウ', '誤', '解除のあとの第三者との関係は対抗関係なので、解除した売主も登記が必要'),
        ('エ', '正', '他の共有者は第三者に当たり、持分の譲受人は登記がなければ対抗できない'),
        ('オ', '正', '他人の物の売買では、売主が所有権を取得した時に買主に所有権が移る'),
    ],
    summary_tail='アは「単純悪意者」と背信的悪意者の取り違え、ウは「解除のあと」の第三者の扱いを入れ替えた出題です。登記がなくても勝てる相手は限られる、と覚えておきましょう。',
    supplements=[
        '### 補足説明（ア）：登記がなくても勝てる相手、登記がいる相手\n\n民法177条の「第三者」に当たるかどうかで、登記の要否が決まります。\n\n| 区分 | 相手の例 |\n|---|---|\n| 第三者に当たらない（登記がなくても対抗できる） | 当事者本人、相続人などの包括承継人、前の持ち主・あとの持ち主の関係にある者、不法占拠者、もっぱら相手を害する目的で買った背信的悪意者 |\n| 第三者に当たる（登記がなければ対抗できない） | 売買を知っていただけの単純悪意者、解除のあとに現れた第三者、他の共有者 |\n\n**たとえば**、売買を知っていただけの買主と、わざと相手を困らせる目的で買った買主は、同じ「知っている」でも扱いが違います。前者には登記が必要ですが、後者には登記がなくても対抗できます。',
        '### 補足説明（ウ）：解除のあとの第三者は、二重譲渡と同じ\n\n売買を解除すると、土地の所有権はもとの売主に戻ります。この復帰と、買主からの転売が、二重譲渡のように競い合います。\n\n- 売却と移転の登記：A→B。\n- 解除：土地の所有権がBからAに戻る。\n- 転売と移転の登記：B→C。AとCは、先に登記を備えた方が勝つ。\n\n**たとえば**、Aさんが解除したあとも、登記がBさん名義のままなら、Bさんは登記上は所有者のままです。その状態でBさんがCさんに売り、登記をCさんに移すと、Aさんは負けてしまいます。解除したら、早めに登記を戻しておくことが大切です。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第40日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '民法176条・177条は `note-articles/laws/` 配下の原文で確認しました。各肢の判例の結論（単純悪意者、不法占拠者、解除後の第三者、他の共有者、他人物売買）は、過去問の解説記事（令和6年度、平成29年度、平成20年度の民法の問題）の記述を参照して確認しています。判例の原文は未確認です。',
        '各肢の具体例（二重に売られた土地、無断駐車、解除のあとの転売、共有持分の売却、あとで買い取る約束の売買）は、判例の結論をかみ砕いた一般的な説明です。',
        '補足説明（ア）の表の「第三者に当たらない」の分類は、過去問の解説記事に整理された判例の枠組みによるもので、民法の条文そのものに書かれているわけではありません。補足説明（ウ）の「解除によって所有権が売主に戻る」という説明も、判例の考え方を一般的にかみ砕いたものです。',
    ],
    phrases=['知っていただけでも登記が必要です', '不法占拠者には登記なしで請求できます', '解除のあとは先に登記した方が勝ちます', '他の共有者にも持分の登記が必要です', '他人の物の売買は取得した時に移ります'],
    header=dict(t1='登記がなくても、', t2='勝てる相手は？', topic='民法　不動産の物権変動',
                kanji='登・記・民・法・物・権・変・動'),
    poster_intro='不動産の物権変動を、「登記が必要かどうか」（グループA：ア・イ・ウ）と「共有者と他人の物の売買」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='不動産の物権変動を整理', sub='民法 第176条・第177条（毎日ドリル 第40日）',
        col_a='登記が必要かどうか', col_b='共有者と他人の物の売買', n_a=3,
        cards=[
            dict(h='知っていただけの買主にも登記が必要',
                 ill='two buyer figures reaching for the same isometric house model. The buyer who holds a round stamp labeled 「登記」 is ahead and highlighted with a green glow; the other buyer is slightly behind. A green check mark sits beside the first buyer.',
                 words=['登記'], tag='先に登記した方が勝つ'),
            dict(h='不法占拠者には登記なしで明渡請求',
                 ill='an isometric land plot with a car parked on it without permission. A buyer figure holding a deed document points toward the car with a firm gesture. The buyer holds no stamp. A green check mark sits beside the buyer. No text on any object.',
                 words=[], tag='登記なしで請求できる'),
            dict(h='解除のあとの買主には登記が必要',
                 ill='a horizontal timeline with three small icons: a house sale, then a flag labeled 「解除」 with a rule book crossed out by a thin horizontal line, then a resale. A figure at the right end holds a round stamp labeled 「登記」 and is highlighted with a green glow. A green check mark sits beside this figure.',
                 words=['解除', '登記'], tag='対抗問題になる'),
            dict(h='共有者にも持分の登記が必要',
                 ill='three co-owner figures standing around an isometric land plot. A buyer figure holding a deed document and no stamp stands apart on the edge of the plot. A thin dotted line connects the buyer to the plot. A label 「持分」 sits on one slice of the plot. A green check mark sits beside the three co-owners.',
                 words=['持分'], tag='他の共有者も第三者'),
            dict(h='他人物売買は売主が取得した時に移転',
                 ill='a horizontal timeline. On the left a flag labeled 「取得」 where a seller figure receives a house model from an owner figure. A green arrow from this flag carries the house model to a buyer figure on the right. A green check mark sits beside the buyer.',
                 words=['取得'], tag='取得した時に移転'),
        ],
        kanji='登・記・解・除・持・分・取・得・占・拠・者・明・渡・請・求・先・勝・対・抗・共・有'.split('・')),
    nb_label='ア・ウ肢', nb_intro='ア・ウの補足説明に合わせた2枚です。1枚目は、登記がなくても勝てる相手と、登記がないと負ける相手を左右の対比で示します。2枚目は、解除のあとに転売された場合の流れを、時間の流れで示します。',
    notebooks=[
        dict(name='登記がなくても勝てる相手、勝てない相手', args=dict(
            title='登記がいる相手、いらない相手', sub='民法177条の第三者（毎日ドリル 第40日 ア）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「登記がないと対抗できない」 on the left and 「登記がなくても対抗できる」 on the right. Draw them large and in different accent colors (orange and blue). Do not draw any check mark or cross mark on this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (orange accent):
Panel header: 登記がないと対抗できない
Scene: three small rows stacked vertically, each with a small person icon and one of these exact labels: 単純悪意者 | 解除のあとの第三者 | 他の共有者

RIGHT PANEL (blue accent):
Panel header: 登記がなくても対抗できる
Scene: four small rows stacked vertically, each with a small person icon and one of these exact labels: 当事者・相続人 | 前の持ち主 | 不法占拠者 | 背信的悪意者""",
            callout='売買を知っていただけの単純悪意者は、第三者に当たります。\n不法占拠者や、もっぱら相手を害する目的で買った背信的悪意者などには、登記がなくても対抗できます。',
            footer='民法177条',
            kanji='登・記・対・抗・単・純・悪・意・者・解・除・第・三・共・有・当・事・相・続・前・持・主・不・法・占・拠・背・信'.split('・'), what='panels',
            check='confirm the two panel headers are different strings in different accent colors, that the left panel has exactly three rows and the right panel exactly four rows, and that no check mark and no cross mark is drawn, ')),
        dict(name='解除のあとに転売された場合', args=dict(
            title='解除のあとの転売は、登記の競争', sub='解除後の第三者（毎日ドリル 第40日 ウ）',
            req='a timeline diagram',
            layout="""--- TIMELINE ---
Render as a clean flat-design horizontal timeline in the upper half, on one axis with three flags from left to right.
Flag 1 (blue): label 売却と移転の登記, with an icon of a house changing hands from a seller figure to a buyer figure, caption: AからB
Flag 2 (orange): label 解除, with an icon of a rule book crossed out by a thin horizontal line (not an X shape), caption: 所有権がAに戻る
Flag 3 (green): label 転売と移転の登記, with an icon of a house changing hands from the buyer figure to a new buyer figure, caption: BからC
Below the axis, a wide green bracket spanning from Flag 2 to the far right end, labeled: 解除のあと
Under the bracket, a banner with two figures racing toward a round stamp labeled 登記, with the label: AとCは先に登記をした方が勝つ
Use exactly these strings, and no others. Do not draw any check mark or cross mark.""",
            callout='解除のあとにBが土地を転売したときは、AとCの二重譲渡と同じに考えます。\nAは登記を備えなければ、Cに対抗できません。',
            footer='民法177条',
            kanji='売・却・移・転・登・記・解・除・所・有・権・戻・勝・先・対・抗'.split('・'), what='timeline',
            check='confirm there are exactly three flags on one axis, that the crossed-out rule book uses a thin horizontal line and not an X shape, and that no check mark and no cross mark is drawn, ')),
    ],
)
