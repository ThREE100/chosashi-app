def _kj(*texts, n=22):
    out = []
    for c in ''.join(texts):
        if '一' <= c <= '龥' and c not in out:
            out.append(c)
    return out[:n]


_P = dict(
    title='建物の床面積の算入を整理', sub='不動産登記規則第115条と準則第82条（毎日ドリル 第112日）',
    col_a='吹抜と出窓と柱', col_b='測る線と塔屋', n_a=3,
    cards=[
        dict(h='吹抜は、上階の床面積に入れない',
             ill='a cutaway isometric two-story house where the living room is open through both floors. On the upper floor plan, the open void area is cut out and drawn as a hole. A green check mark sits beside the upper floor plan.',
             words=[], tag='1階には算入'),
        dict(h='出窓は、高さと下部の位置が条件',
             ill='a bay window attached to a wall, sitting right at floor level, and a tall vertical ruler beside it showing it reaches above a marked line. A green check mark sits beside the bay window.',
             words=[], tag='二つそろえば算入'),
        dict(h='室内の柱は、除かずに内側線で測る',
             ill='a top-down room plan where a pillar protrudes into one corner, and a dotted measuring line runs straight along the inner wall surfaces right past the pillar as if it were not there. A green check mark sits beside the dotted line.',
             words=[], tag='柱の出っ張りは無視'),
        dict(h='専有部分は内側線、一棟は中心線',
             ill='two top-down plans side by side. The left plan is a single apartment unit with a measuring line along the inside of its walls, labeled 「内側線」. The right plan is the whole building with a measuring line through the center of its walls, labeled 「中心線」. A green check mark sits between the two plans.',
             words=['内側線', '中心線'], tag='測る線が違う'),
        dict(h='塔屋の一部が倉庫なら、塔屋の全体を算入',
             ill='a rooftop penthouse box on a flat roof with a storage crate icon in one corner, and the whole penthouse box highlighted with a green glow. A green check mark sits beside the penthouse.',
             words=[], tag='全体が算入される'),
    ],
)
_P['kanji'] = _kj(_P['title'], _P['sub'], _P['col_a'], _P['col_b'], *[c['h'] + ''.join(c['words']) + c['tag'] for c in _P['cards']])

_N1 = dict(
    title='専有部分と一棟の建物は、測る線が違う', sub='不動産登記規則115条（毎日ドリル 第112日 ウ・エ）',
    req='a side-by-side comparison',
    layout="""IMPORTANT: the two panel headers are different strings and must not be confused: 「専有部分」 on the left and 「一棟の建物」 on the right. Draw them in different accent colors (blue and orange). This image uses no check marks and no cross marks.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 専有部分
Scene: a top-down plan of one apartment room with a pillar protruding into a corner. A dotted measuring line runs along the inner wall surfaces and passes straight by the pillar.
Measuring badge: 壁の内側線で囲む

RIGHT PANEL (orange accent):
Panel header: 一棟の建物
Scene: a top-down plan of a whole apartment building with several rooms. A dotted measuring line runs through the center of the outer walls.
Measuring badge: 壁の中心線で囲む""",
    callout='区分建物の専有部分の床面積は、壁その他の区画の内側線で囲まれた部分で測ります。\n専有部分が属する一棟の建物の床面積は、原則どおり、壁その他の区画の中心線で測ります。',
    footer='不動産登記規則115条',
    what='panels',
    check='confirm the two panel headers are different strings (専有部分 on the left and 一棟の建物 on the right) and that the two measuring badges are different strings, ')
_N2 = dict(
    title='床面積に算入するもの、しないもの', sub='出窓と塔屋（毎日ドリル 第112日 イ・オ）',
    req='a comparison table',
    layout="""IMPORTANT: this is a three-row table with two columns. The two column headers 「場面」 and 「床面積」 are different strings. Draw the 「場面」 column in blue and the 「床面積」 column in green. The rows with a green check mark are counted in the floor area; the row with a red cross is not counted.

--- TABLE ---
Row 1: 出窓の高さが1.5メートル以上で、下部が床面と同じ高さ | 算入する（green check mark）
Row 2: 出窓の下部が床面より高い | 算入しない（red cross）
Row 3: 塔屋の一部が倉庫に使われている | 塔屋全体を算入する（green check mark）
Use exactly these strings, and no others.""",
    callout='出窓は、高さが1.5メートル以上で、しかも下部が床面と同じ高さにあるものだけを算入します。\n下部が床面より高い出窓は、算入しません。塔屋は、一部が倉庫などに使われていれば、塔屋の全体を算入します。',
    footer='不動産登記事務取扱手続準則82条11号',
    what='table',
    check='confirm the table has exactly three rows, that rows 1 and 3 carry green check marks and row 2 carries a red cross, ')
for _n in (_N1, _N2):
    _n['kanji'] = _kj(_n['title'], _n['sub'], _n['layout'].split('--- ')[-1], _n['callout'], _n['footer'])

D = dict(
    catch='専有部分は内側線、一棟の建物は中心線',
    intro='建物の床面積に算入するもの、しないもの、そして測り方を問う問題です（不動産登記規則115条、不動産登記事務取扱手続準則82条）。吹抜、出窓、専有部分の柱、一棟の建物、塔屋が出題されています。\n\nこの記事では、原則どおり算入するか、例外として算入しないかを、具体的な場面で確認していきましょう。この問題は、正しい肢の組合せを選ぶ形です。',
    sections={
        'ア': ('吹抜の部分は、上階の床面積に算入しない',
               '建物の一部が上階まで吹抜になっているときは、その吹抜の部分は、上階の床面積に算入しません（不動産登記事務取扱手続準則82条8号）。\n\n本肢は正しいといえます。\n\n**たとえば**、木造2階建の家で、1階の居間の一部が2階まで吹き抜けになっているとします。2階の床面積を数えるときは、その吹抜の部分を除きます。1階には床があるので、1階の床面積には入ります。'),
        'イ': ('出窓は、高さと下部の位置の両方がそろって、算入する',
               '出窓が床面積に算入されるのは、高さが1.5メートル以上のもので、その下部が床面と同じ高さにあるものに限られます（不動産登記事務取扱手続準則82条11号）。\n\n問題文は、高さが1.5メートル以上でも下部が床面より高い位置にあるものを、算入するとしています。条件の一つを欠くので、本肢は誤りです。\n\n**たとえば**、床よりも高い位置から張り出した出窓は、高さが十分にあっても、床面積には入りません。'),
        'ウ': ('専有部分の柱の出っ張りは、除かずに内側線で測る',
               '区分建物の専有部分の床面積は、壁その他の区画の内側線で囲まれた部分の水平投影面積で定めます（不動産登記規則115条）。\n\n内壁に凹凸があったり、部屋の中に柱があったりしても、出っ張りを除かずに、ないものとして測ります。出っ張った柱の部分を除くとする本肢は、誤りです。\n\n**たとえば**、マンションの一室の壁ぎわに、柱が出っ張っているとします。柱の分を削るのではなく、柱がないものとして壁の内側をまっすぐ測った面積が、専有部分の床面積です。'),
        'エ': ('専有部分は内側線、一棟の建物は中心線で測る',
               '建物の床面積は、各階ごとに壁その他の区画の中心線で囲まれた部分の水平投影面積により定めます。区分建物は、壁その他の区画の内側線で囲まれた部分で定めます（不動産登記規則115条）。\n\n内側線で測るのは区分建物（専有部分）の床面積で、その区分建物が属する一棟の建物の床面積は、原則どおり中心線で測ります。本肢は正しいといえます。\n\n**たとえば**、マンションの101号室の面積は、室内の壁の内側で測ります。一方、マンション全体の床面積は、壁の中心で測ります。'),
        'オ': ('塔屋の一部が倉庫なら、塔屋の全体を算入する',
               '屋上に出るための出入口だけの塔屋は、床面積に算入しません。しかし、塔屋の一部が倉庫などとして使われているときは、倉庫として使われている部分に限らず、塔屋の全体を床面積に算入します。\n\n問題文は、倉庫として使われている部分に限り算入するとしているので、本肢は誤りです。\n\n**たとえば**、ビルの屋上にある塔屋の一角が、倉庫として使われているとします。倉庫の部分だけでなく、塔屋の全体が床面積に入ります。'),
    },
    summary=[
        ('ア', '正', '吹抜の部分は、上階の床面積に算入しない'),
        ('イ', '誤', '出窓は、高さ1.5メートル以上で、かつ下部が床面と同じ高さにあるものに限り算入する'),
        ('ウ', '誤', '専有部分の室内の柱の出っ張りは、除かずに、ないものとして内側線で測る'),
        ('エ', '正', '専有部分は内側線、その属する一棟の建物は中心線で囲まれた部分で測る'),
        ('オ', '誤', '塔屋の一部が倉庫などに使われていれば、塔屋の全体を床面積に算入する'),
    ],
    summary_tail='イは「条件の一つ」、ウは「柱を除くか」、オは「算入する範囲」をすり替えた出題です。床面積は、原則と例外を一つずつ当てはめましょう。',
    supplements=[
        '### 補足説明（ウ・エ）：床面積を測る線の違い\n\n同じ建物でも、何の床面積かによって、測る線が違います（不動産登記規則115条）。\n\n- 区分建物の専有部分：壁その他の区画の内側線。\n- その専有部分が属する一棟の建物：壁その他の区画の中心線。\n- 専有部分の室内の柱：除かずに、ないものとして測る。\n\n**たとえば**、同じマンションでも、101号室の床面積を測るときは壁の内側、マンション全体の床面積を測るときは壁の中心を使います。そのため、各室の床面積を足しても、一棟の建物の床面積にはなりません。',
        '### 補足説明（イ・オ）：算入するもの、しないもの\n\n床面積に算入するかどうかは、例外の条件を確かめて決めます。\n\n- 出窓：高さ1.5メートル以上で、かつ下部が床面と同じ高さにあるものだけ算入する（準則82条11号）。\n- 塔屋：一部が倉庫などに使われているときは、塔屋の全体を算入する。\n\n**たとえば**、出窓の下部が床面と同じ高さなら、高さが1.5メートル以上あるときに算入します。下部が床より高い出窓は、算入しません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第112日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記規則115条、不動産登記事務取扱手続準則82条8号・11号は、`note-articles/laws/` 配下の原文で確認しました。',
        'ウの「柱の出っ張りは除かずに測る」、オの「塔屋の一部が倉庫なら塔屋の全体を算入する」は、登記実務の取扱い（先例）に基づく説明で、先例の原文は手元になく、未確認です。',
        'エの「各室の床面積を足しても一棟の建物の床面積にならない」は、115条の測り方の違いからの一般的な整理です。各肢の具体例は、条文の適用場面をイメージするための例です。',
    ],
    phrases=['吹抜は上階の床面積に入れません', '出窓は二つの条件がそろえば算入です', '専有部分の柱は除かずに測ります', '専有部分は内側線で一棟は中心線です', '塔屋は一部が倉庫なら全体を算入します'],
    header=dict(t1='床面積に入るのは、', t2='どこまで？', topic='不動産登記法　建物の床面積',
                kanji='・'.join(_kj('床面積に入るのはどこまで', '不動産登記法建物の床面積', '毎', n=8))),
    poster_intro='建物の床面積を、「吹抜と出窓と柱」（グループA：ア・イ・ウ）と「測る線と塔屋」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=_P,
    nb_label='イ・ウ・エ・オ肢', nb_intro='イ・ウ・エ・オの補足説明に合わせた2枚です。1枚目は、専有部分と一棟の建物で測る線が違うことを左右の対比で示します。2枚目は、出窓と塔屋について、算入するものとしないものを表で整理します。',
    notebooks=[
        dict(name='専有部分と一棟の建物は、測る線が違う', args=_N1),
        dict(name='床面積に算入するもの、しないもの', args=_N2),
    ],
)
