import pandas as pd
import numpy as np
FEATURE_FUNCTIONS = {}

def f110w_f110_working_capital_to_revenue_regime_calc076_21d_base_v076_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc076_21d_base_v076_signal'] = f110w_f110_working_capital_to_revenue_regime_calc076_21d_base_v076_signal

def f110w_f110_working_capital_to_revenue_regime_calc077_42d_base_v077_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(42).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc077_42d_base_v077_signal'] = f110w_f110_working_capital_to_revenue_regime_calc077_42d_base_v077_signal

def f110w_f110_working_capital_to_revenue_regime_calc078_10d_base_v078_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc078_10d_base_v078_signal'] = f110w_f110_working_capital_to_revenue_regime_calc078_10d_base_v078_signal

def f110w_f110_working_capital_to_revenue_regime_calc079_200d_base_v079_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc079_200d_base_v079_signal'] = f110w_f110_working_capital_to_revenue_regime_calc079_200d_base_v079_signal

def f110w_f110_working_capital_to_revenue_regime_calc080_105d_base_v080_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc080_105d_base_v080_signal'] = f110w_f110_working_capital_to_revenue_regime_calc080_105d_base_v080_signal

def f110w_f110_working_capital_to_revenue_regime_calc081_105d_base_v081_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(105)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc081_105d_base_v081_signal'] = f110w_f110_working_capital_to_revenue_regime_calc081_105d_base_v081_signal

def f110w_f110_working_capital_to_revenue_regime_calc082_42d_base_v082_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc082_42d_base_v082_signal'] = f110w_f110_working_capital_to_revenue_regime_calc082_42d_base_v082_signal

def f110w_f110_working_capital_to_revenue_regime_calc083_200d_base_v083_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc083_200d_base_v083_signal'] = f110w_f110_working_capital_to_revenue_regime_calc083_200d_base_v083_signal

def f110w_f110_working_capital_to_revenue_regime_calc084_84d_base_v084_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(84)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc084_84d_base_v084_signal'] = f110w_f110_working_capital_to_revenue_regime_calc084_84d_base_v084_signal

def f110w_f110_working_capital_to_revenue_regime_calc085_63d_base_v085_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(63).mean()) / v_003.rolling(63).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc085_63d_base_v085_signal'] = f110w_f110_working_capital_to_revenue_regime_calc085_63d_base_v085_signal

def f110w_f110_working_capital_to_revenue_regime_calc086_84d_base_v086_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc086_84d_base_v086_signal'] = f110w_f110_working_capital_to_revenue_regime_calc086_84d_base_v086_signal

def f110w_f110_working_capital_to_revenue_regime_calc087_63d_base_v087_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(63)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc087_63d_base_v087_signal'] = f110w_f110_working_capital_to_revenue_regime_calc087_63d_base_v087_signal

def f110w_f110_working_capital_to_revenue_regime_calc088_252d_base_v088_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc088_252d_base_v088_signal'] = f110w_f110_working_capital_to_revenue_regime_calc088_252d_base_v088_signal

def f110w_f110_working_capital_to_revenue_regime_calc089_252d_base_v089_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc089_252d_base_v089_signal'] = f110w_f110_working_capital_to_revenue_regime_calc089_252d_base_v089_signal

def f110w_f110_working_capital_to_revenue_regime_calc090_126d_base_v090_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(126).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc090_126d_base_v090_signal'] = f110w_f110_working_capital_to_revenue_regime_calc090_126d_base_v090_signal

def f110w_f110_working_capital_to_revenue_regime_calc091_84d_base_v091_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc091_84d_base_v091_signal'] = f110w_f110_working_capital_to_revenue_regime_calc091_84d_base_v091_signal

def f110w_f110_working_capital_to_revenue_regime_calc092_5d_base_v092_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc092_5d_base_v092_signal'] = f110w_f110_working_capital_to_revenue_regime_calc092_5d_base_v092_signal

def f110w_f110_working_capital_to_revenue_regime_calc093_126d_base_v093_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(126).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc093_126d_base_v093_signal'] = f110w_f110_working_capital_to_revenue_regime_calc093_126d_base_v093_signal

def f110w_f110_working_capital_to_revenue_regime_calc094_150d_base_v094_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(150).mean()) / v_003.rolling(150).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc094_150d_base_v094_signal'] = f110w_f110_working_capital_to_revenue_regime_calc094_150d_base_v094_signal

def f110w_f110_working_capital_to_revenue_regime_calc095_63d_base_v095_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc095_63d_base_v095_signal'] = f110w_f110_working_capital_to_revenue_regime_calc095_63d_base_v095_signal

def f110w_f110_working_capital_to_revenue_regime_calc096_252d_base_v096_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(252).mean()) / v_003.rolling(252).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc096_252d_base_v096_signal'] = f110w_f110_working_capital_to_revenue_regime_calc096_252d_base_v096_signal

def f110w_f110_working_capital_to_revenue_regime_calc097_84d_base_v097_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc097_84d_base_v097_signal'] = f110w_f110_working_capital_to_revenue_regime_calc097_84d_base_v097_signal

def f110w_f110_working_capital_to_revenue_regime_calc098_21d_base_v098_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc098_21d_base_v098_signal'] = f110w_f110_working_capital_to_revenue_regime_calc098_21d_base_v098_signal

def f110w_f110_working_capital_to_revenue_regime_calc099_84d_base_v099_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc099_84d_base_v099_signal'] = f110w_f110_working_capital_to_revenue_regime_calc099_84d_base_v099_signal

def f110w_f110_working_capital_to_revenue_regime_calc100_63d_base_v100_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc100_63d_base_v100_signal'] = f110w_f110_working_capital_to_revenue_regime_calc100_63d_base_v100_signal

def f110w_f110_working_capital_to_revenue_regime_calc101_10d_base_v101_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc101_10d_base_v101_signal'] = f110w_f110_working_capital_to_revenue_regime_calc101_10d_base_v101_signal

def f110w_f110_working_capital_to_revenue_regime_calc102_105d_base_v102_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc102_105d_base_v102_signal'] = f110w_f110_working_capital_to_revenue_regime_calc102_105d_base_v102_signal

def f110w_f110_working_capital_to_revenue_regime_calc103_200d_base_v103_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(200)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc103_200d_base_v103_signal'] = f110w_f110_working_capital_to_revenue_regime_calc103_200d_base_v103_signal

def f110w_f110_working_capital_to_revenue_regime_calc104_105d_base_v104_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc104_105d_base_v104_signal'] = f110w_f110_working_capital_to_revenue_regime_calc104_105d_base_v104_signal

def f110w_f110_working_capital_to_revenue_regime_calc105_21d_base_v105_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc105_21d_base_v105_signal'] = f110w_f110_working_capital_to_revenue_regime_calc105_21d_base_v105_signal

def f110w_f110_working_capital_to_revenue_regime_calc106_84d_base_v106_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(84).mean()) / v_003.rolling(84).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc106_84d_base_v106_signal'] = f110w_f110_working_capital_to_revenue_regime_calc106_84d_base_v106_signal

def f110w_f110_working_capital_to_revenue_regime_calc107_10d_base_v107_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(10).mean()) / v_003.rolling(10).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc107_10d_base_v107_signal'] = f110w_f110_working_capital_to_revenue_regime_calc107_10d_base_v107_signal

def f110w_f110_working_capital_to_revenue_regime_calc108_252d_base_v108_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(252)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc108_252d_base_v108_signal'] = f110w_f110_working_capital_to_revenue_regime_calc108_252d_base_v108_signal

def f110w_f110_working_capital_to_revenue_regime_calc109_5d_base_v109_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc109_5d_base_v109_signal'] = f110w_f110_working_capital_to_revenue_regime_calc109_5d_base_v109_signal

def f110w_f110_working_capital_to_revenue_regime_calc110_63d_base_v110_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc110_63d_base_v110_signal'] = f110w_f110_working_capital_to_revenue_regime_calc110_63d_base_v110_signal

def f110w_f110_working_capital_to_revenue_regime_calc111_126d_base_v111_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc111_126d_base_v111_signal'] = f110w_f110_working_capital_to_revenue_regime_calc111_126d_base_v111_signal

def f110w_f110_working_capital_to_revenue_regime_calc112_252d_base_v112_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc112_252d_base_v112_signal'] = f110w_f110_working_capital_to_revenue_regime_calc112_252d_base_v112_signal

def f110w_f110_working_capital_to_revenue_regime_calc113_105d_base_v113_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc113_105d_base_v113_signal'] = f110w_f110_working_capital_to_revenue_regime_calc113_105d_base_v113_signal

def f110w_f110_working_capital_to_revenue_regime_calc114_42d_base_v114_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(42)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc114_42d_base_v114_signal'] = f110w_f110_working_capital_to_revenue_regime_calc114_42d_base_v114_signal

def f110w_f110_working_capital_to_revenue_regime_calc115_150d_base_v115_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc115_150d_base_v115_signal'] = f110w_f110_working_capital_to_revenue_regime_calc115_150d_base_v115_signal

def f110w_f110_working_capital_to_revenue_regime_calc116_84d_base_v116_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc116_84d_base_v116_signal'] = f110w_f110_working_capital_to_revenue_regime_calc116_84d_base_v116_signal

def f110w_f110_working_capital_to_revenue_regime_calc117_105d_base_v117_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc117_105d_base_v117_signal'] = f110w_f110_working_capital_to_revenue_regime_calc117_105d_base_v117_signal

def f110w_f110_working_capital_to_revenue_regime_calc118_10d_base_v118_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(10).mean()) / v_003.rolling(10).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc118_10d_base_v118_signal'] = f110w_f110_working_capital_to_revenue_regime_calc118_10d_base_v118_signal

def f110w_f110_working_capital_to_revenue_regime_calc119_10d_base_v119_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(10).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc119_10d_base_v119_signal'] = f110w_f110_working_capital_to_revenue_regime_calc119_10d_base_v119_signal

def f110w_f110_working_capital_to_revenue_regime_calc120_10d_base_v120_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(10).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc120_10d_base_v120_signal'] = f110w_f110_working_capital_to_revenue_regime_calc120_10d_base_v120_signal

def f110w_f110_working_capital_to_revenue_regime_calc121_42d_base_v121_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc121_42d_base_v121_signal'] = f110w_f110_working_capital_to_revenue_regime_calc121_42d_base_v121_signal

def f110w_f110_working_capital_to_revenue_regime_calc122_5d_base_v122_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc122_5d_base_v122_signal'] = f110w_f110_working_capital_to_revenue_regime_calc122_5d_base_v122_signal

def f110w_f110_working_capital_to_revenue_regime_calc123_63d_base_v123_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(63).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc123_63d_base_v123_signal'] = f110w_f110_working_capital_to_revenue_regime_calc123_63d_base_v123_signal

def f110w_f110_working_capital_to_revenue_regime_calc124_5d_base_v124_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc124_5d_base_v124_signal'] = f110w_f110_working_capital_to_revenue_regime_calc124_5d_base_v124_signal

def f110w_f110_working_capital_to_revenue_regime_calc125_252d_base_v125_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc125_252d_base_v125_signal'] = f110w_f110_working_capital_to_revenue_regime_calc125_252d_base_v125_signal

def f110w_f110_working_capital_to_revenue_regime_calc126_84d_base_v126_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc126_84d_base_v126_signal'] = f110w_f110_working_capital_to_revenue_regime_calc126_84d_base_v126_signal

def f110w_f110_working_capital_to_revenue_regime_calc127_252d_base_v127_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc127_252d_base_v127_signal'] = f110w_f110_working_capital_to_revenue_regime_calc127_252d_base_v127_signal

def f110w_f110_working_capital_to_revenue_regime_calc128_105d_base_v128_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(105).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc128_105d_base_v128_signal'] = f110w_f110_working_capital_to_revenue_regime_calc128_105d_base_v128_signal

def f110w_f110_working_capital_to_revenue_regime_calc129_5d_base_v129_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc129_5d_base_v129_signal'] = f110w_f110_working_capital_to_revenue_regime_calc129_5d_base_v129_signal

def f110w_f110_working_capital_to_revenue_regime_calc130_5d_base_v130_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc130_5d_base_v130_signal'] = f110w_f110_working_capital_to_revenue_regime_calc130_5d_base_v130_signal

def f110w_f110_working_capital_to_revenue_regime_calc131_10d_base_v131_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(10)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc131_10d_base_v131_signal'] = f110w_f110_working_capital_to_revenue_regime_calc131_10d_base_v131_signal

def f110w_f110_working_capital_to_revenue_regime_calc132_10d_base_v132_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc132_10d_base_v132_signal'] = f110w_f110_working_capital_to_revenue_regime_calc132_10d_base_v132_signal

def f110w_f110_working_capital_to_revenue_regime_calc133_252d_base_v133_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc133_252d_base_v133_signal'] = f110w_f110_working_capital_to_revenue_regime_calc133_252d_base_v133_signal

def f110w_f110_working_capital_to_revenue_regime_calc134_5d_base_v134_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc134_5d_base_v134_signal'] = f110w_f110_working_capital_to_revenue_regime_calc134_5d_base_v134_signal

def f110w_f110_working_capital_to_revenue_regime_calc135_42d_base_v135_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc135_42d_base_v135_signal'] = f110w_f110_working_capital_to_revenue_regime_calc135_42d_base_v135_signal

def f110w_f110_working_capital_to_revenue_regime_calc136_63d_base_v136_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(63).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc136_63d_base_v136_signal'] = f110w_f110_working_capital_to_revenue_regime_calc136_63d_base_v136_signal

def f110w_f110_working_capital_to_revenue_regime_calc137_84d_base_v137_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc137_84d_base_v137_signal'] = f110w_f110_working_capital_to_revenue_regime_calc137_84d_base_v137_signal

def f110w_f110_working_capital_to_revenue_regime_calc138_200d_base_v138_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc138_200d_base_v138_signal'] = f110w_f110_working_capital_to_revenue_regime_calc138_200d_base_v138_signal

def f110w_f110_working_capital_to_revenue_regime_calc139_200d_base_v139_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc139_200d_base_v139_signal'] = f110w_f110_working_capital_to_revenue_regime_calc139_200d_base_v139_signal

def f110w_f110_working_capital_to_revenue_regime_calc140_5d_base_v140_signal(marketcap, workingcapital):
    v_001 = marketcap
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc140_5d_base_v140_signal'] = f110w_f110_working_capital_to_revenue_regime_calc140_5d_base_v140_signal

def f110w_f110_working_capital_to_revenue_regime_calc141_200d_base_v141_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc141_200d_base_v141_signal'] = f110w_f110_working_capital_to_revenue_regime_calc141_200d_base_v141_signal

def f110w_f110_working_capital_to_revenue_regime_calc142_10d_base_v142_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc142_10d_base_v142_signal'] = f110w_f110_working_capital_to_revenue_regime_calc142_10d_base_v142_signal

def f110w_f110_working_capital_to_revenue_regime_calc143_126d_base_v143_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc143_126d_base_v143_signal'] = f110w_f110_working_capital_to_revenue_regime_calc143_126d_base_v143_signal

def f110w_f110_working_capital_to_revenue_regime_calc144_5d_base_v144_signal(assets, workingcapital):
    v_001 = assets
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc144_5d_base_v144_signal'] = f110w_f110_working_capital_to_revenue_regime_calc144_5d_base_v144_signal

def f110w_f110_working_capital_to_revenue_regime_calc145_150d_base_v145_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc145_150d_base_v145_signal'] = f110w_f110_working_capital_to_revenue_regime_calc145_150d_base_v145_signal

def f110w_f110_working_capital_to_revenue_regime_calc146_10d_base_v146_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc146_10d_base_v146_signal'] = f110w_f110_working_capital_to_revenue_regime_calc146_10d_base_v146_signal

def f110w_f110_working_capital_to_revenue_regime_calc147_5d_base_v147_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc147_5d_base_v147_signal'] = f110w_f110_working_capital_to_revenue_regime_calc147_5d_base_v147_signal

def f110w_f110_working_capital_to_revenue_regime_calc148_126d_base_v148_signal(ebitda, workingcapital):
    v_001 = ebitda
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(126).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc148_126d_base_v148_signal'] = f110w_f110_working_capital_to_revenue_regime_calc148_126d_base_v148_signal

def f110w_f110_working_capital_to_revenue_regime_calc149_42d_base_v149_signal(revenue, workingcapital):
    v_001 = revenue
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc149_42d_base_v149_signal'] = f110w_f110_working_capital_to_revenue_regime_calc149_42d_base_v149_signal

def f110w_f110_working_capital_to_revenue_regime_calc150_10d_base_v150_signal(equity, workingcapital):
    v_001 = equity
    v_002 = workingcapital
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(10).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f110w_f110_working_capital_to_revenue_regime_calc150_10d_base_v150_signal'] = f110w_f110_working_capital_to_revenue_regime_calc150_10d_base_v150_signal


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
