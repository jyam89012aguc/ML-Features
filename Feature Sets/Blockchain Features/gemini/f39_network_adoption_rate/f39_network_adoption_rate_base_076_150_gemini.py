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


def f39nar_f39_network_adoption_rate_calc076_65d_base_v076_signal(revenue):
    res = _sma(revenue, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc077_75d_base_v077_signal(revenue):
    res = _sma(revenue, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc078_85d_base_v078_signal(revenue):
    res = _sma(revenue, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc079_95d_base_v079_signal(revenue):
    res = _sma(revenue, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc080_5d_base_v080_signal(revenue):
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc081_15d_base_v081_signal(revenue):
    res = _sma(revenue, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc082_25d_base_v082_signal(revenue):
    res = _sma(revenue, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc083_35d_base_v083_signal(revenue):
    res = _sma(revenue, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc084_45d_base_v084_signal(revenue):
    res = _sma(revenue, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc085_55d_base_v085_signal(revenue):
    res = _sma(revenue, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc086_65d_base_v086_signal(revenue):
    res = _sma(revenue, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc087_75d_base_v087_signal(revenue):
    res = _sma(revenue, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc088_85d_base_v088_signal(revenue):
    res = _sma(revenue, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc089_95d_base_v089_signal(revenue):
    res = _sma(revenue, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc090_5d_base_v090_signal(revenue):
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc091_15d_base_v091_signal(revenue):
    res = _sma(revenue, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc092_25d_base_v092_signal(revenue):
    res = _sma(revenue, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc093_35d_base_v093_signal(revenue):
    res = _sma(revenue, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc094_45d_base_v094_signal(revenue):
    res = _sma(revenue, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc095_55d_base_v095_signal(revenue):
    res = _sma(revenue, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc096_65d_base_v096_signal(revenue):
    res = _sma(revenue, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc097_75d_base_v097_signal(revenue):
    res = _sma(revenue, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc098_85d_base_v098_signal(revenue):
    res = _sma(revenue, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc099_95d_base_v099_signal(revenue):
    res = _sma(revenue, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc100_5d_base_v100_signal(revenue):
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc101_15d_base_v101_signal(revenue):
    res = _sma(revenue, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc102_25d_base_v102_signal(revenue):
    res = _sma(revenue, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc103_35d_base_v103_signal(revenue):
    res = _sma(revenue, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc104_45d_base_v104_signal(revenue):
    res = _sma(revenue, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc105_55d_base_v105_signal(revenue):
    res = _sma(revenue, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc106_65d_base_v106_signal(revenue):
    res = _sma(revenue, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc107_75d_base_v107_signal(revenue):
    res = _sma(revenue, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc108_85d_base_v108_signal(revenue):
    res = _sma(revenue, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc109_95d_base_v109_signal(revenue):
    res = _sma(revenue, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc110_5d_base_v110_signal(revenue):
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc111_15d_base_v111_signal(revenue):
    res = _sma(revenue, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc112_25d_base_v112_signal(revenue):
    res = _sma(revenue, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc113_35d_base_v113_signal(revenue):
    res = _sma(revenue, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc114_45d_base_v114_signal(revenue):
    res = _sma(revenue, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc115_55d_base_v115_signal(revenue):
    res = _sma(revenue, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc116_65d_base_v116_signal(revenue):
    res = _sma(revenue, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc117_75d_base_v117_signal(revenue):
    res = _sma(revenue, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc118_85d_base_v118_signal(revenue):
    res = _sma(revenue, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc119_95d_base_v119_signal(revenue):
    res = _sma(revenue, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc120_5d_base_v120_signal(revenue):
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc121_15d_base_v121_signal(revenue):
    res = _sma(revenue, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc122_25d_base_v122_signal(revenue):
    res = _sma(revenue, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc123_35d_base_v123_signal(revenue):
    res = _sma(revenue, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc124_45d_base_v124_signal(revenue):
    res = _sma(revenue, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc125_55d_base_v125_signal(revenue):
    res = _sma(revenue, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc126_65d_base_v126_signal(revenue):
    res = _sma(revenue, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc127_75d_base_v127_signal(revenue):
    res = _sma(revenue, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc128_85d_base_v128_signal(revenue):
    res = _sma(revenue, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc129_95d_base_v129_signal(revenue):
    res = _sma(revenue, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc130_5d_base_v130_signal(revenue):
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc131_15d_base_v131_signal(revenue):
    res = _sma(revenue, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc132_25d_base_v132_signal(revenue):
    res = _sma(revenue, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc133_35d_base_v133_signal(revenue):
    res = _sma(revenue, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc134_45d_base_v134_signal(revenue):
    res = _sma(revenue, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc135_55d_base_v135_signal(revenue):
    res = _sma(revenue, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc136_65d_base_v136_signal(revenue):
    res = _sma(revenue, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc137_75d_base_v137_signal(revenue):
    res = _sma(revenue, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc138_85d_base_v138_signal(revenue):
    res = _sma(revenue, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc139_95d_base_v139_signal(revenue):
    res = _sma(revenue, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc140_5d_base_v140_signal(revenue):
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc141_15d_base_v141_signal(revenue):
    res = _sma(revenue, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc142_25d_base_v142_signal(revenue):
    res = _sma(revenue, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc143_35d_base_v143_signal(revenue):
    res = _sma(revenue, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc144_45d_base_v144_signal(revenue):
    res = _sma(revenue, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc145_55d_base_v145_signal(revenue):
    res = _sma(revenue, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc146_65d_base_v146_signal(revenue):
    res = _sma(revenue, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc147_75d_base_v147_signal(revenue):
    res = _sma(revenue, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc148_85d_base_v148_signal(revenue):
    res = _sma(revenue, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc149_95d_base_v149_signal(revenue):
    res = _sma(revenue, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f39nar_f39_network_adoption_rate_calc150_5d_base_v150_signal(revenue):
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['revenue', 'assets', 'workingcapital']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f39nar_'))]
    
    print(f"Testing {{len(funcs)}} functions for f39_network_adoption_rate...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f39nar_'))]}
