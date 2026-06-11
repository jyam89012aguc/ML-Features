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


def f35tinf_f35_tokenomics_inflation_calc076_65d_base_v076_signal(sharesbas):
    res = _sma(sharesbas, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc077_75d_base_v077_signal(sharesbas):
    res = _sma(sharesbas, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc078_85d_base_v078_signal(sharesbas):
    res = _sma(sharesbas, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc079_95d_base_v079_signal(sharesbas):
    res = _sma(sharesbas, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc080_5d_base_v080_signal(sharesbas):
    res = _sma(sharesbas, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc081_15d_base_v081_signal(sharesbas):
    res = _sma(sharesbas, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc082_25d_base_v082_signal(sharesbas):
    res = _sma(sharesbas, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc083_35d_base_v083_signal(sharesbas):
    res = _sma(sharesbas, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc084_45d_base_v084_signal(sharesbas):
    res = _sma(sharesbas, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc085_55d_base_v085_signal(sharesbas):
    res = _sma(sharesbas, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc086_65d_base_v086_signal(sharesbas):
    res = _sma(sharesbas, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc087_75d_base_v087_signal(sharesbas):
    res = _sma(sharesbas, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc088_85d_base_v088_signal(sharesbas):
    res = _sma(sharesbas, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc089_95d_base_v089_signal(sharesbas):
    res = _sma(sharesbas, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc090_5d_base_v090_signal(sharesbas):
    res = _sma(sharesbas, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc091_15d_base_v091_signal(sharesbas):
    res = _sma(sharesbas, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc092_25d_base_v092_signal(sharesbas):
    res = _sma(sharesbas, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc093_35d_base_v093_signal(sharesbas):
    res = _sma(sharesbas, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc094_45d_base_v094_signal(sharesbas):
    res = _sma(sharesbas, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc095_55d_base_v095_signal(sharesbas):
    res = _sma(sharesbas, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc096_65d_base_v096_signal(sharesbas):
    res = _sma(sharesbas, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc097_75d_base_v097_signal(sharesbas):
    res = _sma(sharesbas, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc098_85d_base_v098_signal(sharesbas):
    res = _sma(sharesbas, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc099_95d_base_v099_signal(sharesbas):
    res = _sma(sharesbas, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc100_5d_base_v100_signal(sharesbas):
    res = _sma(sharesbas, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc101_15d_base_v101_signal(sharesbas):
    res = _sma(sharesbas, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc102_25d_base_v102_signal(sharesbas):
    res = _sma(sharesbas, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc103_35d_base_v103_signal(sharesbas):
    res = _sma(sharesbas, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc104_45d_base_v104_signal(sharesbas):
    res = _sma(sharesbas, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc105_55d_base_v105_signal(sharesbas):
    res = _sma(sharesbas, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc106_65d_base_v106_signal(sharesbas):
    res = _sma(sharesbas, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc107_75d_base_v107_signal(sharesbas):
    res = _sma(sharesbas, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc108_85d_base_v108_signal(sharesbas):
    res = _sma(sharesbas, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc109_95d_base_v109_signal(sharesbas):
    res = _sma(sharesbas, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc110_5d_base_v110_signal(sharesbas):
    res = _sma(sharesbas, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc111_15d_base_v111_signal(sharesbas):
    res = _sma(sharesbas, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc112_25d_base_v112_signal(sharesbas):
    res = _sma(sharesbas, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc113_35d_base_v113_signal(sharesbas):
    res = _sma(sharesbas, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc114_45d_base_v114_signal(sharesbas):
    res = _sma(sharesbas, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc115_55d_base_v115_signal(sharesbas):
    res = _sma(sharesbas, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc116_65d_base_v116_signal(sharesbas):
    res = _sma(sharesbas, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc117_75d_base_v117_signal(sharesbas):
    res = _sma(sharesbas, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc118_85d_base_v118_signal(sharesbas):
    res = _sma(sharesbas, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc119_95d_base_v119_signal(sharesbas):
    res = _sma(sharesbas, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc120_5d_base_v120_signal(sharesbas):
    res = _sma(sharesbas, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc121_15d_base_v121_signal(sharesbas):
    res = _sma(sharesbas, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc122_25d_base_v122_signal(sharesbas):
    res = _sma(sharesbas, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc123_35d_base_v123_signal(sharesbas):
    res = _sma(sharesbas, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc124_45d_base_v124_signal(sharesbas):
    res = _sma(sharesbas, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc125_55d_base_v125_signal(sharesbas):
    res = _sma(sharesbas, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc126_65d_base_v126_signal(sharesbas):
    res = _sma(sharesbas, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc127_75d_base_v127_signal(sharesbas):
    res = _sma(sharesbas, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc128_85d_base_v128_signal(sharesbas):
    res = _sma(sharesbas, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc129_95d_base_v129_signal(sharesbas):
    res = _sma(sharesbas, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc130_5d_base_v130_signal(sharesbas):
    res = _sma(sharesbas, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc131_15d_base_v131_signal(sharesbas):
    res = _sma(sharesbas, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc132_25d_base_v132_signal(sharesbas):
    res = _sma(sharesbas, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc133_35d_base_v133_signal(sharesbas):
    res = _sma(sharesbas, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc134_45d_base_v134_signal(sharesbas):
    res = _sma(sharesbas, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc135_55d_base_v135_signal(sharesbas):
    res = _sma(sharesbas, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc136_65d_base_v136_signal(sharesbas):
    res = _sma(sharesbas, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc137_75d_base_v137_signal(sharesbas):
    res = _sma(sharesbas, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc138_85d_base_v138_signal(sharesbas):
    res = _sma(sharesbas, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc139_95d_base_v139_signal(sharesbas):
    res = _sma(sharesbas, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc140_5d_base_v140_signal(sharesbas):
    res = _sma(sharesbas, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc141_15d_base_v141_signal(sharesbas):
    res = _sma(sharesbas, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc142_25d_base_v142_signal(sharesbas):
    res = _sma(sharesbas, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc143_35d_base_v143_signal(sharesbas):
    res = _sma(sharesbas, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc144_45d_base_v144_signal(sharesbas):
    res = _sma(sharesbas, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc145_55d_base_v145_signal(sharesbas):
    res = _sma(sharesbas, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc146_65d_base_v146_signal(sharesbas):
    res = _sma(sharesbas, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc147_75d_base_v147_signal(sharesbas):
    res = _sma(sharesbas, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc148_85d_base_v148_signal(sharesbas):
    res = _sma(sharesbas, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc149_95d_base_v149_signal(sharesbas):
    res = _sma(sharesbas, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc150_5d_base_v150_signal(sharesbas):
    res = _sma(sharesbas, 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['sharesbas', 'revenue', 'equity']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f35tinf_'))]
    
    print(f"Testing {{len(funcs)}} functions for f35_tokenomics_inflation...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f35tinf_'))]}
