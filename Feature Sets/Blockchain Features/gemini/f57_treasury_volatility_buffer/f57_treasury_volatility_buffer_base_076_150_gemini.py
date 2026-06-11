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


def f57tvb_f57_treasury_volatility_buffer_calc076_65d_base_v076_signal(cash, marketcap):
    res = (cash / _std(marketcap, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc077_75d_base_v077_signal(cash, marketcap):
    res = (cash / _std(marketcap, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc078_85d_base_v078_signal(cash, marketcap):
    res = (cash / _std(marketcap, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc079_95d_base_v079_signal(cash, marketcap):
    res = (cash / _std(marketcap, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc080_5d_base_v080_signal(cash, marketcap):
    res = (cash / _std(marketcap, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc081_15d_base_v081_signal(cash, marketcap):
    res = (cash / _std(marketcap, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc082_25d_base_v082_signal(cash, marketcap):
    res = (cash / _std(marketcap, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc083_35d_base_v083_signal(cash, marketcap):
    res = (cash / _std(marketcap, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc084_45d_base_v084_signal(cash, marketcap):
    res = (cash / _std(marketcap, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc085_55d_base_v085_signal(cash, marketcap):
    res = (cash / _std(marketcap, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc086_65d_base_v086_signal(cash, marketcap):
    res = (cash / _std(marketcap, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc087_75d_base_v087_signal(cash, marketcap):
    res = (cash / _std(marketcap, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc088_85d_base_v088_signal(cash, marketcap):
    res = (cash / _std(marketcap, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc089_95d_base_v089_signal(cash, marketcap):
    res = (cash / _std(marketcap, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc090_5d_base_v090_signal(cash, marketcap):
    res = (cash / _std(marketcap, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc091_15d_base_v091_signal(cash, marketcap):
    res = (cash / _std(marketcap, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc092_25d_base_v092_signal(cash, marketcap):
    res = (cash / _std(marketcap, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc093_35d_base_v093_signal(cash, marketcap):
    res = (cash / _std(marketcap, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc094_45d_base_v094_signal(cash, marketcap):
    res = (cash / _std(marketcap, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc095_55d_base_v095_signal(cash, marketcap):
    res = (cash / _std(marketcap, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc096_65d_base_v096_signal(cash, marketcap):
    res = (cash / _std(marketcap, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc097_75d_base_v097_signal(cash, marketcap):
    res = (cash / _std(marketcap, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc098_85d_base_v098_signal(cash, marketcap):
    res = (cash / _std(marketcap, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc099_95d_base_v099_signal(cash, marketcap):
    res = (cash / _std(marketcap, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc100_5d_base_v100_signal(cash, marketcap):
    res = (cash / _std(marketcap, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc101_15d_base_v101_signal(cash, marketcap):
    res = (cash / _std(marketcap, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc102_25d_base_v102_signal(cash, marketcap):
    res = (cash / _std(marketcap, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc103_35d_base_v103_signal(cash, marketcap):
    res = (cash / _std(marketcap, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc104_45d_base_v104_signal(cash, marketcap):
    res = (cash / _std(marketcap, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc105_55d_base_v105_signal(cash, marketcap):
    res = (cash / _std(marketcap, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc106_65d_base_v106_signal(cash, marketcap):
    res = (cash / _std(marketcap, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc107_75d_base_v107_signal(cash, marketcap):
    res = (cash / _std(marketcap, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc108_85d_base_v108_signal(cash, marketcap):
    res = (cash / _std(marketcap, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc109_95d_base_v109_signal(cash, marketcap):
    res = (cash / _std(marketcap, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc110_5d_base_v110_signal(cash, marketcap):
    res = (cash / _std(marketcap, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc111_15d_base_v111_signal(cash, marketcap):
    res = (cash / _std(marketcap, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc112_25d_base_v112_signal(cash, marketcap):
    res = (cash / _std(marketcap, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc113_35d_base_v113_signal(cash, marketcap):
    res = (cash / _std(marketcap, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc114_45d_base_v114_signal(cash, marketcap):
    res = (cash / _std(marketcap, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc115_55d_base_v115_signal(cash, marketcap):
    res = (cash / _std(marketcap, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc116_65d_base_v116_signal(cash, marketcap):
    res = (cash / _std(marketcap, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc117_75d_base_v117_signal(cash, marketcap):
    res = (cash / _std(marketcap, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc118_85d_base_v118_signal(cash, marketcap):
    res = (cash / _std(marketcap, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc119_95d_base_v119_signal(cash, marketcap):
    res = (cash / _std(marketcap, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc120_5d_base_v120_signal(cash, marketcap):
    res = (cash / _std(marketcap, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc121_15d_base_v121_signal(cash, marketcap):
    res = (cash / _std(marketcap, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc122_25d_base_v122_signal(cash, marketcap):
    res = (cash / _std(marketcap, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc123_35d_base_v123_signal(cash, marketcap):
    res = (cash / _std(marketcap, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc124_45d_base_v124_signal(cash, marketcap):
    res = (cash / _std(marketcap, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc125_55d_base_v125_signal(cash, marketcap):
    res = (cash / _std(marketcap, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc126_65d_base_v126_signal(cash, marketcap):
    res = (cash / _std(marketcap, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc127_75d_base_v127_signal(cash, marketcap):
    res = (cash / _std(marketcap, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc128_85d_base_v128_signal(cash, marketcap):
    res = (cash / _std(marketcap, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc129_95d_base_v129_signal(cash, marketcap):
    res = (cash / _std(marketcap, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc130_5d_base_v130_signal(cash, marketcap):
    res = (cash / _std(marketcap, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc131_15d_base_v131_signal(cash, marketcap):
    res = (cash / _std(marketcap, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc132_25d_base_v132_signal(cash, marketcap):
    res = (cash / _std(marketcap, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc133_35d_base_v133_signal(cash, marketcap):
    res = (cash / _std(marketcap, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc134_45d_base_v134_signal(cash, marketcap):
    res = (cash / _std(marketcap, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc135_55d_base_v135_signal(cash, marketcap):
    res = (cash / _std(marketcap, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc136_65d_base_v136_signal(cash, marketcap):
    res = (cash / _std(marketcap, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc137_75d_base_v137_signal(cash, marketcap):
    res = (cash / _std(marketcap, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc138_85d_base_v138_signal(cash, marketcap):
    res = (cash / _std(marketcap, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc139_95d_base_v139_signal(cash, marketcap):
    res = (cash / _std(marketcap, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc140_5d_base_v140_signal(cash, marketcap):
    res = (cash / _std(marketcap, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc141_15d_base_v141_signal(cash, marketcap):
    res = (cash / _std(marketcap, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc142_25d_base_v142_signal(cash, marketcap):
    res = (cash / _std(marketcap, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc143_35d_base_v143_signal(cash, marketcap):
    res = (cash / _std(marketcap, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc144_45d_base_v144_signal(cash, marketcap):
    res = (cash / _std(marketcap, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc145_55d_base_v145_signal(cash, marketcap):
    res = (cash / _std(marketcap, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc146_65d_base_v146_signal(cash, marketcap):
    res = (cash / _std(marketcap, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc147_75d_base_v147_signal(cash, marketcap):
    res = (cash / _std(marketcap, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc148_85d_base_v148_signal(cash, marketcap):
    res = (cash / _std(marketcap, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc149_95d_base_v149_signal(cash, marketcap):
    res = (cash / _std(marketcap, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc150_5d_base_v150_signal(cash, marketcap):
    res = (cash / _std(marketcap, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['cash', 'debt', 'marketcap']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f57tvb_'))]
    
    print(f"Testing {len(funcs)} functions for f57_treasury_volatility_buffer...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{func.__name__} must return a Series"
        assert not res.isna().all(), f"{func.__name__} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f57tvb_'))]}
