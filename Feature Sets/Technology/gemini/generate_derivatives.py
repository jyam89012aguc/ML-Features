import os

def generate_signals(family, args, bases, derivatives_type):
    if derivatives_type == "2nd":
        patterns = [
            lambda b: f"_slope({b}, 4)",
            lambda b: f"_slope({b}, 8)",
            lambda b: f"_diff({b}, 4)",
            lambda b: f"_z(_slope({b}, 4), 8)",
            lambda b: f"_z(_slope({b}, 8), 12)",
            lambda b: f"_z(_diff({b}, 4), 8)",
            lambda b: f"_rank(_slope({b}, 4), 12)",
            lambda b: f"_rank(_diff({b}, 4), 12)",
            lambda b: f"_mean(_slope({b}, 4), 4)",
            lambda b: f"_mean(_diff({b}, 4), 4)",
            lambda b: f"_slope(_mean({b}, 4), 4)",
            lambda b: f"_slope(_mean({b}, 8), 8)",
            lambda b: f"_diff(_mean({b}, 4), 4)",
            lambda b: f"_z(_diff(_mean({b}, 4), 4), 8)",
            lambda b: f"_rank(_slope(_mean({b}, 4), 4), 12)"
        ]
        suffix = "2nd"
    elif derivatives_type == "3rd":
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
        suffix = "3rd"
    else:
        raise ValueError("derivatives_type must be 2nd or 3rd")

    header = """import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z
"""
    output = [header]
    count = 0
    while len(bases) < 10:
        bases.append(bases[len(bases) % len(bases)])

    for p in patterns:
        for b in bases:
            count += 1
            if count > 150: break
            func_name = f"cg_{family}_core{count-1:02}_{suffix}_v{count:03}_signal"
            expr = p(b)
            output.append(f"def {func_name}({args}):\n    return _clean({expr})")
        if count > 150: break

    filename = f"{family}_{suffix}_derivatives_001_150_gemini.py"
    with open(filename, "w") as f:
        f.write("\n".join(output))
    print(f"Generated {filename}")

# f012_operating_cash_quality
bases_f012 = [
    "ncfo", "netinc", "depamor", "sbcomp",
    "_safe_div(ncfo, netinc)", # Accrual quality
    "ncfo - netinc",
    "_safe_div(ncfo, netinc + depamor)", # Cash flow coverage of earnings + non-cash
    "_safe_div(sbcomp, ncfo.abs() + 1.0)", # SBC intensity in cash flow
    "_safe_div(depamor, ncfo.abs() + 1.0)",
    "netinc + depamor + sbcomp" # Proxy for cash earnings
]
generate_signals("f012_operating_cash_quality", "ncfo, netinc, depamor, sbcomp", bases_f012, "2nd")
generate_signals("f012_operating_cash_quality", "ncfo, netinc, depamor, sbcomp", bases_f012, "3rd")
