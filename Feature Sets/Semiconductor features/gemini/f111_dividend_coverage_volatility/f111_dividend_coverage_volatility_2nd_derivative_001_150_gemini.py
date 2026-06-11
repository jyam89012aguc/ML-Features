import pandas as pd
import numpy as np
FEATURE_FUNCTIONS = {}

def f111d_f111_dividend_coverage_volatility_calc001_252d_slope_v001_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).skew()
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc001_252d_slope_v001_signal'] = f111d_f111_dividend_coverage_volatility_calc001_252d_slope_v001_signal

def f111d_f111_dividend_coverage_volatility_calc002_5d_slope_v002_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).skew()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc002_5d_slope_v002_signal'] = f111d_f111_dividend_coverage_volatility_calc002_5d_slope_v002_signal

def f111d_f111_dividend_coverage_volatility_calc003_5d_slope_v003_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(5).std()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc003_5d_slope_v003_signal'] = f111d_f111_dividend_coverage_volatility_calc003_5d_slope_v003_signal

def f111d_f111_dividend_coverage_volatility_calc004_126d_slope_v004_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc004_126d_slope_v004_signal'] = f111d_f111_dividend_coverage_volatility_calc004_126d_slope_v004_signal

def f111d_f111_dividend_coverage_volatility_calc005_5d_slope_v005_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(5)
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc005_5d_slope_v005_signal'] = f111d_f111_dividend_coverage_volatility_calc005_5d_slope_v005_signal

def f111d_f111_dividend_coverage_volatility_calc006_252d_slope_v006_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).quantile(0.5)
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc006_252d_slope_v006_signal'] = f111d_f111_dividend_coverage_volatility_calc006_252d_slope_v006_signal

def f111d_f111_dividend_coverage_volatility_calc007_200d_slope_v007_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).mean()
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc007_200d_slope_v007_signal'] = f111d_f111_dividend_coverage_volatility_calc007_200d_slope_v007_signal

def f111d_f111_dividend_coverage_volatility_calc008_126d_slope_v008_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(126).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc008_126d_slope_v008_signal'] = f111d_f111_dividend_coverage_volatility_calc008_126d_slope_v008_signal

def f111d_f111_dividend_coverage_volatility_calc009_21d_slope_v009_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).mean()
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc009_21d_slope_v009_signal'] = f111d_f111_dividend_coverage_volatility_calc009_21d_slope_v009_signal

def f111d_f111_dividend_coverage_volatility_calc010_10d_slope_v010_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).kurt()
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc010_10d_slope_v010_signal'] = f111d_f111_dividend_coverage_volatility_calc010_10d_slope_v010_signal

def f111d_f111_dividend_coverage_volatility_calc011_21d_slope_v011_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).skew()
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc011_21d_slope_v011_signal'] = f111d_f111_dividend_coverage_volatility_calc011_21d_slope_v011_signal

def f111d_f111_dividend_coverage_volatility_calc012_84d_slope_v012_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).skew()
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc012_84d_slope_v012_signal'] = f111d_f111_dividend_coverage_volatility_calc012_84d_slope_v012_signal

def f111d_f111_dividend_coverage_volatility_calc013_42d_slope_v013_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(42).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc013_42d_slope_v013_signal'] = f111d_f111_dividend_coverage_volatility_calc013_42d_slope_v013_signal

def f111d_f111_dividend_coverage_volatility_calc014_5d_slope_v014_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).std()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc014_5d_slope_v014_signal'] = f111d_f111_dividend_coverage_volatility_calc014_5d_slope_v014_signal

def f111d_f111_dividend_coverage_volatility_calc015_42d_slope_v015_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc015_42d_slope_v015_signal'] = f111d_f111_dividend_coverage_volatility_calc015_42d_slope_v015_signal

def f111d_f111_dividend_coverage_volatility_calc016_10d_slope_v016_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).max()
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc016_10d_slope_v016_signal'] = f111d_f111_dividend_coverage_volatility_calc016_10d_slope_v016_signal

def f111d_f111_dividend_coverage_volatility_calc017_252d_slope_v017_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).quantile(0.5)
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc017_252d_slope_v017_signal'] = f111d_f111_dividend_coverage_volatility_calc017_252d_slope_v017_signal

def f111d_f111_dividend_coverage_volatility_calc018_21d_slope_v018_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).rank(pct=True)
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc018_21d_slope_v018_signal'] = f111d_f111_dividend_coverage_volatility_calc018_21d_slope_v018_signal

def f111d_f111_dividend_coverage_volatility_calc019_42d_slope_v019_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).max()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc019_42d_slope_v019_signal'] = f111d_f111_dividend_coverage_volatility_calc019_42d_slope_v019_signal

def f111d_f111_dividend_coverage_volatility_calc020_126d_slope_v020_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).quantile(0.5)
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc020_126d_slope_v020_signal'] = f111d_f111_dividend_coverage_volatility_calc020_126d_slope_v020_signal

def f111d_f111_dividend_coverage_volatility_calc021_252d_slope_v021_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc021_252d_slope_v021_signal'] = f111d_f111_dividend_coverage_volatility_calc021_252d_slope_v021_signal

def f111d_f111_dividend_coverage_volatility_calc022_84d_slope_v022_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(84).std()
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc022_84d_slope_v022_signal'] = f111d_f111_dividend_coverage_volatility_calc022_84d_slope_v022_signal

def f111d_f111_dividend_coverage_volatility_calc023_200d_slope_v023_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(200).mean()) / v_003.rolling(200).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc023_200d_slope_v023_signal'] = f111d_f111_dividend_coverage_volatility_calc023_200d_slope_v023_signal

def f111d_f111_dividend_coverage_volatility_calc024_105d_slope_v024_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).rank(pct=True)
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc024_105d_slope_v024_signal'] = f111d_f111_dividend_coverage_volatility_calc024_105d_slope_v024_signal

def f111d_f111_dividend_coverage_volatility_calc025_126d_slope_v025_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc025_126d_slope_v025_signal'] = f111d_f111_dividend_coverage_volatility_calc025_126d_slope_v025_signal

def f111d_f111_dividend_coverage_volatility_calc026_42d_slope_v026_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).skew()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc026_42d_slope_v026_signal'] = f111d_f111_dividend_coverage_volatility_calc026_42d_slope_v026_signal

def f111d_f111_dividend_coverage_volatility_calc027_150d_slope_v027_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).quantile(0.5)
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc027_150d_slope_v027_signal'] = f111d_f111_dividend_coverage_volatility_calc027_150d_slope_v027_signal

def f111d_f111_dividend_coverage_volatility_calc028_126d_slope_v028_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(126)
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc028_126d_slope_v028_signal'] = f111d_f111_dividend_coverage_volatility_calc028_126d_slope_v028_signal

def f111d_f111_dividend_coverage_volatility_calc029_126d_slope_v029_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(126)
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc029_126d_slope_v029_signal'] = f111d_f111_dividend_coverage_volatility_calc029_126d_slope_v029_signal

def f111d_f111_dividend_coverage_volatility_calc030_252d_slope_v030_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).max()
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc030_252d_slope_v030_signal'] = f111d_f111_dividend_coverage_volatility_calc030_252d_slope_v030_signal

def f111d_f111_dividend_coverage_volatility_calc031_21d_slope_v031_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(21).std()
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc031_21d_slope_v031_signal'] = f111d_f111_dividend_coverage_volatility_calc031_21d_slope_v031_signal

def f111d_f111_dividend_coverage_volatility_calc032_105d_slope_v032_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).kurt()
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc032_105d_slope_v032_signal'] = f111d_f111_dividend_coverage_volatility_calc032_105d_slope_v032_signal

def f111d_f111_dividend_coverage_volatility_calc033_126d_slope_v033_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(126).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc033_126d_slope_v033_signal'] = f111d_f111_dividend_coverage_volatility_calc033_126d_slope_v033_signal

def f111d_f111_dividend_coverage_volatility_calc034_10d_slope_v034_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).rank(pct=True)
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc034_10d_slope_v034_signal'] = f111d_f111_dividend_coverage_volatility_calc034_10d_slope_v034_signal

def f111d_f111_dividend_coverage_volatility_calc035_42d_slope_v035_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc035_42d_slope_v035_signal'] = f111d_f111_dividend_coverage_volatility_calc035_42d_slope_v035_signal

def f111d_f111_dividend_coverage_volatility_calc036_10d_slope_v036_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(10).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc036_10d_slope_v036_signal'] = f111d_f111_dividend_coverage_volatility_calc036_10d_slope_v036_signal

def f111d_f111_dividend_coverage_volatility_calc037_105d_slope_v037_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).mean()
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc037_105d_slope_v037_signal'] = f111d_f111_dividend_coverage_volatility_calc037_105d_slope_v037_signal

def f111d_f111_dividend_coverage_volatility_calc038_10d_slope_v038_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc038_10d_slope_v038_signal'] = f111d_f111_dividend_coverage_volatility_calc038_10d_slope_v038_signal

def f111d_f111_dividend_coverage_volatility_calc039_252d_slope_v039_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).min()
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc039_252d_slope_v039_signal'] = f111d_f111_dividend_coverage_volatility_calc039_252d_slope_v039_signal

def f111d_f111_dividend_coverage_volatility_calc040_42d_slope_v040_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).skew()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc040_42d_slope_v040_signal'] = f111d_f111_dividend_coverage_volatility_calc040_42d_slope_v040_signal

def f111d_f111_dividend_coverage_volatility_calc041_105d_slope_v041_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).std()
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc041_105d_slope_v041_signal'] = f111d_f111_dividend_coverage_volatility_calc041_105d_slope_v041_signal

def f111d_f111_dividend_coverage_volatility_calc042_21d_slope_v042_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).min()
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc042_21d_slope_v042_signal'] = f111d_f111_dividend_coverage_volatility_calc042_21d_slope_v042_signal

def f111d_f111_dividend_coverage_volatility_calc043_42d_slope_v043_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(42).std()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc043_42d_slope_v043_signal'] = f111d_f111_dividend_coverage_volatility_calc043_42d_slope_v043_signal

def f111d_f111_dividend_coverage_volatility_calc044_63d_slope_v044_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).max()
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc044_63d_slope_v044_signal'] = f111d_f111_dividend_coverage_volatility_calc044_63d_slope_v044_signal

def f111d_f111_dividend_coverage_volatility_calc045_42d_slope_v045_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(42).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc045_42d_slope_v045_signal'] = f111d_f111_dividend_coverage_volatility_calc045_42d_slope_v045_signal

def f111d_f111_dividend_coverage_volatility_calc046_150d_slope_v046_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).skew()
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc046_150d_slope_v046_signal'] = f111d_f111_dividend_coverage_volatility_calc046_150d_slope_v046_signal

def f111d_f111_dividend_coverage_volatility_calc047_42d_slope_v047_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(42)
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc047_42d_slope_v047_signal'] = f111d_f111_dividend_coverage_volatility_calc047_42d_slope_v047_signal

def f111d_f111_dividend_coverage_volatility_calc048_42d_slope_v048_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).rank(pct=True)
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc048_42d_slope_v048_signal'] = f111d_f111_dividend_coverage_volatility_calc048_42d_slope_v048_signal

def f111d_f111_dividend_coverage_volatility_calc049_42d_slope_v049_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).var()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc049_42d_slope_v049_signal'] = f111d_f111_dividend_coverage_volatility_calc049_42d_slope_v049_signal

def f111d_f111_dividend_coverage_volatility_calc050_200d_slope_v050_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).max()
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc050_200d_slope_v050_signal'] = f111d_f111_dividend_coverage_volatility_calc050_200d_slope_v050_signal

def f111d_f111_dividend_coverage_volatility_calc051_84d_slope_v051_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).mean()
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc051_84d_slope_v051_signal'] = f111d_f111_dividend_coverage_volatility_calc051_84d_slope_v051_signal

def f111d_f111_dividend_coverage_volatility_calc052_10d_slope_v052_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(10).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc052_10d_slope_v052_signal'] = f111d_f111_dividend_coverage_volatility_calc052_10d_slope_v052_signal

def f111d_f111_dividend_coverage_volatility_calc053_84d_slope_v053_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).kurt()
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc053_84d_slope_v053_signal'] = f111d_f111_dividend_coverage_volatility_calc053_84d_slope_v053_signal

def f111d_f111_dividend_coverage_volatility_calc054_10d_slope_v054_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(10).std()
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc054_10d_slope_v054_signal'] = f111d_f111_dividend_coverage_volatility_calc054_10d_slope_v054_signal

def f111d_f111_dividend_coverage_volatility_calc055_200d_slope_v055_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).min()
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc055_200d_slope_v055_signal'] = f111d_f111_dividend_coverage_volatility_calc055_200d_slope_v055_signal

def f111d_f111_dividend_coverage_volatility_calc056_200d_slope_v056_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).mean()
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc056_200d_slope_v056_signal'] = f111d_f111_dividend_coverage_volatility_calc056_200d_slope_v056_signal

def f111d_f111_dividend_coverage_volatility_calc057_252d_slope_v057_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(252)
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc057_252d_slope_v057_signal'] = f111d_f111_dividend_coverage_volatility_calc057_252d_slope_v057_signal

def f111d_f111_dividend_coverage_volatility_calc058_21d_slope_v058_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).quantile(0.5)
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc058_21d_slope_v058_signal'] = f111d_f111_dividend_coverage_volatility_calc058_21d_slope_v058_signal

def f111d_f111_dividend_coverage_volatility_calc059_200d_slope_v059_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).skew()
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc059_200d_slope_v059_signal'] = f111d_f111_dividend_coverage_volatility_calc059_200d_slope_v059_signal

def f111d_f111_dividend_coverage_volatility_calc060_150d_slope_v060_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(150)
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc060_150d_slope_v060_signal'] = f111d_f111_dividend_coverage_volatility_calc060_150d_slope_v060_signal

def f111d_f111_dividend_coverage_volatility_calc061_21d_slope_v061_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).var()
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc061_21d_slope_v061_signal'] = f111d_f111_dividend_coverage_volatility_calc061_21d_slope_v061_signal

def f111d_f111_dividend_coverage_volatility_calc062_105d_slope_v062_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).var()
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc062_105d_slope_v062_signal'] = f111d_f111_dividend_coverage_volatility_calc062_105d_slope_v062_signal

def f111d_f111_dividend_coverage_volatility_calc063_200d_slope_v063_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).rank(pct=True)
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc063_200d_slope_v063_signal'] = f111d_f111_dividend_coverage_volatility_calc063_200d_slope_v063_signal

def f111d_f111_dividend_coverage_volatility_calc064_150d_slope_v064_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).kurt()
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc064_150d_slope_v064_signal'] = f111d_f111_dividend_coverage_volatility_calc064_150d_slope_v064_signal

def f111d_f111_dividend_coverage_volatility_calc065_21d_slope_v065_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).mean()
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc065_21d_slope_v065_signal'] = f111d_f111_dividend_coverage_volatility_calc065_21d_slope_v065_signal

def f111d_f111_dividend_coverage_volatility_calc066_5d_slope_v066_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(5)
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc066_5d_slope_v066_signal'] = f111d_f111_dividend_coverage_volatility_calc066_5d_slope_v066_signal

def f111d_f111_dividend_coverage_volatility_calc067_63d_slope_v067_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(63)
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc067_63d_slope_v067_signal'] = f111d_f111_dividend_coverage_volatility_calc067_63d_slope_v067_signal

def f111d_f111_dividend_coverage_volatility_calc068_252d_slope_v068_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc068_252d_slope_v068_signal'] = f111d_f111_dividend_coverage_volatility_calc068_252d_slope_v068_signal

def f111d_f111_dividend_coverage_volatility_calc069_126d_slope_v069_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).quantile(0.5)
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc069_126d_slope_v069_signal'] = f111d_f111_dividend_coverage_volatility_calc069_126d_slope_v069_signal

def f111d_f111_dividend_coverage_volatility_calc070_126d_slope_v070_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).mean()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc070_126d_slope_v070_signal'] = f111d_f111_dividend_coverage_volatility_calc070_126d_slope_v070_signal

def f111d_f111_dividend_coverage_volatility_calc071_84d_slope_v071_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).kurt()
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc071_84d_slope_v071_signal'] = f111d_f111_dividend_coverage_volatility_calc071_84d_slope_v071_signal

def f111d_f111_dividend_coverage_volatility_calc072_200d_slope_v072_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(200)
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc072_200d_slope_v072_signal'] = f111d_f111_dividend_coverage_volatility_calc072_200d_slope_v072_signal

def f111d_f111_dividend_coverage_volatility_calc073_21d_slope_v073_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc073_21d_slope_v073_signal'] = f111d_f111_dividend_coverage_volatility_calc073_21d_slope_v073_signal

def f111d_f111_dividend_coverage_volatility_calc074_126d_slope_v074_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).var()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc074_126d_slope_v074_signal'] = f111d_f111_dividend_coverage_volatility_calc074_126d_slope_v074_signal

def f111d_f111_dividend_coverage_volatility_calc075_150d_slope_v075_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc075_150d_slope_v075_signal'] = f111d_f111_dividend_coverage_volatility_calc075_150d_slope_v075_signal

def f111d_f111_dividend_coverage_volatility_calc076_5d_slope_v076_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).mean()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc076_5d_slope_v076_signal'] = f111d_f111_dividend_coverage_volatility_calc076_5d_slope_v076_signal

def f111d_f111_dividend_coverage_volatility_calc077_21d_slope_v077_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).var()
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc077_21d_slope_v077_signal'] = f111d_f111_dividend_coverage_volatility_calc077_21d_slope_v077_signal

def f111d_f111_dividend_coverage_volatility_calc078_126d_slope_v078_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(126)
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc078_126d_slope_v078_signal'] = f111d_f111_dividend_coverage_volatility_calc078_126d_slope_v078_signal

def f111d_f111_dividend_coverage_volatility_calc079_105d_slope_v079_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(105)
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc079_105d_slope_v079_signal'] = f111d_f111_dividend_coverage_volatility_calc079_105d_slope_v079_signal

def f111d_f111_dividend_coverage_volatility_calc080_84d_slope_v080_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).rank(pct=True)
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc080_84d_slope_v080_signal'] = f111d_f111_dividend_coverage_volatility_calc080_84d_slope_v080_signal

def f111d_f111_dividend_coverage_volatility_calc081_126d_slope_v081_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).kurt()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc081_126d_slope_v081_signal'] = f111d_f111_dividend_coverage_volatility_calc081_126d_slope_v081_signal

def f111d_f111_dividend_coverage_volatility_calc082_63d_slope_v082_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(63).std()
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc082_63d_slope_v082_signal'] = f111d_f111_dividend_coverage_volatility_calc082_63d_slope_v082_signal

def f111d_f111_dividend_coverage_volatility_calc083_252d_slope_v083_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(252)
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc083_252d_slope_v083_signal'] = f111d_f111_dividend_coverage_volatility_calc083_252d_slope_v083_signal

def f111d_f111_dividend_coverage_volatility_calc084_42d_slope_v084_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).min()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc084_42d_slope_v084_signal'] = f111d_f111_dividend_coverage_volatility_calc084_42d_slope_v084_signal

def f111d_f111_dividend_coverage_volatility_calc085_150d_slope_v085_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).var()
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc085_150d_slope_v085_signal'] = f111d_f111_dividend_coverage_volatility_calc085_150d_slope_v085_signal

def f111d_f111_dividend_coverage_volatility_calc086_200d_slope_v086_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).std()
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc086_200d_slope_v086_signal'] = f111d_f111_dividend_coverage_volatility_calc086_200d_slope_v086_signal

def f111d_f111_dividend_coverage_volatility_calc087_63d_slope_v087_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).rank(pct=True)
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc087_63d_slope_v087_signal'] = f111d_f111_dividend_coverage_volatility_calc087_63d_slope_v087_signal

def f111d_f111_dividend_coverage_volatility_calc088_84d_slope_v088_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(84).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc088_84d_slope_v088_signal'] = f111d_f111_dividend_coverage_volatility_calc088_84d_slope_v088_signal

def f111d_f111_dividend_coverage_volatility_calc089_84d_slope_v089_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).kurt()
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc089_84d_slope_v089_signal'] = f111d_f111_dividend_coverage_volatility_calc089_84d_slope_v089_signal

def f111d_f111_dividend_coverage_volatility_calc090_84d_slope_v090_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).quantile(0.5)
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc090_84d_slope_v090_signal'] = f111d_f111_dividend_coverage_volatility_calc090_84d_slope_v090_signal

def f111d_f111_dividend_coverage_volatility_calc091_5d_slope_v091_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).min()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc091_5d_slope_v091_signal'] = f111d_f111_dividend_coverage_volatility_calc091_5d_slope_v091_signal

def f111d_f111_dividend_coverage_volatility_calc092_105d_slope_v092_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).std()
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc092_105d_slope_v092_signal'] = f111d_f111_dividend_coverage_volatility_calc092_105d_slope_v092_signal

def f111d_f111_dividend_coverage_volatility_calc093_84d_slope_v093_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(84)
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc093_84d_slope_v093_signal'] = f111d_f111_dividend_coverage_volatility_calc093_84d_slope_v093_signal

def f111d_f111_dividend_coverage_volatility_calc094_21d_slope_v094_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc094_21d_slope_v094_signal'] = f111d_f111_dividend_coverage_volatility_calc094_21d_slope_v094_signal

def f111d_f111_dividend_coverage_volatility_calc095_150d_slope_v095_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).skew()
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc095_150d_slope_v095_signal'] = f111d_f111_dividend_coverage_volatility_calc095_150d_slope_v095_signal

def f111d_f111_dividend_coverage_volatility_calc096_252d_slope_v096_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc096_252d_slope_v096_signal'] = f111d_f111_dividend_coverage_volatility_calc096_252d_slope_v096_signal

def f111d_f111_dividend_coverage_volatility_calc097_126d_slope_v097_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).quantile(0.5)
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc097_126d_slope_v097_signal'] = f111d_f111_dividend_coverage_volatility_calc097_126d_slope_v097_signal

def f111d_f111_dividend_coverage_volatility_calc098_63d_slope_v098_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc098_63d_slope_v098_signal'] = f111d_f111_dividend_coverage_volatility_calc098_63d_slope_v098_signal

def f111d_f111_dividend_coverage_volatility_calc099_21d_slope_v099_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc099_21d_slope_v099_signal'] = f111d_f111_dividend_coverage_volatility_calc099_21d_slope_v099_signal

def f111d_f111_dividend_coverage_volatility_calc100_42d_slope_v100_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(42).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc100_42d_slope_v100_signal'] = f111d_f111_dividend_coverage_volatility_calc100_42d_slope_v100_signal

def f111d_f111_dividend_coverage_volatility_calc101_21d_slope_v101_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc101_21d_slope_v101_signal'] = f111d_f111_dividend_coverage_volatility_calc101_21d_slope_v101_signal

def f111d_f111_dividend_coverage_volatility_calc102_10d_slope_v102_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).skew()
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc102_10d_slope_v102_signal'] = f111d_f111_dividend_coverage_volatility_calc102_10d_slope_v102_signal

def f111d_f111_dividend_coverage_volatility_calc103_126d_slope_v103_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(126)
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc103_126d_slope_v103_signal'] = f111d_f111_dividend_coverage_volatility_calc103_126d_slope_v103_signal

def f111d_f111_dividend_coverage_volatility_calc104_150d_slope_v104_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).quantile(0.5)
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc104_150d_slope_v104_signal'] = f111d_f111_dividend_coverage_volatility_calc104_150d_slope_v104_signal

def f111d_f111_dividend_coverage_volatility_calc105_150d_slope_v105_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc105_150d_slope_v105_signal'] = f111d_f111_dividend_coverage_volatility_calc105_150d_slope_v105_signal

def f111d_f111_dividend_coverage_volatility_calc106_5d_slope_v106_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(5)
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc106_5d_slope_v106_signal'] = f111d_f111_dividend_coverage_volatility_calc106_5d_slope_v106_signal

def f111d_f111_dividend_coverage_volatility_calc107_63d_slope_v107_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).mean()
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc107_63d_slope_v107_signal'] = f111d_f111_dividend_coverage_volatility_calc107_63d_slope_v107_signal

def f111d_f111_dividend_coverage_volatility_calc108_84d_slope_v108_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).max()
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc108_84d_slope_v108_signal'] = f111d_f111_dividend_coverage_volatility_calc108_84d_slope_v108_signal

def f111d_f111_dividend_coverage_volatility_calc109_84d_slope_v109_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).var()
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc109_84d_slope_v109_signal'] = f111d_f111_dividend_coverage_volatility_calc109_84d_slope_v109_signal

def f111d_f111_dividend_coverage_volatility_calc110_10d_slope_v110_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(10).mean()) / v_003.rolling(10).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc110_10d_slope_v110_signal'] = f111d_f111_dividend_coverage_volatility_calc110_10d_slope_v110_signal

def f111d_f111_dividend_coverage_volatility_calc111_63d_slope_v111_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(63).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc111_63d_slope_v111_signal'] = f111d_f111_dividend_coverage_volatility_calc111_63d_slope_v111_signal

def f111d_f111_dividend_coverage_volatility_calc112_126d_slope_v112_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(126).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc112_126d_slope_v112_signal'] = f111d_f111_dividend_coverage_volatility_calc112_126d_slope_v112_signal

def f111d_f111_dividend_coverage_volatility_calc113_21d_slope_v113_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(21).std()
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc113_21d_slope_v113_signal'] = f111d_f111_dividend_coverage_volatility_calc113_21d_slope_v113_signal

def f111d_f111_dividend_coverage_volatility_calc114_84d_slope_v114_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(84).mean()) / v_003.rolling(84).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc114_84d_slope_v114_signal'] = f111d_f111_dividend_coverage_volatility_calc114_84d_slope_v114_signal

def f111d_f111_dividend_coverage_volatility_calc115_105d_slope_v115_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).quantile(0.5)
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc115_105d_slope_v115_signal'] = f111d_f111_dividend_coverage_volatility_calc115_105d_slope_v115_signal

def f111d_f111_dividend_coverage_volatility_calc116_126d_slope_v116_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(126)
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc116_126d_slope_v116_signal'] = f111d_f111_dividend_coverage_volatility_calc116_126d_slope_v116_signal

def f111d_f111_dividend_coverage_volatility_calc117_42d_slope_v117_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(42)
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc117_42d_slope_v117_signal'] = f111d_f111_dividend_coverage_volatility_calc117_42d_slope_v117_signal

def f111d_f111_dividend_coverage_volatility_calc118_21d_slope_v118_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(21)
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc118_21d_slope_v118_signal'] = f111d_f111_dividend_coverage_volatility_calc118_21d_slope_v118_signal

def f111d_f111_dividend_coverage_volatility_calc119_42d_slope_v119_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc119_42d_slope_v119_signal'] = f111d_f111_dividend_coverage_volatility_calc119_42d_slope_v119_signal

def f111d_f111_dividend_coverage_volatility_calc120_5d_slope_v120_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc120_5d_slope_v120_signal'] = f111d_f111_dividend_coverage_volatility_calc120_5d_slope_v120_signal

def f111d_f111_dividend_coverage_volatility_calc121_105d_slope_v121_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).kurt()
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc121_105d_slope_v121_signal'] = f111d_f111_dividend_coverage_volatility_calc121_105d_slope_v121_signal

def f111d_f111_dividend_coverage_volatility_calc122_252d_slope_v122_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc122_252d_slope_v122_signal'] = f111d_f111_dividend_coverage_volatility_calc122_252d_slope_v122_signal

def f111d_f111_dividend_coverage_volatility_calc123_84d_slope_v123_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(84)
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc123_84d_slope_v123_signal'] = f111d_f111_dividend_coverage_volatility_calc123_84d_slope_v123_signal

def f111d_f111_dividend_coverage_volatility_calc124_5d_slope_v124_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(5)
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc124_5d_slope_v124_signal'] = f111d_f111_dividend_coverage_volatility_calc124_5d_slope_v124_signal

def f111d_f111_dividend_coverage_volatility_calc125_10d_slope_v125_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc125_10d_slope_v125_signal'] = f111d_f111_dividend_coverage_volatility_calc125_10d_slope_v125_signal

def f111d_f111_dividend_coverage_volatility_calc126_84d_slope_v126_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(84)
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc126_84d_slope_v126_signal'] = f111d_f111_dividend_coverage_volatility_calc126_84d_slope_v126_signal

def f111d_f111_dividend_coverage_volatility_calc127_42d_slope_v127_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc127_42d_slope_v127_signal'] = f111d_f111_dividend_coverage_volatility_calc127_42d_slope_v127_signal

def f111d_f111_dividend_coverage_volatility_calc128_252d_slope_v128_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).mean()
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc128_252d_slope_v128_signal'] = f111d_f111_dividend_coverage_volatility_calc128_252d_slope_v128_signal

def f111d_f111_dividend_coverage_volatility_calc129_252d_slope_v129_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc129_252d_slope_v129_signal'] = f111d_f111_dividend_coverage_volatility_calc129_252d_slope_v129_signal

def f111d_f111_dividend_coverage_volatility_calc130_105d_slope_v130_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).quantile(0.5)
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc130_105d_slope_v130_signal'] = f111d_f111_dividend_coverage_volatility_calc130_105d_slope_v130_signal

def f111d_f111_dividend_coverage_volatility_calc131_21d_slope_v131_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc131_21d_slope_v131_signal'] = f111d_f111_dividend_coverage_volatility_calc131_21d_slope_v131_signal

def f111d_f111_dividend_coverage_volatility_calc132_21d_slope_v132_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(21)
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc132_21d_slope_v132_signal'] = f111d_f111_dividend_coverage_volatility_calc132_21d_slope_v132_signal

def f111d_f111_dividend_coverage_volatility_calc133_105d_slope_v133_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).max()
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc133_105d_slope_v133_signal'] = f111d_f111_dividend_coverage_volatility_calc133_105d_slope_v133_signal

def f111d_f111_dividend_coverage_volatility_calc134_150d_slope_v134_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc134_150d_slope_v134_signal'] = f111d_f111_dividend_coverage_volatility_calc134_150d_slope_v134_signal

def f111d_f111_dividend_coverage_volatility_calc135_63d_slope_v135_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).quantile(0.5)
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc135_63d_slope_v135_signal'] = f111d_f111_dividend_coverage_volatility_calc135_63d_slope_v135_signal

def f111d_f111_dividend_coverage_volatility_calc136_105d_slope_v136_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).skew()
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc136_105d_slope_v136_signal'] = f111d_f111_dividend_coverage_volatility_calc136_105d_slope_v136_signal

def f111d_f111_dividend_coverage_volatility_calc137_63d_slope_v137_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).quantile(0.5)
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc137_63d_slope_v137_signal'] = f111d_f111_dividend_coverage_volatility_calc137_63d_slope_v137_signal

def f111d_f111_dividend_coverage_volatility_calc138_5d_slope_v138_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).quantile(0.5)
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc138_5d_slope_v138_signal'] = f111d_f111_dividend_coverage_volatility_calc138_5d_slope_v138_signal

def f111d_f111_dividend_coverage_volatility_calc139_5d_slope_v139_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).max()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc139_5d_slope_v139_signal'] = f111d_f111_dividend_coverage_volatility_calc139_5d_slope_v139_signal

def f111d_f111_dividend_coverage_volatility_calc140_126d_slope_v140_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).std()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc140_126d_slope_v140_signal'] = f111d_f111_dividend_coverage_volatility_calc140_126d_slope_v140_signal

def f111d_f111_dividend_coverage_volatility_calc141_42d_slope_v141_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).min()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc141_42d_slope_v141_signal'] = f111d_f111_dividend_coverage_volatility_calc141_42d_slope_v141_signal

def f111d_f111_dividend_coverage_volatility_calc142_5d_slope_v142_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).rank(pct=True)
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc142_5d_slope_v142_signal'] = f111d_f111_dividend_coverage_volatility_calc142_5d_slope_v142_signal

def f111d_f111_dividend_coverage_volatility_calc143_21d_slope_v143_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(21).std()
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc143_21d_slope_v143_signal'] = f111d_f111_dividend_coverage_volatility_calc143_21d_slope_v143_signal

def f111d_f111_dividend_coverage_volatility_calc144_42d_slope_v144_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(42).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc144_42d_slope_v144_signal'] = f111d_f111_dividend_coverage_volatility_calc144_42d_slope_v144_signal

def f111d_f111_dividend_coverage_volatility_calc145_150d_slope_v145_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).min()
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc145_150d_slope_v145_signal'] = f111d_f111_dividend_coverage_volatility_calc145_150d_slope_v145_signal

def f111d_f111_dividend_coverage_volatility_calc146_84d_slope_v146_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).max()
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc146_84d_slope_v146_signal'] = f111d_f111_dividend_coverage_volatility_calc146_84d_slope_v146_signal

def f111d_f111_dividend_coverage_volatility_calc147_126d_slope_v147_signal(debt, fcf):
    v_001 = debt
    v_002 = fcf
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc147_126d_slope_v147_signal'] = f111d_f111_dividend_coverage_volatility_calc147_126d_slope_v147_signal

def f111d_f111_dividend_coverage_volatility_calc148_5d_slope_v148_signal(fcf, netinc):
    v_001 = fcf
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).min()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc148_5d_slope_v148_signal'] = f111d_f111_dividend_coverage_volatility_calc148_5d_slope_v148_signal

def f111d_f111_dividend_coverage_volatility_calc149_150d_slope_v149_signal(liabilities, netinc):
    v_001 = liabilities
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).max()
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc149_150d_slope_v149_signal'] = f111d_f111_dividend_coverage_volatility_calc149_150d_slope_v149_signal

def f111d_f111_dividend_coverage_volatility_calc150_252d_slope_v150_signal(ebitda, intexp):
    v_001 = ebitda
    v_002 = intexp
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f111d_f111_dividend_coverage_volatility_calc150_252d_slope_v150_signal'] = f111d_f111_dividend_coverage_volatility_calc150_252d_slope_v150_signal


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
