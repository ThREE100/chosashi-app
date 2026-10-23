"""夜の問題・解答のHTMLを1問だけ作り、印刷時のクリップを外したPDFのページ数を数える（A4に問題2枚で収まるか）。
使い方: python3 daily-drill/fit_check.py PM-21 [PM-28 ...]"""
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build  # noqa: E402

CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'


def pages(html):
    d = tempfile.mkdtemp()
    hp, pp = os.path.join(d, 'a.html'), os.path.join(d, 'a.pdf')
    open(hp, 'w', encoding='utf-8').write(html.replace('overflow:hidden;height:297mm', 'overflow:visible;height:auto'))
    subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pp}', 'file://' + hp], capture_output=True)
    out = subprocess.run(['pdfinfo', pp], capture_output=True, text=True).stdout
    return int([l for l in out.splitlines() if l.startswith('Pages')][0].split()[1])


ng = 0
for pid in sys.argv[1:]:
    p = json.load(open(os.path.join(HERE, 'evening', 'problems', pid + '.json'), encoding='utf-8'))
    n = pages(build.pm_q(p))
    ok = n == 2
    ng += not ok
    print(('OK ' if ok else 'NG ') + f'{pid} 問題 {n}ページ（2ページであること）')
sys.exit(1 if ng else 0)
