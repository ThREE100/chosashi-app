"""書式ひな形ドリル（申請書）の1問1ファイル用の共通部品。各問 pmNN.py は PROBLEM（dict）を定義する。
スキーマは evening/gen_shinsei.py の shinsei2 と同じ（exam・form・calc・fig・coords）。gen_forms.py が読み込み、
id・day・kind・forms_no を付けて evening/problems/PM-NN.json に書き出し、registry.json と forms_made.json を更新する。

作り方の決まり（daily-drill/RULES.md の 3.4・3.6 も読む）:
- 条文の引用（basis の quote）は note-articles/laws/ の原文に一字一句あること（check_pm.py が機械照合する。全角数字・かっこもそのまま）。
- 数値（地積・床面積）は座標・寸法から計算し、assert で答えと一致を確かめる。四捨五入の境目を避ける。
- 申請日は令和8年10月26日、提出先はA地方法務局、代理人は「A市D町一丁目2番3号　土地家屋調査士　斉藤一郎」（固定）。
- 期限のある登記は、原因の日付から申請日までを1か月以内にする。
- 注で、答案用紙の書き方の約束（欄番号・原因の文言の形・空欄にする欄・登記識別情報や印鑑証明書の扱い）を必ず書き、答えを一つに決める。
- ひっかけ（事実関係に、申請人でない人・関係のない日付・要らない書類）を2つ以上入れる。
- 個人の演習結果・過去問の年度や問番号は書かない。"""
import math

HO, KI, REI, TOUMEN, JUN = '不動産登記法', '不動産登記規則', '不動産登記令別表', '登録免許税法', '不動産登記事務取扱手続準則'
REI0 = '不動産登記令'
MINPO = '民法'
KUBUN = '区分所有法'   # 建物の区分所有等に関する法律（lawtext では「区分所有法」）

AGENT = 'A市D町一丁目2番3号　土地家屋調査士　斉藤一郎'
DATE = '令和8年10月26日申請　A地方法務局'


def B(law, art, quote):
    return {'law': law, 'article': art, 'quote': quote}


def area(pts):
    s = 0.0
    for i in range(len(pts)):
        x0, y0 = pts[i]
        x1, y1 = pts[(i + 1) % len(pts)]
        s += x0 * y1 - x1 * y0
    return abs(s) / 2


def floor2(v):
    return math.floor(v * 100 + 1e-9) / 100


def en_to_xy(org, pts):
    """(東e, 北n) の寸法を、原点 org=(X,Y) からの座標 (X北, Y東) に直す。"""
    return {n: (round(org[0] + nn, 2), round(org[1] + e, 2)) for n, (e, nn) in pts.items()}


def field(id_, label, answer, basis, note, lines=1, copy=False):
    return {'kind': 'field', 'id': id_, 'label': label, 'lines': lines, 'answer': answer, 'basis': basis, 'note': note, **({'copy': True} if copy else {})}


def f_date():
    return field('date', '申請日・提出先', DATE, [], '問題文に書いてある。', copy=True)


def f_agent(n):
    return field('agent', '代理人（住所・氏名）', AGENT, [], f'事実関係{n}に書いてある。', lines=2, copy=True)


def lot_rect(x0, y0, x1, y1, names):
    """長方形の土地の4つの角（北西・北東・南東・南西）"""
    a, b, c, d = names
    return {a: (x1, y0), b: (x1, y1), c: (x0, y1), d: (x0, y0)}


def fig_generic(points, polys, texts, road=None, lines=None, hidden=()):
    pts = {k: {'xy': list(v), 'kind': 'hidden' if k in hidden else 'ref'} for k, v in points.items()}
    f = {'points': pts, 'polys': polys, 'lines': lines or [], 'texts': texts}
    if road:
        f['road'] = road
    return f
