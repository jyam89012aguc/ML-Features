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


def f47nvm_f47_network_valuation_multiples_calc076_65d_base_v076_signal(pe):
    res = _sma(pe, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc077_75d_base_v077_signal(pe):
    res = _sma(pe, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc078_85d_base_v078_signal(pe):
    res = _sma(pe, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc079_95d_base_v079_signal(pe):
    res = _sma(pe, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc080_5d_base_v080_signal(pe):
    res = _sma(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc081_15d_base_v081_signal(pe):
    res = _sma(pe, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc082_25d_base_v082_signal(pe):
    res = _sma(pe, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc083_35d_base_v083_signal(pe):
    res = _sma(pe, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc084_45d_base_v084_signal(pe):
    res = _sma(pe, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc085_55d_base_v085_signal(pe):
    res = _sma(pe, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc086_65d_base_v086_signal(pe):
    res = _sma(pe, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc087_75d_base_v087_signal(pe):
    res = _sma(pe, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc088_85d_base_v088_signal(pe):
    res = _sma(pe, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc089_95d_base_v089_signal(pe):
    res = _sma(pe, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc090_5d_base_v090_signal(pe):
    res = _sma(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc091_15d_base_v091_signal(pe):
    res = _sma(pe, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc092_25d_base_v092_signal(pe):
    res = _sma(pe, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc093_35d_base_v093_signal(pe):
    res = _sma(pe, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc094_45d_base_v094_signal(pe):
    res = _sma(pe, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc095_55d_base_v095_signal(pe):
    res = _sma(pe, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc096_65d_base_v096_signal(pe):
    res = _sma(pe, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc097_75d_base_v097_signal(pe):
    res = _sma(pe, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc098_85d_base_v098_signal(pe):
    res = _sma(pe, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc099_95d_base_v099_signal(pe):
    res = _sma(pe, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc100_5d_base_v100_signal(pe):
    res = _sma(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc101_15d_base_v101_signal(pe):
    res = _sma(pe, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc102_25d_base_v102_signal(pe):
    res = _sma(pe, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc103_35d_base_v103_signal(pe):
    res = _sma(pe, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc104_45d_base_v104_signal(pe):
    res = _sma(pe, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc105_55d_base_v105_signal(pe):
    res = _sma(pe, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc106_65d_base_v106_signal(pe):
    res = _sma(pe, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc107_75d_base_v107_signal(pe):
    res = _sma(pe, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc108_85d_base_v108_signal(pe):
    res = _sma(pe, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc109_95d_base_v109_signal(pe):
    res = _sma(pe, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc110_5d_base_v110_signal(pe):
    res = _sma(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc111_15d_base_v111_signal(pe):
    res = _sma(pe, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc112_25d_base_v112_signal(pe):
    res = _sma(pe, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc113_35d_base_v113_signal(pe):
    res = _sma(pe, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc114_45d_base_v114_signal(pe):
    res = _sma(pe, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc115_55d_base_v115_signal(pe):
    res = _sma(pe, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc116_65d_base_v116_signal(pe):
    res = _sma(pe, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc117_75d_base_v117_signal(pe):
    res = _sma(pe, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc118_85d_base_v118_signal(pe):
    res = _sma(pe, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc119_95d_base_v119_signal(pe):
    res = _sma(pe, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc120_5d_base_v120_signal(pe):
    res = _sma(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc121_15d_base_v121_signal(pe):
    res = _sma(pe, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc122_25d_base_v122_signal(pe):
    res = _sma(pe, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc123_35d_base_v123_signal(pe):
    res = _sma(pe, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc124_45d_base_v124_signal(pe):
    res = _sma(pe, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc125_55d_base_v125_signal(pe):
    res = _sma(pe, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc126_65d_base_v126_signal(pe):
    res = _sma(pe, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc127_75d_base_v127_signal(pe):
    res = _sma(pe, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc128_85d_base_v128_signal(pe):
    res = _sma(pe, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc129_95d_base_v129_signal(pe):
    res = _sma(pe, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc130_5d_base_v130_signal(pe):
    res = _sma(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc131_15d_base_v131_signal(pe):
    res = _sma(pe, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc132_25d_base_v132_signal(pe):
    res = _sma(pe, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc133_35d_base_v133_signal(pe):
    res = _sma(pe, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc134_45d_base_v134_signal(pe):
    res = _sma(pe, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc135_55d_base_v135_signal(pe):
    res = _sma(pe, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc136_65d_base_v136_signal(pe):
    res = _sma(pe, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc137_75d_base_v137_signal(pe):
    res = _sma(pe, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc138_85d_base_v138_signal(pe):
    res = _sma(pe, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc139_95d_base_v139_signal(pe):
    res = _sma(pe, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc140_5d_base_v140_signal(pe):
    res = _sma(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc141_15d_base_v141_signal(pe):
    res = _sma(pe, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc142_25d_base_v142_signal(pe):
    res = _sma(pe, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc143_35d_base_v143_signal(pe):
    res = _sma(pe, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc144_45d_base_v144_signal(pe):
    res = _sma(pe, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc145_55d_base_v145_signal(pe):
    res = _sma(pe, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc146_65d_base_v146_signal(pe):
    res = _sma(pe, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc147_75d_base_v147_signal(pe):
    res = _sma(pe, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc148_85d_base_v148_signal(pe):
    res = _sma(pe, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc149_95d_base_v149_signal(pe):
    res = _sma(pe, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc150_5d_base_v150_signal(pe):
    res = _sma(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['pe', 'ps', 'pb', 'marketcap']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f47nvm_'))]
    
    print(f"Testing {{len(funcs)}} functions for f47_network_valuation_multiples...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f47nvm_'))]}
