"""実践答練 第2回 択一式の指定をまとめる（specs_a＝第1〜5問、specs_b＝第6〜10問、specs_c＝第11〜15問、specs_d＝第16〜20問）。"""
SPECS = {}
for _name, _var in (("specs_a", "A"), ("specs_b", "B"), ("specs_c", "C"), ("specs_d", "D")):
    try:
        _mod = __import__(_name)
        SPECS.update(getattr(_mod, _var))
    except ImportError:
        pass
