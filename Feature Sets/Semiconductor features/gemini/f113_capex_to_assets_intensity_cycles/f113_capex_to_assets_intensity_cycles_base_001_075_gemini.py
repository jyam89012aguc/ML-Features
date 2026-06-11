import pandas as pd
import numpy as np
FEATURE_FUNCTIONS = {}

def f113c_f113_capex_to_assets_intensity_cycles_calc001_63d_base_v001_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc001_63d_base_v001_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc001_63d_base_v001_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc002_84d_base_v002_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(84).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc002_84d_base_v002_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc002_84d_base_v002_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc003_150d_base_v003_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc003_150d_base_v003_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc003_150d_base_v003_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc004_200d_base_v004_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc004_200d_base_v004_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc004_200d_base_v004_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc005_5d_base_v005_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc005_5d_base_v005_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc005_5d_base_v005_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc006_150d_base_v006_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc006_150d_base_v006_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc006_150d_base_v006_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc007_105d_base_v007_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(105).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc007_105d_base_v007_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc007_105d_base_v007_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc008_5d_base_v008_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc008_5d_base_v008_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc008_5d_base_v008_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc009_42d_base_v009_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc009_42d_base_v009_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc009_42d_base_v009_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc010_252d_base_v010_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(252)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc010_252d_base_v010_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc010_252d_base_v010_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc011_252d_base_v011_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc011_252d_base_v011_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc011_252d_base_v011_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc012_105d_base_v012_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc012_105d_base_v012_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc012_105d_base_v012_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc013_150d_base_v013_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc013_150d_base_v013_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc013_150d_base_v013_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc014_63d_base_v014_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc014_63d_base_v014_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc014_63d_base_v014_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc015_252d_base_v015_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc015_252d_base_v015_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc015_252d_base_v015_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc016_42d_base_v016_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(42).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc016_42d_base_v016_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc016_42d_base_v016_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc017_105d_base_v017_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc017_105d_base_v017_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc017_105d_base_v017_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc018_63d_base_v018_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc018_63d_base_v018_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc018_63d_base_v018_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc019_105d_base_v019_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).kurt()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc019_105d_base_v019_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc019_105d_base_v019_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc020_252d_base_v020_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc020_252d_base_v020_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc020_252d_base_v020_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc021_5d_base_v021_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc021_5d_base_v021_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc021_5d_base_v021_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc022_126d_base_v022_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc022_126d_base_v022_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc022_126d_base_v022_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc023_10d_base_v023_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc023_10d_base_v023_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc023_10d_base_v023_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc024_105d_base_v024_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(105).mean()) / v_003.rolling(105).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc024_105d_base_v024_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc024_105d_base_v024_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc025_42d_base_v025_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(42)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc025_42d_base_v025_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc025_42d_base_v025_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc026_5d_base_v026_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc026_5d_base_v026_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc026_5d_base_v026_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc027_126d_base_v027_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(126).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc027_126d_base_v027_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc027_126d_base_v027_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc028_84d_base_v028_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc028_84d_base_v028_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc028_84d_base_v028_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc029_5d_base_v029_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc029_5d_base_v029_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc029_5d_base_v029_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc030_42d_base_v030_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(42).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc030_42d_base_v030_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc030_42d_base_v030_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc031_21d_base_v031_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(21)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc031_21d_base_v031_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc031_21d_base_v031_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc032_150d_base_v032_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(150).mean()) / v_003.rolling(150).std().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc032_150d_base_v032_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc032_150d_base_v032_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc033_84d_base_v033_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).min()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc033_84d_base_v033_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc033_84d_base_v033_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc034_105d_base_v034_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc034_105d_base_v034_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc034_105d_base_v034_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc035_84d_base_v035_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(84).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc035_84d_base_v035_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc035_84d_base_v035_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc036_126d_base_v036_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc036_126d_base_v036_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc036_126d_base_v036_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc037_252d_base_v037_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc037_252d_base_v037_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc037_252d_base_v037_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc038_105d_base_v038_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(105).min().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc038_105d_base_v038_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc038_105d_base_v038_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc039_5d_base_v039_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc039_5d_base_v039_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc039_5d_base_v039_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc040_5d_base_v040_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc040_5d_base_v040_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc040_5d_base_v040_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc041_63d_base_v041_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc041_63d_base_v041_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc041_63d_base_v041_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc042_42d_base_v042_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(42).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc042_42d_base_v042_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc042_42d_base_v042_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc043_21d_base_v043_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(21)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc043_21d_base_v043_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc043_21d_base_v043_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc044_150d_base_v044_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc044_150d_base_v044_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc044_150d_base_v044_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc045_200d_base_v045_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc045_200d_base_v045_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc045_200d_base_v045_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc046_252d_base_v046_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc046_252d_base_v046_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc046_252d_base_v046_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc047_5d_base_v047_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc047_5d_base_v047_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc047_5d_base_v047_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc048_84d_base_v048_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(84).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc048_84d_base_v048_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc048_84d_base_v048_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc049_252d_base_v049_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc049_252d_base_v049_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc049_252d_base_v049_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc050_5d_base_v050_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc050_5d_base_v050_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc050_5d_base_v050_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc051_10d_base_v051_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(10)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc051_10d_base_v051_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc051_10d_base_v051_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc052_84d_base_v052_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(84)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc052_84d_base_v052_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc052_84d_base_v052_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc053_150d_base_v053_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc053_150d_base_v053_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc053_150d_base_v053_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc054_105d_base_v054_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(105).max().replace(0, np.nan))
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc054_105d_base_v054_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc054_105d_base_v054_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc055_5d_base_v055_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(5).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc055_5d_base_v055_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc055_5d_base_v055_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc056_63d_base_v056_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(63)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc056_63d_base_v056_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc056_63d_base_v056_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc057_252d_base_v057_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc057_252d_base_v057_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc057_252d_base_v057_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc058_5d_base_v058_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc058_5d_base_v058_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc058_5d_base_v058_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc059_5d_base_v059_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc059_5d_base_v059_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc059_5d_base_v059_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc060_5d_base_v060_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc060_5d_base_v060_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc060_5d_base_v060_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc061_84d_base_v061_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc061_84d_base_v061_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc061_84d_base_v061_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc062_126d_base_v062_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc062_126d_base_v062_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc062_126d_base_v062_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc063_84d_base_v063_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc063_84d_base_v063_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc063_84d_base_v063_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc064_10d_base_v064_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(10).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc064_10d_base_v064_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc064_10d_base_v064_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc065_150d_base_v065_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).skew()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc065_150d_base_v065_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc065_150d_base_v065_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc066_5d_base_v066_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc066_5d_base_v066_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc066_5d_base_v066_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc067_5d_base_v067_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).std()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc067_5d_base_v067_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc067_5d_base_v067_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc068_126d_base_v068_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).rank(pct=True)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc068_126d_base_v068_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc068_126d_base_v068_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc069_150d_base_v069_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc069_150d_base_v069_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc069_150d_base_v069_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc070_126d_base_v070_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).var()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc070_126d_base_v070_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc070_126d_base_v070_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc071_63d_base_v071_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(63)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc071_63d_base_v071_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc071_63d_base_v071_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc072_150d_base_v072_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(150)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc072_150d_base_v072_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc072_150d_base_v072_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc073_200d_base_v073_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).max()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc073_200d_base_v073_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc073_200d_base_v073_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc074_10d_base_v074_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc074_10d_base_v074_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc074_10d_base_v074_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc075_63d_base_v075_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).quantile(0.5)
    v_005 = v_004.replace([np.inf, -np.inf], np.nan)
    v_006 = v_005.ffill()
    v_007 = v_006.fillna(0)
    v_008 = v_007.replace([np.inf, -np.inf], np.nan)
    return v_008
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc075_63d_base_v075_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc075_63d_base_v075_signal


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
