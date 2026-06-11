import pandas as pd
import numpy as np
FEATURE_FUNCTIONS = {}

def f109o_f109_operating_cash_flow_efficiency_momentum_calc001_63d_slope_v001_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).std()
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc001_63d_slope_v001_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc001_63d_slope_v001_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc002_5d_slope_v002_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc002_5d_slope_v002_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc002_5d_slope_v002_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc003_63d_slope_v003_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc003_63d_slope_v003_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc003_63d_slope_v003_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc004_42d_slope_v004_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc004_42d_slope_v004_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc004_42d_slope_v004_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc005_42d_slope_v005_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc005_42d_slope_v005_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc005_42d_slope_v005_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc006_5d_slope_v006_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).skew()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc006_5d_slope_v006_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc006_5d_slope_v006_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc007_63d_slope_v007_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).mean()
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc007_63d_slope_v007_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc007_63d_slope_v007_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc008_10d_slope_v008_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).quantile(0.5)
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc008_10d_slope_v008_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc008_10d_slope_v008_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc009_150d_slope_v009_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc009_150d_slope_v009_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc009_150d_slope_v009_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc010_10d_slope_v010_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(10)
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc010_10d_slope_v010_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc010_10d_slope_v010_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc011_150d_slope_v011_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).quantile(0.5)
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc011_150d_slope_v011_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc011_150d_slope_v011_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc012_10d_slope_v012_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(10).mean()) / v_003.rolling(10).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc012_10d_slope_v012_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc012_10d_slope_v012_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc013_252d_slope_v013_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(252).std()
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc013_252d_slope_v013_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc013_252d_slope_v013_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc014_126d_slope_v014_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).rank(pct=True)
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc014_126d_slope_v014_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc014_126d_slope_v014_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc015_126d_slope_v015_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc015_126d_slope_v015_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc015_126d_slope_v015_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc016_126d_slope_v016_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).std()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc016_126d_slope_v016_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc016_126d_slope_v016_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc017_126d_slope_v017_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(126).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc017_126d_slope_v017_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc017_126d_slope_v017_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc018_200d_slope_v018_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).skew()
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc018_200d_slope_v018_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc018_200d_slope_v018_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc019_150d_slope_v019_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).var()
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc019_150d_slope_v019_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc019_150d_slope_v019_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc020_63d_slope_v020_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).skew()
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc020_63d_slope_v020_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc020_63d_slope_v020_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc021_150d_slope_v021_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc021_150d_slope_v021_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc021_150d_slope_v021_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc022_84d_slope_v022_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).std()
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc022_84d_slope_v022_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc022_84d_slope_v022_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc023_63d_slope_v023_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).rank(pct=True)
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc023_63d_slope_v023_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc023_63d_slope_v023_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc024_42d_slope_v024_signal(ncfo, netinc):
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
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc024_42d_slope_v024_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc024_42d_slope_v024_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc025_150d_slope_v025_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).std()
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc025_150d_slope_v025_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc025_150d_slope_v025_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc026_126d_slope_v026_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc026_126d_slope_v026_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc026_126d_slope_v026_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc027_42d_slope_v027_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).max()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc027_42d_slope_v027_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc027_42d_slope_v027_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc028_10d_slope_v028_signal(ncfo, netinc):
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
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc028_10d_slope_v028_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc028_10d_slope_v028_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc029_42d_slope_v029_signal(ncfo, netinc):
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
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc029_42d_slope_v029_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc029_42d_slope_v029_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc030_105d_slope_v030_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).mean()
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc030_105d_slope_v030_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc030_105d_slope_v030_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc031_200d_slope_v031_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).min()
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc031_200d_slope_v031_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc031_200d_slope_v031_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc032_21d_slope_v032_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc032_21d_slope_v032_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc032_21d_slope_v032_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc033_252d_slope_v033_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(252)
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc033_252d_slope_v033_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc033_252d_slope_v033_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc034_42d_slope_v034_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).max()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc034_42d_slope_v034_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc034_42d_slope_v034_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc035_21d_slope_v035_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(21)
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc035_21d_slope_v035_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc035_21d_slope_v035_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc036_5d_slope_v036_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(5)
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc036_5d_slope_v036_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc036_5d_slope_v036_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc037_150d_slope_v037_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(150)
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc037_150d_slope_v037_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc037_150d_slope_v037_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc038_63d_slope_v038_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).rank(pct=True)
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc038_63d_slope_v038_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc038_63d_slope_v038_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc039_42d_slope_v039_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(42).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc039_42d_slope_v039_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc039_42d_slope_v039_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc040_10d_slope_v040_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).std()
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc040_10d_slope_v040_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc040_10d_slope_v040_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc041_5d_slope_v041_signal(ncfo, netinc):
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
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc041_5d_slope_v041_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc041_5d_slope_v041_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc042_252d_slope_v042_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc042_252d_slope_v042_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc042_252d_slope_v042_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc043_252d_slope_v043_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc043_252d_slope_v043_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc043_252d_slope_v043_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc044_42d_slope_v044_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc044_42d_slope_v044_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc044_42d_slope_v044_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc045_84d_slope_v045_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(84).std()
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc045_84d_slope_v045_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc045_84d_slope_v045_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc046_200d_slope_v046_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(200).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc046_200d_slope_v046_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc046_200d_slope_v046_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc047_63d_slope_v047_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc047_63d_slope_v047_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc047_63d_slope_v047_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc048_150d_slope_v048_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(150).std()
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc048_150d_slope_v048_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc048_150d_slope_v048_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc049_252d_slope_v049_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(252).mean()) / v_003.rolling(252).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc049_252d_slope_v049_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc049_252d_slope_v049_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc050_105d_slope_v050_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).quantile(0.5)
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc050_105d_slope_v050_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc050_105d_slope_v050_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc051_5d_slope_v051_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).rank(pct=True)
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc051_5d_slope_v051_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc051_5d_slope_v051_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc052_200d_slope_v052_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).skew()
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc052_200d_slope_v052_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc052_200d_slope_v052_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc053_150d_slope_v053_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(150)
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc053_150d_slope_v053_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc053_150d_slope_v053_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc054_42d_slope_v054_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).quantile(0.5)
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc054_42d_slope_v054_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc054_42d_slope_v054_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc055_126d_slope_v055_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(126).std()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc055_126d_slope_v055_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc055_126d_slope_v055_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc056_126d_slope_v056_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(126).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc056_126d_slope_v056_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc056_126d_slope_v056_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc057_10d_slope_v057_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).skew()
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc057_10d_slope_v057_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc057_10d_slope_v057_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc058_21d_slope_v058_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).min()
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc058_21d_slope_v058_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc058_21d_slope_v058_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc059_10d_slope_v059_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).max()
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc059_10d_slope_v059_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc059_10d_slope_v059_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc060_21d_slope_v060_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc060_21d_slope_v060_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc060_21d_slope_v060_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc061_105d_slope_v061_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).max()
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc061_105d_slope_v061_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc061_105d_slope_v061_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc062_150d_slope_v062_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(150).mean()) / v_003.rolling(150).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc062_150d_slope_v062_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc062_150d_slope_v062_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc063_21d_slope_v063_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc063_21d_slope_v063_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc063_21d_slope_v063_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc064_84d_slope_v064_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(84).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc064_84d_slope_v064_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc064_84d_slope_v064_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc065_42d_slope_v065_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(42).std()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc065_42d_slope_v065_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc065_42d_slope_v065_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc066_21d_slope_v066_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc066_21d_slope_v066_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc066_21d_slope_v066_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc067_63d_slope_v067_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(63).mean()) / v_003.rolling(63).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc067_63d_slope_v067_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc067_63d_slope_v067_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc068_5d_slope_v068_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc068_5d_slope_v068_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc068_5d_slope_v068_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc069_10d_slope_v069_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(10)
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc069_10d_slope_v069_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc069_10d_slope_v069_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc070_252d_slope_v070_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc070_252d_slope_v070_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc070_252d_slope_v070_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc071_252d_slope_v071_signal(ncfo, netinc):
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
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc071_252d_slope_v071_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc071_252d_slope_v071_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc072_10d_slope_v072_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).var()
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc072_10d_slope_v072_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc072_10d_slope_v072_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc073_252d_slope_v073_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(252)
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc073_252d_slope_v073_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc073_252d_slope_v073_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc074_200d_slope_v074_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(200).std()
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc074_200d_slope_v074_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc074_200d_slope_v074_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc075_10d_slope_v075_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).max()
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc075_10d_slope_v075_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc075_10d_slope_v075_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc076_126d_slope_v076_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).rank(pct=True)
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc076_126d_slope_v076_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc076_126d_slope_v076_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc077_126d_slope_v077_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).kurt()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc077_126d_slope_v077_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc077_126d_slope_v077_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc078_42d_slope_v078_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(42).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc078_42d_slope_v078_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc078_42d_slope_v078_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc079_5d_slope_v079_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc079_5d_slope_v079_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc079_5d_slope_v079_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc080_200d_slope_v080_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(200)
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc080_200d_slope_v080_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc080_200d_slope_v080_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc081_10d_slope_v081_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(10).mean()) / v_003.rolling(10).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc081_10d_slope_v081_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc081_10d_slope_v081_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc082_10d_slope_v082_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(10)
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc082_10d_slope_v082_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc082_10d_slope_v082_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc083_84d_slope_v083_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).quantile(0.5)
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc083_84d_slope_v083_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc083_84d_slope_v083_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc084_200d_slope_v084_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(200).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc084_200d_slope_v084_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc084_200d_slope_v084_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc085_5d_slope_v085_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc085_5d_slope_v085_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc085_5d_slope_v085_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc086_126d_slope_v086_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc086_126d_slope_v086_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc086_126d_slope_v086_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc087_126d_slope_v087_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(126)
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc087_126d_slope_v087_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc087_126d_slope_v087_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc088_42d_slope_v088_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(42)
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc088_42d_slope_v088_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc088_42d_slope_v088_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc089_126d_slope_v089_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc089_126d_slope_v089_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc089_126d_slope_v089_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc090_5d_slope_v090_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).min()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc090_5d_slope_v090_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc090_5d_slope_v090_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc091_150d_slope_v091_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).var()
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc091_150d_slope_v091_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc091_150d_slope_v091_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc092_42d_slope_v092_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).max()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc092_42d_slope_v092_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc092_42d_slope_v092_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc093_126d_slope_v093_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(126).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc093_126d_slope_v093_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc093_126d_slope_v093_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc094_5d_slope_v094_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc094_5d_slope_v094_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc094_5d_slope_v094_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc095_200d_slope_v095_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(200).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc095_200d_slope_v095_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc095_200d_slope_v095_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc096_63d_slope_v096_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).quantile(0.5)
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc096_63d_slope_v096_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc096_63d_slope_v096_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc097_63d_slope_v097_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(63).mean()) / v_003.rolling(63).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc097_63d_slope_v097_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc097_63d_slope_v097_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc098_252d_slope_v098_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc098_252d_slope_v098_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc098_252d_slope_v098_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc099_105d_slope_v099_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).mean()
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc099_105d_slope_v099_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc099_105d_slope_v099_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc100_126d_slope_v100_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).quantile(0.5)
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc100_126d_slope_v100_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc100_126d_slope_v100_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc101_105d_slope_v101_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(105)
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc101_105d_slope_v101_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc101_105d_slope_v101_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc102_252d_slope_v102_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).skew()
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc102_252d_slope_v102_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc102_252d_slope_v102_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc103_5d_slope_v103_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(5)
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc103_5d_slope_v103_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc103_5d_slope_v103_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc104_63d_slope_v104_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).max()
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc104_63d_slope_v104_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc104_63d_slope_v104_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc105_10d_slope_v105_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(10).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc105_10d_slope_v105_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc105_10d_slope_v105_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc106_252d_slope_v106_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).quantile(0.5)
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc106_252d_slope_v106_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc106_252d_slope_v106_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc107_63d_slope_v107_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(63).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc107_63d_slope_v107_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc107_63d_slope_v107_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc108_105d_slope_v108_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(105)
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc108_105d_slope_v108_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc108_105d_slope_v108_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc109_5d_slope_v109_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(5).std()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc109_5d_slope_v109_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc109_5d_slope_v109_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc110_150d_slope_v110_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc110_150d_slope_v110_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc110_150d_slope_v110_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc111_42d_slope_v111_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).quantile(0.5)
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc111_42d_slope_v111_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc111_42d_slope_v111_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc112_200d_slope_v112_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(200).std()
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc112_200d_slope_v112_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc112_200d_slope_v112_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc113_5d_slope_v113_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(5)
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc113_5d_slope_v113_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc113_5d_slope_v113_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc114_105d_slope_v114_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).std()
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc114_105d_slope_v114_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc114_105d_slope_v114_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc115_200d_slope_v115_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).quantile(0.5)
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc115_200d_slope_v115_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc115_200d_slope_v115_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc116_63d_slope_v116_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(63)
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc116_63d_slope_v116_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc116_63d_slope_v116_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc117_126d_slope_v117_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(126)
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc117_126d_slope_v117_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc117_126d_slope_v117_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc118_84d_slope_v118_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(84).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc118_84d_slope_v118_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc118_84d_slope_v118_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc119_200d_slope_v119_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(200)
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc119_200d_slope_v119_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc119_200d_slope_v119_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc120_105d_slope_v120_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(105).mean()) / v_003.rolling(105).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc120_105d_slope_v120_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc120_105d_slope_v120_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc121_63d_slope_v121_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(63)
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc121_63d_slope_v121_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc121_63d_slope_v121_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc122_200d_slope_v122_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).kurt()
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc122_200d_slope_v122_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc122_200d_slope_v122_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc123_21d_slope_v123_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc123_21d_slope_v123_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc123_21d_slope_v123_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc124_150d_slope_v124_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).quantile(0.5)
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc124_150d_slope_v124_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc124_150d_slope_v124_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc125_5d_slope_v125_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc125_5d_slope_v125_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc125_5d_slope_v125_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc126_200d_slope_v126_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(200).std()
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc126_200d_slope_v126_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc126_200d_slope_v126_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc127_63d_slope_v127_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(63).std()
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc127_63d_slope_v127_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc127_63d_slope_v127_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc128_150d_slope_v128_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).skew()
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc128_150d_slope_v128_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc128_150d_slope_v128_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc129_252d_slope_v129_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc129_252d_slope_v129_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc129_252d_slope_v129_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc130_150d_slope_v130_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(150).mean()) / v_003.rolling(150).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc130_150d_slope_v130_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc130_150d_slope_v130_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc131_84d_slope_v131_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(84)
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc131_84d_slope_v131_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc131_84d_slope_v131_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc132_5d_slope_v132_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).max()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc132_5d_slope_v132_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc132_5d_slope_v132_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc133_126d_slope_v133_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc133_126d_slope_v133_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc133_126d_slope_v133_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc134_105d_slope_v134_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(105)
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc134_105d_slope_v134_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc134_105d_slope_v134_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc135_42d_slope_v135_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).mean()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc135_42d_slope_v135_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc135_42d_slope_v135_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc136_200d_slope_v136_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).mean()
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc136_200d_slope_v136_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc136_200d_slope_v136_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc137_21d_slope_v137_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).var()
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc137_21d_slope_v137_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc137_21d_slope_v137_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc138_105d_slope_v138_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).kurt()
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc138_105d_slope_v138_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc138_105d_slope_v138_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc139_63d_slope_v139_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).skew()
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc139_63d_slope_v139_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc139_63d_slope_v139_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc140_42d_slope_v140_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).min()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc140_42d_slope_v140_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc140_42d_slope_v140_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc141_150d_slope_v141_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).skew()
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc141_150d_slope_v141_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc141_150d_slope_v141_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc142_5d_slope_v142_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).max()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc142_5d_slope_v142_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc142_5d_slope_v142_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc143_5d_slope_v143_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc143_5d_slope_v143_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc143_5d_slope_v143_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc144_10d_slope_v144_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(10).std()
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc144_10d_slope_v144_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc144_10d_slope_v144_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc145_42d_slope_v145_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc145_42d_slope_v145_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc145_42d_slope_v145_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc146_252d_slope_v146_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).min()
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc146_252d_slope_v146_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc146_252d_slope_v146_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc147_10d_slope_v147_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).min()
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc147_10d_slope_v147_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc147_10d_slope_v147_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc148_150d_slope_v148_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).kurt()
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc148_150d_slope_v148_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc148_150d_slope_v148_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc149_84d_slope_v149_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(84)
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc149_84d_slope_v149_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc149_84d_slope_v149_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc150_21d_slope_v150_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).mean()
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc150_21d_slope_v150_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc150_21d_slope_v150_signal


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
