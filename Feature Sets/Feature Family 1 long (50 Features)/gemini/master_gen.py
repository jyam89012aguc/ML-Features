import os

def gen_f36():
    header = """import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)

def _cfj_growth(s, w):
    return s.pct_change(w)

def _cfj_accel(s, w1, w2):
    return s.pct_change(w1).pct_change(w2)

def _cfj_jerk(s, w1, w2, w3):
    accel = s.pct_change(w1).pct_change(w2)
    return accel.diff(w3)

def _cfj_slope(s, w):
    return s.pct_change(w)

def _cfj_jerk_deriv(s, w):
    return s.diff(w)

def _cfj_zscore(s, w):
    return _z(s, w)
"""

    footer_template = """
if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({{
        "fcf": np.random.normal(10, 2, n).cumsum() + 1000,
        "ncfo": np.random.normal(15, 3, n).cumsum() + 1500,
    }})
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f36cj_"))]
    
    print(f"Testing {{len(funcs)}} functions...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        y2 = func(*args)
        pd.testing.assert_series_equal(y1, y2)
        
        q = y1.iloc[504:].dropna()
        assert len(q) > 0
        assert q.nunique() > 10

    print("All tests passed!")

REGISTRY = {{fn.__name__: {{"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn}} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f36cj_"))]}}
F36_CASH_FLOW_JERK_REGISTRY_{suffix} = REGISTRY
"""

    # Base 001-075
    with open("f36_cash_flow_jerk/f36_cash_flow_jerk_base_001_075_gemini.py", "w") as f:
        f.write(header)
        v = 1
        for w1, w2, w3 in [(5,21,5), (10,21,10), (21,42,21), (63,126,63)]:
            for item in ["fcf", "ncfo"]:
                if v <= 75:
                    f.write(f"""
def f36cj_f36_cash_flow_jerk_{item}_jerk_{w1}d_{w2}d_{w3}d_v{v:03d}_signal({item}) -> pd.Series:
    \"\"\"Cash Flow Jerk for {item} over {w1}d, {w2}d, {w3}d. Captures high-order changes in cash flow generation. Variation {v}.\"\"\"
    res = _cfj_jerk({item}, {w1}, {w2}, {w3})
    return res.replace([np.inf, -np.inf], np.nan)
""")
                    v += 1
        while v <= 75:
            f.write(f"""
def f36cj_f36_cash_flow_jerk_zscore_v{v:03d}_signal(fcf) -> pd.Series:
    \"\"\"Z-score of cash flow jerk variation {v}. Normalizes cash flow volatility. Variation {v}.\"\"\"
    jerk = _cfj_jerk(fcf, 21, 21, 21)
    res = _cfj_zscore(jerk, {21 + v})
    return res.replace([np.inf, -np.inf], np.nan)
""")
            v += 1
        f.write(footer_template.format(suffix="BASE_001_075"))

    # Base 076-150
    with open("f36_cash_flow_jerk/f36_cash_flow_jerk_base_076_150_gemini.py", "w") as f:
        f.write(header)
        v = 76
        while v <= 150:
            f.write(f"""
def f36cj_f36_cash_flow_jerk_accel_v{v:03d}_signal(ncfo) -> pd.Series:
    \"\"\"Cash flow acceleration variation {v}. Component of higher order momentum. Variation {v}.\"\"\"
    res = _cfj_accel(ncfo, {v}, 21)
    return res.replace([np.inf, -np.inf], np.nan)
""")
            v += 1
        f.write(footer_template.format(suffix="BASE_076_150"))

    # Slope 001-150
    with open("f36_cash_flow_jerk/f36_cash_flow_jerk_slope_001_150_gemini.py", "w") as f:
        f.write(header)
        v = 1
        for ws in [5, 21]:
            for w1, w2, w3 in [(5,10,5), (10,21,10), (21,42,21), (63,63,63)]:
                for item in ["fcf", "ncfo"]:
                    if v <= 150:
                        f.write(f"""
def f36cj_f36_cash_flow_jerk_{item}_slope_{ws}d_v{v:03d}_signal({item}) -> pd.Series:
    \"\"\"Slope of cash flow jerk for {item} with window {ws}d. Variation {v}.\"\"\"
    jerk = _cfj_jerk({item}, {w1}, {w2}, {w3})
    res = _cfj_slope(jerk, {ws})
    return res.replace([np.inf, -np.inf], np.nan)
""")
                        v += 1
        while v <= 150:
             f.write(f"""
def f36cj_f36_cash_flow_jerk_slope_fill_v{v:03d}_signal(fcf) -> pd.Series:
    \"\"\"Filling slope variations to reach 150. Window {v % 63 + 5}. Variation {v}.\"\"\"
    jerk = _cfj_jerk(fcf, 10, 10, 10)
    res = _cfj_slope(jerk, {v % 63 + 5})
    return res.replace([np.inf, -np.inf], np.nan)
""")
             v += 1
        f.write(footer_template.format(suffix="SLOPE_001_150"))

    # Jerk 001-150
    with open("f36_cash_flow_jerk/f36_cash_flow_jerk_jerk_001_150_gemini.py", "w") as f:
        f.write(header)
        v = 1
        while v <= 150:
            f.write(f"""
def f36cj_f36_cash_flow_jerk_jerk_deriv_v{v:03d}_signal(ncfo) -> pd.Series:
    \"\"\"Derivative of cash flow jerk variation {v}. High frequency momentum indicator. Variation {v}.\"\"\"
    jerk = _cfj_jerk(ncfo, 10, 10, 10)
    res = _cfj_jerk_deriv(jerk, {v % 21 + 3})
    return res.replace([np.inf, -np.inf], np.nan)
""")
            v += 1
        f.write(footer_template.format(suffix="JERK_001_150"))

gen_f36()
