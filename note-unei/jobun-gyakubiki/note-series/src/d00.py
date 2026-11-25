"""第0回（総論）：図鑑の使い方と、条文から過去問を引くと見えること。数字はすべて図鑑のデータから計算する。"""
import collections
import lib

NO = 0
SLUG = 'soron-tsukaikata'
TITLE = '図鑑の使い方と、条文から過去問を引くと見えること'
LAWS = '不動産登記法・不動産登記令・不動産登記規則・準則・区分所有法・民法・土地家屋調査士法'

_c = lib.total_counts()
_law = collections.Counter(law for (law, _a) in lib.JOBUN)
_ORDER = ['民法', '不動産登記規則', '不動産登記法', '不動産登記事務取扱手続準則', '土地家屋調査士法', '不動産登記令', '区分所有法', '土地家屋調査士法施行規則']
_top = sorted(lib.JOBUN.values(), key=lambda j: (-j['years'], -j['shi']))
_top = [j for j in _top if j['years'] >= 13]

LEAD = [
    f"択一式の過去問を解いていると、「この条文、前にも見た」と感じることがよくあります。その感覚を確かめるために、平成17年度〜令和8年度の択一式の全肢解説から、**条文ごとに「いつ・どの肢で出たか」を引ける図鑑**を作りました。条文は{_c['jobun']}、拾えた肢は{_c['shi_all']:,}肢のうち{_c['shi_cited']:,}肢です。",
    'この記事は、そのシリーズの第0回です。図鑑のページの読み方と、条文から過去問を引くと何が見えてくるかを先にお話しし、最後にシリーズの目次を載せます。',
    '先に結論を書くと、本試験は**同じ条文から、言い回しを少し変えて何年も続けて出ます**。条文ごとに過去の肢を並べると、「出題者がどこを変えてひっかけてくるか」が一目で見えるようになります。',
]

POSTER = dict(
    title='条文の逆引き図鑑の使い方',
    topics='年度の帯・条文の原文・出題された肢',
    cards=[
        ('図鑑のページ', '1条文＝1ページ', 'a single web page card with three stacked bands: a row of small colored year tiles at the top, an open law book in the middle, and a short list with blue circle and red cross marks at the bottom'),
        ('探し方', '番号でも言葉でも', 'a search box with a magnifying glass, next to two small tags 「第58条」 and 「地目」'),
        ('くり返し出る', '毎年のように出る', 'a calendar strip with many tiles filled in for the same law book icon'),
        ('並べて読む', 'ひっかけが見える', 'two quiz cards side by side, one with a blue circle and one with a red cross, with a magnifier on the one changed word'),
        ('シリーズ', '全14回で主要条文', 'a row of fourteen thin book spines on a shelf (blank spines, no numbers, no letters)'),
    ])

_rank = '\n'.join(f"{i}. {lib.law_name(j['law'])} {lib.jn(j['article'])}（{lib.caption(j['law'], j['article']) or '—'}）…{j['years']}年度・{j['shi']}肢"
                  for i, j in enumerate(_top, 1))

SECTIONS = [
    dict(h='図鑑のページは3つの帯でできている', body=[
        '図鑑は、条文1つにつき1ページです。どのページも、上から次の3つが並んでいます。',
        '1. **年度の帯**：平成17年度〜令和8年度のうち、その条文が出た年度に色が付きます。色の付いた年度が多いほど、くり返し出ている条文です。\n2. **条文の原文**：法令の原文をそのまま載せています。肢を読む前に、ここで主語・期限・「できる」か「しなければならない」かを確かめます。\n3. **出題された肢**：その条文を引いている肢を年度順に並べ、○×と、年度別の全肢解説でのポイントを付けています。肢から、年度別の全肢解説へ進めます。',
        '一覧のページでは、条文番号（例：第58条）でも、言葉（例：地目、合筆、共用部分）でも探せます。'],
        zu_no=1, zu=dict(title='図鑑のページの読み方', sub='年度の帯・条文の原文・出題された肢',
                         layout=('Draw one large web-page mock-up in the center (no browser bar text). Inside it, three stacked bands joined by small '
                                 'navy arrows on the right labeled: top band 「年度の帯」 shows a row of small square tiles, some filled blue and some blank '
                                 '(no numbers on the tiles); middle band 「条文の原文」 shows an open law book with blank ruled lines; bottom band 「出題された肢」 '
                                 'shows three short quiz cards, the first and third with a blue circle mark and the second with a red cross mark (blank text lines). '
                                 'To the right of each band, a short sticky label: next to the top band 「くり返し出るかを見る」, next to the middle band '
                                 '「主語と期限を確かめる」, next to the bottom band 「どこを変えたかを見る」. Below the mock-up, a search box with a magnifier and '
                                 'two small tags 「第58条」 and 「地目」, with the caption 「番号でも言葉でも探せる」.'),
                         footer='平成17年度〜令和8年度の択一式から作成')),
    dict(h='数えて分かったこと：くり返し出る条文は決まっている', body=[
        '法令ごとに、図鑑に載った条文の数は次のとおりです。' + '、'.join(f"{lib.law_name(l)}{_law[l]}条" for l in _ORDER if _law[l]) + '。民法は条文の種類は多いのですが、1つの条文が出る年度は少なめです。くり返し出るのは、不動産登記法と、その下の令・規則・準則の条文です。',
        '出た年度が13年度以上の条文は、次のとおりです（年度は22年度分のうち）。',
        _rank,
        '上位には、**分筆・合筆**（第39条・第41条）、**申請情報**（令第3条）、**共有者の一人でできること**（民法第252条）、**代位**（民法第423条）、**地目**（準則第68条）、**建物の表題部の変更**（第51条）、**まとめて申請**（規則第35条）、**地図の訂正**（規則第16条）、**合体**（第49条）、**共用部分**（第58条）が並びます。このシリーズは、これらの条文を中心に取り上げます。'],
        zu_no=2, zu=dict(title='くり返し出る条文', sub='出た年度が多い条文の顔ぶれ',
                         layout=('Draw a horizontal bar chart with plain colored bars and no axis numbers. Each bar has a label on its left, from top to bottom: '
                                 + '、'.join(f"「{lib.law_name(j['law'])}{lib.jn(j['article'])}」" for j in _top)
                                 + '. Bars for 不動産登記法・規則・令・準則 are blue, bars for 民法 are pale orange. The bars get slightly shorter from top to '
                                 'bottom (do not write any number on or beside the bars). Above the chart, a legend with a blue square 「登記の法令」 and a pale '
                                 'orange square 「民法」. Below the chart, a banner 「同じ条文から何年も続けて出る」.'),
                         footer='出た年度の数で並べた。数字は記事の本文を参照')),
    dict(h='使い方：迷った肢から条文を引き、条文から肢を並べる', body=[
        '図鑑のおすすめの使い方は、次の3ステップです。',
        '1. **過去問で迷った肢の条文を引く**：解説に「不動産登記法第41条」と出てきたら、その条文のページを開きます。\n2. **年度の帯でくり返しを見る**：色の付いた年度が多ければ、次の本試験でも出る可能性が高い条文です。優先して覚えます。\n3. **○×の肢を並べて、変えられた言葉を探す**：同じ条文から作られた肢を並べると、出題者が「主語」「期限」「できる／しなければならない」「例外の有無」のどこを変えて誤りの肢にしているかが見えます。',
        '3つめのステップがいちばん大切です。1問ずつ解いているときには気づきにくいのですが、並べてみると、誤りの肢の作り方は条文ごとにほぼ決まっています。'],
        zu_no=3, zu=dict(title='図鑑の使い方', sub='迷った肢→条文→並べた肢',
                         layout=('Draw a vertical flow of three rounded boxes joined by thick downward navy arrows. Box 1 (pale blue): 「迷った肢の条文を引く」 '
                                 'with an icon of a quiz card and a magnifier. Box 2 (pale beige): 「年度の帯でくり返しを見る」 with an icon of a row of tiles, many filled. '
                                 'Box 3 (pale orange, larger): 「並べて変えられた言葉を探す」 with an icon of three quiz cards side by side and one word highlighted. '
                                 'Beside box 3, four small tags in a 2x2 grid: 「主語」「期限」「できる・しなければならない」「例外」.'),
                         footer='このシリーズの各回も、この順で読めるように書いています')),
    dict(h='図鑑で拾えていないもの', body=[
        f"図鑑が拾っているのは、肢の解説の中で**法令名つきで**引いている条文だけです。「法第○条」のように法令名のない書き方は数えていないので、拾えた肢は全体の約{round(_c['shi_cited'] / _c['shi_all'] * 100)}％です。図鑑に載っていない肢でも、条文が関係しないわけではありません。",
        '令和8年度の肢は、正誤を現行法令で確かめ終えていないため、図鑑では「？（記事で確認）」と出ます。このシリーズの記事でも、令和8年度の肢は○×を付けて載せていません。',
        '図鑑の「ポイント」は、年度別の全肢解説の肢の見出しです。見出しは記事によって「正しい結論」の形のものと「肢の主張」の形のものがあるので、迷ったら必ず○×と合わせて読み、年度別の記事の本文に進んでください。']),
    dict(h='シリーズの目次', body=['第1回からは、本試験でくり返し出る条文を、つながりのある順に取り上げます。各回に、総論の図解、条文ごとの解説の図解、取り違えやすいところをまとめた間違いノートを付けます。',
                               '__MOKUJI__']),
]
JOBUN = []

MISTAKES = [
    dict(title='「できる」と「しなければならない」を読み分ける',
         sub='条文の語尾を変えるひっかけ',
         wrong='登記官が職権でするものは、どれも「しなければならない」。',
         right='条文の語尾で決まる。同じ条の中でも「しなければならない」と「できる」が並ぶ。',
         steps=['肢の語尾が「しなければならない」か「できる」かに印を付ける', '条文の語尾と同じかを確かめる', '「できる」には条件（異議がないときに限り など）が付いていないかを見る'],
         callout='不動産登記法第39条は、第2項が「職権で分筆の登記をしなければならない」、第3項が「異議がないときに限り、職権で分筆又は合筆の登記をすることができる」です。語尾と条件を入れ替えた肢がくり返し出ます。',
         footer='不動産登記法第39条第2項・第3項、土地家屋調査士法第16条',
         shi=['R02-Q09-ア', 'H29-Q14-オ', 'H30-Q20-ア'])]

SUMMARY = [
    '図鑑は、条文1つにつき1ページ。年度の帯・条文の原文・出題された肢の3つで、その条文の出方が分かる。',
    'くり返し出る条文は決まっている。不動産登記法と、令・規則・準則の表示に関する登記の条文が中心。',
    '使い方は、迷った肢→条文→並べた肢。並べると、誤りの肢がどの言葉を変えて作られているかが見える。',
    '図鑑の「ポイント」は記事の見出し。必ず○×と合わせて読み、迷ったら年度別の記事の本文へ。',
]
NEXT = '次回（第1回）は、出た年度がいちばん多い不動産登記法第39条と、分筆に伴う権利の消滅の第40条です。「分筆・合筆は誰が申請できるか」を、共有・相続・代位の肢で確かめます。'
NOTES = ['法令ごとの条文の数と、出た年度の多い条文の一覧は、図鑑のデータ（`note-unei/jobun-gyakubiki/data/jobun.json`）から計算しています。']

HEADER = dict(
    store='ポルトの「リブラリア・レロ」（深紅の二股に分かれる階段、ステンドグラスの天窓、彫刻のある木の書棚）',
    scene=('A grand neo-Gothic bookstore hall: a sweeping crimson-carpeted staircase that splits into two curving branches in the center, '
           'richly carved dark wood bookshelves rising to the ceiling, and a colorful stained-glass skylight casting soft jewel-toned light. '
           'Warm golden lamplight; the far shelves fade softly into a gentle blur.'),
    pose='she stands on the lower steps of the staircase, turning back toward the viewer, one hand lightly on the carved banister and the other holding an open notebook against her chest.',
    face='a bright, welcoming smile, as if inviting the reader to come up the stairs with her.',
    prop='a small open notebook (blank pages).',
    pose_ja='階段の下の段に立ち、振り返って手すりに手をかけ、ノートを胸に抱える',
    face_ja='「一緒に行こう」と誘う明るい笑顔',
    l1='条文の逆引き図鑑', l2='使い方と全体像', sub='条文から過去問を引いてみよう')
