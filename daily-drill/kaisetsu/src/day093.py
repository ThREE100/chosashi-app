def _k(*t, n=24):
    out = []
    for c in ''.join(t):
        if '一' <= c <= '龥' and c not in out:
            out.append(c)
    return out[:n]


_T1, _T2, _TOP = '建物と扱われるか、', '一個か二個か？', '不動産登記事務取扱手続準則　建物の認定'
_cards = [
    dict(h='基脚のある作業室は建物',
         ill='an isometric factory machine with a small work room built on top of it. The work room stands on sturdy legs that reach the ground, with small footing blocks at the bottom of each leg. A tag labeled 「基脚」 points to one footing block. A green check mark sits beside the work room.',
         words=['基脚'], tag='機械の上でも地上に基脚あり'),
    dict(h='乗降場は上屋のある部分が建物',
         ill='an isometric railway platform. Only the middle part of the platform is covered by a roof, highlighted with a green glow, and a label 「上屋」 hangs on the roof. The parts without a roof are drawn faded. A green check mark sits beside the roof.',
         words=['上屋'], tag='上屋のない部分は対象外'),
    dict(h='アパートの廊下は別個の建物にならない',
         ill='an isometric apartment building with several rooms opening onto a shared corridor. The corridor is outlined with a dashed line as part of the whole building, and a label 「廊下」 sits on it. A green check mark sits beside the whole building outline.',
         words=['廊下'], tag='共用部分は別に登記できない'),
    dict(h='同じ所有者なら一棟を一個の建物に',
         ill='an isometric two-story house with a clearly separated first floor and second floor, each with its own door. A single large outline surrounds both floors, and a figure carrying a name tag labeled 「所有者」 stands in front. A green check mark sits beside the large outline.',
         words=['所有者'], tag='所有者の意思に反しない限り'),
    dict(h='二つの主な用途を並べて種類を表す',
         ill='an isometric building with a shop on the first floor and a living room on the second floor. Two small sign boards stand in front of it side by side, one labeled 「居宅」 and the other labeled 「店舗」. A green check mark sits beside the sign boards.',
         words=['居宅', '店舗'], tag='主な用途が二つなら二つ書く'),
]

D = dict(
    catch='建物かどうかは準則の例で判断',
    intro='ある建造物を「建物」として登記できるのか、いくつの建物として数えるのか、種類をどう書くのか、を問う問題です（不動産登記規則113条、不動産登記事務取扱手続準則77条・78条・80条）。この問題は、誤っているものの組合せを選びます。\n\nこの記事では、「建物として扱うもの・扱わないもの」の例と、「一個の建物か、別々の建物か」の考え方を、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('機械上の建造物でも、地上に基脚があれば、建物として扱う',
               '機械上に建設した建造物は、建物として取り扱わないとされています。ただし、地上に基脚を有し、又は支柱を施したものは除かれます（不動産登記事務取扱手続準則77条2号イ）。\n\n問題文は、地上に基脚を有する作業室を「建物として取り扱わない」としているので、本肢は誤りです。\n\n**たとえば**、工場内の機械の上に作業室があっても、その作業室が地上に基脚を有しているなら、建物として取り扱います。機械の上に載っているだけの建造物とは区別されます。'),
        'イ': ('停車場の乗降場は、上屋を有する部分に限って建物として扱う',
               '停車場の乗降場や荷物積卸場は、上屋を有する部分に限り、建物として取り扱います（不動産登記事務取扱手続準則77条1号ア）。\n\n本肢は正しいといえます。\n\n**たとえば**、B鉄道会社の駅のホームのうち、屋根（上屋）のかかっている部分だけが建物になります。屋根のない部分は、建物にはなりません。'),
        'ウ': ('アパートの廊下は、申出があっても別個の建物として扱えない',
               '数個の専有部分に通ずる廊下（例えば、アパートの各室に通ずる廊下）、階段室、エレベーター室、屋上など、構造上、区分所有者の全員又は一部の共用に供されるべき建物の部分は、各別に1個の建物として取り扱うことができません（不動産登記事務取扱手続準則78条3項）。\n\n問題文は、所有者の申出があれば各別に登記できるとしているので、本肢は誤りです。\n\n**たとえば**、Cさんのアパートの各部屋に通じる廊下は、構造上区分されていても、廊下だけを独立した一つの建物として登記することはできません。'),
        'エ': ('所有者が同一なら、その意思に反しない限り、一棟全部を一個の建物として扱う',
               '一棟の建物に、構造上区分された数個の部分で、独立して住居などに使えるものがあるときは、原則として、その各部分を各別に1個の建物として取り扱います。ただし、所有者が同一であるときは、その所有者の意思に反しない限り、一棟の建物の全部を1個の建物として取り扱います（不動産登記事務取扱手続準則78条2項）。\n\n本肢は正しいといえます。\n\n**たとえば**、Dさんが二世帯住宅を新築し、1階と2階がそれぞれ独立して住める構造だったとしても、Dさんが一つの建物として登記することを望むなら、一棟全部が1個の建物になります。'),
        'オ': ('主な用途が二つなら、二つの用途で種類を表す',
               '建物の主な用途が二つ以上のときは、その二つ以上の用途により、建物の種類を定めます（不動産登記規則113条2項）。例えば「居宅・店舗」のように表示します（不動産登記事務取扱手続準則80条2項）。\n\n本肢は正しいといえます。\n\n**たとえば**、Eさんが新築した建物の1階が店舗、2階が居宅で、どちらも主な用途であれば、種類は「居宅・店舗」と表示します。'),
    },
    summary=[
        ('ア', '誤', '機械上の建造物でも、地上に基脚を有するものは建物として扱う（ただし書）'),
        ('イ', '正', '停車場の乗降場は、上屋を有する部分に限って建物として扱う'),
        ('ウ', '誤', 'アパートの廊下は、申出があっても別個の建物として扱えない'),
        ('エ', '正', '所有者が同一なら、その意思に反しない限り、一棟の全部を1個の建物として扱う'),
        ('オ', '正', '主な用途が二つなら、「居宅・店舗」のように二つの用途で種類を表す'),
    ],
    summary_tail='アは「ただし書」の見落とし、ウは「各別に1個の建物として扱えない」という決まりを入れ替えた出題です。準則77条の例は、原則とただし書をセットで覚えましょう。',
    supplements=[
        '### 補足説明（ア・イ）：建物として扱うもの、扱わないもの\n\n準則77条は、建物の認定について例を挙げています。ただし書に注意が必要です。\n\n| 建物として取り扱うもの | 建物として取り扱わないもの |\n|---|---|\n| 停車場の乗降場・荷物積卸場（上屋を有する部分に限る） | ガスタンク・石油タンク・給水タンク |\n| 野球場・競馬場の観覧席（屋根を有する部分に限る） | 機械上に建設した建造物（地上に基脚を有し、又は支柱を施したものを除く） |\n| ガード下を利用して築造した店舗、倉庫等 | 浮船を利用したもの（固定しているものを除く） |\n| 地下停車場、地下駐車場、地下街 | アーケード付街路 |\n| 園芸・農耕用の温床施設（半永久的なものに限る） | 容易に運搬できる切符売場、入場券売場等 |\n\n**たとえば**、屋根のない駅のホームの部分や、機械の上に載っているだけで基脚のない建造物は、建物として扱われません。ただし書に当てはまるかどうかが、判断の分かれ目です。',
        '### 補足説明（ウ・エ）：建物の個数の考え方\n\n一個の建物として数えるかどうかは、準則78条が定めています。\n\n- 1項：効用上一体として利用される数棟の建物は、所有者の意思に反しない限り、1個の建物として扱う。\n- 2項：一棟の建物に、構造上区分され、独立して使える部分があるときは、各別に1個の建物とするのが原則。所有者が同一なら、所有者の意思に反しない限り、一棟全部を1個の建物とすることもできる。\n- 3項：廊下、階段室、エレベーター室、屋上など共用に供されるべき部分は、各別に1個の建物としては扱えない。\n\n**たとえば**、二世帯住宅は、1階と2階を別々の建物にも、一棟全部で一つの建物にもできます（2項）。しかし、アパートの廊下だけを一つの建物にすることはできません（3項）。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第93日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記規則113条2項、不動産登記事務取扱手続準則77条、78条、80条2項は、`note-articles/laws/` 配下の原文で確認しました。',
        'オの種類の表示の順序（「居宅・店舗」）は、準則80条2項の例示の表記に合わせたもので、用途の順序について条文に定めがあるかどうかは確認していません。',
        '具体例のうち、駅のホーム、アパートの廊下、二世帯住宅は、条文の言葉（停車場の乗降場、アパートの各室に通ずる廊下、二世帯を含む一棟の建物の各部分）に沿って作った例です。',
    ],
    phrases=['基脚があれば機械上でも建物です', '乗降場は上屋のある部分だけ建物です', 'アパートの廊下は別の建物にできません', '同じ所有者なら一棟を一個にできます', '主な用途が二つなら二つで種類を表します'],
    header=dict(t1=_T1, t2=_T2, topic=_TOP, kanji='・'.join(_k(_T1, _T2, _TOP))),
    poster_intro='建物の認定と個数と種類を、「建物の認定と共用部分」（グループA：ア・イ・ウ）と「個数と種類」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='建物の認定と個数を整理', sub='不動産登記規則 第113条、準則 第77条・第78条・第80条（毎日ドリル 第93日）',
        col_a='建物の認定と共用部分', col_b='個数と種類', n_a=3,
        cards=_cards,
        kanji=_k(*[c['h'] + c['tag'] + ''.join(c['words']) for c in _cards], '建物の認定と個数を整理建物の認定と共用部分個数と種類', n=24)),
    nb_label='ア・イ・ウ・エ肢', nb_intro='ア・イ・ウ・エの補足説明に合わせた2枚です。1枚目は、建物として扱うものと扱わないものを左右の対比で示します。2枚目は、建物の個数の考え方を表で整理します。',
    notebooks=[
        dict(name='建物として扱うもの、扱わないもの', args=dict(
            title='建物として扱うもの、扱わないもの', sub='準則77条の例（毎日ドリル 第93日 ア・イ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two sides must show OPPOSITE marks, not the same mark. The left side shows a green check mark; the right side shows a red cross. The two panel headers are different strings: 「建物として取り扱う」 on the left and 「建物として取り扱わない」 on the right; draw them in different accent colors (blue and gray) so they can never be confused or duplicated. Keep the parenthesized conditions exactly as written, because they are the key point.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 建物として取り扱う
Items (a plain list with a small icon beside each):
停車場の乗降場（上屋を有する部分に限る）
野球場、競馬場の観覧席（屋根を有する部分に限る）
ガード下を利用した店舗、倉庫
地下停車場、地下駐車場、地下街
園芸、農耕用の温床施設（半永久的なものに限る）
Result badge with a green check mark: 建物

RIGHT PANEL (gray accent):
Panel header: 建物として取り扱わない
Items (a plain list with a small icon beside each):
ガスタンク、石油タンク、給水タンク
機械上の建造物（地上に基脚を有するか支柱を施したものを除く）
浮船を利用したもの（固定しているものを除く）
アーケード付街路
容易に運搬できる切符売場、入場券売場
Result badge with a red cross: 建物ではない""",
            callout='準則77条の例には、「上屋を有する部分に限る」「基脚を有するものを除く」のように、ただし書や条件がついています。\n原則だけでなく、条件までセットで覚えることが大切です。',
            footer='不動産登記事務取扱手続準則77条',
            kanji='・'.join(_k('建物取扱停車場乗降場上屋野球競馬観覧席屋根地下駐車半永久温床施設浮船基脚支柱不動産登記事務手続準則')), what='panels',
            check='confirm the two panel headers are different strings (建物として取り扱う on the left and 建物として取り扱わない on the right), that the left panel shows a green check mark while the right panel shows a red cross, and that every parenthesized condition is copied verbatim, ')),
        dict(name='建物の個数の考え方', args=dict(
            title='建物の個数の考え方', sub='準則78条（毎日ドリル 第93日 ウ・エ）',
            req='a three-row table',
            layout="""--- TABLE ---
A table with three rows. Each row has a scene on the left and the rule on the right, connected by a thin arrow. The three rule boxes are drawn in three different accent colors (blue, green, orange).
Row 1: scene 「効用上一体として利用される数棟の建物」 (a house and a small shed joined by a path) → 所有者の意思に反しない限り、1個の建物
Row 2: scene 「構造上区分され、独立して使える数個の部分がある一棟の建物」 (a two-story house with two doors) → 原則は各部分が別々の建物。所有者が同一なら、意思に反しない限り、一棟全部を1個の建物にできる
Row 3: scene 「数個の専有部分に通ずる廊下、階段室、エレベーター室、屋上」 (an apartment corridor and a stairwell) → 各別に1個の建物としては扱えない""",
            callout='構造上区分された部分は、原則として別々の建物ですが、所有者が同一ならまとめて一個にもできます。\nアパートの廊下のような共用部分だけは、別々の建物にできません。',
            footer='不動産登記事務取扱手続準則78条1項から3項',
            kanji='・'.join(_k('建物個数効用上一体数棟構造区分独立専有部分廊下階段室屋上所有者同一意思不動産登記事務取扱手続準則')), what='table',
            check='confirm the three rule boxes are drawn in three different accent colors and that each row is copied verbatim, ')),
    ],
)
