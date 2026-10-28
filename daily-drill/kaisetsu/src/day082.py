def kj(*ss, n=14):
    out = []
    for s in ss:
        for c in s:
            if '一' <= c <= '龥' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='隣地の使用は、通知が困難なら事後でよい',
    intro='隣り合う土地の所有者どうしの権利と義務（相隣関係）について、隣地を使う場合の手続、土地の一部を譲ったときの通行、隣地の竹木の枝と根の扱いを問う問題です（民法209条・213条・233条）。\n\nこの記事では、境界の測量や塀の修繕で隣地に入るとき、袋地になった土地の通行、越境した枝や根をどうするかを、具体的な場面で確認していきましょう。この問題は「誤っているもの」の組合せを選ぶ形式です。',
    sections={
        'ア': ('塀の修繕で隣地を使えるが、住家には承諾がいる',
               '土地の所有者は、境界又はその付近における障壁、建物その他の工作物の築造、収去又は修繕のため必要な範囲内で、隣地を使用することができます。ただし、住家については、その居住者の承諾がなければ、立ち入ることはできません（民法209条1項1号・ただし書）。\n\n本肢は正しいといえます。\n\n**たとえば**、自分の土地との境にある塀を直すために、隣の庭に足場を組む必要があるとします。必要な範囲であれば隣地を使えますが、隣の家の中に入るには、住んでいる人の承諾が必要です。'),
        'イ': ('通知が困難なときは、使用の後に通知すれば足りる',
               '隣地を使用する人は、あらかじめ、目的、日時、場所及び方法を隣地の所有者と隣地使用者に通知しなければなりません。ただし、あらかじめ通知することが困難なときは、使用を開始した後、遅滞なく通知すれば足ります（民法209条3項）。\n\n問題文は、通知が困難なときでも、必ず使用の開始前に通知しなければならないとしています。ただし書を見落としているので、本肢は誤りです。\n\n**たとえば**、隣の土地の所有者が長期の海外出張で連絡がつかず、境界標を調べる日が迫っているとします。あらかじめ通知することが困難なときは、使用を始めた後に、遅れず通知すれば足ります。'),
        'ウ': ('土地の一部を譲って袋地になったら、残りの土地だけを通れる',
               '土地の所有者がその土地の一部を譲り渡したために、譲り受けた土地が公道に通じなくなったときは、その土地の所有者は、公道に至るため、譲り渡した人の所有地（残りの部分）のみを通行することができます。\n\nこの場合、償金を支払う必要はありません（民法213条1項・2項）。\n\n問題文は、残りの部分に限らず、乙部分を囲む他の土地のうち損害が最も少ないものを選んで通行できるとしています。通行できるのは譲渡人の所有地に限られるので、本肢は誤りです。\n\n**たとえば**、広い土地の奥の部分を売ったところ、奥の部分が公道に出られなくなったとします。買った人は、売主が持っている手前の部分を通って公道に出ることになります。他の人の土地を通るのではありません。'),
        'エ': ('催告しても切らないときは、自分で枝を切り取れる',
               '土地の所有者は、隣地の竹木の枝が境界線を越えるときは、その竹木の所有者に枝を切除させることができます（民法233条1項）。\n\nただし、竹木の所有者に枝を切除するよう催告したにもかかわらず、相当の期間内に切除しないときは、土地の所有者が自分で枝を切り取ることができます（同条3項1号）。\n\n本肢は正しいといえます。\n\n**たとえば**、隣の庭の木の枝が自分の土地に伸びてきたので、持ち主に「切ってください」と催告したのに、相当の期間が過ぎても切ってくれなかったとします。このときは、自分で枝を切り取ることができます。'),
        'オ': ('越境した根は、催告なしで自分で切り取れる',
               '隣地の竹木の根が境界線を越えるときは、その根を切り取ることができます（民法233条4項）。枝と違って、竹木の所有者に切除させる手順や催告は、要件になっていません。\n\n本肢は正しいといえます。\n\n**たとえば**、隣の木の根が自分の庭の地中に伸びてきて、花壇を傷めているとします。持ち主に催告をしなくても、境界線を越えて入ってきた根は、自分で切り取ることができます。'),
    },
    summary=[
        ('ア', '正', '塀の修繕のため必要な範囲で隣地を使えるが、住家に立ち入るには居住者の承諾が必要'),
        ('イ', '誤', 'あらかじめ通知することが困難なときは、使用の開始後、遅滞なく通知すれば足りる'),
        ('ウ', '誤', '土地の一部の譲渡で袋地になったときは、譲渡人の所有地のみを通行できる（償金は不要）'),
        ('エ', '正', '枝の切除を催告しても相当の期間内に切除しないときは、自分で枝を切り取れる'),
        ('オ', '正', '越境した根は、枝と違って、催告なしで自分で切り取れる'),
    ],
    summary_tail='イは「ただし書の見落とし」、ウは「一般の通行権との取り違え」がひっかけでした。枝と根の扱いの違い（枝は原則切除させる、根は自分で切れる）も、あわせて覚えておきましょう。',
    supplements=[
        '### 補足説明（イ）：隣地を使うときの手順\n\n隣地を使用する人は、使う前の通知が原則です。例外として、通知が困難なときは使用の後でも足ります（民法209条3項）。\n\n- 原則：あらかじめ、目的、日時、場所及び方法を、隣地の所有者と隣地使用者に通知してから使用する。\n- 例外：あらかじめ通知することが困難なときは、使用を開始した後、遅滞なく通知する。\n\nまた、使用の日時、場所及び方法は、隣地の所有者と隣地使用者のために損害が最も少ないものを選びます（同条2項）。損害を受けた人は、償金を請求できます（同条4項）。\n\n**たとえば**、境界標の調査のために隣地に入るなら、原則は事前の通知です。ところが、持ち主の所在が分からず事前の通知が難しいときは、調査を始めた後で、遅れずに知らせれば足ります。',
        '### 補足説明（ウ）：袋地の通行権は、場面で範囲が違う\n\n公道に通じない土地の所有者が通行できる範囲は、なぜ公道に通じなくなったかで違います。\n\n| 場面 | 通行できる土地 | 償金 | 根拠 |\n|---|---|---|---|\n| 他の土地に囲まれて、もともと公道に通じない | 囲んでいる他の土地 | 支払う | 210条・212条 |\n| 土地の分割で公道に通じなくなった | 他の分割者の所有地のみ | 不要 | 213条1項 |\n| 土地の一部の譲渡で公道に通じなくなった | 譲渡人の所有地のみ | 不要 | 213条2項 |\n\n**たとえば**、もともと他人の土地に囲まれていた土地なら、囲んでいる土地のうち損害が最も少ない所を選んで通行できます（211条）。しかし、自分の土地の一部を売って袋地にしたときは、売主の残りの土地だけを通ります。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第82日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、民法209条、210条、211条、212条、213条、233条は、`note-articles/laws/` 配下の原文で確認しました。',
        '具体例（塀の修繕、海外出張中の所有者、広い土地の奥の部分の売却、隣の木の根など）は、条文の文言を日常の場面にかみ砕いた説明で、個別の判例や運用の確認はしていません。',
        '補足説明（ウ）の表は、民法210条から213条までの規定を並べたものです。袋地の通行権の細かい論点（通路の開設の可否など）は扱っていません。',
    ],
    phrases=['住家に入るには承諾がいります', '通知が困難なら使った後でも大丈夫', '一部を譲ったら通れるのは残りの土地だけ', '催告しても切らなければ自分で切れます', '根は催告なしで切り取れます'],
    header=dict(t1='お隣の土地は、', t2='どう使える？', topic='民法　相隣関係',
                kanji='隣・土・地・使・民・法・関・係・毎'),
    poster_intro='相隣関係を、「隣地の使用と通行」（グループA：ア・イ・ウ）と「竹木の枝と根」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='相隣関係を整理', sub='民法 第209条・第213条・第233条（毎日ドリル 第82日）',
        col_a='隣地の使用と通行', col_b='竹木の枝と根', n_a=3,
        cards=[
            dict(h='住家に入るには居住者の承諾',
                 ill='a worker figure on a ladder repairing a wall along a land boundary. On the neighbor\'s side, a resident figure stands at the door of a house holding a card labeled 「承諾」.',
                 words=['承諾'], tag='塀の修繕は使用できる'),
            dict(h='通知が困難なら使用後に通知',
                 ill='a horizontal timeline. A flag labeled 「使用」 on the left and a later flag labeled 「通知」 on the right, joined by a green bracket.',
                 words=['使用', '通知'], tag='遅滞なく通知'),
            dict(h='一部を譲ったら通れるのは残りの土地',
                 ill='a land plot divided into a back part and a front part. The front part touches a road labeled 「公道」. A path arrow runs through the front part to the road. Surrounding neighbor plots are drawn in pale gray with no arrow.',
                 words=['公道'], tag='償金も不要'),
            dict(h='催告しても切らなければ自分で',
                 ill='a tree branch crossing a boundary line. An owner figure holds a letter labeled 「催告」 toward the neighbor, and in the next scene holds pruning shears near the branch.',
                 words=['催告'], tag='相当の期間のあと'),
            dict(h='根は自分で切り取れる',
                 ill='tree roots crossing under the boundary line into the owner figure\'s garden. The owner figure holds pruning shears near the roots.',
                 words=[], tag='催告は不要'),
        ],
        kanji=kj('住家居者承諾通知困難使用公道残催告切根', n=22)),
    nb_label='イ・ウ肢', nb_intro='イ・ウの補足説明に合わせた2枚です。1枚目は、隣地を使うときの通知の原則と例外を時間の流れで示します。2枚目は、袋地の通行権の範囲を、場面ごとに表で示します。',
    notebooks=[
        dict(name='隣地を使うときの通知', args=dict(
            title='隣地を使うとき、通知はいつ？', sub='民法209条3項（毎日ドリル 第82日 イ）',
            req='a timeline diagram',
            layout="""--- TIMELINE ---
Render as a clean flat-design horizontal timeline in the upper half, with two lanes stacked vertically. A common timeline axis runs left to right with two flags: the left flag labeled 使用の開始 with an icon of a surveyor figure stepping into a neighboring plot, and the right flag labeled 遅滞なく with an icon of a clock.
Upper lane (blue accent), lane label: 原則. A blue bracket spans the stretch just before the left flag and ends at the left flag, labeled あらかじめ通知する.
Lower lane (green accent), lane label: 通知が困難なとき. A green bracket starts at the left flag and extends to the right flag, labeled 使用の後に通知する.
Use exactly these strings, and no others, for the labels. The two bracket labels are different strings; draw them in different accent colors (blue and green).""",
            callout='あらかじめ通知することが困難なときは、使用を開始した後、遅滞なく通知すれば足ります。\n通知が困難でなければ、事前の通知が原則です。',
            footer='民法209条3項',
            kanji=kj('隣地使用開始通知困難原則遅滞', n=14), what='timeline',
            check='confirm the two lanes have different bracket labels in different accent colors, ')),
        dict(name='袋地の通行権の範囲', args=dict(
            title='袋地は、どこを通れる？', sub='民法210条から213条まで（毎日ドリル 第82日 ウ）',
            req='a comparison table',
            layout="""--- TABLE ---
Render as a clean flat-design table with a header row and three body rows, in rounded panel style. Each body row carries a small icon at the left edge (a plot surrounded by other plots, a plot divided in two, a plot with one part sold).
Header row (blue accent), three column headers: 場面 | 通行できる土地 | 償金
Row 1: もともと囲まれている | 囲んでいる他の土地 | 支払う
Row 2: 分割で袋地になった | 他の分割者の所有地のみ | 不要
Row 3: 一部の譲渡で袋地になった | 譲渡人の所有地のみ | 不要
Use exactly these strings, and no others. Do not use check marks or cross marks.""",
            callout='土地の一部を譲り渡して袋地になったときは、譲渡人の所有地のみを通行でき、償金は要りません。\n他の人の土地まで広がるのではありません。',
            footer='民法210条・212条・213条',
            kanji=kj('場面通行土地償金囲分割譲渡所有者', n=16), what='table',
            check='confirm the table has exactly three body rows and that no check mark or cross mark appears, ')),
    ],
)
