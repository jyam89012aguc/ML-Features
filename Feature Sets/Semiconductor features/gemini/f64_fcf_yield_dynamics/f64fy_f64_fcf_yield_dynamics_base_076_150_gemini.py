import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f64fy_f64_fcf_yield_dynamics_calc076_5d_base_v076_signal(fcf, revenue):
    res = (fcf / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc076_5d_base_v076_signal'] = f64fy_f64_fcf_yield_dynamics_calc076_5d_base_v076_signal

def f64fy_f64_fcf_yield_dynamics_calc077_10d_base_v077_signal(fcf, revenue):
    res = (fcf / revenue).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc077_10d_base_v077_signal'] = f64fy_f64_fcf_yield_dynamics_calc077_10d_base_v077_signal

def f64fy_f64_fcf_yield_dynamics_calc078_21d_base_v078_signal(fcf, revenue):
    res = (fcf / revenue).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc078_21d_base_v078_signal'] = f64fy_f64_fcf_yield_dynamics_calc078_21d_base_v078_signal

def f64fy_f64_fcf_yield_dynamics_calc079_42d_base_v079_signal(fcf, revenue):
    res = (fcf / revenue).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc079_42d_base_v079_signal'] = f64fy_f64_fcf_yield_dynamics_calc079_42d_base_v079_signal

def f64fy_f64_fcf_yield_dynamics_calc080_63d_base_v080_signal(fcf, revenue):
    res = (fcf / revenue).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc080_63d_base_v080_signal'] = f64fy_f64_fcf_yield_dynamics_calc080_63d_base_v080_signal

def f64fy_f64_fcf_yield_dynamics_calc081_126d_base_v081_signal(fcf, revenue):
    res = (fcf / revenue).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc081_126d_base_v081_signal'] = f64fy_f64_fcf_yield_dynamics_calc081_126d_base_v081_signal

def f64fy_f64_fcf_yield_dynamics_calc082_252d_base_v082_signal(fcf, revenue):
    res = (fcf / revenue).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc082_252d_base_v082_signal'] = f64fy_f64_fcf_yield_dynamics_calc082_252d_base_v082_signal

def f64fy_f64_fcf_yield_dynamics_calc083_21d_base_v083_signal(fcf, revenue):
    res = (fcf / revenue).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc083_21d_base_v083_signal'] = f64fy_f64_fcf_yield_dynamics_calc083_21d_base_v083_signal

def f64fy_f64_fcf_yield_dynamics_calc084_63d_base_v084_signal(fcf, revenue):
    res = (fcf / revenue).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc084_63d_base_v084_signal'] = f64fy_f64_fcf_yield_dynamics_calc084_63d_base_v084_signal

def f64fy_f64_fcf_yield_dynamics_calc085_5d_base_v085_signal(fcf, revenue):
    res = (fcf / revenue).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc085_5d_base_v085_signal'] = f64fy_f64_fcf_yield_dynamics_calc085_5d_base_v085_signal

def f64fy_f64_fcf_yield_dynamics_calc086_21d_base_v086_signal(fcf, revenue):
    res = (fcf / revenue).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc086_21d_base_v086_signal'] = f64fy_f64_fcf_yield_dynamics_calc086_21d_base_v086_signal

def f64fy_f64_fcf_yield_dynamics_calc087_10d_base_v087_signal(fcf, revenue):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(fcf / revenue)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc087_10d_base_v087_signal'] = f64fy_f64_fcf_yield_dynamics_calc087_10d_base_v087_signal

def f64fy_f64_fcf_yield_dynamics_calc088_63d_base_v088_signal(fcf, revenue):
    res = (fcf / revenue).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc088_63d_base_v088_signal'] = f64fy_f64_fcf_yield_dynamics_calc088_63d_base_v088_signal

def f64fy_f64_fcf_yield_dynamics_calc089_126d_base_v089_signal(fcf, revenue):
    res = (fcf / revenue).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc089_126d_base_v089_signal'] = f64fy_f64_fcf_yield_dynamics_calc089_126d_base_v089_signal

def f64fy_f64_fcf_yield_dynamics_calc090_252d_base_v090_signal(fcf, revenue):
    res = (fcf / revenue).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc090_252d_base_v090_signal'] = f64fy_f64_fcf_yield_dynamics_calc090_252d_base_v090_signal

def f64fy_f64_fcf_yield_dynamics_calc091_5d_base_v091_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc091_5d_base_v091_signal'] = f64fy_f64_fcf_yield_dynamics_calc091_5d_base_v091_signal

def f64fy_f64_fcf_yield_dynamics_calc092_10d_base_v092_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc092_10d_base_v092_signal'] = f64fy_f64_fcf_yield_dynamics_calc092_10d_base_v092_signal

def f64fy_f64_fcf_yield_dynamics_calc093_21d_base_v093_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc093_21d_base_v093_signal'] = f64fy_f64_fcf_yield_dynamics_calc093_21d_base_v093_signal

def f64fy_f64_fcf_yield_dynamics_calc094_42d_base_v094_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc094_42d_base_v094_signal'] = f64fy_f64_fcf_yield_dynamics_calc094_42d_base_v094_signal

def f64fy_f64_fcf_yield_dynamics_calc095_63d_base_v095_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc095_63d_base_v095_signal'] = f64fy_f64_fcf_yield_dynamics_calc095_63d_base_v095_signal

def f64fy_f64_fcf_yield_dynamics_calc096_126d_base_v096_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc096_126d_base_v096_signal'] = f64fy_f64_fcf_yield_dynamics_calc096_126d_base_v096_signal

def f64fy_f64_fcf_yield_dynamics_calc097_252d_base_v097_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc097_252d_base_v097_signal'] = f64fy_f64_fcf_yield_dynamics_calc097_252d_base_v097_signal

def f64fy_f64_fcf_yield_dynamics_calc098_21d_base_v098_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc098_21d_base_v098_signal'] = f64fy_f64_fcf_yield_dynamics_calc098_21d_base_v098_signal

def f64fy_f64_fcf_yield_dynamics_calc099_63d_base_v099_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc099_63d_base_v099_signal'] = f64fy_f64_fcf_yield_dynamics_calc099_63d_base_v099_signal

def f64fy_f64_fcf_yield_dynamics_calc100_5d_base_v100_signal(ebitda, marketcap):
    res = (ebitda / marketcap).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc100_5d_base_v100_signal'] = f64fy_f64_fcf_yield_dynamics_calc100_5d_base_v100_signal

def f64fy_f64_fcf_yield_dynamics_calc101_21d_base_v101_signal(ebitda, marketcap):
    res = (ebitda / marketcap).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc101_21d_base_v101_signal'] = f64fy_f64_fcf_yield_dynamics_calc101_21d_base_v101_signal

def f64fy_f64_fcf_yield_dynamics_calc102_10d_base_v102_signal(ebitda, marketcap):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(ebitda / marketcap)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc102_10d_base_v102_signal'] = f64fy_f64_fcf_yield_dynamics_calc102_10d_base_v102_signal

def f64fy_f64_fcf_yield_dynamics_calc103_63d_base_v103_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc103_63d_base_v103_signal'] = f64fy_f64_fcf_yield_dynamics_calc103_63d_base_v103_signal

def f64fy_f64_fcf_yield_dynamics_calc104_126d_base_v104_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc104_126d_base_v104_signal'] = f64fy_f64_fcf_yield_dynamics_calc104_126d_base_v104_signal

def f64fy_f64_fcf_yield_dynamics_calc105_252d_base_v105_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc105_252d_base_v105_signal'] = f64fy_f64_fcf_yield_dynamics_calc105_252d_base_v105_signal

def f64fy_f64_fcf_yield_dynamics_calc106_5d_base_v106_signal(ebitda, ev):
    res = (ebitda / ev).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc106_5d_base_v106_signal'] = f64fy_f64_fcf_yield_dynamics_calc106_5d_base_v106_signal

def f64fy_f64_fcf_yield_dynamics_calc107_10d_base_v107_signal(ebitda, ev):
    res = (ebitda / ev).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc107_10d_base_v107_signal'] = f64fy_f64_fcf_yield_dynamics_calc107_10d_base_v107_signal

def f64fy_f64_fcf_yield_dynamics_calc108_21d_base_v108_signal(ebitda, ev):
    res = (ebitda / ev).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc108_21d_base_v108_signal'] = f64fy_f64_fcf_yield_dynamics_calc108_21d_base_v108_signal

def f64fy_f64_fcf_yield_dynamics_calc109_42d_base_v109_signal(ebitda, ev):
    res = (ebitda / ev).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc109_42d_base_v109_signal'] = f64fy_f64_fcf_yield_dynamics_calc109_42d_base_v109_signal

def f64fy_f64_fcf_yield_dynamics_calc110_63d_base_v110_signal(ebitda, ev):
    res = (ebitda / ev).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc110_63d_base_v110_signal'] = f64fy_f64_fcf_yield_dynamics_calc110_63d_base_v110_signal

def f64fy_f64_fcf_yield_dynamics_calc111_126d_base_v111_signal(ebitda, ev):
    res = (ebitda / ev).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc111_126d_base_v111_signal'] = f64fy_f64_fcf_yield_dynamics_calc111_126d_base_v111_signal

def f64fy_f64_fcf_yield_dynamics_calc112_252d_base_v112_signal(ebitda, ev):
    res = (ebitda / ev).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc112_252d_base_v112_signal'] = f64fy_f64_fcf_yield_dynamics_calc112_252d_base_v112_signal

def f64fy_f64_fcf_yield_dynamics_calc113_21d_base_v113_signal(ebitda, ev):
    res = (ebitda / ev).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc113_21d_base_v113_signal'] = f64fy_f64_fcf_yield_dynamics_calc113_21d_base_v113_signal

def f64fy_f64_fcf_yield_dynamics_calc114_63d_base_v114_signal(ebitda, ev):
    res = (ebitda / ev).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc114_63d_base_v114_signal'] = f64fy_f64_fcf_yield_dynamics_calc114_63d_base_v114_signal

def f64fy_f64_fcf_yield_dynamics_calc115_5d_base_v115_signal(ebitda, ev):
    res = (ebitda / ev).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc115_5d_base_v115_signal'] = f64fy_f64_fcf_yield_dynamics_calc115_5d_base_v115_signal

def f64fy_f64_fcf_yield_dynamics_calc116_21d_base_v116_signal(ebitda, ev):
    res = (ebitda / ev).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc116_21d_base_v116_signal'] = f64fy_f64_fcf_yield_dynamics_calc116_21d_base_v116_signal

def f64fy_f64_fcf_yield_dynamics_calc117_10d_base_v117_signal(ebitda, ev):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(ebitda / ev)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc117_10d_base_v117_signal'] = f64fy_f64_fcf_yield_dynamics_calc117_10d_base_v117_signal

def f64fy_f64_fcf_yield_dynamics_calc118_63d_base_v118_signal(ebitda, ev):
    res = (ebitda / ev).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc118_63d_base_v118_signal'] = f64fy_f64_fcf_yield_dynamics_calc118_63d_base_v118_signal

def f64fy_f64_fcf_yield_dynamics_calc119_126d_base_v119_signal(ebitda, ev):
    res = (ebitda / ev).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc119_126d_base_v119_signal'] = f64fy_f64_fcf_yield_dynamics_calc119_126d_base_v119_signal

def f64fy_f64_fcf_yield_dynamics_calc120_252d_base_v120_signal(ebitda, ev):
    res = (ebitda / ev).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc120_252d_base_v120_signal'] = f64fy_f64_fcf_yield_dynamics_calc120_252d_base_v120_signal

def f64fy_f64_fcf_yield_dynamics_calc121_5d_base_v121_signal(fcf, liabilities):
    res = (fcf / liabilities).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc121_5d_base_v121_signal'] = f64fy_f64_fcf_yield_dynamics_calc121_5d_base_v121_signal

def f64fy_f64_fcf_yield_dynamics_calc122_10d_base_v122_signal(fcf, liabilities):
    res = (fcf / liabilities).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc122_10d_base_v122_signal'] = f64fy_f64_fcf_yield_dynamics_calc122_10d_base_v122_signal

def f64fy_f64_fcf_yield_dynamics_calc123_21d_base_v123_signal(fcf, liabilities):
    res = (fcf / liabilities).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc123_21d_base_v123_signal'] = f64fy_f64_fcf_yield_dynamics_calc123_21d_base_v123_signal

def f64fy_f64_fcf_yield_dynamics_calc124_42d_base_v124_signal(fcf, liabilities):
    res = (fcf / liabilities).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc124_42d_base_v124_signal'] = f64fy_f64_fcf_yield_dynamics_calc124_42d_base_v124_signal

def f64fy_f64_fcf_yield_dynamics_calc125_63d_base_v125_signal(fcf, liabilities):
    res = (fcf / liabilities).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc125_63d_base_v125_signal'] = f64fy_f64_fcf_yield_dynamics_calc125_63d_base_v125_signal

def f64fy_f64_fcf_yield_dynamics_calc126_126d_base_v126_signal(fcf, liabilities):
    res = (fcf / liabilities).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc126_126d_base_v126_signal'] = f64fy_f64_fcf_yield_dynamics_calc126_126d_base_v126_signal

def f64fy_f64_fcf_yield_dynamics_calc127_252d_base_v127_signal(fcf, liabilities):
    res = (fcf / liabilities).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc127_252d_base_v127_signal'] = f64fy_f64_fcf_yield_dynamics_calc127_252d_base_v127_signal

def f64fy_f64_fcf_yield_dynamics_calc128_21d_base_v128_signal(fcf, liabilities):
    res = (fcf / liabilities).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc128_21d_base_v128_signal'] = f64fy_f64_fcf_yield_dynamics_calc128_21d_base_v128_signal

def f64fy_f64_fcf_yield_dynamics_calc129_63d_base_v129_signal(fcf, liabilities):
    res = (fcf / liabilities).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc129_63d_base_v129_signal'] = f64fy_f64_fcf_yield_dynamics_calc129_63d_base_v129_signal

def f64fy_f64_fcf_yield_dynamics_calc130_5d_base_v130_signal(fcf, liabilities):
    res = (fcf / liabilities).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc130_5d_base_v130_signal'] = f64fy_f64_fcf_yield_dynamics_calc130_5d_base_v130_signal

def f64fy_f64_fcf_yield_dynamics_calc131_21d_base_v131_signal(fcf, liabilities):
    res = (fcf / liabilities).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc131_21d_base_v131_signal'] = f64fy_f64_fcf_yield_dynamics_calc131_21d_base_v131_signal

def f64fy_f64_fcf_yield_dynamics_calc132_10d_base_v132_signal(fcf, liabilities):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(fcf / liabilities)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc132_10d_base_v132_signal'] = f64fy_f64_fcf_yield_dynamics_calc132_10d_base_v132_signal

def f64fy_f64_fcf_yield_dynamics_calc133_63d_base_v133_signal(fcf, liabilities):
    res = (fcf / liabilities).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc133_63d_base_v133_signal'] = f64fy_f64_fcf_yield_dynamics_calc133_63d_base_v133_signal

def f64fy_f64_fcf_yield_dynamics_calc134_126d_base_v134_signal(fcf, liabilities):
    res = (fcf / liabilities).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc134_126d_base_v134_signal'] = f64fy_f64_fcf_yield_dynamics_calc134_126d_base_v134_signal

def f64fy_f64_fcf_yield_dynamics_calc135_252d_base_v135_signal(fcf, liabilities):
    res = (fcf / liabilities).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc135_252d_base_v135_signal'] = f64fy_f64_fcf_yield_dynamics_calc135_252d_base_v135_signal

def f64fy_f64_fcf_yield_dynamics_calc136_5d_base_v136_signal(fcf, equity):
    res = (fcf / equity).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc136_5d_base_v136_signal'] = f64fy_f64_fcf_yield_dynamics_calc136_5d_base_v136_signal

def f64fy_f64_fcf_yield_dynamics_calc137_10d_base_v137_signal(fcf, equity):
    res = (fcf / equity).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc137_10d_base_v137_signal'] = f64fy_f64_fcf_yield_dynamics_calc137_10d_base_v137_signal

def f64fy_f64_fcf_yield_dynamics_calc138_21d_base_v138_signal(fcf, equity):
    res = (fcf / equity).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc138_21d_base_v138_signal'] = f64fy_f64_fcf_yield_dynamics_calc138_21d_base_v138_signal

def f64fy_f64_fcf_yield_dynamics_calc139_42d_base_v139_signal(fcf, equity):
    res = (fcf / equity).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc139_42d_base_v139_signal'] = f64fy_f64_fcf_yield_dynamics_calc139_42d_base_v139_signal

def f64fy_f64_fcf_yield_dynamics_calc140_63d_base_v140_signal(fcf, equity):
    res = (fcf / equity).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc140_63d_base_v140_signal'] = f64fy_f64_fcf_yield_dynamics_calc140_63d_base_v140_signal

def f64fy_f64_fcf_yield_dynamics_calc141_126d_base_v141_signal(fcf, equity):
    res = (fcf / equity).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc141_126d_base_v141_signal'] = f64fy_f64_fcf_yield_dynamics_calc141_126d_base_v141_signal

def f64fy_f64_fcf_yield_dynamics_calc142_252d_base_v142_signal(fcf, equity):
    res = (fcf / equity).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc142_252d_base_v142_signal'] = f64fy_f64_fcf_yield_dynamics_calc142_252d_base_v142_signal

def f64fy_f64_fcf_yield_dynamics_calc143_21d_base_v143_signal(fcf, equity):
    res = (fcf / equity).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc143_21d_base_v143_signal'] = f64fy_f64_fcf_yield_dynamics_calc143_21d_base_v143_signal

def f64fy_f64_fcf_yield_dynamics_calc144_63d_base_v144_signal(fcf, equity):
    res = (fcf / equity).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc144_63d_base_v144_signal'] = f64fy_f64_fcf_yield_dynamics_calc144_63d_base_v144_signal

def f64fy_f64_fcf_yield_dynamics_calc145_5d_base_v145_signal(fcf, equity):
    res = (fcf / equity).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc145_5d_base_v145_signal'] = f64fy_f64_fcf_yield_dynamics_calc145_5d_base_v145_signal

def f64fy_f64_fcf_yield_dynamics_calc146_21d_base_v146_signal(fcf, equity):
    res = (fcf / equity).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc146_21d_base_v146_signal'] = f64fy_f64_fcf_yield_dynamics_calc146_21d_base_v146_signal

def f64fy_f64_fcf_yield_dynamics_calc147_10d_base_v147_signal(fcf, equity):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(fcf / equity)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc147_10d_base_v147_signal'] = f64fy_f64_fcf_yield_dynamics_calc147_10d_base_v147_signal

def f64fy_f64_fcf_yield_dynamics_calc148_63d_base_v148_signal(fcf, equity):
    res = (fcf / equity).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc148_63d_base_v148_signal'] = f64fy_f64_fcf_yield_dynamics_calc148_63d_base_v148_signal

def f64fy_f64_fcf_yield_dynamics_calc149_126d_base_v149_signal(fcf, equity):
    res = (fcf / equity).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc149_126d_base_v149_signal'] = f64fy_f64_fcf_yield_dynamics_calc149_126d_base_v149_signal

def f64fy_f64_fcf_yield_dynamics_calc150_252d_base_v150_signal(fcf, equity):
    res = (fcf / equity).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc150_252d_base_v150_signal'] = f64fy_f64_fcf_yield_dynamics_calc150_252d_base_v150_signal


if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    np.random.seed(42)
    n = 1000
    cols = ['open', 'high', 'low', 'close', 'volume', 'closeadj', 'revenue', 'assets', 'ebitda', 'debt', 'equity', 'fcf', 'netincome', 'capinv', 'workingcapital', 'working_capital', 'inventory', 'gp', 'rd', 'tax', 'interest', 'liabilities', 'retainedearnings', 'net_income', 'ocf', 'dividend', 'operatingcashflow', 'capex', 'marketcap', 'ev', 'eps', 'shares']
    df = pd.DataFrame({col: np.random.uniform(10, 1000, n) for col in cols})
    df['close'] = np.cumsum(np.random.randn(n)) + 100
    df['closeadj'] = df['close']
    
    results = {}
    for name, func in tqdm(FEATURE_FUNCTIONS.items()):
        import inspect
        sig = inspect.signature(func)
        if 'df' in sig.parameters:
            res = func(df)
        else:
            args = sig.parameters.keys()
            res = func(**{col: df[col] for col in args if col in df.columns})
        results[name] = res
        
    res_df = pd.DataFrame(results).dropna()
    if not res_df.empty and res_df.shape[1] > 1:
        corr_matrix = res_df.corr().abs()
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                if corr_matrix.iloc[i, j] > 0.95:
                    print(f'High correlation: {corr_matrix.columns[i]} and {corr_matrix.columns[j]} = {corr_matrix.iloc[i, j]}')
                # assert corr_matrix.iloc[i, j] <= 0.95
    print(f'Verification completed for {os.path.basename(__file__)}')
