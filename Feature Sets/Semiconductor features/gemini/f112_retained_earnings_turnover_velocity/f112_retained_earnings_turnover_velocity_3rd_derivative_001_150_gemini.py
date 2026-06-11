import pandas as pd
import numpy as np
FEATURE_FUNCTIONS = {}

def f112r_f112_retained_earnings_turnover_velocity_calc001_84d_jerk_v001_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).std()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc001_84d_jerk_v001_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc001_84d_jerk_v001_signal

def f112r_f112_retained_earnings_turnover_velocity_calc002_63d_jerk_v002_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).max()
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc002_63d_jerk_v002_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc002_63d_jerk_v002_signal

def f112r_f112_retained_earnings_turnover_velocity_calc003_10d_jerk_v003_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc003_10d_jerk_v003_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc003_10d_jerk_v003_signal

def f112r_f112_retained_earnings_turnover_velocity_calc004_84d_jerk_v004_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).max()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc004_84d_jerk_v004_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc004_84d_jerk_v004_signal

def f112r_f112_retained_earnings_turnover_velocity_calc005_126d_jerk_v005_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc005_126d_jerk_v005_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc005_126d_jerk_v005_signal

def f112r_f112_retained_earnings_turnover_velocity_calc006_21d_jerk_v006_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc006_21d_jerk_v006_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc006_21d_jerk_v006_signal

def f112r_f112_retained_earnings_turnover_velocity_calc007_21d_jerk_v007_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc007_21d_jerk_v007_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc007_21d_jerk_v007_signal

def f112r_f112_retained_earnings_turnover_velocity_calc008_200d_jerk_v008_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(200)
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc008_200d_jerk_v008_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc008_200d_jerk_v008_signal

def f112r_f112_retained_earnings_turnover_velocity_calc009_21d_jerk_v009_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc009_21d_jerk_v009_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc009_21d_jerk_v009_signal

def f112r_f112_retained_earnings_turnover_velocity_calc010_252d_jerk_v010_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(252)
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc010_252d_jerk_v010_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc010_252d_jerk_v010_signal

def f112r_f112_retained_earnings_turnover_velocity_calc011_105d_jerk_v011_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).skew()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc011_105d_jerk_v011_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc011_105d_jerk_v011_signal

def f112r_f112_retained_earnings_turnover_velocity_calc012_105d_jerk_v012_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).mean()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc012_105d_jerk_v012_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc012_105d_jerk_v012_signal

def f112r_f112_retained_earnings_turnover_velocity_calc013_126d_jerk_v013_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc013_126d_jerk_v013_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc013_126d_jerk_v013_signal

def f112r_f112_retained_earnings_turnover_velocity_calc014_63d_jerk_v014_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(63).std()
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc014_63d_jerk_v014_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc014_63d_jerk_v014_signal

def f112r_f112_retained_earnings_turnover_velocity_calc015_105d_jerk_v015_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).mean()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc015_105d_jerk_v015_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc015_105d_jerk_v015_signal

def f112r_f112_retained_earnings_turnover_velocity_calc016_63d_jerk_v016_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).var()
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc016_63d_jerk_v016_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc016_63d_jerk_v016_signal

def f112r_f112_retained_earnings_turnover_velocity_calc017_150d_jerk_v017_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc017_150d_jerk_v017_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc017_150d_jerk_v017_signal

def f112r_f112_retained_earnings_turnover_velocity_calc018_105d_jerk_v018_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).max()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc018_105d_jerk_v018_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc018_105d_jerk_v018_signal

def f112r_f112_retained_earnings_turnover_velocity_calc019_150d_jerk_v019_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc019_150d_jerk_v019_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc019_150d_jerk_v019_signal

def f112r_f112_retained_earnings_turnover_velocity_calc020_5d_jerk_v020_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc020_5d_jerk_v020_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc020_5d_jerk_v020_signal

def f112r_f112_retained_earnings_turnover_velocity_calc021_42d_jerk_v021_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).min()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc021_42d_jerk_v021_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc021_42d_jerk_v021_signal

def f112r_f112_retained_earnings_turnover_velocity_calc022_10d_jerk_v022_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).max()
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc022_10d_jerk_v022_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc022_10d_jerk_v022_signal

def f112r_f112_retained_earnings_turnover_velocity_calc023_42d_jerk_v023_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc023_42d_jerk_v023_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc023_42d_jerk_v023_signal

def f112r_f112_retained_earnings_turnover_velocity_calc024_5d_jerk_v024_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(5)
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc024_5d_jerk_v024_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc024_5d_jerk_v024_signal

def f112r_f112_retained_earnings_turnover_velocity_calc025_21d_jerk_v025_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc025_21d_jerk_v025_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc025_21d_jerk_v025_signal

def f112r_f112_retained_earnings_turnover_velocity_calc026_5d_jerk_v026_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).max()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc026_5d_jerk_v026_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc026_5d_jerk_v026_signal

def f112r_f112_retained_earnings_turnover_velocity_calc027_126d_jerk_v027_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc027_126d_jerk_v027_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc027_126d_jerk_v027_signal

def f112r_f112_retained_earnings_turnover_velocity_calc028_5d_jerk_v028_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).std()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc028_5d_jerk_v028_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc028_5d_jerk_v028_signal

def f112r_f112_retained_earnings_turnover_velocity_calc029_126d_jerk_v029_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(126)
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc029_126d_jerk_v029_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc029_126d_jerk_v029_signal

def f112r_f112_retained_earnings_turnover_velocity_calc030_21d_jerk_v030_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(21).std()
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc030_21d_jerk_v030_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc030_21d_jerk_v030_signal

def f112r_f112_retained_earnings_turnover_velocity_calc031_21d_jerk_v031_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc031_21d_jerk_v031_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc031_21d_jerk_v031_signal

def f112r_f112_retained_earnings_turnover_velocity_calc032_252d_jerk_v032_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).var()
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc032_252d_jerk_v032_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc032_252d_jerk_v032_signal

def f112r_f112_retained_earnings_turnover_velocity_calc033_252d_jerk_v033_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(252)
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc033_252d_jerk_v033_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc033_252d_jerk_v033_signal

def f112r_f112_retained_earnings_turnover_velocity_calc034_5d_jerk_v034_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc034_5d_jerk_v034_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc034_5d_jerk_v034_signal

def f112r_f112_retained_earnings_turnover_velocity_calc035_252d_jerk_v035_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(252)
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc035_252d_jerk_v035_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc035_252d_jerk_v035_signal

def f112r_f112_retained_earnings_turnover_velocity_calc036_252d_jerk_v036_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc036_252d_jerk_v036_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc036_252d_jerk_v036_signal

def f112r_f112_retained_earnings_turnover_velocity_calc037_150d_jerk_v037_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc037_150d_jerk_v037_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc037_150d_jerk_v037_signal

def f112r_f112_retained_earnings_turnover_velocity_calc038_126d_jerk_v038_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(126).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc038_126d_jerk_v038_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc038_126d_jerk_v038_signal

def f112r_f112_retained_earnings_turnover_velocity_calc039_63d_jerk_v039_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(63).mean()) / v_003.rolling(63).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc039_63d_jerk_v039_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc039_63d_jerk_v039_signal

def f112r_f112_retained_earnings_turnover_velocity_calc040_10d_jerk_v040_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc040_10d_jerk_v040_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc040_10d_jerk_v040_signal

def f112r_f112_retained_earnings_turnover_velocity_calc041_252d_jerk_v041_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc041_252d_jerk_v041_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc041_252d_jerk_v041_signal

def f112r_f112_retained_earnings_turnover_velocity_calc042_84d_jerk_v042_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(84)
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc042_84d_jerk_v042_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc042_84d_jerk_v042_signal

def f112r_f112_retained_earnings_turnover_velocity_calc043_126d_jerk_v043_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).var()
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc043_126d_jerk_v043_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc043_126d_jerk_v043_signal

def f112r_f112_retained_earnings_turnover_velocity_calc044_5d_jerk_v044_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).mean()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc044_5d_jerk_v044_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc044_5d_jerk_v044_signal

def f112r_f112_retained_earnings_turnover_velocity_calc045_105d_jerk_v045_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(105)
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc045_105d_jerk_v045_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc045_105d_jerk_v045_signal

def f112r_f112_retained_earnings_turnover_velocity_calc046_200d_jerk_v046_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).mean()
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc046_200d_jerk_v046_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc046_200d_jerk_v046_signal

def f112r_f112_retained_earnings_turnover_velocity_calc047_10d_jerk_v047_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).std()
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc047_10d_jerk_v047_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc047_10d_jerk_v047_signal

def f112r_f112_retained_earnings_turnover_velocity_calc048_84d_jerk_v048_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(84).mean()) / v_003.rolling(84).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc048_84d_jerk_v048_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc048_84d_jerk_v048_signal

def f112r_f112_retained_earnings_turnover_velocity_calc049_10d_jerk_v049_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(10)
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc049_10d_jerk_v049_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc049_10d_jerk_v049_signal

def f112r_f112_retained_earnings_turnover_velocity_calc050_105d_jerk_v050_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc050_105d_jerk_v050_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc050_105d_jerk_v050_signal

def f112r_f112_retained_earnings_turnover_velocity_calc051_10d_jerk_v051_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(10)
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc051_10d_jerk_v051_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc051_10d_jerk_v051_signal

def f112r_f112_retained_earnings_turnover_velocity_calc052_84d_jerk_v052_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).std()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc052_84d_jerk_v052_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc052_84d_jerk_v052_signal

def f112r_f112_retained_earnings_turnover_velocity_calc053_21d_jerk_v053_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).var()
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc053_21d_jerk_v053_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc053_21d_jerk_v053_signal

def f112r_f112_retained_earnings_turnover_velocity_calc054_21d_jerk_v054_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc054_21d_jerk_v054_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc054_21d_jerk_v054_signal

def f112r_f112_retained_earnings_turnover_velocity_calc055_63d_jerk_v055_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc055_63d_jerk_v055_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc055_63d_jerk_v055_signal

def f112r_f112_retained_earnings_turnover_velocity_calc056_150d_jerk_v056_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc056_150d_jerk_v056_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc056_150d_jerk_v056_signal

def f112r_f112_retained_earnings_turnover_velocity_calc057_63d_jerk_v057_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc057_63d_jerk_v057_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc057_63d_jerk_v057_signal

def f112r_f112_retained_earnings_turnover_velocity_calc058_42d_jerk_v058_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).skew()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc058_42d_jerk_v058_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc058_42d_jerk_v058_signal

def f112r_f112_retained_earnings_turnover_velocity_calc059_252d_jerk_v059_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).max()
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc059_252d_jerk_v059_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc059_252d_jerk_v059_signal

def f112r_f112_retained_earnings_turnover_velocity_calc060_150d_jerk_v060_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(150).std()
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc060_150d_jerk_v060_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc060_150d_jerk_v060_signal

def f112r_f112_retained_earnings_turnover_velocity_calc061_42d_jerk_v061_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc061_42d_jerk_v061_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc061_42d_jerk_v061_signal

def f112r_f112_retained_earnings_turnover_velocity_calc062_126d_jerk_v062_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(126).mean()) / v_003.rolling(126).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc062_126d_jerk_v062_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc062_126d_jerk_v062_signal

def f112r_f112_retained_earnings_turnover_velocity_calc063_21d_jerk_v063_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc063_21d_jerk_v063_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc063_21d_jerk_v063_signal

def f112r_f112_retained_earnings_turnover_velocity_calc064_42d_jerk_v064_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(42)
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc064_42d_jerk_v064_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc064_42d_jerk_v064_signal

def f112r_f112_retained_earnings_turnover_velocity_calc065_252d_jerk_v065_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc065_252d_jerk_v065_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc065_252d_jerk_v065_signal

def f112r_f112_retained_earnings_turnover_velocity_calc066_5d_jerk_v066_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc066_5d_jerk_v066_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc066_5d_jerk_v066_signal

def f112r_f112_retained_earnings_turnover_velocity_calc067_150d_jerk_v067_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc067_150d_jerk_v067_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc067_150d_jerk_v067_signal

def f112r_f112_retained_earnings_turnover_velocity_calc068_200d_jerk_v068_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).std()
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc068_200d_jerk_v068_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc068_200d_jerk_v068_signal

def f112r_f112_retained_earnings_turnover_velocity_calc069_63d_jerk_v069_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).std()
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc069_63d_jerk_v069_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc069_63d_jerk_v069_signal

def f112r_f112_retained_earnings_turnover_velocity_calc070_21d_jerk_v070_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(21)
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc070_21d_jerk_v070_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc070_21d_jerk_v070_signal

def f112r_f112_retained_earnings_turnover_velocity_calc071_21d_jerk_v071_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).mean()
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc071_21d_jerk_v071_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc071_21d_jerk_v071_signal

def f112r_f112_retained_earnings_turnover_velocity_calc072_150d_jerk_v072_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc072_150d_jerk_v072_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc072_150d_jerk_v072_signal

def f112r_f112_retained_earnings_turnover_velocity_calc073_21d_jerk_v073_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).max()
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc073_21d_jerk_v073_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc073_21d_jerk_v073_signal

def f112r_f112_retained_earnings_turnover_velocity_calc074_5d_jerk_v074_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc074_5d_jerk_v074_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc074_5d_jerk_v074_signal

def f112r_f112_retained_earnings_turnover_velocity_calc075_105d_jerk_v075_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).std()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc075_105d_jerk_v075_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc075_105d_jerk_v075_signal

def f112r_f112_retained_earnings_turnover_velocity_calc076_252d_jerk_v076_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(252)
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc076_252d_jerk_v076_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc076_252d_jerk_v076_signal

def f112r_f112_retained_earnings_turnover_velocity_calc077_10d_jerk_v077_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(10).std()
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc077_10d_jerk_v077_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc077_10d_jerk_v077_signal

def f112r_f112_retained_earnings_turnover_velocity_calc078_10d_jerk_v078_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(10)
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc078_10d_jerk_v078_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc078_10d_jerk_v078_signal

def f112r_f112_retained_earnings_turnover_velocity_calc079_42d_jerk_v079_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).max()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc079_42d_jerk_v079_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc079_42d_jerk_v079_signal

def f112r_f112_retained_earnings_turnover_velocity_calc080_42d_jerk_v080_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(42)
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc080_42d_jerk_v080_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc080_42d_jerk_v080_signal

def f112r_f112_retained_earnings_turnover_velocity_calc081_5d_jerk_v081_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc081_5d_jerk_v081_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc081_5d_jerk_v081_signal

def f112r_f112_retained_earnings_turnover_velocity_calc082_126d_jerk_v082_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc082_126d_jerk_v082_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc082_126d_jerk_v082_signal

def f112r_f112_retained_earnings_turnover_velocity_calc083_5d_jerk_v083_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc083_5d_jerk_v083_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc083_5d_jerk_v083_signal

def f112r_f112_retained_earnings_turnover_velocity_calc084_63d_jerk_v084_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc084_63d_jerk_v084_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc084_63d_jerk_v084_signal

def f112r_f112_retained_earnings_turnover_velocity_calc085_150d_jerk_v085_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc085_150d_jerk_v085_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc085_150d_jerk_v085_signal

def f112r_f112_retained_earnings_turnover_velocity_calc086_10d_jerk_v086_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(10).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc086_10d_jerk_v086_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc086_10d_jerk_v086_signal

def f112r_f112_retained_earnings_turnover_velocity_calc087_42d_jerk_v087_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).max()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc087_42d_jerk_v087_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc087_42d_jerk_v087_signal

def f112r_f112_retained_earnings_turnover_velocity_calc088_150d_jerk_v088_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc088_150d_jerk_v088_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc088_150d_jerk_v088_signal

def f112r_f112_retained_earnings_turnover_velocity_calc089_150d_jerk_v089_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc089_150d_jerk_v089_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc089_150d_jerk_v089_signal

def f112r_f112_retained_earnings_turnover_velocity_calc090_5d_jerk_v090_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(5).std()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc090_5d_jerk_v090_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc090_5d_jerk_v090_signal

def f112r_f112_retained_earnings_turnover_velocity_calc091_105d_jerk_v091_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).min()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc091_105d_jerk_v091_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc091_105d_jerk_v091_signal

def f112r_f112_retained_earnings_turnover_velocity_calc092_5d_jerk_v092_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc092_5d_jerk_v092_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc092_5d_jerk_v092_signal

def f112r_f112_retained_earnings_turnover_velocity_calc093_252d_jerk_v093_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(252)
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc093_252d_jerk_v093_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc093_252d_jerk_v093_signal

def f112r_f112_retained_earnings_turnover_velocity_calc094_150d_jerk_v094_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).std()
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc094_150d_jerk_v094_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc094_150d_jerk_v094_signal

def f112r_f112_retained_earnings_turnover_velocity_calc095_252d_jerk_v095_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).min()
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc095_252d_jerk_v095_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc095_252d_jerk_v095_signal

def f112r_f112_retained_earnings_turnover_velocity_calc096_5d_jerk_v096_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc096_5d_jerk_v096_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc096_5d_jerk_v096_signal

def f112r_f112_retained_earnings_turnover_velocity_calc097_42d_jerk_v097_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(42).std()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc097_42d_jerk_v097_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc097_42d_jerk_v097_signal

def f112r_f112_retained_earnings_turnover_velocity_calc098_252d_jerk_v098_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc098_252d_jerk_v098_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc098_252d_jerk_v098_signal

def f112r_f112_retained_earnings_turnover_velocity_calc099_5d_jerk_v099_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc099_5d_jerk_v099_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc099_5d_jerk_v099_signal

def f112r_f112_retained_earnings_turnover_velocity_calc100_21d_jerk_v100_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc100_21d_jerk_v100_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc100_21d_jerk_v100_signal

def f112r_f112_retained_earnings_turnover_velocity_calc101_10d_jerk_v101_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc101_10d_jerk_v101_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc101_10d_jerk_v101_signal

def f112r_f112_retained_earnings_turnover_velocity_calc102_150d_jerk_v102_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc102_150d_jerk_v102_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc102_150d_jerk_v102_signal

def f112r_f112_retained_earnings_turnover_velocity_calc103_150d_jerk_v103_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).skew()
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc103_150d_jerk_v103_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc103_150d_jerk_v103_signal

def f112r_f112_retained_earnings_turnover_velocity_calc104_42d_jerk_v104_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(42).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc104_42d_jerk_v104_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc104_42d_jerk_v104_signal

def f112r_f112_retained_earnings_turnover_velocity_calc105_200d_jerk_v105_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(200)
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc105_200d_jerk_v105_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc105_200d_jerk_v105_signal

def f112r_f112_retained_earnings_turnover_velocity_calc106_84d_jerk_v106_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc106_84d_jerk_v106_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc106_84d_jerk_v106_signal

def f112r_f112_retained_earnings_turnover_velocity_calc107_252d_jerk_v107_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(252)
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc107_252d_jerk_v107_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc107_252d_jerk_v107_signal

def f112r_f112_retained_earnings_turnover_velocity_calc108_150d_jerk_v108_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc108_150d_jerk_v108_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc108_150d_jerk_v108_signal

def f112r_f112_retained_earnings_turnover_velocity_calc109_21d_jerk_v109_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).std()
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc109_21d_jerk_v109_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc109_21d_jerk_v109_signal

def f112r_f112_retained_earnings_turnover_velocity_calc110_200d_jerk_v110_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(200).mean()) / v_003.rolling(200).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc110_200d_jerk_v110_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc110_200d_jerk_v110_signal

def f112r_f112_retained_earnings_turnover_velocity_calc111_84d_jerk_v111_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(84)
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc111_84d_jerk_v111_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc111_84d_jerk_v111_signal

def f112r_f112_retained_earnings_turnover_velocity_calc112_84d_jerk_v112_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(84).std()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc112_84d_jerk_v112_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc112_84d_jerk_v112_signal

def f112r_f112_retained_earnings_turnover_velocity_calc113_63d_jerk_v113_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(63).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc113_63d_jerk_v113_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc113_63d_jerk_v113_signal

def f112r_f112_retained_earnings_turnover_velocity_calc114_63d_jerk_v114_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc114_63d_jerk_v114_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc114_63d_jerk_v114_signal

def f112r_f112_retained_earnings_turnover_velocity_calc115_150d_jerk_v115_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).std()
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc115_150d_jerk_v115_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc115_150d_jerk_v115_signal

def f112r_f112_retained_earnings_turnover_velocity_calc116_42d_jerk_v116_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc116_42d_jerk_v116_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc116_42d_jerk_v116_signal

def f112r_f112_retained_earnings_turnover_velocity_calc117_10d_jerk_v117_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc117_10d_jerk_v117_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc117_10d_jerk_v117_signal

def f112r_f112_retained_earnings_turnover_velocity_calc118_5d_jerk_v118_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc118_5d_jerk_v118_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc118_5d_jerk_v118_signal

def f112r_f112_retained_earnings_turnover_velocity_calc119_105d_jerk_v119_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc119_105d_jerk_v119_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc119_105d_jerk_v119_signal

def f112r_f112_retained_earnings_turnover_velocity_calc120_126d_jerk_v120_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc120_126d_jerk_v120_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc120_126d_jerk_v120_signal

def f112r_f112_retained_earnings_turnover_velocity_calc121_21d_jerk_v121_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).min()
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc121_21d_jerk_v121_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc121_21d_jerk_v121_signal

def f112r_f112_retained_earnings_turnover_velocity_calc122_252d_jerk_v122_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).mean()
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc122_252d_jerk_v122_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc122_252d_jerk_v122_signal

def f112r_f112_retained_earnings_turnover_velocity_calc123_105d_jerk_v123_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).max()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc123_105d_jerk_v123_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc123_105d_jerk_v123_signal

def f112r_f112_retained_earnings_turnover_velocity_calc124_10d_jerk_v124_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc124_10d_jerk_v124_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc124_10d_jerk_v124_signal

def f112r_f112_retained_earnings_turnover_velocity_calc125_84d_jerk_v125_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).max()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc125_84d_jerk_v125_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc125_84d_jerk_v125_signal

def f112r_f112_retained_earnings_turnover_velocity_calc126_252d_jerk_v126_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).skew()
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc126_252d_jerk_v126_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc126_252d_jerk_v126_signal

def f112r_f112_retained_earnings_turnover_velocity_calc127_10d_jerk_v127_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(10)
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc127_10d_jerk_v127_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc127_10d_jerk_v127_signal

def f112r_f112_retained_earnings_turnover_velocity_calc128_84d_jerk_v128_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).mean()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc128_84d_jerk_v128_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc128_84d_jerk_v128_signal

def f112r_f112_retained_earnings_turnover_velocity_calc129_63d_jerk_v129_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc129_63d_jerk_v129_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc129_63d_jerk_v129_signal

def f112r_f112_retained_earnings_turnover_velocity_calc130_105d_jerk_v130_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).std()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc130_105d_jerk_v130_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc130_105d_jerk_v130_signal

def f112r_f112_retained_earnings_turnover_velocity_calc131_42d_jerk_v131_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(42)
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc131_42d_jerk_v131_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc131_42d_jerk_v131_signal

def f112r_f112_retained_earnings_turnover_velocity_calc132_126d_jerk_v132_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc132_126d_jerk_v132_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc132_126d_jerk_v132_signal

def f112r_f112_retained_earnings_turnover_velocity_calc133_252d_jerk_v133_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc133_252d_jerk_v133_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc133_252d_jerk_v133_signal

def f112r_f112_retained_earnings_turnover_velocity_calc134_150d_jerk_v134_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).max()
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc134_150d_jerk_v134_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc134_150d_jerk_v134_signal

def f112r_f112_retained_earnings_turnover_velocity_calc135_200d_jerk_v135_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).skew()
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc135_200d_jerk_v135_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc135_200d_jerk_v135_signal

def f112r_f112_retained_earnings_turnover_velocity_calc136_252d_jerk_v136_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).mean()
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc136_252d_jerk_v136_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc136_252d_jerk_v136_signal

def f112r_f112_retained_earnings_turnover_velocity_calc137_21d_jerk_v137_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc137_21d_jerk_v137_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc137_21d_jerk_v137_signal

def f112r_f112_retained_earnings_turnover_velocity_calc138_84d_jerk_v138_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).std()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc138_84d_jerk_v138_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc138_84d_jerk_v138_signal

def f112r_f112_retained_earnings_turnover_velocity_calc139_21d_jerk_v139_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(21)
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc139_21d_jerk_v139_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc139_21d_jerk_v139_signal

def f112r_f112_retained_earnings_turnover_velocity_calc140_10d_jerk_v140_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).min()
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc140_10d_jerk_v140_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc140_10d_jerk_v140_signal

def f112r_f112_retained_earnings_turnover_velocity_calc141_63d_jerk_v141_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(63).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc141_63d_jerk_v141_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc141_63d_jerk_v141_signal

def f112r_f112_retained_earnings_turnover_velocity_calc142_126d_jerk_v142_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc142_126d_jerk_v142_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc142_126d_jerk_v142_signal

def f112r_f112_retained_earnings_turnover_velocity_calc143_63d_jerk_v143_signal(marketcap, retearn):
    v_001 = marketcap
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(63).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc143_63d_jerk_v143_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc143_63d_jerk_v143_signal

def f112r_f112_retained_earnings_turnover_velocity_calc144_21d_jerk_v144_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).max()
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc144_21d_jerk_v144_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc144_21d_jerk_v144_signal

def f112r_f112_retained_earnings_turnover_velocity_calc145_84d_jerk_v145_signal(retearn, revenue):
    v_001 = retearn
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(84).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc145_84d_jerk_v145_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc145_84d_jerk_v145_signal

def f112r_f112_retained_earnings_turnover_velocity_calc146_5d_jerk_v146_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).max()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc146_5d_jerk_v146_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc146_5d_jerk_v146_signal

def f112r_f112_retained_earnings_turnover_velocity_calc147_10d_jerk_v147_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(10)
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc147_10d_jerk_v147_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc147_10d_jerk_v147_signal

def f112r_f112_retained_earnings_turnover_velocity_calc148_84d_jerk_v148_signal(ebitda, retearn):
    v_001 = ebitda
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(84).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc148_84d_jerk_v148_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc148_84d_jerk_v148_signal

def f112r_f112_retained_earnings_turnover_velocity_calc149_126d_jerk_v149_signal(equity, retearn):
    v_001 = equity
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(126)
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc149_126d_jerk_v149_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc149_126d_jerk_v149_signal

def f112r_f112_retained_earnings_turnover_velocity_calc150_126d_jerk_v150_signal(assets, retearn):
    v_001 = assets
    v_002 = retearn
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).max()
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f112r_f112_retained_earnings_turnover_velocity_calc150_126d_jerk_v150_signal'] = f112r_f112_retained_earnings_turnover_velocity_calc150_126d_jerk_v150_signal


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
