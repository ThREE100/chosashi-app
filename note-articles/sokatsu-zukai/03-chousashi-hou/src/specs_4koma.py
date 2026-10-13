# 総合記事③ 土地家屋調査士法編：4コマ5本の設計データの読み込み口。各本の設計データは spec_4koma_C1-N_NN.py（SPEC と HEADER）。
# 生成は tools/drill/manga/gen_prompts.py の render(spec)。build_4koma.py が生成・機械チェック・体裁の変換を行う。
import importlib.util, pathlib
HERE = pathlib.Path(__file__).resolve().parent
SPECS = {}
for _p in sorted(HERE.glob("spec_4koma_C1-*.py")):
    _sp = importlib.util.spec_from_file_location(_p.stem.replace("-", "_"), _p); _m = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(_m)
    _s = _m.SPEC; _s["header"] = _m.HEADER; _s["_stem"] = _p.stem
    SPECS[_s["fid"]] = _s
