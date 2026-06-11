import pandas as pd
import numpy as np
FEATURE_FUNCTIONS = {}

def f111d_f111_dividend_coverage_volatility_calc001_252d_base_v001_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc001_252d_base_v001_signal'] = f111d_f111_dividend_coverage_volatility_calc001_252d_base_v001_signal

def f111d_f111_dividend_coverage_volatility_calc002_5d_base_v002_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc002_5d_base_v002_signal'] = f111d_f111_dividend_coverage_volatility_calc002_5d_base_v002_signal

def f111d_f111_dividend_coverage_volatility_calc003_5d_base_v003_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(5).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc003_5d_base_v003_signal'] = f111d_f111_dividend_coverage_volatility_calc003_5d_base_v003_signal

def f111d_f111_dividend_coverage_volatility_calc004_126d_base_v004_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc004_126d_base_v004_signal'] = f111d_f111_dividend_coverage_volatility_calc004_126d_base_v004_signal

def f111d_f111_dividend_coverage_volatility_calc005_5d_base_v005_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc005_5d_base_v005_signal'] = f111d_f111_dividend_coverage_volatility_calc005_5d_base_v005_signal

def f111d_f111_dividend_coverage_volatility_calc006_252d_base_v006_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc006_252d_base_v006_signal'] = f111d_f111_dividend_coverage_volatility_calc006_252d_base_v006_signal

def f111d_f111_dividend_coverage_volatility_calc007_200d_base_v007_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc007_200d_base_v007_signal'] = f111d_f111_dividend_coverage_volatility_calc007_200d_base_v007_signal

def f111d_f111_dividend_coverage_volatility_calc008_126d_base_v008_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(126).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc008_126d_base_v008_signal'] = f111d_f111_dividend_coverage_volatility_calc008_126d_base_v008_signal

def f111d_f111_dividend_coverage_volatility_calc009_21d_base_v009_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc009_21d_base_v009_signal'] = f111d_f111_dividend_coverage_volatility_calc009_21d_base_v009_signal

def f111d_f111_dividend_coverage_volatility_calc010_10d_base_v010_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc010_10d_base_v010_signal'] = f111d_f111_dividend_coverage_volatility_calc010_10d_base_v010_signal

def f111d_f111_dividend_coverage_volatility_calc011_21d_base_v011_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc011_21d_base_v011_signal'] = f111d_f111_dividend_coverage_volatility_calc011_21d_base_v011_signal

def f111d_f111_dividend_coverage_volatility_calc012_84d_base_v012_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc012_84d_base_v012_signal'] = f111d_f111_dividend_coverage_volatility_calc012_84d_base_v012_signal

def f111d_f111_dividend_coverage_volatility_calc013_42d_base_v013_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(42).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc013_42d_base_v013_signal'] = f111d_f111_dividend_coverage_volatility_calc013_42d_base_v013_signal

def f111d_f111_dividend_coverage_volatility_calc014_5d_base_v014_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc014_5d_base_v014_signal'] = f111d_f111_dividend_coverage_volatility_calc014_5d_base_v014_signal

def f111d_f111_dividend_coverage_volatility_calc015_42d_base_v015_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc015_42d_base_v015_signal'] = f111d_f111_dividend_coverage_volatility_calc015_42d_base_v015_signal

def f111d_f111_dividend_coverage_volatility_calc016_10d_base_v016_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc016_10d_base_v016_signal'] = f111d_f111_dividend_coverage_volatility_calc016_10d_base_v016_signal

def f111d_f111_dividend_coverage_volatility_calc017_252d_base_v017_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc017_252d_base_v017_signal'] = f111d_f111_dividend_coverage_volatility_calc017_252d_base_v017_signal

def f111d_f111_dividend_coverage_volatility_calc018_21d_base_v018_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc018_21d_base_v018_signal'] = f111d_f111_dividend_coverage_volatility_calc018_21d_base_v018_signal

def f111d_f111_dividend_coverage_volatility_calc019_42d_base_v019_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc019_42d_base_v019_signal'] = f111d_f111_dividend_coverage_volatility_calc019_42d_base_v019_signal

def f111d_f111_dividend_coverage_volatility_calc020_126d_base_v020_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc020_126d_base_v020_signal'] = f111d_f111_dividend_coverage_volatility_calc020_126d_base_v020_signal

def f111d_f111_dividend_coverage_volatility_calc021_252d_base_v021_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc021_252d_base_v021_signal'] = f111d_f111_dividend_coverage_volatility_calc021_252d_base_v021_signal

def f111d_f111_dividend_coverage_volatility_calc022_84d_base_v022_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(84).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc022_84d_base_v022_signal'] = f111d_f111_dividend_coverage_volatility_calc022_84d_base_v022_signal

def f111d_f111_dividend_coverage_volatility_calc023_200d_base_v023_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(200).mean()) / v_003.rolling(200).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc023_200d_base_v023_signal'] = f111d_f111_dividend_coverage_volatility_calc023_200d_base_v023_signal

def f111d_f111_dividend_coverage_volatility_calc024_105d_base_v024_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc024_105d_base_v024_signal'] = f111d_f111_dividend_coverage_volatility_calc024_105d_base_v024_signal

def f111d_f111_dividend_coverage_volatility_calc025_126d_base_v025_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc025_126d_base_v025_signal'] = f111d_f111_dividend_coverage_volatility_calc025_126d_base_v025_signal

def f111d_f111_dividend_coverage_volatility_calc026_42d_base_v026_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc026_42d_base_v026_signal'] = f111d_f111_dividend_coverage_volatility_calc026_42d_base_v026_signal

def f111d_f111_dividend_coverage_volatility_calc027_150d_base_v027_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc027_150d_base_v027_signal'] = f111d_f111_dividend_coverage_volatility_calc027_150d_base_v027_signal

def f111d_f111_dividend_coverage_volatility_calc028_126d_base_v028_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(126)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc028_126d_base_v028_signal'] = f111d_f111_dividend_coverage_volatility_calc028_126d_base_v028_signal

def f111d_f111_dividend_coverage_volatility_calc029_126d_base_v029_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(126)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc029_126d_base_v029_signal'] = f111d_f111_dividend_coverage_volatility_calc029_126d_base_v029_signal

def f111d_f111_dividend_coverage_volatility_calc030_252d_base_v030_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc030_252d_base_v030_signal'] = f111d_f111_dividend_coverage_volatility_calc030_252d_base_v030_signal

def f111d_f111_dividend_coverage_volatility_calc031_21d_base_v031_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(21).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc031_21d_base_v031_signal'] = f111d_f111_dividend_coverage_volatility_calc031_21d_base_v031_signal

def f111d_f111_dividend_coverage_volatility_calc032_105d_base_v032_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc032_105d_base_v032_signal'] = f111d_f111_dividend_coverage_volatility_calc032_105d_base_v032_signal

def f111d_f111_dividend_coverage_volatility_calc033_126d_base_v033_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(126).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc033_126d_base_v033_signal'] = f111d_f111_dividend_coverage_volatility_calc033_126d_base_v033_signal

def f111d_f111_dividend_coverage_volatility_calc034_10d_base_v034_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc034_10d_base_v034_signal'] = f111d_f111_dividend_coverage_volatility_calc034_10d_base_v034_signal

def f111d_f111_dividend_coverage_volatility_calc035_42d_base_v035_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc035_42d_base_v035_signal'] = f111d_f111_dividend_coverage_volatility_calc035_42d_base_v035_signal

def f111d_f111_dividend_coverage_volatility_calc036_10d_base_v036_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(10).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc036_10d_base_v036_signal'] = f111d_f111_dividend_coverage_volatility_calc036_10d_base_v036_signal

def f111d_f111_dividend_coverage_volatility_calc037_105d_base_v037_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc037_105d_base_v037_signal'] = f111d_f111_dividend_coverage_volatility_calc037_105d_base_v037_signal

def f111d_f111_dividend_coverage_volatility_calc038_10d_base_v038_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc038_10d_base_v038_signal'] = f111d_f111_dividend_coverage_volatility_calc038_10d_base_v038_signal

def f111d_f111_dividend_coverage_volatility_calc039_252d_base_v039_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc039_252d_base_v039_signal'] = f111d_f111_dividend_coverage_volatility_calc039_252d_base_v039_signal

def f111d_f111_dividend_coverage_volatility_calc040_42d_base_v040_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc040_42d_base_v040_signal'] = f111d_f111_dividend_coverage_volatility_calc040_42d_base_v040_signal

def f111d_f111_dividend_coverage_volatility_calc041_105d_base_v041_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc041_105d_base_v041_signal'] = f111d_f111_dividend_coverage_volatility_calc041_105d_base_v041_signal

def f111d_f111_dividend_coverage_volatility_calc042_21d_base_v042_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc042_21d_base_v042_signal'] = f111d_f111_dividend_coverage_volatility_calc042_21d_base_v042_signal

def f111d_f111_dividend_coverage_volatility_calc043_42d_base_v043_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(42).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc043_42d_base_v043_signal'] = f111d_f111_dividend_coverage_volatility_calc043_42d_base_v043_signal

def f111d_f111_dividend_coverage_volatility_calc044_63d_base_v044_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc044_63d_base_v044_signal'] = f111d_f111_dividend_coverage_volatility_calc044_63d_base_v044_signal

def f111d_f111_dividend_coverage_volatility_calc045_42d_base_v045_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(42).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc045_42d_base_v045_signal'] = f111d_f111_dividend_coverage_volatility_calc045_42d_base_v045_signal

def f111d_f111_dividend_coverage_volatility_calc046_150d_base_v046_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc046_150d_base_v046_signal'] = f111d_f111_dividend_coverage_volatility_calc046_150d_base_v046_signal

def f111d_f111_dividend_coverage_volatility_calc047_42d_base_v047_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(42)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc047_42d_base_v047_signal'] = f111d_f111_dividend_coverage_volatility_calc047_42d_base_v047_signal

def f111d_f111_dividend_coverage_volatility_calc048_42d_base_v048_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc048_42d_base_v048_signal'] = f111d_f111_dividend_coverage_volatility_calc048_42d_base_v048_signal

def f111d_f111_dividend_coverage_volatility_calc049_42d_base_v049_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc049_42d_base_v049_signal'] = f111d_f111_dividend_coverage_volatility_calc049_42d_base_v049_signal

def f111d_f111_dividend_coverage_volatility_calc050_200d_base_v050_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc050_200d_base_v050_signal'] = f111d_f111_dividend_coverage_volatility_calc050_200d_base_v050_signal

def f111d_f111_dividend_coverage_volatility_calc051_84d_base_v051_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc051_84d_base_v051_signal'] = f111d_f111_dividend_coverage_volatility_calc051_84d_base_v051_signal

def f111d_f111_dividend_coverage_volatility_calc052_10d_base_v052_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(10).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc052_10d_base_v052_signal'] = f111d_f111_dividend_coverage_volatility_calc052_10d_base_v052_signal

def f111d_f111_dividend_coverage_volatility_calc053_84d_base_v053_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc053_84d_base_v053_signal'] = f111d_f111_dividend_coverage_volatility_calc053_84d_base_v053_signal

def f111d_f111_dividend_coverage_volatility_calc054_10d_base_v054_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(10).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc054_10d_base_v054_signal'] = f111d_f111_dividend_coverage_volatility_calc054_10d_base_v054_signal

def f111d_f111_dividend_coverage_volatility_calc055_200d_base_v055_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc055_200d_base_v055_signal'] = f111d_f111_dividend_coverage_volatility_calc055_200d_base_v055_signal

def f111d_f111_dividend_coverage_volatility_calc056_200d_base_v056_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc056_200d_base_v056_signal'] = f111d_f111_dividend_coverage_volatility_calc056_200d_base_v056_signal

def f111d_f111_dividend_coverage_volatility_calc057_252d_base_v057_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(252)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc057_252d_base_v057_signal'] = f111d_f111_dividend_coverage_volatility_calc057_252d_base_v057_signal

def f111d_f111_dividend_coverage_volatility_calc058_21d_base_v058_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc058_21d_base_v058_signal'] = f111d_f111_dividend_coverage_volatility_calc058_21d_base_v058_signal

def f111d_f111_dividend_coverage_volatility_calc059_200d_base_v059_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc059_200d_base_v059_signal'] = f111d_f111_dividend_coverage_volatility_calc059_200d_base_v059_signal

def f111d_f111_dividend_coverage_volatility_calc060_150d_base_v060_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(150)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc060_150d_base_v060_signal'] = f111d_f111_dividend_coverage_volatility_calc060_150d_base_v060_signal

def f111d_f111_dividend_coverage_volatility_calc061_21d_base_v061_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc061_21d_base_v061_signal'] = f111d_f111_dividend_coverage_volatility_calc061_21d_base_v061_signal

def f111d_f111_dividend_coverage_volatility_calc062_105d_base_v062_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc062_105d_base_v062_signal'] = f111d_f111_dividend_coverage_volatility_calc062_105d_base_v062_signal

def f111d_f111_dividend_coverage_volatility_calc063_200d_base_v063_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc063_200d_base_v063_signal'] = f111d_f111_dividend_coverage_volatility_calc063_200d_base_v063_signal

def f111d_f111_dividend_coverage_volatility_calc064_150d_base_v064_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc064_150d_base_v064_signal'] = f111d_f111_dividend_coverage_volatility_calc064_150d_base_v064_signal

def f111d_f111_dividend_coverage_volatility_calc065_21d_base_v065_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc065_21d_base_v065_signal'] = f111d_f111_dividend_coverage_volatility_calc065_21d_base_v065_signal

def f111d_f111_dividend_coverage_volatility_calc066_5d_base_v066_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc066_5d_base_v066_signal'] = f111d_f111_dividend_coverage_volatility_calc066_5d_base_v066_signal

def f111d_f111_dividend_coverage_volatility_calc067_63d_base_v067_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(63)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc067_63d_base_v067_signal'] = f111d_f111_dividend_coverage_volatility_calc067_63d_base_v067_signal

def f111d_f111_dividend_coverage_volatility_calc068_252d_base_v068_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc068_252d_base_v068_signal'] = f111d_f111_dividend_coverage_volatility_calc068_252d_base_v068_signal

def f111d_f111_dividend_coverage_volatility_calc069_126d_base_v069_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc069_126d_base_v069_signal'] = f111d_f111_dividend_coverage_volatility_calc069_126d_base_v069_signal

def f111d_f111_dividend_coverage_volatility_calc070_126d_base_v070_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc070_126d_base_v070_signal'] = f111d_f111_dividend_coverage_volatility_calc070_126d_base_v070_signal

def f111d_f111_dividend_coverage_volatility_calc071_84d_base_v071_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc071_84d_base_v071_signal'] = f111d_f111_dividend_coverage_volatility_calc071_84d_base_v071_signal

def f111d_f111_dividend_coverage_volatility_calc072_200d_base_v072_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(200)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc072_200d_base_v072_signal'] = f111d_f111_dividend_coverage_volatility_calc072_200d_base_v072_signal

def f111d_f111_dividend_coverage_volatility_calc073_21d_base_v073_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc073_21d_base_v073_signal'] = f111d_f111_dividend_coverage_volatility_calc073_21d_base_v073_signal

def f111d_f111_dividend_coverage_volatility_calc074_126d_base_v074_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc074_126d_base_v074_signal'] = f111d_f111_dividend_coverage_volatility_calc074_126d_base_v074_signal

def f111d_f111_dividend_coverage_volatility_calc075_150d_base_v075_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc075_150d_base_v075_signal'] = f111d_f111_dividend_coverage_volatility_calc075_150d_base_v075_signal


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
