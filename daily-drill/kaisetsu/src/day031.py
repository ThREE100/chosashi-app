D = dict(
    catch='床面積に入れるか、入れないか',
    intro='建物の「床面積」を、どの線で測り、どの部分を入れるかを問う問題です（不動産登記規則115条、不動産登記事務取扱手続準則82条）。正しいものの組合せを選びます。\n\nこの記事では、区分建物の測り方、天井の低い部分、出窓、煙突、地下街の通路について、具体的な場面で確認します。',
    sections={
        'ア': ('区分建物の床面積は、壁の内側線で測る',
               '建物の床面積は、各階ごとに壁その他の区画の中心線で囲まれた部分の水平投影面積で定めます。ただし、区分建物は、壁その他の区画の内側線で囲まれた部分で定めます（不動産登記規則115条）。\n\n問題文は、区分建物の床面積を「中心線」で囲まれた部分としているので、本肢は誤りです。\n\n**たとえば**、一戸建ての居宅は壁の中心線で測りますが、マンションの一室は、壁の内側の線で測ります。壁の厚みの分だけ、数字が小さくなります。'),
        'イ': ('1室の一部が低い天井でも、その部分は床面積に入れる',
               '天井の高さ1.5メートル未満の地階及び屋階は、床面積に算入しません。ただし、1室の一部が天井の高さ1.5メートル未満であっても、その部分は、その1室の面積に算入します（準則82条1号）。\n\n本肢は正しいといえます。\n\n**たとえば**、屋根の傾きで、2階の部屋の端の天井が1.5メートルより低くなっていても、その部分を含めて部屋全体の床面積に入れます。'),
        'ウ': ('出窓は、高さと下部の位置の両方の条件を満たすときだけ',
               '出窓は、その高さが1.5メートル以上で、かつ下部が床面と同一の高さにあるものに限り、床面積に算入します（準則82条11号）。\n\n問題文の出窓は、高さは1.6メートルですが、下部が床面から40センチメートル高い位置にあります。下部が床面と同じ高さではないので、床面積には算入されず、本肢は誤りです。\n\n**たとえば**、床から腰の高さにある出窓は、背が高くても床面積に入りません。床と同じ高さから始まる、高さ1.5メートル以上の出窓だけが入ります。'),
        'エ': ('建物の内部にある煙突は、外に出ていても床面積に入れる',
               '建物の内部に煙突又はダストシュートがある場合には、その一部が外側に及んでいるものも含めて、その部分は各階の床面積に算入します（準則82条10号）。\n\n本肢は正しいといえます。\n\n**たとえば**、建物の中を通る煙突が、壁の外側に少しはみ出していても、その煙突の部分は各階の床面積に入ります。建物の完全に外側にある煙突は、入りません。'),
        'オ': ('地下街の床面積から、常時開放の通路と階段は除く',
               '地下街の建物の床面積は、壁又は柱等により区画された部分の面積で定めます。ただし、常時一般に開放されている通路及び階段の部分は除きます（準則82条4号）。\n\n問題文は、常時一般に開放されている通路の部分も含めるとしているので、本肢は誤りです。\n\n**たとえば**、地下街で、だれでも自由に通れる通路は床面積に入れず、壁や柱で区画された店舗の部分だけが床面積になります。'),
    },
    summary=[
        ('ア', '誤', '区分建物の床面積は、壁その他の区画の内側線で囲まれた部分で定める'),
        ('イ', '正', '1室の一部が天井の高さ1.5メートル未満でも、その部分は1室の面積に算入する'),
        ('ウ', '誤', '出窓は、高さ1.5メートル以上で、下部が床面と同一の高さにあるときだけ算入する'),
        ('エ', '正', '建物の内部にある煙突は、一部が外側に及んでいても各階の床面積に算入する'),
        ('オ', '誤', '地下街の床面積から、常時一般に開放されている通路と階段の部分は除く'),
    ],
    summary_tail='アは「中心線」と「内側線」、ウは「両方の条件」のうち一方の見落とし、オは「ただし書」の見落としです。床面積は、測る線と、入れる部分・入れない部分の条件を、セットで覚えましょう。',
    supplements=[
        '### 補足説明（ウ）：出窓が床面積に入るのは、2つの条件がそろうとき\n\n出窓は、次の2つの条件を両方満たすときだけ、床面積に算入されます（準則82条11号）。\n\n- 高さが1.5メートル以上であること。\n- 下部が床面と同一の高さにあること。\n\n**たとえば**、高さ1.6メートルでも、下部が床から40センチメートル上にあれば、2つ目の条件を満たさないので入りません。高さが1.2メートルで床と同じ高さから始まる出窓も、1つ目の条件を満たさないので入りません。',
        '### 補足説明（ア）：壁の中心線と内側線\n\n床面積を測る線は、建物の種類によって違います（不動産登記規則115条）。\n\n- 区分建物以外の建物：壁その他の区画の中心線で囲まれた部分。\n- 区分建物：壁その他の区画の内側線で囲まれた部分。\n\n**たとえば**、壁の厚みが20センチメートルなら、中心線で測る一戸建てに比べ、内側線で測るマンションの一室は、壁の厚みの半分にあたる10センチメートルずつ、四方が内側になります。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第31日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記規則115条は `note-articles/laws/` 配下の原文で、準則82条1号・4号・10号・11号は準則の原文で確認しました。',
        'アの補足説明の「壁の厚みの半分にあたる10センチメートルずつ」は、壁の中心線から内側線までの距離という条文の文言からの一般的な計算例で、実際の建物の寸法ではありません。',
        '各具体例（屋根の傾きで低い天井、腰の高さにある出窓、地下街の通路など）は、条文の文言を日常の場面に置き換えた説明で、個別の事例の判断ではありません。',
    ],
    phrases=['区分建物は壁の内側線で測ります', '一部が低い天井でもその部屋に含めます', '出窓は条件を二つとも満たすときだけ入ります', '建物内の煙突は床面積に入ります', '地下街の通路と階段は除きます'],
    header=dict(t1='床面積に、', t2='入る？入らない？', topic='不動産登記規則　床面積',
                kanji='床・面・積・入・毎・登・記'),
    poster_intro='建物の床面積を、「測り方と天井・出窓」（グループA：ア・イ・ウ）と「煙突と地下街」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='床面積を整理', sub='不動産登記規則115条と準則82条（毎日ドリル 第31日）',
        col_a='測り方と天井・出窓', col_b='煙突と地下街', n_a=3,
        cards=[
            dict(h='区分建物は壁の内側線で測る',
                 ill='a top-down floor plan of one apartment room with thick walls. A green dotted outline runs along the inner face of the walls and is labeled 「内側線」. A green check mark sits beside the outline.',
                 words=['内側線'], tag='内側線で測る'),
            dict(h='一部が低い天井でも部屋に含める',
                 ill='a cross-section of a room under a sloping roof. The lower edge of the ceiling on the left is marked with a small height marker, and the whole floor of the room, including the low edge part, is highlighted in green. A label 「1室」 sits under the floor. A green check mark sits beside the room.',
                 words=['1室'], tag='その部分も算入'),
            dict(h='出窓は高さと下部の位置の両方が条件',
                 ill='two isometric bay windows side by side. The left one starts at floor level and is tall, drawn with a green check mark. The right one starts high above the floor, drawn faded in gray with no mark. A label 「床と同じ高さ」 sits under the left window.',
                 words=['床と同じ高さ'], tag='両方の条件が必要'),
            dict(h='建物内の煙突は床面積に入る',
                 ill='a top-down floor plan of a room with a square chimney in one corner, and a corner of the chimney slightly sticking out of the outer wall. The whole chimney square is highlighted in green. A label 「煙突」 sits beside it. A green check mark sits beside the chimney.',
                 words=['煙突'], tag='外にはみ出しても算入'),
            dict(h='地下街の通路と階段は除く',
                 ill='a top-down floor plan of an underground shopping street. Shop rooms on both sides are highlighted in green and the open walkway in the middle is drawn in gray with a label 「通路」. A green check mark sits beside the shops.',
                 words=['通路'], tag='開放された通路は除く'),
        ],
        kanji='床・面・積・内・側・線・室・出・窓・煙・突・通・路'.split('・')),
    nb_label='ウ・ア肢', nb_intro='ウとアの補足説明に合わせた2枚です。1枚目は、出窓が床面積に入る2つの条件を確認します。2枚目は、床面積を測る線の違いを、区分建物とそれ以外の建物の対比で示します。',
    notebooks=[
        dict(name='出窓が床面積に入る2つの条件', args=dict(
            title='出窓が床面積に入る条件', sub='準則82条11号（毎日ドリル 第31日 ウ）',
            req='a checklist diagram',
            layout="""--- CHECKLIST ---
Render as a clean flat-design vertical flow in two blocks.
Block 1 (blue accent), block header: 次の二つをどちらも満たすとき. Below it, two checklist rows stacked vertically, each with an empty box that carries a green check mark, with these exact labels: 高さが1.5メートル以上 | 下部が床面と同一の高さ
Between the two blocks, draw a small downward arrow with no text.
Block 2 (green accent), block header: 結論. A single row with an isometric bay window starting at floor level and the label: 床面積に算入する
Use exactly these strings, and no others.""",
            callout='出窓は、高さ1.5メートル以上で、かつ下部が床面と同一の高さにあるものだけが、床面積に入ります。\n高さが足りても、下部が床から高い位置にある出窓は入りません。',
            footer='不動産登記事務取扱手続準則82条11号',
            kanji='出・窓・高・床・面・積・算・入・条・件'.split('・'), what='blocks',
            check='confirm there are exactly two checklist rows in Block 1, each with a green check mark, ')),
        dict(name='床面積を測る線の違い', args=dict(
            title='壁の中心線と内側線', sub='不動産登記規則115条（毎日ドリル 第31日 ア）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: neither panel uses a cross mark; no cross mark anywhere. The two panel headers are different strings: 「区分建物以外」 on the left and 「区分建物」 on the right; draw them in different accent colors (blue and green).

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 区分建物以外
Scene: a top-down floor plan of a detached house with thick walls; a blue dotted line runs along the middle of the walls.
Result badge with a green check mark: 壁の中心線

RIGHT PANEL (green accent):
Panel header: 区分建物
Scene: a top-down floor plan of one apartment room with thick walls; a green dotted line runs along the inner face of the walls.
Result badge with a green check mark: 壁の内側線""",
            callout='区分建物以外の建物は壁の中心線、区分建物は壁の内側線で囲まれた部分で、床面積を測ります。\n区分建物のほうが、壁の厚みの分だけ小さくなります。',
            footer='不動産登記規則115条',
            kanji='区・分・建・物・壁・中・心・線・内・側・床・面・積'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (区分建物以外 on the left and 区分建物 on the right) in different accent colors and that no cross mark appears anywhere, ')),
    ],
)
