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


def f65lac_f65_liquid_alpha_composite_calc076_65d_base_v076_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 65) * _roc(closeadj, 65) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc077_75d_base_v077_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 75) * _roc(closeadj, 75) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc078_85d_base_v078_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 85) * _roc(closeadj, 85) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc079_95d_base_v079_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 95) * _roc(closeadj, 95) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc080_5d_base_v080_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 5) * _roc(closeadj, 5) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc081_15d_base_v081_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 15) * _roc(closeadj, 15) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc082_25d_base_v082_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 25) * _roc(closeadj, 25) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc083_35d_base_v083_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 35) * _roc(closeadj, 35) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc084_45d_base_v084_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 45) * _roc(closeadj, 45) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc085_55d_base_v085_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 55) * _roc(closeadj, 55) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc086_65d_base_v086_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 65) * _roc(closeadj, 65) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc087_75d_base_v087_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 75) * _roc(closeadj, 75) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc088_85d_base_v088_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 85) * _roc(closeadj, 85) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc089_95d_base_v089_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 95) * _roc(closeadj, 95) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc090_5d_base_v090_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 5) * _roc(closeadj, 5) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc091_15d_base_v091_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 15) * _roc(closeadj, 15) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc092_25d_base_v092_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 25) * _roc(closeadj, 25) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc093_35d_base_v093_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 35) * _roc(closeadj, 35) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc094_45d_base_v094_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 45) * _roc(closeadj, 45) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc095_55d_base_v095_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 55) * _roc(closeadj, 55) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc096_65d_base_v096_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 65) * _roc(closeadj, 65) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc097_75d_base_v097_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 75) * _roc(closeadj, 75) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc098_85d_base_v098_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 85) * _roc(closeadj, 85) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc099_95d_base_v099_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 95) * _roc(closeadj, 95) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc100_5d_base_v100_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 5) * _roc(closeadj, 5) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc101_15d_base_v101_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 15) * _roc(closeadj, 15) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc102_25d_base_v102_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 25) * _roc(closeadj, 25) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc103_35d_base_v103_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 35) * _roc(closeadj, 35) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc104_45d_base_v104_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 45) * _roc(closeadj, 45) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc105_55d_base_v105_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 55) * _roc(closeadj, 55) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc106_65d_base_v106_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 65) * _roc(closeadj, 65) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc107_75d_base_v107_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 75) * _roc(closeadj, 75) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc108_85d_base_v108_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 85) * _roc(closeadj, 85) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc109_95d_base_v109_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 95) * _roc(closeadj, 95) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc110_5d_base_v110_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 5) * _roc(closeadj, 5) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc111_15d_base_v111_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 15) * _roc(closeadj, 15) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc112_25d_base_v112_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 25) * _roc(closeadj, 25) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc113_35d_base_v113_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 35) * _roc(closeadj, 35) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc114_45d_base_v114_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 45) * _roc(closeadj, 45) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc115_55d_base_v115_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 55) * _roc(closeadj, 55) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc116_65d_base_v116_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 65) * _roc(closeadj, 65) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc117_75d_base_v117_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 75) * _roc(closeadj, 75) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc118_85d_base_v118_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 85) * _roc(closeadj, 85) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc119_95d_base_v119_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 95) * _roc(closeadj, 95) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc120_5d_base_v120_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 5) * _roc(closeadj, 5) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc121_15d_base_v121_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 15) * _roc(closeadj, 15) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc122_25d_base_v122_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 25) * _roc(closeadj, 25) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc123_35d_base_v123_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 35) * _roc(closeadj, 35) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc124_45d_base_v124_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 45) * _roc(closeadj, 45) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc125_55d_base_v125_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 55) * _roc(closeadj, 55) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc126_65d_base_v126_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 65) * _roc(closeadj, 65) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc127_75d_base_v127_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 75) * _roc(closeadj, 75) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc128_85d_base_v128_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 85) * _roc(closeadj, 85) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc129_95d_base_v129_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 95) * _roc(closeadj, 95) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc130_5d_base_v130_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 5) * _roc(closeadj, 5) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc131_15d_base_v131_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 15) * _roc(closeadj, 15) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc132_25d_base_v132_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 25) * _roc(closeadj, 25) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc133_35d_base_v133_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 35) * _roc(closeadj, 35) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc134_45d_base_v134_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 45) * _roc(closeadj, 45) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc135_55d_base_v135_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 55) * _roc(closeadj, 55) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc136_65d_base_v136_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 65) * _roc(closeadj, 65) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc137_75d_base_v137_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 75) * _roc(closeadj, 75) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc138_85d_base_v138_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 85) * _roc(closeadj, 85) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc139_95d_base_v139_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 95) * _roc(closeadj, 95) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc140_5d_base_v140_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 5) * _roc(closeadj, 5) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc141_15d_base_v141_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 15) * _roc(closeadj, 15) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc142_25d_base_v142_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 25) * _roc(closeadj, 25) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc143_35d_base_v143_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 35) * _roc(closeadj, 35) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc144_45d_base_v144_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 45) * _roc(closeadj, 45) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc145_55d_base_v145_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 55) * _roc(closeadj, 55) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc146_65d_base_v146_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 65) * _roc(closeadj, 65) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc147_75d_base_v147_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 75) * _roc(closeadj, 75) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc148_85d_base_v148_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 85) * _roc(closeadj, 85) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc149_95d_base_v149_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 95) * _roc(closeadj, 95) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

def f65lac_f65_liquid_alpha_composite_calc150_5d_base_v150_signal(closeadj, revenue, sf3a_value):
    res = (_roc(revenue, 5) * _roc(closeadj, 5) * sf3a_value)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['closeadj', 'volume', 'revenue', 'sf3a_value']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f65lac_'))]
    
    print(f"Testing {len(funcs)} functions for f65_liquid_alpha_composite...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{func.__name__} must return a Series"
        assert not res.isna().all(), f"{func.__name__} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f65lac_'))]}
