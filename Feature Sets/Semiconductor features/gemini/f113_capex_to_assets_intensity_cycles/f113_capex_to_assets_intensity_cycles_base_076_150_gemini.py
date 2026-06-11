import pandas as pd
import numpy as np
FEATURE_FUNCTIONS = {}

def f113c_f113_capex_to_assets_intensity_cycles_calc076_150d_base_v076_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc076_150d_base_v076_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc076_150d_base_v076_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc077_21d_base_v077_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc077_21d_base_v077_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc077_21d_base_v077_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc078_10d_base_v078_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(10).mean()) / v_003.rolling(10).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc078_10d_base_v078_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc078_10d_base_v078_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc079_42d_base_v079_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc079_42d_base_v079_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc079_42d_base_v079_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc080_10d_base_v080_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(10).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc080_10d_base_v080_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc080_10d_base_v080_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc081_21d_base_v081_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc081_21d_base_v081_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc081_21d_base_v081_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc082_126d_base_v082_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(126).mean()) / v_003.rolling(126).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc082_126d_base_v082_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc082_126d_base_v082_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc083_200d_base_v083_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc083_200d_base_v083_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc083_200d_base_v083_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc084_10d_base_v084_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc084_10d_base_v084_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc084_10d_base_v084_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc085_84d_base_v085_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(84).mean()) / v_003.rolling(84).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc085_84d_base_v085_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc085_84d_base_v085_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc086_252d_base_v086_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(252)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc086_252d_base_v086_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc086_252d_base_v086_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc087_42d_base_v087_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(42)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc087_42d_base_v087_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc087_42d_base_v087_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc088_150d_base_v088_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc088_150d_base_v088_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc088_150d_base_v088_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc089_63d_base_v089_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(63).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc089_63d_base_v089_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc089_63d_base_v089_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc090_10d_base_v090_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc090_10d_base_v090_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc090_10d_base_v090_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc091_200d_base_v091_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc091_200d_base_v091_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc091_200d_base_v091_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc092_21d_base_v092_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc092_21d_base_v092_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc092_21d_base_v092_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc093_5d_base_v093_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc093_5d_base_v093_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc093_5d_base_v093_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc094_200d_base_v094_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(200).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc094_200d_base_v094_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc094_200d_base_v094_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc095_84d_base_v095_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(84).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc095_84d_base_v095_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc095_84d_base_v095_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc096_150d_base_v096_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc096_150d_base_v096_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc096_150d_base_v096_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc097_200d_base_v097_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc097_200d_base_v097_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc097_200d_base_v097_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc098_42d_base_v098_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc098_42d_base_v098_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc098_42d_base_v098_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc099_126d_base_v099_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc099_126d_base_v099_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc099_126d_base_v099_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc100_10d_base_v100_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc100_10d_base_v100_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc100_10d_base_v100_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc101_150d_base_v101_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc101_150d_base_v101_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc101_150d_base_v101_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc102_84d_base_v102_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(84)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc102_84d_base_v102_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc102_84d_base_v102_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc103_5d_base_v103_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc103_5d_base_v103_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc103_5d_base_v103_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc104_105d_base_v104_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc104_105d_base_v104_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc104_105d_base_v104_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc105_105d_base_v105_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(105)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc105_105d_base_v105_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc105_105d_base_v105_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc106_21d_base_v106_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc106_21d_base_v106_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc106_21d_base_v106_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc107_105d_base_v107_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc107_105d_base_v107_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc107_105d_base_v107_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc108_42d_base_v108_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc108_42d_base_v108_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc108_42d_base_v108_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc109_126d_base_v109_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc109_126d_base_v109_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc109_126d_base_v109_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc110_42d_base_v110_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(42)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc110_42d_base_v110_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc110_42d_base_v110_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc111_126d_base_v111_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc111_126d_base_v111_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc111_126d_base_v111_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc112_21d_base_v112_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc112_21d_base_v112_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc112_21d_base_v112_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc113_10d_base_v113_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc113_10d_base_v113_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc113_10d_base_v113_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc114_21d_base_v114_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc114_21d_base_v114_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc114_21d_base_v114_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc115_63d_base_v115_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc115_63d_base_v115_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc115_63d_base_v115_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc116_10d_base_v116_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc116_10d_base_v116_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc116_10d_base_v116_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc117_84d_base_v117_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc117_84d_base_v117_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc117_84d_base_v117_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc118_252d_base_v118_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc118_252d_base_v118_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc118_252d_base_v118_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc119_10d_base_v119_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc119_10d_base_v119_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc119_10d_base_v119_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc120_21d_base_v120_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(21)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc120_21d_base_v120_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc120_21d_base_v120_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc121_252d_base_v121_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc121_252d_base_v121_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc121_252d_base_v121_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc122_200d_base_v122_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(200)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc122_200d_base_v122_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc122_200d_base_v122_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc123_42d_base_v123_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc123_42d_base_v123_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc123_42d_base_v123_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc124_84d_base_v124_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(84).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc124_84d_base_v124_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc124_84d_base_v124_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc125_200d_base_v125_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc125_200d_base_v125_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc125_200d_base_v125_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc126_63d_base_v126_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(63).mean()) / v_003.rolling(63).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc126_63d_base_v126_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc126_63d_base_v126_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc127_42d_base_v127_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(42).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc127_42d_base_v127_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc127_42d_base_v127_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc128_10d_base_v128_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(10).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc128_10d_base_v128_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc128_10d_base_v128_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc129_105d_base_v129_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc129_105d_base_v129_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc129_105d_base_v129_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc130_84d_base_v130_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc130_84d_base_v130_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc130_84d_base_v130_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc131_252d_base_v131_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc131_252d_base_v131_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc131_252d_base_v131_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc132_126d_base_v132_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc132_126d_base_v132_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc132_126d_base_v132_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc133_21d_base_v133_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc133_21d_base_v133_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc133_21d_base_v133_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc134_10d_base_v134_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc134_10d_base_v134_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc134_10d_base_v134_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc135_5d_base_v135_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc135_5d_base_v135_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc135_5d_base_v135_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc136_63d_base_v136_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(63).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc136_63d_base_v136_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc136_63d_base_v136_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc137_200d_base_v137_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(200).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc137_200d_base_v137_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc137_200d_base_v137_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc138_84d_base_v138_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc138_84d_base_v138_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc138_84d_base_v138_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc139_200d_base_v139_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(200)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc139_200d_base_v139_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc139_200d_base_v139_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc140_150d_base_v140_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc140_150d_base_v140_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc140_150d_base_v140_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc141_84d_base_v141_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc141_84d_base_v141_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc141_84d_base_v141_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc142_63d_base_v142_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(63)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc142_63d_base_v142_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc142_63d_base_v142_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc143_42d_base_v143_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc143_42d_base_v143_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc143_42d_base_v143_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc144_105d_base_v144_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc144_105d_base_v144_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc144_105d_base_v144_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc145_21d_base_v145_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc145_21d_base_v145_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc145_21d_base_v145_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc146_200d_base_v146_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(200)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc146_200d_base_v146_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc146_200d_base_v146_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc147_5d_base_v147_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc147_5d_base_v147_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc147_5d_base_v147_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc148_252d_base_v148_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc148_252d_base_v148_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc148_252d_base_v148_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc149_126d_base_v149_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(126).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc149_126d_base_v149_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc149_126d_base_v149_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc150_63d_base_v150_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc150_63d_base_v150_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc150_63d_base_v150_signal


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
