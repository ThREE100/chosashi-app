def kj(*ss, n=14):
    out = []
    for s in ss:
        for c in s:
            if '一' <= c <= '龥' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='共有の土地、持分と同意の関係',
    intro='甲土地をAが3分の2、Bが3分の1の持分で共有している設定で、共有者や第三者との関係を問う問題です（民法251条・252条と判例の趣旨）。この問題は、判例の趣旨に照らして正しいものを選ぶ形です。\n\nこの記事では、無断で変更されたとき、不法に占有されたとき、賃貸借を解除するとき、使っている共有者がいるときの決め方を、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('無断の変更は、持分の多少にかかわらず原状回復を請求できる',
               '共有物に著しい変更を加えるには、他の共有者全員の同意が必要です（民法251条1項）。無断で変更されたときは、原状回復が不能であるなどの特段の事情がない限り、他の共有者は原状回復を請求できる、というのが判例の趣旨です。\n\n問題文は、Aの持分が過半数だからBは請求できないとしています。持分の多少は関係ないので、本肢は誤りです。\n\n**たとえば**、Aが黙って宅地造成工事をしてしまい、元に戻すことが可能であれば、Bは「元の状態に戻してほしい」と請求できます。'),
        'イ': ('不法占有による損害の賠償は、持分に応じた部分だけ請求できる',
               '第三者が共有物を不法に占有したことによる損害賠償の請求は、各共有者が自己の持分に応じた部分に限って行うことができる、というのが判例の趣旨です。\n\n本肢は、Bが自己の持分の割合に応じた部分に限り請求できるとしているので、正しいといえます。\n\n**たとえば**、Cが甲土地を不法に占有して、賃料相当の損害が生じたとします。Bの持分は3分の1なので、Bが請求できるのは、その損害の3分の1の部分までです。'),
        'ウ': ('共有者の一人の承諾で占有する人には、当然には明渡しを求められない',
               '共有者の一人の承諾を得て共有物を占有している第三者に対し、持分の価格の過半数を有する共有者でも、当然には明渡しを請求できない、というのが判例の趣旨です。その占有には、一応の根拠があるからです。\n\n問題文は、Aが過半数だから当然に全部の明渡しを請求できるとしています。本肢は誤りです。\n\n**たとえば**、Bが「使っていいよ」と承諾してCに貸している土地について、Aが「私は3分の2だから、今すぐ出ていけ」と当然に請求することはできません。'),
        'エ': ('共有物の賃貸借の解除は管理にあたり、過半数で決められる',
               '共有物を賃貸している場合に、賃借人の債務不履行を理由として賃貸借契約を解除することは、共有物の管理に関する事項にあたり、持分の価格の過半数で決めることができる、というのが判例の趣旨です（民法252条1項）。\n\nAの持分は3分の2で、過半数を超えているので、Aは単独で解除できます。本肢は正しいといえます。\n\n**たとえば**、AとBが貸している土地の借主が賃料を払わなくなったとき、3分の2を持つAは、Bの同意がなくても解除できます。'),
        'オ': ('使っている共有者に特別の影響があるなら、その人の承諾が必要',
               '共有物の管理に関する事項を過半数で決める場合でも、共有者間の決定に基づいて共有物を使用している共有者に特別の影響を及ぼすべきときは、その共有者の承諾を得なければなりません（民法252条3項）。\n\n問題文は、Bの使用に特別の影響を及ぼす決定でも、Aは過半数だからBの承諾なしにできるとしています。本肢は誤りです。\n\n**たとえば**、決定に基づいてBが畑として使っている土地を、Aが、Bの承諾なしに月極駐車場として貸すことを決めても、Bの使用に特別の影響があれば、その決定はできません。'),
    },
    summary=[
        ('ア', '誤', '無断で変更されたときは、持分の多少に関係なく、他の共有者は原状回復を請求できる'),
        ('イ', '正', '不法占有による損害賠償は、各共有者が自己の持分に応じた部分に限って請求できる'),
        ('ウ', '誤', '共有者の一人の承諾で占有する第三者には、過半数の持分でも当然には明渡しを請求できない'),
        ('エ', '正', '共有物の賃貸借の解除は管理にあたり、持分の価格の過半数で決められる'),
        ('オ', '誤', '使用している共有者に特別の影響を及ぼすときは、その共有者の承諾が必要'),
    ],
    summary_tail='ア・ウ・オは、「過半数なら何でもできる」と思わせる出題です。持分が過半数でも、変更には全員の同意、第三者の占有には根拠の有無、使用している共有者には承諾が必要、という例外を見逃さないようにしましょう。',
    supplements=[
        '### 補足説明（ウ）：占有する第三者との関係\n\n共有地を第三者が占有しているとき、占有に根拠があるかどうかで、請求できることが変わります。\n\n| 第三者の占有 | 共有者からの請求 |\n|---|---|\n| 不法に占有している | 各共有者が、持分に応じた損害賠償を請求できる（イ） |\n| 共有者の一人の承諾を得て占有している | 過半数の持分でも、当然には明渡しを請求できない（ウ） |\n\n**たとえば**、勝手に居座っている人には、各共有者が持分に応じた賠償を求められます。これに対して、共有者の一人が承諾して貸している人には、占有する根拠があるので、他の共有者が当然に追い出すことはできません。',
        '### 補足説明（オ）：過半数でも、承諾が必要になる場面\n\n管理に関する事項は持分の価格の過半数で決められますが（民法252条1項）、例外があります。\n\n| 場面 | 結論 |\n|---|---|\n| 決定に基づいて使用している共有者がいる | その共有者に特別の影響を及ぼすべきときは、その承諾が必要（252条3項） |\n| そうした影響がない | 過半数で決められる |\n\n**たとえば**、過半数の持分を持つAが、決定に基づいてBが使っている畑を駐車場にするには、Bに特別の影響があるなら、Bの承諾が要ります。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第12日（朝）　択一」とし、note の引用の出典欄は空欄にします。この問題は、判例の趣旨に照らして「正しいものの組合せ」を選ぶ形です。',
        '各肢の根拠のうち、民法251条1項、252条1項・3項は、`note-articles/laws/` 配下の原文で確認しました。',
        'ア・イ・ウ・エの結論は判例の趣旨に基づくもので、判例の原文は手元にないため、番号は書かず、原文は未確認です。過去の年度別解説記事の整理（共有に関する判例の結論）と一致していることのみ確認しました。',
        'エの「持分の価格の過半数で解除できる」は、252条1項の管理に関する事項を過半数で決する定めと、判例の趣旨との組み合わせによる整理です。具体例は条文や判例の結論をかみ砕いた一般的な例です。',
    ],
    phrases=['無断の変更は元に戻すよう求められます', '不法占有の賠償は持分の分だけです', '承諾を得た人には当然には出ていけと言えません', '賃貸借の解除は過半数で足ります', '使っている人の承諾が要る場面があります'],
    header=dict(t1='共有の土地、', t2='過半数でどこまで？', topic='民法　共有と判例',
                kanji='共・有・過・半・数・民・法'),
    poster_intro='共有の土地をめぐる判例の結論を、「変更・損害・占有」（グループA：ア・イ・ウ）と「解除と使用」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='共有の土地をめぐる判例を整理', sub='民法 第251条・第252条と判例の趣旨（毎日ドリル 第12日）',
        col_a='変更・損害・占有', col_b='解除と使用', n_a=3,
        cards=[
            dict(h='無断の変更は、原状回復を請求できる',
                 ill='an isometric land plot graded by an excavator on the left, and on the right the same plot restored to its original shape, with a thin arrow between them. A co-owner figure raises a hand beside the arrow. A green check mark sits beside the restored plot.',
                 words=[], tag='持分の多少は関係ない'),
            dict(h='不法占有の損害賠償は持分に応じて',
                 ill='an isometric land plot with an intruder figure sitting on it, and a co-owner figure holding a pie chart labeled 「持分」 with one slice highlighted. A green check mark sits beside the highlighted slice.',
                 words=['持分'], tag='自分の持分の分だけ'),
            dict(h='承諾を得た占有者には、当然には明渡しを求められない',
                 ill='an isometric land plot with a tenant figure sitting on it holding a permission slip signed by one co-owner. A second co-owner figure stands outside with hands open, not able to push the tenant out. A green check mark sits beside the permission slip.',
                 words=[], tag='占有には根拠がある'),
            dict(h='賃貸借の解除は過半数で決められる',
                 ill='an isometric land plot with a lease document being cancelled, and the larger co-owner figure holding the cancellation notice. A label beside the larger figure reads 「過半数」. A green check mark sits beside the notice.',
                 words=['過半数'], tag='管理にあたる'),
            dict(h='使っている共有者の承諾が必要な場合',
                 ill='an isometric garden plot used by a co-owner figure, and a larger co-owner figure holding a plan sheet. The two figures exchange a handshake. A label above the handshake reads 「承諾」. A green check mark sits beside the handshake.',
                 words=['承諾'], tag='特別の影響があれば'),
        ],
        kanji=kj('変更原状回復不法占有損害賠償持分承諾賃貸借解除過半数')),
    nb_label='ウ・オ肢', nb_intro='ウ・オの補足説明に合わせた2枚です。1枚目は、占有する第三者との関係を左右の対比で示します。2枚目は、過半数でも承諾が必要になる場面を示します。',
    notebooks=[
        dict(name='占有する第三者との関係', args=dict(
            title='占有する人に、何を請求できる？', sub='共有地と第三者（毎日ドリル 第12日 イ・ウ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「不法に占有」 on the left and 「承諾を得て占有」 on the right. Draw them large and in different accent colors (orange on the left, blue on the right) so they can never be confused or duplicated. Do not draw any cross mark or check mark in this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (orange accent):
Panel header: 不法に占有
Scene: an isometric land plot with an intruder figure sitting on it and a co-owner figure standing beside it.
Text row: 各共有者が持分に応じた損害賠償を請求できる

RIGHT PANEL (blue accent):
Panel header: 承諾を得て占有
Scene: an isometric land plot with a tenant figure sitting on it holding a permission slip, and a co-owner figure standing beside it.
Text row: 過半数の持分でも当然には明渡しを請求できない""",
            callout='不法に占有している人には、各共有者が持分に応じた損害賠償を請求できます。\n共有者の一人の承諾を得て占有している人には、占有に根拠があるので、過半数の持分でも当然には明渡しを請求できません。',
            footer='判例の趣旨',
            kanji=kj('不法占有承諾共有者持分損害賠償請求過半数明渡'), what='panels',
            check='confirm the two panel headers are different strings drawn in different accent colors, and that no check mark or cross mark appears anywhere, ')),
        dict(name='過半数でも承諾が必要になる場面', args=dict(
            title='過半数でも、承諾が要る場面', sub='民法252条3項（毎日ドリル 第12日 オ）',
            req='a step-by-step flow diagram',
            layout="""--- FLOW ---
A clean flat-design vertical flow with three steps connected by downward arrows.

Step 1 (blue box): 持分の価格の過半数で管理に関する事項を決める
Icon: a larger co-owner figure holding a plan sheet.

Step 2 (orange box): 決定に基づいて使用している共有者に、特別の影響を及ぼすべきとき
Icon: a smaller co-owner figure tending a vegetable garden.

Step 3 (green box): その共有者の承諾を得なければならない
Icon: a handshake between the two figures.""",
            callout='管理に関する事項を過半数で決めるときでも、決定に基づいて使用している共有者に特別の影響を及ぼすべきときは、その共有者の承諾が必要です。',
            footer='民法252条1項・3項',
            kanji=kj('持分価格過半数管理決定使用共有者特別影響承諾'), what='flow',
            check='confirm that the three steps are connected by downward arrows and that the third step reads その共有者の承諾を得なければならない, ')),
    ],
)
