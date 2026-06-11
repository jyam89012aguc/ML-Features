import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f157o_f157_operating_income_to_liabilities_cycles_calc001_252d_slope_v001_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(10).mean()
    v_003 = v_002.rolling(252).max() / v_002.rolling(252).min().replace(0, np.nan)
    v_004 = (v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan)
    v_005 = v_004.rolling(10).var()
    v_006 = v_005.rolling(21).min()
    v_007 = v_006.rolling(126).rank(pct=True)
    v_008 = v_007.rolling(63).skew()
    v_009 = v_008.rolling(21).mean()
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc001_252d_slope_v001_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc001_252d_slope_v001_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc002_21d_slope_v002_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(21).var()
    v_003 = v_002.rolling(5).std()
    v_004 = v_003.rolling(10).mean()
    v_005 = (v_004 - v_004.rolling(252).mean()) / v_004.rolling(252).std().replace(0, np.nan)
    v_006 = (v_005 - v_005.rolling(126).mean()) / v_005.rolling(126).std().replace(0, np.nan)
    v_007 = v_006.rolling(252).skew()
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc002_21d_slope_v002_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc002_21d_slope_v002_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc003_42d_slope_v003_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(63).skew()
    v_003 = v_002.rolling(21).std()
    v_004 = v_003.rolling(126).std()
    v_005 = v_004.rolling(21).var()
    v_006 = v_005.rolling(42).std()
    v_007 = v_006.rolling(63).kurt()
    res = v_007.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc003_42d_slope_v003_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc003_42d_slope_v003_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc004_42d_slope_v004_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(10).kurt()
    v_003 = v_002.rolling(252).mean()
    v_004 = v_003.rolling(252).min()
    v_005 = v_004.rolling(252).skew()
    v_006 = v_005.rolling(42).max() / v_005.rolling(42).min().replace(0, np.nan)
    v_007 = v_006.rolling(63).rank(pct=True)
    v_008 = v_007.rolling(42).rank(pct=True)
    v_009 = v_008.rolling(21).var()
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc004_42d_slope_v004_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc004_42d_slope_v004_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc005_10d_slope_v005_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(126).mean()
    v_003 = v_002.rolling(5).min()
    v_004 = v_003.rolling(42).rank(pct=True)
    v_005 = v_004.rolling(126).std()
    v_006 = v_005.rolling(5).rank(pct=True)
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc005_10d_slope_v005_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc005_10d_slope_v005_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc006_63d_slope_v006_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(63).kurt()
    v_003 = v_002.rolling(63).mean()
    v_004 = v_003.rolling(10).std()
    v_005 = v_004.rolling(10).std()
    v_006 = v_005.rolling(5).skew()
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc006_63d_slope_v006_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc006_63d_slope_v006_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc007_10d_slope_v007_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(252).std()
    v_003 = v_002.rolling(252).kurt()
    v_004 = v_003.rolling(252).var()
    v_005 = v_004.rolling(21).std()
    v_006 = v_005.rolling(21).var()
    v_007 = v_006.rolling(5).skew()
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc007_10d_slope_v007_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc007_10d_slope_v007_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc008_42d_slope_v008_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(63).skew()
    v_003 = v_002.rolling(63).min()
    v_004 = v_003.rolling(21).var()
    v_005 = v_004.rolling(252).kurt()
    v_006 = v_005.rolling(10).min()
    v_007 = v_006.rolling(42).std()
    res = v_007.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc008_42d_slope_v008_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc008_42d_slope_v008_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc009_5d_slope_v009_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(5).mean()
    v_003 = v_002.rolling(10).max()
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.rolling(42).skew()
    v_006 = v_005.rolling(252).max()
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc009_5d_slope_v009_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc009_5d_slope_v009_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc010_252d_slope_v010_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(10).kurt()
    v_003 = v_002.rolling(126).min()
    v_004 = v_003.rolling(5).rank(pct=True)
    v_005 = v_004.rolling(42).max()
    v_006 = v_005.rolling(5).mean()
    v_007 = v_006.rolling(10).skew()
    res = v_007.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc010_252d_slope_v010_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc010_252d_slope_v010_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc011_21d_slope_v011_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(5).skew()
    v_003 = v_002.rolling(63).kurt()
    v_004 = v_003.rolling(21).max() / v_003.rolling(21).min().replace(0, np.nan)
    v_005 = v_004.rolling(10).max()
    v_006 = v_005.rolling(126).std()
    v_007 = v_006.rolling(10).skew()
    v_008 = v_007.rolling(5).max() / v_007.rolling(5).min().replace(0, np.nan)
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc011_21d_slope_v011_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc011_21d_slope_v011_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc012_5d_slope_v012_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(63).mean()
    v_003 = v_002.rolling(63).mean()
    v_004 = v_003.rolling(63).max()
    v_005 = (v_004 - v_004.rolling(126).mean()) / v_004.rolling(126).std().replace(0, np.nan)
    v_006 = v_005.rolling(126).kurt()
    v_007 = v_006.rolling(10).skew()
    v_008 = v_007.rolling(10).skew()
    v_009 = v_008.rolling(21).rank(pct=True)
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc012_5d_slope_v012_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc012_5d_slope_v012_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc013_42d_slope_v013_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(126).rank(pct=True)
    v_003 = v_002.rolling(42).min()
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.rolling(21).max() / v_004.rolling(21).min().replace(0, np.nan)
    v_006 = v_005.rolling(126).std()
    v_007 = v_006.rolling(42).rank(pct=True)
    v_008 = v_007.rolling(5).var()
    res = v_008.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc013_42d_slope_v013_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc013_42d_slope_v013_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc014_5d_slope_v014_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(126).max() / v_001.rolling(126).min().replace(0, np.nan)
    v_003 = (v_002 - v_002.rolling(126).mean()) / v_002.rolling(126).std().replace(0, np.nan)
    v_004 = v_003.rolling(63).mean()
    v_005 = v_004.rolling(63).max()
    v_006 = v_005.rolling(42).rank(pct=True)
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc014_5d_slope_v014_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc014_5d_slope_v014_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc015_63d_slope_v015_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(21).kurt()
    v_003 = v_002.rolling(63).kurt()
    v_004 = v_003.rolling(126).kurt()
    v_005 = v_004.rolling(42).max()
    v_006 = v_005.rolling(21).kurt()
    v_007 = v_006.rolling(21).kurt()
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc015_63d_slope_v015_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc015_63d_slope_v015_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc016_10d_slope_v016_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(5).skew()
    v_003 = v_002.rolling(10).std()
    v_004 = v_003.rolling(5).std()
    v_005 = v_004.rolling(10).kurt()
    v_006 = v_005.rolling(126).max()
    v_007 = v_006.rolling(63).max() / v_006.rolling(63).min().replace(0, np.nan)
    v_008 = v_007.rolling(5).var()
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc016_10d_slope_v016_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc016_10d_slope_v016_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc017_42d_slope_v017_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(10).skew()
    v_003 = v_002.rolling(252).mean()
    v_004 = v_003.rolling(10).std()
    v_005 = v_004.rolling(252).mean()
    v_006 = v_005.rolling(63).max()
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc017_42d_slope_v017_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc017_42d_slope_v017_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc018_252d_slope_v018_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(126).skew()
    v_003 = v_002.rolling(126).max()
    v_004 = v_003.rolling(126).rank(pct=True)
    v_005 = v_004.rolling(10).rank(pct=True)
    v_006 = v_005.rolling(63).std()
    v_007 = v_006.rolling(5).max() / v_006.rolling(5).min().replace(0, np.nan)
    v_008 = v_007.rolling(126).mean()
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc018_252d_slope_v018_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc018_252d_slope_v018_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc019_21d_slope_v019_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(252).mean()
    v_003 = v_002.rolling(63).var()
    v_004 = v_003.rolling(21).max() / v_003.rolling(21).min().replace(0, np.nan)
    v_005 = v_004.rolling(63).std()
    v_006 = (v_005 - v_005.rolling(21).mean()) / v_005.rolling(21).std().replace(0, np.nan)
    v_007 = v_006.rolling(21).kurt()
    v_008 = v_007.rolling(252).std()
    v_009 = v_008.rolling(252).mean()
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc019_21d_slope_v019_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc019_21d_slope_v019_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc020_126d_slope_v020_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(63).rank(pct=True)
    v_003 = v_002.rolling(5).skew()
    v_004 = v_003.rolling(63).max() / v_003.rolling(63).min().replace(0, np.nan)
    v_005 = v_004.rolling(252).var()
    v_006 = v_005.rolling(42).skew()
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc020_126d_slope_v020_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc020_126d_slope_v020_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc021_21d_slope_v021_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(5).std()
    v_003 = v_002.rolling(10).min()
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.rolling(126).std()
    v_006 = v_005.rolling(126).max()
    res = v_006.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc021_21d_slope_v021_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc021_21d_slope_v021_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc022_63d_slope_v022_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(5).rank(pct=True)
    v_003 = v_002.rolling(252).mean()
    v_004 = v_003.rolling(63).rank(pct=True)
    v_005 = v_004.rolling(5).mean()
    v_006 = v_005.rolling(42).std()
    v_007 = v_006.rolling(10).std()
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc022_63d_slope_v022_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc022_63d_slope_v022_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc023_126d_slope_v023_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(21).max() / v_001.rolling(21).min().replace(0, np.nan)
    v_003 = v_002.rolling(21).var()
    v_004 = v_003.rolling(10).max() / v_003.rolling(10).min().replace(0, np.nan)
    v_005 = v_004.rolling(126).skew()
    v_006 = v_005.rolling(42).min()
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc023_126d_slope_v023_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc023_126d_slope_v023_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc024_5d_slope_v024_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(21).skew()
    v_003 = v_002.rolling(63).skew()
    v_004 = v_003.rolling(21).var()
    v_005 = v_004.rolling(21).max() / v_004.rolling(21).min().replace(0, np.nan)
    v_006 = v_005.rolling(5).kurt()
    v_007 = v_006.rolling(126).mean()
    v_008 = v_007.rolling(42).rank(pct=True)
    v_009 = v_008.rolling(5).mean()
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc024_5d_slope_v024_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc024_5d_slope_v024_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc025_5d_slope_v025_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(63).max()
    v_003 = v_002.rolling(42).rank(pct=True)
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.rolling(10).skew()
    v_006 = v_005.rolling(10).max() / v_005.rolling(10).min().replace(0, np.nan)
    res = v_006.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc025_5d_slope_v025_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc025_5d_slope_v025_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc026_21d_slope_v026_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(10).std()
    v_003 = v_002.rolling(252).max()
    v_004 = v_003.rolling(5).max() / v_003.rolling(5).min().replace(0, np.nan)
    v_005 = v_004.rolling(126).var()
    v_006 = v_005.rolling(10).var()
    v_007 = v_006.rolling(21).rank(pct=True)
    v_008 = v_007.rolling(5).std()
    res = v_008.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc026_21d_slope_v026_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc026_21d_slope_v026_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc027_42d_slope_v027_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(10).skew()
    v_003 = v_002.rolling(42).std()
    v_004 = v_003.rolling(5).mean()
    v_005 = v_004.rolling(126).rank(pct=True)
    v_006 = (v_005 - v_005.rolling(42).mean()) / v_005.rolling(42).std().replace(0, np.nan)
    v_007 = v_006.rolling(5).max() / v_006.rolling(5).min().replace(0, np.nan)
    v_008 = v_007.rolling(42).std()
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc027_42d_slope_v027_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc027_42d_slope_v027_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc028_5d_slope_v028_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(126).max()
    v_003 = v_002.rolling(10).std()
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.rolling(10).skew()
    v_006 = v_005.rolling(21).rank(pct=True)
    v_007 = v_006.rolling(5).max()
    v_008 = (v_007 - v_007.rolling(5).mean()) / v_007.rolling(5).std().replace(0, np.nan)
    v_009 = v_008.rolling(42).mean()
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc028_5d_slope_v028_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc028_5d_slope_v028_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc029_42d_slope_v029_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(5).var()
    v_003 = v_002.rolling(10).std()
    v_004 = v_003.rolling(10).min()
    v_005 = v_004.rolling(10).max()
    v_006 = (v_005 - v_005.rolling(21).mean()) / v_005.rolling(21).std().replace(0, np.nan)
    v_007 = v_006.rolling(252).kurt()
    v_008 = v_007.rolling(126).max() / v_007.rolling(126).min().replace(0, np.nan)
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc029_42d_slope_v029_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc029_42d_slope_v029_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc030_21d_slope_v030_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(63).max()
    v_003 = v_002.rolling(10).rank(pct=True)
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.rolling(10).rank(pct=True)
    v_006 = v_005.rolling(10).kurt()
    res = v_006.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc030_21d_slope_v030_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc030_21d_slope_v030_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc031_42d_slope_v031_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(5).std()
    v_003 = v_002.rolling(10).min()
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.rolling(42).skew()
    v_006 = v_005.rolling(63).std()
    v_007 = v_006.rolling(126).max() / v_006.rolling(126).min().replace(0, np.nan)
    res = v_007.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc031_42d_slope_v031_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc031_42d_slope_v031_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc032_63d_slope_v032_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(5).var()
    v_003 = v_002.rolling(42).max()
    v_004 = v_003.rolling(21).skew()
    v_005 = v_004.rolling(21).kurt()
    v_006 = v_005.rolling(21).mean()
    v_007 = v_006.rolling(126).mean()
    v_008 = v_007.rolling(10).std()
    v_009 = v_008.rolling(5).mean()
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc032_63d_slope_v032_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc032_63d_slope_v032_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc033_126d_slope_v033_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = (v_001 - v_001.rolling(21).mean()) / v_001.rolling(21).std().replace(0, np.nan)
    v_003 = v_002.rolling(21).var()
    v_004 = v_003.rolling(5).min()
    v_005 = v_004.rolling(10).std()
    v_006 = v_005.rolling(42).max() / v_005.rolling(42).min().replace(0, np.nan)
    v_007 = v_006.rolling(21).mean()
    v_008 = v_007.rolling(5).max() / v_007.rolling(5).min().replace(0, np.nan)
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc033_126d_slope_v033_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc033_126d_slope_v033_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc034_21d_slope_v034_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(126).mean()
    v_003 = v_002.rolling(63).min()
    v_004 = v_003.rolling(21).min()
    v_005 = (v_004 - v_004.rolling(126).mean()) / v_004.rolling(126).std().replace(0, np.nan)
    v_006 = v_005.rolling(10).max() / v_005.rolling(10).min().replace(0, np.nan)
    v_007 = v_006.rolling(42).min()
    v_008 = v_007.rolling(5).kurt()
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc034_21d_slope_v034_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc034_21d_slope_v034_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc035_126d_slope_v035_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(5).var()
    v_003 = v_002.rolling(63).kurt()
    v_004 = v_003.rolling(21).min()
    v_005 = v_004.rolling(126).max() / v_004.rolling(126).min().replace(0, np.nan)
    v_006 = v_005.rolling(252).var()
    v_007 = (v_006 - v_006.rolling(63).mean()) / v_006.rolling(63).std().replace(0, np.nan)
    res = v_007.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc035_126d_slope_v035_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc035_126d_slope_v035_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc036_252d_slope_v036_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(63).std()
    v_003 = v_002.rolling(252).max() / v_002.rolling(252).min().replace(0, np.nan)
    v_004 = v_003.rolling(21).max()
    v_005 = v_004.rolling(42).mean()
    v_006 = v_005.rolling(42).kurt()
    v_007 = v_006.rolling(42).kurt()
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc036_252d_slope_v036_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc036_252d_slope_v036_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc037_42d_slope_v037_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(5).max() / v_001.rolling(5).min().replace(0, np.nan)
    v_003 = v_002.rolling(5).min()
    v_004 = (v_003 - v_003.rolling(126).mean()) / v_003.rolling(126).std().replace(0, np.nan)
    v_005 = v_004.rolling(42).std()
    v_006 = v_005.rolling(252).max()
    v_007 = v_006.rolling(5).max()
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc037_42d_slope_v037_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc037_42d_slope_v037_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc038_10d_slope_v038_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(3)
    v_002 = (v_001 - v_001.rolling(10).mean()) / v_001.rolling(10).std().replace(0, np.nan)
    v_003 = v_002.rolling(10).skew()
    v_004 = v_003.rolling(10).min()
    v_005 = v_004.rolling(126).min()
    v_006 = v_005.rolling(252).skew()
    v_007 = v_006.rolling(42).max()
    v_008 = v_007.rolling(126).max()
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc038_10d_slope_v038_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc038_10d_slope_v038_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc039_63d_slope_v039_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(63).max() / v_001.rolling(63).min().replace(0, np.nan)
    v_003 = v_002.rolling(10).kurt()
    v_004 = (v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan)
    v_005 = v_004.rolling(10).max()
    v_006 = v_005.rolling(5).max() / v_005.rolling(5).min().replace(0, np.nan)
    v_007 = v_006.rolling(21).rank(pct=True)
    v_008 = v_007.rolling(21).rank(pct=True)
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc039_63d_slope_v039_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc039_63d_slope_v039_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc040_42d_slope_v040_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(126).mean()
    v_003 = v_002.rolling(21).min()
    v_004 = v_003.rolling(5).mean()
    v_005 = v_004.rolling(21).max()
    v_006 = v_005.rolling(42).rank(pct=True)
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc040_42d_slope_v040_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc040_42d_slope_v040_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc041_21d_slope_v041_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(10).mean()
    v_003 = v_002.rolling(10).max() / v_002.rolling(10).min().replace(0, np.nan)
    v_004 = v_003.rolling(5).max() / v_003.rolling(5).min().replace(0, np.nan)
    v_005 = v_004.rolling(126).max()
    v_006 = v_005.rolling(5).min()
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc041_21d_slope_v041_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc041_21d_slope_v041_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc042_252d_slope_v042_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = (v_001 - v_001.rolling(21).mean()) / v_001.rolling(21).std().replace(0, np.nan)
    v_003 = v_002.rolling(10).max() / v_002.rolling(10).min().replace(0, np.nan)
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.rolling(10).std()
    v_006 = v_005.rolling(10).var()
    v_007 = v_006.rolling(21).std()
    v_008 = v_007.rolling(42).rank(pct=True)
    v_009 = v_008.rolling(42).kurt()
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc042_252d_slope_v042_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc042_252d_slope_v042_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc043_42d_slope_v043_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(42).min()
    v_003 = v_002.rolling(126).rank(pct=True)
    v_004 = v_003.rolling(5).max() / v_003.rolling(5).min().replace(0, np.nan)
    v_005 = v_004.rolling(10).max() / v_004.rolling(10).min().replace(0, np.nan)
    v_006 = v_005.rolling(252).rank(pct=True)
    v_007 = v_006.rolling(126).std()
    res = v_007.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc043_42d_slope_v043_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc043_42d_slope_v043_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc044_10d_slope_v044_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(10).std()
    v_003 = v_002.rolling(126).var()
    v_004 = v_003.rolling(5).std()
    v_005 = v_004.rolling(10).max()
    v_006 = v_005.rolling(63).skew()
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc044_10d_slope_v044_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc044_10d_slope_v044_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc045_252d_slope_v045_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(252).skew()
    v_003 = v_002.rolling(10).skew()
    v_004 = (v_003 - v_003.rolling(252).mean()) / v_003.rolling(252).std().replace(0, np.nan)
    v_005 = v_004.rolling(21).kurt()
    v_006 = v_005.rolling(126).rank(pct=True)
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc045_252d_slope_v045_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc045_252d_slope_v045_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc046_5d_slope_v046_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(10).kurt()
    v_003 = v_002.rolling(42).rank(pct=True)
    v_004 = v_003.rolling(42).min()
    v_005 = v_004.rolling(21).rank(pct=True)
    v_006 = v_005.rolling(42).mean()
    v_007 = v_006.rolling(10).rank(pct=True)
    v_008 = v_007.rolling(63).skew()
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc046_5d_slope_v046_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc046_5d_slope_v046_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc047_252d_slope_v047_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(63).kurt()
    v_003 = v_002.rolling(5).max() / v_002.rolling(5).min().replace(0, np.nan)
    v_004 = v_003.rolling(252).max()
    v_005 = v_004.rolling(10).std()
    v_006 = v_005.rolling(10).skew()
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc047_252d_slope_v047_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc047_252d_slope_v047_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc048_252d_slope_v048_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(10).max() / v_001.rolling(10).min().replace(0, np.nan)
    v_003 = v_002.rolling(126).std()
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.rolling(5).rank(pct=True)
    v_006 = (v_005 - v_005.rolling(5).mean()) / v_005.rolling(5).std().replace(0, np.nan)
    v_007 = v_006.rolling(21).max() / v_006.rolling(21).min().replace(0, np.nan)
    v_008 = v_007.rolling(63).kurt()
    res = v_008.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc048_252d_slope_v048_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc048_252d_slope_v048_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc049_42d_slope_v049_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(10).min()
    v_003 = v_002.rolling(42).rank(pct=True)
    v_004 = v_003.rolling(21).max()
    v_005 = v_004.rolling(10).min()
    v_006 = v_005.rolling(10).std()
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc049_42d_slope_v049_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc049_42d_slope_v049_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc050_126d_slope_v050_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(42).max() / v_001.rolling(42).min().replace(0, np.nan)
    v_003 = v_002.rolling(21).mean()
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.rolling(252).skew()
    v_006 = v_005.rolling(252).rank(pct=True)
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc050_126d_slope_v050_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc050_126d_slope_v050_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc051_21d_slope_v051_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(126).var()
    v_003 = v_002.rolling(252).var()
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.rolling(42).min()
    v_006 = v_005.rolling(10).max() / v_005.rolling(10).min().replace(0, np.nan)
    v_007 = v_006.rolling(21).kurt()
    v_008 = v_007.rolling(10).rank(pct=True)
    v_009 = v_008.rolling(21).std()
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc051_21d_slope_v051_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc051_21d_slope_v051_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc052_10d_slope_v052_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(252).min()
    v_003 = v_002.rolling(10).mean()
    v_004 = (v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan)
    v_005 = v_004.rolling(63).std()
    v_006 = v_005.rolling(63).var()
    v_007 = v_006.rolling(42).max()
    v_008 = v_007.rolling(63).max()
    v_009 = (v_008 - v_008.rolling(42).mean()) / v_008.rolling(42).std().replace(0, np.nan)
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc052_10d_slope_v052_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc052_10d_slope_v052_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc053_5d_slope_v053_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(5).mean()
    v_003 = (v_002 - v_002.rolling(252).mean()) / v_002.rolling(252).std().replace(0, np.nan)
    v_004 = v_003.rolling(21).skew()
    v_005 = v_004.rolling(42).max()
    v_006 = v_005.rolling(5).rank(pct=True)
    v_007 = v_006.rolling(21).skew()
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc053_5d_slope_v053_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc053_5d_slope_v053_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc054_126d_slope_v054_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(1)
    v_002 = (v_001 - v_001.rolling(10).mean()) / v_001.rolling(10).std().replace(0, np.nan)
    v_003 = (v_002 - v_002.rolling(5).mean()) / v_002.rolling(5).std().replace(0, np.nan)
    v_004 = v_003.rolling(5).rank(pct=True)
    v_005 = v_004.rolling(42).rank(pct=True)
    v_006 = v_005.rolling(126).skew()
    v_007 = v_006.rolling(21).std()
    v_008 = v_007.rolling(126).skew()
    v_009 = v_008.rolling(126).kurt()
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc054_126d_slope_v054_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc054_126d_slope_v054_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc055_42d_slope_v055_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(21).rank(pct=True)
    v_003 = v_002.rolling(5).rank(pct=True)
    v_004 = (v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan)
    v_005 = v_004.rolling(63).skew()
    v_006 = v_005.rolling(10).std()
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc055_42d_slope_v055_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc055_42d_slope_v055_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc056_126d_slope_v056_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(126).std()
    v_003 = v_002.rolling(42).mean()
    v_004 = v_003.rolling(21).skew()
    v_005 = v_004.rolling(10).kurt()
    v_006 = v_005.rolling(126).skew()
    v_007 = v_006.rolling(63).skew()
    v_008 = v_007.rolling(63).rank(pct=True)
    v_009 = v_008.rolling(5).rank(pct=True)
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc056_126d_slope_v056_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc056_126d_slope_v056_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc057_5d_slope_v057_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = (v_001 - v_001.rolling(42).mean()) / v_001.rolling(42).std().replace(0, np.nan)
    v_003 = v_002.rolling(21).rank(pct=True)
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.rolling(10).std()
    v_006 = (v_005 - v_005.rolling(42).mean()) / v_005.rolling(42).std().replace(0, np.nan)
    v_007 = v_006.rolling(5).min()
    v_008 = (v_007 - v_007.rolling(42).mean()) / v_007.rolling(42).std().replace(0, np.nan)
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc057_5d_slope_v057_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc057_5d_slope_v057_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc058_42d_slope_v058_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(10).std()
    v_003 = v_002.rolling(252).skew()
    v_004 = v_003.rolling(126).mean()
    v_005 = v_004.rolling(10).std()
    v_006 = v_005.rolling(5).max() / v_005.rolling(5).min().replace(0, np.nan)
    v_007 = v_006.rolling(5).kurt()
    v_008 = v_007.rolling(63).mean()
    v_009 = v_008.rolling(5).mean()
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc058_42d_slope_v058_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc058_42d_slope_v058_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc059_42d_slope_v059_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = (v_001 - v_001.rolling(63).mean()) / v_001.rolling(63).std().replace(0, np.nan)
    v_003 = v_002.rolling(252).skew()
    v_004 = v_003.rolling(10).max() / v_003.rolling(10).min().replace(0, np.nan)
    v_005 = v_004.rolling(10).max()
    v_006 = v_005.rolling(10).skew()
    res = v_006.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc059_42d_slope_v059_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc059_42d_slope_v059_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc060_63d_slope_v060_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(5).mean()
    v_003 = v_002.rolling(5).max() / v_002.rolling(5).min().replace(0, np.nan)
    v_004 = v_003.rolling(252).mean()
    v_005 = v_004.rolling(42).max() / v_004.rolling(42).min().replace(0, np.nan)
    v_006 = v_005.rolling(10).max()
    res = v_006.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc060_63d_slope_v060_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc060_63d_slope_v060_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc061_126d_slope_v061_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(42).mean()
    v_003 = v_002.rolling(5).max()
    v_004 = v_003.rolling(252).max()
    v_005 = v_004.rolling(5).rank(pct=True)
    v_006 = v_005.rolling(252).min()
    res = v_006.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc061_126d_slope_v061_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc061_126d_slope_v061_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc062_126d_slope_v062_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(126).rank(pct=True)
    v_003 = v_002.rolling(5).var()
    v_004 = v_003.rolling(126).kurt()
    v_005 = (v_004 - v_004.rolling(10).mean()) / v_004.rolling(10).std().replace(0, np.nan)
    v_006 = v_005.rolling(252).rank(pct=True)
    v_007 = v_006.rolling(63).rank(pct=True)
    res = v_007.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc062_126d_slope_v062_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc062_126d_slope_v062_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc063_5d_slope_v063_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(21).max() / v_001.rolling(21).min().replace(0, np.nan)
    v_003 = v_002.rolling(252).min()
    v_004 = v_003.rolling(5).std()
    v_005 = v_004.rolling(10).std()
    v_006 = (v_005 - v_005.rolling(63).mean()) / v_005.rolling(63).std().replace(0, np.nan)
    v_007 = v_006.rolling(5).min()
    v_008 = v_007.rolling(63).rank(pct=True)
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc063_5d_slope_v063_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc063_5d_slope_v063_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc064_5d_slope_v064_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(63).max() / v_001.rolling(63).min().replace(0, np.nan)
    v_003 = v_002.rolling(42).kurt()
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.rolling(10).mean()
    v_006 = v_005.rolling(10).max() / v_005.rolling(10).min().replace(0, np.nan)
    v_007 = v_006.rolling(21).kurt()
    res = v_007.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc064_5d_slope_v064_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc064_5d_slope_v064_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc065_10d_slope_v065_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(126).rank(pct=True)
    v_003 = v_002.rolling(21).var()
    v_004 = v_003.rolling(21).var()
    v_005 = v_004.rolling(126).var()
    v_006 = v_005.rolling(5).rank(pct=True)
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc065_10d_slope_v065_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc065_10d_slope_v065_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc066_42d_slope_v066_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(42).std()
    v_003 = v_002.rolling(126).min()
    v_004 = v_003.rolling(42).rank(pct=True)
    v_005 = v_004.rolling(63).mean()
    v_006 = v_005.rolling(21).min()
    v_007 = v_006.rolling(5).mean()
    v_008 = v_007.rolling(63).std()
    res = v_008.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc066_42d_slope_v066_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc066_42d_slope_v066_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc067_42d_slope_v067_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(5).max()
    v_003 = v_002.rolling(252).rank(pct=True)
    v_004 = v_003.rolling(21).kurt()
    v_005 = v_004.rolling(10).std()
    v_006 = v_005.rolling(42).min()
    v_007 = v_006.rolling(10).kurt()
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc067_42d_slope_v067_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc067_42d_slope_v067_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc068_126d_slope_v068_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(126).var()
    v_003 = v_002.rolling(252).max()
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.rolling(10).kurt()
    v_006 = v_005.rolling(42).kurt()
    v_007 = v_006.rolling(10).std()
    v_008 = v_007.rolling(21).std()
    v_009 = v_008.rolling(21).kurt()
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc068_126d_slope_v068_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc068_126d_slope_v068_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc069_63d_slope_v069_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(5).var()
    v_003 = v_002.rolling(10).max()
    v_004 = v_003.rolling(10).var()
    v_005 = (v_004 - v_004.rolling(21).mean()) / v_004.rolling(21).std().replace(0, np.nan)
    v_006 = v_005.rolling(5).min()
    v_007 = v_006.rolling(252).min()
    v_008 = v_007.rolling(5).std()
    res = v_008.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc069_63d_slope_v069_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc069_63d_slope_v069_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc070_5d_slope_v070_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = (v_001 - v_001.rolling(252).mean()) / v_001.rolling(252).std().replace(0, np.nan)
    v_003 = v_002.rolling(252).skew()
    v_004 = v_003.rolling(21).std()
    v_005 = v_004.rolling(126).max() / v_004.rolling(126).min().replace(0, np.nan)
    v_006 = v_005.rolling(5).rank(pct=True)
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc070_5d_slope_v070_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc070_5d_slope_v070_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc071_126d_slope_v071_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(252).var()
    v_003 = v_002.rolling(63).std()
    v_004 = (v_003 - v_003.rolling(126).mean()) / v_003.rolling(126).std().replace(0, np.nan)
    v_005 = v_004.rolling(10).max() / v_004.rolling(10).min().replace(0, np.nan)
    v_006 = v_005.rolling(5).skew()
    v_007 = v_006.rolling(21).std()
    v_008 = v_007.rolling(10).max() / v_007.rolling(10).min().replace(0, np.nan)
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc071_126d_slope_v071_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc071_126d_slope_v071_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc072_10d_slope_v072_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(21).std()
    v_003 = v_002.rolling(42).min()
    v_004 = v_003.rolling(63).skew()
    v_005 = v_004.rolling(10).min()
    v_006 = v_005.rolling(126).kurt()
    v_007 = v_006.rolling(63).min()
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc072_10d_slope_v072_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc072_10d_slope_v072_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc073_5d_slope_v073_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(10).var()
    v_003 = v_002.rolling(252).var()
    v_004 = v_003.rolling(5).mean()
    v_005 = v_004.rolling(21).std()
    v_006 = v_005.rolling(126).max()
    v_007 = v_006.rolling(42).skew()
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc073_5d_slope_v073_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc073_5d_slope_v073_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc074_21d_slope_v074_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = (v_001 - v_001.rolling(42).mean()) / v_001.rolling(42).std().replace(0, np.nan)
    v_003 = v_002.rolling(252).max()
    v_004 = v_003.rolling(63).rank(pct=True)
    v_005 = v_004.rolling(10).std()
    v_006 = v_005.rolling(10).mean()
    v_007 = (v_006 - v_006.rolling(126).mean()) / v_006.rolling(126).std().replace(0, np.nan)
    res = v_007.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc074_21d_slope_v074_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc074_21d_slope_v074_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc075_10d_slope_v075_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(21).max() / v_001.rolling(21).min().replace(0, np.nan)
    v_003 = v_002.rolling(252).max()
    v_004 = v_003.rolling(126).kurt()
    v_005 = v_004.rolling(126).var()
    v_006 = v_005.rolling(42).var()
    res = v_006.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc075_10d_slope_v075_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc075_10d_slope_v075_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc076_21d_slope_v076_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(10).kurt()
    v_003 = v_002.rolling(42).var()
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.rolling(63).max()
    v_006 = v_005.rolling(63).rank(pct=True)
    v_007 = v_006.rolling(42).std()
    v_008 = v_007.rolling(252).max() / v_007.rolling(252).min().replace(0, np.nan)
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc076_21d_slope_v076_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc076_21d_slope_v076_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc077_10d_slope_v077_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(5).kurt()
    v_003 = v_002.rolling(63).skew()
    v_004 = v_003.rolling(5).std()
    v_005 = v_004.rolling(126).var()
    v_006 = v_005.rolling(63).min()
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc077_10d_slope_v077_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc077_10d_slope_v077_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc078_63d_slope_v078_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = (v_001 - v_001.rolling(10).mean()) / v_001.rolling(10).std().replace(0, np.nan)
    v_003 = v_002.rolling(63).var()
    v_004 = v_003.rolling(5).std()
    v_005 = (v_004 - v_004.rolling(252).mean()) / v_004.rolling(252).std().replace(0, np.nan)
    v_006 = v_005.rolling(5).var()
    v_007 = v_006.rolling(252).mean()
    v_008 = v_007.rolling(42).var()
    v_009 = v_008.rolling(5).std()
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc078_63d_slope_v078_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc078_63d_slope_v078_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc079_252d_slope_v079_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(252).max() / v_001.rolling(252).min().replace(0, np.nan)
    v_003 = v_002.rolling(126).std()
    v_004 = (v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan)
    v_005 = v_004.rolling(5).std()
    v_006 = v_005.rolling(5).skew()
    v_007 = v_006.rolling(252).rank(pct=True)
    v_008 = v_007.rolling(252).mean()
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc079_252d_slope_v079_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc079_252d_slope_v079_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc080_42d_slope_v080_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = (v_001 - v_001.rolling(63).mean()) / v_001.rolling(63).std().replace(0, np.nan)
    v_003 = v_002.rolling(10).std()
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.rolling(252).std()
    v_006 = v_005.rolling(252).skew()
    v_007 = v_006.rolling(42).min()
    v_008 = v_007.rolling(126).rank(pct=True)
    v_009 = v_008.rolling(126).std()
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc080_42d_slope_v080_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc080_42d_slope_v080_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc081_5d_slope_v081_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = (v_001 - v_001.rolling(5).mean()) / v_001.rolling(5).std().replace(0, np.nan)
    v_003 = v_002.rolling(63).rank(pct=True)
    v_004 = v_003.rolling(126).kurt()
    v_005 = v_004.rolling(252).min()
    v_006 = v_005.rolling(252).std()
    v_007 = v_006.rolling(252).max() / v_006.rolling(252).min().replace(0, np.nan)
    v_008 = v_007.rolling(10).max()
    v_009 = v_008.rolling(10).mean()
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc081_5d_slope_v081_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc081_5d_slope_v081_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc082_10d_slope_v082_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(63).skew()
    v_003 = v_002.rolling(5).max()
    v_004 = v_003.rolling(42).min()
    v_005 = v_004.rolling(126).skew()
    v_006 = v_005.rolling(42).rank(pct=True)
    v_007 = v_006.rolling(10).mean()
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc082_10d_slope_v082_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc082_10d_slope_v082_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc083_252d_slope_v083_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(252).std()
    v_003 = v_002.rolling(126).max() / v_002.rolling(126).min().replace(0, np.nan)
    v_004 = v_003.rolling(21).skew()
    v_005 = v_004.rolling(10).kurt()
    v_006 = v_005.rolling(126).skew()
    v_007 = v_006.rolling(252).min()
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc083_252d_slope_v083_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc083_252d_slope_v083_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc084_42d_slope_v084_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(21).rank(pct=True)
    v_003 = v_002.rolling(10).max() / v_002.rolling(10).min().replace(0, np.nan)
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.rolling(252).var()
    v_006 = v_005.rolling(252).mean()
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc084_42d_slope_v084_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc084_42d_slope_v084_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc085_126d_slope_v085_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(42).kurt()
    v_003 = v_002.rolling(10).kurt()
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.rolling(126).mean()
    v_006 = v_005.rolling(252).var()
    v_007 = v_006.rolling(10).rank(pct=True)
    v_008 = v_007.rolling(5).max() / v_007.rolling(5).min().replace(0, np.nan)
    v_009 = v_008.rolling(126).rank(pct=True)
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc085_126d_slope_v085_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc085_126d_slope_v085_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc086_42d_slope_v086_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(63).var()
    v_003 = v_002.rolling(63).min()
    v_004 = v_003.rolling(10).skew()
    v_005 = v_004.rolling(126).max()
    v_006 = v_005.rolling(5).max() / v_005.rolling(5).min().replace(0, np.nan)
    v_007 = (v_006 - v_006.rolling(63).mean()) / v_006.rolling(63).std().replace(0, np.nan)
    v_008 = v_007.rolling(63).skew()
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc086_42d_slope_v086_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc086_42d_slope_v086_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc087_21d_slope_v087_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = (v_001 - v_001.rolling(5).mean()) / v_001.rolling(5).std().replace(0, np.nan)
    v_003 = v_002.rolling(10).mean()
    v_004 = (v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan)
    v_005 = v_004.rolling(21).rank(pct=True)
    v_006 = v_005.rolling(42).max() / v_005.rolling(42).min().replace(0, np.nan)
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc087_21d_slope_v087_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc087_21d_slope_v087_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc088_252d_slope_v088_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(42).var()
    v_003 = v_002.rolling(42).max()
    v_004 = (v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan)
    v_005 = v_004.rolling(10).rank(pct=True)
    v_006 = v_005.rolling(42).max() / v_005.rolling(42).min().replace(0, np.nan)
    v_007 = v_006.rolling(63).kurt()
    v_008 = v_007.rolling(21).min()
    v_009 = v_008.rolling(252).rank(pct=True)
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc088_252d_slope_v088_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc088_252d_slope_v088_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc089_126d_slope_v089_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(63).mean()
    v_003 = v_002.rolling(63).kurt()
    v_004 = v_003.rolling(42).std()
    v_005 = (v_004 - v_004.rolling(63).mean()) / v_004.rolling(63).std().replace(0, np.nan)
    v_006 = v_005.rolling(21).mean()
    v_007 = v_006.rolling(42).kurt()
    v_008 = v_007.rolling(5).rank(pct=True)
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc089_126d_slope_v089_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc089_126d_slope_v089_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc090_252d_slope_v090_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(5).std()
    v_003 = v_002.rolling(10).kurt()
    v_004 = v_003.rolling(42).mean()
    v_005 = v_004.rolling(21).rank(pct=True)
    v_006 = (v_005 - v_005.rolling(5).mean()) / v_005.rolling(5).std().replace(0, np.nan)
    v_007 = (v_006 - v_006.rolling(126).mean()) / v_006.rolling(126).std().replace(0, np.nan)
    v_008 = v_007.rolling(21).mean()
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc090_252d_slope_v090_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc090_252d_slope_v090_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc091_63d_slope_v091_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(126).skew()
    v_003 = v_002.rolling(10).mean()
    v_004 = v_003.rolling(63).var()
    v_005 = v_004.rolling(10).mean()
    v_006 = v_005.rolling(5).max()
    v_007 = v_006.rolling(21).std()
    v_008 = v_007.rolling(10).min()
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc091_63d_slope_v091_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc091_63d_slope_v091_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc092_63d_slope_v092_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(126).min()
    v_003 = v_002.rolling(126).std()
    v_004 = v_003.rolling(21).std()
    v_005 = v_004.rolling(10).mean()
    v_006 = (v_005 - v_005.rolling(5).mean()) / v_005.rolling(5).std().replace(0, np.nan)
    res = v_006.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc092_63d_slope_v092_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc092_63d_slope_v092_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc093_21d_slope_v093_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(5).kurt()
    v_003 = v_002.rolling(10).var()
    v_004 = v_003.rolling(21).min()
    v_005 = v_004.rolling(42).min()
    v_006 = (v_005 - v_005.rolling(63).mean()) / v_005.rolling(63).std().replace(0, np.nan)
    v_007 = v_006.rolling(21).skew()
    v_008 = v_007.rolling(126).skew()
    v_009 = v_008.rolling(5).min()
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc093_21d_slope_v093_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc093_21d_slope_v093_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc094_252d_slope_v094_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(126).mean()
    v_003 = v_002.rolling(5).skew()
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.rolling(126).std()
    v_006 = v_005.rolling(21).max() / v_005.rolling(21).min().replace(0, np.nan)
    res = v_006.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc094_252d_slope_v094_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc094_252d_slope_v094_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc095_252d_slope_v095_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(63).var()
    v_003 = v_002.rolling(42).skew()
    v_004 = v_003.rolling(126).max() / v_003.rolling(126).min().replace(0, np.nan)
    v_005 = v_004.rolling(42).var()
    v_006 = v_005.rolling(252).kurt()
    v_007 = v_006.rolling(63).mean()
    v_008 = v_007.rolling(5).kurt()
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc095_252d_slope_v095_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc095_252d_slope_v095_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc096_252d_slope_v096_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(252).mean()
    v_003 = v_002.rolling(10).std()
    v_004 = v_003.rolling(5).rank(pct=True)
    v_005 = (v_004 - v_004.rolling(126).mean()) / v_004.rolling(126).std().replace(0, np.nan)
    v_006 = v_005.rolling(252).mean()
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc096_252d_slope_v096_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc096_252d_slope_v096_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc097_126d_slope_v097_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(5).kurt()
    v_003 = v_002.rolling(5).max() / v_002.rolling(5).min().replace(0, np.nan)
    v_004 = v_003.rolling(21).max() / v_003.rolling(21).min().replace(0, np.nan)
    v_005 = v_004.rolling(252).min()
    v_006 = v_005.rolling(21).std()
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc097_126d_slope_v097_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc097_126d_slope_v097_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc098_42d_slope_v098_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(252).mean()
    v_003 = v_002.rolling(252).rank(pct=True)
    v_004 = v_003.rolling(252).min()
    v_005 = v_004.rolling(126).std()
    v_006 = v_005.rolling(126).var()
    v_007 = v_006.rolling(63).kurt()
    res = v_007.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc098_42d_slope_v098_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc098_42d_slope_v098_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc099_21d_slope_v099_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(10).var()
    v_003 = v_002.rolling(21).kurt()
    v_004 = v_003.rolling(126).max() / v_003.rolling(126).min().replace(0, np.nan)
    v_005 = v_004.rolling(21).kurt()
    v_006 = v_005.rolling(252).max()
    v_007 = (v_006 - v_006.rolling(126).mean()) / v_006.rolling(126).std().replace(0, np.nan)
    v_008 = (v_007 - v_007.rolling(126).mean()) / v_007.rolling(126).std().replace(0, np.nan)
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc099_21d_slope_v099_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc099_21d_slope_v099_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc100_42d_slope_v100_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(126).skew()
    v_003 = (v_002 - v_002.rolling(42).mean()) / v_002.rolling(42).std().replace(0, np.nan)
    v_004 = v_003.rolling(10).std()
    v_005 = v_004.rolling(5).var()
    v_006 = v_005.rolling(10).mean()
    v_007 = v_006.rolling(252).min()
    res = v_007.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc100_42d_slope_v100_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc100_42d_slope_v100_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc101_126d_slope_v101_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(5).max()
    v_003 = v_002.rolling(10).rank(pct=True)
    v_004 = v_003.rolling(42).mean()
    v_005 = v_004.rolling(252).var()
    v_006 = v_005.rolling(63).min()
    v_007 = (v_006 - v_006.rolling(252).mean()) / v_006.rolling(252).std().replace(0, np.nan)
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc101_126d_slope_v101_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc101_126d_slope_v101_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc102_63d_slope_v102_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(126).rank(pct=True)
    v_003 = v_002.rolling(252).max() / v_002.rolling(252).min().replace(0, np.nan)
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.rolling(10).kurt()
    v_006 = v_005.rolling(5).var()
    v_007 = v_006.rolling(10).kurt()
    v_008 = v_007.rolling(42).skew()
    v_009 = v_008.rolling(21).rank(pct=True)
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc102_63d_slope_v102_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc102_63d_slope_v102_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc103_42d_slope_v103_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(63).kurt()
    v_003 = v_002.rolling(21).kurt()
    v_004 = v_003.rolling(10).std()
    v_005 = v_004.rolling(42).rank(pct=True)
    v_006 = v_005.rolling(42).max()
    v_007 = v_006.rolling(21).max()
    v_008 = v_007.rolling(42).skew()
    res = v_008.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc103_42d_slope_v103_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc103_42d_slope_v103_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc104_42d_slope_v104_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(10).std()
    v_003 = v_002.rolling(10).max() / v_002.rolling(10).min().replace(0, np.nan)
    v_004 = v_003.rolling(10).std()
    v_005 = v_004.rolling(21).min()
    v_006 = v_005.rolling(63).max()
    v_007 = v_006.rolling(63).var()
    v_008 = v_007.rolling(5).std()
    v_009 = v_008.rolling(126).skew()
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc104_42d_slope_v104_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc104_42d_slope_v104_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc105_63d_slope_v105_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(63).skew()
    v_003 = v_002.rolling(10).max() / v_002.rolling(10).min().replace(0, np.nan)
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.rolling(21).kurt()
    v_006 = (v_005 - v_005.rolling(63).mean()) / v_005.rolling(63).std().replace(0, np.nan)
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc105_63d_slope_v105_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc105_63d_slope_v105_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc106_21d_slope_v106_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(42).max() / v_001.rolling(42).min().replace(0, np.nan)
    v_003 = (v_002 - v_002.rolling(10).mean()) / v_002.rolling(10).std().replace(0, np.nan)
    v_004 = (v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan)
    v_005 = v_004.rolling(126).max() / v_004.rolling(126).min().replace(0, np.nan)
    v_006 = v_005.rolling(21).min()
    v_007 = v_006.rolling(5).skew()
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc106_21d_slope_v106_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc106_21d_slope_v106_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc107_10d_slope_v107_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(126).mean()
    v_003 = v_002.rolling(10).kurt()
    v_004 = v_003.rolling(21).rank(pct=True)
    v_005 = v_004.rolling(10).var()
    v_006 = v_005.rolling(126).skew()
    v_007 = v_006.rolling(42).var()
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc107_10d_slope_v107_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc107_10d_slope_v107_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc108_252d_slope_v108_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(126).rank(pct=True)
    v_003 = v_002.rolling(63).skew()
    v_004 = v_003.rolling(42).mean()
    v_005 = v_004.rolling(5).min()
    v_006 = v_005.rolling(252).var()
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc108_252d_slope_v108_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc108_252d_slope_v108_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc109_42d_slope_v109_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(126).min()
    v_003 = v_002.rolling(252).max() / v_002.rolling(252).min().replace(0, np.nan)
    v_004 = (v_003 - v_003.rolling(63).mean()) / v_003.rolling(63).std().replace(0, np.nan)
    v_005 = v_004.rolling(10).max()
    v_006 = v_005.rolling(252).rank(pct=True)
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc109_42d_slope_v109_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc109_42d_slope_v109_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc110_5d_slope_v110_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(126).var()
    v_003 = v_002.rolling(63).mean()
    v_004 = v_003.rolling(126).max() / v_003.rolling(126).min().replace(0, np.nan)
    v_005 = v_004.rolling(21).var()
    v_006 = v_005.rolling(42).mean()
    v_007 = v_006.rolling(252).skew()
    v_008 = v_007.rolling(21).mean()
    v_009 = v_008.rolling(63).mean()
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc110_5d_slope_v110_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc110_5d_slope_v110_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc111_5d_slope_v111_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(42).rank(pct=True)
    v_003 = (v_002 - v_002.rolling(126).mean()) / v_002.rolling(126).std().replace(0, np.nan)
    v_004 = v_003.rolling(21).rank(pct=True)
    v_005 = v_004.rolling(5).var()
    v_006 = (v_005 - v_005.rolling(63).mean()) / v_005.rolling(63).std().replace(0, np.nan)
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc111_5d_slope_v111_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc111_5d_slope_v111_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc112_21d_slope_v112_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = (v_001 - v_001.rolling(42).mean()) / v_001.rolling(42).std().replace(0, np.nan)
    v_003 = v_002.rolling(21).kurt()
    v_004 = v_003.rolling(42).max()
    v_005 = v_004.rolling(10).max()
    v_006 = v_005.rolling(126).max() / v_005.rolling(126).min().replace(0, np.nan)
    res = v_006.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc112_21d_slope_v112_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc112_21d_slope_v112_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc113_42d_slope_v113_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(3)
    v_002 = (v_001 - v_001.rolling(5).mean()) / v_001.rolling(5).std().replace(0, np.nan)
    v_003 = v_002.rolling(63).min()
    v_004 = v_003.rolling(252).mean()
    v_005 = v_004.rolling(5).min()
    v_006 = v_005.rolling(252).std()
    v_007 = v_006.rolling(63).var()
    v_008 = v_007.rolling(21).mean()
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc113_42d_slope_v113_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc113_42d_slope_v113_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc114_42d_slope_v114_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(63).rank(pct=True)
    v_003 = v_002.rolling(63).max() / v_002.rolling(63).min().replace(0, np.nan)
    v_004 = v_003.rolling(126).max()
    v_005 = v_004.rolling(21).rank(pct=True)
    v_006 = v_005.rolling(21).var()
    v_007 = v_006.rolling(252).kurt()
    v_008 = v_007.rolling(5).max() / v_007.rolling(5).min().replace(0, np.nan)
    v_009 = v_008.rolling(5).var()
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc114_42d_slope_v114_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc114_42d_slope_v114_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc115_10d_slope_v115_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(5).max() / v_001.rolling(5).min().replace(0, np.nan)
    v_003 = v_002.rolling(21).std()
    v_004 = v_003.rolling(5).skew()
    v_005 = v_004.rolling(10).max() / v_004.rolling(10).min().replace(0, np.nan)
    v_006 = v_005.rolling(21).mean()
    v_007 = v_006.rolling(126).max()
    v_008 = v_007.rolling(10).max()
    v_009 = v_008.rolling(126).kurt()
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc115_10d_slope_v115_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc115_10d_slope_v115_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc116_126d_slope_v116_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(10).max() / v_001.rolling(10).min().replace(0, np.nan)
    v_003 = v_002.rolling(42).skew()
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.rolling(42).std()
    v_006 = v_005.rolling(5).std()
    res = v_006.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc116_126d_slope_v116_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc116_126d_slope_v116_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc117_10d_slope_v117_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(252).mean()
    v_003 = v_002.rolling(10).min()
    v_004 = (v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan)
    v_005 = v_004.rolling(42).rank(pct=True)
    v_006 = v_005.rolling(10).max()
    v_007 = v_006.rolling(21).max() / v_006.rolling(21).min().replace(0, np.nan)
    v_008 = v_007.rolling(21).kurt()
    v_009 = v_008.rolling(126).min()
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc117_10d_slope_v117_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc117_10d_slope_v117_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc118_5d_slope_v118_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(42).max()
    v_003 = v_002.rolling(63).mean()
    v_004 = v_003.rolling(42).mean()
    v_005 = v_004.rolling(42).mean()
    v_006 = v_005.rolling(42).var()
    v_007 = v_006.rolling(42).std()
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc118_5d_slope_v118_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc118_5d_slope_v118_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc119_5d_slope_v119_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(21).min()
    v_003 = (v_002 - v_002.rolling(63).mean()) / v_002.rolling(63).std().replace(0, np.nan)
    v_004 = v_003.rolling(21).max()
    v_005 = v_004.rolling(63).rank(pct=True)
    v_006 = v_005.rolling(63).max()
    v_007 = v_006.rolling(5).max() / v_006.rolling(5).min().replace(0, np.nan)
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc119_5d_slope_v119_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc119_5d_slope_v119_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc120_126d_slope_v120_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(42).max()
    v_003 = v_002.rolling(5).skew()
    v_004 = v_003.rolling(21).skew()
    v_005 = v_004.rolling(21).kurt()
    v_006 = v_005.rolling(5).min()
    v_007 = v_006.rolling(63).max() / v_006.rolling(63).min().replace(0, np.nan)
    v_008 = v_007.rolling(126).var()
    v_009 = v_008.rolling(252).mean()
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc120_126d_slope_v120_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc120_126d_slope_v120_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc121_5d_slope_v121_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(126).max()
    v_003 = v_002.rolling(10).var()
    v_004 = (v_003 - v_003.rolling(126).mean()) / v_003.rolling(126).std().replace(0, np.nan)
    v_005 = v_004.rolling(21).rank(pct=True)
    v_006 = v_005.rolling(126).max() / v_005.rolling(126).min().replace(0, np.nan)
    v_007 = v_006.rolling(252).skew()
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc121_5d_slope_v121_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc121_5d_slope_v121_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc122_252d_slope_v122_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(63).rank(pct=True)
    v_003 = v_002.rolling(63).kurt()
    v_004 = v_003.rolling(10).kurt()
    v_005 = (v_004 - v_004.rolling(5).mean()) / v_004.rolling(5).std().replace(0, np.nan)
    v_006 = v_005.rolling(5).var()
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc122_252d_slope_v122_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc122_252d_slope_v122_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc123_5d_slope_v123_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(42).max() / v_001.rolling(42).min().replace(0, np.nan)
    v_003 = v_002.rolling(10).var()
    v_004 = (v_003 - v_003.rolling(252).mean()) / v_003.rolling(252).std().replace(0, np.nan)
    v_005 = v_004.rolling(21).max()
    v_006 = v_005.rolling(126).min()
    res = v_006.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc123_5d_slope_v123_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc123_5d_slope_v123_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc124_42d_slope_v124_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(10).rank(pct=True)
    v_003 = (v_002 - v_002.rolling(10).mean()) / v_002.rolling(10).std().replace(0, np.nan)
    v_004 = v_003.rolling(126).max()
    v_005 = v_004.rolling(10).max()
    v_006 = v_005.rolling(42).var()
    res = v_006.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc124_42d_slope_v124_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc124_42d_slope_v124_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc125_126d_slope_v125_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(42).std()
    v_003 = v_002.rolling(42).kurt()
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.rolling(10).std()
    v_006 = v_005.rolling(21).skew()
    v_007 = v_006.rolling(5).var()
    v_008 = v_007.rolling(42).min()
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc125_126d_slope_v125_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc125_126d_slope_v125_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc126_5d_slope_v126_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(42).rank(pct=True)
    v_003 = v_002.rolling(21).var()
    v_004 = v_003.rolling(10).skew()
    v_005 = v_004.rolling(63).mean()
    v_006 = v_005.rolling(10).max()
    v_007 = v_006.rolling(126).mean()
    v_008 = v_007.rolling(42).max()
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc126_5d_slope_v126_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc126_5d_slope_v126_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc127_10d_slope_v127_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(21).min()
    v_003 = v_002.rolling(126).var()
    v_004 = v_003.rolling(21).rank(pct=True)
    v_005 = v_004.rolling(42).max() / v_004.rolling(42).min().replace(0, np.nan)
    v_006 = v_005.rolling(252).kurt()
    v_007 = v_006.rolling(42).var()
    v_008 = v_007.rolling(63).var()
    res = v_008.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc127_10d_slope_v127_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc127_10d_slope_v127_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc128_42d_slope_v128_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(63).min()
    v_003 = v_002.rolling(63).mean()
    v_004 = v_003.rolling(252).min()
    v_005 = v_004.rolling(5).std()
    v_006 = v_005.rolling(5).skew()
    v_007 = v_006.rolling(10).rank(pct=True)
    v_008 = v_007.rolling(126).kurt()
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc128_42d_slope_v128_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc128_42d_slope_v128_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc129_63d_slope_v129_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = (v_001 - v_001.rolling(5).mean()) / v_001.rolling(5).std().replace(0, np.nan)
    v_003 = v_002.rolling(126).rank(pct=True)
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.rolling(5).std()
    v_006 = v_005.rolling(63).skew()
    v_007 = v_006.rolling(5).max() / v_006.rolling(5).min().replace(0, np.nan)
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc129_63d_slope_v129_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc129_63d_slope_v129_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc130_126d_slope_v130_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(21).rank(pct=True)
    v_003 = v_002.rolling(126).kurt()
    v_004 = v_003.rolling(42).var()
    v_005 = v_004.rolling(126).rank(pct=True)
    v_006 = v_005.rolling(63).min()
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc130_126d_slope_v130_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc130_126d_slope_v130_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc131_21d_slope_v131_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(3)
    v_002 = (v_001 - v_001.rolling(10).mean()) / v_001.rolling(10).std().replace(0, np.nan)
    v_003 = v_002.rolling(42).rank(pct=True)
    v_004 = v_003.rolling(252).max()
    v_005 = (v_004 - v_004.rolling(5).mean()) / v_004.rolling(5).std().replace(0, np.nan)
    v_006 = v_005.rolling(5).min()
    v_007 = v_006.rolling(10).kurt()
    v_008 = v_007.rolling(252).skew()
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc131_21d_slope_v131_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc131_21d_slope_v131_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc132_10d_slope_v132_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(10).mean()
    v_003 = v_002.rolling(42).max()
    v_004 = (v_003 - v_003.rolling(252).mean()) / v_003.rolling(252).std().replace(0, np.nan)
    v_005 = (v_004 - v_004.rolling(63).mean()) / v_004.rolling(63).std().replace(0, np.nan)
    v_006 = v_005.rolling(63).var()
    res = v_006.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc132_10d_slope_v132_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc132_10d_slope_v132_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc133_21d_slope_v133_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(126).std()
    v_003 = v_002.rolling(252).std()
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.rolling(10).kurt()
    v_006 = v_005.rolling(21).max()
    v_007 = v_006.rolling(5).kurt()
    v_008 = v_007.rolling(10).var()
    v_009 = v_008.rolling(63).skew()
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc133_21d_slope_v133_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc133_21d_slope_v133_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc134_63d_slope_v134_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(42).max() / v_001.rolling(42).min().replace(0, np.nan)
    v_003 = v_002.rolling(5).mean()
    v_004 = v_003.rolling(21).rank(pct=True)
    v_005 = v_004.rolling(63).kurt()
    v_006 = v_005.rolling(10).min()
    v_007 = v_006.rolling(63).max()
    v_008 = v_007.rolling(21).max()
    res = v_008.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc134_63d_slope_v134_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc134_63d_slope_v134_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc135_63d_slope_v135_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(21).skew()
    v_003 = v_002.rolling(21).std()
    v_004 = (v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan)
    v_005 = v_004.rolling(10).skew()
    v_006 = (v_005 - v_005.rolling(63).mean()) / v_005.rolling(63).std().replace(0, np.nan)
    res = v_006.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc135_63d_slope_v135_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc135_63d_slope_v135_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc136_5d_slope_v136_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(252).kurt()
    v_003 = v_002.rolling(63).min()
    v_004 = v_003.rolling(21).skew()
    v_005 = v_004.rolling(42).kurt()
    v_006 = v_005.rolling(126).min()
    v_007 = v_006.rolling(5).min()
    v_008 = v_007.rolling(42).max()
    v_009 = v_008.rolling(21).rank(pct=True)
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc136_5d_slope_v136_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc136_5d_slope_v136_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc137_252d_slope_v137_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(10).max()
    v_003 = v_002.rolling(42).mean()
    v_004 = v_003.rolling(21).var()
    v_005 = (v_004 - v_004.rolling(5).mean()) / v_004.rolling(5).std().replace(0, np.nan)
    v_006 = v_005.rolling(5).skew()
    v_007 = (v_006 - v_006.rolling(63).mean()) / v_006.rolling(63).std().replace(0, np.nan)
    v_008 = v_007.rolling(252).min()
    v_009 = v_008.rolling(126).std()
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc137_252d_slope_v137_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc137_252d_slope_v137_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc138_5d_slope_v138_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(126).std()
    v_003 = v_002.rolling(42).rank(pct=True)
    v_004 = v_003.rolling(63).std()
    v_005 = v_004.rolling(5).rank(pct=True)
    v_006 = v_005.rolling(5).var()
    v_007 = v_006.rolling(21).min()
    v_008 = v_007.rolling(10).mean()
    v_009 = v_008.rolling(42).mean()
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc138_5d_slope_v138_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc138_5d_slope_v138_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc139_126d_slope_v139_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = (v_001 - v_001.rolling(42).mean()) / v_001.rolling(42).std().replace(0, np.nan)
    v_003 = v_002.rolling(63).max()
    v_004 = v_003.rolling(252).skew()
    v_005 = v_004.rolling(252).skew()
    v_006 = (v_005 - v_005.rolling(252).mean()) / v_005.rolling(252).std().replace(0, np.nan)
    res = v_006.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc139_126d_slope_v139_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc139_126d_slope_v139_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc140_252d_slope_v140_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(21).rank(pct=True)
    v_003 = v_002.rolling(21).skew()
    v_004 = v_003.rolling(63).mean()
    v_005 = (v_004 - v_004.rolling(21).mean()) / v_004.rolling(21).std().replace(0, np.nan)
    v_006 = v_005.rolling(63).rank(pct=True)
    v_007 = v_006.rolling(42).std()
    v_008 = v_007.rolling(126).kurt()
    v_009 = v_008.rolling(5).kurt()
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc140_252d_slope_v140_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc140_252d_slope_v140_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc141_63d_slope_v141_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(126).var()
    v_003 = v_002.rolling(21).max() / v_002.rolling(21).min().replace(0, np.nan)
    v_004 = v_003.rolling(21).max()
    v_005 = (v_004 - v_004.rolling(63).mean()) / v_004.rolling(63).std().replace(0, np.nan)
    v_006 = v_005.rolling(21).max() / v_005.rolling(21).min().replace(0, np.nan)
    v_007 = v_006.rolling(63).max()
    res = v_007.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc141_63d_slope_v141_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc141_63d_slope_v141_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc142_252d_slope_v142_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(5).max() / v_001.rolling(5).min().replace(0, np.nan)
    v_003 = (v_002 - v_002.rolling(10).mean()) / v_002.rolling(10).std().replace(0, np.nan)
    v_004 = v_003.rolling(10).max()
    v_005 = v_004.rolling(126).max() / v_004.rolling(126).min().replace(0, np.nan)
    v_006 = v_005.rolling(10).max()
    v_007 = v_006.rolling(21).kurt()
    v_008 = v_007.rolling(5).rank(pct=True)
    v_009 = (v_008 - v_008.rolling(126).mean()) / v_008.rolling(126).std().replace(0, np.nan)
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc142_252d_slope_v142_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc142_252d_slope_v142_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc143_42d_slope_v143_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(21).skew()
    v_003 = v_002.rolling(63).max() / v_002.rolling(63).min().replace(0, np.nan)
    v_004 = v_003.rolling(21).std()
    v_005 = v_004.rolling(5).kurt()
    v_006 = v_005.rolling(252).max() / v_005.rolling(252).min().replace(0, np.nan)
    v_007 = v_006.rolling(42).min()
    v_008 = v_007.rolling(5).var()
    v_009 = v_008.rolling(42).std()
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc143_42d_slope_v143_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc143_42d_slope_v143_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc144_252d_slope_v144_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(126).rank(pct=True)
    v_003 = v_002.rolling(63).std()
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.rolling(5).max() / v_004.rolling(5).min().replace(0, np.nan)
    v_006 = v_005.rolling(252).max()
    v_007 = v_006.rolling(5).mean()
    v_008 = v_007.rolling(252).min()
    v_009 = v_008.rolling(252).mean()
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc144_252d_slope_v144_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc144_252d_slope_v144_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc145_42d_slope_v145_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(252).std()
    v_003 = v_002.rolling(252).skew()
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.rolling(126).std()
    v_006 = v_005.rolling(252).max() / v_005.rolling(252).min().replace(0, np.nan)
    v_007 = v_006.rolling(42).max()
    v_008 = v_007.rolling(63).std()
    v_009 = v_008.rolling(252).min()
    res = v_009.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc145_42d_slope_v145_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc145_42d_slope_v145_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc146_10d_slope_v146_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(5).rank(pct=True)
    v_003 = v_002.rolling(252).max() / v_002.rolling(252).min().replace(0, np.nan)
    v_004 = v_003.rolling(5).max() / v_003.rolling(5).min().replace(0, np.nan)
    v_005 = (v_004 - v_004.rolling(252).mean()) / v_004.rolling(252).std().replace(0, np.nan)
    v_006 = v_005.rolling(21).max()
    v_007 = v_006.rolling(63).mean()
    res = v_007.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc146_10d_slope_v146_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc146_10d_slope_v146_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc147_21d_slope_v147_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(252).max() / v_001.rolling(252).min().replace(0, np.nan)
    v_003 = v_002.rolling(5).min()
    v_004 = v_003.rolling(21).kurt()
    v_005 = v_004.rolling(126).min()
    v_006 = v_005.rolling(252).mean()
    v_007 = v_006.rolling(252).max() / v_006.rolling(252).min().replace(0, np.nan)
    v_008 = v_007.rolling(42).rank(pct=True)
    res = v_008.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc147_21d_slope_v147_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc147_21d_slope_v147_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc148_126d_slope_v148_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(21).skew()
    v_003 = v_002.rolling(126).var()
    v_004 = v_003.rolling(10).max()
    v_005 = v_004.rolling(5).std()
    v_006 = v_005.rolling(5).min()
    v_007 = v_006.rolling(63).max() / v_006.rolling(63).min().replace(0, np.nan)
    v_008 = v_007.rolling(21).max()
    v_009 = v_008.rolling(42).kurt()
    res = v_009.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc148_126d_slope_v148_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc148_126d_slope_v148_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc149_42d_slope_v149_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(10).rank(pct=True)
    v_003 = v_002.rolling(10).rank(pct=True)
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.rolling(10).skew()
    v_006 = v_005.rolling(126).kurt()
    v_007 = v_006.rolling(10).skew()
    v_008 = v_007.rolling(252).max()
    v_009 = v_008.rolling(63).var()
    res = v_009.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc149_42d_slope_v149_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc149_42d_slope_v149_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc150_42d_slope_v150_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(5).max() / v_001.rolling(5).min().replace(0, np.nan)
    v_003 = v_002.rolling(63).mean()
    v_004 = v_003.rolling(63).skew()
    v_005 = (v_004 - v_004.rolling(21).mean()) / v_004.rolling(21).std().replace(0, np.nan)
    v_006 = v_005.rolling(5).kurt()
    v_007 = v_006.rolling(42).max()
    v_008 = v_007.rolling(63).kurt()
    res = v_008.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc150_42d_slope_v150_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc150_42d_slope_v150_signal


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
