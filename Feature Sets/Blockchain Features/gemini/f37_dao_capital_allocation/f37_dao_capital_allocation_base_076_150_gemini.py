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


def f37dca_f37_dao_capital_allocation_calc076_65d_base_v076_signal(capex):
    res = _sma(capex, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc077_75d_base_v077_signal(capex):
    res = _sma(capex, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc078_85d_base_v078_signal(capex):
    res = _sma(capex, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc079_95d_base_v079_signal(capex):
    res = _sma(capex, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc080_5d_base_v080_signal(capex):
    res = _sma(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc081_15d_base_v081_signal(capex):
    res = _sma(capex, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc082_25d_base_v082_signal(capex):
    res = _sma(capex, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc083_35d_base_v083_signal(capex):
    res = _sma(capex, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc084_45d_base_v084_signal(capex):
    res = _sma(capex, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc085_55d_base_v085_signal(capex):
    res = _sma(capex, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc086_65d_base_v086_signal(capex):
    res = _sma(capex, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc087_75d_base_v087_signal(capex):
    res = _sma(capex, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc088_85d_base_v088_signal(capex):
    res = _sma(capex, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc089_95d_base_v089_signal(capex):
    res = _sma(capex, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc090_5d_base_v090_signal(capex):
    res = _sma(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc091_15d_base_v091_signal(capex):
    res = _sma(capex, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc092_25d_base_v092_signal(capex):
    res = _sma(capex, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc093_35d_base_v093_signal(capex):
    res = _sma(capex, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc094_45d_base_v094_signal(capex):
    res = _sma(capex, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc095_55d_base_v095_signal(capex):
    res = _sma(capex, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc096_65d_base_v096_signal(capex):
    res = _sma(capex, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc097_75d_base_v097_signal(capex):
    res = _sma(capex, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc098_85d_base_v098_signal(capex):
    res = _sma(capex, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc099_95d_base_v099_signal(capex):
    res = _sma(capex, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc100_5d_base_v100_signal(capex):
    res = _sma(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc101_15d_base_v101_signal(capex):
    res = _sma(capex, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc102_25d_base_v102_signal(capex):
    res = _sma(capex, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc103_35d_base_v103_signal(capex):
    res = _sma(capex, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc104_45d_base_v104_signal(capex):
    res = _sma(capex, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc105_55d_base_v105_signal(capex):
    res = _sma(capex, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc106_65d_base_v106_signal(capex):
    res = _sma(capex, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc107_75d_base_v107_signal(capex):
    res = _sma(capex, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc108_85d_base_v108_signal(capex):
    res = _sma(capex, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc109_95d_base_v109_signal(capex):
    res = _sma(capex, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc110_5d_base_v110_signal(capex):
    res = _sma(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc111_15d_base_v111_signal(capex):
    res = _sma(capex, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc112_25d_base_v112_signal(capex):
    res = _sma(capex, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc113_35d_base_v113_signal(capex):
    res = _sma(capex, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc114_45d_base_v114_signal(capex):
    res = _sma(capex, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc115_55d_base_v115_signal(capex):
    res = _sma(capex, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc116_65d_base_v116_signal(capex):
    res = _sma(capex, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc117_75d_base_v117_signal(capex):
    res = _sma(capex, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc118_85d_base_v118_signal(capex):
    res = _sma(capex, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc119_95d_base_v119_signal(capex):
    res = _sma(capex, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc120_5d_base_v120_signal(capex):
    res = _sma(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc121_15d_base_v121_signal(capex):
    res = _sma(capex, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc122_25d_base_v122_signal(capex):
    res = _sma(capex, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc123_35d_base_v123_signal(capex):
    res = _sma(capex, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc124_45d_base_v124_signal(capex):
    res = _sma(capex, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc125_55d_base_v125_signal(capex):
    res = _sma(capex, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc126_65d_base_v126_signal(capex):
    res = _sma(capex, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc127_75d_base_v127_signal(capex):
    res = _sma(capex, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc128_85d_base_v128_signal(capex):
    res = _sma(capex, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc129_95d_base_v129_signal(capex):
    res = _sma(capex, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc130_5d_base_v130_signal(capex):
    res = _sma(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc131_15d_base_v131_signal(capex):
    res = _sma(capex, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc132_25d_base_v132_signal(capex):
    res = _sma(capex, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc133_35d_base_v133_signal(capex):
    res = _sma(capex, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc134_45d_base_v134_signal(capex):
    res = _sma(capex, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc135_55d_base_v135_signal(capex):
    res = _sma(capex, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc136_65d_base_v136_signal(capex):
    res = _sma(capex, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc137_75d_base_v137_signal(capex):
    res = _sma(capex, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc138_85d_base_v138_signal(capex):
    res = _sma(capex, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc139_95d_base_v139_signal(capex):
    res = _sma(capex, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc140_5d_base_v140_signal(capex):
    res = _sma(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc141_15d_base_v141_signal(capex):
    res = _sma(capex, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc142_25d_base_v142_signal(capex):
    res = _sma(capex, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc143_35d_base_v143_signal(capex):
    res = _sma(capex, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc144_45d_base_v144_signal(capex):
    res = _sma(capex, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc145_55d_base_v145_signal(capex):
    res = _sma(capex, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc146_65d_base_v146_signal(capex):
    res = _sma(capex, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc147_75d_base_v147_signal(capex):
    res = _sma(capex, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc148_85d_base_v148_signal(capex):
    res = _sma(capex, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc149_95d_base_v149_signal(capex):
    res = _sma(capex, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc150_5d_base_v150_signal(capex):
    res = _sma(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['capex', 'revenue', 'assets']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f37dca_'))]
    
    print(f"Testing {{len(funcs)}} functions for f37_dao_capital_allocation...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f37dca_'))]}
