D = dict(
    catch='建物かどうかは、屋根や上屋で決まる',
    intro='登記上の「建物」にあたるか、建物の個数や家屋番号をどう定めるか、階数をどう数えるかを問う問題です（不動産登記事務取扱手続準則77条から79条まで・81条）。正しいものの組合せを選びます。\n\nこの記事では、観覧席や乗降場の「屋根・上屋のある部分に限る」という条件、母屋と離れの扱い、複数の土地にまたがる建物の家屋番号、天井の低い屋階の扱いを、具体的な場面で確認します。',
    sections={
        'ア': ('野球場の観覧席は、屋根のある部分に限って建物',
               '野球場又は競馬場の観覧席は、屋根を有する部分に限り、建物として取り扱います（準則77条1項1号イ）。\n\n問題文は「屋根を有しない部分を含め、その全体」としているので、本肢は誤りです。\n\n**たとえば**、屋根のかかった座席の部分は建物として扱われますが、屋根のないスタンドの部分は建物として扱われません。'),
        'イ': ('停車場の乗降場は、上屋のある部分に限って建物',
               '停車場の乗降場又は荷物積卸場は、上屋を有する部分に限り、建物として取り扱います（準則77条1項1号ア）。\n\n本肢は正しいといえます。\n\n**たとえば**、駅のホームのうち、屋根（上屋）がかかっている部分だけが建物として扱われます。屋根のない部分は建物ではありません。'),
        'ウ': ('一体で使う母屋と離れでも、所有者の意思を優先する',
               '効用上一体として利用される状態にある数棟の建物は、所有者の意思に反しない限り、1個の建物として取り扱います（準則78条1項）。\n\n問題文は、所有者が別個の建物として登記したいと希望している場合でも、1個の建物として取り扱わなければならないとしているので、本肢は誤りです。\n\n**たとえば**、母屋と離れを1個の建物とするのが原則ですが、所有者が離れを別の建物として登記したいと希望するなら、それに反してまで1個にまとめることはありません。'),
        'エ': ('複数の土地にまたがる建物は、床面積の多い部分の土地の地番',
               '2筆以上の土地にまたがって1個の建物がある場合、附属建物がないときは、床面積の多い部分がある敷地の地番と同じ番号を家屋番号とします（準則79条3号）。\n\n問題文は「地番の若い5番」としているので、本肢は誤りです。\n\n**たとえば**、5番の土地の上に30平方メートル、6番の土地の上に90平方メートルの部分がある建物なら、床面積の多い6番の土地の上にあるので、家屋番号は6番です。'),
        'オ': ('天井の高さ1.5メートル未満の屋階は、階数に数えない',
               '天井の高さ1.5メートル未満の地階及び屋階等（特殊階）は、階数に算入しません（準則81条4項）。\n\n本肢は正しいといえます。\n\n**たとえば**、2階建の居宅の2階の上に、天井の高さが1.4メートルの屋根裏の部屋があるとします。1.5メートル未満なので階数に数えず、この建物は2階建のままです。'),
    },
    summary=[
        ('ア', '誤', '野球場の観覧席は、屋根を有する部分に限り建物として取り扱う'),
        ('イ', '正', '停車場の乗降場は、上屋を有する部分に限り建物として取り扱う'),
        ('ウ', '誤', '効用上一体の数棟を1個の建物とするのは、所有者の意思に反しない限りである'),
        ('エ', '誤', '附属建物がない場合の家屋番号は、床面積の多い部分がある敷地の地番と同じにする'),
        ('オ', '正', '天井の高さ1.5メートル未満の屋階は、階数に算入しない'),
    ],
    summary_tail='アは「屋根のある部分に限る」を「全体」、ウは「所有者の意思に反しない限り」を「必ず」、エは「床面積の多い部分」を「地番の若い方」に入れ替えた出題です。条件の言葉を、ひとつずつ確かめましょう。',
    supplements=[
        '### 補足説明（ア・イ）：「屋根・上屋のある部分に限る」施設\n\n準則77条は、観覧席や乗降場のように一部だけが建物になる施設を、次のように定めています。床面積も、建物になる部分だけで計算します。\n\n- 停車場の乗降場・荷物積卸場：上屋を有する部分に限り建物。床面積は上屋の占める部分で計算する（準則82条2号）。\n- 野球場・競馬場の観覧席：屋根を有する部分に限り建物。床面積は屋根の設備のある部分で計算する（準則82条3号）。\n\n**たとえば**、屋根のかかった座席は建物ですが、屋根のないスタンドは建物ではなく、床面積にも入りません。',
        '### 補足説明（エ）：複数の土地にまたがる建物の家屋番号\n\n1個の建物が2筆以上の土地にまたがるときの家屋番号は、附属建物があるかどうかで決め方が変わります（準則79条3号）。\n\n- 附属建物がある：主たる建物がある敷地の地番と同じ番号。\n- 附属建物がない：床面積の多い部分がある敷地の地番と同じ番号。\n\n**たとえば**、5番と6番にまたがる建物で、6番の土地の上の床面積が多ければ、家屋番号は6番です。地番が若い5番ではありません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第29日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、準則77条1項1号ア・イ、78条1項、79条3号、81条4項、82条2号・3号は、`note-articles/laws/` 配下の準則の原文で確認しました。',
        'オの具体例は、準則81条4項の「天井の高さ1.5メートル未満の屋階等（特殊階）」を屋根裏の部屋に置き換えた説明で、個別の建物の判断ではありません。',
        'ウの「離れを別の建物として登記する」の具体例は、準則78条1項の「所有者の意思に反しない限り」の文言からの一般的な整理です。',
    ],
    phrases=['観覧席は屋根のある部分に限って建物です', '乗降場は上屋のある部分に限って建物です', '離れを別の建物にするかは所有者の意思です', '家屋番号は床面積の多い部分の地番です', '天井の低い屋階は階数に数えません'],
    header=dict(t1='建物かどうかは、', t2='どう決まる？', topic='不動産登記　建物の認定',
                kanji='建・物・決・毎・登・記・認・定'),
    poster_intro='建物の認定と登記事項を、「建物として扱う範囲と個数」（グループA：ア・イ・ウ）と「家屋番号と階数」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='建物の認定を整理', sub='不動産登記事務取扱手続準則77条から79条まで・81条（毎日ドリル 第29日）',
        col_a='建物として扱う範囲と個数', col_b='家屋番号と階数', n_a=3,
        cards=[
            dict(h='観覧席は屋根のある部分だけ建物',
                 ill='an isometric stadium grandstand cut into two parts: the part under a roof is highlighted in green and labeled 「屋根あり」, and the open part without a roof is drawn in gray. A green check mark sits beside the roofed part.',
                 words=['屋根あり'], tag='屋根のある部分に限る'),
            dict(h='乗降場は上屋のある部分だけ建物',
                 ill='an isometric station platform cut into two parts: the part under a canopy is highlighted in green and labeled 「上屋あり」, and the open part is drawn in gray. A green check mark sits beside the canopy part.',
                 words=['上屋あり'], tag='上屋のある部分に限る'),
            dict(h='別の建物にするかは所有者の意思',
                 ill='a main house and a small annex side by side, with an owner figure standing between them holding a form labeled 「別個に登記」. A green check mark sits beside the owner.',
                 words=['別個に登記'], tag='意思に反しない限り'),
            dict(h='家屋番号は床面積の多い部分の地番',
                 ill='a building lying across two land plots, with the larger part on the right plot. The right plot carries a sign labeled 「6番」 and the left plot carries a sign labeled 「5番」. A green arrow points from the larger part to the right plot. A green check mark sits beside the right plot.',
                 words=['5番', '6番'], tag='多い部分の地番'),
            dict(h='天井の低い屋階は階数に数えない',
                 ill='an isometric two-story house with a low attic room above the second floor, drawn smaller and in gray with a small height marker labeled 「1.4メートル」 on its side. A green check mark sits beside the house.',
                 words=['1.4メートル'], tag='1.5メートル未満は不算入'),
        ],
        kanji='建・物・観・覧・席・屋・根・乗・降・場・上・意・思・家・番・階・数'.split('・')),
    nb_label='ア・イ・エ肢', nb_intro='ア・イ・エの補足説明に合わせた2枚です。1枚目は、屋根・上屋のある部分に限って建物になる施設を早見表にします。2枚目は、複数の土地にまたがる建物の家屋番号の決め方を対比で示します。',
    notebooks=[
        dict(name='屋根・上屋のある部分に限る施設', args=dict(
            title='建物になるのは、どの部分？', sub='観覧席と乗降場（毎日ドリル 第29日 ア・イ）',
            req='a table',
            layout="""--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Three columns and two data rows. The header row has the column names. Each data row has a small isometric icon at the left of its first cell (a grandstand with a partial roof for the first row, a station platform with a partial canopy for the second row). Use exactly these strings, and no others:
Header row: 施設 | 建物になる部分 | 床面積
Row 1: 野球場の観覧席 | 屋根を有する部分に限る | 屋根の設備のある部分
Row 2: 停車場の乗降場 | 上屋を有する部分に限る | 上屋の占める部分
The two middle cells 「屋根を有する部分に限る」 (Row 1) and 「上屋を有する部分に限る」 (Row 2) are different strings; draw them in different accent colors (green and blue).""",
            callout='観覧席や乗降場は、屋根や上屋のある部分に限って建物として扱います。\n屋根のない部分は建物ではなく、床面積にも入りません。',
            footer='不動産登記事務取扱手続準則77条、82条',
            kanji='建・物・観・覧・席・乗・降・場・屋・根・床・面・積'.split('・'), what='table',
            check='confirm the table has exactly 3 columns and 2 data rows, confirm the two middle cells are different strings in different accent colors, ')),
        dict(name='複数の土地にまたがる建物の家屋番号', args=dict(
            title='またがる建物の家屋番号', sub='準則79条3号（毎日ドリル 第29日 エ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: neither panel uses a cross mark; no cross mark anywhere. The two panel headers are different strings: 「附属建物がある」 on the left and 「附属建物がない」 on the right; draw them in different accent colors (blue and green).

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 附属建物がある
Scene: an isometric scene of a main building and a small annex lying across two plots, with the main building highlighted on the right plot.
Result badge with a green check mark: 主たる建物のある敷地の地番

RIGHT PANEL (green accent):
Panel header: 附属建物がない
Scene: an isometric scene of one building lying across two plots, with the larger floor part highlighted on the right plot.
Result badge with a green check mark: 床面積の多い部分の敷地の地番""",
            callout='家屋番号は、附属建物があるときは主たる建物のある敷地の地番、ないときは床面積の多い部分のある敷地の地番と同じにします。\n地番が若い方、という決め方ではありません。',
            footer='不動産登記事務取扱手続準則79条3号',
            kanji='家・屋・番・号・附・属・建・物・床・面・積・敷・地'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (附属建物がある on the left and 附属建物がない on the right) in different accent colors and that no cross mark appears anywhere, ')),
    ],
)
