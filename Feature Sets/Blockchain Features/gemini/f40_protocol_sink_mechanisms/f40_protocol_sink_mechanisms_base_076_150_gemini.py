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


def f40psm_f40_protocol_sink_mechanisms_calc076_65d_base_v076_signal(fcf):
    res = _sma(fcf, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc077_75d_base_v077_signal(fcf):
    res = _sma(fcf, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc078_85d_base_v078_signal(fcf):
    res = _sma(fcf, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc079_95d_base_v079_signal(fcf):
    res = _sma(fcf, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc080_5d_base_v080_signal(fcf):
    res = _sma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc081_15d_base_v081_signal(fcf):
    res = _sma(fcf, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc082_25d_base_v082_signal(fcf):
    res = _sma(fcf, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc083_35d_base_v083_signal(fcf):
    res = _sma(fcf, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc084_45d_base_v084_signal(fcf):
    res = _sma(fcf, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc085_55d_base_v085_signal(fcf):
    res = _sma(fcf, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc086_65d_base_v086_signal(fcf):
    res = _sma(fcf, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc087_75d_base_v087_signal(fcf):
    res = _sma(fcf, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc088_85d_base_v088_signal(fcf):
    res = _sma(fcf, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc089_95d_base_v089_signal(fcf):
    res = _sma(fcf, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc090_5d_base_v090_signal(fcf):
    res = _sma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc091_15d_base_v091_signal(fcf):
    res = _sma(fcf, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc092_25d_base_v092_signal(fcf):
    res = _sma(fcf, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc093_35d_base_v093_signal(fcf):
    res = _sma(fcf, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc094_45d_base_v094_signal(fcf):
    res = _sma(fcf, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc095_55d_base_v095_signal(fcf):
    res = _sma(fcf, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc096_65d_base_v096_signal(fcf):
    res = _sma(fcf, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc097_75d_base_v097_signal(fcf):
    res = _sma(fcf, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc098_85d_base_v098_signal(fcf):
    res = _sma(fcf, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc099_95d_base_v099_signal(fcf):
    res = _sma(fcf, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc100_5d_base_v100_signal(fcf):
    res = _sma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc101_15d_base_v101_signal(fcf):
    res = _sma(fcf, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc102_25d_base_v102_signal(fcf):
    res = _sma(fcf, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc103_35d_base_v103_signal(fcf):
    res = _sma(fcf, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc104_45d_base_v104_signal(fcf):
    res = _sma(fcf, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc105_55d_base_v105_signal(fcf):
    res = _sma(fcf, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc106_65d_base_v106_signal(fcf):
    res = _sma(fcf, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc107_75d_base_v107_signal(fcf):
    res = _sma(fcf, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc108_85d_base_v108_signal(fcf):
    res = _sma(fcf, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc109_95d_base_v109_signal(fcf):
    res = _sma(fcf, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc110_5d_base_v110_signal(fcf):
    res = _sma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc111_15d_base_v111_signal(fcf):
    res = _sma(fcf, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc112_25d_base_v112_signal(fcf):
    res = _sma(fcf, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc113_35d_base_v113_signal(fcf):
    res = _sma(fcf, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc114_45d_base_v114_signal(fcf):
    res = _sma(fcf, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc115_55d_base_v115_signal(fcf):
    res = _sma(fcf, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc116_65d_base_v116_signal(fcf):
    res = _sma(fcf, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc117_75d_base_v117_signal(fcf):
    res = _sma(fcf, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc118_85d_base_v118_signal(fcf):
    res = _sma(fcf, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc119_95d_base_v119_signal(fcf):
    res = _sma(fcf, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc120_5d_base_v120_signal(fcf):
    res = _sma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc121_15d_base_v121_signal(fcf):
    res = _sma(fcf, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc122_25d_base_v122_signal(fcf):
    res = _sma(fcf, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc123_35d_base_v123_signal(fcf):
    res = _sma(fcf, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc124_45d_base_v124_signal(fcf):
    res = _sma(fcf, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc125_55d_base_v125_signal(fcf):
    res = _sma(fcf, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc126_65d_base_v126_signal(fcf):
    res = _sma(fcf, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc127_75d_base_v127_signal(fcf):
    res = _sma(fcf, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc128_85d_base_v128_signal(fcf):
    res = _sma(fcf, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc129_95d_base_v129_signal(fcf):
    res = _sma(fcf, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc130_5d_base_v130_signal(fcf):
    res = _sma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc131_15d_base_v131_signal(fcf):
    res = _sma(fcf, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc132_25d_base_v132_signal(fcf):
    res = _sma(fcf, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc133_35d_base_v133_signal(fcf):
    res = _sma(fcf, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc134_45d_base_v134_signal(fcf):
    res = _sma(fcf, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc135_55d_base_v135_signal(fcf):
    res = _sma(fcf, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc136_65d_base_v136_signal(fcf):
    res = _sma(fcf, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc137_75d_base_v137_signal(fcf):
    res = _sma(fcf, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc138_85d_base_v138_signal(fcf):
    res = _sma(fcf, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc139_95d_base_v139_signal(fcf):
    res = _sma(fcf, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc140_5d_base_v140_signal(fcf):
    res = _sma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc141_15d_base_v141_signal(fcf):
    res = _sma(fcf, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc142_25d_base_v142_signal(fcf):
    res = _sma(fcf, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc143_35d_base_v143_signal(fcf):
    res = _sma(fcf, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc144_45d_base_v144_signal(fcf):
    res = _sma(fcf, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc145_55d_base_v145_signal(fcf):
    res = _sma(fcf, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc146_65d_base_v146_signal(fcf):
    res = _sma(fcf, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc147_75d_base_v147_signal(fcf):
    res = _sma(fcf, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc148_85d_base_v148_signal(fcf):
    res = _sma(fcf, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc149_95d_base_v149_signal(fcf):
    res = _sma(fcf, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc150_5d_base_v150_signal(fcf):
    res = _sma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['fcf', 'revenue', 'netinc']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f40psm_'))]
    
    print(f"Testing {{len(funcs)}} functions for f40_protocol_sink_mechanisms...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f40psm_'))]}
