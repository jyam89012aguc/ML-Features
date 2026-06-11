import pandas as pd
import numpy as np
FEATURE_FUNCTIONS = {}

def f108r_f108_revenue_growth_relative_to_assets_calc001_105d_base_v001_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc001_105d_base_v001_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc001_105d_base_v001_signal

def f108r_f108_revenue_growth_relative_to_assets_calc002_150d_base_v002_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc002_150d_base_v002_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc002_150d_base_v002_signal

def f108r_f108_revenue_growth_relative_to_assets_calc003_5d_base_v003_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc003_5d_base_v003_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc003_5d_base_v003_signal

def f108r_f108_revenue_growth_relative_to_assets_calc004_10d_base_v004_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(10)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc004_10d_base_v004_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc004_10d_base_v004_signal

def f108r_f108_revenue_growth_relative_to_assets_calc005_5d_base_v005_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc005_5d_base_v005_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc005_5d_base_v005_signal

def f108r_f108_revenue_growth_relative_to_assets_calc006_200d_base_v006_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(200).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc006_200d_base_v006_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc006_200d_base_v006_signal

def f108r_f108_revenue_growth_relative_to_assets_calc007_42d_base_v007_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc007_42d_base_v007_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc007_42d_base_v007_signal

def f108r_f108_revenue_growth_relative_to_assets_calc008_5d_base_v008_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc008_5d_base_v008_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc008_5d_base_v008_signal

def f108r_f108_revenue_growth_relative_to_assets_calc009_105d_base_v009_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc009_105d_base_v009_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc009_105d_base_v009_signal

def f108r_f108_revenue_growth_relative_to_assets_calc010_63d_base_v010_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(63).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc010_63d_base_v010_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc010_63d_base_v010_signal

def f108r_f108_revenue_growth_relative_to_assets_calc011_252d_base_v011_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc011_252d_base_v011_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc011_252d_base_v011_signal

def f108r_f108_revenue_growth_relative_to_assets_calc012_200d_base_v012_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(200)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc012_200d_base_v012_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc012_200d_base_v012_signal

def f108r_f108_revenue_growth_relative_to_assets_calc013_200d_base_v013_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(200)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc013_200d_base_v013_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc013_200d_base_v013_signal

def f108r_f108_revenue_growth_relative_to_assets_calc014_252d_base_v014_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc014_252d_base_v014_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc014_252d_base_v014_signal

def f108r_f108_revenue_growth_relative_to_assets_calc015_252d_base_v015_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc015_252d_base_v015_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc015_252d_base_v015_signal

def f108r_f108_revenue_growth_relative_to_assets_calc016_200d_base_v016_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(200).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc016_200d_base_v016_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc016_200d_base_v016_signal

def f108r_f108_revenue_growth_relative_to_assets_calc017_42d_base_v017_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc017_42d_base_v017_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc017_42d_base_v017_signal

def f108r_f108_revenue_growth_relative_to_assets_calc018_10d_base_v018_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(10)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc018_10d_base_v018_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc018_10d_base_v018_signal

def f108r_f108_revenue_growth_relative_to_assets_calc019_126d_base_v019_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(126).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc019_126d_base_v019_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc019_126d_base_v019_signal

def f108r_f108_revenue_growth_relative_to_assets_calc020_84d_base_v020_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc020_84d_base_v020_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc020_84d_base_v020_signal

def f108r_f108_revenue_growth_relative_to_assets_calc021_200d_base_v021_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc021_200d_base_v021_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc021_200d_base_v021_signal

def f108r_f108_revenue_growth_relative_to_assets_calc022_5d_base_v022_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc022_5d_base_v022_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc022_5d_base_v022_signal

def f108r_f108_revenue_growth_relative_to_assets_calc023_126d_base_v023_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc023_126d_base_v023_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc023_126d_base_v023_signal

def f108r_f108_revenue_growth_relative_to_assets_calc024_21d_base_v024_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(21)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc024_21d_base_v024_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc024_21d_base_v024_signal

def f108r_f108_revenue_growth_relative_to_assets_calc025_126d_base_v025_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc025_126d_base_v025_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc025_126d_base_v025_signal

def f108r_f108_revenue_growth_relative_to_assets_calc026_126d_base_v026_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc026_126d_base_v026_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc026_126d_base_v026_signal

def f108r_f108_revenue_growth_relative_to_assets_calc027_5d_base_v027_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc027_5d_base_v027_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc027_5d_base_v027_signal

def f108r_f108_revenue_growth_relative_to_assets_calc028_252d_base_v028_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc028_252d_base_v028_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc028_252d_base_v028_signal

def f108r_f108_revenue_growth_relative_to_assets_calc029_63d_base_v029_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc029_63d_base_v029_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc029_63d_base_v029_signal

def f108r_f108_revenue_growth_relative_to_assets_calc030_5d_base_v030_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc030_5d_base_v030_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc030_5d_base_v030_signal

def f108r_f108_revenue_growth_relative_to_assets_calc031_21d_base_v031_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc031_21d_base_v031_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc031_21d_base_v031_signal

def f108r_f108_revenue_growth_relative_to_assets_calc032_63d_base_v032_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(63)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc032_63d_base_v032_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc032_63d_base_v032_signal

def f108r_f108_revenue_growth_relative_to_assets_calc033_21d_base_v033_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc033_21d_base_v033_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc033_21d_base_v033_signal

def f108r_f108_revenue_growth_relative_to_assets_calc034_105d_base_v034_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(105).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc034_105d_base_v034_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc034_105d_base_v034_signal

def f108r_f108_revenue_growth_relative_to_assets_calc035_105d_base_v035_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc035_105d_base_v035_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc035_105d_base_v035_signal

def f108r_f108_revenue_growth_relative_to_assets_calc036_84d_base_v036_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(84).mean()) / v_003.rolling(84).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc036_84d_base_v036_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc036_84d_base_v036_signal

def f108r_f108_revenue_growth_relative_to_assets_calc037_63d_base_v037_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc037_63d_base_v037_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc037_63d_base_v037_signal

def f108r_f108_revenue_growth_relative_to_assets_calc038_200d_base_v038_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc038_200d_base_v038_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc038_200d_base_v038_signal

def f108r_f108_revenue_growth_relative_to_assets_calc039_150d_base_v039_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc039_150d_base_v039_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc039_150d_base_v039_signal

def f108r_f108_revenue_growth_relative_to_assets_calc040_21d_base_v040_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(21)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc040_21d_base_v040_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc040_21d_base_v040_signal

def f108r_f108_revenue_growth_relative_to_assets_calc041_150d_base_v041_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc041_150d_base_v041_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc041_150d_base_v041_signal

def f108r_f108_revenue_growth_relative_to_assets_calc042_42d_base_v042_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc042_42d_base_v042_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc042_42d_base_v042_signal

def f108r_f108_revenue_growth_relative_to_assets_calc043_10d_base_v043_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(10).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc043_10d_base_v043_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc043_10d_base_v043_signal

def f108r_f108_revenue_growth_relative_to_assets_calc044_150d_base_v044_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc044_150d_base_v044_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc044_150d_base_v044_signal

def f108r_f108_revenue_growth_relative_to_assets_calc045_126d_base_v045_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc045_126d_base_v045_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc045_126d_base_v045_signal

def f108r_f108_revenue_growth_relative_to_assets_calc046_10d_base_v046_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc046_10d_base_v046_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc046_10d_base_v046_signal

def f108r_f108_revenue_growth_relative_to_assets_calc047_5d_base_v047_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc047_5d_base_v047_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc047_5d_base_v047_signal

def f108r_f108_revenue_growth_relative_to_assets_calc048_200d_base_v048_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(200).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc048_200d_base_v048_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc048_200d_base_v048_signal

def f108r_f108_revenue_growth_relative_to_assets_calc049_84d_base_v049_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(84).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc049_84d_base_v049_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc049_84d_base_v049_signal

def f108r_f108_revenue_growth_relative_to_assets_calc050_5d_base_v050_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc050_5d_base_v050_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc050_5d_base_v050_signal

def f108r_f108_revenue_growth_relative_to_assets_calc051_105d_base_v051_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc051_105d_base_v051_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc051_105d_base_v051_signal

def f108r_f108_revenue_growth_relative_to_assets_calc052_63d_base_v052_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc052_63d_base_v052_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc052_63d_base_v052_signal

def f108r_f108_revenue_growth_relative_to_assets_calc053_10d_base_v053_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc053_10d_base_v053_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc053_10d_base_v053_signal

def f108r_f108_revenue_growth_relative_to_assets_calc054_150d_base_v054_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc054_150d_base_v054_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc054_150d_base_v054_signal

def f108r_f108_revenue_growth_relative_to_assets_calc055_21d_base_v055_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc055_21d_base_v055_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc055_21d_base_v055_signal

def f108r_f108_revenue_growth_relative_to_assets_calc056_5d_base_v056_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc056_5d_base_v056_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc056_5d_base_v056_signal

def f108r_f108_revenue_growth_relative_to_assets_calc057_84d_base_v057_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc057_84d_base_v057_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc057_84d_base_v057_signal

def f108r_f108_revenue_growth_relative_to_assets_calc058_21d_base_v058_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc058_21d_base_v058_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc058_21d_base_v058_signal

def f108r_f108_revenue_growth_relative_to_assets_calc059_10d_base_v059_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(10)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc059_10d_base_v059_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc059_10d_base_v059_signal

def f108r_f108_revenue_growth_relative_to_assets_calc060_21d_base_v060_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc060_21d_base_v060_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc060_21d_base_v060_signal

def f108r_f108_revenue_growth_relative_to_assets_calc061_21d_base_v061_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc061_21d_base_v061_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc061_21d_base_v061_signal

def f108r_f108_revenue_growth_relative_to_assets_calc062_21d_base_v062_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc062_21d_base_v062_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc062_21d_base_v062_signal

def f108r_f108_revenue_growth_relative_to_assets_calc063_84d_base_v063_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc063_84d_base_v063_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc063_84d_base_v063_signal

def f108r_f108_revenue_growth_relative_to_assets_calc064_105d_base_v064_signal(ebitda, revenue):
    v_001 = ebitda
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(105)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc064_105d_base_v064_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc064_105d_base_v064_signal

def f108r_f108_revenue_growth_relative_to_assets_calc065_252d_base_v065_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(252)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc065_252d_base_v065_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc065_252d_base_v065_signal

def f108r_f108_revenue_growth_relative_to_assets_calc066_63d_base_v066_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(63).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc066_63d_base_v066_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc066_63d_base_v066_signal

def f108r_f108_revenue_growth_relative_to_assets_calc067_42d_base_v067_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc067_42d_base_v067_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc067_42d_base_v067_signal

def f108r_f108_revenue_growth_relative_to_assets_calc068_105d_base_v068_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(105)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc068_105d_base_v068_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc068_105d_base_v068_signal

def f108r_f108_revenue_growth_relative_to_assets_calc069_21d_base_v069_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc069_21d_base_v069_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc069_21d_base_v069_signal

def f108r_f108_revenue_growth_relative_to_assets_calc070_10d_base_v070_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc070_10d_base_v070_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc070_10d_base_v070_signal

def f108r_f108_revenue_growth_relative_to_assets_calc071_126d_base_v071_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc071_126d_base_v071_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc071_126d_base_v071_signal

def f108r_f108_revenue_growth_relative_to_assets_calc072_63d_base_v072_signal(assets, revenue):
    v_001 = assets
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc072_63d_base_v072_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc072_63d_base_v072_signal

def f108r_f108_revenue_growth_relative_to_assets_calc073_63d_base_v073_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc073_63d_base_v073_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc073_63d_base_v073_signal

def f108r_f108_revenue_growth_relative_to_assets_calc074_150d_base_v074_signal(equity, revenue):
    v_001 = equity
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc074_150d_base_v074_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc074_150d_base_v074_signal

def f108r_f108_revenue_growth_relative_to_assets_calc075_63d_base_v075_signal(netinc, revenue):
    v_001 = netinc
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f108r_f108_revenue_growth_relative_to_assets_calc075_63d_base_v075_signal'] = f108r_f108_revenue_growth_relative_to_assets_calc075_63d_base_v075_signal


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
