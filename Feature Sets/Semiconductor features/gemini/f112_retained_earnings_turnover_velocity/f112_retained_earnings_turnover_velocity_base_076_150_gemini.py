import pandas as pd
import numpy as np
FEATURE_FUNCTIONS = {}

def f112r_f112_retained_earnings_turnover_velocity_calc076_252d_base_v076_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(252)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc076_252d_base_v076_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc076_252d_base_v076_signal

def f112r_f112_retained_earnings_turnover_velocity_calc077_10d_base_v077_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(10).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc077_10d_base_v077_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc077_10d_base_v077_signal

def f112r_f112_retained_earnings_turnover_velocity_calc078_10d_base_v078_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(10)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc078_10d_base_v078_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc078_10d_base_v078_signal

def f112r_f112_retained_earnings_turnover_velocity_calc079_42d_base_v079_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc079_42d_base_v079_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc079_42d_base_v079_signal

def f112r_f112_retained_earnings_turnover_velocity_calc080_42d_base_v080_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(42)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc080_42d_base_v080_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc080_42d_base_v080_signal

def f112r_f112_retained_earnings_turnover_velocity_calc081_5d_base_v081_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc081_5d_base_v081_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc081_5d_base_v081_signal

def f112r_f112_retained_earnings_turnover_velocity_calc082_126d_base_v082_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc082_126d_base_v082_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc082_126d_base_v082_signal

def f112r_f112_retained_earnings_turnover_velocity_calc083_5d_base_v083_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc083_5d_base_v083_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc083_5d_base_v083_signal

def f112r_f112_retained_earnings_turnover_velocity_calc084_63d_base_v084_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc084_63d_base_v084_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc084_63d_base_v084_signal

def f112r_f112_retained_earnings_turnover_velocity_calc085_150d_base_v085_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc085_150d_base_v085_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc085_150d_base_v085_signal

def f112r_f112_retained_earnings_turnover_velocity_calc086_10d_base_v086_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(10).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc086_10d_base_v086_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc086_10d_base_v086_signal

def f112r_f112_retained_earnings_turnover_velocity_calc087_42d_base_v087_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc087_42d_base_v087_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc087_42d_base_v087_signal

def f112r_f112_retained_earnings_turnover_velocity_calc088_150d_base_v088_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc088_150d_base_v088_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc088_150d_base_v088_signal

def f112r_f112_retained_earnings_turnover_velocity_calc089_150d_base_v089_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc089_150d_base_v089_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc089_150d_base_v089_signal

def f112r_f112_retained_earnings_turnover_velocity_calc090_5d_base_v090_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(5).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc090_5d_base_v090_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc090_5d_base_v090_signal

def f112r_f112_retained_earnings_turnover_velocity_calc091_105d_base_v091_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc091_105d_base_v091_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc091_105d_base_v091_signal

def f112r_f112_retained_earnings_turnover_velocity_calc092_5d_base_v092_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc092_5d_base_v092_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc092_5d_base_v092_signal

def f112r_f112_retained_earnings_turnover_velocity_calc093_252d_base_v093_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(252)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc093_252d_base_v093_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc093_252d_base_v093_signal

def f112r_f112_retained_earnings_turnover_velocity_calc094_150d_base_v094_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc094_150d_base_v094_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc094_150d_base_v094_signal

def f112r_f112_retained_earnings_turnover_velocity_calc095_252d_base_v095_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc095_252d_base_v095_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc095_252d_base_v095_signal

def f112r_f112_retained_earnings_turnover_velocity_calc096_5d_base_v096_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc096_5d_base_v096_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc096_5d_base_v096_signal

def f112r_f112_retained_earnings_turnover_velocity_calc097_42d_base_v097_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(42).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc097_42d_base_v097_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc097_42d_base_v097_signal

def f112r_f112_retained_earnings_turnover_velocity_calc098_252d_base_v098_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc098_252d_base_v098_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc098_252d_base_v098_signal

def f112r_f112_retained_earnings_turnover_velocity_calc099_5d_base_v099_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc099_5d_base_v099_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc099_5d_base_v099_signal

def f112r_f112_retained_earnings_turnover_velocity_calc100_21d_base_v100_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc100_21d_base_v100_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc100_21d_base_v100_signal

def f112r_f112_retained_earnings_turnover_velocity_calc101_10d_base_v101_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc101_10d_base_v101_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc101_10d_base_v101_signal

def f112r_f112_retained_earnings_turnover_velocity_calc102_150d_base_v102_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc102_150d_base_v102_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc102_150d_base_v102_signal

def f112r_f112_retained_earnings_turnover_velocity_calc103_150d_base_v103_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc103_150d_base_v103_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc103_150d_base_v103_signal

def f112r_f112_retained_earnings_turnover_velocity_calc104_42d_base_v104_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(42).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc104_42d_base_v104_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc104_42d_base_v104_signal

def f112r_f112_retained_earnings_turnover_velocity_calc105_200d_base_v105_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(200)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc105_200d_base_v105_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc105_200d_base_v105_signal

def f112r_f112_retained_earnings_turnover_velocity_calc106_84d_base_v106_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc106_84d_base_v106_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc106_84d_base_v106_signal

def f112r_f112_retained_earnings_turnover_velocity_calc107_252d_base_v107_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(252)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc107_252d_base_v107_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc107_252d_base_v107_signal

def f112r_f112_retained_earnings_turnover_velocity_calc108_150d_base_v108_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc108_150d_base_v108_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc108_150d_base_v108_signal

def f112r_f112_retained_earnings_turnover_velocity_calc109_21d_base_v109_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc109_21d_base_v109_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc109_21d_base_v109_signal

def f112r_f112_retained_earnings_turnover_velocity_calc110_200d_base_v110_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(200).mean()) / v_003.rolling(200).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc110_200d_base_v110_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc110_200d_base_v110_signal

def f112r_f112_retained_earnings_turnover_velocity_calc111_84d_base_v111_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(84)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc111_84d_base_v111_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc111_84d_base_v111_signal

def f112r_f112_retained_earnings_turnover_velocity_calc112_84d_base_v112_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(84).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc112_84d_base_v112_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc112_84d_base_v112_signal

def f112r_f112_retained_earnings_turnover_velocity_calc113_63d_base_v113_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(63).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc113_63d_base_v113_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc113_63d_base_v113_signal

def f112r_f112_retained_earnings_turnover_velocity_calc114_63d_base_v114_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc114_63d_base_v114_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc114_63d_base_v114_signal

def f112r_f112_retained_earnings_turnover_velocity_calc115_150d_base_v115_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc115_150d_base_v115_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc115_150d_base_v115_signal

def f112r_f112_retained_earnings_turnover_velocity_calc116_42d_base_v116_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc116_42d_base_v116_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc116_42d_base_v116_signal

def f112r_f112_retained_earnings_turnover_velocity_calc117_10d_base_v117_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc117_10d_base_v117_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc117_10d_base_v117_signal

def f112r_f112_retained_earnings_turnover_velocity_calc118_5d_base_v118_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc118_5d_base_v118_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc118_5d_base_v118_signal

def f112r_f112_retained_earnings_turnover_velocity_calc119_105d_base_v119_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc119_105d_base_v119_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc119_105d_base_v119_signal

def f112r_f112_retained_earnings_turnover_velocity_calc120_126d_base_v120_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc120_126d_base_v120_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc120_126d_base_v120_signal

def f112r_f112_retained_earnings_turnover_velocity_calc121_21d_base_v121_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc121_21d_base_v121_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc121_21d_base_v121_signal

def f112r_f112_retained_earnings_turnover_velocity_calc122_252d_base_v122_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc122_252d_base_v122_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc122_252d_base_v122_signal

def f112r_f112_retained_earnings_turnover_velocity_calc123_105d_base_v123_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc123_105d_base_v123_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc123_105d_base_v123_signal

def f112r_f112_retained_earnings_turnover_velocity_calc124_10d_base_v124_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc124_10d_base_v124_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc124_10d_base_v124_signal

def f112r_f112_retained_earnings_turnover_velocity_calc125_84d_base_v125_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc125_84d_base_v125_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc125_84d_base_v125_signal

def f112r_f112_retained_earnings_turnover_velocity_calc126_252d_base_v126_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc126_252d_base_v126_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc126_252d_base_v126_signal

def f112r_f112_retained_earnings_turnover_velocity_calc127_10d_base_v127_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(10)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc127_10d_base_v127_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc127_10d_base_v127_signal

def f112r_f112_retained_earnings_turnover_velocity_calc128_84d_base_v128_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc128_84d_base_v128_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc128_84d_base_v128_signal

def f112r_f112_retained_earnings_turnover_velocity_calc129_63d_base_v129_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc129_63d_base_v129_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc129_63d_base_v129_signal

def f112r_f112_retained_earnings_turnover_velocity_calc130_105d_base_v130_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc130_105d_base_v130_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc130_105d_base_v130_signal

def f112r_f112_retained_earnings_turnover_velocity_calc131_42d_base_v131_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(42)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc131_42d_base_v131_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc131_42d_base_v131_signal

def f112r_f112_retained_earnings_turnover_velocity_calc132_126d_base_v132_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc132_126d_base_v132_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc132_126d_base_v132_signal

def f112r_f112_retained_earnings_turnover_velocity_calc133_252d_base_v133_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc133_252d_base_v133_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc133_252d_base_v133_signal

def f112r_f112_retained_earnings_turnover_velocity_calc134_150d_base_v134_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc134_150d_base_v134_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc134_150d_base_v134_signal

def f112r_f112_retained_earnings_turnover_velocity_calc135_200d_base_v135_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc135_200d_base_v135_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc135_200d_base_v135_signal

def f112r_f112_retained_earnings_turnover_velocity_calc136_252d_base_v136_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc136_252d_base_v136_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc136_252d_base_v136_signal

def f112r_f112_retained_earnings_turnover_velocity_calc137_21d_base_v137_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc137_21d_base_v137_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc137_21d_base_v137_signal

def f112r_f112_retained_earnings_turnover_velocity_calc138_84d_base_v138_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc138_84d_base_v138_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc138_84d_base_v138_signal

def f112r_f112_retained_earnings_turnover_velocity_calc139_21d_base_v139_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(21)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc139_21d_base_v139_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc139_21d_base_v139_signal

def f112r_f112_retained_earnings_turnover_velocity_calc140_10d_base_v140_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc140_10d_base_v140_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc140_10d_base_v140_signal

def f112r_f112_retained_earnings_turnover_velocity_calc141_63d_base_v141_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(63).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc141_63d_base_v141_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc141_63d_base_v141_signal

def f112r_f112_retained_earnings_turnover_velocity_calc142_126d_base_v142_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc142_126d_base_v142_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc142_126d_base_v142_signal

def f112r_f112_retained_earnings_turnover_velocity_calc143_63d_base_v143_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(63).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc143_63d_base_v143_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc143_63d_base_v143_signal

def f112r_f112_retained_earnings_turnover_velocity_calc144_21d_base_v144_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc144_21d_base_v144_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc144_21d_base_v144_signal

def f112r_f112_retained_earnings_turnover_velocity_calc145_84d_base_v145_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(84).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc145_84d_base_v145_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc145_84d_base_v145_signal

def f112r_f112_retained_earnings_turnover_velocity_calc146_5d_base_v146_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc146_5d_base_v146_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc146_5d_base_v146_signal

def f112r_f112_retained_earnings_turnover_velocity_calc147_10d_base_v147_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(10)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc147_10d_base_v147_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc147_10d_base_v147_signal

def f112r_f112_retained_earnings_turnover_velocity_calc148_84d_base_v148_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(84).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc148_84d_base_v148_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc148_84d_base_v148_signal

def f112r_f112_retained_earnings_turnover_velocity_calc149_126d_base_v149_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(126)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc149_126d_base_v149_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc149_126d_base_v149_signal

def f112r_f112_retained_earnings_turnover_velocity_calc150_126d_base_v150_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc150_126d_base_v150_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc150_126d_base_v150_signal


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
