"""実践答練 第2回 択一式の指定をまとめる（第1問〜第10問＝specs_a、第11問〜第20問＝specs_b）。"""
from specs_a import A

SPECS = dict(A)
try:
    from specs_b import B
    SPECS.update(B)
except ImportError:
    pass
