D = dict(
    catch='床面積に入るもの、入らないもの',
    intro='建物の床面積の測り方を問う問題です（不動産登記規則115条、不動産登記事務取扱手続準則82条）。床面積は、ふつうの建物は壁の中心線で、区分建物は壁の内側の線で測ります。そのうえで、屋根裏、吹抜、出窓など、床面積に入れるかどうか迷う部分について、準則に細かい決まりがあります。\n\nこの記事では、天井が低い部屋、ダストシュート、吹抜、出窓、区分建物の測り方を、具体的な場面で確かめていきましょう。',
    sections={
        'ア': ('天井が低い部分があっても、1室なら全体を床面積に入れる',
               '天井の高さが1.5メートル未満の地階と屋階（特殊階）は、床面積に算入しません。ただし、1室の一部だけが天井の高さ1.5メートル未満であっても、その部分は、当該1室の面積に算入します（不動産登記事務取扱手続準則82条1号）。\n\n問題文は「天井の高さが1.5メートル未満の部分を除いて算定する」としているので、本肢は誤りです。ただし書を見落とさないようにしましょう。\n\n**たとえば**、屋根裏の1室で、勾配の関係で壁際だけ天井が1.5メートルに満たなくても、その部屋の床面積は、低い部分も含めて数えます。'),
        'イ': ('建物の内部のダストシュートは、床面積に入れる',
               '建物の内部に煙突又はダストシュートがある場合は、その部分は各階の床面積に算入します。その一部が外側に及んでいるものも含みます。外側にあるときは算入しません（不動産登記事務取扱手続準則82条10号）。\n\n本肢は正しいといえます。一部が外側に出ていても、内部にあるものとして扱われます。\n\n**たとえば**、建物の中を上下に通るダストシュートの一部が、外壁から少し外に出ていても、各階の床面積に含めます。'),
        'ウ': ('吹抜の部分は、上の階の床面積に入れない',
               '建物の一部が上階まで吹抜になっている場合、その吹抜の部分は、上階の床面積に算入しません（不動産登記事務取扱手続準則82条8号）。\n\n本肢は正しいといえます。吹抜の下の部分は、下の階の床面積には入ります。\n\n**たとえば**、1階の玄関ホールが2階まで吹き抜けになっている家では、2階には、その吹抜の上に床がありません。そのため、2階の床面積には入れません。'),
        'エ': ('出窓は、高さと床との位置の両方がそろったものだけ入れる',
               '出窓を床面積に算入するのは、その高さが1.5メートル以上で、かつ、その下部が床面と同一の高さにあるものに限られます（不動産登記事務取扱手続準則82条11号）。\n\n問題文の出窓は、高さが1.6メートルあるものの、下部が床面から0.4メートル高い位置にあります。床面と同一の高さではないので、算入しません。本肢は誤りです。\n\n**たとえば**、床から少し上に張り出した出窓は、高さが十分あっても、下が床と同じ高さでなければ、床面積には入りません。'),
        'オ': ('区分建物は、壁の内側線で測る',
               '建物の床面積は、各階ごとに壁その他の区画の中心線で囲まれた部分の水平投影面積により定めます。ただし、区分建物は、壁その他の区画の内側線で囲まれた部分によります（不動産登記規則115条）。1平方メートルの100分の1未満の端数は、切り捨てます。\n\n問題文は、区分建物の専有部分も中心線で測るとしているので、本肢は誤りです。端数の切捨ては正しい点です。\n\n**たとえば**、マンションの一室は、壁の厚みの半分を含めずに、部屋の内側の線で測ります。ふつうの一戸建ては、壁の中心線で測ります。'),
    },
    summary=[
        ('ア', '誤', '1室の一部が天井1.5メートル未満でも、その部分も当該1室の面積に算入する'),
        ('イ', '正', '建物の内部のダストシュートは、一部が外側に及んでいても、各階の床面積に算入する'),
        ('ウ', '正', '吹抜の部分は、上階の床面積に算入しない'),
        ('エ', '誤', '出窓は、高さ1.5メートル以上で、下部が床面と同一の高さのものだけ算入する'),
        ('オ', '誤', '区分建物の専有部分は、壁その他の区画の内側線で測る'),
    ],
    summary_tail='アは「ただし書」、エは「二つの条件の両方」、オは「かっこ書き」を見落としやすい出題でした。床面積は、例外やかっこ書きの確認が決め手です。',
    supplements=[
        '### 補足説明（ア）：天井の高さ1.5メートルの決まり\n\n天井の高さが1.5メートル未満の部分の扱いは、屋階や地階の「階」としての扱いと、1室の中の部分の扱いで分かれます（準則82条1号）。\n\n- 天井の高さが1.5メートル未満の地階・屋階（特殊階）：床面積に算入しない。\n- ただし、1室の一部だけが1.5メートル未満：その部分も、当該1室の面積に算入する。\n\n**たとえば**、屋根裏の部屋のうち、壁際の勾配のきつい部分だけが1.5メートル未満でも、その部屋は一つのまとまりとして、全体を床面積に数えます。',
        '### 補足説明（エ）：出窓は二つの条件が両方必要\n\n出窓を床面積に入れるには、次の二つの条件を、どちらも満たす必要があります（準則82条11号）。\n\n- 高さが1.5メートル以上であること。\n- 下部が床面と同一の高さにあること。\n\n**たとえば**、高さ1.6メートルの出窓でも、下が床から0.4メートル高い位置なら、二つ目の条件を満たさないので、床面積には入りません。逆に、床と同じ高さまで下がっていても、高さが1.5メートルに足りなければ、入りません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第63日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記規則115条、不動産登記事務取扱手続準則82条1号・8号・10号・11号は、`note-articles/laws/` 配下の原文で確認しました。',
        '具体例（屋根裏の1室、玄関ホールの吹抜、出窓の高さなど）は、条文の文言をかみ砕いた一般的な説明です。',
        'ウで「吹抜の下の部分は、下の階の床面積に入る」と書いたのは、準則82条8号が「上階の床面積に算入しない」とだけ定めていることからの一般的な整理です。',
    ],
    phrases=['1室の一部が低くても、全体を数えます', 'ダストシュートは、建物の内部なら入れます', '吹抜の部分は、上の階に入れません', '出窓は、高さと位置の両方が必要です', '区分建物は、壁の内側で測ります'],
    header=dict(t1='床面積に入る？', t2='入らない？', topic='不動産登記法　建物の床面積',
                kanji='登・記・毎・建・物・床・面・積'),
    poster_intro='建物の床面積を、「入る部分、入らない部分」（グループA：ア・イ・ウ）と「出窓と測り方」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='建物の床面積を整理', sub='不動産登記規則 第115条と準則 第82条（毎日ドリル 第63日）',
        col_a='入る部分、入らない部分', col_b='出窓と測り方', n_a=3,
        cards=[
            dict(h='一室の一部が低くても全体を入れる',
                 ill='an attic room with a sloped ceiling, the entire floor of the room highlighted with a green glow, including the low corner near the wall, which has a small ruler icon beside it. A green check mark sits beside the room.',
                 words=[], tag='一室は全体'),
            dict(h='内部のダストシュートは入れる',
                 ill='a cutaway of a building with a vertical chute running through it, a small part of the chute sticking out slightly through the outer wall. The whole chute is highlighted with a green glow labeled 「内部」. A green check mark sits beside the chute.',
                 words=['内部'], tag='各階に算入'),
            dict(h='吹抜は上階に入れない',
                 ill='a two-story building in cross-section, the entry hall open through both floors. The open space on the upper floor is drawn as an empty square with a dotted outline. The lower floor of the hall is filled with a green tint. A green check mark sits beside the empty square.',
                 words=[], tag='上階は不算入'),
            dict(h='出窓は高さと位置の両方がそろえば入る',
                 ill='a bay window protruding from a wall, with a vertical ruler beside it labeled 「一点五メートル」 and a small level marker where the window bottom meets the floor. A green check mark sits beside the level marker.',
                 words=['一点五メートル'], tag='二条件の両方'),
            dict(h='区分建物は壁の内側線で測る',
                 ill='a top view of an apartment room, with a dotted line drawn on the inner face of the walls labeled 「内側線」. A green check mark sits beside the dotted line.',
                 words=['内側線'], tag='内法で測る'),
        ],
        kanji='内・部・吹・抜・出・窓・区・分・側・線・法'.split('・')),
    nb_label='ア・エ肢', nb_intro='ア・エの補足説明に合わせた2枚です。1枚目は、天井の低い部分の扱いを左右の対比で示します。2枚目は、出窓の二つの条件を示します。',
    notebooks=[
        dict(name='天井が低い部分の扱い', args=dict(
            title='天井が低いと、どうなる？', sub='天井の高さ一点五メートル未満の扱い（毎日ドリル 第63日 ア）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two sides must show OPPOSITE marks, not the same mark. The left side shows a red cross; the right side shows a green check mark. The two panel headers are different strings: 「地階か屋階の全体が低い」 on the left and 「一室の一部だけが低い」 on the right; draw them in different accent colors (gray and green).

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (gray accent):
Panel header: 地階か屋階の全体が低い
Scene: an isometric scene of an attic floor whose whole ceiling is low, drawn as a flat, squat box.
Result badge with a red cross: 床面積に算入しない

RIGHT PANEL (green accent):
Panel header: 一室の一部だけが低い
Scene: an isometric scene of one attic room with a sloped ceiling, only the corner by the wall being low, the whole floor of the room highlighted with a green tint.
Result badge with a green check mark: 低い部分も算入する""",
            callout='天井の高さが一点五メートル未満の地階や屋階（特殊階）は、床面積に算入しません。\nただし、一室の一部だけが一点五メートル未満のときは、その部分も当該一室の面積に算入します。',
            footer='不動産登記事務取扱手続準則八十二条一号',
            kanji='地・階・屋・天・井・低・床・面・積・算・入・部・分'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (地階か屋階の全体が低い on the left and 一室の一部だけが低い on the right), that the left panel shows a red cross and the right panel shows a green check mark, ')),
        dict(name='出窓が床面積に入る条件', args=dict(
            title='出窓は、いつ床面積に入る？', sub='出窓の算入の条件（毎日ドリル 第63日 エ）',
            req='a checklist diagram',
            layout="""--- CHECKLIST ---
Render as a clean flat-design vertical layout in two blocks.
Block 1 (blue accent), block header: 次の二つを両方満たす出窓だけ. Below it, two checklist rows stacked vertically, each with an empty box that carries a green check mark, with these exact labels: 高さが一点五メートル以上 | 下部が床面と同一の高さ
Block 2 (orange accent), block header: 一つでも欠けると算入しない. Below it, two small side-by-side panels:
Panel left, label: 高さは足りていても 下部が床面より高い. A red cross.
Panel right, label: 下部が床面と同じでも 高さが足りない. A red cross.
Use exactly these strings, and no others.""",
            callout='出窓は、高さが一点五メートル以上で、かつ、下部が床面と同一の高さにあるものに限り、床面積に算入します。\nどちらか一方だけでは、算入しません。',
            footer='不動産登記事務取扱手続準則八十二条十一号',
            kanji='出・窓・床・面・積・高・下・部・同・一・両・方・欠・算・入'.split('・'), what='blocks',
            check='confirm Block 1 has exactly two checklist rows, each with a green check mark, and Block 2 has exactly two panels, each with a red cross, ')),
    ],
)
