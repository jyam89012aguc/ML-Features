import pandas as pd
import numpy as np
FEATURE_FUNCTIONS = {}

def f109o_f109_operating_cash_flow_efficiency_momentum_calc001_63d_base_v001_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc001_63d_base_v001_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc001_63d_base_v001_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc002_5d_base_v002_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc002_5d_base_v002_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc002_5d_base_v002_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc003_63d_base_v003_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc003_63d_base_v003_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc003_63d_base_v003_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc004_42d_base_v004_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc004_42d_base_v004_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc004_42d_base_v004_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc005_42d_base_v005_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc005_42d_base_v005_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc005_42d_base_v005_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc006_5d_base_v006_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc006_5d_base_v006_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc006_5d_base_v006_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc007_63d_base_v007_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc007_63d_base_v007_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc007_63d_base_v007_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc008_10d_base_v008_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc008_10d_base_v008_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc008_10d_base_v008_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc009_150d_base_v009_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc009_150d_base_v009_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc009_150d_base_v009_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc010_10d_base_v010_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(10)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc010_10d_base_v010_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc010_10d_base_v010_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc011_150d_base_v011_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc011_150d_base_v011_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc011_150d_base_v011_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc012_10d_base_v012_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(10).mean()) / v_003.rolling(10).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc012_10d_base_v012_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc012_10d_base_v012_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc013_252d_base_v013_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(252).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc013_252d_base_v013_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc013_252d_base_v013_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc014_126d_base_v014_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc014_126d_base_v014_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc014_126d_base_v014_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc015_126d_base_v015_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc015_126d_base_v015_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc015_126d_base_v015_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc016_126d_base_v016_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc016_126d_base_v016_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc016_126d_base_v016_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc017_126d_base_v017_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(126).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc017_126d_base_v017_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc017_126d_base_v017_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc018_200d_base_v018_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc018_200d_base_v018_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc018_200d_base_v018_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc019_150d_base_v019_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc019_150d_base_v019_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc019_150d_base_v019_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc020_63d_base_v020_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc020_63d_base_v020_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc020_63d_base_v020_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc021_150d_base_v021_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc021_150d_base_v021_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc021_150d_base_v021_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc022_84d_base_v022_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc022_84d_base_v022_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc022_84d_base_v022_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc023_63d_base_v023_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc023_63d_base_v023_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc023_63d_base_v023_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc024_42d_base_v024_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc024_42d_base_v024_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc024_42d_base_v024_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc025_150d_base_v025_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc025_150d_base_v025_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc025_150d_base_v025_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc026_126d_base_v026_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc026_126d_base_v026_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc026_126d_base_v026_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc027_42d_base_v027_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc027_42d_base_v027_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc027_42d_base_v027_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc028_10d_base_v028_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc028_10d_base_v028_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc028_10d_base_v028_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc029_42d_base_v029_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc029_42d_base_v029_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc029_42d_base_v029_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc030_105d_base_v030_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc030_105d_base_v030_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc030_105d_base_v030_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc031_200d_base_v031_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc031_200d_base_v031_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc031_200d_base_v031_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc032_21d_base_v032_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc032_21d_base_v032_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc032_21d_base_v032_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc033_252d_base_v033_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(252)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc033_252d_base_v033_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc033_252d_base_v033_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc034_42d_base_v034_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc034_42d_base_v034_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc034_42d_base_v034_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc035_21d_base_v035_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(21)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc035_21d_base_v035_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc035_21d_base_v035_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc036_5d_base_v036_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc036_5d_base_v036_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc036_5d_base_v036_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc037_150d_base_v037_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(150)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc037_150d_base_v037_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc037_150d_base_v037_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc038_63d_base_v038_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc038_63d_base_v038_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc038_63d_base_v038_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc039_42d_base_v039_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(42).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc039_42d_base_v039_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc039_42d_base_v039_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc040_10d_base_v040_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc040_10d_base_v040_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc040_10d_base_v040_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc041_5d_base_v041_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc041_5d_base_v041_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc041_5d_base_v041_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc042_252d_base_v042_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc042_252d_base_v042_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc042_252d_base_v042_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc043_252d_base_v043_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc043_252d_base_v043_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc043_252d_base_v043_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc044_42d_base_v044_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(42).mean()) / v_003.rolling(42).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc044_42d_base_v044_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc044_42d_base_v044_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc045_84d_base_v045_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(84).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc045_84d_base_v045_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc045_84d_base_v045_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc046_200d_base_v046_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(200).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc046_200d_base_v046_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc046_200d_base_v046_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc047_63d_base_v047_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc047_63d_base_v047_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc047_63d_base_v047_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc048_150d_base_v048_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(150).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc048_150d_base_v048_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc048_150d_base_v048_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc049_252d_base_v049_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(252).mean()) / v_003.rolling(252).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc049_252d_base_v049_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc049_252d_base_v049_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc050_105d_base_v050_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc050_105d_base_v050_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc050_105d_base_v050_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc051_5d_base_v051_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc051_5d_base_v051_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc051_5d_base_v051_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc052_200d_base_v052_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc052_200d_base_v052_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc052_200d_base_v052_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc053_150d_base_v053_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(150)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc053_150d_base_v053_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc053_150d_base_v053_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc054_42d_base_v054_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc054_42d_base_v054_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc054_42d_base_v054_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc055_126d_base_v055_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(126).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc055_126d_base_v055_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc055_126d_base_v055_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc056_126d_base_v056_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(126).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc056_126d_base_v056_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc056_126d_base_v056_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc057_10d_base_v057_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc057_10d_base_v057_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc057_10d_base_v057_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc058_21d_base_v058_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc058_21d_base_v058_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc058_21d_base_v058_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc059_10d_base_v059_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc059_10d_base_v059_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc059_10d_base_v059_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc060_21d_base_v060_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc060_21d_base_v060_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc060_21d_base_v060_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc061_105d_base_v061_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc061_105d_base_v061_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc061_105d_base_v061_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc062_150d_base_v062_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(150).mean()) / v_003.rolling(150).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc062_150d_base_v062_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc062_150d_base_v062_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc063_21d_base_v063_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc063_21d_base_v063_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc063_21d_base_v063_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc064_84d_base_v064_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(84).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc064_84d_base_v064_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc064_84d_base_v064_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc065_42d_base_v065_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(42).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc065_42d_base_v065_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc065_42d_base_v065_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc066_21d_base_v066_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc066_21d_base_v066_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc066_21d_base_v066_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc067_63d_base_v067_signal(assets, ncfo):
    v_001 = assets
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(63).mean()) / v_003.rolling(63).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc067_63d_base_v067_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc067_63d_base_v067_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc068_5d_base_v068_signal(ncfo, revenue):
    v_001 = ncfo
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc068_5d_base_v068_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc068_5d_base_v068_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc069_10d_base_v069_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(10)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc069_10d_base_v069_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc069_10d_base_v069_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc070_252d_base_v070_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc070_252d_base_v070_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc070_252d_base_v070_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc071_252d_base_v071_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc071_252d_base_v071_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc071_252d_base_v071_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc072_10d_base_v072_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc072_10d_base_v072_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc072_10d_base_v072_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc073_252d_base_v073_signal(fcf, ncfo):
    v_001 = fcf
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(252)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc073_252d_base_v073_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc073_252d_base_v073_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc074_200d_base_v074_signal(ncfo, netinc):
    v_001 = ncfo
    v_002 = netinc
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(200).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc074_200d_base_v074_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc074_200d_base_v074_signal

def f109o_f109_operating_cash_flow_efficiency_momentum_calc075_10d_base_v075_signal(ebitda, ncfo):
    v_001 = ebitda
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f109o_f109_operating_cash_flow_efficiency_momentum_calc075_10d_base_v075_signal'] = f109o_f109_operating_cash_flow_efficiency_momentum_calc075_10d_base_v075_signal


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
