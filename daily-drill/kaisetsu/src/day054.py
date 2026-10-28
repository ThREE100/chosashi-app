D = dict(
    catch='無権代理は、確答がなければ追認拒絶',
    intro='代理と無権代理の基本ルールを、五つの場面で問う問題です（民法102条・108条・113条・114条・117条）。代理人が未成年者だったら、自分が相手方になったら、追認を誰に伝えたら、催告に返事がなかったら、本人が相続したら、と場面ごとに結論が変わります。\n\nこの問題は、判例の趣旨に照らして誤っている記述の組合せを選ぶ形です。',
    sections={
        'ア': ('本人は追認を拒絶できても、賠償責任は免れない',
               '無権代理人が死亡し、本人が単独で相続した場合、本人は、本人の立場で追認を拒絶できます。ただし、無権代理人が負っていた責任（民法117条1項）は、相続によって本人に引き継がれるので、損害賠償の責任は免れません。\n\n本肢は正しい記述です。\n\n**たとえば**、Aが勝手にBの土地をCに売り、そのAが亡くなってBが相続したとします。Bは「売買は認めない」と言えますが、Aが負っていた賠償の責任は引き継ぎます。'),
        'イ': ('相手方が追認の事実を知れば、追認を対抗できる',
               '追認又はその拒絶は、相手方に対してしなければ、その相手方に対抗することができません。ただし、相手方がその事実を知ったときは、対抗できます（民法113条2項）。\n\n無権代理人に対して追認の意思表示をした場合でも、相手方Cがその事実を知れば、Aは追認をCに対抗できます。本肢は正しい記述です。\n\n**たとえば**、Aが代理権のないBに「その契約を認めます」と伝えたとします。後で相手方のCがその話を知ったときは、Aは追認をCに主張できます。'),
        'ウ': ('未成年者が代理人でも、本人は取り消せない',
               '制限行為能力者が代理人としてした行為は、行為能力の制限によっては取り消すことができません（民法102条本文）。代理の効果は本人に生じ、代理人自身が不利益を受けるわけではないからです。\n\n問題文は、Aが、Bが未成年者であることを理由に売買契約を取り消せるとしているので、本肢は誤りです。\n\n**たとえば**、Aが未成年者のBを代理人にして売買契約を結ばせたとします。後になって、Bが未成年者だったことを理由に契約を取り消すことはできません。'),
        'エ': ('本人があらかじめ許諾した自己契約は、有効',
               '同一の法律行為について、相手方の代理人としてした行為は、代理権を有しない者がした行為とみなされます。ただし、本人があらかじめ許諾した行為については、この限りではありません（民法108条1項）。\n\n本人Aがあらかじめ許諾していたときは、代理権を有しない者がした行為とはみなされません。本肢は正しい記述です。\n\n**たとえば**、土地の売却を頼まれた代理人Bが、自分で買主になるとします。Aが前もって了承していたなら、この契約は有効に成立します。'),
        'オ': ('催告に確答しなければ、追認を拒絶したものとみなす',
               '無権代理の相手方は、本人に対し、相当の期間を定めて、その期間内に追認をするかどうかを確答すべき旨を催告できます。この期間内に本人が確答しないときは、追認を拒絶したものとみなされます（民法114条）。\n\n問題文は、追認をしたものとみなされるとしているので、本肢は誤りです。\n\n**たとえば**、相手方のCが本人のAに「1か月以内に追認するか答えてください」と催告したのに、Aが何も答えなかったとします。Aは、追認を拒絶したものとして扱われます。'),
    },
    summary=[
        ('ア', '正', '本人が無権代理人を相続しても、追認の拒絶はできるが、無権代理人の責任は免れない'),
        ('イ', '正', '追認の相手方への対抗は、相手方が追認の事実を知ったときはできる'),
        ('ウ', '誤', '制限行為能力者が代理人としてした行為は、行為能力の制限によっては取り消せない'),
        ('エ', '正', '本人があらかじめ許諾した自己契約は、代理権を有しない者の行為とはみなされない'),
        ('オ', '誤', '催告に本人が確答しないときは、追認を拒絶したものとみなされる'),
    ],
    summary_tail='ウは代理人の能力と本人の取消しの取り違え、オは「追認」と「拒絶」の入れ替えを狙った出題です。確答しないときは追認ではなく拒絶、と覚えておきましょう。',
    supplements=[
        '### 補足説明（ウ）：制限行為能力者が代理人になったとき\n\n代理人が制限行為能力者だった場合の取消しの可否です（民法102条）。\n\n| 場面 | 行為能力の制限を理由に取り消せるか |\n|---|---|\n| 制限行為能力者が、本人の任意代理人としてした行為 | 取り消せない（本文） |\n| 制限行為能力者が、他の制限行為能力者の法定代理人としてした行為 | 取り消せる（ただし書） |\n\n**たとえば**、成年の本人Aが未成年者のBを代理人にして契約を結ばせたときは、Bの未成年を理由に取り消せません。Bが、別の未成年者の法定代理人として結んだ契約は、取り消せる場合があります。',
        '### 補足説明（オ）：無権代理の本人の対応と結果\n\n無権代理行為について、本人が取れる対応と、その結果です（民法113条・114条）。\n\n| 本人の対応 | 結果 |\n|---|---|\n| 追認をする | 契約が本人に効力を生じる（113条1項） |\n| 追認を拒絶する | 契約は本人に効力を生じない |\n| 催告の期間内に確答しない | 追認を拒絶したものとみなされる（114条） |\n\n**たとえば**、相手方から追認の催告を受けた本人が、期限までに返事をしなかったとします。返事をしないことは「追認」ではなく、「拒絶」として扱われます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第54日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、民法102条、108条1項、113条2項、114条、117条1項は、`note-articles/laws/` 配下の原文で確認しました。',
        'ア（本人が無権代理人を相続したとき、追認は拒絶できるが無権代理人の責任は免れない）は、判例の趣旨に基づく説明です。判例の原文は手元にないため未確認で、本文には判例の番号を書いていません。',
        'ウの「代理人自身が不利益を受けるわけではない」という理由は、条文からの一般的な整理です。具体例（1か月以内の催告、土地を自分で買う代理人など）は、場面を思い描くための例です。',
    ],
    phrases=['追認を拒絶しても賠償の責任は残ります', '相手方が知れば追認を主張できます', '未成年者の代理人でも取消しはできません', 'あらかじめ許諾すれば自己契約もできます', '確答しなければ追認の拒絶になります'],
    header=dict(t1='無権代理、', t2='どうなる？', topic='民法　代理と無権代理',
                kanji='無・権・代・理'),
    poster_intro='代理と無権代理を、「無権代理と代理人の能力」（グループA：ア・イ・ウ）と「自己契約と催告」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='代理と無権代理を整理', sub='民法 第102条から第117条（毎日ドリル 第54日）',
        col_a='無権代理と代理人の能力', col_b='自己契約と催告', n_a=3,
        cards=[
            dict(h='本人は拒絶できても賠償責任は残る',
                 ill='a person figure holding a sheet labeled 「追認拒絶」 in one hand, while a bill labeled 「損害賠償」 stays attached to the other side of the figure. A green check mark sits beside the figure.',
                 words=['追認拒絶', '損害賠償'], tag='責任は引き継がれる'),
            dict(h='相手方が知れば追認を主張できる',
                 ill='a horizontal flow of three figures. The left figure hands a sheet labeled 「追認」 to the middle figure. The right figure, the counterparty, looks at the sheet with a light bulb above the head. A green check mark sits beside the right figure.',
                 words=['追認'], tag='相手方が知れば有効'),
            dict(h='未成年の代理人でも取消しはできない',
                 ill='a young agent figure labeled 「未成年者」 signing a contract sheet on behalf of an adult principal figure standing behind. The contract sheet carries a green check mark.',
                 words=['未成年者'], tag='行為能力の制限は理由にならない'),
            dict(h='事前に許諾すれば自己契約もできる',
                 ill='an agent figure holding a contract sheet where both the seller side and the buyer side show the same agent figure, and an approval sheet labeled 「許諾」 held by the principal figure behind. A green check mark sits beside the approval sheet.',
                 words=['許諾'], tag='あらかじめの許諾'),
            dict(h='確答しなければ追認の拒絶になる',
                 ill='a counterparty figure handing a notice sheet labeled 「催告」 to the principal figure, with a calendar page beside them. A round stamp labeled 「拒絶」 sits at the end of the calendar. A green check mark sits beside the stamp.',
                 words=['催告', '拒絶'], tag='返事がなければ拒絶'),
        ],
        kanji='追・認・拒・絶・損・害・賠・償・未・成・年・者・許・諾・催・告'.split('・')),
    nb_label='ウ・オ肢', nb_intro='ウ・オの補足説明に合わせた2枚です。1枚目は、制限行為能力者が代理人になった場合の取消しの可否を表で示します。2枚目は、無権代理の本人の対応と結果を表で整理します。',
    notebooks=[
        dict(name='制限行為能力者が代理人になったとき', args=dict(
            title='代理人が未成年者だったら？', sub='代理人の行為能力（毎日ドリル 第54日 ウ）',
            req='a table diagram',
            layout="""--- TABLE ---
Render as a clean flat-design table in the upper half, with two rows and two columns, and a small isometric icon at the left of each row.
Column headers: 場面 | 取り消せるか
Row 1 (blue accent), icon: a young agent figure and a principal figure. Cells: 制限行為能力者が、本人の任意代理人としてした行為 | 取り消せない
Row 2 (orange accent), icon: a young agent figure and another young figure. Cells: 制限行為能力者が、他の制限行為能力者の法定代理人としてした行為 | 取り消せる
Use exactly these strings, and no others, for the table text. The two result cells 取り消せない and 取り消せる are different strings; draw 取り消せない in blue and 取り消せる in orange so they can never be confused or duplicated.""",
            callout='制限行為能力者が代理人としてした行為は、行為能力の制限を理由には取り消せません。\n例外は、他の制限行為能力者の法定代理人としてした行為です。',
            footer='民法102条',
            kanji='場・面・取・消・制・限・行・為・能・力・者・本・人・任・意・代・理・他・法・定'.split('・'), what='table',
            check='confirm the two result cells 取り消せない and 取り消せる are different strings in different accent colors, ')),
        dict(name='無権代理の本人の対応と結果', args=dict(
            title='本人が答えなかったら？', sub='追認、拒絶、催告（毎日ドリル 第54日 オ）',
            req='a table diagram',
            layout="""--- TABLE ---
Render as a clean flat-design table in the upper half, with three rows and two columns, and a small isometric icon at the left of each row.
Column headers: 本人の対応 | 結果
Row 1 (green accent), icon: a principal figure holding a sheet with a green check mark. Cells: 追認をする | 契約が本人に効力を生じる
Row 2 (orange accent), icon: a principal figure holding a sheet with a hand-stop gesture. Cells: 追認を拒絶する | 契約は本人に効力を生じない
Row 3 (gray accent), icon: a calendar page with a principal figure looking away. Cells: 催告の期間内に確答しない | 追認を拒絶したものとみなされる
Use exactly these strings, and no others, for the table text. Rows 1 and 3 have different results; draw 契約が本人に効力を生じる in green and 追認を拒絶したものとみなされる in gray.""",
            callout='相手方の催告に、本人が期間内に確答しないときは、追認を拒絶したものとみなされます。\n返事をしないことは、追認ではなく拒絶として扱われます。',
            footer='民法113条・114条',
            kanji='本・人・対・応・結・果・追・認・拒・絶・契・約・効・力・生・催・告・期・間・確・答'.split('・'), what='table',
            check='confirm that rows 1 and 3 show different result strings in different accent colors, ')),
    ],
)
