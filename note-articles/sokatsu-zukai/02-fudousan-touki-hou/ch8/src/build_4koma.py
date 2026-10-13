#!/usr/bin/env python3
"""総合記事②不動産登記法編 第8章の4コマ：設計データ（spec_4koma_PG1-*.py）から prompt_4koma_*.md を生成し、check_prompt.py で機械チェックする。
使い方: python3 note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch8/src/build_4koma.py [--check-only | --verify-sync]
- 生成器は tools/drill/manga/gen_prompts.py の render()。一時フォルダに <fid>_prompt.md（単独記事用の節つき）を作って check_prompt.py を通し、
  NG 0件・WARN 0件のときだけ、総合記事に差し込む体裁（記事タイトル・冒頭文・見出し画像・画像ファイル名の節を外し、保存名を足した版）を ../prompt_4koma_*.md に書く。
- 生成物は手で直さない。直すときは spec_4koma_PG1-*.py を直して再生成する。"""
import sys, re, subprocess, tempfile, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
MANGA = ROOT / "tools" / "drill" / "manga"
sys.path.insert(0, str(MANGA)); sys.path.insert(0, str(HERE))
import gen_prompts
from specs_4koma import SPECS

OUT = HERE.parent
NAMES = {  # fid -> (出力ファイル名, 保存名の頭)
    "D1359-D1361": ("prompt_4koma_PG1-1_01_kiyaku-kyouyou-bubun.md", "不登法8章_4コマ1"),
    "D0403-D0986": ("prompt_4koma_PG1-5_01_genin-no-hizuke.md", "不登法8章_4コマ2"),
    "D1588-D1589-D1501": ("prompt_4koma_PG1-5_02_genin-no-bungon.md", "不登法8章_4コマ3"),
    "D2063-D2065": ("prompt_4koma_PG1-6_01_tochi-no-seigen.md", "不登法8章_4コマ4"),
    "D2064": ("prompt_4koma_PG1-7_01_jusho-fuicchi.md", "不登法8章_4コマ5"),
    "D0583": ("prompt_4koma_PG1-9_01_shikichi-nomi-teitouken.md", "不登法8章_4コマ6"),
}

def cut(text, head):
    """'## <head>…' の節を、次の '## ' の直前まで取り除く。"""
    m = re.search(r"^## " + re.escape(head) + r".*?(?=^## )", text, flags=re.S | re.M)
    return text[:m.start()] + text[m.end():] if m else text

def embed(text, sp, fname, savebase):
    lines = text.split("\n", 1)
    head = lines[0]
    body = lines[1]
    note = (
        "\n> **このファイルについて**\n>\n"
        "> - 総合記事②「直前期の苦手論点つぶし 不動産登記法編」第8章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch8.md`）の、論点【" + sp["_stem"].split("_")[2] + "】に差し込む4コマのプロンプトです。"
        "単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/" + sp["_stem"] + ".py` です。\n"
        "> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。\n"
        "> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。\n")
    body = re.sub(r"^- 肢：.*$", f"- 肢：{sp['id']}（{sp['topic']}、出典 {sp['src']}）。正解＝{sp['truth']}。", body, count=1, flags=re.M)
    for h in ["記事タイトル", "note記事の冒頭文", "見出し画像プロンプト", "画像ファイル名"]:
        body = cut(body, h)
    save = (f"## 保存名\n\n- 4コマ（採用版）：`{savebase}_{sp['title']}.png`\n- 途中の版・不採用の版：`{savebase}_{sp['title']}_v01.png`\n\n")
    body = body.replace("## 作成時の品質ゲート", save + "## 作成時の品質ゲート", 1)
    rel = f"note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch8/{fname}"
    body = re.sub(r"`python3 tools/drill/manga/check_prompt.py tools/drill/manga/[^`]*`", f"`python3 tools/drill/manga/check_prompt.py {rel}`", body)
    body = body.replace("## 改訂履歴（このファイルは `manga_specs.py` から生成。直すときは設計データを直して再生成する）",
                        f"## 改訂履歴（このファイルは `src/{sp['_stem']}.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）")
    return head + "\n" + note + body

def main():
    only_check = "--check-only" in sys.argv or "--verify-sync" in sys.argv
    verify_sync = "--verify-sync" in sys.argv
    bad = 0
    for fid, sp in SPECS.items():
        if fid not in NAMES: print("NAMES にない:", fid); bad += 1; continue
        fname, savebase = NAMES[fid]
        full = gen_prompts.render(sp)
        tmp = pathlib.Path(tempfile.mkdtemp()) / f"{fid}_prompt.md"; tmp.write_text(full, encoding="utf8")
        r = subprocess.run([sys.executable, str(MANGA / "check_prompt.py"), str(tmp)], capture_output=True, text=True)
        tail = [l for l in r.stdout.splitlines() if l.startswith(("NG", "WARN", "結果"))]
        print(f"== {fid}"); print("\n".join(tail) if tail else r.stdout[-300:])
        ok = "NG 0件 / WARN 0件" in r.stdout
        if not ok: bad += 1
        if verify_sync:
            if (OUT / fname).read_text(encoding="utf8") != embed(full, sp, fname, savebase):
                print(f"OUT OF SYNC {fname}: 設計データ（src/{sp['_stem']}.py）から作り直した内容と違う"); bad += 1
        if not only_check and ok:
            (OUT / fname).write_text(embed(full, sp, fname, savebase), encoding="utf8"); print("  wrote", fname)
    sys.exit(1 if bad else 0)

main()
