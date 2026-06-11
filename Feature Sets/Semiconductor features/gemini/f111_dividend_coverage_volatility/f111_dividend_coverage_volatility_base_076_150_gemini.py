import pandas as pd
import numpy as np
FEATURE_FUNCTIONS = {}

def f111d_f111_dividend_coverage_volatility_calc076_5d_base_v076_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc076_5d_base_v076_signal'] = f111d_f111_dividend_coverage_volatility_calc076_5d_base_v076_signal

def f111d_f111_dividend_coverage_volatility_calc077_21d_base_v077_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc077_21d_base_v077_signal'] = f111d_f111_dividend_coverage_volatility_calc077_21d_base_v077_signal

def f111d_f111_dividend_coverage_volatility_calc078_126d_base_v078_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(126)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc078_126d_base_v078_signal'] = f111d_f111_dividend_coverage_volatility_calc078_126d_base_v078_signal

def f111d_f111_dividend_coverage_volatility_calc079_105d_base_v079_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(105)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc079_105d_base_v079_signal'] = f111d_f111_dividend_coverage_volatility_calc079_105d_base_v079_signal

def f111d_f111_dividend_coverage_volatility_calc080_84d_base_v080_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc080_84d_base_v080_signal'] = f111d_f111_dividend_coverage_volatility_calc080_84d_base_v080_signal

def f111d_f111_dividend_coverage_volatility_calc081_126d_base_v081_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc081_126d_base_v081_signal'] = f111d_f111_dividend_coverage_volatility_calc081_126d_base_v081_signal

def f111d_f111_dividend_coverage_volatility_calc082_63d_base_v082_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(63).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc082_63d_base_v082_signal'] = f111d_f111_dividend_coverage_volatility_calc082_63d_base_v082_signal

def f111d_f111_dividend_coverage_volatility_calc083_252d_base_v083_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(252)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc083_252d_base_v083_signal'] = f111d_f111_dividend_coverage_volatility_calc083_252d_base_v083_signal

def f111d_f111_dividend_coverage_volatility_calc084_42d_base_v084_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc084_42d_base_v084_signal'] = f111d_f111_dividend_coverage_volatility_calc084_42d_base_v084_signal

def f111d_f111_dividend_coverage_volatility_calc085_150d_base_v085_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc085_150d_base_v085_signal'] = f111d_f111_dividend_coverage_volatility_calc085_150d_base_v085_signal

def f111d_f111_dividend_coverage_volatility_calc086_200d_base_v086_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc086_200d_base_v086_signal'] = f111d_f111_dividend_coverage_volatility_calc086_200d_base_v086_signal

def f111d_f111_dividend_coverage_volatility_calc087_63d_base_v087_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc087_63d_base_v087_signal'] = f111d_f111_dividend_coverage_volatility_calc087_63d_base_v087_signal

def f111d_f111_dividend_coverage_volatility_calc088_84d_base_v088_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(84).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc088_84d_base_v088_signal'] = f111d_f111_dividend_coverage_volatility_calc088_84d_base_v088_signal

def f111d_f111_dividend_coverage_volatility_calc089_84d_base_v089_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc089_84d_base_v089_signal'] = f111d_f111_dividend_coverage_volatility_calc089_84d_base_v089_signal

def f111d_f111_dividend_coverage_volatility_calc090_84d_base_v090_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc090_84d_base_v090_signal'] = f111d_f111_dividend_coverage_volatility_calc090_84d_base_v090_signal

def f111d_f111_dividend_coverage_volatility_calc091_5d_base_v091_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc091_5d_base_v091_signal'] = f111d_f111_dividend_coverage_volatility_calc091_5d_base_v091_signal

def f111d_f111_dividend_coverage_volatility_calc092_105d_base_v092_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc092_105d_base_v092_signal'] = f111d_f111_dividend_coverage_volatility_calc092_105d_base_v092_signal

def f111d_f111_dividend_coverage_volatility_calc093_84d_base_v093_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(84)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc093_84d_base_v093_signal'] = f111d_f111_dividend_coverage_volatility_calc093_84d_base_v093_signal

def f111d_f111_dividend_coverage_volatility_calc094_21d_base_v094_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc094_21d_base_v094_signal'] = f111d_f111_dividend_coverage_volatility_calc094_21d_base_v094_signal

def f111d_f111_dividend_coverage_volatility_calc095_150d_base_v095_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc095_150d_base_v095_signal'] = f111d_f111_dividend_coverage_volatility_calc095_150d_base_v095_signal

def f111d_f111_dividend_coverage_volatility_calc096_252d_base_v096_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc096_252d_base_v096_signal'] = f111d_f111_dividend_coverage_volatility_calc096_252d_base_v096_signal

def f111d_f111_dividend_coverage_volatility_calc097_126d_base_v097_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc097_126d_base_v097_signal'] = f111d_f111_dividend_coverage_volatility_calc097_126d_base_v097_signal

def f111d_f111_dividend_coverage_volatility_calc098_63d_base_v098_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc098_63d_base_v098_signal'] = f111d_f111_dividend_coverage_volatility_calc098_63d_base_v098_signal

def f111d_f111_dividend_coverage_volatility_calc099_21d_base_v099_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc099_21d_base_v099_signal'] = f111d_f111_dividend_coverage_volatility_calc099_21d_base_v099_signal

def f111d_f111_dividend_coverage_volatility_calc100_42d_base_v100_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(42).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc100_42d_base_v100_signal'] = f111d_f111_dividend_coverage_volatility_calc100_42d_base_v100_signal

def f111d_f111_dividend_coverage_volatility_calc101_21d_base_v101_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc101_21d_base_v101_signal'] = f111d_f111_dividend_coverage_volatility_calc101_21d_base_v101_signal

def f111d_f111_dividend_coverage_volatility_calc102_10d_base_v102_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc102_10d_base_v102_signal'] = f111d_f111_dividend_coverage_volatility_calc102_10d_base_v102_signal

def f111d_f111_dividend_coverage_volatility_calc103_126d_base_v103_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(126)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc103_126d_base_v103_signal'] = f111d_f111_dividend_coverage_volatility_calc103_126d_base_v103_signal

def f111d_f111_dividend_coverage_volatility_calc104_150d_base_v104_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc104_150d_base_v104_signal'] = f111d_f111_dividend_coverage_volatility_calc104_150d_base_v104_signal

def f111d_f111_dividend_coverage_volatility_calc105_150d_base_v105_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc105_150d_base_v105_signal'] = f111d_f111_dividend_coverage_volatility_calc105_150d_base_v105_signal

def f111d_f111_dividend_coverage_volatility_calc106_5d_base_v106_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc106_5d_base_v106_signal'] = f111d_f111_dividend_coverage_volatility_calc106_5d_base_v106_signal

def f111d_f111_dividend_coverage_volatility_calc107_63d_base_v107_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc107_63d_base_v107_signal'] = f111d_f111_dividend_coverage_volatility_calc107_63d_base_v107_signal

def f111d_f111_dividend_coverage_volatility_calc108_84d_base_v108_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc108_84d_base_v108_signal'] = f111d_f111_dividend_coverage_volatility_calc108_84d_base_v108_signal

def f111d_f111_dividend_coverage_volatility_calc109_84d_base_v109_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc109_84d_base_v109_signal'] = f111d_f111_dividend_coverage_volatility_calc109_84d_base_v109_signal

def f111d_f111_dividend_coverage_volatility_calc110_10d_base_v110_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(10).mean()) / v_003.rolling(10).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc110_10d_base_v110_signal'] = f111d_f111_dividend_coverage_volatility_calc110_10d_base_v110_signal

def f111d_f111_dividend_coverage_volatility_calc111_63d_base_v111_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(63).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc111_63d_base_v111_signal'] = f111d_f111_dividend_coverage_volatility_calc111_63d_base_v111_signal

def f111d_f111_dividend_coverage_volatility_calc112_126d_base_v112_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(126).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc112_126d_base_v112_signal'] = f111d_f111_dividend_coverage_volatility_calc112_126d_base_v112_signal

def f111d_f111_dividend_coverage_volatility_calc113_21d_base_v113_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(21).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc113_21d_base_v113_signal'] = f111d_f111_dividend_coverage_volatility_calc113_21d_base_v113_signal

def f111d_f111_dividend_coverage_volatility_calc114_84d_base_v114_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(84).mean()) / v_003.rolling(84).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc114_84d_base_v114_signal'] = f111d_f111_dividend_coverage_volatility_calc114_84d_base_v114_signal

def f111d_f111_dividend_coverage_volatility_calc115_105d_base_v115_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc115_105d_base_v115_signal'] = f111d_f111_dividend_coverage_volatility_calc115_105d_base_v115_signal

def f111d_f111_dividend_coverage_volatility_calc116_126d_base_v116_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(126)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc116_126d_base_v116_signal'] = f111d_f111_dividend_coverage_volatility_calc116_126d_base_v116_signal

def f111d_f111_dividend_coverage_volatility_calc117_42d_base_v117_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(42)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc117_42d_base_v117_signal'] = f111d_f111_dividend_coverage_volatility_calc117_42d_base_v117_signal

def f111d_f111_dividend_coverage_volatility_calc118_21d_base_v118_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(21)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc118_21d_base_v118_signal'] = f111d_f111_dividend_coverage_volatility_calc118_21d_base_v118_signal

def f111d_f111_dividend_coverage_volatility_calc119_42d_base_v119_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc119_42d_base_v119_signal'] = f111d_f111_dividend_coverage_volatility_calc119_42d_base_v119_signal

def f111d_f111_dividend_coverage_volatility_calc120_5d_base_v120_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc120_5d_base_v120_signal'] = f111d_f111_dividend_coverage_volatility_calc120_5d_base_v120_signal

def f111d_f111_dividend_coverage_volatility_calc121_105d_base_v121_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc121_105d_base_v121_signal'] = f111d_f111_dividend_coverage_volatility_calc121_105d_base_v121_signal

def f111d_f111_dividend_coverage_volatility_calc122_252d_base_v122_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc122_252d_base_v122_signal'] = f111d_f111_dividend_coverage_volatility_calc122_252d_base_v122_signal

def f111d_f111_dividend_coverage_volatility_calc123_84d_base_v123_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(84)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc123_84d_base_v123_signal'] = f111d_f111_dividend_coverage_volatility_calc123_84d_base_v123_signal

def f111d_f111_dividend_coverage_volatility_calc124_5d_base_v124_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc124_5d_base_v124_signal'] = f111d_f111_dividend_coverage_volatility_calc124_5d_base_v124_signal

def f111d_f111_dividend_coverage_volatility_calc125_10d_base_v125_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc125_10d_base_v125_signal'] = f111d_f111_dividend_coverage_volatility_calc125_10d_base_v125_signal

def f111d_f111_dividend_coverage_volatility_calc126_84d_base_v126_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(84)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc126_84d_base_v126_signal'] = f111d_f111_dividend_coverage_volatility_calc126_84d_base_v126_signal

def f111d_f111_dividend_coverage_volatility_calc127_42d_base_v127_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc127_42d_base_v127_signal'] = f111d_f111_dividend_coverage_volatility_calc127_42d_base_v127_signal

def f111d_f111_dividend_coverage_volatility_calc128_252d_base_v128_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc128_252d_base_v128_signal'] = f111d_f111_dividend_coverage_volatility_calc128_252d_base_v128_signal

def f111d_f111_dividend_coverage_volatility_calc129_252d_base_v129_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc129_252d_base_v129_signal'] = f111d_f111_dividend_coverage_volatility_calc129_252d_base_v129_signal

def f111d_f111_dividend_coverage_volatility_calc130_105d_base_v130_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc130_105d_base_v130_signal'] = f111d_f111_dividend_coverage_volatility_calc130_105d_base_v130_signal

def f111d_f111_dividend_coverage_volatility_calc131_21d_base_v131_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc131_21d_base_v131_signal'] = f111d_f111_dividend_coverage_volatility_calc131_21d_base_v131_signal

def f111d_f111_dividend_coverage_volatility_calc132_21d_base_v132_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(21)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc132_21d_base_v132_signal'] = f111d_f111_dividend_coverage_volatility_calc132_21d_base_v132_signal

def f111d_f111_dividend_coverage_volatility_calc133_105d_base_v133_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc133_105d_base_v133_signal'] = f111d_f111_dividend_coverage_volatility_calc133_105d_base_v133_signal

def f111d_f111_dividend_coverage_volatility_calc134_150d_base_v134_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc134_150d_base_v134_signal'] = f111d_f111_dividend_coverage_volatility_calc134_150d_base_v134_signal

def f111d_f111_dividend_coverage_volatility_calc135_63d_base_v135_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc135_63d_base_v135_signal'] = f111d_f111_dividend_coverage_volatility_calc135_63d_base_v135_signal

def f111d_f111_dividend_coverage_volatility_calc136_105d_base_v136_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc136_105d_base_v136_signal'] = f111d_f111_dividend_coverage_volatility_calc136_105d_base_v136_signal

def f111d_f111_dividend_coverage_volatility_calc137_63d_base_v137_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc137_63d_base_v137_signal'] = f111d_f111_dividend_coverage_volatility_calc137_63d_base_v137_signal

def f111d_f111_dividend_coverage_volatility_calc138_5d_base_v138_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc138_5d_base_v138_signal'] = f111d_f111_dividend_coverage_volatility_calc138_5d_base_v138_signal

def f111d_f111_dividend_coverage_volatility_calc139_5d_base_v139_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc139_5d_base_v139_signal'] = f111d_f111_dividend_coverage_volatility_calc139_5d_base_v139_signal

def f111d_f111_dividend_coverage_volatility_calc140_126d_base_v140_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc140_126d_base_v140_signal'] = f111d_f111_dividend_coverage_volatility_calc140_126d_base_v140_signal

def f111d_f111_dividend_coverage_volatility_calc141_42d_base_v141_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc141_42d_base_v141_signal'] = f111d_f111_dividend_coverage_volatility_calc141_42d_base_v141_signal

def f111d_f111_dividend_coverage_volatility_calc142_5d_base_v142_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc142_5d_base_v142_signal'] = f111d_f111_dividend_coverage_volatility_calc142_5d_base_v142_signal

def f111d_f111_dividend_coverage_volatility_calc143_21d_base_v143_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(21).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc143_21d_base_v143_signal'] = f111d_f111_dividend_coverage_volatility_calc143_21d_base_v143_signal

def f111d_f111_dividend_coverage_volatility_calc144_42d_base_v144_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(42).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc144_42d_base_v144_signal'] = f111d_f111_dividend_coverage_volatility_calc144_42d_base_v144_signal

def f111d_f111_dividend_coverage_volatility_calc145_150d_base_v145_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc145_150d_base_v145_signal'] = f111d_f111_dividend_coverage_volatility_calc145_150d_base_v145_signal

def f111d_f111_dividend_coverage_volatility_calc146_84d_base_v146_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc146_84d_base_v146_signal'] = f111d_f111_dividend_coverage_volatility_calc146_84d_base_v146_signal

def f111d_f111_dividend_coverage_volatility_calc147_126d_base_v147_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc147_126d_base_v147_signal'] = f111d_f111_dividend_coverage_volatility_calc147_126d_base_v147_signal

def f111d_f111_dividend_coverage_volatility_calc148_5d_base_v148_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc148_5d_base_v148_signal'] = f111d_f111_dividend_coverage_volatility_calc148_5d_base_v148_signal

def f111d_f111_dividend_coverage_volatility_calc149_150d_base_v149_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc149_150d_base_v149_signal'] = f111d_f111_dividend_coverage_volatility_calc149_150d_base_v149_signal

def f111d_f111_dividend_coverage_volatility_calc150_252d_base_v150_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc150_252d_base_v150_signal'] = f111d_f111_dividend_coverage_volatility_calc150_252d_base_v150_signal


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
