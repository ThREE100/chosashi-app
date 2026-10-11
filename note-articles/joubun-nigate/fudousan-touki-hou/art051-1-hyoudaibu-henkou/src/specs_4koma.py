# 不動産登記法 第51条第1項：4コマ4本の設計データの読み込み口。各本の設計データは spec_4koma_NN.py（SPEC と HEADER）。
# 生成は tools/drill/manga/gen_prompts.py の render(spec)（mainブランチ）。再生成は note-articles/joubun-nigate/ の README と tools/drill/manga/MANGA_RULES.md を参照。
import importlib.util, pathlib
HERE = pathlib.Path(__file__).resolve().parent
SPECS = {}
for _p in sorted(HERE.glob("spec_4koma_0*.py")):
    _sp = importlib.util.spec_from_file_location(_p.stem, _p); _m = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(_m)
    _s = _m.SPEC; _s["header"] = _m.HEADER
    SPECS[_s["fid"]] = _s
