# E-03 床面積の求積と端数処理
from decimal import Decimal as D, ROUND_DOWN, ROUND_HALF_UP

# 計算例の数値（壁の厚さ0.12メートル、壁の中心線で測った外形 9.10×7.28 の平家建）
A, B, T = D('9.10'), D('7.28'), D('0.12')
HEKISHIN = A * B                       # 壁心の面積（そのまま）
UA, UB = A - T, B - T                  # 内法：両側で壁の厚さの半分ずつ、計1枚分減る
UCHINORI = UA * UB


def cut(x):
    return x.quantize(D('0.01'), rounding=ROUND_DOWN)


def rnd(x):
    return x.quantize(D('0.01'), rounding=ROUND_HALF_UP)


SHEET = dict(
    id='E-03',
    law='不動産登記規則',
    articles='不動産登記規則第100条・第115条、準則第82条',
    conclusion=[
        '床面積は**各階ごと**に、壁その他の区画の**中心線**（区分建物は**内側線**）で囲まれた部分の水平投影面積で求める。',
        '単位は平方メートル。**100分の1未満は切り捨て**る（四捨五入しない）。',
        '地積と違い、端数の扱いは建物の種類や広さで変わらない。算入の可否は準則第82条。',
    ],
    blocks=[
        dict(kind='table', title='どの線で測るか',
             head=['建物', '測る線', '根拠'],
             rows=[['区分建物でない建物', '壁その他の区画の中心線（壁心）', '規則第115条'],
                   ['区分建物', '壁その他の区画の内側線（内法）', '規則第115条かっこ書'],
                   ['柱や壁が傾いている', '各階の床面の接着する壁その他の区画の中心線', '準則第82条第9号']]),
        dict(kind='steps', title='計算の型',
             items=['区分建物かどうかを決め、壁心か内法かを選ぶ。',
                    '内法なら、壁の中心線から壁の厚さの半分ずつ内側へ寄せた寸法にする（両側で厚さ1枚分短くなる）。',
                    '各階ごとに長方形に分けて面積を出し、準則第82条で入れない部分を除く。',
                    '各階の合計を100分の1未満切り捨てで書く。']),
        dict(kind='check', title='床面積に入れるか（準則第82条）',
             yes_label='算入する',
             yes=['階段室・エレベーター室（床があるとみなす。第6号）',
                  '1室の一部が天井高1.5メートル未満でも、その室の面積に入れる（第1号ただし書）',
                  '建物の内部の煙突・ダストシュート（第10号）',
                  '高さ1.5メートル以上で下部が床面と同じ高さの出窓（第11号）'],
             no_label='算入しない',
             no=['天井高1.5メートル未満の地階・屋階（特殊階。第1号）',
                 '建物に附属する屋外の階段（第7号）',
                 '上階まで吹抜になっている部分（上階の床面積に入れない。第8号）',
                 '外側にある煙突・ダストシュート（第10号）']),
    ],
    example=dict(kind='計算例', title='同じ平家建を壁心と内法で比べる（壁の厚さ0.12メートル）',
                 lines=[f'壁心：{A} × {B} ＝ {HEKISHIN} → 切り捨てて {cut(HEKISHIN)}㎡（四捨五入なら {rnd(HEKISHIN)} で誤り）',
                        f'内法：({A} − {T}) × ({B} − {T}) ＝ {UA} × {UB} ＝ {UCHINORI} → 切り捨てて {cut(UCHINORI)}㎡（四捨五入なら {rnd(UCHINORI)} で誤り）',
                        f'区分建物でなければ {cut(HEKISHIN)}㎡、区分建物の専有部分なら {cut(UCHINORI)}㎡ になる。']),
    traps=['端数は**切り捨て**。四捨五入すると、第3位が5以上のときに0.01ずれる。',
           '地積は宅地・鉱泉地以外で10㎡を超えると1㎡未満を切り捨てる（規則第100条）。**床面積はいつも100分の1未満**の切り捨てで、地積の扱いと混ぜない。',
           '内法にするとき、壁の厚さの**半分を両側から**引く。片側だけ引いたり、厚さ1枚分を片側ずつ引いたりしない。'],
    basis=['不動産登記規則第100条・第115条', '準則第82条'],
    more=['topics/KE_10_yukamenseki-sannyu.md'],
    claims=[
        ('不動産登記規則', '115', '各階ごとに壁その他の区画の中心線（区分建物にあっては、壁その他の区画の内側線）で囲まれた部分の水平投影面積'),
        ('不動産登記規則', '115', '一平方メートルの百分の一未満の端数は、切り捨てるものとする'),
        ('不動産登記規則', '100', '宅地及び鉱泉地以外の土地で十平方メートルを超えるものについては、一平方メートル'),
        ('準則', '82', '天井の高さ１．５メートル未満の地階及び屋階（特殊階）は、床面積に算入しない'),
        ('準則', '82', '１室の一部が天井の高さ１．５メートル未満であっても、その部分は、当該１室の面積に算入する'),
        ('準則', '82', '階段室、エレベーター室又はこれに準ずるものは、床を有するものとみなして各階の床面積に算入する'),
        ('準則', '82', '建物に附属する屋外の階段は、床面積に算入しない'),
        ('準則', '82', 'その吹抜の部分は、上階の床面積に算入しない'),
        ('準則', '82', '出窓は、その高さ１．５メートル以上のものでその下部が床面と同一の高さにあるものに限り、床面積に算入する'),
    ],
    header=dict(l1='床面積の求め方と', l2='端数の切り捨て', hl='切り捨て',
                left='a simple floor plan of a one-story house with thick walls, a dashed line along the middle of the walls, all without any text',
                right='a calculator, a pencil and a ruler on a desk next to a small house model, all without any text'),
    zukai=dict(title='床面積の求め方', topics='壁心と内法・切り捨て・算入しない部分',
               cards=[
                   dict(h='ふつうの建物は壁の中心線', illust='A thick wall seen from above with a dashed line running through the middle of the wall, and the enclosed area shaded.', words=['壁心'], tag='中心線で囲む'),
                   dict(h='区分建物は壁の内側線', illust='An apartment unit seen from above with the shading stopping at the inner face of the walls.', words=['内法'], tag='内側線で囲む'),
                   dict(h='端数は切り捨て', illust='A number line with a small piece cut off by scissors, no figures shown.', words=[], tag='100分の1未満は切り捨て'),
                   dict(h='吹抜は上の階に入れない', illust='A two-story section where an open void rises from the first floor; the void area on the second floor is left unshaded.', words=['吹抜'], tag='上階に算入しない'),
                   dict(h='屋外の階段は入れない', illust='A house with an outside staircase attached; the staircase is left unshaded.', words=[], tag='屋外の階段は不算入'),
                   dict(h='階段室は各階に入れる', illust='A stair core inside a building, shaded on every floor.', words=[], tag='床があるとみなす'),
               ]),
)


def verify():
    assert HEKISHIN == D('66.2480'), HEKISHIN
    assert cut(HEKISHIN) == D('66.24') and rnd(HEKISHIN) == D('66.25')
    assert (UA, UB) == (D('8.98'), D('7.16'))
    assert UCHINORI == D('64.2968'), UCHINORI
    assert cut(UCHINORI) == D('64.29') and rnd(UCHINORI) == D('64.30')
    assert cut(HEKISHIN) > cut(UCHINORI)
