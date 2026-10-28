def kj(*ss, n=14):
    out = []
    for s in ss:
        for c in s:
            if '一' <= c <= '龥' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='主な用途が二つなら二つとも書く',
    intro='登記の対象となる「建物」とは何か、一つの建物として数えるのはどこまでか、そして建物の種類や構造をどう書くのかを問う問題です（不動産登記規則113条、不動産登記事務取扱手続準則77条・78条・80条・81条）。\n\nこの記事では、建物として取り扱うものと取り扱わないものの「ただし書」、所有者の意思で個数が変わる場面、複数の用途や材料があるときの書き方を、具体的な場面で確認していきましょう。この問題は「誤っているもの」の組合せを選ぶ形式です。',
    sections={
        'ア': ('野球場の観覧席は、屋根のある部分だけが建物',
               '野球場や競馬場の観覧席は、屋根を有する部分に限り、建物として取り扱います（不動産登記事務取扱手続準則77条1号イ）。\n\n本肢は正しいといえます。\n\n**たとえば**、野球場のスタンドのうち、屋根が掛かっている席の部分は建物として取り扱われます。屋根のない席の部分は、建物としては取り扱われません。'),
        'イ': ('機械の上の建造物でも、基脚や支柱があれば除かれる',
               '機械上に建設した建造物は、建物として取り扱いません。ただし、地上に基脚を有し、又は支柱を施したものは、この取り扱わないものから除かれます（不動産登記事務取扱手続準則77条2号イ）。\n\n問題文は、地上に基脚を有するものであっても建物として取り扱わないとしています。ただし書を見落としているので、本肢は誤りです。\n\n**たとえば**、工場の大きな機械の上に作業室を載せた場合、作業室が機械だけに載っているのなら、建物として取り扱いません。しかし、作業室を支える脚が地面まで届いているときは、取り扱わないものからは除かれます。'),
        'ウ': ('効用上一体の建物も、所有者の意思しだいで別の建物になる',
               '効用上一体として利用される状態にある数棟の建物は、所有者の意思に反しない限り、1個の建物として取り扱います（不動産登記事務取扱手続準則78条1項）。\n\n「所有者の意思に反しない限り」という条件が付いていますから、所有者が別個に登記することを望んでいるなら、物置は居宅とは別の1個の建物として取り扱われます。本肢は正しいといえます。\n\n**たとえば**、居宅と物置を一緒に使っていても、所有者が「物置は別の建物として登記したい」と望むなら、居宅と物置は別々の建物として扱うことができます。'),
        'エ': ('主たる用途が二つなら、二つの用途で種類を定める',
               '建物の主な用途が二以上の場合には、その二以上の用途により建物の種類を定めます（不動産登記規則113条2項）。準則でも、「居宅・店舗」のように表示するとされています（不動産登記事務取扱手続準則80条2項）。\n\n問題文は、床面積の大きい方の用途により種類を定めるとしています。一つに絞るのではなく、二つの用途を並べて書くので、本肢は誤りです。\n\n**たとえば**、1階が美容室、2階が住まいで、どちらも主な用途であれば、建物の種類は「居宅・店舗」と表示します。床面積が大きい方の「店舗」だけにはしません。'),
        'オ': ('構成材料が違えば、「木・鉄骨造」のように並べて書く',
               '建物の主たる部分の構成材料が異なる場合には、例えば「木・鉄骨造」と表示します。屋根の種類が異なる場合も、例えば「かわら・亜鉛メッキ鋼板ぶき」と並べて表示します（不動産登記事務取扱手続準則81条2項）。\n\n本肢は正しいといえます。\n\n**たとえば**、建物の主要な部分が木造と鉄骨造の組合せでできているときは、どちらか一方に決めずに、「木・鉄骨造」と書きます。'),
    },
    summary=[
        ('ア', '正', '野球場の観覧席は、屋根を有する部分に限り、建物として取り扱う'),
        ('イ', '誤', '機械上に建設した建造物でも、地上に基脚を有し、又は支柱を施したものは、取り扱わないものから除かれる'),
        ('ウ', '正', '効用上一体の建物も、所有者が別個の登記を望むなら、別の1個の建物として取り扱われる'),
        ('エ', '誤', '主たる用途が二以上のときは、床面積の大きい方に絞らず、二以上の用途で種類を定める'),
        ('オ', '正', '主たる部分の構成材料が異なるときは、「木・鉄骨造」のように並べて表示する'),
    ],
    summary_tail='イは「ただし書の見落とし」、エは「一つに絞る」という条件のすり替えです。建物の認定は「〜に限る」「ただし〜を除く」の言葉に注意して読みましょう。',
    supplements=[
        '### 補足説明（イ）：ただし書きで結論が変わる例\n\n準則77条の例示には、原則に「ただし」で例外が付いているものが多くあります。結論を取り違えやすいので、まとめて確認します。\n\n| 例 | 原則 | ただし書き |\n|---|---|---|\n| 停車場の乗降場 | 建物として取り扱う | 上屋を有する部分に限る |\n| 野球場の観覧席 | 建物として取り扱う | 屋根を有する部分に限る |\n| 機械上に建設した建造物 | 建物として取り扱わない | 地上に基脚を有し、又は支柱を施したものは除く |\n| 浮船を利用したもの | 建物として取り扱わない | 固定しているものは除く |\n\n**たとえば**、駅のホームは、屋根（上屋）のある部分だけが建物の扱いで、屋根のない部分は建物の扱いになりません。「ただし書き」を読み落とすと、全体が建物だと誤解してしまいます。',
        '### 補足説明（エ・オ）：複数あるときの書き方\n\n用途や材料が複数あるときは、一つに絞らず、並べて書くのが基本です。\n\n| 場面 | 書き方 | 根拠 |\n|---|---|---|\n| 主たる用途が二つある | 居宅・店舗 | 規則113条2項、準則80条2項 |\n| 構成材料が異なる | 木・鉄骨造 | 準則81条2項 |\n| 屋根の種類が異なる | かわら・亜鉛メッキ鋼板ぶき | 準則81条2項 |\n\n**たとえば**、1階が店舗、2階が居宅の建物を登記するなら、種類は「居宅・店舗」です。柱や梁が木造と鉄骨造でできているなら、構造は「木・鉄骨造」です。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第77日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記規則113条、不動産登記事務取扱手続準則77条、78条、80条、81条は、`note-articles/laws/` 配下の原文で確認しました。',
        'イとウの具体例（機械の上の作業室、居宅と物置）は、準則の文言をかみ砕いた一般的な説明で、個別の登記実務の取扱いの確認はしていません。',
        '補足説明の表（浮船、停車場の乗降場など）は準則77条の例示の整理です。例示は「類推し、利用状況等を勘案して判定する」ものとされており、個別の事案の結論を保証するものではありません。',
    ],
    phrases=['屋根のある観覧席だけが建物です', '基脚や支柱があれば除かれます', '別々に登記したいなら別の建物です', '用途が二つなら二つとも書きます', '木と鉄骨なら並べて書きます'],
    header=dict(t1='建物かどうか、', t2='どう書く？', topic='不動産登記法　建物の認定と表示',
                kanji='建・物・認・定・表・示・毎'),
    poster_intro='建物の認定と表示を、「建物かどうかと個数」（グループA：ア・イ・ウ）と「種類と構造の書き方」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='建物の認定と表示を整理', sub='不動産登記規則 第113条と準則 第77条〜第81条（毎日ドリル 第77日）',
        col_a='建物かどうかと個数', col_b='種類と構造の書き方', n_a=3,
        cards=[
            dict(h='屋根のある観覧席は建物',
                 ill='an isometric baseball stadium stand. The roofed section is shaded green. The section without a roof is drawn in pale gray. A green check mark sits beside the roofed section.',
                 words=[], tag='屋根の部分だけ'),
            dict(h='基脚や支柱があれば除外',
                 ill='a large factory machine with a small work room on top. The work room is held up by legs that reach the ground, labeled 「基脚」 and 「支柱」 with thin lines. A green check mark sits beside the legs.',
                 words=['基脚', '支柱'], tag='取り扱わない例から除く'),
            dict(h='別々に登記したいなら別の建物',
                 ill='a house and a storage shed side by side inside one dashed outline. The owner figure holds two separate registration forms, one for the house and one for the shed.',
                 words=[], tag='所有者の意思しだい'),
            dict(h='居宅と店舗なら二つとも',
                 ill='a two-story building with a shop on the first floor and a living room on the second floor. A label plate in front of the building shows 「居宅・店舗」.',
                 words=['居宅・店舗'], tag='一つに絞らない'),
            dict(h='木と鉄骨なら並べて書く',
                 ill='a cut-away view of a building frame whose lower half is built of wooden beams and whose upper half is built of steel beams. A label plate shows 「木・鉄骨造」.',
                 words=['木・鉄骨造'], tag='構成材料が異なるとき'),
        ],
        kanji=kj('屋根観覧席基脚支柱別登記所有者居宅店舗木鉄骨', n=24)),
    nb_label='イ・エ・オ肢', nb_intro='イ・エ・オの補足説明に合わせた2枚です。1枚目は、ただし書きで結論が変わる例を表で示します。2枚目は、複数の用途や材料があるときの書き方を表で示します。',
    notebooks=[
        dict(name='ただし書きで結論が変わる例', args=dict(
            title='ただし書きに注意', sub='不動産登記事務取扱手続準則77条（毎日ドリル 第77日 イ）',
            req='a comparison table',
            layout="""--- TABLE ---
Render as a clean flat-design table with a header row and four body rows, in rounded panel style. Each body row carries a small icon at the left edge (a station platform with a roof, a stadium stand, a machine with legs, a floating boat).
Header row (blue accent), three column headers: 例 | 原則 | ただし書き
Row 1: 停車場の乗降場 | 建物として取り扱う | 上屋を有する部分に限る
Row 2: 野球場の観覧席 | 建物として取り扱う | 屋根を有する部分に限る
Row 3: 機械上に建設した建造物 | 建物として取り扱わない | 基脚や支柱があるものは除く
Row 4: 浮船を利用したもの | 建物として取り扱わない | 固定しているものは除く
Use exactly these strings, and no others. Do not use check marks or cross marks.""",
            callout='機械上に建設した建造物は、原則は建物として取り扱いませんが、地上に基脚を有し、又は支柱を施したものは除かれます。\n「ただし」以下を読み落とさないようにしましょう。',
            footer='不動産登記事務取扱手続準則77条',
            kanji=kj('例原則建物取扱停車場乗降上屋野球観覧席機械基脚支柱浮船', n=16), what='table',
            check='confirm the table has exactly four body rows and that no check mark or cross mark appears, ')),
        dict(name='複数あるときの書き方', args=dict(
            title='複数あるときは、並べて書く', sub='建物の種類と構造（毎日ドリル 第77日 エ・オ）',
            req='a comparison table',
            layout="""--- TABLE ---
Render as a clean flat-design table with a header row and three body rows, in rounded panel style. Each body row carries a small icon at the left edge (a shop with a house, a wooden beam with a steel beam, two kinds of roof tiles).
Header row (blue accent), two column headers: 場面 | 書き方
Row 1: 居宅と店舗が主な用途 | 居宅・店舗
Row 2: 木造と鉄骨造が混在 | 木・鉄骨造
Row 3: かわらと亜鉛メッキ鋼板の屋根 | かわら・亜鉛メッキ鋼板ぶき
Use exactly these strings, and no others. Do not use check marks or cross marks.""",
            callout='用途や材料が複数あるときは、床面積の大きい方などに絞らず、並べて書きます。',
            footer='不動産登記規則113条2項、準則80条2項・81条2項',
            kanji=kj('居宅店舗木造鉄骨屋根場面書方', n=16), what='table',
            check='confirm the table has exactly three body rows and that no check mark or cross mark appears, ')),
    ],
)
