import pandas as pd
import numpy as np
FEATURE_FUNCTIONS = {}

def f112r_f112_retained_earnings_turnover_velocity_calc001_84d_base_v001_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc001_84d_base_v001_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc001_84d_base_v001_signal

def f112r_f112_retained_earnings_turnover_velocity_calc002_63d_base_v002_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc002_63d_base_v002_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc002_63d_base_v002_signal

def f112r_f112_retained_earnings_turnover_velocity_calc003_10d_base_v003_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc003_10d_base_v003_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc003_10d_base_v003_signal

def f112r_f112_retained_earnings_turnover_velocity_calc004_84d_base_v004_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc004_84d_base_v004_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc004_84d_base_v004_signal

def f112r_f112_retained_earnings_turnover_velocity_calc005_126d_base_v005_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc005_126d_base_v005_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc005_126d_base_v005_signal

def f112r_f112_retained_earnings_turnover_velocity_calc006_21d_base_v006_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc006_21d_base_v006_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc006_21d_base_v006_signal

def f112r_f112_retained_earnings_turnover_velocity_calc007_21d_base_v007_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc007_21d_base_v007_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc007_21d_base_v007_signal

def f112r_f112_retained_earnings_turnover_velocity_calc008_200d_base_v008_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(200)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc008_200d_base_v008_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc008_200d_base_v008_signal

def f112r_f112_retained_earnings_turnover_velocity_calc009_21d_base_v009_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc009_21d_base_v009_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc009_21d_base_v009_signal

def f112r_f112_retained_earnings_turnover_velocity_calc010_252d_base_v010_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(252)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc010_252d_base_v010_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc010_252d_base_v010_signal

def f112r_f112_retained_earnings_turnover_velocity_calc011_105d_base_v011_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc011_105d_base_v011_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc011_105d_base_v011_signal

def f112r_f112_retained_earnings_turnover_velocity_calc012_105d_base_v012_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc012_105d_base_v012_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc012_105d_base_v012_signal

def f112r_f112_retained_earnings_turnover_velocity_calc013_126d_base_v013_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc013_126d_base_v013_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc013_126d_base_v013_signal

def f112r_f112_retained_earnings_turnover_velocity_calc014_63d_base_v014_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(63).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc014_63d_base_v014_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc014_63d_base_v014_signal

def f112r_f112_retained_earnings_turnover_velocity_calc015_105d_base_v015_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc015_105d_base_v015_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc015_105d_base_v015_signal

def f112r_f112_retained_earnings_turnover_velocity_calc016_63d_base_v016_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc016_63d_base_v016_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc016_63d_base_v016_signal

def f112r_f112_retained_earnings_turnover_velocity_calc017_150d_base_v017_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc017_150d_base_v017_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc017_150d_base_v017_signal

def f112r_f112_retained_earnings_turnover_velocity_calc018_105d_base_v018_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc018_105d_base_v018_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc018_105d_base_v018_signal

def f112r_f112_retained_earnings_turnover_velocity_calc019_150d_base_v019_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc019_150d_base_v019_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc019_150d_base_v019_signal

def f112r_f112_retained_earnings_turnover_velocity_calc020_5d_base_v020_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc020_5d_base_v020_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc020_5d_base_v020_signal

def f112r_f112_retained_earnings_turnover_velocity_calc021_42d_base_v021_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc021_42d_base_v021_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc021_42d_base_v021_signal

def f112r_f112_retained_earnings_turnover_velocity_calc022_10d_base_v022_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc022_10d_base_v022_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc022_10d_base_v022_signal

def f112r_f112_retained_earnings_turnover_velocity_calc023_42d_base_v023_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc023_42d_base_v023_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc023_42d_base_v023_signal

def f112r_f112_retained_earnings_turnover_velocity_calc024_5d_base_v024_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc024_5d_base_v024_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc024_5d_base_v024_signal

def f112r_f112_retained_earnings_turnover_velocity_calc025_21d_base_v025_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc025_21d_base_v025_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc025_21d_base_v025_signal

def f112r_f112_retained_earnings_turnover_velocity_calc026_5d_base_v026_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc026_5d_base_v026_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc026_5d_base_v026_signal

def f112r_f112_retained_earnings_turnover_velocity_calc027_126d_base_v027_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc027_126d_base_v027_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc027_126d_base_v027_signal

def f112r_f112_retained_earnings_turnover_velocity_calc028_5d_base_v028_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc028_5d_base_v028_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc028_5d_base_v028_signal

def f112r_f112_retained_earnings_turnover_velocity_calc029_126d_base_v029_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(126)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc029_126d_base_v029_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc029_126d_base_v029_signal

def f112r_f112_retained_earnings_turnover_velocity_calc030_21d_base_v030_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(21).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc030_21d_base_v030_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc030_21d_base_v030_signal

def f112r_f112_retained_earnings_turnover_velocity_calc031_21d_base_v031_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc031_21d_base_v031_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc031_21d_base_v031_signal

def f112r_f112_retained_earnings_turnover_velocity_calc032_252d_base_v032_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc032_252d_base_v032_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc032_252d_base_v032_signal

def f112r_f112_retained_earnings_turnover_velocity_calc033_252d_base_v033_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(252)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc033_252d_base_v033_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc033_252d_base_v033_signal

def f112r_f112_retained_earnings_turnover_velocity_calc034_5d_base_v034_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc034_5d_base_v034_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc034_5d_base_v034_signal

def f112r_f112_retained_earnings_turnover_velocity_calc035_252d_base_v035_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(252)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc035_252d_base_v035_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc035_252d_base_v035_signal

def f112r_f112_retained_earnings_turnover_velocity_calc036_252d_base_v036_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc036_252d_base_v036_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc036_252d_base_v036_signal

def f112r_f112_retained_earnings_turnover_velocity_calc037_150d_base_v037_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc037_150d_base_v037_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc037_150d_base_v037_signal

def f112r_f112_retained_earnings_turnover_velocity_calc038_126d_base_v038_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(126).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc038_126d_base_v038_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc038_126d_base_v038_signal

def f112r_f112_retained_earnings_turnover_velocity_calc039_63d_base_v039_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(63).mean()) / v_003.rolling(63).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc039_63d_base_v039_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc039_63d_base_v039_signal

def f112r_f112_retained_earnings_turnover_velocity_calc040_10d_base_v040_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc040_10d_base_v040_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc040_10d_base_v040_signal

def f112r_f112_retained_earnings_turnover_velocity_calc041_252d_base_v041_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc041_252d_base_v041_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc041_252d_base_v041_signal

def f112r_f112_retained_earnings_turnover_velocity_calc042_84d_base_v042_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(84)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc042_84d_base_v042_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc042_84d_base_v042_signal

def f112r_f112_retained_earnings_turnover_velocity_calc043_126d_base_v043_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc043_126d_base_v043_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc043_126d_base_v043_signal

def f112r_f112_retained_earnings_turnover_velocity_calc044_5d_base_v044_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc044_5d_base_v044_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc044_5d_base_v044_signal

def f112r_f112_retained_earnings_turnover_velocity_calc045_105d_base_v045_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(105)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc045_105d_base_v045_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc045_105d_base_v045_signal

def f112r_f112_retained_earnings_turnover_velocity_calc046_200d_base_v046_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc046_200d_base_v046_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc046_200d_base_v046_signal

def f112r_f112_retained_earnings_turnover_velocity_calc047_10d_base_v047_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc047_10d_base_v047_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc047_10d_base_v047_signal

def f112r_f112_retained_earnings_turnover_velocity_calc048_84d_base_v048_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(84).mean()) / v_003.rolling(84).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc048_84d_base_v048_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc048_84d_base_v048_signal

def f112r_f112_retained_earnings_turnover_velocity_calc049_10d_base_v049_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(10)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc049_10d_base_v049_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc049_10d_base_v049_signal

def f112r_f112_retained_earnings_turnover_velocity_calc050_105d_base_v050_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc050_105d_base_v050_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc050_105d_base_v050_signal

def f112r_f112_retained_earnings_turnover_velocity_calc051_10d_base_v051_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(10)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc051_10d_base_v051_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc051_10d_base_v051_signal

def f112r_f112_retained_earnings_turnover_velocity_calc052_84d_base_v052_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc052_84d_base_v052_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc052_84d_base_v052_signal

def f112r_f112_retained_earnings_turnover_velocity_calc053_21d_base_v053_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc053_21d_base_v053_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc053_21d_base_v053_signal

def f112r_f112_retained_earnings_turnover_velocity_calc054_21d_base_v054_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc054_21d_base_v054_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc054_21d_base_v054_signal

def f112r_f112_retained_earnings_turnover_velocity_calc055_63d_base_v055_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc055_63d_base_v055_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc055_63d_base_v055_signal

def f112r_f112_retained_earnings_turnover_velocity_calc056_150d_base_v056_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc056_150d_base_v056_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc056_150d_base_v056_signal

def f112r_f112_retained_earnings_turnover_velocity_calc057_63d_base_v057_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc057_63d_base_v057_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc057_63d_base_v057_signal

def f112r_f112_retained_earnings_turnover_velocity_calc058_42d_base_v058_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc058_42d_base_v058_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc058_42d_base_v058_signal

def f112r_f112_retained_earnings_turnover_velocity_calc059_252d_base_v059_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc059_252d_base_v059_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc059_252d_base_v059_signal

def f112r_f112_retained_earnings_turnover_velocity_calc060_150d_base_v060_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(150).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc060_150d_base_v060_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc060_150d_base_v060_signal

def f112r_f112_retained_earnings_turnover_velocity_calc061_42d_base_v061_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc061_42d_base_v061_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc061_42d_base_v061_signal

def f112r_f112_retained_earnings_turnover_velocity_calc062_126d_base_v062_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(126).mean()) / v_003.rolling(126).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc062_126d_base_v062_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc062_126d_base_v062_signal

def f112r_f112_retained_earnings_turnover_velocity_calc063_21d_base_v063_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc063_21d_base_v063_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc063_21d_base_v063_signal

def f112r_f112_retained_earnings_turnover_velocity_calc064_42d_base_v064_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(42)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc064_42d_base_v064_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc064_42d_base_v064_signal

def f112r_f112_retained_earnings_turnover_velocity_calc065_252d_base_v065_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc065_252d_base_v065_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc065_252d_base_v065_signal

def f112r_f112_retained_earnings_turnover_velocity_calc066_5d_base_v066_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc066_5d_base_v066_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc066_5d_base_v066_signal

def f112r_f112_retained_earnings_turnover_velocity_calc067_150d_base_v067_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc067_150d_base_v067_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc067_150d_base_v067_signal

def f112r_f112_retained_earnings_turnover_velocity_calc068_200d_base_v068_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc068_200d_base_v068_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc068_200d_base_v068_signal

def f112r_f112_retained_earnings_turnover_velocity_calc069_63d_base_v069_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc069_63d_base_v069_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc069_63d_base_v069_signal

def f112r_f112_retained_earnings_turnover_velocity_calc070_21d_base_v070_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(21)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc070_21d_base_v070_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc070_21d_base_v070_signal

def f112r_f112_retained_earnings_turnover_velocity_calc071_21d_base_v071_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc071_21d_base_v071_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc071_21d_base_v071_signal

def f112r_f112_retained_earnings_turnover_velocity_calc072_150d_base_v072_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc072_150d_base_v072_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc072_150d_base_v072_signal

def f112r_f112_retained_earnings_turnover_velocity_calc073_21d_base_v073_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc073_21d_base_v073_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc073_21d_base_v073_signal

def f112r_f112_retained_earnings_turnover_velocity_calc074_5d_base_v074_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc074_5d_base_v074_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc074_5d_base_v074_signal

def f112r_f112_retained_earnings_turnover_velocity_calc075_105d_base_v075_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc075_105d_base_v075_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc075_105d_base_v075_signal


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
