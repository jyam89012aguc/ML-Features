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


def f60cba_f60_composite_blockchain_alpha_calc076_65d_base_v076_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc077_75d_base_v077_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc078_85d_base_v078_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc079_95d_base_v079_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc080_5d_base_v080_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc081_15d_base_v081_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 15) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc082_25d_base_v082_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 25) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc083_35d_base_v083_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 35) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc084_45d_base_v084_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 45) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc085_55d_base_v085_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 55) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc086_65d_base_v086_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc087_75d_base_v087_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc088_85d_base_v088_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc089_95d_base_v089_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc090_5d_base_v090_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc091_15d_base_v091_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 15) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc092_25d_base_v092_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 25) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc093_35d_base_v093_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 35) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc094_45d_base_v094_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 45) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc095_55d_base_v095_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 55) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc096_65d_base_v096_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc097_75d_base_v097_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc098_85d_base_v098_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc099_95d_base_v099_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc100_5d_base_v100_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc101_15d_base_v101_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 15) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc102_25d_base_v102_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 25) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc103_35d_base_v103_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 35) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc104_45d_base_v104_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 45) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc105_55d_base_v105_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 55) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc106_65d_base_v106_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc107_75d_base_v107_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc108_85d_base_v108_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc109_95d_base_v109_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc110_5d_base_v110_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc111_15d_base_v111_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 15) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc112_25d_base_v112_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 25) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc113_35d_base_v113_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 35) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc114_45d_base_v114_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 45) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc115_55d_base_v115_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 55) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc116_65d_base_v116_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc117_75d_base_v117_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc118_85d_base_v118_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc119_95d_base_v119_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc120_5d_base_v120_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc121_15d_base_v121_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 15) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc122_25d_base_v122_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 25) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc123_35d_base_v123_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 35) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc124_45d_base_v124_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 45) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc125_55d_base_v125_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 55) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc126_65d_base_v126_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc127_75d_base_v127_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc128_85d_base_v128_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc129_95d_base_v129_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc130_5d_base_v130_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc131_15d_base_v131_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 15) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc132_25d_base_v132_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 25) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc133_35d_base_v133_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 35) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc134_45d_base_v134_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 45) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc135_55d_base_v135_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 55) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc136_65d_base_v136_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc137_75d_base_v137_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc138_85d_base_v138_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc139_95d_base_v139_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc140_5d_base_v140_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc141_15d_base_v141_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 15) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc142_25d_base_v142_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 25) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc143_35d_base_v143_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 35) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc144_45d_base_v144_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 45) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc145_55d_base_v145_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 55) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc146_65d_base_v146_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc147_75d_base_v147_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc148_85d_base_v148_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc149_95d_base_v149_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc150_5d_base_v150_signal(marketcap, revenue, sf3a_value):
    res = ((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['marketcap', 'revenue', 'sf3a_value', 'volume']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f60cba_'))]
    
    print(f"Testing {len(funcs)} functions for f60_composite_blockchain_alpha...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{func.__name__} must return a Series"
        assert not res.isna().all(), f"{func.__name__} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f60cba_'))]}
