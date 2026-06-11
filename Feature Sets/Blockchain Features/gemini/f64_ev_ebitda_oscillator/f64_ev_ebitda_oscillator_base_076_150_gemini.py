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


def f64eeo_f64_ev_ebitda_oscillator_calc076_65d_base_v076_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 65))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc077_75d_base_v077_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 75))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc078_85d_base_v078_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 85))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc079_95d_base_v079_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 95))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc080_5d_base_v080_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc081_15d_base_v081_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc082_25d_base_v082_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc083_35d_base_v083_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc084_45d_base_v084_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc085_55d_base_v085_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 55))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc086_65d_base_v086_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 65))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc087_75d_base_v087_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 75))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc088_85d_base_v088_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 85))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc089_95d_base_v089_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 95))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc090_5d_base_v090_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc091_15d_base_v091_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc092_25d_base_v092_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc093_35d_base_v093_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc094_45d_base_v094_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc095_55d_base_v095_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 55))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc096_65d_base_v096_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 65))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc097_75d_base_v097_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 75))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc098_85d_base_v098_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 85))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc099_95d_base_v099_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 95))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc100_5d_base_v100_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc101_15d_base_v101_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc102_25d_base_v102_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc103_35d_base_v103_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc104_45d_base_v104_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc105_55d_base_v105_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 55))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc106_65d_base_v106_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 65))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc107_75d_base_v107_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 75))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc108_85d_base_v108_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 85))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc109_95d_base_v109_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 95))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc110_5d_base_v110_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc111_15d_base_v111_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc112_25d_base_v112_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc113_35d_base_v113_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc114_45d_base_v114_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc115_55d_base_v115_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 55))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc116_65d_base_v116_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 65))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc117_75d_base_v117_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 75))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc118_85d_base_v118_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 85))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc119_95d_base_v119_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 95))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc120_5d_base_v120_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc121_15d_base_v121_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc122_25d_base_v122_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc123_35d_base_v123_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc124_45d_base_v124_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc125_55d_base_v125_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 55))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc126_65d_base_v126_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 65))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc127_75d_base_v127_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 75))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc128_85d_base_v128_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 85))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc129_95d_base_v129_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 95))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc130_5d_base_v130_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc131_15d_base_v131_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc132_25d_base_v132_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc133_35d_base_v133_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc134_45d_base_v134_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc135_55d_base_v135_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 55))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc136_65d_base_v136_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 65))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc137_75d_base_v137_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 75))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc138_85d_base_v138_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 85))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc139_95d_base_v139_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 95))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc140_5d_base_v140_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc141_15d_base_v141_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc142_25d_base_v142_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc143_35d_base_v143_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc144_45d_base_v144_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc145_55d_base_v145_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 55))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc146_65d_base_v146_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 65))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc147_75d_base_v147_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 75))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc148_85d_base_v148_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 85))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc149_95d_base_v149_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 95))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc150_5d_base_v150_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 5))
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['ev', 'ebitda', 'close']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f64eeo_'))]
    
    print(f"Testing {len(funcs)} functions for f64_ev_ebitda_oscillator...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{func.__name__} must return a Series"
        assert not res.isna().all(), f"{func.__name__} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f64eeo_'))]}
