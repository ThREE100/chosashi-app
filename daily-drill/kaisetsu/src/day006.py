def kj(*ss, n=14):
    out = []
    for s in ss:
        for c in s:
            if '一' <= c <= '龥' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='筆界特定の代理は断れる、研修は努力義務',
    intro='土地家屋調査士の義務を定めた、土地家屋調査士法22条から25条までの問題です。依頼を断れるか、秘密を守る義務はいつまで続くか、研修は義務なのか、といった「調査士としての心がまえ」が問われています。\n\nこの記事では、「してはならない」と書かれている義務と、「努めなければならない」と書かれている努力義務の違いを、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('筆界特定の代理の依頼は、断れないという義務の対象外',
               '調査士は、正当な事由がある場合でなければ、依頼を拒んではなりません。ただし、筆界特定の手続についての代理（3条1項4号）などは、この義務の対象から除かれています（土地家屋調査士法22条）。\n\n問題文は、筆界特定の手続の代理の依頼であっても、正当な事由がなければ拒んではならないとしています。本肢は誤りです。\n\n**たとえば**、隣の土地との境目をめぐって、筆界特定の手続の代理を頼まれたとします。登記の申請手続の代理のように「正当な事由がなければ断れない」という義務は、この依頼にはかかりません。'),
        'イ': ('業務に関して、虚偽の調査や測量をしてはならない',
               '調査士は、その業務に関して虚偽の調査又は測量をしてはなりません（土地家屋調査士法23条）。\n\n本肢は正しいといえます。\n\n**たとえば**、現地で測量していないのに、測ったことにして図面の数字を書いたり、調べていない境界標を「確認した」と報告したりすることは許されません。'),
        'ウ': ('調査士をやめた後も、業務上知った秘密は漏らしてはならない',
               '調査士又は調査士であった者は、正当な事由がある場合でなければ、業務上取り扱った事件について知ることのできた秘密を他に漏らしてはなりません（土地家屋調査士法24条の2）。\n\n本肢は正しいといえます。\n\n**たとえば**、依頼者の土地の売却計画を仕事で知った調査士が、廃業した後に、その話を周りの人に話してしまうことも許されません。やめたからといって、秘密を守る義務がなくなるわけではありません。'),
        'エ': ('公務員として扱った事件は、調査士として業務を行えない',
               '調査士は、公務員として職務上取り扱った事件及び仲裁手続により仲裁人として取り扱った事件については、その業務を行ってはなりません（土地家屋調査士法22条の2第1項）。\n\n本肢は正しいといえます。\n\n**たとえば**、以前に公務員として、ある土地の事件を職務で担当していた人が、その後に調査士になったとします。同じ事件について、調査士として依頼を受けて業務を行うことはできません。'),
        'オ': ('研修を受けて資質の向上を図ることは、努力義務',
               '調査士は、所属する調査士会及び調査士会連合会が実施する研修を受け、その資質の向上を図るように努めなければなりません（土地家屋調査士法25条1項）。\n\n問題文は「図らなければならない」と言い切っていますが、条文は「図るように努めなければならない」です。本肢は誤りです。\n\n**たとえば**、仕事が忙しく、研修に参加できない年があったとします。研修を受けるよう努める義務はありますが、受けなければ直ちに義務違反になる、という書き方ではありません。'),
    },
    summary=[
        ('ア', '誤', '筆界特定の手続の代理は、正当な事由がなければ依頼を拒めない、という義務の対象から除かれている'),
        ('イ', '正', '業務に関して虚偽の調査又は測量をしてはならない'),
        ('ウ', '正', '調査士であった者も、正当な事由がなければ、業務上知った秘密を漏らしてはならない'),
        ('エ', '正', '公務員として職務上取り扱った事件は、調査士としての業務を行えない'),
        ('オ', '誤', '研修を受けて資質の向上を図ることは、「努めなければならない」という努力義務'),
    ],
    summary_tail='アは「断れない義務」に例外があること、オは「努めなければならない」を言い切りに変えた出題です。条文の結びが「してはならない」なのか「努めなければならない」なのかを、まず見分けましょう。',
    supplements=[
        '### 補足説明（ア）：依頼を拒んではならない範囲には、例外がある\n\n22条は、正当な事由がなければ依頼を拒んではならないと定めていますが、かっこ書きで次の業務を除いています。\n\n| 22条の義務の対象から除かれるもの | 条文 |\n|---|---|\n| 筆界特定の手続についての代理 | 3条1項4号 |\n| 筆界特定の手続の代理についての相談 | 3条1項6号（4号に関する部分に限る） |\n| 民間紛争解決手続代理関係業務 | 3条1項7号・8号 |\n\n**たとえば**、新築した建物の表題登記の申請手続の代理は、正当な事由がなければ断れません。これに対して、筆界特定の手続の代理は、この義務の対象から除かれています。',
        '### 補足説明（オ）：「してはならない」と「努めなければならない」\n\n調査士法には、結びの言葉が違う義務が並んでいます。\n\n| 内容 | 条文 | 結び |\n|---|---|---|\n| 虚偽の調査又は測量 | 23条 | してはならない |\n| 業務上知った秘密を漏らすこと | 24条の2 | 漏らしてはならない |\n| 研修を受け、資質の向上を図ること | 25条1項 | 図るように努めなければならない |\n\n**たとえば**、虚偽の測量は、絶対にしてはならない禁止です。これに対し、研修は「努めなければならない」と書かれているので、心がけを求める努力義務です。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第6日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、土地家屋調査士法3条、22条、22条の2第1項、23条、24条の2、25条1項は、`note-articles/laws/` 配下の原文で確認しました。',
        'エの具体例（もと公務員だった人の例）は、22条の2第1項の文言から導いた一般的な説明です。',
        'ウ・オの具体例は、条文の文言をかみ砕いた一般的な説明で、懲戒などの処分の運用までは確認していません。オで「受けなければ直ちに義務違反になる、という書き方ではない」としたのは、25条1項の結びの言葉からの整理です。',
    ],
    phrases=['断れない義務にも例外があります', '虚偽の測量は許されません', 'やめた後も秘密は守ります', '公務員だった事件は受けられません', '研修は努力義務なんです'],
    header=dict(t1='調査士の義務は、', t2='どこまで厳しい？', topic='土地家屋調査士法　調査士の義務',
                kanji='調・査・士・義・務・毎'),
    poster_intro='調査士の義務を、「業務の心得」（グループA：ア・イ・ウ）と「公務員の事件と研修」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='調査士の義務を整理', sub='土地家屋調査士法 第22条から第25条まで（毎日ドリル 第6日）',
        col_a='業務の心得', col_b='公務員の事件と研修', n_a=3,
        cards=[
            dict(h='筆界特定の代理は、断れない義務の対象外',
                 ill='two neighboring land plots with a dotted boundary line and a boundary stake. A surveyor figure stands beside a form labeled 「筆界特定」. A small door on the side is drawn open to show that the request may be declined. A green check mark sits beside the form.',
                 words=['筆界特定'], tag='対象から除かれる'),
            dict(h='虚偽の調査や測量はしてはならない',
                 ill='a surveyor figure with a tripod at a land plot, carefully measuring, with a drawing sheet showing honest figures. A green check mark sits beside the drawing sheet. No cross mark is drawn.',
                 words=[], tag='事実のとおりに'),
            dict(h='調査士であった者も秘密を守る',
                 ill='a retired surveyor figure with a white hat, with a finger raised to the lips, standing next to a locked folder. A green check mark sits beside the locked folder.',
                 words=[], tag='やめた後も'),
            dict(h='公務員として扱った事件は受けられない',
                 ill='a case folder placed on a government desk on the left, and a surveyor figure on the right standing apart from the folder, hands behind the back. A green check mark sits beside the surveyor figure.',
                 words=[], tag='業務を行えない'),
            dict(h='研修を受けて資質の向上に努める',
                 ill='a surveyor figure sitting at a training desk with a notebook, and a small ladder going upward beside the desk. A green check mark sits beside the notebook.',
                 words=[], tag='努力義務'),
        ],
        kanji=kj('調査士義務筆界特定虚偽測量公務員秘密研修努力')),
    nb_label='ア・オ肢', nb_intro='ア・オの補足説明に合わせた2枚です。1枚目は、依頼を拒んではならない業務と、その対象から除かれる業務を左右の対比で示します。2枚目は、結びの言葉が違う義務を並べます。',
    notebooks=[
        dict(name='依頼を拒んではならない業務、対象から除かれる業務', args=dict(
            title='依頼は断れる？断れない？', sub='土地家屋調査士法22条（毎日ドリル 第6日 ア）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「正当な事由がなければ拒めない」 on the left and 「この義務の対象から除かれる」 on the right. Draw them large and in different accent colors (blue on the left, orange on the right) so they can never be confused or duplicated. Do not draw any cross mark or check mark in this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 正当な事由がなければ拒めない
Scene: an isometric scene of a surveyor figure at a counter with a newly built house in the background.
Label under the scene: 表題登記の申請手続の代理など

RIGHT PANEL (orange accent):
Panel header: この義務の対象から除かれる
Scene: an isometric scene of a surveyor figure beside two neighboring land plots with a dotted boundary line.
Labels under the scene: 筆界特定の手続の代理 / 民間紛争解決手続代理関係業務""",
            callout='正当な事由がなければ依頼を拒めないのは、登記の申請手続の代理などです。\n筆界特定の手続の代理などは、22条の義務の対象から除かれています。',
            footer='土地家屋調査士法22条',
            kanji=kj('正当事由拒筆界特定表題登記申請手続代理除'), what='panels',
            check='confirm the two panel headers are different strings drawn in different accent colors, and that no check mark or cross mark appears anywhere, ')),
        dict(name='結びの言葉が違う義務', args=dict(
            title='「してはならない」と「努める」', sub='土地家屋調査士法23条から25条まで（毎日ドリル 第6日 オ）',
            req='a table-like comparison',
            layout="""IMPORTANT: the two group headers are different strings: 「してはならない」 (orange accent) and 「努めなければならない」 (blue accent). Draw them large and in different colors so they can never be confused or duplicated. Do not draw any cross mark or check mark in this image.

--- COMPARISON ---
Two rows of rounded boxes, one row per group.

ROW 1 (orange accent): group header 「してはならない」
Box 1: 虚偽の調査又は測量
Box 2: 業務上知った秘密を漏らすこと

ROW 2 (blue accent): group header 「努めなければならない」
Box 1: 研修を受け、資質の向上を図ること""",
            callout='虚偽の調査や測量、秘密を漏らすことは、してはならない禁止です。\n研修を受けて資質の向上を図ることは、「図るように努めなければならない」という努力義務です。',
            footer='土地家屋調査士法23条、24条の2、25条',
            kanji=kj('虚偽調査測量秘密漏研修資質向上図努'), what='comparison',
            check='confirm the two group headers are different strings drawn in different colors, and that no check mark or cross mark appears anywhere, ')),
    ],
)
