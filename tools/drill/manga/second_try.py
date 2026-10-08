#!/usr/bin/env python3
"""第二案（specs2/<ID>.py の SPEC2）の試し生成と機械チェック。リポジトリのファイルは書き換えない（一時フォルダに出力する）。
使い方: python3 tools/drill/manga/second_try.py D0315 [--show]
- 第一案（manga_specs.py の SPECS[ID]）に specs2/<ID>.py の第二案を付けた <ID>_prompt.md を一時フォルダに作り、check_prompt.py を実行する。
- NG 0件・WARN 0件になるまで specs2/<ID>.py を直す。--show を付けると、第二案の節（構成表2とプロンプト本体2）を表示する。"""
import sys, pathlib, subprocess, tempfile
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import gen_prompts
from manga_specs import SPECS

def main():
    ids = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not ids: print(__doc__); sys.exit(2)
    i = ids[0]
    if i not in SPECS: print(f"SPECS に {i} がない"); sys.exit(2)
    if i not in gen_prompts.SECOND: print(f"specs2/{i}.py（SPEC2）がない"); sys.exit(2)
    text = gen_prompts.render(SPECS[i])
    d = pathlib.Path(tempfile.mkdtemp()); f = d / f"{i}_prompt.md"; f.write_text(text, encoding="utf8")
    if "--show" in sys.argv:
        print(text[text.find("## 第二案（B案）"):]); print("=" * 60)
    r = subprocess.run([sys.executable, str(HERE / "check_prompt.py"), str(f)], capture_output=True, text=True)
    print(r.stdout, end=""); print(r.stderr, end=""); sys.exit(r.returncode)

main()
