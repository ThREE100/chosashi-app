"""out/ のHTMLを、配布用のPDFに一括で書き出す（pdf/ に同じ名前で .pdf）。
- ヘッダー・フッター（日付・ファイルの場所）を付けない、背景（網掛け・色）を付ける、A4・余白はページの指定どおり。
- 文書情報（PDFのプロパティ）を整える：タイトル＝ページの題、作成者・作成アプリ・PDF変換は下の DOC_INFO の値だけにし、
  ブラウザやPCの情報（Chrome の版、ユーザー名、ファイルの場所）を残さない。XMPメタデータも消す。
- 書き出した後、文書情報と本文に PC のユーザー名・ホームフォルダのパス・file:/// が入っていないことを確かめる。
必要なもの：Google Chrome または Microsoft Edge（または Chromium）、Python のパッケージ pypdf（pip install pypdf）。
使い方: python daily-drill/make_pdf.py                    （out/ の全部）
        python daily-drill/make_pdf.py day001 day002 sat01 （名前の頭で絞る）
        CHROME_PATH=…/chrome.exe python daily-drill/make_pdf.py （ブラウザの場所を指定）"""
import getpass
import glob
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out')
PDF = os.path.join(HERE, 'pdf')
DOC_INFO = {                       # PDFのプロパティに入れる値（ここを書き換える。個人名は入れない）
    '/Author': '毎日ドリル（土地家屋調査士試験）',
    '/Subject': '土地家屋調査士試験 毎日ドリル（令和8年8月時点の法令による）',
    '/Keywords': '土地家屋調査士, 毎日ドリル',
    '/Creator': '毎日ドリル',
    '/Producer': '毎日ドリル',
}


def find_browser():
    cands = [os.environ.get('CHROME_PATH', '')]
    cands += [shutil.which(x) or '' for x in ('google-chrome', 'google-chrome-stable', 'chromium', 'chromium-browser', 'chrome', 'msedge', 'microsoft-edge')]
    pf = [os.environ.get(k, '') for k in ('PROGRAMFILES', 'PROGRAMFILES(X86)', 'LOCALAPPDATA')]
    for base in pf:
        if base:
            cands += [os.path.join(base, 'Google', 'Chrome', 'Application', 'chrome.exe'),
                      os.path.join(base, 'Microsoft', 'Edge', 'Application', 'msedge.exe')]
    cands += ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
              '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge']
    cands += sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'), reverse=True)
    for c in cands:
        if c and os.path.isfile(c):
            return c
    sys.exit('Chrome / Edge が見つからない。CHROME_PATH にブラウザの実行ファイルの場所を指定する。')


def render(browser, html, pdf, tmpdir):
    uri = pathlib.Path(html).resolve().as_uri()
    cmd = [browser, '--headless', '--disable-gpu', '--no-pdf-header-footer', '--print-to-pdf-no-header',
           f'--user-data-dir={tmpdir}', f'--print-to-pdf={pdf}', uri]
    if os.name != 'nt' and hasattr(os, 'geteuid') and os.geteuid() == 0:
        cmd.insert(1, '--no-sandbox')
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
    return os.path.exists(pdf)


def clean(pdf, title):
    from pypdf import PdfReader, PdfWriter
    r = PdfReader(pdf)
    w = PdfWriter(clone_from=r)
    w._root_object.pop('/Metadata', None)                    # XMPメタデータを消す
    w._info = None
    info = {'/Title': title}
    info.update(DOC_INFO)
    w.add_metadata(info)
    for k in ('/CreationDate', '/ModDate'):
        w._info.get_object().pop(k, None) if w._info is not None else None
    tmp = pdf + '.tmp'
    with open(tmp, 'wb') as f:
        w.write(f)
    os.replace(tmp, pdf)


def check(pdf):
    """文書情報と本文に、ユーザー名・ホームのパス・file:/// が入っていないか"""
    from pypdf import PdfReader
    r = PdfReader(pdf)
    meta = ' '.join(str(v) for v in (r.metadata or {}).values())
    text = meta + ' '.join((p.extract_text() or '') for p in r.pages)
    bad = [x for x in {getpass.getuser(), os.path.expanduser('~'), 'file:///', 'HeadlessChrome', 'Mozilla/'} if x and len(x) > 2 and x in text]
    raw = open(pdf, 'rb').read()
    if b'/Metadata' in raw and b'<x:xmpmeta' in raw:
        bad.append('XMP')
    return bad


def main():
    try:
        import pypdf  # noqa: F401
    except ImportError:
        sys.exit('pypdf がない。 pip install pypdf で入れる。')
    pre = [a for a in sys.argv[1:]]
    files = sorted(f for f in glob.glob(os.path.join(OUT, '*.html')) if os.path.basename(f) != 'index.html')
    if pre:
        files = [f for f in files if any(os.path.basename(f).startswith(p) for p in pre)]
    os.makedirs(PDF, exist_ok=True)
    browser = find_browser()
    ng = 0
    with tempfile.TemporaryDirectory() as td:
        for i, html in enumerate(files, 1):
            name = os.path.basename(html)[:-5]
            pdf = os.path.join(PDF, name + '.pdf')
            t = re.search(r'<title>(.*?)</title>', open(html, encoding='utf-8').read(), re.S)
            title = t.group(1).strip() if t else name
            if not render(browser, html, pdf, td):
                print(f'NG {name}: PDFにできなかった'); ng += 1; continue
            clean(pdf, title)
            bad = check(pdf)
            if bad:
                print(f'NG {name}: 文書情報か本文に {bad} が入っている'); ng += 1
            if i % 50 == 0:
                print(f'… {i}/{len(files)}')
    print(f'{len(files)}ファイルを {PDF} に書き出し。NG {ng}件')
    sys.exit(1 if ng else 0)


if __name__ == '__main__':
    main()
