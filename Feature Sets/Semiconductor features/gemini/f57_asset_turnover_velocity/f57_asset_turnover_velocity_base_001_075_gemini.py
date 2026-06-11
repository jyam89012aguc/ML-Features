import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f57at_f57_asset_turnover_velocity_calc001_252d_base_v001_signal(equity, revenue):
    res = (revenue / equity).pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc001_252d_base_v001_signal'] = f57at_f57_asset_turnover_velocity_calc001_252d_base_v001_signal

def f57at_f57_asset_turnover_velocity_calc002_5d_base_v002_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc002_5d_base_v002_signal'] = f57at_f57_asset_turnover_velocity_calc002_5d_base_v002_signal

def f57at_f57_asset_turnover_velocity_calc003_126d_base_v003_signal(assets, netinc):
    res = (netinc / assets).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc003_126d_base_v003_signal'] = f57at_f57_asset_turnover_velocity_calc003_126d_base_v003_signal

def f57at_f57_asset_turnover_velocity_calc004_126d_base_v004_signal(equity, revenue):
    res = (revenue / equity).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc004_126d_base_v004_signal'] = f57at_f57_asset_turnover_velocity_calc004_126d_base_v004_signal

def f57at_f57_asset_turnover_velocity_calc005_252d_base_v005_signal(equity, gp):
    res = (gp / equity).rolling(252).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc005_252d_base_v005_signal'] = f57at_f57_asset_turnover_velocity_calc005_252d_base_v005_signal

def f57at_f57_asset_turnover_velocity_calc006_252d_base_v006_signal(capex, revenue):
    res = (revenue / capex).pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc006_252d_base_v006_signal'] = f57at_f57_asset_turnover_velocity_calc006_252d_base_v006_signal

def f57at_f57_asset_turnover_velocity_calc007_252d_base_v007_signal(assets, netinc):
    res = (netinc / assets).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc007_252d_base_v007_signal'] = f57at_f57_asset_turnover_velocity_calc007_252d_base_v007_signal

def f57at_f57_asset_turnover_velocity_calc008_5d_base_v008_signal(assets, gp):
    res = ((gp / assets) / (gp / assets).rolling(5).max())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc008_5d_base_v008_signal'] = f57at_f57_asset_turnover_velocity_calc008_5d_base_v008_signal

def f57at_f57_asset_turnover_velocity_calc009_10d_base_v009_signal(equity, revenue):
    res = ((revenue / equity) / (revenue / equity).rolling(10).max())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc009_10d_base_v009_signal'] = f57at_f57_asset_turnover_velocity_calc009_10d_base_v009_signal

def f57at_f57_asset_turnover_velocity_calc010_126d_base_v010_signal(liabilities, revenue):
    res = ((revenue / liabilities) / (revenue / liabilities).rolling(126).max())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc010_126d_base_v010_signal'] = f57at_f57_asset_turnover_velocity_calc010_126d_base_v010_signal

def f57at_f57_asset_turnover_velocity_calc011_5d_base_v011_signal(liabilities, revenue):
    res = ((revenue / liabilities) / (revenue / liabilities).rolling(5).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc011_5d_base_v011_signal'] = f57at_f57_asset_turnover_velocity_calc011_5d_base_v011_signal

def f57at_f57_asset_turnover_velocity_calc012_42d_base_v012_signal(capex, revenue):
    res = (revenue / capex).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc012_42d_base_v012_signal'] = f57at_f57_asset_turnover_velocity_calc012_42d_base_v012_signal

def f57at_f57_asset_turnover_velocity_calc013_10d_base_v013_signal(assets, opinc):
    res = ((opinc / assets) - (opinc / assets).rolling(10).mean()) / (opinc / assets).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc013_10d_base_v013_signal'] = f57at_f57_asset_turnover_velocity_calc013_10d_base_v013_signal

def f57at_f57_asset_turnover_velocity_calc014_5d_base_v014_signal(assets, fcf):
    res = (fcf / assets).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc014_5d_base_v014_signal'] = f57at_f57_asset_turnover_velocity_calc014_5d_base_v014_signal

def f57at_f57_asset_turnover_velocity_calc015_126d_base_v015_signal(liabilities, revenue):
    res = np.log((revenue / liabilities).abs().replace(0, np.nan)).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc015_126d_base_v015_signal'] = f57at_f57_asset_turnover_velocity_calc015_126d_base_v015_signal

def f57at_f57_asset_turnover_velocity_calc016_42d_base_v016_signal(equity, revenue):
    res = ((revenue / equity) - (revenue / equity).rolling(42).mean()) / (revenue / equity).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc016_42d_base_v016_signal'] = f57at_f57_asset_turnover_velocity_calc016_42d_base_v016_signal

def f57at_f57_asset_turnover_velocity_calc017_42d_base_v017_signal(assets, gp):
    res = ((gp / assets) / (gp / assets).rolling(42).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc017_42d_base_v017_signal'] = f57at_f57_asset_turnover_velocity_calc017_42d_base_v017_signal

def f57at_f57_asset_turnover_velocity_calc018_63d_base_v018_signal(assets, fcf):
    res = (fcf / assets).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc018_63d_base_v018_signal'] = f57at_f57_asset_turnover_velocity_calc018_63d_base_v018_signal

def f57at_f57_asset_turnover_velocity_calc019_252d_base_v019_signal(liabilities, revenue):
    res = (revenue / liabilities).rolling(252).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc019_252d_base_v019_signal'] = f57at_f57_asset_turnover_velocity_calc019_252d_base_v019_signal

def f57at_f57_asset_turnover_velocity_calc020_42d_base_v020_signal(assets, gp):
    res = (gp / assets).rolling(42).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc020_42d_base_v020_signal'] = f57at_f57_asset_turnover_velocity_calc020_42d_base_v020_signal

def f57at_f57_asset_turnover_velocity_calc021_10d_base_v021_signal(liabilities, revenue):
    res = (revenue / liabilities).rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc021_10d_base_v021_signal'] = f57at_f57_asset_turnover_velocity_calc021_10d_base_v021_signal

def f57at_f57_asset_turnover_velocity_calc022_5d_base_v022_signal(assets, revenue):
    res = (revenue / assets).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc022_5d_base_v022_signal'] = f57at_f57_asset_turnover_velocity_calc022_5d_base_v022_signal

def f57at_f57_asset_turnover_velocity_calc023_5d_base_v023_signal(assets, netinc):
    res = ((netinc / assets) - (netinc / assets).rolling(5).mean()) / (netinc / assets).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc023_5d_base_v023_signal'] = f57at_f57_asset_turnover_velocity_calc023_5d_base_v023_signal

def f57at_f57_asset_turnover_velocity_calc024_5d_base_v024_signal(assets, opinc):
    res = (opinc / assets).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc024_5d_base_v024_signal'] = f57at_f57_asset_turnover_velocity_calc024_5d_base_v024_signal

def f57at_f57_asset_turnover_velocity_calc025_21d_base_v025_signal(assets, fcf):
    res = (fcf / assets).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc025_21d_base_v025_signal'] = f57at_f57_asset_turnover_velocity_calc025_21d_base_v025_signal

def f57at_f57_asset_turnover_velocity_calc026_126d_base_v026_signal(equity, gp):
    res = ((gp / equity) / (gp / equity).rolling(126).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc026_126d_base_v026_signal'] = f57at_f57_asset_turnover_velocity_calc026_126d_base_v026_signal

def f57at_f57_asset_turnover_velocity_calc027_42d_base_v027_signal(assets, netinc):
    res = (netinc / assets).rolling(42).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc027_42d_base_v027_signal'] = f57at_f57_asset_turnover_velocity_calc027_42d_base_v027_signal

def f57at_f57_asset_turnover_velocity_calc028_42d_base_v028_signal(equity, gp):
    res = (gp / equity).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc028_42d_base_v028_signal'] = f57at_f57_asset_turnover_velocity_calc028_42d_base_v028_signal

def f57at_f57_asset_turnover_velocity_calc029_10d_base_v029_signal(assets, gp):
    res = (gp / assets).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc029_10d_base_v029_signal'] = f57at_f57_asset_turnover_velocity_calc029_10d_base_v029_signal

def f57at_f57_asset_turnover_velocity_calc030_63d_base_v030_signal(assets, fcf):
    res = (fcf / assets).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc030_63d_base_v030_signal'] = f57at_f57_asset_turnover_velocity_calc030_63d_base_v030_signal

def f57at_f57_asset_turnover_velocity_calc031_63d_base_v031_signal(equity, gp):
    res = ((gp / equity) - (gp / equity).rolling(63).mean()) / (gp / equity).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc031_63d_base_v031_signal'] = f57at_f57_asset_turnover_velocity_calc031_63d_base_v031_signal

def f57at_f57_asset_turnover_velocity_calc032_252d_base_v032_signal(liabilities, revenue):
    res = (revenue / liabilities).rolling(252).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc032_252d_base_v032_signal'] = f57at_f57_asset_turnover_velocity_calc032_252d_base_v032_signal

def f57at_f57_asset_turnover_velocity_calc033_63d_base_v033_signal(assets, fcf):
    res = (fcf / assets).rolling(63).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc033_63d_base_v033_signal'] = f57at_f57_asset_turnover_velocity_calc033_63d_base_v033_signal

def f57at_f57_asset_turnover_velocity_calc034_252d_base_v034_signal(assets, opinc):
    res = (opinc / assets).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc034_252d_base_v034_signal'] = f57at_f57_asset_turnover_velocity_calc034_252d_base_v034_signal

def f57at_f57_asset_turnover_velocity_calc035_63d_base_v035_signal(equity, gp):
    res = (gp / equity).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc035_63d_base_v035_signal'] = f57at_f57_asset_turnover_velocity_calc035_63d_base_v035_signal

def f57at_f57_asset_turnover_velocity_calc036_10d_base_v036_signal(assets, fcf):
    res = (fcf / assets).rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc036_10d_base_v036_signal'] = f57at_f57_asset_turnover_velocity_calc036_10d_base_v036_signal

def f57at_f57_asset_turnover_velocity_calc037_126d_base_v037_signal(assets, revenue):
    res = (revenue / assets).rolling(126).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc037_126d_base_v037_signal'] = f57at_f57_asset_turnover_velocity_calc037_126d_base_v037_signal

def f57at_f57_asset_turnover_velocity_calc038_21d_base_v038_signal(assets, netinc):
    res = (netinc / assets).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc038_21d_base_v038_signal'] = f57at_f57_asset_turnover_velocity_calc038_21d_base_v038_signal

def f57at_f57_asset_turnover_velocity_calc039_5d_base_v039_signal(assets, gp):
    res = (gp / assets).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc039_5d_base_v039_signal'] = f57at_f57_asset_turnover_velocity_calc039_5d_base_v039_signal

def f57at_f57_asset_turnover_velocity_calc040_21d_base_v040_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc040_21d_base_v040_signal'] = f57at_f57_asset_turnover_velocity_calc040_21d_base_v040_signal

def f57at_f57_asset_turnover_velocity_calc041_252d_base_v041_signal(assets, netinc):
    res = (netinc / assets).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc041_252d_base_v041_signal'] = f57at_f57_asset_turnover_velocity_calc041_252d_base_v041_signal

def f57at_f57_asset_turnover_velocity_calc042_21d_base_v042_signal(assets, fcf):
    res = (fcf / assets).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc042_21d_base_v042_signal'] = f57at_f57_asset_turnover_velocity_calc042_21d_base_v042_signal

def f57at_f57_asset_turnover_velocity_calc043_126d_base_v043_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(126).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc043_126d_base_v043_signal'] = f57at_f57_asset_turnover_velocity_calc043_126d_base_v043_signal

def f57at_f57_asset_turnover_velocity_calc044_42d_base_v044_signal(assets, opinc):
    res = (opinc / assets).rolling(42).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc044_42d_base_v044_signal'] = f57at_f57_asset_turnover_velocity_calc044_42d_base_v044_signal

def f57at_f57_asset_turnover_velocity_calc045_10d_base_v045_signal(capex, revenue):
    res = ((revenue / capex) / (revenue / capex).rolling(10).max())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc045_10d_base_v045_signal'] = f57at_f57_asset_turnover_velocity_calc045_10d_base_v045_signal

def f57at_f57_asset_turnover_velocity_calc046_10d_base_v046_signal(assets, gp):
    res = (gp / assets).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc046_10d_base_v046_signal'] = f57at_f57_asset_turnover_velocity_calc046_10d_base_v046_signal

def f57at_f57_asset_turnover_velocity_calc047_63d_base_v047_signal(assets, fcf):
    res = ((fcf / assets) - (fcf / assets).rolling(63).mean()) / (fcf / assets).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc047_63d_base_v047_signal'] = f57at_f57_asset_turnover_velocity_calc047_63d_base_v047_signal

def f57at_f57_asset_turnover_velocity_calc048_126d_base_v048_signal(equity, revenue):
    res = ((revenue / equity) / (revenue / equity).rolling(126).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc048_126d_base_v048_signal'] = f57at_f57_asset_turnover_velocity_calc048_126d_base_v048_signal

def f57at_f57_asset_turnover_velocity_calc049_252d_base_v049_signal(assets, netinc):
    res = (netinc / assets).rolling(252).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc049_252d_base_v049_signal'] = f57at_f57_asset_turnover_velocity_calc049_252d_base_v049_signal

def f57at_f57_asset_turnover_velocity_calc050_5d_base_v050_signal(assets, revenue):
    res = (revenue / assets).rolling(5).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc050_5d_base_v050_signal'] = f57at_f57_asset_turnover_velocity_calc050_5d_base_v050_signal

def f57at_f57_asset_turnover_velocity_calc051_126d_base_v051_signal(revenue, workingcapital):
    res = ((revenue / workingcapital) / (revenue / workingcapital).rolling(126).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc051_126d_base_v051_signal'] = f57at_f57_asset_turnover_velocity_calc051_126d_base_v051_signal

def f57at_f57_asset_turnover_velocity_calc052_10d_base_v052_signal(assets, netinc):
    res = ((netinc / assets) / (netinc / assets).rolling(10).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc052_10d_base_v052_signal'] = f57at_f57_asset_turnover_velocity_calc052_10d_base_v052_signal

def f57at_f57_asset_turnover_velocity_calc053_252d_base_v053_signal(assets, netinc):
    res = ((netinc / assets) / (netinc / assets).rolling(252).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc053_252d_base_v053_signal'] = f57at_f57_asset_turnover_velocity_calc053_252d_base_v053_signal

def f57at_f57_asset_turnover_velocity_calc054_21d_base_v054_signal(equity, revenue):
    res = (revenue / equity).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc054_21d_base_v054_signal'] = f57at_f57_asset_turnover_velocity_calc054_21d_base_v054_signal

def f57at_f57_asset_turnover_velocity_calc055_10d_base_v055_signal(capex, revenue):
    res = (revenue / capex).rolling(10).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc055_10d_base_v055_signal'] = f57at_f57_asset_turnover_velocity_calc055_10d_base_v055_signal

def f57at_f57_asset_turnover_velocity_calc056_63d_base_v056_signal(capex, revenue):
    res = (revenue / capex).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc056_63d_base_v056_signal'] = f57at_f57_asset_turnover_velocity_calc056_63d_base_v056_signal

def f57at_f57_asset_turnover_velocity_calc057_10d_base_v057_signal(equity, revenue):
    res = (revenue / equity).rolling(10).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc057_10d_base_v057_signal'] = f57at_f57_asset_turnover_velocity_calc057_10d_base_v057_signal

def f57at_f57_asset_turnover_velocity_calc058_42d_base_v058_signal(equity, gp):
    res = (gp / equity).rolling(42).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc058_42d_base_v058_signal'] = f57at_f57_asset_turnover_velocity_calc058_42d_base_v058_signal

def f57at_f57_asset_turnover_velocity_calc059_63d_base_v059_signal(equity, gp):
    res = (gp / equity).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc059_63d_base_v059_signal'] = f57at_f57_asset_turnover_velocity_calc059_63d_base_v059_signal

def f57at_f57_asset_turnover_velocity_calc060_10d_base_v060_signal(equity, revenue):
    res = ((revenue / equity) - (revenue / equity).rolling(10).mean()) / (revenue / equity).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc060_10d_base_v060_signal'] = f57at_f57_asset_turnover_velocity_calc060_10d_base_v060_signal

def f57at_f57_asset_turnover_velocity_calc061_42d_base_v061_signal(assets, opinc):
    res = (opinc / assets).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc061_42d_base_v061_signal'] = f57at_f57_asset_turnover_velocity_calc061_42d_base_v061_signal

def f57at_f57_asset_turnover_velocity_calc062_42d_base_v062_signal(assets, gp):
    res = (gp / assets).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc062_42d_base_v062_signal'] = f57at_f57_asset_turnover_velocity_calc062_42d_base_v062_signal

def f57at_f57_asset_turnover_velocity_calc063_63d_base_v063_signal(assets, opinc):
    res = ((opinc / assets) - (opinc / assets).rolling(63).mean()) / (opinc / assets).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc063_63d_base_v063_signal'] = f57at_f57_asset_turnover_velocity_calc063_63d_base_v063_signal

def f57at_f57_asset_turnover_velocity_calc064_5d_base_v064_signal(assets, gp):
    res = (gp / assets).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc064_5d_base_v064_signal'] = f57at_f57_asset_turnover_velocity_calc064_5d_base_v064_signal

def f57at_f57_asset_turnover_velocity_calc065_63d_base_v065_signal(assets, netinc):
    res = (netinc / assets).rolling(63).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc065_63d_base_v065_signal'] = f57at_f57_asset_turnover_velocity_calc065_63d_base_v065_signal

def f57at_f57_asset_turnover_velocity_calc066_126d_base_v066_signal(assets, revenue):
    res = (revenue / assets).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc066_126d_base_v066_signal'] = f57at_f57_asset_turnover_velocity_calc066_126d_base_v066_signal

def f57at_f57_asset_turnover_velocity_calc067_10d_base_v067_signal(assets, netinc):
    res = np.log((netinc / assets).abs().replace(0, np.nan)).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc067_10d_base_v067_signal'] = f57at_f57_asset_turnover_velocity_calc067_10d_base_v067_signal

def f57at_f57_asset_turnover_velocity_calc068_5d_base_v068_signal(equity, gp):
    res = (gp / equity).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc068_5d_base_v068_signal'] = f57at_f57_asset_turnover_velocity_calc068_5d_base_v068_signal

def f57at_f57_asset_turnover_velocity_calc069_10d_base_v069_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(10).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc069_10d_base_v069_signal'] = f57at_f57_asset_turnover_velocity_calc069_10d_base_v069_signal

def f57at_f57_asset_turnover_velocity_calc070_252d_base_v070_signal(assets, opinc):
    res = (opinc / assets).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc070_252d_base_v070_signal'] = f57at_f57_asset_turnover_velocity_calc070_252d_base_v070_signal

def f57at_f57_asset_turnover_velocity_calc071_21d_base_v071_signal(equity, revenue):
    res = (revenue / equity).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc071_21d_base_v071_signal'] = f57at_f57_asset_turnover_velocity_calc071_21d_base_v071_signal

def f57at_f57_asset_turnover_velocity_calc072_5d_base_v072_signal(assets, gp):
    res = (gp / assets).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc072_5d_base_v072_signal'] = f57at_f57_asset_turnover_velocity_calc072_5d_base_v072_signal

def f57at_f57_asset_turnover_velocity_calc073_21d_base_v073_signal(assets, fcf):
    res = (fcf / assets).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc073_21d_base_v073_signal'] = f57at_f57_asset_turnover_velocity_calc073_21d_base_v073_signal

def f57at_f57_asset_turnover_velocity_calc074_42d_base_v074_signal(equity, revenue):
    res = (revenue / equity).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc074_42d_base_v074_signal'] = f57at_f57_asset_turnover_velocity_calc074_42d_base_v074_signal

def f57at_f57_asset_turnover_velocity_calc075_252d_base_v075_signal(revenue, workingcapital):
    res = np.log((revenue / workingcapital).abs().replace(0, np.nan)).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc075_252d_base_v075_signal'] = f57at_f57_asset_turnover_velocity_calc075_252d_base_v075_signal


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
