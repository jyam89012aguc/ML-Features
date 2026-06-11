import pandas as pd
import numpy as np
FEATURE_FUNCTIONS = {}

def f109o_f109_operating_cash_flow_efficiency_momentum_calc076_126d_base_v076_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc076_126d_base_v076_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc076_126d_base_v076_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc077_126d_base_v077_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc077_126d_base_v077_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc077_126d_base_v077_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc078_42d_base_v078_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(42).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc078_42d_base_v078_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc078_42d_base_v078_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc079_5d_base_v079_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc079_5d_base_v079_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc079_5d_base_v079_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc080_200d_base_v080_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(200)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc080_200d_base_v080_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc080_200d_base_v080_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc081_10d_base_v081_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(10).mean()) / v_003.rolling(10).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc081_10d_base_v081_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc081_10d_base_v081_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc082_10d_base_v082_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(10)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc082_10d_base_v082_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc082_10d_base_v082_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc083_84d_base_v083_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc083_84d_base_v083_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc083_84d_base_v083_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc084_200d_base_v084_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(200).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc084_200d_base_v084_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc084_200d_base_v084_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc085_5d_base_v085_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc085_5d_base_v085_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc085_5d_base_v085_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc086_126d_base_v086_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc086_126d_base_v086_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc086_126d_base_v086_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc087_126d_base_v087_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(126)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc087_126d_base_v087_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc087_126d_base_v087_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc088_42d_base_v088_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(42)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc088_42d_base_v088_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc088_42d_base_v088_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc089_126d_base_v089_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc089_126d_base_v089_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc089_126d_base_v089_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc090_5d_base_v090_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc090_5d_base_v090_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc090_5d_base_v090_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc091_150d_base_v091_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc091_150d_base_v091_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc091_150d_base_v091_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc092_42d_base_v092_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc092_42d_base_v092_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc092_42d_base_v092_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc093_126d_base_v093_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(126).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc093_126d_base_v093_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc093_126d_base_v093_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc094_5d_base_v094_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc094_5d_base_v094_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc094_5d_base_v094_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc095_200d_base_v095_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(200).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc095_200d_base_v095_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc095_200d_base_v095_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc096_63d_base_v096_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc096_63d_base_v096_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc096_63d_base_v096_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc097_63d_base_v097_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(63).mean()) / v_003.rolling(63).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc097_63d_base_v097_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc097_63d_base_v097_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc098_252d_base_v098_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc098_252d_base_v098_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc098_252d_base_v098_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc099_105d_base_v099_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc099_105d_base_v099_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc099_105d_base_v099_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc100_126d_base_v100_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc100_126d_base_v100_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc100_126d_base_v100_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc101_105d_base_v101_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(105)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc101_105d_base_v101_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc101_105d_base_v101_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc102_252d_base_v102_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc102_252d_base_v102_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc102_252d_base_v102_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc103_5d_base_v103_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc103_5d_base_v103_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc103_5d_base_v103_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc104_63d_base_v104_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc104_63d_base_v104_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc104_63d_base_v104_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc105_10d_base_v105_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(10).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc105_10d_base_v105_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc105_10d_base_v105_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc106_252d_base_v106_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc106_252d_base_v106_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc106_252d_base_v106_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc107_63d_base_v107_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(63).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc107_63d_base_v107_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc107_63d_base_v107_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc108_105d_base_v108_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(105)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc108_105d_base_v108_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc108_105d_base_v108_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc109_5d_base_v109_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(5).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc109_5d_base_v109_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc109_5d_base_v109_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc110_150d_base_v110_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc110_150d_base_v110_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc110_150d_base_v110_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc111_42d_base_v111_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc111_42d_base_v111_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc111_42d_base_v111_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc112_200d_base_v112_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(200).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc112_200d_base_v112_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc112_200d_base_v112_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc113_5d_base_v113_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc113_5d_base_v113_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc113_5d_base_v113_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc114_105d_base_v114_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc114_105d_base_v114_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc114_105d_base_v114_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc115_200d_base_v115_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc115_200d_base_v115_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc115_200d_base_v115_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc116_63d_base_v116_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(63)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc116_63d_base_v116_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc116_63d_base_v116_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc117_126d_base_v117_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(126)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc117_126d_base_v117_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc117_126d_base_v117_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc118_84d_base_v118_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(84).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc118_84d_base_v118_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc118_84d_base_v118_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc119_200d_base_v119_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(200)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc119_200d_base_v119_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc119_200d_base_v119_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc120_105d_base_v120_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(105).mean()) / v_003.rolling(105).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc120_105d_base_v120_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc120_105d_base_v120_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc121_63d_base_v121_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(63)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc121_63d_base_v121_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc121_63d_base_v121_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc122_200d_base_v122_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc122_200d_base_v122_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc122_200d_base_v122_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc123_21d_base_v123_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc123_21d_base_v123_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc123_21d_base_v123_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc124_150d_base_v124_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc124_150d_base_v124_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc124_150d_base_v124_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc125_5d_base_v125_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc125_5d_base_v125_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc125_5d_base_v125_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc126_200d_base_v126_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(200).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc126_200d_base_v126_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc126_200d_base_v126_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc127_63d_base_v127_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(63).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc127_63d_base_v127_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc127_63d_base_v127_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc128_150d_base_v128_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc128_150d_base_v128_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc128_150d_base_v128_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc129_252d_base_v129_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc129_252d_base_v129_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc129_252d_base_v129_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc130_150d_base_v130_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(150).mean()) / v_003.rolling(150).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc130_150d_base_v130_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc130_150d_base_v130_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc131_84d_base_v131_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(84)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc131_84d_base_v131_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc131_84d_base_v131_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc132_5d_base_v132_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc132_5d_base_v132_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc132_5d_base_v132_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc133_126d_base_v133_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc133_126d_base_v133_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc133_126d_base_v133_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc134_105d_base_v134_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(105)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc134_105d_base_v134_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc134_105d_base_v134_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc135_42d_base_v135_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc135_42d_base_v135_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc135_42d_base_v135_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc136_200d_base_v136_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc136_200d_base_v136_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc136_200d_base_v136_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc137_21d_base_v137_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc137_21d_base_v137_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc137_21d_base_v137_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc138_105d_base_v138_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc138_105d_base_v138_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc138_105d_base_v138_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc139_63d_base_v139_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc139_63d_base_v139_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc139_63d_base_v139_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc140_42d_base_v140_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc140_42d_base_v140_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc140_42d_base_v140_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc141_150d_base_v141_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc141_150d_base_v141_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc141_150d_base_v141_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc142_5d_base_v142_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc142_5d_base_v142_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc142_5d_base_v142_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc143_5d_base_v143_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc143_5d_base_v143_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc143_5d_base_v143_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc144_10d_base_v144_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(10).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc144_10d_base_v144_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc144_10d_base_v144_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc145_42d_base_v145_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc145_42d_base_v145_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc145_42d_base_v145_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc146_252d_base_v146_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc146_252d_base_v146_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc146_252d_base_v146_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc147_10d_base_v147_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc147_10d_base_v147_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc147_10d_base_v147_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc148_150d_base_v148_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc148_150d_base_v148_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc148_150d_base_v148_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc149_84d_base_v149_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(84)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc149_84d_base_v149_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc149_84d_base_v149_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc150_21d_base_v150_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc150_21d_base_v150_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc150_21d_base_v150_signal


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
