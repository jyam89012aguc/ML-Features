import pandas as pd
import numpy as np
FEATURE_FUNCTIONS = {}

def f113c_f113_capex_to_assets_intensity_cycles_calc001_63d_slope_v001_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc001_63d_slope_v001_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc001_63d_slope_v001_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc002_84d_slope_v002_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(84).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc002_84d_slope_v002_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc002_84d_slope_v002_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc003_150d_slope_v003_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc003_150d_slope_v003_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc003_150d_slope_v003_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc004_200d_slope_v004_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).min()
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc004_200d_slope_v004_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc004_200d_slope_v004_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc005_5d_slope_v005_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).kurt()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc005_5d_slope_v005_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc005_5d_slope_v005_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc006_150d_slope_v006_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc006_150d_slope_v006_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc006_150d_slope_v006_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc007_105d_slope_v007_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(105).std()
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc007_105d_slope_v007_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc007_105d_slope_v007_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc008_5d_slope_v008_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc008_5d_slope_v008_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc008_5d_slope_v008_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc009_42d_slope_v009_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).mean()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc009_42d_slope_v009_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc009_42d_slope_v009_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc010_252d_slope_v010_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(252)
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc010_252d_slope_v010_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc010_252d_slope_v010_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc011_252d_slope_v011_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).mean()
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc011_252d_slope_v011_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc011_252d_slope_v011_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc012_105d_slope_v012_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).std()
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc012_105d_slope_v012_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc012_105d_slope_v012_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc013_150d_slope_v013_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).max()
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc013_150d_slope_v013_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc013_150d_slope_v013_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc014_63d_slope_v014_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc014_63d_slope_v014_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc014_63d_slope_v014_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc015_252d_slope_v015_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc015_252d_slope_v015_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc015_252d_slope_v015_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc016_42d_slope_v016_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(42).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc016_42d_slope_v016_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc016_42d_slope_v016_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc017_105d_slope_v017_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).rank(pct=True)
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc017_105d_slope_v017_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc017_105d_slope_v017_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc018_63d_slope_v018_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).min()
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc018_63d_slope_v018_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc018_63d_slope_v018_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc019_105d_slope_v019_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).kurt()
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc019_105d_slope_v019_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc019_105d_slope_v019_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc020_252d_slope_v020_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).skew()
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc020_252d_slope_v020_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc020_252d_slope_v020_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc021_5d_slope_v021_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).min()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc021_5d_slope_v021_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc021_5d_slope_v021_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc022_126d_slope_v022_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).quantile(0.5)
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc022_126d_slope_v022_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc022_126d_slope_v022_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc023_10d_slope_v023_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).rank(pct=True)
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc023_10d_slope_v023_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc023_10d_slope_v023_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc024_105d_slope_v024_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(105).mean()) / v_003.rolling(105).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc024_105d_slope_v024_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc024_105d_slope_v024_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc025_42d_slope_v025_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(42)
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc025_42d_slope_v025_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc025_42d_slope_v025_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc026_5d_slope_v026_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).var()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc026_5d_slope_v026_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc026_5d_slope_v026_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc027_126d_slope_v027_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(126).std()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc027_126d_slope_v027_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc027_126d_slope_v027_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc028_84d_slope_v028_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).mean()
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc028_84d_slope_v028_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc028_84d_slope_v028_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc029_5d_slope_v029_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).mean()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc029_5d_slope_v029_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc029_5d_slope_v029_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc030_42d_slope_v030_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(42).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc030_42d_slope_v030_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc030_42d_slope_v030_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc031_21d_slope_v031_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(21)
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc031_21d_slope_v031_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc031_21d_slope_v031_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc032_150d_slope_v032_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(150).mean()) / v_003.rolling(150).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc032_150d_slope_v032_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc032_150d_slope_v032_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc033_84d_slope_v033_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).min()
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc033_84d_slope_v033_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc033_84d_slope_v033_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc034_105d_slope_v034_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).quantile(0.5)
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc034_105d_slope_v034_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc034_105d_slope_v034_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc035_84d_slope_v035_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(84).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc035_84d_slope_v035_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc035_84d_slope_v035_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc036_126d_slope_v036_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc036_126d_slope_v036_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc036_126d_slope_v036_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc037_252d_slope_v037_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(252).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc037_252d_slope_v037_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc037_252d_slope_v037_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc038_105d_slope_v038_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(105).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc038_105d_slope_v038_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc038_105d_slope_v038_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc039_5d_slope_v039_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).rank(pct=True)
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc039_5d_slope_v039_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc039_5d_slope_v039_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc040_5d_slope_v040_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(5)
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc040_5d_slope_v040_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc040_5d_slope_v040_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc041_63d_slope_v041_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).quantile(0.5)
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc041_63d_slope_v041_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc041_63d_slope_v041_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc042_42d_slope_v042_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(42).std()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc042_42d_slope_v042_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc042_42d_slope_v042_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc043_21d_slope_v043_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(21)
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc043_21d_slope_v043_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc043_21d_slope_v043_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc044_150d_slope_v044_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).quantile(0.5)
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc044_150d_slope_v044_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc044_150d_slope_v044_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc045_200d_slope_v045_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).skew()
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc045_200d_slope_v045_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc045_200d_slope_v045_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc046_252d_slope_v046_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).quantile(0.5)
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc046_252d_slope_v046_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc046_252d_slope_v046_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc047_5d_slope_v047_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).max()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc047_5d_slope_v047_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc047_5d_slope_v047_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc048_84d_slope_v048_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(84).std()
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc048_84d_slope_v048_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc048_84d_slope_v048_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc049_252d_slope_v049_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).std()
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc049_252d_slope_v049_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc049_252d_slope_v049_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc050_5d_slope_v050_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).skew()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc050_5d_slope_v050_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc050_5d_slope_v050_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc051_10d_slope_v051_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(10)
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc051_10d_slope_v051_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc051_10d_slope_v051_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc052_84d_slope_v052_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(84)
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc052_84d_slope_v052_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc052_84d_slope_v052_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc053_150d_slope_v053_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).std()
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc053_150d_slope_v053_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc053_150d_slope_v053_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc054_105d_slope_v054_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(105).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc054_105d_slope_v054_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc054_105d_slope_v054_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc055_5d_slope_v055_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(5).std()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc055_5d_slope_v055_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc055_5d_slope_v055_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc056_63d_slope_v056_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(63)
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc056_63d_slope_v056_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc056_63d_slope_v056_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc057_252d_slope_v057_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).rank(pct=True)
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc057_252d_slope_v057_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc057_252d_slope_v057_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc058_5d_slope_v058_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).max()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc058_5d_slope_v058_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc058_5d_slope_v058_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc059_5d_slope_v059_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).rank(pct=True)
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc059_5d_slope_v059_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc059_5d_slope_v059_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc060_5d_slope_v060_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).skew()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc060_5d_slope_v060_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc060_5d_slope_v060_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc061_84d_slope_v061_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).quantile(0.5)
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc061_84d_slope_v061_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc061_84d_slope_v061_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc062_126d_slope_v062_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).var()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc062_126d_slope_v062_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc062_126d_slope_v062_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc063_84d_slope_v063_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).skew()
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc063_84d_slope_v063_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc063_84d_slope_v063_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc064_10d_slope_v064_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(10).std()
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc064_10d_slope_v064_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc064_10d_slope_v064_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc065_150d_slope_v065_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).skew()
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc065_150d_slope_v065_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc065_150d_slope_v065_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc066_5d_slope_v066_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).std()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc066_5d_slope_v066_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc066_5d_slope_v066_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc067_5d_slope_v067_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).std()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc067_5d_slope_v067_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc067_5d_slope_v067_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc068_126d_slope_v068_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).rank(pct=True)
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc068_126d_slope_v068_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc068_126d_slope_v068_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc069_150d_slope_v069_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(150)
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc069_150d_slope_v069_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc069_150d_slope_v069_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc070_126d_slope_v070_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).var()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc070_126d_slope_v070_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc070_126d_slope_v070_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc071_63d_slope_v071_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(63)
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc071_63d_slope_v071_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc071_63d_slope_v071_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc072_150d_slope_v072_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(150)
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc072_150d_slope_v072_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc072_150d_slope_v072_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc073_200d_slope_v073_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).max()
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc073_200d_slope_v073_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc073_200d_slope_v073_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc074_10d_slope_v074_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).mean()
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc074_10d_slope_v074_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc074_10d_slope_v074_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc075_63d_slope_v075_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).quantile(0.5)
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc075_63d_slope_v075_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc075_63d_slope_v075_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc076_150d_slope_v076_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc076_150d_slope_v076_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc076_150d_slope_v076_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc077_21d_slope_v077_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).quantile(0.5)
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc077_21d_slope_v077_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc077_21d_slope_v077_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc078_10d_slope_v078_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(10).mean()) / v_003.rolling(10).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc078_10d_slope_v078_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc078_10d_slope_v078_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc079_42d_slope_v079_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).kurt()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc079_42d_slope_v079_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc079_42d_slope_v079_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc080_10d_slope_v080_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(10).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc080_10d_slope_v080_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc080_10d_slope_v080_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc081_21d_slope_v081_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc081_21d_slope_v081_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc081_21d_slope_v081_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc082_126d_slope_v082_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(126).mean()) / v_003.rolling(126).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc082_126d_slope_v082_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc082_126d_slope_v082_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc083_200d_slope_v083_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).kurt()
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc083_200d_slope_v083_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc083_200d_slope_v083_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc084_10d_slope_v084_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).skew()
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc084_10d_slope_v084_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc084_10d_slope_v084_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc085_84d_slope_v085_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(84).mean()) / v_003.rolling(84).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc085_84d_slope_v085_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc085_84d_slope_v085_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc086_252d_slope_v086_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(252)
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc086_252d_slope_v086_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc086_252d_slope_v086_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc087_42d_slope_v087_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(42)
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc087_42d_slope_v087_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc087_42d_slope_v087_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc088_150d_slope_v088_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).kurt()
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc088_150d_slope_v088_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc088_150d_slope_v088_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc089_63d_slope_v089_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(63).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc089_63d_slope_v089_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc089_63d_slope_v089_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc090_10d_slope_v090_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).max()
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc090_10d_slope_v090_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc090_10d_slope_v090_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc091_200d_slope_v091_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).mean()
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc091_200d_slope_v091_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc091_200d_slope_v091_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc092_21d_slope_v092_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(21).mean()) / v_003.rolling(21).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc092_21d_slope_v092_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc092_21d_slope_v092_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc093_5d_slope_v093_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(5).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc093_5d_slope_v093_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc093_5d_slope_v093_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc094_200d_slope_v094_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(200).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc094_200d_slope_v094_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc094_200d_slope_v094_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc095_84d_slope_v095_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(84).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc095_84d_slope_v095_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc095_84d_slope_v095_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc096_150d_slope_v096_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).kurt()
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc096_150d_slope_v096_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc096_150d_slope_v096_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc097_200d_slope_v097_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).quantile(0.5)
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc097_200d_slope_v097_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc097_200d_slope_v097_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc098_42d_slope_v098_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).var()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc098_42d_slope_v098_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc098_42d_slope_v098_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc099_126d_slope_v099_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).quantile(0.5)
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc099_126d_slope_v099_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc099_126d_slope_v099_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc100_10d_slope_v100_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).min()
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc100_10d_slope_v100_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc100_10d_slope_v100_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc101_150d_slope_v101_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(150).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc101_150d_slope_v101_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc101_150d_slope_v101_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc102_84d_slope_v102_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(84)
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc102_84d_slope_v102_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc102_84d_slope_v102_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc103_5d_slope_v103_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc103_5d_slope_v103_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc103_5d_slope_v103_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc104_105d_slope_v104_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).mean()
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc104_105d_slope_v104_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc104_105d_slope_v104_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc105_105d_slope_v105_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(105)
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc105_105d_slope_v105_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc105_105d_slope_v105_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc106_21d_slope_v106_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).skew()
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc106_21d_slope_v106_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc106_21d_slope_v106_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc107_105d_slope_v107_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).kurt()
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc107_105d_slope_v107_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc107_105d_slope_v107_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc108_42d_slope_v108_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).mean()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc108_42d_slope_v108_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc108_42d_slope_v108_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc109_126d_slope_v109_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc109_126d_slope_v109_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc109_126d_slope_v109_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc110_42d_slope_v110_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(42)
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc110_42d_slope_v110_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc110_42d_slope_v110_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc111_126d_slope_v111_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).min()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc111_126d_slope_v111_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc111_126d_slope_v111_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc112_21d_slope_v112_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(21).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc112_21d_slope_v112_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc112_21d_slope_v112_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc113_10d_slope_v113_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).max()
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc113_10d_slope_v113_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc113_10d_slope_v113_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc114_21d_slope_v114_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).std()
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc114_21d_slope_v114_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc114_21d_slope_v114_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc115_63d_slope_v115_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).max()
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc115_63d_slope_v115_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc115_63d_slope_v115_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc116_10d_slope_v116_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).quantile(0.5)
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc116_10d_slope_v116_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc116_10d_slope_v116_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc117_84d_slope_v117_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).std()
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc117_84d_slope_v117_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc117_84d_slope_v117_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc118_252d_slope_v118_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).min()
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc118_252d_slope_v118_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc118_252d_slope_v118_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc119_10d_slope_v119_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).rank(pct=True)
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc119_10d_slope_v119_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc119_10d_slope_v119_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc120_21d_slope_v120_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.diff(21)
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc120_21d_slope_v120_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc120_21d_slope_v120_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc121_252d_slope_v121_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).kurt()
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc121_252d_slope_v121_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc121_252d_slope_v121_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc122_200d_slope_v122_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(200)
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc122_200d_slope_v122_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc122_200d_slope_v122_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc123_42d_slope_v123_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).std()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc123_42d_slope_v123_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc123_42d_slope_v123_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc124_84d_slope_v124_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(84).max().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc124_84d_slope_v124_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc124_84d_slope_v124_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc125_200d_slope_v125_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(200).skew()
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc125_200d_slope_v125_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc125_200d_slope_v125_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc126_63d_slope_v126_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(63).mean()) / v_003.rolling(63).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc126_63d_slope_v126_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc126_63d_slope_v126_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc127_42d_slope_v127_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(42).std()
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc127_42d_slope_v127_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc127_42d_slope_v127_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc128_10d_slope_v128_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(10).std()
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc128_10d_slope_v128_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc128_10d_slope_v128_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc129_105d_slope_v129_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).std()
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc129_105d_slope_v129_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc129_105d_slope_v129_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc130_84d_slope_v130_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).kurt()
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc130_84d_slope_v130_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc130_84d_slope_v130_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc131_252d_slope_v131_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).max()
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc131_252d_slope_v131_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc131_252d_slope_v131_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc132_126d_slope_v132_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(126).skew()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc132_126d_slope_v132_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc132_126d_slope_v132_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc133_21d_slope_v133_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).kurt()
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc133_21d_slope_v133_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc133_21d_slope_v133_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc134_10d_slope_v134_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(10).kurt()
    v_005 = v_004.diff(1).rolling(10).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc134_10d_slope_v134_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc134_10d_slope_v134_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc135_5d_slope_v135_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(5).min()
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc135_5d_slope_v135_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc135_5d_slope_v135_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc136_63d_slope_v136_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = (v_003 / v_003.rolling(63).min().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc136_63d_slope_v136_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc136_63d_slope_v136_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc137_200d_slope_v137_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(200).std()
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc137_200d_slope_v137_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc137_200d_slope_v137_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc138_84d_slope_v138_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).skew()
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc138_84d_slope_v138_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc138_84d_slope_v138_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc139_200d_slope_v139_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(200)
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc139_200d_slope_v139_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc139_200d_slope_v139_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc140_150d_slope_v140_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(150).max()
    v_005 = v_004.diff(1).rolling(150).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc140_150d_slope_v140_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc140_150d_slope_v140_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc141_84d_slope_v141_signal(capex, equity):
    v_001 = capex
    v_002 = equity
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(84).mean()
    v_005 = v_004.diff(1).rolling(84).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc141_84d_slope_v141_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc141_84d_slope_v141_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc142_63d_slope_v142_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(63)
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc142_63d_slope_v142_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc142_63d_slope_v142_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc143_42d_slope_v143_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(42).rank(pct=True)
    v_005 = v_004.diff(1).rolling(42).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc143_42d_slope_v143_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc143_42d_slope_v143_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc144_105d_slope_v144_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(105).mean()
    v_005 = v_004.diff(1).rolling(105).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc144_105d_slope_v144_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc144_105d_slope_v144_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc145_21d_slope_v145_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(21).kurt()
    v_005 = v_004.diff(1).rolling(21).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc145_21d_slope_v145_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc145_21d_slope_v145_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc146_200d_slope_v146_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.pct_change(200)
    v_005 = v_004.diff(1).rolling(200).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc146_200d_slope_v146_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc146_200d_slope_v146_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc147_5d_slope_v147_signal(assets, capex):
    v_001 = assets
    v_002 = capex
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = ((v_003 - v_003.rolling(5).mean()) / v_003.rolling(5).std().replace(0, np.nan))
    v_005 = v_004.diff(1).rolling(5).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc147_5d_slope_v147_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc147_5d_slope_v147_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc148_252d_slope_v148_signal(capex, revenue):
    v_001 = capex
    v_002 = revenue
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(252).skew()
    v_005 = v_004.diff(1).rolling(252).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc148_252d_slope_v148_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc148_252d_slope_v148_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc149_126d_slope_v149_signal(capex, ncfo):
    v_001 = capex
    v_002 = ncfo
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = np.log(v_003.abs().replace(0, np.nan)).rolling(126).std()
    v_005 = v_004.diff(1).rolling(126).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc149_126d_slope_v149_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc149_126d_slope_v149_signal

def f113c_f113_capex_to_assets_intensity_cycles_calc150_63d_slope_v150_signal(capex, ebitda):
    v_001 = capex
    v_002 = ebitda
    v_003 = v_001 / v_002.replace(0, np.nan)
    v_004 = v_003.rolling(63).kurt()
    v_005 = v_004.diff(1).rolling(63).mean()
    v_006 = v_005.replace([np.inf, -np.inf], np.nan)
    v_007 = v_006.ffill()
    v_008 = v_007.fillna(0)
    v_009 = v_008.replace([np.inf, -np.inf], np.nan)
    return v_009
FEATURE_FUNCTIONS['f113c_f113_capex_to_assets_intensity_cycles_calc150_63d_slope_v150_signal'] = f113c_f113_capex_to_assets_intensity_cycles_calc150_63d_slope_v150_signal


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
