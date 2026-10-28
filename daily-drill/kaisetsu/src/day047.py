D = dict(
    catch='貸すのは過半数、追い出しは単独で',
    intro='三人で土地と建物を共有しているとき、どこまでを一人で、どこまでを過半数で、どこからを全員で決められるのかを問う問題です（民法251条・252条）。賃借権の期間の上限や、第三者に対する請求の範囲も出てきます。\n\nこの記事では、持分が各3分の1の三人（A、B、C）という場面で、一つずつ確かめます。この問題は、判例の趣旨に照らして誤っている記述の組合せを選ぶ形です。',
    sections={
        'ア': ('土地を四年貸すのは、過半数で決められる',
               '共有者は、持分の価格の過半数で、土地の賃借権のうち五年を超えないものを設定することができます（民法252条1項・4項2号）。\n\nAとBの持分を合わせると3分の2で、過半数です。期間4年は五年以内なので、Cの同意は要りません。本肢は正しい記述です。\n\n**たとえば**、三人で持っている空き地を、AとBの二人が相談して、Dに4年間の駐車場として貸すことにしたとします。Cが反対でも、この賃借権を設定できます。'),
        'イ': ('建物の賃借権は、三年までしか過半数で設定できない',
               '過半数で設定できる賃借権の期間は、土地の賃借権は五年、建物の賃借権は三年が上限です（民法252条4項2号・3号）。\n\n問題文は、乙建物について期間5年の賃借権を、Cの同意を得なくても設定できるとしています。建物は三年を超えているので、A及びBだけでは設定できません。本肢は誤りです。\n\n**たとえば**、共有している建物をDに5年間貸すときは、AとBが賛成しても、Cの同意が別に必要です。3年以内なら、AとBだけで足ります。'),
        'ウ': ('不法占有者への明渡しの請求は、単独でできる',
               '権原のない第三者に対する明渡しの請求は、保存行為にあたるとされています。各共有者は、保存行為を単独ですることができます（民法252条5項）。\n\nAは、B及びCの同意を得なくても、Dに明渡しを請求できます。本肢は正しい記述です。\n\n**たとえば**、三人で持っている空き地に、見知らぬ人が勝手に居座ったとします。Aは、BやCに相談しなくても、一人で「出て行ってください」と請求できます。'),
        'エ': ('損害賠償は、自分の持分の分しか請求できない',
               '共有物が不法に占有されたときの損害賠償の請求は、各共有者が自分の持分の割合に応じた部分についてだけできる、とされています。明渡しの請求とは範囲が違います。\n\n問題文は、B及びCに生じた損害を含めた全額を請求できるとしているので、本肢は誤りです。\n\n**たとえば**、不法占有で土地の使用料相当の損害が3万円出たとします。Aが請求できるのは自分の3分の1にあたる1万円だけで、BとCの分の2万円までは請求できません。'),
        'オ': ('著しい変更でなければ、過半数で決められる',
               '共有物に変更を加えるには、他の共有者の同意が必要です。ただし、その形状又は効用の著しい変更を伴わないものは、ここでいう変更から除かれ、管理に関する事項として持分の価格の過半数で決めます（民法251条1項・252条1項）。\n\nAとBの同意があれば足り、Cの同意は要りません。本肢は正しい記述です。\n\n**たとえば**、共有の空き地に砂利を敷いて整える程度で、土地の形や使い道が大きく変わらない場合は、AとBの賛成で行えます。'),
    },
    summary=[
        ('ア', '正', '土地の賃借権で五年を超えないものは、持分の過半数で設定できる'),
        ('イ', '誤', '建物の賃借権は三年を超えると、過半数だけでは設定できない'),
        ('ウ', '正', '不法占有者への明渡しの請求は、保存行為として各共有者が単独でできる'),
        ('エ', '誤', '損害賠償の請求は、自分の持分の割合に応じた部分だけできる'),
        ('オ', '正', '形状又は効用の著しい変更を伴わない変更は、持分の価格の過半数で決められる'),
    ],
    summary_tail='イは土地の五年と建物の三年の数字の取り違え、エは明渡しの請求と損害賠償の請求の範囲の取り違えを狙った出題です。何を一人で、何を過半数で、何を全員で決めるのか、三段に分けて整理しましょう。',
    supplements=[
        '### 補足説明（イ）：過半数で設定できる賃借権の期間\n\n過半数で設定できる賃借権等には、目的物ごとに期間の上限があります（民法252条4項）。\n\n| 目的物 | 過半数で設定できる期間の上限 |\n|---|---|\n| 山林（樹木の栽植又は伐採が目的） | 十年 |\n| 山林以外の土地 | 五年 |\n| 建物 | 三年 |\n| 動産 | 六箇月 |\n\n上限を超える賃借権は、過半数だけでは設定できません。\n\n**たとえば**、共有地を4年貸すのは土地なので過半数で足りますが、共有の建物を4年貸すときは、建物の上限の三年を超えるので、Cの同意も必要です。',
        '### 補足説明（エ）：明渡しの請求と損害賠償の請求\n\n不法占有に対する二つの請求は、単独でできる範囲が違います。\n\n| | 明渡しの請求 | 損害賠償の請求 |\n|---|---|---|\n| 性質 | 保存行為（252条5項） | 各共有者が自分の持分に応じた分を請求する |\n| 単独でできるか | 各共有者が単独でできる | 単独でできるが、自分の持分の分だけ |\n| 範囲 | 土地の全部 | 持分3分の1なら損害の3分の1 |\n\n**たとえば**、不法占有者に出て行ってもらうのは、Aが一人で土地の全部について請求できます。一方、お金の請求は、三人の損害のうち自分の分に限られます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第47日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、民法251条1項と、252条1項・4項・5項は、`note-articles/laws/` 配下の原文で確認しました。',
        'ウ（不法占有者への明渡しの請求は保存行為）とエ（損害賠償の請求は自己の持分の割合に応じた部分のみ）は、判例の趣旨に基づく説明で、判例の原文は手元にないため未確認です。本文には判例の番号を書いていません。',
        'ウ・エ・オの具体例（空き地の不法占有、3万円の損害、砂利を敷く場面）は、場面を思い描くための例です。オで砂利を敷くことが著しい変更にあたらない、という点は、例として置いた前提です。',
    ],
    phrases=['土地を四年貸すのは過半数でできます', '建物の賃借権は三年が上限です', '出て行ってくださいは一人でできます', '損害賠償は自分の持分の分だけです', '軽い変更なら過半数で決められます'],
    header=dict(t1='共有物は、', t2='どこまで単独？', topic='民法　共有物の管理',
                kanji='共・有・物・単・独・管・理'),
    poster_intro='共有物の管理と変更を、「賃借権の設定」（グループA：ア・イ）と「請求と変更」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='共有物の管理を整理', sub='民法 第251条と第252条（毎日ドリル 第47日）',
        col_a='賃借権の設定', col_b='請求と変更', n_a=2,
        cards=[
            dict(h='土地の賃借権は五年まで過半数',
                 ill='an isometric empty land plot used as a parking lot, with two owner figures out of three standing together in a green group. A signboard on the plot is labeled 「五年」. A green check mark sits beside the signboard.',
                 words=['五年'], tag='過半数で設定できる'),
            dict(h='建物の賃借権は三年まで過半数',
                 ill='an isometric small building with a signboard labeled 「三年」 beside the entrance. Two owner figures out of three stand together in a green group. A green check mark sits beside the signboard.',
                 words=['三年'], tag='三年が上限'),
            dict(h='明渡しの請求は一人でできる',
                 ill='an isometric land plot with a stranger figure sitting on it and one owner figure pointing toward the exit with a form labeled 「明渡し」. Two other owner figures stand faded in the background. A green check mark sits beside the single owner.',
                 words=['明渡し'], tag='保存行為'),
            dict(h='損害賠償は持分の分だけ',
                 ill='a pie chart cut into three equal slices, with only one slice highlighted in green and labeled 「三分の一」. A coin icon sits beside the highlighted slice. A green check mark sits beside the slice.',
                 words=['三分の一'], tag='自分の持分の分'),
            dict(h='著しくない変更は過半数',
                 ill='an isometric empty land plot being lightly covered with gravel by a worker figure, with a signboard labeled 「過半数」. Two owner figures out of three stand together in a green group. A green check mark sits beside the signboard.',
                 words=['過半数'], tag='全員の同意は不要'),
        ],
        kanji='賃・借・権・五・年・建・物・三・明・渡・請・求・損・害・賠・償・持・分・過・半・数'.split('・')),
    nb_label='イ・エ肢', nb_intro='イ・エの補足説明に合わせた2枚です。1枚目は、過半数で設定できる賃借権の期間の上限を、目的物ごとの表で示します。2枚目は、明渡しの請求と損害賠償の請求の違いを左右の対比で示します。',
    notebooks=[
        dict(name='過半数で設定できる賃借権の期間', args=dict(
            title='賃借権は、何年まで過半数で？', sub='共有物の賃借権等の期間（毎日ドリル 第47日 イ）',
            req='a table diagram',
            layout="""--- TABLE ---
Render as a clean flat-design table in the upper half, with four rows and two columns, and a small isometric icon at the left of each row.
Column headers: 目的物 | 過半数で設定できる上限
Row 1 (green accent), icon: a mountain forest. Cells: 山林（樹木の栽植又は伐採が目的） | 十年
Row 2 (blue accent), icon: an empty land plot. Cells: 山林以外の土地 | 五年
Row 3 (orange accent), icon: a small building. Cells: 建物 | 三年
Row 4 (gray accent), icon: a bicycle. Cells: 動産 | 六箇月
Use exactly these strings, and no others, for the table text. Draw the three duration cells 五年, 三年 and 十年 in different accent colors so they can never be confused or duplicated.""",
            callout='過半数で設定できる賃借権の期間は、土地は五年、建物は三年までです。\nこの上限を超えると、過半数だけでは設定できず、共有者全員の同意が必要になります。',
            footer='民法252条4項',
            kanji='山・林・樹・木・栽・植・伐・採・目・的・土・地・建・物・動・産・設・定・上・限'.split('・'), what='table',
            check='confirm the duration cells 十年, 五年, 三年 and 六箇月 are four different strings in different accent colors, ')),
        dict(name='明渡しの請求と損害賠償の請求', args=dict(
            title='単独でどこまで請求できる？', sub='不法占有に対する請求（毎日ドリル 第47日 エ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings. The left header is 明渡しの請求 and the right header is 損害賠償の請求. Draw them in different accent colors (blue on the left and orange on the right) so they can never be confused or duplicated. Neither panel uses a cross mark.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 明渡しの請求
Scene: an isometric scene of one owner figure pointing a stranger figure out of a whole land plot, with the whole plot highlighted in green.
Result badges (stacked): 保存行為 | 一人で土地の全部について請求できる

RIGHT PANEL (orange accent):
Panel header: 損害賠償の請求
Scene: an isometric scene of a pie chart cut into three equal slices with one slice highlighted in orange, and a coin icon beside the slice.
Result badges (stacked): 自分の持分の割合の分 | 他の共有者の分は請求できない""",
            callout='不法占有者に出て行ってもらう請求は、一人で土地の全部についてできます。\nお金の請求は、自分の持分の割合に応じた分だけで、他の共有者の損害までは請求できません。',
            footer='民法252条5項',
            kanji='明・渡・請・求・損・害・賠・償・保・存・行・為・持・分・割・合'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (明渡しの請求 on the left and 損害賠償の請求 on the right) in different accent colors, ')),
    ],
)
