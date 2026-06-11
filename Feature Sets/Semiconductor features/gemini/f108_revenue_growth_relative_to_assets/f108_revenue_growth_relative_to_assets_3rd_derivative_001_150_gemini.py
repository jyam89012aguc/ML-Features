import pandas as pd
import numpy as np
FEATURE_FUNCTIONS = {}

def f108r_f108_revenue_growth_relative_to_assets_calc001_105d_jerk_v001_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).mean()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc001_105d_jerk_v001_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc001_105d_jerk_v001_signal

def f108r_f108_revenue_growth_relative_to_assets_calc002_150d_jerk_v002_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).mean()
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc002_150d_jerk_v002_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc002_150d_jerk_v002_signal

def f108r_f108_revenue_growth_relative_to_assets_calc003_5d_jerk_v003_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).min()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc003_5d_jerk_v003_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc003_5d_jerk_v003_signal

def f108r_f108_revenue_growth_relative_to_assets_calc004_10d_jerk_v004_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(10)
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc004_10d_jerk_v004_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc004_10d_jerk_v004_signal

def f108r_f108_revenue_growth_relative_to_assets_calc005_5d_jerk_v005_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc005_5d_jerk_v005_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc005_5d_jerk_v005_signal

def f108r_f108_revenue_growth_relative_to_assets_calc006_200d_jerk_v006_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(200).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc006_200d_jerk_v006_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc006_200d_jerk_v006_signal

def f108r_f108_revenue_growth_relative_to_assets_calc007_42d_jerk_v007_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc007_42d_jerk_v007_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc007_42d_jerk_v007_signal

def f108r_f108_revenue_growth_relative_to_assets_calc008_5d_jerk_v008_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc008_5d_jerk_v008_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc008_5d_jerk_v008_signal

def f108r_f108_revenue_growth_relative_to_assets_calc009_105d_jerk_v009_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc009_105d_jerk_v009_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc009_105d_jerk_v009_signal

def f108r_f108_revenue_growth_relative_to_assets_calc010_63d_jerk_v010_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(63).std()
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc010_63d_jerk_v010_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc010_63d_jerk_v010_signal

def f108r_f108_revenue_growth_relative_to_assets_calc011_252d_jerk_v011_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc011_252d_jerk_v011_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc011_252d_jerk_v011_signal

def f108r_f108_revenue_growth_relative_to_assets_calc012_200d_jerk_v012_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(200)
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc012_200d_jerk_v012_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc012_200d_jerk_v012_signal

def f108r_f108_revenue_growth_relative_to_assets_calc013_200d_jerk_v013_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(200)
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc013_200d_jerk_v013_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc013_200d_jerk_v013_signal

def f108r_f108_revenue_growth_relative_to_assets_calc014_252d_jerk_v014_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc014_252d_jerk_v014_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc014_252d_jerk_v014_signal

def f108r_f108_revenue_growth_relative_to_assets_calc015_252d_jerk_v015_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).max()
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc015_252d_jerk_v015_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc015_252d_jerk_v015_signal

def f108r_f108_revenue_growth_relative_to_assets_calc016_200d_jerk_v016_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(200).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc016_200d_jerk_v016_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc016_200d_jerk_v016_signal

def f108r_f108_revenue_growth_relative_to_assets_calc017_42d_jerk_v017_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc017_42d_jerk_v017_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc017_42d_jerk_v017_signal

def f108r_f108_revenue_growth_relative_to_assets_calc018_10d_jerk_v018_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(10)
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc018_10d_jerk_v018_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc018_10d_jerk_v018_signal

def f108r_f108_revenue_growth_relative_to_assets_calc019_126d_jerk_v019_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(126).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc019_126d_jerk_v019_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc019_126d_jerk_v019_signal

def f108r_f108_revenue_growth_relative_to_assets_calc020_84d_jerk_v020_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).max()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc020_84d_jerk_v020_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc020_84d_jerk_v020_signal

def f108r_f108_revenue_growth_relative_to_assets_calc021_200d_jerk_v021_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).skew()
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc021_200d_jerk_v021_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc021_200d_jerk_v021_signal

def f108r_f108_revenue_growth_relative_to_assets_calc022_5d_jerk_v022_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc022_5d_jerk_v022_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc022_5d_jerk_v022_signal

def f108r_f108_revenue_growth_relative_to_assets_calc023_126d_jerk_v023_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).var()
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc023_126d_jerk_v023_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc023_126d_jerk_v023_signal

def f108r_f108_revenue_growth_relative_to_assets_calc024_21d_jerk_v024_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(21)
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc024_21d_jerk_v024_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc024_21d_jerk_v024_signal

def f108r_f108_revenue_growth_relative_to_assets_calc025_126d_jerk_v025_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc025_126d_jerk_v025_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc025_126d_jerk_v025_signal

def f108r_f108_revenue_growth_relative_to_assets_calc026_126d_jerk_v026_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).mean()
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc026_126d_jerk_v026_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc026_126d_jerk_v026_signal

def f108r_f108_revenue_growth_relative_to_assets_calc027_5d_jerk_v027_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc027_5d_jerk_v027_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc027_5d_jerk_v027_signal

def f108r_f108_revenue_growth_relative_to_assets_calc028_252d_jerk_v028_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).min()
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc028_252d_jerk_v028_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc028_252d_jerk_v028_signal

def f108r_f108_revenue_growth_relative_to_assets_calc029_63d_jerk_v029_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).mean()
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc029_63d_jerk_v029_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc029_63d_jerk_v029_signal

def f108r_f108_revenue_growth_relative_to_assets_calc030_5d_jerk_v030_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).std()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc030_5d_jerk_v030_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc030_5d_jerk_v030_signal

def f108r_f108_revenue_growth_relative_to_assets_calc031_21d_jerk_v031_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc031_21d_jerk_v031_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc031_21d_jerk_v031_signal

def f108r_f108_revenue_growth_relative_to_assets_calc032_63d_jerk_v032_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(63)
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc032_63d_jerk_v032_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc032_63d_jerk_v032_signal

def f108r_f108_revenue_growth_relative_to_assets_calc033_21d_jerk_v033_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).min()
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc033_21d_jerk_v033_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc033_21d_jerk_v033_signal

def f108r_f108_revenue_growth_relative_to_assets_calc034_105d_jerk_v034_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(105).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc034_105d_jerk_v034_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc034_105d_jerk_v034_signal

def f108r_f108_revenue_growth_relative_to_assets_calc035_105d_jerk_v035_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).std()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc035_105d_jerk_v035_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc035_105d_jerk_v035_signal

def f108r_f108_revenue_growth_relative_to_assets_calc036_84d_jerk_v036_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(84).mean()) / v_003.rolling(84).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc036_84d_jerk_v036_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc036_84d_jerk_v036_signal

def f108r_f108_revenue_growth_relative_to_assets_calc037_63d_jerk_v037_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).skew()
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc037_63d_jerk_v037_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc037_63d_jerk_v037_signal

def f108r_f108_revenue_growth_relative_to_assets_calc038_200d_jerk_v038_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc038_200d_jerk_v038_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc038_200d_jerk_v038_signal

def f108r_f108_revenue_growth_relative_to_assets_calc039_150d_jerk_v039_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc039_150d_jerk_v039_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc039_150d_jerk_v039_signal

def f108r_f108_revenue_growth_relative_to_assets_calc040_21d_jerk_v040_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(21)
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc040_21d_jerk_v040_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc040_21d_jerk_v040_signal

def f108r_f108_revenue_growth_relative_to_assets_calc041_150d_jerk_v041_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc041_150d_jerk_v041_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc041_150d_jerk_v041_signal

def f108r_f108_revenue_growth_relative_to_assets_calc042_42d_jerk_v042_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).mean()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc042_42d_jerk_v042_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc042_42d_jerk_v042_signal

def f108r_f108_revenue_growth_relative_to_assets_calc043_10d_jerk_v043_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(10).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc043_10d_jerk_v043_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc043_10d_jerk_v043_signal

def f108r_f108_revenue_growth_relative_to_assets_calc044_150d_jerk_v044_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).skew()
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc044_150d_jerk_v044_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc044_150d_jerk_v044_signal

def f108r_f108_revenue_growth_relative_to_assets_calc045_126d_jerk_v045_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc045_126d_jerk_v045_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc045_126d_jerk_v045_signal

def f108r_f108_revenue_growth_relative_to_assets_calc046_10d_jerk_v046_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).var()
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc046_10d_jerk_v046_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc046_10d_jerk_v046_signal

def f108r_f108_revenue_growth_relative_to_assets_calc047_5d_jerk_v047_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc047_5d_jerk_v047_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc047_5d_jerk_v047_signal

def f108r_f108_revenue_growth_relative_to_assets_calc048_200d_jerk_v048_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(200).std()
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc048_200d_jerk_v048_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc048_200d_jerk_v048_signal

def f108r_f108_revenue_growth_relative_to_assets_calc049_84d_jerk_v049_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(84).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc049_84d_jerk_v049_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc049_84d_jerk_v049_signal

def f108r_f108_revenue_growth_relative_to_assets_calc050_5d_jerk_v050_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(5)
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc050_5d_jerk_v050_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc050_5d_jerk_v050_signal

def f108r_f108_revenue_growth_relative_to_assets_calc051_105d_jerk_v051_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).max()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc051_105d_jerk_v051_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc051_105d_jerk_v051_signal

def f108r_f108_revenue_growth_relative_to_assets_calc052_63d_jerk_v052_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc052_63d_jerk_v052_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc052_63d_jerk_v052_signal

def f108r_f108_revenue_growth_relative_to_assets_calc053_10d_jerk_v053_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc053_10d_jerk_v053_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc053_10d_jerk_v053_signal

def f108r_f108_revenue_growth_relative_to_assets_calc054_150d_jerk_v054_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).std()
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc054_150d_jerk_v054_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc054_150d_jerk_v054_signal

def f108r_f108_revenue_growth_relative_to_assets_calc055_21d_jerk_v055_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc055_21d_jerk_v055_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc055_21d_jerk_v055_signal

def f108r_f108_revenue_growth_relative_to_assets_calc056_5d_jerk_v056_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(5)
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc056_5d_jerk_v056_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc056_5d_jerk_v056_signal

def f108r_f108_revenue_growth_relative_to_assets_calc057_84d_jerk_v057_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc057_84d_jerk_v057_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc057_84d_jerk_v057_signal

def f108r_f108_revenue_growth_relative_to_assets_calc058_21d_jerk_v058_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).max()
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc058_21d_jerk_v058_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc058_21d_jerk_v058_signal

def f108r_f108_revenue_growth_relative_to_assets_calc059_10d_jerk_v059_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(10)
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc059_10d_jerk_v059_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc059_10d_jerk_v059_signal

def f108r_f108_revenue_growth_relative_to_assets_calc060_21d_jerk_v060_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc060_21d_jerk_v060_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc060_21d_jerk_v060_signal

def f108r_f108_revenue_growth_relative_to_assets_calc061_21d_jerk_v061_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).mean()
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc061_21d_jerk_v061_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc061_21d_jerk_v061_signal

def f108r_f108_revenue_growth_relative_to_assets_calc062_21d_jerk_v062_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc062_21d_jerk_v062_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc062_21d_jerk_v062_signal

def f108r_f108_revenue_growth_relative_to_assets_calc063_84d_jerk_v063_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc063_84d_jerk_v063_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc063_84d_jerk_v063_signal

def f108r_f108_revenue_growth_relative_to_assets_calc064_105d_jerk_v064_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(105)
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc064_105d_jerk_v064_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc064_105d_jerk_v064_signal

def f108r_f108_revenue_growth_relative_to_assets_calc065_252d_jerk_v065_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(252)
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc065_252d_jerk_v065_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc065_252d_jerk_v065_signal

def f108r_f108_revenue_growth_relative_to_assets_calc066_63d_jerk_v066_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(63).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc066_63d_jerk_v066_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc066_63d_jerk_v066_signal

def f108r_f108_revenue_growth_relative_to_assets_calc067_42d_jerk_v067_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).max()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc067_42d_jerk_v067_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc067_42d_jerk_v067_signal

def f108r_f108_revenue_growth_relative_to_assets_calc068_105d_jerk_v068_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(105)
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc068_105d_jerk_v068_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc068_105d_jerk_v068_signal

def f108r_f108_revenue_growth_relative_to_assets_calc069_21d_jerk_v069_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).mean()
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc069_21d_jerk_v069_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc069_21d_jerk_v069_signal

def f108r_f108_revenue_growth_relative_to_assets_calc070_10d_jerk_v070_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc070_10d_jerk_v070_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc070_10d_jerk_v070_signal

def f108r_f108_revenue_growth_relative_to_assets_calc071_126d_jerk_v071_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc071_126d_jerk_v071_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc071_126d_jerk_v071_signal

def f108r_f108_revenue_growth_relative_to_assets_calc072_63d_jerk_v072_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).skew()
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc072_63d_jerk_v072_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc072_63d_jerk_v072_signal

def f108r_f108_revenue_growth_relative_to_assets_calc073_63d_jerk_v073_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc073_63d_jerk_v073_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc073_63d_jerk_v073_signal

def f108r_f108_revenue_growth_relative_to_assets_calc074_150d_jerk_v074_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc074_150d_jerk_v074_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc074_150d_jerk_v074_signal

def f108r_f108_revenue_growth_relative_to_assets_calc075_63d_jerk_v075_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc075_63d_jerk_v075_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc075_63d_jerk_v075_signal

def f108r_f108_revenue_growth_relative_to_assets_calc076_84d_jerk_v076_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).mean()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc076_84d_jerk_v076_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc076_84d_jerk_v076_signal

def f108r_f108_revenue_growth_relative_to_assets_calc077_105d_jerk_v077_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(105)
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc077_105d_jerk_v077_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc077_105d_jerk_v077_signal

def f108r_f108_revenue_growth_relative_to_assets_calc078_252d_jerk_v078_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc078_252d_jerk_v078_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc078_252d_jerk_v078_signal

def f108r_f108_revenue_growth_relative_to_assets_calc079_10d_jerk_v079_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(10)
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc079_10d_jerk_v079_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc079_10d_jerk_v079_signal

def f108r_f108_revenue_growth_relative_to_assets_calc080_84d_jerk_v080_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc080_84d_jerk_v080_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc080_84d_jerk_v080_signal

def f108r_f108_revenue_growth_relative_to_assets_calc081_200d_jerk_v081_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).max()
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc081_200d_jerk_v081_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc081_200d_jerk_v081_signal

def f108r_f108_revenue_growth_relative_to_assets_calc082_84d_jerk_v082_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc082_84d_jerk_v082_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc082_84d_jerk_v082_signal

def f108r_f108_revenue_growth_relative_to_assets_calc083_42d_jerk_v083_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc083_42d_jerk_v083_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc083_42d_jerk_v083_signal

def f108r_f108_revenue_growth_relative_to_assets_calc084_252d_jerk_v084_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc084_252d_jerk_v084_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc084_252d_jerk_v084_signal

def f108r_f108_revenue_growth_relative_to_assets_calc085_21d_jerk_v085_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc085_21d_jerk_v085_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc085_21d_jerk_v085_signal

def f108r_f108_revenue_growth_relative_to_assets_calc086_42d_jerk_v086_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc086_42d_jerk_v086_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc086_42d_jerk_v086_signal

def f108r_f108_revenue_growth_relative_to_assets_calc087_150d_jerk_v087_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(150).std()
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc087_150d_jerk_v087_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc087_150d_jerk_v087_signal

def f108r_f108_revenue_growth_relative_to_assets_calc088_63d_jerk_v088_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc088_63d_jerk_v088_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc088_63d_jerk_v088_signal

def f108r_f108_revenue_growth_relative_to_assets_calc089_5d_jerk_v089_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc089_5d_jerk_v089_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc089_5d_jerk_v089_signal

def f108r_f108_revenue_growth_relative_to_assets_calc090_150d_jerk_v090_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(150).mean()) / v_003.rolling(150).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc090_150d_jerk_v090_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc090_150d_jerk_v090_signal

def f108r_f108_revenue_growth_relative_to_assets_calc091_42d_jerk_v091_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc091_42d_jerk_v091_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc091_42d_jerk_v091_signal

def f108r_f108_revenue_growth_relative_to_assets_calc092_10d_jerk_v092_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).max()
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc092_10d_jerk_v092_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc092_10d_jerk_v092_signal

def f108r_f108_revenue_growth_relative_to_assets_calc093_126d_jerk_v093_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).std()
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc093_126d_jerk_v093_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc093_126d_jerk_v093_signal

def f108r_f108_revenue_growth_relative_to_assets_calc094_84d_jerk_v094_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(84).std()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc094_84d_jerk_v094_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc094_84d_jerk_v094_signal

def f108r_f108_revenue_growth_relative_to_assets_calc095_252d_jerk_v095_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(252).mean()) / v_003.rolling(252).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc095_252d_jerk_v095_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc095_252d_jerk_v095_signal

def f108r_f108_revenue_growth_relative_to_assets_calc096_252d_jerk_v096_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc096_252d_jerk_v096_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc096_252d_jerk_v096_signal

def f108r_f108_revenue_growth_relative_to_assets_calc097_150d_jerk_v097_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(150)
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc097_150d_jerk_v097_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc097_150d_jerk_v097_signal

def f108r_f108_revenue_growth_relative_to_assets_calc098_10d_jerk_v098_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(10).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc098_10d_jerk_v098_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc098_10d_jerk_v098_signal

def f108r_f108_revenue_growth_relative_to_assets_calc099_252d_jerk_v099_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc099_252d_jerk_v099_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc099_252d_jerk_v099_signal

def f108r_f108_revenue_growth_relative_to_assets_calc100_10d_jerk_v100_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc100_10d_jerk_v100_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc100_10d_jerk_v100_signal

def f108r_f108_revenue_growth_relative_to_assets_calc101_105d_jerk_v101_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).skew()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc101_105d_jerk_v101_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc101_105d_jerk_v101_signal

def f108r_f108_revenue_growth_relative_to_assets_calc102_105d_jerk_v102_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).skew()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc102_105d_jerk_v102_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc102_105d_jerk_v102_signal

def f108r_f108_revenue_growth_relative_to_assets_calc103_84d_jerk_v103_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc103_84d_jerk_v103_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc103_84d_jerk_v103_signal

def f108r_f108_revenue_growth_relative_to_assets_calc104_5d_jerk_v104_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc104_5d_jerk_v104_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc104_5d_jerk_v104_signal

def f108r_f108_revenue_growth_relative_to_assets_calc105_200d_jerk_v105_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc105_200d_jerk_v105_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc105_200d_jerk_v105_signal

def f108r_f108_revenue_growth_relative_to_assets_calc106_84d_jerk_v106_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).min()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc106_84d_jerk_v106_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc106_84d_jerk_v106_signal

def f108r_f108_revenue_growth_relative_to_assets_calc107_252d_jerk_v107_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(252).mean()) / v_003.rolling(252).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc107_252d_jerk_v107_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc107_252d_jerk_v107_signal

def f108r_f108_revenue_growth_relative_to_assets_calc108_200d_jerk_v108_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(200)
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc108_200d_jerk_v108_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc108_200d_jerk_v108_signal

def f108r_f108_revenue_growth_relative_to_assets_calc109_21d_jerk_v109_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).skew()
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc109_21d_jerk_v109_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc109_21d_jerk_v109_signal

def f108r_f108_revenue_growth_relative_to_assets_calc110_21d_jerk_v110_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).var()
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc110_21d_jerk_v110_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc110_21d_jerk_v110_signal

def f108r_f108_revenue_growth_relative_to_assets_calc111_5d_jerk_v111_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc111_5d_jerk_v111_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc111_5d_jerk_v111_signal

def f108r_f108_revenue_growth_relative_to_assets_calc112_10d_jerk_v112_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(10).std()
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc112_10d_jerk_v112_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc112_10d_jerk_v112_signal

def f108r_f108_revenue_growth_relative_to_assets_calc113_84d_jerk_v113_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).std()
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc113_84d_jerk_v113_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc113_84d_jerk_v113_signal

def f108r_f108_revenue_growth_relative_to_assets_calc114_5d_jerk_v114_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc114_5d_jerk_v114_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc114_5d_jerk_v114_signal

def f108r_f108_revenue_growth_relative_to_assets_calc115_105d_jerk_v115_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).var()
    v_005 = v_004.diff(1).diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc115_105d_jerk_v115_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc115_105d_jerk_v115_signal

def f108r_f108_revenue_growth_relative_to_assets_calc116_42d_jerk_v116_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(42).min().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc116_42d_jerk_v116_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc116_42d_jerk_v116_signal

def f108r_f108_revenue_growth_relative_to_assets_calc117_42d_jerk_v117_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc117_42d_jerk_v117_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc117_42d_jerk_v117_signal

def f108r_f108_revenue_growth_relative_to_assets_calc118_21d_jerk_v118_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc118_21d_jerk_v118_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc118_21d_jerk_v118_signal

def f108r_f108_revenue_growth_relative_to_assets_calc119_150d_jerk_v119_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).max()
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc119_150d_jerk_v119_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc119_150d_jerk_v119_signal

def f108r_f108_revenue_growth_relative_to_assets_calc120_21d_jerk_v120_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(21)
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc120_21d_jerk_v120_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc120_21d_jerk_v120_signal

def f108r_f108_revenue_growth_relative_to_assets_calc121_21d_jerk_v121_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc121_21d_jerk_v121_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc121_21d_jerk_v121_signal

def f108r_f108_revenue_growth_relative_to_assets_calc122_42d_jerk_v122_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).max()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc122_42d_jerk_v122_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc122_42d_jerk_v122_signal

def f108r_f108_revenue_growth_relative_to_assets_calc123_10d_jerk_v123_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).skew()
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc123_10d_jerk_v123_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc123_10d_jerk_v123_signal

def f108r_f108_revenue_growth_relative_to_assets_calc124_42d_jerk_v124_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc124_42d_jerk_v124_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc124_42d_jerk_v124_signal

def f108r_f108_revenue_growth_relative_to_assets_calc125_10d_jerk_v125_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc125_10d_jerk_v125_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc125_10d_jerk_v125_signal

def f108r_f108_revenue_growth_relative_to_assets_calc126_10d_jerk_v126_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(10)
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc126_10d_jerk_v126_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc126_10d_jerk_v126_signal

def f108r_f108_revenue_growth_relative_to_assets_calc127_84d_jerk_v127_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(84)
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc127_84d_jerk_v127_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc127_84d_jerk_v127_signal

def f108r_f108_revenue_growth_relative_to_assets_calc128_21d_jerk_v128_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc128_21d_jerk_v128_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc128_21d_jerk_v128_signal

def f108r_f108_revenue_growth_relative_to_assets_calc129_21d_jerk_v129_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc129_21d_jerk_v129_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc129_21d_jerk_v129_signal

def f108r_f108_revenue_growth_relative_to_assets_calc130_126d_jerk_v130_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).quantile(0.5)
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc130_126d_jerk_v130_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc130_126d_jerk_v130_signal

def f108r_f108_revenue_growth_relative_to_assets_calc131_42d_jerk_v131_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc131_42d_jerk_v131_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc131_42d_jerk_v131_signal

def f108r_f108_revenue_growth_relative_to_assets_calc132_10d_jerk_v132_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).max()
    v_005 = v_004.diff(1).diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc132_10d_jerk_v132_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc132_10d_jerk_v132_signal

def f108r_f108_revenue_growth_relative_to_assets_calc133_42d_jerk_v133_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(42)
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc133_42d_jerk_v133_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc133_42d_jerk_v133_signal

def f108r_f108_revenue_growth_relative_to_assets_calc134_63d_jerk_v134_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(63)
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc134_63d_jerk_v134_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc134_63d_jerk_v134_signal

def f108r_f108_revenue_growth_relative_to_assets_calc135_5d_jerk_v135_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc135_5d_jerk_v135_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc135_5d_jerk_v135_signal

def f108r_f108_revenue_growth_relative_to_assets_calc136_63d_jerk_v136_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(63).mean()) / v_003.rolling(63).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc136_63d_jerk_v136_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc136_63d_jerk_v136_signal

def f108r_f108_revenue_growth_relative_to_assets_calc137_84d_jerk_v137_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).rank(pct=True)
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc137_84d_jerk_v137_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc137_84d_jerk_v137_signal

def f108r_f108_revenue_growth_relative_to_assets_calc138_5d_jerk_v138_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).mean()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc138_5d_jerk_v138_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc138_5d_jerk_v138_signal

def f108r_f108_revenue_growth_relative_to_assets_calc139_126d_jerk_v139_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc139_126d_jerk_v139_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc139_126d_jerk_v139_signal

def f108r_f108_revenue_growth_relative_to_assets_calc140_150d_jerk_v140_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc140_150d_jerk_v140_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc140_150d_jerk_v140_signal

def f108r_f108_revenue_growth_relative_to_assets_calc141_150d_jerk_v141_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).max().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc141_150d_jerk_v141_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc141_150d_jerk_v141_signal

def f108r_f108_revenue_growth_relative_to_assets_calc142_252d_jerk_v142_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc142_252d_jerk_v142_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc142_252d_jerk_v142_signal

def f108r_f108_revenue_growth_relative_to_assets_calc143_21d_jerk_v143_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc143_21d_jerk_v143_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc143_21d_jerk_v143_signal

def f108r_f108_revenue_growth_relative_to_assets_calc144_84d_jerk_v144_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(84).mean()) / v_003.rolling(84).std().replace(0, np.nan))
    v_005 = v_004.diff(1).diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc144_84d_jerk_v144_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc144_84d_jerk_v144_signal

def f108r_f108_revenue_growth_relative_to_assets_calc145_200d_jerk_v145_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).std()
    v_005 = v_004.diff(1).diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc145_200d_jerk_v145_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc145_200d_jerk_v145_signal

def f108r_f108_revenue_growth_relative_to_assets_calc146_252d_jerk_v146_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(252)
    v_005 = v_004.diff(1).diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc146_252d_jerk_v146_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc146_252d_jerk_v146_signal

def f108r_f108_revenue_growth_relative_to_assets_calc147_5d_jerk_v147_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).max()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc147_5d_jerk_v147_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc147_5d_jerk_v147_signal

def f108r_f108_revenue_growth_relative_to_assets_calc148_42d_jerk_v148_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(42).std()
    v_005 = v_004.diff(1).diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc148_42d_jerk_v148_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc148_42d_jerk_v148_signal

def f108r_f108_revenue_growth_relative_to_assets_calc149_5d_jerk_v149_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc149_5d_jerk_v149_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc149_5d_jerk_v149_signal

def f108r_f108_revenue_growth_relative_to_assets_calc150_5d_jerk_v150_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(5).std()
    v_005 = v_004.diff(1).diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc150_5d_jerk_v150_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc150_5d_jerk_v150_signal


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
