import os

family = "f007_liabilities_coverage"
args = "cashneq, investmentsc, liabilities, liabilitiesc"
bases = [
    "cashneq",
    "investmentsc",
    "liabilities",
    "liabilitiesc",
    "_safe_div(cashneq, liabilities)",
    "_safe_div(cashneq, liabilitiesc)",
    "_safe_div(investmentsc, liabilities)",
    "_safe_div(investmentsc, liabilitiesc)",
    "_safe_div(cashneq + investmentsc, liabilities)",
    "_safe_div(cashneq + investmentsc, liabilitiesc)"
]

patterns = [
    lambda b: f"_diff(_diff({b}, 4), 4)",
    lambda b: f"_slope(_diff({b}, 4), 8)",
    lambda b: f"_diff(_slope({b}, 4), 4)",
    lambda b: f"_z(_diff(_diff({b}, 4), 4), 8)",
    lambda b: f"_z(_slope(_diff({b}, 4), 8), 12)",
    lambda b: f"_z(_diff(_slope({b}, 4), 4), 8)",
    lambda b: f"_rank(_diff(_diff({b}, 4), 4), 12)",
    lambda b: f"_rank(_slope(_diff({b}, 4), 8), 12)",
    lambda b: f"_rank(_diff(_slope({b}, 4), 4), 12)",
    lambda b: f"_mean(_diff(_diff({b}, 4), 4), 4)",
    lambda b: f"_mean(_slope(_diff({b}, 4), 8), 4)",
    lambda b: f"_mean(_diff(_slope({b}, 4), 4), 4)",
    lambda b: f"_slope(_diff(_diff({b}, 4), 4), 4)",
    lambda b: f"_diff(_diff(_diff({b}, 4), 4), 4)",
    lambda b: f"_z(_slope(_diff(_diff({b}, 4), 4), 4), 8)"
]

header = """import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z
"""

output = [header]

count = 0
for p_idx, p in enumerate(patterns):
    for b_idx, b in enumerate(bases):
        count += 1
        func_name = f"cg_{family}_core{count-1:02}_3rd_v{count:03}_signal"
        expr = p(b)
        output.append(f"def {func_name}({args}):\n    return _clean({expr})")

with open(f"{family}_3rd_derivatives_001_150_gemini.py", "w") as f:
    f.write("\n".join(output))
