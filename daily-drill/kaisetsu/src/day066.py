def K(*texts, n=20):
    out = []
    for t in texts:
        for c in t:
            if '一' <= c <= '龥' and c not in out and c not in '一二三四五六七八九十':
                out.append(c)
    return out[:n]


_H = dict(t1='土地の図面は、', t2='何枚つくる？', topic='不動産登記法　土地の表題登記')
_PT = '土地の表題登記を整理'
_PS = '不動産登記規則と不動産登記法（毎日ドリル 第66日）'

_cards = [
    dict(h='図面は一筆の土地ごとに作る',
         ill='two neighboring isometric land plots, each with its own separate drawing sheet beside it. The left sheet is labeled 「甲土地」 and the right sheet is labeled 「乙土地」. A green check mark sits beside each sheet.',
         words=['甲土地', '乙土地'], tag='一筆に一枚'),
    dict(h='署名用電子証明書で住所の証明に代える',
         ill='a laptop on a desk with a small certificate card beside it, labeled 「署名用電子証明書」. A green check mark sits beside the card.',
         words=['署名用電子証明書'], tag='電子申請の特例'),
    dict(h='余白に土地所在図を描ける',
         ill='a large drawing sheet with a small drawing in the empty margin at the lower right. The small drawing is labeled 「土地所在図」. A green check mark sits beside the margin drawing.',
         words=['土地所在図'], tag='書面申請の余白'),
    dict(h='縮尺が同じなら図面を兼ねられる',
         ill='one drawing sheet shown with two labels attached on the same sheet, 「土地所在図」 and 「地積測量図」, and a ruler beside it showing equal scales. A green check mark sits beside the sheet.',
         words=['土地所在図', '地積測量図'], tag='縮尺が同一'),
    dict(h='買った土地は一月以内に表題登記',
         ill='a buyer figure holding a form beside a land plot with a small calendar page labeled 「一月以内」. A green check mark sits beside the buyer.',
         words=['一月以内'], tag='取得の日から'),
]

_nb1_layout = """--- LAYOUT ---
Render as a clean flat-design diagram in two blocks stacked vertically.
Block 1 (blue accent), block header: 甲土地と乙土地を同時に申請する場合. Scene: two neighboring land plots with a dotted boundary line between them.
Block 2 (green accent), block header: 地積測量図. Scene: two separate drawing sheets side by side, the left labeled 甲土地の図面 and the right labeled 乙土地の図面. Below the sheets, a small label: 一筆の土地ごとに作る
Between the two blocks, a small downward arrow with no text.
Use exactly these strings, and no others."""

_nb2_layout = """IMPORTANT: this is a two-condition checklist. The left row shows a green check mark; the right row shows a red cross. The two row headers are different strings: 「縮尺が同じ」 and 「縮尺が違う」; draw them in different accent colors (blue and orange) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 縮尺が同じ
Scene: one drawing sheet with a ruler showing the same scale as the area map, and the label 土地の所在を明確に表示できる.
Result badge with a green check mark: 土地所在図を兼ねられる

RIGHT PANEL (orange accent):
Panel header: 縮尺が違う
Scene: one drawing sheet with a ruler showing a different scale from the area map.
Result badge with a red cross: 兼ねられない"""

D = dict(
    catch='地積測量図は一筆の土地ごとに作る',
    intro='土地の表題登記について、図面の作り方、電子申請での住所の証明、申請義務を問う問題です（不動産登記規則44条・75条、不動産登記事務取扱手続準則51条、不動産登記法36条）。\n\nこの記事では、地積測量図を作る単位と、地積測量図が土地所在図を兼ねる条件を、具体的な場面で確認します。この問題は、誤っているものを選ぶ形式です。',
    sections={
        'ア': ('地積測量図は、一筆の土地ごとに作る',
               '土地所在図と地積測量図は、一筆の土地ごとに作成しなければなりません（不動産登記規則75条1項）。\n\n同時に申請する場合でも、2筆の土地をまとめて1枚の図面にすることはできません。本肢は誤りです。\n\n**たとえば**、隣り合う甲土地と乙土地を同時に表題登記する場合でも、地積測量図は、甲土地の図面と乙土地の図面を別々に2枚作ります。'),
        'イ': ('署名用電子証明書を提供すれば、住所の証明に代えられる',
               '電子申請の申請人が、署名用電子証明書（地方公共団体情報システム機構の認証業務に関する法律に基づき作成されたもの）を提供したときは、その提供をもって、現在の住所を証する情報の提供に代えることができます（不動産登記規則44条1項、43条1項1号）。\n\n本肢は正しいといえます。\n\n**たとえば**、オンラインで土地の表題登記を申請する人が、署名用電子証明書を提供したとします。この場合、その人の現在の住所を証する情報を、別に提供しなくて済みます。'),
        'ウ': ('用紙に余白があれば、その余白に土地所在図を作れる',
               '書面申請で、日本産業規格B列4番の用紙により地積測量図を作成する場合、用紙に余白があるときは、便宜、その余白に土地所在図を作成することができます。この場合は、図面の標記に「土地所在図」と追記します（不動産登記事務取扱手続準則51条3項）。\n\n本肢は正しいといえます。\n\n**たとえば**、書面で申請する人が、地積測量図の用紙の余白に土地所在図を描いたとします。その図面の標記には、「土地所在図」と書き足します。'),
        'エ': ('縮尺が違うと、土地所在図を兼ねられない',
               '書面の地積測量図が土地所在図を兼ねるには、縮尺がその土地について作成すべき土地所在図の縮尺と同一であって、土地の所在を明確に表示できることが必要です（不動産登記事務取扱手続準則51条4項）。\n\n問題文は、縮尺が異なっても兼ねられるとしているので、本肢は誤りです。\n\n**たとえば**、近くの地図が500分の1だとします。この場合、土地所在図も同じ縮尺で作ります。地積測量図を別の縮尺で作ったときは、土地の所在がはっきり描けていても、土地所在図を兼ねることはできません。'),
        'オ': ('買い受けた土地は、取得の日から一月以内に申請する',
               '新たに生じた土地又は表題登記がない土地の所有権を取得した者は、その所有権の取得の日から一月以内に、表題登記を申請しなければなりません（不動産登記法36条）。\n\n本肢は正しいといえます。\n\n**たとえば**、AがBから、表題登記がない土地を買い受けたとします。Aは、買い受けた日から一月以内に、その土地の表題登記を申請します。'),
    },
    summary=[
        ('ア', '誤', '土地所在図と地積測量図は、一筆の土地ごとに作る。まとめて1枚にはできない'),
        ('イ', '正', '電子申請では、署名用電子証明書の提供で、住所を証する情報の提供に代えられる'),
        ('ウ', '正', '書面申請では、地積測量図の用紙の余白に土地所在図を作れる'),
        ('エ', '誤', '地積測量図が土地所在図を兼ねるには、縮尺が土地所在図と同一であることが必要'),
        ('オ', '正', '表題登記がない土地を取得した人は、取得の日から一月以内に表題登記を申請する'),
    ],
    summary_tail='アは「一筆ごと」を、エは「縮尺が同一」という条件を外した出題です。図面は一筆ごとに作ること、兼ねるには縮尺が同じであることを押さえましょう。',
    supplements=[
        '### 補足説明（ア）：図面を作る単位\n\n土地所在図と地積測量図は、一筆の土地ごとに作ります（不動産登記規則75条1項）。\n\n- 表題登記を同時に申請する2筆の土地：図面は2枚。\n- 分筆の登記を申請するとき：分筆後の土地の地積測量図は、分筆前の土地ごとに作成する（同条2項）。\n\n**たとえば**、1つの土地を2つに分筆するときは、分筆前の1筆の土地について、分筆後の2つの区画を描いた地積測量図を1枚作ります。分筆後の2筆について、図面を2枚作るのではありません。',
        '### 補足説明（エ）：地積測量図が土地所在図を兼ねる条件\n\n書面の地積測量図が、土地所在図を兼ねるための条件は、次の2つです（不動産登記事務取扱手続準則51条4項）。\n\n| 条件 | 内容 |\n|---|---|\n| 縮尺 | 地積測量図の縮尺が、土地所在図の縮尺と同一であること |\n| 表示 | 土地の所在を明確に表示することができること |\n\n土地所在図の縮尺は、近傍類似の土地の地図と同一の縮尺で作ります（不動産登記規則76条2項）。\n\n**たとえば**、地積測量図の縮尺が土地所在図と同じでも、土地の所在がはっきり描けていなければ、兼ねることはできません。逆に、所在がはっきり描けていても、縮尺が違えば兼ねることはできません。2つの条件が、ともに必要です。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第66日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法36条、不動産登記規則43条・44条・75条・76条、不動産登記事務取扱手続準則51条は、`note-articles/laws/` 配下の原文で確認しました。',
        'イの根拠は、令別表四の項添付情報欄ニ（現在の住所を証する情報）を、署名用電子証明書で代える規則44条1項です。令別表の原文との対応は確認しましたが、個別の先例・通達の確認はしていません。',
        '補足説明（エ）の「近くの地図が500分の1だとして」という例は、縮尺が同一という要件を説明するための仮定の数字で、実際の縮尺は地域によって異なります。',
    ],
    phrases=['地積測量図は一筆ごとに作ります', '署名用電子証明書で住所の証明に代えられます', '余白に土地所在図を描けるんです', '縮尺が違えば図面は兼ねられません', '買った土地は一月以内に表題登記です'],
    header=dict(t1=_H['t1'], t2=_H['t2'], topic=_H['topic'], kanji='・'.join(K(*_H.values()))),
    poster_intro='土地の表題登記を、「図面と電子申請の特例」（グループA：ア・イ・ウ）と「図面の兼用と申請義務」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title=_PT, sub=_PS,
        col_a='図面と電子申請の特例', col_b='図面の兼用と申請義務', n_a=3,
        cards=_cards,
        kanji=K(_PT, _PS, '図面と電子申請の特例図面の兼用と申請義務', *[c['h'] + c['tag'] + ''.join(c['words']) for c in _cards])),
    nb_label='ア・エ肢', nb_intro='ア・エの補足説明に合わせた2枚です。1枚目は、図面を一筆の土地ごとに作ることを図で示します。2枚目は、地積測量図が土地所在図を兼ねられる場合とそうでない場合を左右の対比で示します。',
    notebooks=[
        dict(name='図面は一筆の土地ごとに作る', args=dict(
            title='地積測量図は何枚つくる？', sub='図面を作る単位（毎日ドリル 第66日 ア）',
            req='a diagram',
            layout=_nb1_layout,
            callout='土地所在図と地積測量図は、一筆の土地ごとに作ります。\n同時に申請する2筆の土地でも、まとめて1枚の図面にはできません。',
            footer='不動産登記規則75条1項',
            kanji=K('地積測量図は何枚つくる図面を作る単位甲土地乙土地同時に申請一筆ごと不動産登記規則'), what='blocks',
            check='confirm there are exactly two blocks and exactly two separate drawing sheets in Block 2, ')),
        dict(name='地積測量図が土地所在図を兼ねられるとき', args=dict(
            title='地積測量図が土地所在図を兼ねるには', sub='縮尺の条件（毎日ドリル 第66日 エ）',
            req='a side-by-side comparison',
            layout=_nb2_layout,
            callout='地積測量図が土地所在図を兼ねるには、縮尺が土地所在図と同一で、土地の所在を明確に表示できることが必要です。\n縮尺が違えば、所在がはっきり描けていても兼ねられません。',
            footer='不動産登記事務取扱手続準則51条4項',
            kanji=K('地積測量図が土地所在図を兼ねるには縮尺の条件同じ違う所在明確に表示不動産登記事務取扱手続準則'), what='panels',
            check='confirm the two panel headers are different strings (縮尺が同じ on the left and 縮尺が違う on the right) and that the left panel shows a green check mark while the right panel shows a red cross, ')),
    ],
)
