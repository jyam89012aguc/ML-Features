import inspect
import pandas as pd
import numpy as np

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()

def _std(s, w):
    return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()

def _roc(s, w):
    return s.pct_change(w)

def _zscore(s, w):
    return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)


def f56prj_f56_protocol_revenue_jerk_calc076_65d_base_v076_signal(revenue):
    res = _roc(_roc(revenue, 65), 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc077_75d_base_v077_signal(revenue):
    res = _roc(_roc(revenue, 75), 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc078_85d_base_v078_signal(revenue):
    res = _roc(_roc(revenue, 85), 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc079_95d_base_v079_signal(revenue):
    res = _roc(_roc(revenue, 95), 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc080_5d_base_v080_signal(revenue):
    res = _roc(_roc(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc081_15d_base_v081_signal(revenue):
    res = _roc(_roc(revenue, 15), 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc082_25d_base_v082_signal(revenue):
    res = _roc(_roc(revenue, 25), 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc083_35d_base_v083_signal(revenue):
    res = _roc(_roc(revenue, 35), 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc084_45d_base_v084_signal(revenue):
    res = _roc(_roc(revenue, 45), 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc085_55d_base_v085_signal(revenue):
    res = _roc(_roc(revenue, 55), 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc086_65d_base_v086_signal(revenue):
    res = _roc(_roc(revenue, 65), 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc087_75d_base_v087_signal(revenue):
    res = _roc(_roc(revenue, 75), 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc088_85d_base_v088_signal(revenue):
    res = _roc(_roc(revenue, 85), 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc089_95d_base_v089_signal(revenue):
    res = _roc(_roc(revenue, 95), 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc090_5d_base_v090_signal(revenue):
    res = _roc(_roc(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc091_15d_base_v091_signal(revenue):
    res = _roc(_roc(revenue, 15), 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc092_25d_base_v092_signal(revenue):
    res = _roc(_roc(revenue, 25), 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc093_35d_base_v093_signal(revenue):
    res = _roc(_roc(revenue, 35), 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc094_45d_base_v094_signal(revenue):
    res = _roc(_roc(revenue, 45), 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc095_55d_base_v095_signal(revenue):
    res = _roc(_roc(revenue, 55), 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc096_65d_base_v096_signal(revenue):
    res = _roc(_roc(revenue, 65), 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc097_75d_base_v097_signal(revenue):
    res = _roc(_roc(revenue, 75), 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc098_85d_base_v098_signal(revenue):
    res = _roc(_roc(revenue, 85), 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc099_95d_base_v099_signal(revenue):
    res = _roc(_roc(revenue, 95), 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc100_5d_base_v100_signal(revenue):
    res = _roc(_roc(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc101_15d_base_v101_signal(revenue):
    res = _roc(_roc(revenue, 15), 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc102_25d_base_v102_signal(revenue):
    res = _roc(_roc(revenue, 25), 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc103_35d_base_v103_signal(revenue):
    res = _roc(_roc(revenue, 35), 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc104_45d_base_v104_signal(revenue):
    res = _roc(_roc(revenue, 45), 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc105_55d_base_v105_signal(revenue):
    res = _roc(_roc(revenue, 55), 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc106_65d_base_v106_signal(revenue):
    res = _roc(_roc(revenue, 65), 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc107_75d_base_v107_signal(revenue):
    res = _roc(_roc(revenue, 75), 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc108_85d_base_v108_signal(revenue):
    res = _roc(_roc(revenue, 85), 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc109_95d_base_v109_signal(revenue):
    res = _roc(_roc(revenue, 95), 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc110_5d_base_v110_signal(revenue):
    res = _roc(_roc(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc111_15d_base_v111_signal(revenue):
    res = _roc(_roc(revenue, 15), 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc112_25d_base_v112_signal(revenue):
    res = _roc(_roc(revenue, 25), 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc113_35d_base_v113_signal(revenue):
    res = _roc(_roc(revenue, 35), 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc114_45d_base_v114_signal(revenue):
    res = _roc(_roc(revenue, 45), 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc115_55d_base_v115_signal(revenue):
    res = _roc(_roc(revenue, 55), 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc116_65d_base_v116_signal(revenue):
    res = _roc(_roc(revenue, 65), 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc117_75d_base_v117_signal(revenue):
    res = _roc(_roc(revenue, 75), 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc118_85d_base_v118_signal(revenue):
    res = _roc(_roc(revenue, 85), 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc119_95d_base_v119_signal(revenue):
    res = _roc(_roc(revenue, 95), 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc120_5d_base_v120_signal(revenue):
    res = _roc(_roc(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc121_15d_base_v121_signal(revenue):
    res = _roc(_roc(revenue, 15), 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc122_25d_base_v122_signal(revenue):
    res = _roc(_roc(revenue, 25), 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc123_35d_base_v123_signal(revenue):
    res = _roc(_roc(revenue, 35), 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc124_45d_base_v124_signal(revenue):
    res = _roc(_roc(revenue, 45), 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc125_55d_base_v125_signal(revenue):
    res = _roc(_roc(revenue, 55), 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc126_65d_base_v126_signal(revenue):
    res = _roc(_roc(revenue, 65), 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc127_75d_base_v127_signal(revenue):
    res = _roc(_roc(revenue, 75), 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc128_85d_base_v128_signal(revenue):
    res = _roc(_roc(revenue, 85), 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc129_95d_base_v129_signal(revenue):
    res = _roc(_roc(revenue, 95), 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc130_5d_base_v130_signal(revenue):
    res = _roc(_roc(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc131_15d_base_v131_signal(revenue):
    res = _roc(_roc(revenue, 15), 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc132_25d_base_v132_signal(revenue):
    res = _roc(_roc(revenue, 25), 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc133_35d_base_v133_signal(revenue):
    res = _roc(_roc(revenue, 35), 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc134_45d_base_v134_signal(revenue):
    res = _roc(_roc(revenue, 45), 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc135_55d_base_v135_signal(revenue):
    res = _roc(_roc(revenue, 55), 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc136_65d_base_v136_signal(revenue):
    res = _roc(_roc(revenue, 65), 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc137_75d_base_v137_signal(revenue):
    res = _roc(_roc(revenue, 75), 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc138_85d_base_v138_signal(revenue):
    res = _roc(_roc(revenue, 85), 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc139_95d_base_v139_signal(revenue):
    res = _roc(_roc(revenue, 95), 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc140_5d_base_v140_signal(revenue):
    res = _roc(_roc(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc141_15d_base_v141_signal(revenue):
    res = _roc(_roc(revenue, 15), 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc142_25d_base_v142_signal(revenue):
    res = _roc(_roc(revenue, 25), 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc143_35d_base_v143_signal(revenue):
    res = _roc(_roc(revenue, 35), 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc144_45d_base_v144_signal(revenue):
    res = _roc(_roc(revenue, 45), 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc145_55d_base_v145_signal(revenue):
    res = _roc(_roc(revenue, 55), 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc146_65d_base_v146_signal(revenue):
    res = _roc(_roc(revenue, 65), 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc147_75d_base_v147_signal(revenue):
    res = _roc(_roc(revenue, 75), 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc148_85d_base_v148_signal(revenue):
    res = _roc(_roc(revenue, 85), 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc149_95d_base_v149_signal(revenue):
    res = _roc(_roc(revenue, 95), 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f56prj_f56_protocol_revenue_jerk_calc150_5d_base_v150_signal(revenue):
    res = _roc(_roc(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['revenue', 'netinc', 'assets']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f56prj_'))]
    
    print(f"Testing {len(funcs)} functions for f56_protocol_revenue_jerk...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{func.__name__} must return a Series"
        assert not res.isna().all(), f"{func.__name__} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f56prj_'))]}
