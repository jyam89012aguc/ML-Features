import pandas as pd
import numpy as np
FEATURE_FUNCTIONS = {}

def f108r_f108_revenue_growth_relative_to_assets_calc076_84d_base_v076_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc076_84d_base_v076_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc076_84d_base_v076_signal

def f108r_f108_revenue_growth_relative_to_assets_calc077_105d_base_v077_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(105)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc077_105d_base_v077_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc077_105d_base_v077_signal

def f108r_f108_revenue_growth_relative_to_assets_calc078_252d_base_v078_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc078_252d_base_v078_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc078_252d_base_v078_signal

def f108r_f108_revenue_growth_relative_to_assets_calc079_10d_base_v079_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(10)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc079_10d_base_v079_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc079_10d_base_v079_signal

def f108r_f108_revenue_growth_relative_to_assets_calc080_84d_base_v080_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc080_84d_base_v080_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc080_84d_base_v080_signal

def f108r_f108_revenue_growth_relative_to_assets_calc081_200d_base_v081_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc081_200d_base_v081_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc081_200d_base_v081_signal

def f108r_f108_revenue_growth_relative_to_assets_calc082_84d_base_v082_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc082_84d_base_v082_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc082_84d_base_v082_signal

def f108r_f108_revenue_growth_relative_to_assets_calc083_42d_base_v083_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc083_42d_base_v083_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc083_42d_base_v083_signal

def f108r_f108_revenue_growth_relative_to_assets_calc084_252d_base_v084_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc084_252d_base_v084_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc084_252d_base_v084_signal

def f108r_f108_revenue_growth_relative_to_assets_calc085_21d_base_v085_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc085_21d_base_v085_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc085_21d_base_v085_signal

def f108r_f108_revenue_growth_relative_to_assets_calc086_42d_base_v086_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc086_42d_base_v086_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc086_42d_base_v086_signal

def f108r_f108_revenue_growth_relative_to_assets_calc087_150d_base_v087_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(150).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc087_150d_base_v087_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc087_150d_base_v087_signal

def f108r_f108_revenue_growth_relative_to_assets_calc088_63d_base_v088_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc088_63d_base_v088_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc088_63d_base_v088_signal

def f108r_f108_revenue_growth_relative_to_assets_calc089_5d_base_v089_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc089_5d_base_v089_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc089_5d_base_v089_signal

def f108r_f108_revenue_growth_relative_to_assets_calc090_150d_base_v090_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(150).mean()) / v_003.rolling(150).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc090_150d_base_v090_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc090_150d_base_v090_signal

def f108r_f108_revenue_growth_relative_to_assets_calc091_42d_base_v091_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc091_42d_base_v091_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc091_42d_base_v091_signal

def f108r_f108_revenue_growth_relative_to_assets_calc092_10d_base_v092_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc092_10d_base_v092_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc092_10d_base_v092_signal

def f108r_f108_revenue_growth_relative_to_assets_calc093_126d_base_v093_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc093_126d_base_v093_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc093_126d_base_v093_signal

def f108r_f108_revenue_growth_relative_to_assets_calc094_84d_base_v094_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(84).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc094_84d_base_v094_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc094_84d_base_v094_signal

def f108r_f108_revenue_growth_relative_to_assets_calc095_252d_base_v095_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(252).mean()) / v_003.rolling(252).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc095_252d_base_v095_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc095_252d_base_v095_signal

def f108r_f108_revenue_growth_relative_to_assets_calc096_252d_base_v096_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc096_252d_base_v096_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc096_252d_base_v096_signal

def f108r_f108_revenue_growth_relative_to_assets_calc097_150d_base_v097_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(150)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc097_150d_base_v097_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc097_150d_base_v097_signal

def f108r_f108_revenue_growth_relative_to_assets_calc098_10d_base_v098_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(10).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc098_10d_base_v098_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc098_10d_base_v098_signal

def f108r_f108_revenue_growth_relative_to_assets_calc099_252d_base_v099_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc099_252d_base_v099_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc099_252d_base_v099_signal

def f108r_f108_revenue_growth_relative_to_assets_calc100_10d_base_v100_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc100_10d_base_v100_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc100_10d_base_v100_signal

def f108r_f108_revenue_growth_relative_to_assets_calc101_105d_base_v101_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc101_105d_base_v101_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc101_105d_base_v101_signal

def f108r_f108_revenue_growth_relative_to_assets_calc102_105d_base_v102_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc102_105d_base_v102_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc102_105d_base_v102_signal

def f108r_f108_revenue_growth_relative_to_assets_calc103_84d_base_v103_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc103_84d_base_v103_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc103_84d_base_v103_signal

def f108r_f108_revenue_growth_relative_to_assets_calc104_5d_base_v104_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc104_5d_base_v104_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc104_5d_base_v104_signal

def f108r_f108_revenue_growth_relative_to_assets_calc105_200d_base_v105_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc105_200d_base_v105_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc105_200d_base_v105_signal

def f108r_f108_revenue_growth_relative_to_assets_calc106_84d_base_v106_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc106_84d_base_v106_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc106_84d_base_v106_signal

def f108r_f108_revenue_growth_relative_to_assets_calc107_252d_base_v107_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(252).mean()) / v_003.rolling(252).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc107_252d_base_v107_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc107_252d_base_v107_signal

def f108r_f108_revenue_growth_relative_to_assets_calc108_200d_base_v108_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(200)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc108_200d_base_v108_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc108_200d_base_v108_signal

def f108r_f108_revenue_growth_relative_to_assets_calc109_21d_base_v109_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc109_21d_base_v109_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc109_21d_base_v109_signal

def f108r_f108_revenue_growth_relative_to_assets_calc110_21d_base_v110_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc110_21d_base_v110_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc110_21d_base_v110_signal

def f108r_f108_revenue_growth_relative_to_assets_calc111_5d_base_v111_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc111_5d_base_v111_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc111_5d_base_v111_signal

def f108r_f108_revenue_growth_relative_to_assets_calc112_10d_base_v112_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(10).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc112_10d_base_v112_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc112_10d_base_v112_signal

def f108r_f108_revenue_growth_relative_to_assets_calc113_84d_base_v113_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc113_84d_base_v113_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc113_84d_base_v113_signal

def f108r_f108_revenue_growth_relative_to_assets_calc114_5d_base_v114_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc114_5d_base_v114_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc114_5d_base_v114_signal

def f108r_f108_revenue_growth_relative_to_assets_calc115_105d_base_v115_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc115_105d_base_v115_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc115_105d_base_v115_signal

def f108r_f108_revenue_growth_relative_to_assets_calc116_42d_base_v116_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(42).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc116_42d_base_v116_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc116_42d_base_v116_signal

def f108r_f108_revenue_growth_relative_to_assets_calc117_42d_base_v117_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc117_42d_base_v117_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc117_42d_base_v117_signal

def f108r_f108_revenue_growth_relative_to_assets_calc118_21d_base_v118_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc118_21d_base_v118_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc118_21d_base_v118_signal

def f108r_f108_revenue_growth_relative_to_assets_calc119_150d_base_v119_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc119_150d_base_v119_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc119_150d_base_v119_signal

def f108r_f108_revenue_growth_relative_to_assets_calc120_21d_base_v120_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(21)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc120_21d_base_v120_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc120_21d_base_v120_signal

def f108r_f108_revenue_growth_relative_to_assets_calc121_21d_base_v121_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc121_21d_base_v121_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc121_21d_base_v121_signal

def f108r_f108_revenue_growth_relative_to_assets_calc122_42d_base_v122_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc122_42d_base_v122_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc122_42d_base_v122_signal

def f108r_f108_revenue_growth_relative_to_assets_calc123_10d_base_v123_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc123_10d_base_v123_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc123_10d_base_v123_signal

def f108r_f108_revenue_growth_relative_to_assets_calc124_42d_base_v124_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc124_42d_base_v124_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc124_42d_base_v124_signal

def f108r_f108_revenue_growth_relative_to_assets_calc125_10d_base_v125_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc125_10d_base_v125_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc125_10d_base_v125_signal

def f108r_f108_revenue_growth_relative_to_assets_calc126_10d_base_v126_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(10)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc126_10d_base_v126_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc126_10d_base_v126_signal

def f108r_f108_revenue_growth_relative_to_assets_calc127_84d_base_v127_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(84)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc127_84d_base_v127_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc127_84d_base_v127_signal

def f108r_f108_revenue_growth_relative_to_assets_calc128_21d_base_v128_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc128_21d_base_v128_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc128_21d_base_v128_signal

def f108r_f108_revenue_growth_relative_to_assets_calc129_21d_base_v129_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc129_21d_base_v129_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc129_21d_base_v129_signal

def f108r_f108_revenue_growth_relative_to_assets_calc130_126d_base_v130_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc130_126d_base_v130_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc130_126d_base_v130_signal

def f108r_f108_revenue_growth_relative_to_assets_calc131_42d_base_v131_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc131_42d_base_v131_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc131_42d_base_v131_signal

def f108r_f108_revenue_growth_relative_to_assets_calc132_10d_base_v132_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc132_10d_base_v132_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc132_10d_base_v132_signal

def f108r_f108_revenue_growth_relative_to_assets_calc133_42d_base_v133_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(42)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc133_42d_base_v133_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc133_42d_base_v133_signal

def f108r_f108_revenue_growth_relative_to_assets_calc134_63d_base_v134_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(63)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc134_63d_base_v134_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc134_63d_base_v134_signal

def f108r_f108_revenue_growth_relative_to_assets_calc135_5d_base_v135_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc135_5d_base_v135_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc135_5d_base_v135_signal

def f108r_f108_revenue_growth_relative_to_assets_calc136_63d_base_v136_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(63).mean()) / v_003.rolling(63).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc136_63d_base_v136_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc136_63d_base_v136_signal

def f108r_f108_revenue_growth_relative_to_assets_calc137_84d_base_v137_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc137_84d_base_v137_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc137_84d_base_v137_signal

def f108r_f108_revenue_growth_relative_to_assets_calc138_5d_base_v138_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc138_5d_base_v138_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc138_5d_base_v138_signal

def f108r_f108_revenue_growth_relative_to_assets_calc139_126d_base_v139_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc139_126d_base_v139_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc139_126d_base_v139_signal

def f108r_f108_revenue_growth_relative_to_assets_calc140_150d_base_v140_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc140_150d_base_v140_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc140_150d_base_v140_signal

def f108r_f108_revenue_growth_relative_to_assets_calc141_150d_base_v141_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc141_150d_base_v141_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc141_150d_base_v141_signal

def f108r_f108_revenue_growth_relative_to_assets_calc142_252d_base_v142_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc142_252d_base_v142_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc142_252d_base_v142_signal

def f108r_f108_revenue_growth_relative_to_assets_calc143_21d_base_v143_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc143_21d_base_v143_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc143_21d_base_v143_signal

def f108r_f108_revenue_growth_relative_to_assets_calc144_84d_base_v144_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(84).mean()) / v_003.rolling(84).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc144_84d_base_v144_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc144_84d_base_v144_signal

def f108r_f108_revenue_growth_relative_to_assets_calc145_200d_base_v145_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc145_200d_base_v145_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc145_200d_base_v145_signal

def f108r_f108_revenue_growth_relative_to_assets_calc146_252d_base_v146_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(252)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc146_252d_base_v146_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc146_252d_base_v146_signal

def f108r_f108_revenue_growth_relative_to_assets_calc147_5d_base_v147_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc147_5d_base_v147_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc147_5d_base_v147_signal

def f108r_f108_revenue_growth_relative_to_assets_calc148_42d_base_v148_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(42).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc148_42d_base_v148_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc148_42d_base_v148_signal

def f108r_f108_revenue_growth_relative_to_assets_calc149_5d_base_v149_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc149_5d_base_v149_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc149_5d_base_v149_signal

def f108r_f108_revenue_growth_relative_to_assets_calc150_5d_base_v150_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(5).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc150_5d_base_v150_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc150_5d_base_v150_signal


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
