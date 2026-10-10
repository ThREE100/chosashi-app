#!/usr/bin/env python3
"""設計データ（SPEC と HEADER を定義した *_spec.py）から <fid>_prompt.md を作り、check_prompt.py を実行する。
manga_specs.py に登録していない肢・条文の4コマ（2026-10-10 以降に追加した D1578ほか、joubun/ 配下）の再生成に使う。
使い方: python3 tools/drill/manga/render_spec.py <spec.py> [出力フォルダ（省略時は spec.py と同じ）]
注意: 生成した md の先頭に付いている「このファイルについて」の注記（条文版）は生成器が作らないので、再生成後に手で戻す。"""
import sys, pathlib, subprocess, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
spec_path = pathlib.Path(sys.argv[1]).resolve()
outdir = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else spec_path.parent
outdir.mkdir(parents=True, exist_ok=True)
sp = importlib.util.spec_from_file_location("sp", spec_path); mod = importlib.util.module_from_spec(sp); sp.loader.exec_module(mod)
import manga_specs, gen_prompts
S = mod.SPEC; S["header"] = mod.HEADER
manga_specs.SPECS[S["fid"]] = S
out = outdir / f"{S['fid']}_prompt.md"
out.write_text(gen_prompts.render(S), encoding="utf8")
r = subprocess.run([sys.executable, str(HERE / "check_prompt.py"), str(out)], capture_output=True, text=True)
print(out); print(r.stdout[-4000:], r.stderr[-1500:])
