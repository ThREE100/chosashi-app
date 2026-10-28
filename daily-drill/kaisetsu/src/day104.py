def kj(*texts, n=20):
    out = []
    for t in texts:
        for c in t:
            if '一' <= c <= '鿿' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='代理権は死亡で消えず、取下げは完了前',
    intro='登記の申請の手続について、取下げができる時期、原本の還付、代理権の不消滅、申請の却下を問う問題です（不動産登記法17条、不動産登記規則38条・39条・55条）。\n\nこの記事では、申請したあとにできること、できないことを、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('申請の取下げは、登記が完了するまで',
               '申請の取下げは、登記完了後は、することができません（不動産登記規則39条2項）。\n\n問題文は、登記が完了した後でも、登記完了証の交付を受けるまでは取り下げられるとしているので、本肢は誤りです。登記完了証の交付の前か後かは、関係がありません。\n\n**たとえば**、土地家屋調査士のAさんが分筆の登記を申請し、登記官がその登記を完了したなら、登記完了証をまだ受け取っていなくても、もう取り下げることはできません。'),
        'イ': ('施工会社の印鑑証明書は、原本の還付を請求できる',
               '書面申請をした申請人は、申請書の添付書面の原本の還付を請求できます（不動産登記規則55条1項）。\n\nただし、申請書や委任状に押印した申請人の印鑑に関する証明書、同意や承諾を証する書面に押印した人の印鑑に関する証明書、その申請のためにのみ作成された委任状その他の書面は、この限りではありません。\n\n施工会社Bの印鑑に関する証明書は、これらに当たらないので、原本の還付を請求できます。本肢は正しいといえます。\n\n**たとえば**、新築した家の所有権を示すために、工務店が作った工事完了引渡証明書と、その工務店の印鑑証明書を添えて申請したとします。工務店の印鑑証明書は、申請人のAさんが押印したものではないので、登記のあと、原本を返してほしいと請求できます。'),
        'ウ': ('登記の申請の代理権は、本人が死亡しても消えない',
               '登記の申請をする人の委任による代理人の権限は、本人の死亡によっては消滅しません（不動産登記法17条1号）。民法では、本人が死亡すると代理権が消滅するのが原則ですが（民法111条1項1号）、登記の申請では特別の扱いです。\n\n問題文は、Aが死亡するとBの代理権は消滅し、相続人から改めて委任を受けなければ申請できないとしているので、本肢は誤りです。\n\n**たとえば**、Aさんが調査士のBさんに地目の変更の登記を頼んだあと、申請の前にAさんが亡くなったとします。Bさんは、Aさんの相続人から改めて委任を受けなくても、申請できます。'),
        'エ': ('却下の決定書は代理人に交付すれば足り、添付書面は還付される',
               '登記官は、申請を却下するときは、決定書を作成して、申請人ごとに交付します。ただし、代理人によって申請がされた場合は、代理人に交付すれば足ります（不動産登記規則38条1項）。\n\nまた、書面申請を却下したときは、添付書面を還付します。ただし、偽造された書面その他の不正な登記の申請のために用いられた疑いがある書面は、除かれます（同条3項）。本肢は正しいといえます。\n\n**たとえば**、調査士のAさんが、依頼者Bさんの代理人として書面で申請した分筆の登記が却下された場合、決定書はAさんに渡せば足ります。添付した書類は、疑いのあるものを除いて、返してもらえます。'),
        'オ': ('戸籍の原本の還付は、相続関係説明図で足りる取扱いがある',
               '原本の還付を請求する申請人は、原本と相違ない旨を記載した謄本を提出しなければなりません（不動産登記規則55条2項）。\n\nただし、相続を証する戸籍謄本などの原本の還付を請求するときは、相続関係説明図を提出すれば、その謄本を別に作って提出しなくてよいという取扱いがあります。問題文は、相続関係説明図を提出しても謄本を提出しなければならないとしているので、本肢は誤りです。\n\n**たとえば**、亡くなった表題部所有者の相続人Bさんが、何通もの戸籍謄本を添えて申請する場合です。全部の謄本を作る代わりに、相続関係説明図を出せば足ります。'),
    },
    summary=[
        ('ア', '誤', '申請の取下げは、登記完了後はできない（登記完了証の交付の前後は関係がない）'),
        ('イ', '正', '施工会社の印鑑証明書は、規則55条1項ただし書に当たらず、原本の還付を請求できる'),
        ('ウ', '誤', '登記の申請の委任による代理権は、本人の死亡によっては消滅しない'),
        ('エ', '正', '却下の決定書は代理人に交付すれば足り、添付書面は（疑いのあるものを除き）還付される'),
        ('オ', '誤', '相続関係説明図を提出すれば、戸籍の原本の還付に謄本の提出は要らない取扱いがある'),
    ],
    summary_tail='アは「取下げの終わり」、ウは「代理権の消滅」、オは「謄本の要否」をすり替えた出題です。登記の申請の手続には、民法の原則と違う特別な扱いがあることに注意しましょう。',
    supplements=[
        '### 補足説明（ア）：取り下げられるのは、いつまで？\n\n申請の取下げができる時期は、登記完了の前後で決まります（不動産登記規則39条2項）。\n\n- 申請したとき：取下げができる。\n- 登記が完了する前：取下げができる。\n- 登記が完了した後：取下げができない。\n\n登記完了証を受け取ったかどうかは、取下げができるかどうかに関係しません。\n\n**たとえば**、申請の翌日に、依頼者が「やはり取りやめたい」と言ってきたとしても、すでに登記が完了していたなら、取り下げることはできません。',
        '### 補足説明（ウ）：民法と登記法で、代理権の扱いが違う\n\n本人が死亡したときの代理権の扱いは、民法と登記法で違います。\n\n- 民法の原則：本人の死亡で代理権は消滅する（民法111条1項1号）。\n- 登記の申請：委任による代理人の権限は、本人の死亡によっては消滅しない（不動産登記法17条1号）。\n\n**たとえば**、依頼者が申請の前に亡くなっても、頼まれた調査士は、そのまま申請を進めることができます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第104日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法17条1号、不動産登記規則38条、39条2項、55条1項・2項、不動産登記令16条2項・18条2項・19条2項、民法111条1項1号は、`note-articles/laws/` 配下の原文で確認しました。',
        'イの「施工会社の印鑑証明書は、ただし書に挙げられたものに当たらない」は、55条1項ただし書の列挙の範囲からの整理です。オの相続関係説明図による取扱いは、条文に明記がない登記実務の取扱いで、原文（通達）は未確認です。',
        '具体例の人物と場面は、理解のために設けた架空の例です。条文にない事実は断定していません。',
    ],
    phrases=['登記が完了したら取り下げられません', '施工会社の印鑑証明書は原本を返してもらえます', '代理権は本人が死亡しても消えません', '却下の決定書は代理人に渡せば足ります', '戸籍の還付は相続関係説明図で足ります'],
    header=dict(t1='申請の手続、', t2='何ができる？', topic='不動産登記法　申請の取下げと却下', kanji=''),
    poster_intro='登記の申請の手続を、「取下げ・原本還付・代理権」（グループA：ア・イ・ウ）と「却下と謄本」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='登記の申請の手続を整理', sub='不動産登記法 第17条と不動産登記規則 第38条と第39条と第55条（毎日ドリル 第104日）',
        col_a='取下げと還付と代理権', col_b='却下と謄本', n_a=3,
        cards=[
            dict(h='登記完了後は取り下げられない',
                 ill='a horizontal timeline with a flag labeled 「登記完了」. The part of the timeline before the flag is drawn in green with a small withdrawal-form icon; the part after the flag is drawn in gray with the same icon faded. A green check mark sits beside the flag.',
                 words=['登記完了'], tag='完了証の交付は無関係'),
            dict(h='施工会社の印鑑証明書は原本還付できる',
                 ill='an applicant figure receiving back a certificate sheet with a round seal, with a thin returning arrow. A tag on the certificate is labeled 「印鑑証明書」. A green check mark sits beside the certificate.',
                 words=['印鑑証明書'], tag='原本の還付を請求'),
            dict(h='代理権は本人が死亡しても消えない',
                 ill='a surveyor figure holding a document labeled 「委任状」 and a form, with a faded gray portrait frame of the client behind. A green check mark sits beside the surveyor.',
                 words=['委任状'], tag='改めての委任は不要'),
            dict(h='却下の決定書は代理人に交付すれば足りる',
                 ill='a registry clerk figure handing a sheet labeled 「決定書」 to a surveyor figure, with a folder of returned documents on the counter. A green check mark sits beside the sheet.',
                 words=['決定書'], tag='添付書面は還付'),
            dict(h='戸籍の還付は相続関係説明図で足りる',
                 ill='a stack of family-register documents being returned to an heir figure, with a family-tree diagram sheet labeled 「相続関係説明図」 on the counter. A green check mark sits beside the diagram sheet.',
                 words=['相続関係説明図'], tag='謄本の提出を省略'),
        ],
        kanji=[]),
    nb_label='ア・ウ肢', nb_intro='ア・ウの補足説明に合わせた2枚です。1枚目は、取り下げられる時期を時間の流れで示します。2枚目は、民法と登記法で代理権の扱いが違うことを左右の対比で示します。',
    notebooks=[
        dict(name='取り下げられるのは、いつまで', args=dict(
            title='申請を取り下げられる時期', sub='登記完了の前と後（毎日ドリル 第104日 ア）',
            req='a timeline diagram',
            layout="""--- TIMELINE ---
Render as a clean flat-design horizontal timeline with a common axis running left to right and three flags. Use exactly these strings, and no others, for the labels. Do not use any check mark or cross mark.
Flag 1 (left): 申請. Flag 2 (middle): 登記完了. Flag 3 (right): 登記完了証の交付.
Between flag 1 and flag 2, draw the axis in green with a bracket labeled 取り下げられる.
After flag 2, draw the axis in gray with a bracket labeled 取り下げられない. The bracket after flag 2 must cover flag 3 as well, to show that the issue of the completion certificate does not change the result.""",
            callout='申請の取下げができるのは、登記が完了するまでです。\n登記完了証の交付を受ける前でも、登記が完了したあとは、取り下げられません。',
            footer='不動産登記規則39条2項', kanji=[], what='timeline',
            check='confirm there are exactly three flags and two brackets with the given strings, and that the gray bracket covers the third flag, ')),
        dict(name='民法と登記法の代理権の違い', args=dict(
            title='本人が死亡したら代理権は？', sub='民法と不動産登記法（毎日ドリル 第104日 ウ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two sides must show OPPOSITE marks, not the same mark. The left side shows a red cross; the right side shows a green check mark. The two panel headers are different strings: 「民法の原則」 on the left and 「登記の申請」 on the right; draw them in different accent colors (blue on the left, orange on the right) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 民法の原則
Scene: an agent figure holding a power-of-attorney document, with the client figure behind drawn as a faded gray portrait frame, and the document drawn torn.
Label under the scene: 本人が死亡すると代理権は消滅する
Result badge with a red cross: 代理権は消える

RIGHT PANEL (orange accent):
Panel header: 登記の申請
Scene: a surveyor figure holding a power-of-attorney document and a form, with the client figure behind drawn as a faded gray portrait frame, and the document intact.
Label under the scene: 本人が死亡しても代理権は消滅しない
Result badge with a green check mark: 代理権は消えない
Use exactly these strings, and no others, for the labels.""",
            callout='民法では、本人が死亡すると代理権は消滅するのが原則です。\n登記の申請の委任による代理人の権限は、本人が死亡しても消滅しません。',
            footer='民法111条1項1号、不動産登記法17条1号', kanji=[], what='panels',
            check='confirm the two panel headers are different strings (民法の原則 on the left and 登記の申請 on the right) and that the left panel shows a red cross while the right panel shows a green check mark, ')),
    ],
)

_p = D['poster']
_p['kanji'] = kj(_p['title'], _p['sub'], _p['col_a'], _p['col_b'], *[c['h'] + c['tag'] + ''.join(c['words']) for c in _p['cards']])
D['header']['kanji'] = '・'.join(kj(D['header']['t1'], D['header']['t2'], D['header']['topic']))
for _nb in D['notebooks']:
    _a = _nb['args']
    _a['kanji'] = kj(_a['title'], _a['sub'], _a['callout'], _a['footer'])
