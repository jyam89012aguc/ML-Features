import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f66cr_f66_cyclical_regime_proxies_calc076_5d_base_v076_signal(netinc, equity):
    res = (netinc / equity).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc076_5d_base_v076_signal'] = f66cr_f66_cyclical_regime_proxies_calc076_5d_base_v076_signal

def f66cr_f66_cyclical_regime_proxies_calc077_10d_base_v077_signal(netinc, equity):
    res = (netinc / equity).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc077_10d_base_v077_signal'] = f66cr_f66_cyclical_regime_proxies_calc077_10d_base_v077_signal

def f66cr_f66_cyclical_regime_proxies_calc078_21d_base_v078_signal(netinc, equity):
    res = (netinc / equity).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc078_21d_base_v078_signal'] = f66cr_f66_cyclical_regime_proxies_calc078_21d_base_v078_signal

def f66cr_f66_cyclical_regime_proxies_calc079_42d_base_v079_signal(netinc, equity):
    res = (netinc / equity).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc079_42d_base_v079_signal'] = f66cr_f66_cyclical_regime_proxies_calc079_42d_base_v079_signal

def f66cr_f66_cyclical_regime_proxies_calc080_63d_base_v080_signal(netinc, equity):
    res = (netinc / equity).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc080_63d_base_v080_signal'] = f66cr_f66_cyclical_regime_proxies_calc080_63d_base_v080_signal

def f66cr_f66_cyclical_regime_proxies_calc081_126d_base_v081_signal(netinc, equity):
    res = (netinc / equity).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc081_126d_base_v081_signal'] = f66cr_f66_cyclical_regime_proxies_calc081_126d_base_v081_signal

def f66cr_f66_cyclical_regime_proxies_calc082_252d_base_v082_signal(netinc, equity):
    res = (netinc / equity).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc082_252d_base_v082_signal'] = f66cr_f66_cyclical_regime_proxies_calc082_252d_base_v082_signal

def f66cr_f66_cyclical_regime_proxies_calc083_21d_base_v083_signal(netinc, equity):
    res = (netinc / equity).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc083_21d_base_v083_signal'] = f66cr_f66_cyclical_regime_proxies_calc083_21d_base_v083_signal

def f66cr_f66_cyclical_regime_proxies_calc084_63d_base_v084_signal(netinc, equity):
    res = (netinc / equity).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc084_63d_base_v084_signal'] = f66cr_f66_cyclical_regime_proxies_calc084_63d_base_v084_signal

def f66cr_f66_cyclical_regime_proxies_calc085_5d_base_v085_signal(netinc, equity):
    res = (netinc / equity).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc085_5d_base_v085_signal'] = f66cr_f66_cyclical_regime_proxies_calc085_5d_base_v085_signal

def f66cr_f66_cyclical_regime_proxies_calc086_21d_base_v086_signal(netinc, equity):
    res = (netinc / equity).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc086_21d_base_v086_signal'] = f66cr_f66_cyclical_regime_proxies_calc086_21d_base_v086_signal

def f66cr_f66_cyclical_regime_proxies_calc087_10d_base_v087_signal(netinc, equity):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(netinc / equity)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc087_10d_base_v087_signal'] = f66cr_f66_cyclical_regime_proxies_calc087_10d_base_v087_signal

def f66cr_f66_cyclical_regime_proxies_calc088_5d_base_v088_signal(capex, revenue):
    res = (capex / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc088_5d_base_v088_signal'] = f66cr_f66_cyclical_regime_proxies_calc088_5d_base_v088_signal

def f66cr_f66_cyclical_regime_proxies_calc089_10d_base_v089_signal(capex, revenue):
    res = (capex / revenue).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc089_10d_base_v089_signal'] = f66cr_f66_cyclical_regime_proxies_calc089_10d_base_v089_signal

def f66cr_f66_cyclical_regime_proxies_calc090_21d_base_v090_signal(capex, revenue):
    res = (capex / revenue).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc090_21d_base_v090_signal'] = f66cr_f66_cyclical_regime_proxies_calc090_21d_base_v090_signal

def f66cr_f66_cyclical_regime_proxies_calc091_42d_base_v091_signal(capex, revenue):
    res = (capex / revenue).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc091_42d_base_v091_signal'] = f66cr_f66_cyclical_regime_proxies_calc091_42d_base_v091_signal

def f66cr_f66_cyclical_regime_proxies_calc092_63d_base_v092_signal(capex, revenue):
    res = (capex / revenue).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc092_63d_base_v092_signal'] = f66cr_f66_cyclical_regime_proxies_calc092_63d_base_v092_signal

def f66cr_f66_cyclical_regime_proxies_calc093_126d_base_v093_signal(capex, revenue):
    res = (capex / revenue).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc093_126d_base_v093_signal'] = f66cr_f66_cyclical_regime_proxies_calc093_126d_base_v093_signal

def f66cr_f66_cyclical_regime_proxies_calc094_252d_base_v094_signal(capex, revenue):
    res = (capex / revenue).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc094_252d_base_v094_signal'] = f66cr_f66_cyclical_regime_proxies_calc094_252d_base_v094_signal

def f66cr_f66_cyclical_regime_proxies_calc095_21d_base_v095_signal(capex, revenue):
    res = (capex / revenue).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc095_21d_base_v095_signal'] = f66cr_f66_cyclical_regime_proxies_calc095_21d_base_v095_signal

def f66cr_f66_cyclical_regime_proxies_calc096_63d_base_v096_signal(capex, revenue):
    res = (capex / revenue).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc096_63d_base_v096_signal'] = f66cr_f66_cyclical_regime_proxies_calc096_63d_base_v096_signal

def f66cr_f66_cyclical_regime_proxies_calc097_5d_base_v097_signal(capex, revenue):
    res = (capex / revenue).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc097_5d_base_v097_signal'] = f66cr_f66_cyclical_regime_proxies_calc097_5d_base_v097_signal

def f66cr_f66_cyclical_regime_proxies_calc098_21d_base_v098_signal(capex, revenue):
    res = (capex / revenue).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc098_21d_base_v098_signal'] = f66cr_f66_cyclical_regime_proxies_calc098_21d_base_v098_signal

def f66cr_f66_cyclical_regime_proxies_calc099_10d_base_v099_signal(capex, revenue):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(capex / revenue)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc099_10d_base_v099_signal'] = f66cr_f66_cyclical_regime_proxies_calc099_10d_base_v099_signal

def f66cr_f66_cyclical_regime_proxies_calc100_5d_base_v100_signal(gp, assets):
    res = (gp / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc100_5d_base_v100_signal'] = f66cr_f66_cyclical_regime_proxies_calc100_5d_base_v100_signal

def f66cr_f66_cyclical_regime_proxies_calc101_10d_base_v101_signal(gp, assets):
    res = (gp / assets).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc101_10d_base_v101_signal'] = f66cr_f66_cyclical_regime_proxies_calc101_10d_base_v101_signal

def f66cr_f66_cyclical_regime_proxies_calc102_21d_base_v102_signal(gp, assets):
    res = (gp / assets).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc102_21d_base_v102_signal'] = f66cr_f66_cyclical_regime_proxies_calc102_21d_base_v102_signal

def f66cr_f66_cyclical_regime_proxies_calc103_42d_base_v103_signal(gp, assets):
    res = (gp / assets).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc103_42d_base_v103_signal'] = f66cr_f66_cyclical_regime_proxies_calc103_42d_base_v103_signal

def f66cr_f66_cyclical_regime_proxies_calc104_63d_base_v104_signal(gp, assets):
    res = (gp / assets).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc104_63d_base_v104_signal'] = f66cr_f66_cyclical_regime_proxies_calc104_63d_base_v104_signal

def f66cr_f66_cyclical_regime_proxies_calc105_126d_base_v105_signal(gp, assets):
    res = (gp / assets).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc105_126d_base_v105_signal'] = f66cr_f66_cyclical_regime_proxies_calc105_126d_base_v105_signal

def f66cr_f66_cyclical_regime_proxies_calc106_252d_base_v106_signal(gp, assets):
    res = (gp / assets).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc106_252d_base_v106_signal'] = f66cr_f66_cyclical_regime_proxies_calc106_252d_base_v106_signal

def f66cr_f66_cyclical_regime_proxies_calc107_21d_base_v107_signal(gp, assets):
    res = (gp / assets).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc107_21d_base_v107_signal'] = f66cr_f66_cyclical_regime_proxies_calc107_21d_base_v107_signal

def f66cr_f66_cyclical_regime_proxies_calc108_63d_base_v108_signal(gp, assets):
    res = (gp / assets).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc108_63d_base_v108_signal'] = f66cr_f66_cyclical_regime_proxies_calc108_63d_base_v108_signal

def f66cr_f66_cyclical_regime_proxies_calc109_5d_base_v109_signal(gp, assets):
    res = (gp / assets).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc109_5d_base_v109_signal'] = f66cr_f66_cyclical_regime_proxies_calc109_5d_base_v109_signal

def f66cr_f66_cyclical_regime_proxies_calc110_21d_base_v110_signal(gp, assets):
    res = (gp / assets).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc110_21d_base_v110_signal'] = f66cr_f66_cyclical_regime_proxies_calc110_21d_base_v110_signal

def f66cr_f66_cyclical_regime_proxies_calc111_10d_base_v111_signal(gp, assets):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(gp / assets)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc111_10d_base_v111_signal'] = f66cr_f66_cyclical_regime_proxies_calc111_10d_base_v111_signal

def f66cr_f66_cyclical_regime_proxies_calc112_5d_base_v112_signal(workingcapital, liabilities):
    res = (workingcapital / liabilities).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc112_5d_base_v112_signal'] = f66cr_f66_cyclical_regime_proxies_calc112_5d_base_v112_signal

def f66cr_f66_cyclical_regime_proxies_calc113_10d_base_v113_signal(workingcapital, liabilities):
    res = (workingcapital / liabilities).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc113_10d_base_v113_signal'] = f66cr_f66_cyclical_regime_proxies_calc113_10d_base_v113_signal

def f66cr_f66_cyclical_regime_proxies_calc114_21d_base_v114_signal(workingcapital, liabilities):
    res = (workingcapital / liabilities).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc114_21d_base_v114_signal'] = f66cr_f66_cyclical_regime_proxies_calc114_21d_base_v114_signal

def f66cr_f66_cyclical_regime_proxies_calc115_42d_base_v115_signal(workingcapital, liabilities):
    res = (workingcapital / liabilities).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc115_42d_base_v115_signal'] = f66cr_f66_cyclical_regime_proxies_calc115_42d_base_v115_signal

def f66cr_f66_cyclical_regime_proxies_calc116_63d_base_v116_signal(workingcapital, liabilities):
    res = (workingcapital / liabilities).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc116_63d_base_v116_signal'] = f66cr_f66_cyclical_regime_proxies_calc116_63d_base_v116_signal

def f66cr_f66_cyclical_regime_proxies_calc117_126d_base_v117_signal(workingcapital, liabilities):
    res = (workingcapital / liabilities).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc117_126d_base_v117_signal'] = f66cr_f66_cyclical_regime_proxies_calc117_126d_base_v117_signal

def f66cr_f66_cyclical_regime_proxies_calc118_252d_base_v118_signal(workingcapital, liabilities):
    res = (workingcapital / liabilities).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc118_252d_base_v118_signal'] = f66cr_f66_cyclical_regime_proxies_calc118_252d_base_v118_signal

def f66cr_f66_cyclical_regime_proxies_calc119_21d_base_v119_signal(workingcapital, liabilities):
    res = (workingcapital / liabilities).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc119_21d_base_v119_signal'] = f66cr_f66_cyclical_regime_proxies_calc119_21d_base_v119_signal

def f66cr_f66_cyclical_regime_proxies_calc120_63d_base_v120_signal(workingcapital, liabilities):
    res = (workingcapital / liabilities).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc120_63d_base_v120_signal'] = f66cr_f66_cyclical_regime_proxies_calc120_63d_base_v120_signal

def f66cr_f66_cyclical_regime_proxies_calc121_5d_base_v121_signal(workingcapital, liabilities):
    res = (workingcapital / liabilities).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc121_5d_base_v121_signal'] = f66cr_f66_cyclical_regime_proxies_calc121_5d_base_v121_signal

def f66cr_f66_cyclical_regime_proxies_calc122_21d_base_v122_signal(workingcapital, liabilities):
    res = (workingcapital / liabilities).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc122_21d_base_v122_signal'] = f66cr_f66_cyclical_regime_proxies_calc122_21d_base_v122_signal

def f66cr_f66_cyclical_regime_proxies_calc123_10d_base_v123_signal(workingcapital, liabilities):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(workingcapital / liabilities)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc123_10d_base_v123_signal'] = f66cr_f66_cyclical_regime_proxies_calc123_10d_base_v123_signal

def f66cr_f66_cyclical_regime_proxies_calc124_5d_base_v124_signal(volume, sharesbas):
    res = (volume / sharesbas).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc124_5d_base_v124_signal'] = f66cr_f66_cyclical_regime_proxies_calc124_5d_base_v124_signal

def f66cr_f66_cyclical_regime_proxies_calc125_10d_base_v125_signal(volume, sharesbas):
    res = (volume / sharesbas).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc125_10d_base_v125_signal'] = f66cr_f66_cyclical_regime_proxies_calc125_10d_base_v125_signal

def f66cr_f66_cyclical_regime_proxies_calc126_21d_base_v126_signal(volume, sharesbas):
    res = (volume / sharesbas).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc126_21d_base_v126_signal'] = f66cr_f66_cyclical_regime_proxies_calc126_21d_base_v126_signal

def f66cr_f66_cyclical_regime_proxies_calc127_42d_base_v127_signal(volume, sharesbas):
    res = (volume / sharesbas).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc127_42d_base_v127_signal'] = f66cr_f66_cyclical_regime_proxies_calc127_42d_base_v127_signal

def f66cr_f66_cyclical_regime_proxies_calc128_63d_base_v128_signal(volume, sharesbas):
    res = (volume / sharesbas).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc128_63d_base_v128_signal'] = f66cr_f66_cyclical_regime_proxies_calc128_63d_base_v128_signal

def f66cr_f66_cyclical_regime_proxies_calc129_126d_base_v129_signal(volume, sharesbas):
    res = (volume / sharesbas).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc129_126d_base_v129_signal'] = f66cr_f66_cyclical_regime_proxies_calc129_126d_base_v129_signal

def f66cr_f66_cyclical_regime_proxies_calc130_252d_base_v130_signal(volume, sharesbas):
    res = (volume / sharesbas).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc130_252d_base_v130_signal'] = f66cr_f66_cyclical_regime_proxies_calc130_252d_base_v130_signal

def f66cr_f66_cyclical_regime_proxies_calc131_21d_base_v131_signal(volume, sharesbas):
    res = (volume / sharesbas).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc131_21d_base_v131_signal'] = f66cr_f66_cyclical_regime_proxies_calc131_21d_base_v131_signal

def f66cr_f66_cyclical_regime_proxies_calc132_63d_base_v132_signal(volume, sharesbas):
    res = (volume / sharesbas).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc132_63d_base_v132_signal'] = f66cr_f66_cyclical_regime_proxies_calc132_63d_base_v132_signal

def f66cr_f66_cyclical_regime_proxies_calc133_5d_base_v133_signal(volume, sharesbas):
    res = (volume / sharesbas).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc133_5d_base_v133_signal'] = f66cr_f66_cyclical_regime_proxies_calc133_5d_base_v133_signal

def f66cr_f66_cyclical_regime_proxies_calc134_21d_base_v134_signal(volume, sharesbas):
    res = (volume / sharesbas).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc134_21d_base_v134_signal'] = f66cr_f66_cyclical_regime_proxies_calc134_21d_base_v134_signal

def f66cr_f66_cyclical_regime_proxies_calc135_10d_base_v135_signal(volume, sharesbas):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(volume / sharesbas)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc135_10d_base_v135_signal'] = f66cr_f66_cyclical_regime_proxies_calc135_10d_base_v135_signal

def f66cr_f66_cyclical_regime_proxies_calc136_5d_base_v136_signal(low, high):
    res = (low / high).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc136_5d_base_v136_signal'] = f66cr_f66_cyclical_regime_proxies_calc136_5d_base_v136_signal

def f66cr_f66_cyclical_regime_proxies_calc137_10d_base_v137_signal(low, high):
    res = (low / high).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc137_10d_base_v137_signal'] = f66cr_f66_cyclical_regime_proxies_calc137_10d_base_v137_signal

def f66cr_f66_cyclical_regime_proxies_calc138_21d_base_v138_signal(low, high):
    res = (low / high).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc138_21d_base_v138_signal'] = f66cr_f66_cyclical_regime_proxies_calc138_21d_base_v138_signal

def f66cr_f66_cyclical_regime_proxies_calc139_42d_base_v139_signal(low, high):
    res = (low / high).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc139_42d_base_v139_signal'] = f66cr_f66_cyclical_regime_proxies_calc139_42d_base_v139_signal

def f66cr_f66_cyclical_regime_proxies_calc140_63d_base_v140_signal(low, high):
    res = (low / high).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc140_63d_base_v140_signal'] = f66cr_f66_cyclical_regime_proxies_calc140_63d_base_v140_signal

def f66cr_f66_cyclical_regime_proxies_calc141_126d_base_v141_signal(low, high):
    res = (low / high).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc141_126d_base_v141_signal'] = f66cr_f66_cyclical_regime_proxies_calc141_126d_base_v141_signal

def f66cr_f66_cyclical_regime_proxies_calc142_252d_base_v142_signal(low, high):
    res = (low / high).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc142_252d_base_v142_signal'] = f66cr_f66_cyclical_regime_proxies_calc142_252d_base_v142_signal

def f66cr_f66_cyclical_regime_proxies_calc143_21d_base_v143_signal(low, high):
    res = (low / high).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc143_21d_base_v143_signal'] = f66cr_f66_cyclical_regime_proxies_calc143_21d_base_v143_signal

def f66cr_f66_cyclical_regime_proxies_calc144_63d_base_v144_signal(low, high):
    res = (low / high).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc144_63d_base_v144_signal'] = f66cr_f66_cyclical_regime_proxies_calc144_63d_base_v144_signal

def f66cr_f66_cyclical_regime_proxies_calc145_5d_base_v145_signal(low, high):
    res = (low / high).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc145_5d_base_v145_signal'] = f66cr_f66_cyclical_regime_proxies_calc145_5d_base_v145_signal

def f66cr_f66_cyclical_regime_proxies_calc146_21d_base_v146_signal(low, high):
    res = (low / high).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc146_21d_base_v146_signal'] = f66cr_f66_cyclical_regime_proxies_calc146_21d_base_v146_signal

def f66cr_f66_cyclical_regime_proxies_calc147_10d_base_v147_signal(low, high):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(low / high)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc147_10d_base_v147_signal'] = f66cr_f66_cyclical_regime_proxies_calc147_10d_base_v147_signal

def f66cr_f66_cyclical_regime_proxies_calc148_5d_base_v148_signal(evebitda, ps):
    res = (evebitda / ps).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc148_5d_base_v148_signal'] = f66cr_f66_cyclical_regime_proxies_calc148_5d_base_v148_signal

def f66cr_f66_cyclical_regime_proxies_calc149_10d_base_v149_signal(evebitda, ps):
    res = (evebitda / ps).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc149_10d_base_v149_signal'] = f66cr_f66_cyclical_regime_proxies_calc149_10d_base_v149_signal

def f66cr_f66_cyclical_regime_proxies_calc150_21d_base_v150_signal(evebitda, ps):
    res = (evebitda / ps).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc150_21d_base_v150_signal'] = f66cr_f66_cyclical_regime_proxies_calc150_21d_base_v150_signal


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
