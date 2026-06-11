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


def f38ycm_f38_yield_capture_margins_calc076_65d_base_v076_signal(ebitda):
    res = _sma(ebitda, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc077_75d_base_v077_signal(ebitda):
    res = _sma(ebitda, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc078_85d_base_v078_signal(ebitda):
    res = _sma(ebitda, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc079_95d_base_v079_signal(ebitda):
    res = _sma(ebitda, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc080_5d_base_v080_signal(ebitda):
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc081_15d_base_v081_signal(ebitda):
    res = _sma(ebitda, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc082_25d_base_v082_signal(ebitda):
    res = _sma(ebitda, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc083_35d_base_v083_signal(ebitda):
    res = _sma(ebitda, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc084_45d_base_v084_signal(ebitda):
    res = _sma(ebitda, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc085_55d_base_v085_signal(ebitda):
    res = _sma(ebitda, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc086_65d_base_v086_signal(ebitda):
    res = _sma(ebitda, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc087_75d_base_v087_signal(ebitda):
    res = _sma(ebitda, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc088_85d_base_v088_signal(ebitda):
    res = _sma(ebitda, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc089_95d_base_v089_signal(ebitda):
    res = _sma(ebitda, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc090_5d_base_v090_signal(ebitda):
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc091_15d_base_v091_signal(ebitda):
    res = _sma(ebitda, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc092_25d_base_v092_signal(ebitda):
    res = _sma(ebitda, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc093_35d_base_v093_signal(ebitda):
    res = _sma(ebitda, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc094_45d_base_v094_signal(ebitda):
    res = _sma(ebitda, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc095_55d_base_v095_signal(ebitda):
    res = _sma(ebitda, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc096_65d_base_v096_signal(ebitda):
    res = _sma(ebitda, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc097_75d_base_v097_signal(ebitda):
    res = _sma(ebitda, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc098_85d_base_v098_signal(ebitda):
    res = _sma(ebitda, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc099_95d_base_v099_signal(ebitda):
    res = _sma(ebitda, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc100_5d_base_v100_signal(ebitda):
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc101_15d_base_v101_signal(ebitda):
    res = _sma(ebitda, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc102_25d_base_v102_signal(ebitda):
    res = _sma(ebitda, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc103_35d_base_v103_signal(ebitda):
    res = _sma(ebitda, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc104_45d_base_v104_signal(ebitda):
    res = _sma(ebitda, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc105_55d_base_v105_signal(ebitda):
    res = _sma(ebitda, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc106_65d_base_v106_signal(ebitda):
    res = _sma(ebitda, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc107_75d_base_v107_signal(ebitda):
    res = _sma(ebitda, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc108_85d_base_v108_signal(ebitda):
    res = _sma(ebitda, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc109_95d_base_v109_signal(ebitda):
    res = _sma(ebitda, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc110_5d_base_v110_signal(ebitda):
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc111_15d_base_v111_signal(ebitda):
    res = _sma(ebitda, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc112_25d_base_v112_signal(ebitda):
    res = _sma(ebitda, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc113_35d_base_v113_signal(ebitda):
    res = _sma(ebitda, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc114_45d_base_v114_signal(ebitda):
    res = _sma(ebitda, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc115_55d_base_v115_signal(ebitda):
    res = _sma(ebitda, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc116_65d_base_v116_signal(ebitda):
    res = _sma(ebitda, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc117_75d_base_v117_signal(ebitda):
    res = _sma(ebitda, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc118_85d_base_v118_signal(ebitda):
    res = _sma(ebitda, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc119_95d_base_v119_signal(ebitda):
    res = _sma(ebitda, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc120_5d_base_v120_signal(ebitda):
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc121_15d_base_v121_signal(ebitda):
    res = _sma(ebitda, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc122_25d_base_v122_signal(ebitda):
    res = _sma(ebitda, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc123_35d_base_v123_signal(ebitda):
    res = _sma(ebitda, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc124_45d_base_v124_signal(ebitda):
    res = _sma(ebitda, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc125_55d_base_v125_signal(ebitda):
    res = _sma(ebitda, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc126_65d_base_v126_signal(ebitda):
    res = _sma(ebitda, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc127_75d_base_v127_signal(ebitda):
    res = _sma(ebitda, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc128_85d_base_v128_signal(ebitda):
    res = _sma(ebitda, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc129_95d_base_v129_signal(ebitda):
    res = _sma(ebitda, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc130_5d_base_v130_signal(ebitda):
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc131_15d_base_v131_signal(ebitda):
    res = _sma(ebitda, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc132_25d_base_v132_signal(ebitda):
    res = _sma(ebitda, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc133_35d_base_v133_signal(ebitda):
    res = _sma(ebitda, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc134_45d_base_v134_signal(ebitda):
    res = _sma(ebitda, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc135_55d_base_v135_signal(ebitda):
    res = _sma(ebitda, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc136_65d_base_v136_signal(ebitda):
    res = _sma(ebitda, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc137_75d_base_v137_signal(ebitda):
    res = _sma(ebitda, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc138_85d_base_v138_signal(ebitda):
    res = _sma(ebitda, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc139_95d_base_v139_signal(ebitda):
    res = _sma(ebitda, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc140_5d_base_v140_signal(ebitda):
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc141_15d_base_v141_signal(ebitda):
    res = _sma(ebitda, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc142_25d_base_v142_signal(ebitda):
    res = _sma(ebitda, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc143_35d_base_v143_signal(ebitda):
    res = _sma(ebitda, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc144_45d_base_v144_signal(ebitda):
    res = _sma(ebitda, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc145_55d_base_v145_signal(ebitda):
    res = _sma(ebitda, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc146_65d_base_v146_signal(ebitda):
    res = _sma(ebitda, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc147_75d_base_v147_signal(ebitda):
    res = _sma(ebitda, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc148_85d_base_v148_signal(ebitda):
    res = _sma(ebitda, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc149_95d_base_v149_signal(ebitda):
    res = _sma(ebitda, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc150_5d_base_v150_signal(ebitda):
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['ebitda', 'revenue', 'gp']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f38ycm_'))]
    
    print(f"Testing {{len(funcs)}} functions for f38_yield_capture_margins...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f38ycm_'))]}
