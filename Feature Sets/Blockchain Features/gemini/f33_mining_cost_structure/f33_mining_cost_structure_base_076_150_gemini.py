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


def f33mcs_f33_mining_cost_structure_calc076_65d_base_v076_signal(opinc):
    res = _sma(opinc, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc077_75d_base_v077_signal(opinc):
    res = _sma(opinc, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc078_85d_base_v078_signal(opinc):
    res = _sma(opinc, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc079_95d_base_v079_signal(opinc):
    res = _sma(opinc, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc080_5d_base_v080_signal(opinc):
    res = _sma(opinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc081_15d_base_v081_signal(opinc):
    res = _sma(opinc, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc082_25d_base_v082_signal(opinc):
    res = _sma(opinc, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc083_35d_base_v083_signal(opinc):
    res = _sma(opinc, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc084_45d_base_v084_signal(opinc):
    res = _sma(opinc, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc085_55d_base_v085_signal(opinc):
    res = _sma(opinc, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc086_65d_base_v086_signal(opinc):
    res = _sma(opinc, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc087_75d_base_v087_signal(opinc):
    res = _sma(opinc, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc088_85d_base_v088_signal(opinc):
    res = _sma(opinc, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc089_95d_base_v089_signal(opinc):
    res = _sma(opinc, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc090_5d_base_v090_signal(opinc):
    res = _sma(opinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc091_15d_base_v091_signal(opinc):
    res = _sma(opinc, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc092_25d_base_v092_signal(opinc):
    res = _sma(opinc, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc093_35d_base_v093_signal(opinc):
    res = _sma(opinc, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc094_45d_base_v094_signal(opinc):
    res = _sma(opinc, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc095_55d_base_v095_signal(opinc):
    res = _sma(opinc, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc096_65d_base_v096_signal(opinc):
    res = _sma(opinc, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc097_75d_base_v097_signal(opinc):
    res = _sma(opinc, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc098_85d_base_v098_signal(opinc):
    res = _sma(opinc, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc099_95d_base_v099_signal(opinc):
    res = _sma(opinc, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc100_5d_base_v100_signal(opinc):
    res = _sma(opinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc101_15d_base_v101_signal(opinc):
    res = _sma(opinc, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc102_25d_base_v102_signal(opinc):
    res = _sma(opinc, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc103_35d_base_v103_signal(opinc):
    res = _sma(opinc, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc104_45d_base_v104_signal(opinc):
    res = _sma(opinc, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc105_55d_base_v105_signal(opinc):
    res = _sma(opinc, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc106_65d_base_v106_signal(opinc):
    res = _sma(opinc, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc107_75d_base_v107_signal(opinc):
    res = _sma(opinc, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc108_85d_base_v108_signal(opinc):
    res = _sma(opinc, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc109_95d_base_v109_signal(opinc):
    res = _sma(opinc, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc110_5d_base_v110_signal(opinc):
    res = _sma(opinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc111_15d_base_v111_signal(opinc):
    res = _sma(opinc, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc112_25d_base_v112_signal(opinc):
    res = _sma(opinc, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc113_35d_base_v113_signal(opinc):
    res = _sma(opinc, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc114_45d_base_v114_signal(opinc):
    res = _sma(opinc, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc115_55d_base_v115_signal(opinc):
    res = _sma(opinc, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc116_65d_base_v116_signal(opinc):
    res = _sma(opinc, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc117_75d_base_v117_signal(opinc):
    res = _sma(opinc, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc118_85d_base_v118_signal(opinc):
    res = _sma(opinc, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc119_95d_base_v119_signal(opinc):
    res = _sma(opinc, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc120_5d_base_v120_signal(opinc):
    res = _sma(opinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc121_15d_base_v121_signal(opinc):
    res = _sma(opinc, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc122_25d_base_v122_signal(opinc):
    res = _sma(opinc, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc123_35d_base_v123_signal(opinc):
    res = _sma(opinc, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc124_45d_base_v124_signal(opinc):
    res = _sma(opinc, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc125_55d_base_v125_signal(opinc):
    res = _sma(opinc, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc126_65d_base_v126_signal(opinc):
    res = _sma(opinc, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc127_75d_base_v127_signal(opinc):
    res = _sma(opinc, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc128_85d_base_v128_signal(opinc):
    res = _sma(opinc, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc129_95d_base_v129_signal(opinc):
    res = _sma(opinc, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc130_5d_base_v130_signal(opinc):
    res = _sma(opinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc131_15d_base_v131_signal(opinc):
    res = _sma(opinc, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc132_25d_base_v132_signal(opinc):
    res = _sma(opinc, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc133_35d_base_v133_signal(opinc):
    res = _sma(opinc, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc134_45d_base_v134_signal(opinc):
    res = _sma(opinc, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc135_55d_base_v135_signal(opinc):
    res = _sma(opinc, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc136_65d_base_v136_signal(opinc):
    res = _sma(opinc, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc137_75d_base_v137_signal(opinc):
    res = _sma(opinc, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc138_85d_base_v138_signal(opinc):
    res = _sma(opinc, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc139_95d_base_v139_signal(opinc):
    res = _sma(opinc, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc140_5d_base_v140_signal(opinc):
    res = _sma(opinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc141_15d_base_v141_signal(opinc):
    res = _sma(opinc, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc142_25d_base_v142_signal(opinc):
    res = _sma(opinc, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc143_35d_base_v143_signal(opinc):
    res = _sma(opinc, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc144_45d_base_v144_signal(opinc):
    res = _sma(opinc, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc145_55d_base_v145_signal(opinc):
    res = _sma(opinc, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc146_65d_base_v146_signal(opinc):
    res = _sma(opinc, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc147_75d_base_v147_signal(opinc):
    res = _sma(opinc, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc148_85d_base_v148_signal(opinc):
    res = _sma(opinc, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc149_95d_base_v149_signal(opinc):
    res = _sma(opinc, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc150_5d_base_v150_signal(opinc):
    res = _sma(opinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['opinc', 'revenue', 'ebitda']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f33mcs_'))]
    
    print(f"Testing {{len(funcs)}} functions for f33_mining_cost_structure...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f33mcs_'))]}
