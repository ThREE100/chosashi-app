D = dict(
    catch='床面積に入るもの、階数に入るもの',
    intro='建物の表題登記で、床面積と階数をどう定めるかを問う問題です（不動産登記規則115条、不動産登記事務取扱手続準則81条・82条）。壁のどこで測るのか、天井が低い部分や出窓、屋外の階段は数えるのかが、細かく決まっています。\n\nこの記事では、床面積に入るものと入らないものを、具体的な場面で確かめましょう。この問題は、正しい記述の組合せを選ぶ形です。',
    sections={
        'ア': ('区分建物の床面積は、壁の内側線で測る',
               '建物の床面積は、各階ごとに壁その他の区画の中心線で囲まれた部分の水平投影面積により定めます。ただし、区分建物は、壁その他の区画の内側線で囲まれた部分によります（不動産登記規則115条）。\n\n問題文は、区分建物の床面積を中心線で測るとしているので、本肢は誤りです。\n\n**たとえば**、分譲マンションの一室の床面積は、壁の厚みの真ん中までは含めず、部屋の内側の線で測ります。一戸建ての居宅なら、壁の中心線で測ります。'),
        'イ': ('1室の一部が低い天井でも、その部分は算入する',
               '天井の高さ1.5メートル未満の地階及び屋階は、床面積に算入しません。ただし、1室の一部が天井の高さ1.5メートル未満であっても、その部分は、その1室の面積に算入します（不動産登記事務取扱手続準則82条1号）。\n\n本肢は正しい記述です。\n\n**たとえば**、2階の洋室の屋根が斜めで、壁際の天井の高さが1.2メートルしかない部分があったとします。この部分も、洋室の面積に含めて床面積を定めます。'),
        'ウ': ('床と同じ高さの高い出窓は、床面積に算入する',
               '出窓は、その高さが1.5メートル以上で、下部が床面と同一の高さにあるものに限り、床面積に算入します（不動産登記事務取扱手続準則82条11号）。\n\n高さ1.6メートルで、下部が床面と同一の高さにある出窓は、この条件を満たします。本肢は正しい記述です。\n\n**たとえば**、居間の床から天井近くまで窓が張り出していて、足元から床と同じ高さで外に出ているような出窓は、居間の床面積に入ります。窓の下に腰かけられる台があるような出窓は、入りません。'),
        'エ': ('低い屋階は、階数に数えない',
               '天井の高さ1.5メートル未満の地階及び屋階等は、特殊階として階数に算入しません（不動産登記事務取扱手続準則81条4項）。\n\n天井の高さ1.4メートルの屋階は、この特殊階にあたります。2階建の上にあっても階数には数えないので、構造は木造2階建です。問題文の木造3階建は誤りです。\n\n**たとえば**、2階建の家の屋根裏に、天井の高さ1.4メートルの小さな部屋があっても、階数は2階建のままです。'),
        'オ': ('屋外の階段は、床面積に算入しない',
               '建物に附属する屋外の階段は、床面積に算入しません（不動産登記事務取扱手続準則82条7号）。床面積に算入するのは、階段室、エレベーター室又はこれに準ずるものです（同条6号）。\n\n問題文は、2階の廊下に通ずる屋外の階段の部分を2階の床面積に算入するとしているので、本肢は誤りです。\n\n**たとえば**、アパートの外壁に取り付けた鉄の階段は、2階の床面積に入りません。建物の中にある階段室とは違います。'),
    },
    summary=[
        ('ア', '誤', '区分建物の床面積は、壁その他の区画の内側線で囲まれた部分で定める'),
        ('イ', '正', '1室の一部が天井の高さ1.5メートル未満でも、その部分は1室の面積に算入する'),
        ('ウ', '正', '高さ1.5メートル以上で下部が床面と同一の高さにある出窓は、床面積に算入する'),
        ('エ', '誤', '天井の高さ1.5メートル未満の屋階は階数に算入しないので、木造2階建となる'),
        ('オ', '誤', '建物に附属する屋外の階段は、床面積に算入しない'),
    ],
    summary_tail='アとオは、測り方と対象を取り違えさせる出題です。エは、低い屋階を階数に数えてしまう誤りです。床面積に入るもの、入らないもの、階数に入るものを分けて整理しましょう。',
    supplements=[
        '### 補足説明（ア）：壁の中心線と内側線\n\n床面積を測る線は、建物の種類で変わります（不動産登記規則115条）。\n\n| 建物の種類 | 測る線 | 壁の厚みの扱い |\n|---|---|---|\n| 区分建物以外 | 壁その他の区画の中心線 | 壁の厚みの半分を含める |\n| 区分建物 | 壁その他の区画の内側線 | 壁の厚みを含めない |\n\n**たとえば**、同じ広さの部屋でも、一戸建ての居宅は壁の中心線で測るので広く出ます。分譲マンションの一室は内側線で測るので、その分だけ狭く出ます。',
        '### 補足説明（エ・オ）：床面積と階数に入るもの、入らないもの\n\n天井の高さや場所によって、床面積と階数に入るかが決まります（不動産登記事務取扱手続準則81条・82条）。\n\n| 対象 | 床面積 | 階数 |\n|---|---|---|\n| 天井の高さ1.5メートル未満の屋階 | 算入しない | 算入しない |\n| 1室の一部の、1.5メートル未満の部分 | 1室に含めて算入する | （階数の話ではない） |\n| 屋外の階段 | 算入しない | （階数の話ではない） |\n| 階段室、エレベーター室 | 算入する | （階数の話ではない） |\n\n**たとえば**、屋根裏の低い部屋は数えませんが、洋室の中の低い天井の一角は洋室の一部として数えます。屋外階段は数えず、建物の中の階段室は数えます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第49日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記規則115条と、不動産登記事務取扱手続準則81条4項・82条1号・6号・7号・11号は、`note-articles/laws/` 配下の原文で確認しました。',
        'エの「2階建の上の屋根裏に低い部屋がある」例は、準則81条4項の屋階等を場面に置き換えた例です。屋階の意味（屋根裏の階）は、条文からの一般的な整理です。',
        'ウで、窓の下に腰かけられる台がある出窓が算入されない例は、準則82条11号の「下部が床面と同一の高さにある」という条件を裏返した説明です。',
    ],
    phrases=['区分建物は壁の内側線で測ります', '天井の低い一角も部屋に含めます', '床と同じ高さの高い出窓は算入です', '低い屋階は階数に数えません', '屋外の階段は床面積に入りません'],
    header=dict(t1='床面積に、', t2='入る？入らない？', topic='不動産登記　建物の床面積',
                kanji='床・面・積・入・建・物'),
    poster_intro='建物の床面積と階数の定め方を、「床面積の測り方と算入」（グループA：ア・イ・ウ）と「階数と屋外階段」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='建物の床面積と階数を整理', sub='不動産登記規則 第115条と準則（毎日ドリル 第49日）',
        col_a='床面積の測り方と算入', col_b='階数と屋外階段', n_a=3,
        cards=[
            dict(h='区分建物は壁の内側線で測る',
                 ill='an isometric apartment room cut away to show a floor plan. The inner edge line of the walls is drawn as a thick green line around the room floor, and the wall thickness is shown as a pale band outside the line. A label 「内側線」 sits beside the green line. A green check mark sits beside the label.',
                 words=['内側線'], tag='区分建物は内側'),
            dict(h='1室の低い天井の一角も算入',
                 ill='an isometric room under a sloping roof, with one low corner of the room under the slope drawn with a pale dashed region that is included in the green floor outline. A label 「一室」 sits beside the room. A green check mark sits beside the label.',
                 words=['一室'], tag='その部分も床面積に'),
            dict(h='床と同じ高さの高い出窓は算入',
                 ill='an isometric living room with a tall bay window whose lower edge is at the same level as the floor, with the bay window floor area outlined in green. A label 「出窓」 sits beside the bay window. A green check mark sits beside the label.',
                 words=['出窓'], tag='床面積に算入する'),
            dict(h='低い屋階は階数に数えない',
                 ill='an isometric two-story house with a small low attic room under the roof drawn with a dotted outline and in pale gray. A label 「屋階」 sits beside the attic. A green check mark sits beside the label.',
                 words=['屋階'], tag='階数に入れない'),
            dict(h='屋外の階段は床面積に入れない',
                 ill='an isometric apartment building with an iron staircase attached to the outside wall, drawn outside the green floor outline of the building. A label 「屋外階段」 sits beside the staircase. A green check mark sits beside the label.',
                 words=['屋外階段'], tag='床面積に入れない'),
        ],
        kanji='内・側・線・区・分・建・物・一・室・出・窓・屋・階・数・外・段・床・面・積・算・入'.split('・')),
    nb_label='ア・エ・オ肢', nb_intro='ア・エ・オの補足説明に合わせた2枚です。1枚目は、床面積を測る線が建物の種類で変わることを左右の対比で示します。2枚目は、床面積や階数に入るもの、入らないものを表で整理します。',
    notebooks=[
        dict(name='壁の中心線と内側線', args=dict(
            title='床面積は、どの線で測る？', sub='建物の床面積の測り方（毎日ドリル 第49日 ア）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings. The left header is 区分建物以外 and the right header is 区分建物. Draw them in different accent colors (blue on the left and orange on the right) so they can never be confused or duplicated. Neither panel uses a cross mark.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 区分建物以外
Scene: an isometric plan view of a detached house wall, with a thick blue line running through the middle of the wall thickness.
Result badge: 壁の中心線で測る

RIGHT PANEL (orange accent):
Panel header: 区分建物
Scene: an isometric plan view of one apartment room wall, with a thick orange line running along the inner edge of the wall.
Result badge: 壁の内側線で測る""",
            callout='区分建物以外の建物は、壁その他の区画の中心線で囲まれた部分で床面積を定めます。\n区分建物は、壁その他の区画の内側線で囲まれた部分で定めます。',
            footer='不動産登記規則115条',
            kanji='区・分・建・物・壁・中・心・線・内・側・以・外・測'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (区分建物以外 on the left and 区分建物 on the right) in different accent colors, ')),
        dict(name='床面積と階数に入るもの、入らないもの', args=dict(
            title='入る？入らない？', sub='床面積と階数の数え方（毎日ドリル 第49日 エ・オ）',
            req='a table diagram',
            layout="""--- TABLE ---
Render as a clean flat-design table in the upper half, with four rows and three columns, and a small isometric icon at the left of each row.
Column headers: 対象 | 床面積 | 階数
Row 1 (blue accent), icon: a small attic room under a roof. Cells: 天井の高さ1.5メートル未満の屋階 | 算入しない | 算入しない
Row 2 (green accent), icon: a sloping ceiling room. Cells: 1室の一部の、低い天井の部分 | 1室に含めて算入する | 階数の話ではない
Row 3 (orange accent), icon: an iron staircase on an outside wall. Cells: 屋外の階段 | 算入しない | 階数の話ではない
Row 4 (gray accent), icon: a stairwell inside a building. Cells: 階段室、エレベーター室 | 算入する | 階数の話ではない
Use exactly these strings, and no others, for the table text. Cells with 算入しない are drawn in orange text and cells with 算入する are drawn in green text, so they can never be confused or duplicated.""",
            callout='天井の高さ1.5メートル未満の屋階は、床面積にも階数にも数えません。\n屋外の階段は床面積に入りませんが、建物の中の階段室は入ります。',
            footer='不動産登記事務取扱手続準則81条・82条',
            kanji='対・象・床・面・積・階・数・屋・天・井・算・入・外・段・室'.split('・'), what='table',
            check='confirm the cells 算入しない and 算入する are different strings in different colors (orange and green), ')),
    ],
)
