import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f157o_f157_operating_income_to_liabilities_cycles_calc001_252d_base_v001_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(5).std()
    v_003 = v_002.rolling(42).std()
    v_004 = v_003.rolling(252).mean()
    v_005 = v_004.rolling(42).std()
    v_006 = v_005.rolling(5).var()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc001_252d_base_v001_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc001_252d_base_v001_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc002_21d_base_v002_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(42).var()
    v_003 = v_002.rolling(21).rank(pct=True)
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.rolling(63).kurt()
    v_006 = v_005.rolling(126).var()
    v_007 = v_006.rolling(126).max()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc002_21d_base_v002_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc002_21d_base_v002_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc003_42d_base_v003_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(21).std()
    v_003 = v_002.rolling(63).var()
    v_004 = v_003.rolling(63).std()
    v_005 = v_004.rolling(252).mean()
    v_006 = v_005.rolling(21).max() / v_005.rolling(21).min().replace(0, np.nan)
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc003_42d_base_v003_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc003_42d_base_v003_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc004_42d_base_v004_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(21).mean()
    v_003 = v_002.rolling(5).min()
    v_004 = v_003.rolling(42).mean()
    v_005 = v_004.rolling(42).kurt()
    v_006 = v_005.rolling(21).mean()
    v_007 = v_006.rolling(21).std()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc004_42d_base_v004_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc004_42d_base_v004_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc005_10d_base_v005_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(63).max() / v_001.rolling(63).min().replace(0, np.nan)
    v_003 = v_002.rolling(126).kurt()
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.rolling(5).max() / v_004.rolling(5).min().replace(0, np.nan)
    v_006 = v_005.rolling(10).mean()
    v_007 = v_006.rolling(63).skew()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc005_10d_base_v005_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc005_10d_base_v005_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc006_63d_base_v006_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(63).min()
    v_003 = v_002.rolling(21).std()
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.rolling(63).var()
    v_006 = v_005.rolling(21).skew()
    v_007 = v_006.rolling(63).std()
    v_008 = v_007.rolling(21).std()
    v_009 = v_008.rolling(5).min()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc006_63d_base_v006_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc006_63d_base_v006_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc007_10d_base_v007_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(63).var()
    v_003 = v_002.rolling(10).mean()
    v_004 = v_003.rolling(21).min()
    v_005 = v_004.rolling(42).mean()
    v_006 = (v_005 - v_005.rolling(42).mean()) / v_005.rolling(42).std().replace(0, np.nan)
    v_007 = v_006.rolling(252).kurt()
    v_008 = v_007.rolling(10).max()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc007_10d_base_v007_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc007_10d_base_v007_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc008_42d_base_v008_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(42).min()
    v_003 = (v_002 - v_002.rolling(63).mean()) / v_002.rolling(63).std().replace(0, np.nan)
    v_004 = v_003.rolling(126).kurt()
    v_005 = v_004.rolling(5).min()
    v_006 = v_005.rolling(21).min()
    v_007 = v_006.rolling(5).max() / v_006.rolling(5).min().replace(0, np.nan)
    v_008 = v_007.rolling(252).min()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc008_42d_base_v008_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc008_42d_base_v008_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc009_5d_base_v009_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(126).kurt()
    v_003 = v_002.rolling(63).max() / v_002.rolling(63).min().replace(0, np.nan)
    v_004 = v_003.rolling(42).max() / v_003.rolling(42).min().replace(0, np.nan)
    v_005 = v_004.rolling(21).max()
    v_006 = (v_005 - v_005.rolling(42).mean()) / v_005.rolling(42).std().replace(0, np.nan)
    v_007 = v_006.rolling(21).std()
    v_008 = v_007.rolling(63).min()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc009_5d_base_v009_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc009_5d_base_v009_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc010_252d_base_v010_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(42).min()
    v_003 = (v_002 - v_002.rolling(126).mean()) / v_002.rolling(126).std().replace(0, np.nan)
    v_004 = v_003.rolling(21).var()
    v_005 = v_004.rolling(252).max()
    v_006 = v_005.rolling(252).min()
    v_007 = v_006.rolling(63).std()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc010_252d_base_v010_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc010_252d_base_v010_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc011_21d_base_v011_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(10).rank(pct=True)
    v_003 = v_002.rolling(126).rank(pct=True)
    v_004 = v_003.rolling(252).max() / v_003.rolling(252).min().replace(0, np.nan)
    v_005 = v_004.rolling(42).std()
    v_006 = v_005.rolling(252).mean()
    v_007 = v_006.rolling(126).kurt()
    v_008 = (v_007 - v_007.rolling(252).mean()) / v_007.rolling(252).std().replace(0, np.nan)
    v_009 = v_008.rolling(21).std()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc011_21d_base_v011_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc011_21d_base_v011_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc012_5d_base_v012_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(10).std()
    v_003 = v_002.rolling(10).kurt()
    v_004 = (v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan)
    v_005 = (v_004 - v_004.rolling(252).mean()) / v_004.rolling(252).std().replace(0, np.nan)
    v_006 = v_005.rolling(42).max() / v_005.rolling(42).min().replace(0, np.nan)
    v_007 = v_006.rolling(63).var()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc012_5d_base_v012_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc012_5d_base_v012_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc013_42d_base_v013_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(21).rank(pct=True)
    v_003 = v_002.rolling(5).rank(pct=True)
    v_004 = v_003.rolling(252).max() / v_003.rolling(252).min().replace(0, np.nan)
    v_005 = v_004.rolling(126).max() / v_004.rolling(126).min().replace(0, np.nan)
    v_006 = v_005.rolling(10).max()
    v_007 = v_006.rolling(126).skew()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc013_42d_base_v013_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc013_42d_base_v013_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc014_5d_base_v014_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(63).mean()
    v_003 = v_002.rolling(252).max() / v_002.rolling(252).min().replace(0, np.nan)
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.rolling(126).mean()
    v_006 = v_005.rolling(42).kurt()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc014_5d_base_v014_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc014_5d_base_v014_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc015_63d_base_v015_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(126).max()
    v_003 = v_002.rolling(252).min()
    v_004 = v_003.rolling(21).max()
    v_005 = v_004.rolling(5).var()
    v_006 = (v_005 - v_005.rolling(63).mean()) / v_005.rolling(63).std().replace(0, np.nan)
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc015_63d_base_v015_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc015_63d_base_v015_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc016_10d_base_v016_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = (v_001 - v_001.rolling(42).mean()) / v_001.rolling(42).std().replace(0, np.nan)
    v_003 = (v_002 - v_002.rolling(10).mean()) / v_002.rolling(10).std().replace(0, np.nan)
    v_004 = v_003.rolling(10).kurt()
    v_005 = (v_004 - v_004.rolling(21).mean()) / v_004.rolling(21).std().replace(0, np.nan)
    v_006 = v_005.rolling(42).var()
    v_007 = v_006.rolling(252).max() / v_006.rolling(252).min().replace(0, np.nan)
    v_008 = v_007.rolling(5).min()
    v_009 = v_008.rolling(63).var()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc016_10d_base_v016_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc016_10d_base_v016_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc017_42d_base_v017_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(126).var()
    v_003 = (v_002 - v_002.rolling(21).mean()) / v_002.rolling(21).std().replace(0, np.nan)
    v_004 = v_003.rolling(21).rank(pct=True)
    v_005 = v_004.rolling(126).var()
    v_006 = v_005.rolling(252).mean()
    v_007 = v_006.rolling(5).max() / v_006.rolling(5).min().replace(0, np.nan)
    v_008 = v_007.rolling(5).min()
    v_009 = v_008.rolling(126).skew()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc017_42d_base_v017_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc017_42d_base_v017_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc018_252d_base_v018_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(63).kurt()
    v_003 = (v_002 - v_002.rolling(252).mean()) / v_002.rolling(252).std().replace(0, np.nan)
    v_004 = v_003.rolling(42).var()
    v_005 = v_004.rolling(42).skew()
    v_006 = v_005.rolling(21).max() / v_005.rolling(21).min().replace(0, np.nan)
    v_007 = v_006.rolling(252).kurt()
    v_008 = (v_007 - v_007.rolling(21).mean()) / v_007.rolling(21).std().replace(0, np.nan)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc018_252d_base_v018_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc018_252d_base_v018_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc019_21d_base_v019_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(252).std()
    v_003 = v_002.rolling(21).skew()
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.rolling(42).var()
    v_006 = v_005.rolling(252).std()
    v_007 = v_006.rolling(126).mean()
    v_008 = v_007.rolling(252).std()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc019_21d_base_v019_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc019_21d_base_v019_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc020_126d_base_v020_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(42).mean()
    v_003 = v_002.rolling(126).min()
    v_004 = v_003.rolling(126).max()
    v_005 = v_004.rolling(42).mean()
    v_006 = v_005.rolling(252).skew()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc020_126d_base_v020_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc020_126d_base_v020_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc021_21d_base_v021_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(42).skew()
    v_003 = (v_002 - v_002.rolling(126).mean()) / v_002.rolling(126).std().replace(0, np.nan)
    v_004 = v_003.rolling(21).max() / v_003.rolling(21).min().replace(0, np.nan)
    v_005 = v_004.rolling(5).min()
    v_006 = v_005.rolling(10).kurt()
    v_007 = (v_006 - v_006.rolling(63).mean()) / v_006.rolling(63).std().replace(0, np.nan)
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc021_21d_base_v021_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc021_21d_base_v021_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc022_63d_base_v022_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(252).var()
    v_003 = v_002.rolling(21).rank(pct=True)
    v_004 = v_003.rolling(126).rank(pct=True)
    v_005 = v_004.rolling(252).min()
    v_006 = v_005.rolling(252).mean()
    v_007 = v_006.rolling(10).max() / v_006.rolling(10).min().replace(0, np.nan)
    v_008 = v_007.rolling(42).kurt()
    v_009 = v_008.rolling(10).mean()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc022_63d_base_v022_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc022_63d_base_v022_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc023_126d_base_v023_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(63).skew()
    v_003 = v_002.rolling(126).min()
    v_004 = (v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan)
    v_005 = v_004.rolling(10).var()
    v_006 = v_005.rolling(126).max() / v_005.rolling(126).min().replace(0, np.nan)
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc023_126d_base_v023_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc023_126d_base_v023_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc024_5d_base_v024_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(21).min()
    v_003 = v_002.rolling(5).rank(pct=True)
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.rolling(5).min()
    v_006 = v_005.rolling(126).skew()
    v_007 = v_006.rolling(42).max()
    v_008 = v_007.rolling(252).var()
    v_009 = v_008.rolling(5).var()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc024_5d_base_v024_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc024_5d_base_v024_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc025_5d_base_v025_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(126).max() / v_001.rolling(126).min().replace(0, np.nan)
    v_003 = v_002.rolling(42).var()
    v_004 = v_003.rolling(42).rank(pct=True)
    v_005 = (v_004 - v_004.rolling(63).mean()) / v_004.rolling(63).std().replace(0, np.nan)
    v_006 = (v_005 - v_005.rolling(252).mean()) / v_005.rolling(252).std().replace(0, np.nan)
    v_007 = v_006.rolling(126).max() / v_006.rolling(126).min().replace(0, np.nan)
    v_008 = (v_007 - v_007.rolling(42).mean()) / v_007.rolling(42).std().replace(0, np.nan)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc025_5d_base_v025_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc025_5d_base_v025_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc026_21d_base_v026_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(21).max() / v_001.rolling(21).min().replace(0, np.nan)
    v_003 = (v_002 - v_002.rolling(63).mean()) / v_002.rolling(63).std().replace(0, np.nan)
    v_004 = v_003.rolling(10).var()
    v_005 = v_004.rolling(63).mean()
    v_006 = v_005.rolling(5).var()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc026_21d_base_v026_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc026_21d_base_v026_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc027_42d_base_v027_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(126).std()
    v_003 = (v_002 - v_002.rolling(126).mean()) / v_002.rolling(126).std().replace(0, np.nan)
    v_004 = v_003.rolling(126).std()
    v_005 = v_004.rolling(126).std()
    v_006 = v_005.rolling(21).min()
    v_007 = v_006.rolling(5).kurt()
    v_008 = v_007.rolling(5).max()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc027_42d_base_v027_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc027_42d_base_v027_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc028_5d_base_v028_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(63).mean()
    v_003 = v_002.rolling(126).min()
    v_004 = v_003.rolling(5).skew()
    v_005 = v_004.rolling(63).max() / v_004.rolling(63).min().replace(0, np.nan)
    v_006 = v_005.rolling(42).min()
    v_007 = v_006.rolling(42).max() / v_006.rolling(42).min().replace(0, np.nan)
    v_008 = v_007.rolling(10).mean()
    v_009 = v_008.rolling(5).max()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc028_5d_base_v028_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc028_5d_base_v028_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc029_42d_base_v029_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(42).mean()
    v_003 = v_002.rolling(5).rank(pct=True)
    v_004 = v_003.rolling(126).mean()
    v_005 = v_004.rolling(42).max()
    v_006 = v_005.rolling(21).rank(pct=True)
    v_007 = v_006.rolling(21).kurt()
    v_008 = v_007.rolling(10).skew()
    v_009 = v_008.rolling(252).var()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc029_42d_base_v029_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc029_42d_base_v029_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc030_21d_base_v030_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(252).min()
    v_003 = v_002.rolling(63).max() / v_002.rolling(63).min().replace(0, np.nan)
    v_004 = v_003.rolling(42).mean()
    v_005 = v_004.rolling(21).rank(pct=True)
    v_006 = v_005.rolling(252).var()
    v_007 = v_006.rolling(63).rank(pct=True)
    v_008 = v_007.rolling(5).var()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc030_21d_base_v030_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc030_21d_base_v030_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc031_42d_base_v031_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(5).rank(pct=True)
    v_003 = v_002.rolling(21).var()
    v_004 = v_003.rolling(126).rank(pct=True)
    v_005 = v_004.rolling(42).var()
    v_006 = v_005.rolling(42).kurt()
    v_007 = v_006.rolling(42).skew()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc031_42d_base_v031_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc031_42d_base_v031_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc032_63d_base_v032_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(5).rank(pct=True)
    v_003 = v_002.rolling(5).mean()
    v_004 = (v_003 - v_003.rolling(252).mean()) / v_003.rolling(252).std().replace(0, np.nan)
    v_005 = v_004.rolling(10).max() / v_004.rolling(10).min().replace(0, np.nan)
    v_006 = v_005.rolling(126).rank(pct=True)
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc032_63d_base_v032_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc032_63d_base_v032_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc033_126d_base_v033_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(5).std()
    v_003 = (v_002 - v_002.rolling(252).mean()) / v_002.rolling(252).std().replace(0, np.nan)
    v_004 = v_003.rolling(126).var()
    v_005 = v_004.rolling(21).kurt()
    v_006 = v_005.rolling(21).skew()
    v_007 = v_006.rolling(42).kurt()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc033_126d_base_v033_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc033_126d_base_v033_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc034_21d_base_v034_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(5).skew()
    v_003 = v_002.rolling(252).var()
    v_004 = v_003.rolling(42).var()
    v_005 = v_004.rolling(63).max() / v_004.rolling(63).min().replace(0, np.nan)
    v_006 = v_005.rolling(21).skew()
    v_007 = v_006.rolling(126).skew()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc034_21d_base_v034_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc034_21d_base_v034_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc035_126d_base_v035_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(252).skew()
    v_003 = v_002.rolling(21).max() / v_002.rolling(21).min().replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.rolling(63).kurt()
    v_006 = v_005.rolling(42).min()
    v_007 = v_006.rolling(42).kurt()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc035_126d_base_v035_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc035_126d_base_v035_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc036_252d_base_v036_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(5).kurt()
    v_003 = (v_002 - v_002.rolling(10).mean()) / v_002.rolling(10).std().replace(0, np.nan)
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.rolling(21).std()
    v_006 = v_005.rolling(5).rank(pct=True)
    v_007 = v_006.rolling(42).max() / v_006.rolling(42).min().replace(0, np.nan)
    v_008 = v_007.rolling(126).std()
    v_009 = v_008.rolling(126).max() / v_008.rolling(126).min().replace(0, np.nan)
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc036_252d_base_v036_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc036_252d_base_v036_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc037_42d_base_v037_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(10).max()
    v_003 = v_002.rolling(42).var()
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.rolling(63).max() / v_004.rolling(63).min().replace(0, np.nan)
    v_006 = v_005.rolling(42).min()
    v_007 = v_006.rolling(252).kurt()
    v_008 = v_007.rolling(252).std()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc037_42d_base_v037_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc037_42d_base_v037_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc038_10d_base_v038_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(5).kurt()
    v_003 = v_002.rolling(21).max()
    v_004 = v_003.rolling(126).var()
    v_005 = (v_004 - v_004.rolling(126).mean()) / v_004.rolling(126).std().replace(0, np.nan)
    v_006 = v_005.rolling(42).rank(pct=True)
    v_007 = v_006.rolling(126).max()
    v_008 = v_007.rolling(5).max()
    v_009 = v_008.rolling(42).max() / v_008.rolling(42).min().replace(0, np.nan)
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc038_10d_base_v038_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc038_10d_base_v038_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc039_63d_base_v039_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(126).rank(pct=True)
    v_003 = v_002.rolling(252).max() / v_002.rolling(252).min().replace(0, np.nan)
    v_004 = (v_003 - v_003.rolling(63).mean()) / v_003.rolling(63).std().replace(0, np.nan)
    v_005 = v_004.rolling(21).std()
    v_006 = v_005.rolling(5).min()
    v_007 = v_006.rolling(5).max()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc039_63d_base_v039_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc039_63d_base_v039_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc040_42d_base_v040_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(126).var()
    v_003 = v_002.rolling(252).min()
    v_004 = v_003.rolling(21).max() / v_003.rolling(21).min().replace(0, np.nan)
    v_005 = v_004.rolling(63).max() / v_004.rolling(63).min().replace(0, np.nan)
    v_006 = v_005.rolling(252).kurt()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc040_42d_base_v040_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc040_42d_base_v040_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc041_21d_base_v041_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(5).std()
    v_003 = v_002.rolling(42).kurt()
    v_004 = v_003.rolling(21).max() / v_003.rolling(21).min().replace(0, np.nan)
    v_005 = v_004.rolling(126).min()
    v_006 = v_005.rolling(252).var()
    v_007 = v_006.rolling(63).var()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc041_21d_base_v041_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc041_21d_base_v041_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc042_252d_base_v042_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(5).rank(pct=True)
    v_003 = v_002.rolling(21).min()
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.rolling(5).max()
    v_006 = v_005.rolling(42).skew()
    v_007 = v_006.rolling(5).kurt()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc042_252d_base_v042_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc042_252d_base_v042_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc043_42d_base_v043_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(5)
    v_002 = v_001.rolling(126).min()
    v_003 = v_002.rolling(21).var()
    v_004 = v_003.rolling(252).min()
    v_005 = v_004.rolling(21).min()
    v_006 = v_005.rolling(252).std()
    v_007 = v_006.rolling(5).max() / v_006.rolling(5).min().replace(0, np.nan)
    v_008 = v_007.rolling(10).rank(pct=True)
    v_009 = v_008.rolling(10).skew()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc043_42d_base_v043_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc043_42d_base_v043_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc044_10d_base_v044_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = (v_001 - v_001.rolling(42).mean()) / v_001.rolling(42).std().replace(0, np.nan)
    v_003 = v_002.rolling(126).rank(pct=True)
    v_004 = (v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan)
    v_005 = v_004.rolling(10).max()
    v_006 = v_005.rolling(21).kurt()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc044_10d_base_v044_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc044_10d_base_v044_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc045_252d_base_v045_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(10).kurt()
    v_003 = v_002.rolling(126).rank(pct=True)
    v_004 = v_003.rolling(42).var()
    v_005 = v_004.rolling(5).var()
    v_006 = v_005.rolling(63).var()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc045_252d_base_v045_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc045_252d_base_v045_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc046_5d_base_v046_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(21).skew()
    v_003 = v_002.rolling(5).skew()
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.rolling(126).var()
    v_006 = v_005.rolling(63).min()
    v_007 = v_006.rolling(21).max()
    v_008 = v_007.rolling(42).skew()
    v_009 = v_008.rolling(42).std()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc046_5d_base_v046_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc046_5d_base_v046_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc047_252d_base_v047_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(63).std()
    v_003 = v_002.rolling(63).mean()
    v_004 = v_003.rolling(21).kurt()
    v_005 = v_004.rolling(42).std()
    v_006 = v_005.rolling(42).kurt()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc047_252d_base_v047_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc047_252d_base_v047_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc048_252d_base_v048_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(126).max() / v_001.rolling(126).min().replace(0, np.nan)
    v_003 = (v_002 - v_002.rolling(42).mean()) / v_002.rolling(42).std().replace(0, np.nan)
    v_004 = v_003.rolling(42).mean()
    v_005 = (v_004 - v_004.rolling(63).mean()) / v_004.rolling(63).std().replace(0, np.nan)
    v_006 = (v_005 - v_005.rolling(63).mean()) / v_005.rolling(63).std().replace(0, np.nan)
    v_007 = v_006.rolling(63).mean()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc048_252d_base_v048_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc048_252d_base_v048_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc049_42d_base_v049_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(252).std()
    v_003 = v_002.rolling(252).mean()
    v_004 = v_003.rolling(252).var()
    v_005 = v_004.rolling(63).rank(pct=True)
    v_006 = (v_005 - v_005.rolling(21).mean()) / v_005.rolling(21).std().replace(0, np.nan)
    v_007 = v_006.rolling(126).kurt()
    v_008 = v_007.rolling(10).var()
    v_009 = v_008.rolling(10).rank(pct=True)
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc049_42d_base_v049_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc049_42d_base_v049_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc050_126d_base_v050_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(21).var()
    v_003 = (v_002 - v_002.rolling(10).mean()) / v_002.rolling(10).std().replace(0, np.nan)
    v_004 = v_003.rolling(5).max()
    v_005 = v_004.rolling(21).skew()
    v_006 = v_005.rolling(21).max() / v_005.rolling(21).min().replace(0, np.nan)
    v_007 = v_006.rolling(10).rank(pct=True)
    v_008 = v_007.rolling(5).max()
    v_009 = v_008.rolling(21).kurt()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc050_126d_base_v050_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc050_126d_base_v050_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc051_21d_base_v051_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(10).max()
    v_003 = v_002.rolling(21).var()
    v_004 = v_003.rolling(252).mean()
    v_005 = v_004.rolling(252).mean()
    v_006 = v_005.rolling(252).skew()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc051_21d_base_v051_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc051_21d_base_v051_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc052_10d_base_v052_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(252).var()
    v_003 = v_002.rolling(252).var()
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.rolling(63).min()
    v_006 = v_005.rolling(252).kurt()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc052_10d_base_v052_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc052_10d_base_v052_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc053_5d_base_v053_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = (v_001 - v_001.rolling(21).mean()) / v_001.rolling(21).std().replace(0, np.nan)
    v_003 = v_002.rolling(126).rank(pct=True)
    v_004 = v_003.rolling(126).max() / v_003.rolling(126).min().replace(0, np.nan)
    v_005 = v_004.rolling(252).var()
    v_006 = v_005.rolling(42).max()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc053_5d_base_v053_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc053_5d_base_v053_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc054_126d_base_v054_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(5).rank(pct=True)
    v_003 = (v_002 - v_002.rolling(42).mean()) / v_002.rolling(42).std().replace(0, np.nan)
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.rolling(10).skew()
    v_006 = v_005.rolling(21).var()
    v_007 = v_006.rolling(63).max() / v_006.rolling(63).min().replace(0, np.nan)
    v_008 = v_007.rolling(5).rank(pct=True)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc054_126d_base_v054_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc054_126d_base_v054_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc055_42d_base_v055_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(252).rank(pct=True)
    v_003 = v_002.rolling(42).max()
    v_004 = (v_003 - v_003.rolling(10).mean()) / v_003.rolling(10).std().replace(0, np.nan)
    v_005 = v_004.rolling(42).std()
    v_006 = v_005.rolling(42).std()
    v_007 = v_006.rolling(252).max()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc055_42d_base_v055_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc055_42d_base_v055_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc056_126d_base_v056_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(5).max()
    v_003 = v_002.rolling(21).kurt()
    v_004 = v_003.rolling(42).mean()
    v_005 = v_004.rolling(42).rank(pct=True)
    v_006 = v_005.rolling(42).skew()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc056_126d_base_v056_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc056_126d_base_v056_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc057_5d_base_v057_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan))
    v_002 = v_001.rolling(42).std()
    v_003 = v_002.rolling(252).max()
    v_004 = v_003.rolling(126).max() / v_003.rolling(126).min().replace(0, np.nan)
    v_005 = v_004.rolling(21).mean()
    v_006 = v_005.rolling(252).skew()
    v_007 = v_006.rolling(63).max() / v_006.rolling(63).min().replace(0, np.nan)
    v_008 = v_007.rolling(10).min()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc057_5d_base_v057_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc057_5d_base_v057_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc058_42d_base_v058_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(252).mean()
    v_003 = v_002.rolling(252).std()
    v_004 = (v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan)
    v_005 = v_004.rolling(5).kurt()
    v_006 = v_005.rolling(21).max()
    v_007 = v_006.rolling(126).std()
    v_008 = v_007.rolling(63).rank(pct=True)
    v_009 = v_008.rolling(21).max()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc058_42d_base_v058_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc058_42d_base_v058_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc059_42d_base_v059_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(5).rank(pct=True)
    v_003 = v_002.rolling(252).skew()
    v_004 = v_003.rolling(63).max()
    v_005 = v_004.rolling(10).max() / v_004.rolling(10).min().replace(0, np.nan)
    v_006 = v_005.rolling(126).max() / v_005.rolling(126).min().replace(0, np.nan)
    v_007 = v_006.rolling(63).std()
    v_008 = v_007.rolling(126).kurt()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc059_42d_base_v059_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc059_42d_base_v059_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc060_63d_base_v060_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(5).kurt()
    v_003 = v_002.rolling(42).kurt()
    v_004 = v_003.rolling(63).max() / v_003.rolling(63).min().replace(0, np.nan)
    v_005 = v_004.rolling(42).skew()
    v_006 = v_005.rolling(10).mean()
    v_007 = v_006.rolling(63).min()
    v_008 = v_007.rolling(252).max()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc060_63d_base_v060_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc060_63d_base_v060_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc061_126d_base_v061_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(126).min()
    v_003 = v_002.rolling(126).rank(pct=True)
    v_004 = v_003.rolling(63).std()
    v_005 = (v_004 - v_004.rolling(5).mean()) / v_004.rolling(5).std().replace(0, np.nan)
    v_006 = v_005.rolling(63).mean()
    v_007 = v_006.rolling(10).min()
    v_008 = v_007.rolling(42).mean()
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc061_126d_base_v061_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc061_126d_base_v061_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc062_126d_base_v062_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(5).kurt()
    v_003 = v_002.rolling(10).std()
    v_004 = v_003.rolling(10).var()
    v_005 = v_004.rolling(5).var()
    v_006 = v_005.rolling(126).mean()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc062_126d_base_v062_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc062_126d_base_v062_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc063_5d_base_v063_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = v_001.rolling(42).std()
    v_003 = v_002.rolling(126).var()
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.rolling(10).rank(pct=True)
    v_006 = v_005.rolling(10).max()
    v_007 = v_006.rolling(126).var()
    v_008 = v_007.rolling(10).var()
    v_009 = v_008.rolling(252).max()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc063_5d_base_v063_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc063_5d_base_v063_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc064_5d_base_v064_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(63).rank(pct=True)
    v_003 = v_002.rolling(5).mean()
    v_004 = v_003.rolling(252).min()
    v_005 = v_004.rolling(5).std()
    v_006 = v_005.rolling(21).kurt()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc064_5d_base_v064_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc064_5d_base_v064_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc065_10d_base_v065_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(21).mean()
    v_003 = v_002.rolling(21).mean()
    v_004 = v_003.rolling(42).max() / v_003.rolling(42).min().replace(0, np.nan)
    v_005 = v_004.rolling(252).skew()
    v_006 = v_005.rolling(10).rank(pct=True)
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc065_10d_base_v065_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc065_10d_base_v065_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc066_42d_base_v066_signal(liabilities, opinc):
    v_001 = (liabilities + opinc)
    v_002 = (v_001 - v_001.rolling(10).mean()) / v_001.rolling(10).std().replace(0, np.nan)
    v_003 = v_002.rolling(5).var()
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.rolling(5).mean()
    v_006 = v_005.rolling(42).skew()
    v_007 = v_006.rolling(63).var()
    v_008 = v_007.rolling(63).max() / v_007.rolling(63).min().replace(0, np.nan)
    res = v_008
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc066_42d_base_v066_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc066_42d_base_v066_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc067_42d_base_v067_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan)).pct_change(3)
    v_002 = v_001.rolling(63).rank(pct=True)
    v_003 = v_002.rolling(252).var()
    v_004 = v_003.rolling(126).var()
    v_005 = v_004.rolling(10).var()
    v_006 = v_005.rolling(5).mean()
    v_007 = v_006.rolling(126).min()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc067_42d_base_v067_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc067_42d_base_v067_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc068_126d_base_v068_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(63).mean()
    v_003 = v_002.rolling(126).skew()
    v_004 = v_003.rolling(126).var()
    v_005 = v_004.rolling(126).max() / v_004.rolling(126).min().replace(0, np.nan)
    v_006 = v_005.rolling(252).kurt()
    v_007 = v_006.rolling(126).rank(pct=True)
    v_008 = v_007.rolling(63).skew()
    v_009 = v_008.rolling(63).max() / v_008.rolling(63).min().replace(0, np.nan)
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc068_126d_base_v068_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc068_126d_base_v068_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc069_63d_base_v069_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(63).min()
    v_003 = (v_002 - v_002.rolling(252).mean()) / v_002.rolling(252).std().replace(0, np.nan)
    v_004 = v_003.rolling(63).var()
    v_005 = v_004.rolling(5).skew()
    v_006 = v_005.rolling(10).max()
    res = v_006
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc069_63d_base_v069_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc069_63d_base_v069_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc070_5d_base_v070_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(42).min()
    v_003 = v_002.rolling(252).kurt()
    v_004 = v_003.rolling(63).max()
    v_005 = v_004.rolling(42).mean()
    v_006 = v_005.rolling(5).min()
    v_007 = v_006.rolling(252).var()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc070_5d_base_v070_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc070_5d_base_v070_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc071_126d_base_v071_signal(liabilities, opinc):
    v_001 = (opinc.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(1)
    v_002 = v_001.rolling(252).skew()
    v_003 = v_002.rolling(21).max()
    v_004 = v_003.rolling(21).std()
    v_005 = v_004.rolling(5).kurt()
    v_006 = v_005.rolling(63).kurt()
    v_007 = v_006.rolling(21).rank(pct=True)
    v_008 = v_007.rolling(10).rank(pct=True)
    v_009 = v_008.rolling(252).max() / v_008.rolling(252).min().replace(0, np.nan)
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc071_126d_base_v071_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc071_126d_base_v071_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc072_10d_base_v072_signal(liabilities, opinc):
    v_001 = (opinc + liabilities)
    v_002 = v_001.rolling(5).rank(pct=True)
    v_003 = v_002.rolling(21).min()
    v_004 = v_003.rolling(5).rank(pct=True)
    v_005 = v_004.rolling(21).skew()
    v_006 = v_005.rolling(5).std()
    v_007 = v_006.rolling(10).mean()
    v_008 = v_007.rolling(21).std()
    v_009 = v_008.rolling(42).max() / v_008.rolling(42).min().replace(0, np.nan)
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc072_10d_base_v072_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc072_10d_base_v072_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc073_5d_base_v073_signal(liabilities, opinc):
    v_001 = (opinc - liabilities)
    v_002 = v_001.rolling(63).min()
    v_003 = (v_002 - v_002.rolling(42).mean()) / v_002.rolling(42).std().replace(0, np.nan)
    v_004 = v_003.rolling(252).max()
    v_005 = v_004.rolling(42).max()
    v_006 = v_005.rolling(21).kurt()
    v_007 = v_006.rolling(21).skew()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc073_5d_base_v073_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc073_5d_base_v073_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc074_21d_base_v074_signal(liabilities, opinc):
    v_001 = (liabilities.replace(0, np.nan) / opinc.replace(0, np.nan))
    v_002 = v_001.rolling(42).skew()
    v_003 = (v_002 - v_002.rolling(5).mean()) / v_002.rolling(5).std().replace(0, np.nan)
    v_004 = v_003.rolling(63).max() / v_003.rolling(63).min().replace(0, np.nan)
    v_005 = v_004.rolling(126).min()
    v_006 = v_005.rolling(10).kurt()
    v_007 = v_006.rolling(126).max()
    v_008 = v_007.rolling(21).rank(pct=True)
    v_009 = v_008.rolling(42).min()
    res = v_009
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc074_21d_base_v074_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc074_21d_base_v074_signal

def f157o_f157_operating_income_to_liabilities_cycles_calc075_10d_base_v075_signal(liabilities, opinc):
    v_001 = (liabilities - opinc)
    v_002 = v_001.rolling(63).mean()
    v_003 = v_002.rolling(252).rank(pct=True)
    v_004 = (v_003 - v_003.rolling(63).mean()) / v_003.rolling(63).std().replace(0, np.nan)
    v_005 = v_004.rolling(63).std()
    v_006 = v_005.rolling(5).var()
    v_007 = v_006.rolling(252).skew()
    res = v_007
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f157o_f157_operating_income_to_liabilities_cycles_calc075_10d_base_v075_signal'] = f157o_f157_operating_income_to_liabilities_cycles_calc075_10d_base_v075_signal


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
