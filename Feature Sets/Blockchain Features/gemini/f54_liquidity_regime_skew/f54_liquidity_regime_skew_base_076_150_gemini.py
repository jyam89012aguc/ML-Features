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


def f54lrs_f54_liquidity_regime_skew_calc076_65d_base_v076_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc077_75d_base_v077_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc078_85d_base_v078_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc079_95d_base_v079_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc080_5d_base_v080_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc081_15d_base_v081_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc082_25d_base_v082_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc083_35d_base_v083_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc084_45d_base_v084_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc085_55d_base_v085_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc086_65d_base_v086_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc087_75d_base_v087_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc088_85d_base_v088_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc089_95d_base_v089_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc090_5d_base_v090_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc091_15d_base_v091_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc092_25d_base_v092_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc093_35d_base_v093_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc094_45d_base_v094_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc095_55d_base_v095_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc096_65d_base_v096_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc097_75d_base_v097_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc098_85d_base_v098_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc099_95d_base_v099_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc100_5d_base_v100_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc101_15d_base_v101_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc102_25d_base_v102_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc103_35d_base_v103_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc104_45d_base_v104_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc105_55d_base_v105_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc106_65d_base_v106_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc107_75d_base_v107_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc108_85d_base_v108_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc109_95d_base_v109_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc110_5d_base_v110_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc111_15d_base_v111_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc112_25d_base_v112_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc113_35d_base_v113_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc114_45d_base_v114_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc115_55d_base_v115_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc116_65d_base_v116_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc117_75d_base_v117_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc118_85d_base_v118_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc119_95d_base_v119_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc120_5d_base_v120_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc121_15d_base_v121_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc122_25d_base_v122_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc123_35d_base_v123_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc124_45d_base_v124_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc125_55d_base_v125_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc126_65d_base_v126_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc127_75d_base_v127_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc128_85d_base_v128_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc129_95d_base_v129_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc130_5d_base_v130_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc131_15d_base_v131_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc132_25d_base_v132_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc133_35d_base_v133_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc134_45d_base_v134_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc135_55d_base_v135_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc136_65d_base_v136_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc137_75d_base_v137_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc138_85d_base_v138_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc139_95d_base_v139_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc140_5d_base_v140_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc141_15d_base_v141_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc142_25d_base_v142_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc143_35d_base_v143_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc144_45d_base_v144_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc145_55d_base_v145_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc146_65d_base_v146_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc147_75d_base_v147_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc148_85d_base_v148_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc149_95d_base_v149_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc150_5d_base_v150_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['high', 'low', 'volume', 'closeadj']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f54lrs_'))]
    
    print(f"Testing {len(funcs)} functions for f54_liquidity_regime_skew...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{func.__name__} must return a Series"
        assert not res.isna().all(), f"{func.__name__} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f54lrs_'))]}
