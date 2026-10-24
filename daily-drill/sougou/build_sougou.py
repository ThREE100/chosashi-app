"""本番形式の統合問題（記述式）：1つの事案で、第1部 調査・計算 → 第2部 申請書 → 第3部 図面 を通して解く（目安60分）。
sougou/sNN/ に次の3つ（＋meta）を置く：
  calc.py  SPEC（evening/chain.py の形。計算エンジンで答え・方法B・キー列・答えが一つに決まるかを確かめる）
  form.py  PROBLEM（evening/forms/ の書式ひな形と同じ形。check_pm の申請書の検査をそのまま使う）
  draw.py  DRAW（evening/problems/PM-09.json・PM-10.json と同じ作図の形：draw・text・tables・answers・spec・rubric・steps・trap）
  meta.py  META = {'title', 'minutes', 'lead'（事案の全体と時間配分の目安）, 'links'（部をまたいで同じ値を使う欄）}
links の例：{'from': ['calc', '本件土地の地積'], 'to': ['form', 'land', '（イ）', 3]}  … 計算の答えと申請書の表の欄が同じ値であること。
           {'from': ['calc', '点P'], 'to': ['draw', '点P']}                     … 計算の答えと作図の答えの欄が同じであること。
使い方: python3 daily-drill/sougou/build_sougou.py [s01 …]   （検査して out/sougouNN.html・sougouNN-ans.html を書き出す）"""
import glob
import importlib.util
import json
import os
import re
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'evening'))
sys.path.insert(0, os.path.join(ROOT, 'evening', 'forms'))
import build as B  # noqa: E402
import chain  # noqa: E402
import check_pm as CP  # noqa: E402


def load(fp, name):
    if not os.path.exists(fp):
        return None
    spec = importlib.util.spec_from_file_location(os.path.basename(fp)[:-3] + '_' + os.path.basename(os.path.dirname(fp)), fp)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return getattr(m, name)


def body_of(html):
    return html.split('<body>', 1)[1].rsplit('</body>', 1)[0]


def parts(sid):
    d = os.path.join(HERE, sid)
    meta = load(os.path.join(d, 'meta.py'), 'META')
    up = sid.upper()
    out = {}
    S = load(os.path.join(d, 'calc.py'), 'SPEC')
    if S:
        S['pid'] = f'{up}-1'
        p, _, _ = chain.build_problem(S, 0)
        p['day'] = f'本番形式 {up}'
        p['title'] = '第1部　調査・計算：' + p['title']
        out['calc'] = p
    F = load(os.path.join(d, 'form.py'), 'PROBLEM')
    if F:
        p = dict(F)
        p.update({'id': f'{up}-2', 'day': f'本番形式 {up}', 'kind': 'shinsei2', 'module': True})
        p.setdefault('layout', 'generic' if p.get('fig') else 'none')
        p['title'] = '第2部　申請書：' + p['title']
        out['form'] = p
    D = load(os.path.join(d, 'draw.py'), 'DRAW')
    if D:
        p = dict(D)
        p.update({'id': f'{up}-3', 'day': f'本番形式 {up}', 'kind': 'draw'})
        p['title'] = '第3部　図面：' + p['title']
        out['draw'] = p
    return meta, out


def value(part, key):
    """部の答えの値（ラベルの頭の語で探す）"""
    if part['kind'] == 'shinsei2':
        raise KeyError
    for a in part['answers']:
        if a['label'].startswith(key):
            return a['value']
    raise KeyError(key)


def check(sid):
    meta, ps = parts(sid)
    errs = []
    if not meta:
        return [f'{sid}: meta.py がない']
    for k in ('calc', 'form', 'draw'):
        if k not in ps:
            errs.append(f'{sid}: {k}.py がない（第1部〜第3部の3つが要る）')
    CP.nerr = 0
    if 'calc' in ps:
        errs += [f'{sid} 第1部: {e}' for e in chain.verify_problem(ps['calc'])]
    if 'form' in ps:
        before = CP.nerr
        CP.check_shinsei2(ps['form'])
        if CP.nerr > before:
            errs.append(f'{sid} 第2部: 申請書の検査で NG {CP.nerr - before}件（上の NG の行）')
    if 'draw' in ps:
        p = ps['draw']
        for k in ('draw', 'text', 'answers', 'spec', 'rubric', 'steps', 'trap'):
            if k not in p:
                errs.append(f'{sid} 第3部: {k} がない')
        if len(p.get('rubric', [])) < 6:
            errs.append(f'{sid} 第3部: 自己採点の項目が少ない（6つ以上）')
        if 'verify' in p:      # 答えの欄を座標から計算し直す・キー列の表示を再現する（evening の作図ドリルと同じ検査）
            CP.check_draw_module(p, report=lambda m: errs.append(f'{sid} 第3部: {m}'))
        else:
            errs.append(f'{sid} 第3部: verify がない（答えの欄を座標から計算し直す式）')
        try:
            (B.draw_forms.chiseki_solved(p['spec']) if p['draw'] == 'chiseki' else B.draw_forms.tatemono_solved(p['spec']))
        except Exception as e:   # noqa: BLE001
            errs.append(f'{sid} 第3部: 模範の作図が描けない（{e}）')
    for ln in meta.get('links', []):
        try:
            a = value(ps[ln['from'][0]], ln['from'][1])
            if ln['to'][0] == 'form':
                tb = [it for it in ps['form']['form']['items'] if it.get('id') == ln['to'][1]][0]
                row = [r for r in tb['rows'] if r['name'] == ln['to'][2]][0]
                b = row['cells'][ln['to'][3]]
                ok = (a if isinstance(a, str) else ' '.join(a)) in b
            else:
                b = value(ps[ln['to'][0]], ln['to'][1])
                ok = a == b
            if not ok:
                errs.append(f'{sid}: 部をまたぐ値が合わない {ln["from"]}＝{a} ／ {ln["to"]}＝{b}')
        except (KeyError, IndexError) as e:
            errs.append(f'{sid}: links の指定が見つからない {ln}（{e}）')
    if len(meta.get('links', [])) < 2:
        errs.append(f'{sid}: links が少ない（計算の答えを申請書・図面で使う欄を2つ以上照らす）')
    return errs


def write(sid):
    meta, ps = parts(sid)
    cover = B.head(f'本番形式 {sid.upper()}', '記述式の統合問題（' + meta['title'] + '）', '第1部 調査・計算 → 第2部 申請書 → 第3部 図面を、1つの事案として通して解く', meta.get('minutes', 60))
    cover += '<h2>事案の全体と解き方の目安</h2>' + ''.join(f'<p>{B.E(x)}</p>' for x in meta['lead'])
    cover_html = B.page(f'本番形式 {sid}', cover, f'{sid.upper()} 表紙', right='')
    q = body_of(cover_html) + ''.join(body_of(B.pm_q(ps[k])) for k in ('calc', 'form', 'draw'))
    a = ''.join(body_of(B.pm_a(ps[k])) for k in ('calc', 'form', 'draw'))
    head = cover_html.split('<body>', 1)[0]
    open(os.path.join(B.OUT, f'sougou{sid[1:]}.html'), 'w', encoding='utf-8').write(head + '<body>' + q + '</body></html>')
    open(os.path.join(B.OUT, f'sougou{sid[1:]}-ans.html'), 'w', encoding='utf-8').write(head + '<body>' + a + '</body></html>')
    json.dump({k: v for k, v in ps.items()}, open(os.path.join(HERE, sid, 'built.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def main(only):
    ng = 0
    for d in sorted(glob.glob(os.path.join(HERE, 's[0-9][0-9]'))):
        sid = os.path.basename(d)
        if only and sid not in only:
            continue
        try:
            errs = check(sid)
        except chain.SpecError as e:
            errs = [f'{sid} 第1部: {e}']
        for e in errs:
            print('NG ' + e)
        ng += len(errs)
        if not errs:
            write(sid)
            print(f'OK {sid}：out/sougou{sid[1:]}.html・sougou{sid[1:]}-ans.html を書き出し')
    print(f'統合問題の検査：NG {ng}件')
    return ng


if __name__ == '__main__':
    sys.exit(1 if main(set(sys.argv[1:])) else 0)
