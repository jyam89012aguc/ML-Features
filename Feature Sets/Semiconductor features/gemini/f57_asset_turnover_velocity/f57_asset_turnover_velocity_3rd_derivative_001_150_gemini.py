import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f57at_f57_asset_turnover_velocity_calc001_252d_jerk_v001_signal(equity, revenue):
    res = ((revenue / equity).pct_change(252)).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc001_252d_jerk_v001_signal'] = f57at_f57_asset_turnover_velocity_calc001_252d_jerk_v001_signal

def f57at_f57_asset_turnover_velocity_calc002_5d_jerk_v002_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).rolling(5).skew()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc002_5d_jerk_v002_signal'] = f57at_f57_asset_turnover_velocity_calc002_5d_jerk_v002_signal

def f57at_f57_asset_turnover_velocity_calc003_126d_jerk_v003_signal(assets, netinc):
    res = ((netinc / assets).rolling(126).max()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc003_126d_jerk_v003_signal'] = f57at_f57_asset_turnover_velocity_calc003_126d_jerk_v003_signal

def f57at_f57_asset_turnover_velocity_calc004_126d_jerk_v004_signal(equity, revenue):
    res = ((revenue / equity).rolling(126).mean()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc004_126d_jerk_v004_signal'] = f57at_f57_asset_turnover_velocity_calc004_126d_jerk_v004_signal

def f57at_f57_asset_turnover_velocity_calc005_252d_jerk_v005_signal(equity, gp):
    res = ((gp / equity).rolling(252).var()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc005_252d_jerk_v005_signal'] = f57at_f57_asset_turnover_velocity_calc005_252d_jerk_v005_signal

def f57at_f57_asset_turnover_velocity_calc006_252d_jerk_v006_signal(capex, revenue):
    res = ((revenue / capex).pct_change(252)).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc006_252d_jerk_v006_signal'] = f57at_f57_asset_turnover_velocity_calc006_252d_jerk_v006_signal

def f57at_f57_asset_turnover_velocity_calc007_252d_jerk_v007_signal(assets, netinc):
    res = ((netinc / assets).rolling(252).min()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc007_252d_jerk_v007_signal'] = f57at_f57_asset_turnover_velocity_calc007_252d_jerk_v007_signal

def f57at_f57_asset_turnover_velocity_calc008_5d_jerk_v008_signal(assets, gp):
    res = (((gp / assets) / (gp / assets).rolling(5).max())).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc008_5d_jerk_v008_signal'] = f57at_f57_asset_turnover_velocity_calc008_5d_jerk_v008_signal

def f57at_f57_asset_turnover_velocity_calc009_10d_jerk_v009_signal(equity, revenue):
    res = (((revenue / equity) / (revenue / equity).rolling(10).max())).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc009_10d_jerk_v009_signal'] = f57at_f57_asset_turnover_velocity_calc009_10d_jerk_v009_signal

def f57at_f57_asset_turnover_velocity_calc010_126d_jerk_v010_signal(liabilities, revenue):
    res = (((revenue / liabilities) / (revenue / liabilities).rolling(126).max())).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc010_126d_jerk_v010_signal'] = f57at_f57_asset_turnover_velocity_calc010_126d_jerk_v010_signal

def f57at_f57_asset_turnover_velocity_calc011_5d_jerk_v011_signal(liabilities, revenue):
    res = (((revenue / liabilities) / (revenue / liabilities).rolling(5).min())).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc011_5d_jerk_v011_signal'] = f57at_f57_asset_turnover_velocity_calc011_5d_jerk_v011_signal

def f57at_f57_asset_turnover_velocity_calc012_42d_jerk_v012_signal(capex, revenue):
    res = ((revenue / capex).diff(42)).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc012_42d_jerk_v012_signal'] = f57at_f57_asset_turnover_velocity_calc012_42d_jerk_v012_signal

def f57at_f57_asset_turnover_velocity_calc013_10d_jerk_v013_signal(assets, opinc):
    res = (((opinc / assets) - (opinc / assets).rolling(10).mean()) / (opinc / assets).rolling(10).std()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc013_10d_jerk_v013_signal'] = f57at_f57_asset_turnover_velocity_calc013_10d_jerk_v013_signal

def f57at_f57_asset_turnover_velocity_calc014_5d_jerk_v014_signal(assets, fcf):
    res = ((fcf / assets).pct_change(5)).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc014_5d_jerk_v014_signal'] = f57at_f57_asset_turnover_velocity_calc014_5d_jerk_v014_signal

def f57at_f57_asset_turnover_velocity_calc015_126d_jerk_v015_signal(liabilities, revenue):
    res = (np.log((revenue / liabilities).abs().replace(0, np.nan)).rolling(126).std()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc015_126d_jerk_v015_signal'] = f57at_f57_asset_turnover_velocity_calc015_126d_jerk_v015_signal

def f57at_f57_asset_turnover_velocity_calc016_42d_jerk_v016_signal(equity, revenue):
    res = (((revenue / equity) - (revenue / equity).rolling(42).mean()) / (revenue / equity).rolling(42).std()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc016_42d_jerk_v016_signal'] = f57at_f57_asset_turnover_velocity_calc016_42d_jerk_v016_signal

def f57at_f57_asset_turnover_velocity_calc017_42d_jerk_v017_signal(assets, gp):
    res = (((gp / assets) / (gp / assets).rolling(42).min())).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc017_42d_jerk_v017_signal'] = f57at_f57_asset_turnover_velocity_calc017_42d_jerk_v017_signal

def f57at_f57_asset_turnover_velocity_calc018_63d_jerk_v018_signal(assets, fcf):
    res = ((fcf / assets).rolling(63).max()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc018_63d_jerk_v018_signal'] = f57at_f57_asset_turnover_velocity_calc018_63d_jerk_v018_signal

def f57at_f57_asset_turnover_velocity_calc019_252d_jerk_v019_signal(liabilities, revenue):
    res = ((revenue / liabilities).rolling(252).rank(pct=True)).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc019_252d_jerk_v019_signal'] = f57at_f57_asset_turnover_velocity_calc019_252d_jerk_v019_signal

def f57at_f57_asset_turnover_velocity_calc020_42d_jerk_v020_signal(assets, gp):
    res = ((gp / assets).rolling(42).max()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc020_42d_jerk_v020_signal'] = f57at_f57_asset_turnover_velocity_calc020_42d_jerk_v020_signal

def f57at_f57_asset_turnover_velocity_calc021_10d_jerk_v021_signal(liabilities, revenue):
    res = ((revenue / liabilities).rolling(10).skew()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc021_10d_jerk_v021_signal'] = f57at_f57_asset_turnover_velocity_calc021_10d_jerk_v021_signal

def f57at_f57_asset_turnover_velocity_calc022_5d_jerk_v022_signal(assets, revenue):
    res = ((revenue / assets).diff(5)).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc022_5d_jerk_v022_signal'] = f57at_f57_asset_turnover_velocity_calc022_5d_jerk_v022_signal

def f57at_f57_asset_turnover_velocity_calc023_5d_jerk_v023_signal(assets, netinc):
    res = (((netinc / assets) - (netinc / assets).rolling(5).mean()) / (netinc / assets).rolling(5).std()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc023_5d_jerk_v023_signal'] = f57at_f57_asset_turnover_velocity_calc023_5d_jerk_v023_signal

def f57at_f57_asset_turnover_velocity_calc024_5d_jerk_v024_signal(assets, opinc):
    res = ((opinc / assets).rolling(5).kurt()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc024_5d_jerk_v024_signal'] = f57at_f57_asset_turnover_velocity_calc024_5d_jerk_v024_signal

def f57at_f57_asset_turnover_velocity_calc025_21d_jerk_v025_signal(assets, fcf):
    res = ((fcf / assets).rolling(21).max()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc025_21d_jerk_v025_signal'] = f57at_f57_asset_turnover_velocity_calc025_21d_jerk_v025_signal

def f57at_f57_asset_turnover_velocity_calc026_126d_jerk_v026_signal(equity, gp):
    res = (((gp / equity) / (gp / equity).rolling(126).min())).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc026_126d_jerk_v026_signal'] = f57at_f57_asset_turnover_velocity_calc026_126d_jerk_v026_signal

def f57at_f57_asset_turnover_velocity_calc027_42d_jerk_v027_signal(assets, netinc):
    res = ((netinc / assets).rolling(42).max()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc027_42d_jerk_v027_signal'] = f57at_f57_asset_turnover_velocity_calc027_42d_jerk_v027_signal

def f57at_f57_asset_turnover_velocity_calc028_42d_jerk_v028_signal(equity, gp):
    res = ((gp / equity).diff(42)).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc028_42d_jerk_v028_signal'] = f57at_f57_asset_turnover_velocity_calc028_42d_jerk_v028_signal

def f57at_f57_asset_turnover_velocity_calc029_10d_jerk_v029_signal(assets, gp):
    res = ((gp / assets).rolling(10).mean()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc029_10d_jerk_v029_signal'] = f57at_f57_asset_turnover_velocity_calc029_10d_jerk_v029_signal

def f57at_f57_asset_turnover_velocity_calc030_63d_jerk_v030_signal(assets, fcf):
    res = ((fcf / assets).diff(63)).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc030_63d_jerk_v030_signal'] = f57at_f57_asset_turnover_velocity_calc030_63d_jerk_v030_signal

def f57at_f57_asset_turnover_velocity_calc031_63d_jerk_v031_signal(equity, gp):
    res = (((gp / equity) - (gp / equity).rolling(63).mean()) / (gp / equity).rolling(63).std()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc031_63d_jerk_v031_signal'] = f57at_f57_asset_turnover_velocity_calc031_63d_jerk_v031_signal

def f57at_f57_asset_turnover_velocity_calc032_252d_jerk_v032_signal(liabilities, revenue):
    res = ((revenue / liabilities).rolling(252).quantile(0.5)).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc032_252d_jerk_v032_signal'] = f57at_f57_asset_turnover_velocity_calc032_252d_jerk_v032_signal

def f57at_f57_asset_turnover_velocity_calc033_63d_jerk_v033_signal(assets, fcf):
    res = ((fcf / assets).rolling(63).rank(pct=True)).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc033_63d_jerk_v033_signal'] = f57at_f57_asset_turnover_velocity_calc033_63d_jerk_v033_signal

def f57at_f57_asset_turnover_velocity_calc034_252d_jerk_v034_signal(assets, opinc):
    res = ((opinc / assets).rolling(252).std()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc034_252d_jerk_v034_signal'] = f57at_f57_asset_turnover_velocity_calc034_252d_jerk_v034_signal

def f57at_f57_asset_turnover_velocity_calc035_63d_jerk_v035_signal(equity, gp):
    res = ((gp / equity).rolling(63).mean()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc035_63d_jerk_v035_signal'] = f57at_f57_asset_turnover_velocity_calc035_63d_jerk_v035_signal

def f57at_f57_asset_turnover_velocity_calc036_10d_jerk_v036_signal(assets, fcf):
    res = ((fcf / assets).rolling(10).skew()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc036_10d_jerk_v036_signal'] = f57at_f57_asset_turnover_velocity_calc036_10d_jerk_v036_signal

def f57at_f57_asset_turnover_velocity_calc037_126d_jerk_v037_signal(assets, revenue):
    res = ((revenue / assets).rolling(126).min()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc037_126d_jerk_v037_signal'] = f57at_f57_asset_turnover_velocity_calc037_126d_jerk_v037_signal

def f57at_f57_asset_turnover_velocity_calc038_21d_jerk_v038_signal(assets, netinc):
    res = ((netinc / assets).rolling(21).kurt()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc038_21d_jerk_v038_signal'] = f57at_f57_asset_turnover_velocity_calc038_21d_jerk_v038_signal

def f57at_f57_asset_turnover_velocity_calc039_5d_jerk_v039_signal(assets, gp):
    res = ((gp / assets).rolling(5).max()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc039_5d_jerk_v039_signal'] = f57at_f57_asset_turnover_velocity_calc039_5d_jerk_v039_signal

def f57at_f57_asset_turnover_velocity_calc040_21d_jerk_v040_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).rolling(21).max()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc040_21d_jerk_v040_signal'] = f57at_f57_asset_turnover_velocity_calc040_21d_jerk_v040_signal

def f57at_f57_asset_turnover_velocity_calc041_252d_jerk_v041_signal(assets, netinc):
    res = ((netinc / assets).rolling(252).std()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc041_252d_jerk_v041_signal'] = f57at_f57_asset_turnover_velocity_calc041_252d_jerk_v041_signal

def f57at_f57_asset_turnover_velocity_calc042_21d_jerk_v042_signal(assets, fcf):
    res = ((fcf / assets).rolling(21).skew()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc042_21d_jerk_v042_signal'] = f57at_f57_asset_turnover_velocity_calc042_21d_jerk_v042_signal

def f57at_f57_asset_turnover_velocity_calc043_126d_jerk_v043_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).rolling(126).quantile(0.5)).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc043_126d_jerk_v043_signal'] = f57at_f57_asset_turnover_velocity_calc043_126d_jerk_v043_signal

def f57at_f57_asset_turnover_velocity_calc044_42d_jerk_v044_signal(assets, opinc):
    res = ((opinc / assets).rolling(42).quantile(0.5)).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc044_42d_jerk_v044_signal'] = f57at_f57_asset_turnover_velocity_calc044_42d_jerk_v044_signal

def f57at_f57_asset_turnover_velocity_calc045_10d_jerk_v045_signal(capex, revenue):
    res = (((revenue / capex) / (revenue / capex).rolling(10).max())).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc045_10d_jerk_v045_signal'] = f57at_f57_asset_turnover_velocity_calc045_10d_jerk_v045_signal

def f57at_f57_asset_turnover_velocity_calc046_10d_jerk_v046_signal(assets, gp):
    res = ((gp / assets).rolling(10).std()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc046_10d_jerk_v046_signal'] = f57at_f57_asset_turnover_velocity_calc046_10d_jerk_v046_signal

def f57at_f57_asset_turnover_velocity_calc047_63d_jerk_v047_signal(assets, fcf):
    res = (((fcf / assets) - (fcf / assets).rolling(63).mean()) / (fcf / assets).rolling(63).std()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc047_63d_jerk_v047_signal'] = f57at_f57_asset_turnover_velocity_calc047_63d_jerk_v047_signal

def f57at_f57_asset_turnover_velocity_calc048_126d_jerk_v048_signal(equity, revenue):
    res = (((revenue / equity) / (revenue / equity).rolling(126).min())).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc048_126d_jerk_v048_signal'] = f57at_f57_asset_turnover_velocity_calc048_126d_jerk_v048_signal

def f57at_f57_asset_turnover_velocity_calc049_252d_jerk_v049_signal(assets, netinc):
    res = ((netinc / assets).rolling(252).rank(pct=True)).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc049_252d_jerk_v049_signal'] = f57at_f57_asset_turnover_velocity_calc049_252d_jerk_v049_signal

def f57at_f57_asset_turnover_velocity_calc050_5d_jerk_v050_signal(assets, revenue):
    res = ((revenue / assets).rolling(5).quantile(0.5)).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc050_5d_jerk_v050_signal'] = f57at_f57_asset_turnover_velocity_calc050_5d_jerk_v050_signal

def f57at_f57_asset_turnover_velocity_calc051_126d_jerk_v051_signal(revenue, workingcapital):
    res = (((revenue / workingcapital) / (revenue / workingcapital).rolling(126).min())).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc051_126d_jerk_v051_signal'] = f57at_f57_asset_turnover_velocity_calc051_126d_jerk_v051_signal

def f57at_f57_asset_turnover_velocity_calc052_10d_jerk_v052_signal(assets, netinc):
    res = (((netinc / assets) / (netinc / assets).rolling(10).min())).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc052_10d_jerk_v052_signal'] = f57at_f57_asset_turnover_velocity_calc052_10d_jerk_v052_signal

def f57at_f57_asset_turnover_velocity_calc053_252d_jerk_v053_signal(assets, netinc):
    res = (((netinc / assets) / (netinc / assets).rolling(252).min())).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc053_252d_jerk_v053_signal'] = f57at_f57_asset_turnover_velocity_calc053_252d_jerk_v053_signal

def f57at_f57_asset_turnover_velocity_calc054_21d_jerk_v054_signal(equity, revenue):
    res = ((revenue / equity).rolling(21).min()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc054_21d_jerk_v054_signal'] = f57at_f57_asset_turnover_velocity_calc054_21d_jerk_v054_signal

def f57at_f57_asset_turnover_velocity_calc055_10d_jerk_v055_signal(capex, revenue):
    res = ((revenue / capex).rolling(10).var()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc055_10d_jerk_v055_signal'] = f57at_f57_asset_turnover_velocity_calc055_10d_jerk_v055_signal

def f57at_f57_asset_turnover_velocity_calc056_63d_jerk_v056_signal(capex, revenue):
    res = ((revenue / capex).rolling(63).kurt()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc056_63d_jerk_v056_signal'] = f57at_f57_asset_turnover_velocity_calc056_63d_jerk_v056_signal

def f57at_f57_asset_turnover_velocity_calc057_10d_jerk_v057_signal(equity, revenue):
    res = ((revenue / equity).rolling(10).quantile(0.5)).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc057_10d_jerk_v057_signal'] = f57at_f57_asset_turnover_velocity_calc057_10d_jerk_v057_signal

def f57at_f57_asset_turnover_velocity_calc058_42d_jerk_v058_signal(equity, gp):
    res = ((gp / equity).rolling(42).var()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc058_42d_jerk_v058_signal'] = f57at_f57_asset_turnover_velocity_calc058_42d_jerk_v058_signal

def f57at_f57_asset_turnover_velocity_calc059_63d_jerk_v059_signal(equity, gp):
    res = ((gp / equity).rolling(63).max()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc059_63d_jerk_v059_signal'] = f57at_f57_asset_turnover_velocity_calc059_63d_jerk_v059_signal

def f57at_f57_asset_turnover_velocity_calc060_10d_jerk_v060_signal(equity, revenue):
    res = (((revenue / equity) - (revenue / equity).rolling(10).mean()) / (revenue / equity).rolling(10).std()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc060_10d_jerk_v060_signal'] = f57at_f57_asset_turnover_velocity_calc060_10d_jerk_v060_signal

def f57at_f57_asset_turnover_velocity_calc061_42d_jerk_v061_signal(assets, opinc):
    res = ((opinc / assets).diff(42)).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc061_42d_jerk_v061_signal'] = f57at_f57_asset_turnover_velocity_calc061_42d_jerk_v061_signal

def f57at_f57_asset_turnover_velocity_calc062_42d_jerk_v062_signal(assets, gp):
    res = ((gp / assets).rolling(42).skew()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc062_42d_jerk_v062_signal'] = f57at_f57_asset_turnover_velocity_calc062_42d_jerk_v062_signal

def f57at_f57_asset_turnover_velocity_calc063_63d_jerk_v063_signal(assets, opinc):
    res = (((opinc / assets) - (opinc / assets).rolling(63).mean()) / (opinc / assets).rolling(63).std()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc063_63d_jerk_v063_signal'] = f57at_f57_asset_turnover_velocity_calc063_63d_jerk_v063_signal

def f57at_f57_asset_turnover_velocity_calc064_5d_jerk_v064_signal(assets, gp):
    res = ((gp / assets).rolling(5).std()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc064_5d_jerk_v064_signal'] = f57at_f57_asset_turnover_velocity_calc064_5d_jerk_v064_signal

def f57at_f57_asset_turnover_velocity_calc065_63d_jerk_v065_signal(assets, netinc):
    res = ((netinc / assets).rolling(63).rank(pct=True)).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc065_63d_jerk_v065_signal'] = f57at_f57_asset_turnover_velocity_calc065_63d_jerk_v065_signal

def f57at_f57_asset_turnover_velocity_calc066_126d_jerk_v066_signal(assets, revenue):
    res = ((revenue / assets).rolling(126).skew()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc066_126d_jerk_v066_signal'] = f57at_f57_asset_turnover_velocity_calc066_126d_jerk_v066_signal

def f57at_f57_asset_turnover_velocity_calc067_10d_jerk_v067_signal(assets, netinc):
    res = (np.log((netinc / assets).abs().replace(0, np.nan)).rolling(10).std()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc067_10d_jerk_v067_signal'] = f57at_f57_asset_turnover_velocity_calc067_10d_jerk_v067_signal

def f57at_f57_asset_turnover_velocity_calc068_5d_jerk_v068_signal(equity, gp):
    res = ((gp / equity).rolling(5).skew()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc068_5d_jerk_v068_signal'] = f57at_f57_asset_turnover_velocity_calc068_5d_jerk_v068_signal

def f57at_f57_asset_turnover_velocity_calc069_10d_jerk_v069_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).rolling(10).var()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc069_10d_jerk_v069_signal'] = f57at_f57_asset_turnover_velocity_calc069_10d_jerk_v069_signal

def f57at_f57_asset_turnover_velocity_calc070_252d_jerk_v070_signal(assets, opinc):
    res = ((opinc / assets).rolling(252).mean()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc070_252d_jerk_v070_signal'] = f57at_f57_asset_turnover_velocity_calc070_252d_jerk_v070_signal

def f57at_f57_asset_turnover_velocity_calc071_21d_jerk_v071_signal(equity, revenue):
    res = ((revenue / equity).rolling(21).max()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc071_21d_jerk_v071_signal'] = f57at_f57_asset_turnover_velocity_calc071_21d_jerk_v071_signal

def f57at_f57_asset_turnover_velocity_calc072_5d_jerk_v072_signal(assets, gp):
    res = ((gp / assets).rolling(5).rank(pct=True)).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc072_5d_jerk_v072_signal'] = f57at_f57_asset_turnover_velocity_calc072_5d_jerk_v072_signal

def f57at_f57_asset_turnover_velocity_calc073_21d_jerk_v073_signal(assets, fcf):
    res = ((fcf / assets).rolling(21).kurt()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc073_21d_jerk_v073_signal'] = f57at_f57_asset_turnover_velocity_calc073_21d_jerk_v073_signal

def f57at_f57_asset_turnover_velocity_calc074_42d_jerk_v074_signal(equity, revenue):
    res = ((revenue / equity).rolling(42).skew()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc074_42d_jerk_v074_signal'] = f57at_f57_asset_turnover_velocity_calc074_42d_jerk_v074_signal

def f57at_f57_asset_turnover_velocity_calc075_252d_jerk_v075_signal(revenue, workingcapital):
    res = (np.log((revenue / workingcapital).abs().replace(0, np.nan)).rolling(252).std()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc075_252d_jerk_v075_signal'] = f57at_f57_asset_turnover_velocity_calc075_252d_jerk_v075_signal

def f57at_f57_asset_turnover_velocity_calc076_126d_jerk_v076_signal(capex, revenue):
    res = (((revenue / capex) / (revenue / capex).rolling(126).min())).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc076_126d_jerk_v076_signal'] = f57at_f57_asset_turnover_velocity_calc076_126d_jerk_v076_signal

def f57at_f57_asset_turnover_velocity_calc077_42d_jerk_v077_signal(assets, netinc):
    res = ((netinc / assets).rolling(42).std()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc077_42d_jerk_v077_signal'] = f57at_f57_asset_turnover_velocity_calc077_42d_jerk_v077_signal

def f57at_f57_asset_turnover_velocity_calc078_42d_jerk_v078_signal(assets, revenue):
    res = ((revenue / assets).rolling(42).max()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc078_42d_jerk_v078_signal'] = f57at_f57_asset_turnover_velocity_calc078_42d_jerk_v078_signal

def f57at_f57_asset_turnover_velocity_calc079_5d_jerk_v079_signal(assets, revenue):
    res = ((revenue / assets).rolling(5).skew()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc079_5d_jerk_v079_signal'] = f57at_f57_asset_turnover_velocity_calc079_5d_jerk_v079_signal

def f57at_f57_asset_turnover_velocity_calc080_5d_jerk_v080_signal(assets, gp):
    res = (((gp / assets) - (gp / assets).rolling(5).mean()) / (gp / assets).rolling(5).std()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc080_5d_jerk_v080_signal'] = f57at_f57_asset_turnover_velocity_calc080_5d_jerk_v080_signal

def f57at_f57_asset_turnover_velocity_calc081_10d_jerk_v081_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).rolling(10).min()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc081_10d_jerk_v081_signal'] = f57at_f57_asset_turnover_velocity_calc081_10d_jerk_v081_signal

def f57at_f57_asset_turnover_velocity_calc082_5d_jerk_v082_signal(assets, netinc):
    res = ((netinc / assets).rolling(5).kurt()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc082_5d_jerk_v082_signal'] = f57at_f57_asset_turnover_velocity_calc082_5d_jerk_v082_signal

def f57at_f57_asset_turnover_velocity_calc083_63d_jerk_v083_signal(revenue, workingcapital):
    res = (((revenue / workingcapital) / (revenue / workingcapital).rolling(63).max())).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc083_63d_jerk_v083_signal'] = f57at_f57_asset_turnover_velocity_calc083_63d_jerk_v083_signal

def f57at_f57_asset_turnover_velocity_calc084_21d_jerk_v084_signal(capex, revenue):
    res = ((revenue / capex).rolling(21).max()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc084_21d_jerk_v084_signal'] = f57at_f57_asset_turnover_velocity_calc084_21d_jerk_v084_signal

def f57at_f57_asset_turnover_velocity_calc085_63d_jerk_v085_signal(assets, fcf):
    res = (np.log((fcf / assets).abs().replace(0, np.nan)).rolling(63).std()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc085_63d_jerk_v085_signal'] = f57at_f57_asset_turnover_velocity_calc085_63d_jerk_v085_signal

def f57at_f57_asset_turnover_velocity_calc086_21d_jerk_v086_signal(liabilities, revenue):
    res = ((revenue / liabilities).rolling(21).std()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc086_21d_jerk_v086_signal'] = f57at_f57_asset_turnover_velocity_calc086_21d_jerk_v086_signal

def f57at_f57_asset_turnover_velocity_calc087_21d_jerk_v087_signal(assets, opinc):
    res = ((opinc / assets).rolling(21).rank(pct=True)).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc087_21d_jerk_v087_signal'] = f57at_f57_asset_turnover_velocity_calc087_21d_jerk_v087_signal

def f57at_f57_asset_turnover_velocity_calc088_252d_jerk_v088_signal(capex, revenue):
    res = ((revenue / capex).rolling(252).max()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc088_252d_jerk_v088_signal'] = f57at_f57_asset_turnover_velocity_calc088_252d_jerk_v088_signal

def f57at_f57_asset_turnover_velocity_calc089_5d_jerk_v089_signal(assets, gp):
    res = ((gp / assets).rolling(5).skew()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc089_5d_jerk_v089_signal'] = f57at_f57_asset_turnover_velocity_calc089_5d_jerk_v089_signal

def f57at_f57_asset_turnover_velocity_calc090_5d_jerk_v090_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).rolling(5).quantile(0.5)).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc090_5d_jerk_v090_signal'] = f57at_f57_asset_turnover_velocity_calc090_5d_jerk_v090_signal

def f57at_f57_asset_turnover_velocity_calc091_42d_jerk_v091_signal(assets, fcf):
    res = ((fcf / assets).rolling(42).var()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc091_42d_jerk_v091_signal'] = f57at_f57_asset_turnover_velocity_calc091_42d_jerk_v091_signal

def f57at_f57_asset_turnover_velocity_calc092_126d_jerk_v092_signal(liabilities, revenue):
    res = ((revenue / liabilities).rolling(126).quantile(0.5)).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc092_126d_jerk_v092_signal'] = f57at_f57_asset_turnover_velocity_calc092_126d_jerk_v092_signal

def f57at_f57_asset_turnover_velocity_calc093_126d_jerk_v093_signal(liabilities, revenue):
    res = ((revenue / liabilities).rolling(126).kurt()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc093_126d_jerk_v093_signal'] = f57at_f57_asset_turnover_velocity_calc093_126d_jerk_v093_signal

def f57at_f57_asset_turnover_velocity_calc094_63d_jerk_v094_signal(capex, revenue):
    res = ((revenue / capex).rolling(63).min()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc094_63d_jerk_v094_signal'] = f57at_f57_asset_turnover_velocity_calc094_63d_jerk_v094_signal

def f57at_f57_asset_turnover_velocity_calc095_42d_jerk_v095_signal(assets, fcf):
    res = ((fcf / assets).diff(42)).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc095_42d_jerk_v095_signal'] = f57at_f57_asset_turnover_velocity_calc095_42d_jerk_v095_signal

def f57at_f57_asset_turnover_velocity_calc096_63d_jerk_v096_signal(liabilities, revenue):
    res = ((revenue / liabilities).pct_change(63)).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc096_63d_jerk_v096_signal'] = f57at_f57_asset_turnover_velocity_calc096_63d_jerk_v096_signal

def f57at_f57_asset_turnover_velocity_calc097_10d_jerk_v097_signal(assets, gp):
    res = (((gp / assets) / (gp / assets).rolling(10).max())).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc097_10d_jerk_v097_signal'] = f57at_f57_asset_turnover_velocity_calc097_10d_jerk_v097_signal

def f57at_f57_asset_turnover_velocity_calc098_21d_jerk_v098_signal(revenue, workingcapital):
    res = (((revenue / workingcapital) - (revenue / workingcapital).rolling(21).mean()) / (revenue / workingcapital).rolling(21).std()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc098_21d_jerk_v098_signal'] = f57at_f57_asset_turnover_velocity_calc098_21d_jerk_v098_signal

def f57at_f57_asset_turnover_velocity_calc099_10d_jerk_v099_signal(assets, revenue):
    res = ((revenue / assets).rolling(10).min()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc099_10d_jerk_v099_signal'] = f57at_f57_asset_turnover_velocity_calc099_10d_jerk_v099_signal

def f57at_f57_asset_turnover_velocity_calc100_10d_jerk_v100_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).rolling(10).max()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc100_10d_jerk_v100_signal'] = f57at_f57_asset_turnover_velocity_calc100_10d_jerk_v100_signal

def f57at_f57_asset_turnover_velocity_calc101_126d_jerk_v101_signal(equity, gp):
    res = ((gp / equity).rolling(126).skew()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc101_126d_jerk_v101_signal'] = f57at_f57_asset_turnover_velocity_calc101_126d_jerk_v101_signal

def f57at_f57_asset_turnover_velocity_calc102_10d_jerk_v102_signal(assets, gp):
    res = ((gp / assets).diff(10)).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc102_10d_jerk_v102_signal'] = f57at_f57_asset_turnover_velocity_calc102_10d_jerk_v102_signal

def f57at_f57_asset_turnover_velocity_calc103_252d_jerk_v103_signal(assets, opinc):
    res = ((opinc / assets).rolling(252).max()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc103_252d_jerk_v103_signal'] = f57at_f57_asset_turnover_velocity_calc103_252d_jerk_v103_signal

def f57at_f57_asset_turnover_velocity_calc104_10d_jerk_v104_signal(equity, gp):
    res = ((gp / equity).rolling(10).skew()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc104_10d_jerk_v104_signal'] = f57at_f57_asset_turnover_velocity_calc104_10d_jerk_v104_signal

def f57at_f57_asset_turnover_velocity_calc105_252d_jerk_v105_signal(equity, revenue):
    res = (((revenue / equity) / (revenue / equity).rolling(252).max())).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc105_252d_jerk_v105_signal'] = f57at_f57_asset_turnover_velocity_calc105_252d_jerk_v105_signal

def f57at_f57_asset_turnover_velocity_calc106_63d_jerk_v106_signal(equity, revenue):
    res = ((revenue / equity).rolling(63).max()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc106_63d_jerk_v106_signal'] = f57at_f57_asset_turnover_velocity_calc106_63d_jerk_v106_signal

def f57at_f57_asset_turnover_velocity_calc107_126d_jerk_v107_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).rolling(126).std()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc107_126d_jerk_v107_signal'] = f57at_f57_asset_turnover_velocity_calc107_126d_jerk_v107_signal

def f57at_f57_asset_turnover_velocity_calc108_21d_jerk_v108_signal(liabilities, revenue):
    res = ((revenue / liabilities).diff(21)).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc108_21d_jerk_v108_signal'] = f57at_f57_asset_turnover_velocity_calc108_21d_jerk_v108_signal

def f57at_f57_asset_turnover_velocity_calc109_63d_jerk_v109_signal(equity, gp):
    res = (np.log((gp / equity).abs().replace(0, np.nan)).rolling(63).std()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc109_63d_jerk_v109_signal'] = f57at_f57_asset_turnover_velocity_calc109_63d_jerk_v109_signal

def f57at_f57_asset_turnover_velocity_calc110_10d_jerk_v110_signal(equity, revenue):
    res = ((revenue / equity).rolling(10).skew()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc110_10d_jerk_v110_signal'] = f57at_f57_asset_turnover_velocity_calc110_10d_jerk_v110_signal

def f57at_f57_asset_turnover_velocity_calc111_63d_jerk_v111_signal(equity, revenue):
    res = ((revenue / equity).rolling(63).std()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc111_63d_jerk_v111_signal'] = f57at_f57_asset_turnover_velocity_calc111_63d_jerk_v111_signal

def f57at_f57_asset_turnover_velocity_calc112_21d_jerk_v112_signal(assets, netinc):
    res = ((netinc / assets).rolling(21).max()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc112_21d_jerk_v112_signal'] = f57at_f57_asset_turnover_velocity_calc112_21d_jerk_v112_signal

def f57at_f57_asset_turnover_velocity_calc113_252d_jerk_v113_signal(assets, gp):
    res = ((gp / assets).rolling(252).var()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc113_252d_jerk_v113_signal'] = f57at_f57_asset_turnover_velocity_calc113_252d_jerk_v113_signal

def f57at_f57_asset_turnover_velocity_calc114_21d_jerk_v114_signal(assets, opinc):
    res = (((opinc / assets) / (opinc / assets).rolling(21).max())).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc114_21d_jerk_v114_signal'] = f57at_f57_asset_turnover_velocity_calc114_21d_jerk_v114_signal

def f57at_f57_asset_turnover_velocity_calc115_10d_jerk_v115_signal(capex, revenue):
    res = ((revenue / capex).rolling(10).kurt()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc115_10d_jerk_v115_signal'] = f57at_f57_asset_turnover_velocity_calc115_10d_jerk_v115_signal

def f57at_f57_asset_turnover_velocity_calc116_252d_jerk_v116_signal(capex, revenue):
    res = (np.log((revenue / capex).abs().replace(0, np.nan)).rolling(252).std()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc116_252d_jerk_v116_signal'] = f57at_f57_asset_turnover_velocity_calc116_252d_jerk_v116_signal

def f57at_f57_asset_turnover_velocity_calc117_5d_jerk_v117_signal(equity, gp):
    res = ((gp / equity).pct_change(5)).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc117_5d_jerk_v117_signal'] = f57at_f57_asset_turnover_velocity_calc117_5d_jerk_v117_signal

def f57at_f57_asset_turnover_velocity_calc118_21d_jerk_v118_signal(capex, revenue):
    res = ((revenue / capex).rolling(21).min()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc118_21d_jerk_v118_signal'] = f57at_f57_asset_turnover_velocity_calc118_21d_jerk_v118_signal

def f57at_f57_asset_turnover_velocity_calc119_21d_jerk_v119_signal(assets, netinc):
    res = ((netinc / assets).pct_change(21)).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc119_21d_jerk_v119_signal'] = f57at_f57_asset_turnover_velocity_calc119_21d_jerk_v119_signal

def f57at_f57_asset_turnover_velocity_calc120_42d_jerk_v120_signal(capex, revenue):
    res = ((revenue / capex).rolling(42).min()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc120_42d_jerk_v120_signal'] = f57at_f57_asset_turnover_velocity_calc120_42d_jerk_v120_signal

def f57at_f57_asset_turnover_velocity_calc121_5d_jerk_v121_signal(capex, revenue):
    res = ((revenue / capex).rolling(5).min()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc121_5d_jerk_v121_signal'] = f57at_f57_asset_turnover_velocity_calc121_5d_jerk_v121_signal

def f57at_f57_asset_turnover_velocity_calc122_252d_jerk_v122_signal(equity, revenue):
    res = ((revenue / equity).rolling(252).mean()).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc122_252d_jerk_v122_signal'] = f57at_f57_asset_turnover_velocity_calc122_252d_jerk_v122_signal

def f57at_f57_asset_turnover_velocity_calc123_126d_jerk_v123_signal(capex, revenue):
    res = ((revenue / capex).rolling(126).min()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc123_126d_jerk_v123_signal'] = f57at_f57_asset_turnover_velocity_calc123_126d_jerk_v123_signal

def f57at_f57_asset_turnover_velocity_calc124_21d_jerk_v124_signal(equity, revenue):
    res = ((revenue / equity).pct_change(21)).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc124_21d_jerk_v124_signal'] = f57at_f57_asset_turnover_velocity_calc124_21d_jerk_v124_signal

def f57at_f57_asset_turnover_velocity_calc125_42d_jerk_v125_signal(equity, gp):
    res = ((gp / equity).rolling(42).std()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc125_42d_jerk_v125_signal'] = f57at_f57_asset_turnover_velocity_calc125_42d_jerk_v125_signal

def f57at_f57_asset_turnover_velocity_calc126_5d_jerk_v126_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).rolling(5).max()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc126_5d_jerk_v126_signal'] = f57at_f57_asset_turnover_velocity_calc126_5d_jerk_v126_signal

def f57at_f57_asset_turnover_velocity_calc127_21d_jerk_v127_signal(equity, gp):
    res = ((gp / equity).rolling(21).rank(pct=True)).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc127_21d_jerk_v127_signal'] = f57at_f57_asset_turnover_velocity_calc127_21d_jerk_v127_signal

def f57at_f57_asset_turnover_velocity_calc128_21d_jerk_v128_signal(capex, revenue):
    res = ((revenue / capex).pct_change(21)).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc128_21d_jerk_v128_signal'] = f57at_f57_asset_turnover_velocity_calc128_21d_jerk_v128_signal

def f57at_f57_asset_turnover_velocity_calc129_5d_jerk_v129_signal(assets, revenue):
    res = (((revenue / assets) / (revenue / assets).rolling(5).min())).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc129_5d_jerk_v129_signal'] = f57at_f57_asset_turnover_velocity_calc129_5d_jerk_v129_signal

def f57at_f57_asset_turnover_velocity_calc130_10d_jerk_v130_signal(assets, fcf):
    res = ((fcf / assets).diff(10)).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc130_10d_jerk_v130_signal'] = f57at_f57_asset_turnover_velocity_calc130_10d_jerk_v130_signal

def f57at_f57_asset_turnover_velocity_calc131_42d_jerk_v131_signal(liabilities, revenue):
    res = ((revenue / liabilities).rolling(42).kurt()).diff(1).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc131_42d_jerk_v131_signal'] = f57at_f57_asset_turnover_velocity_calc131_42d_jerk_v131_signal

def f57at_f57_asset_turnover_velocity_calc132_63d_jerk_v132_signal(equity, revenue):
    res = ((revenue / equity).pct_change(63)).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc132_63d_jerk_v132_signal'] = f57at_f57_asset_turnover_velocity_calc132_63d_jerk_v132_signal

def f57at_f57_asset_turnover_velocity_calc133_5d_jerk_v133_signal(equity, gp):
    res = (((gp / equity) - (gp / equity).rolling(5).mean()) / (gp / equity).rolling(5).std()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc133_5d_jerk_v133_signal'] = f57at_f57_asset_turnover_velocity_calc133_5d_jerk_v133_signal

def f57at_f57_asset_turnover_velocity_calc134_126d_jerk_v134_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).rolling(126).rank(pct=True)).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc134_126d_jerk_v134_signal'] = f57at_f57_asset_turnover_velocity_calc134_126d_jerk_v134_signal

def f57at_f57_asset_turnover_velocity_calc135_21d_jerk_v135_signal(equity, revenue):
    res = ((revenue / equity).rolling(21).mean()).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc135_21d_jerk_v135_signal'] = f57at_f57_asset_turnover_velocity_calc135_21d_jerk_v135_signal

def f57at_f57_asset_turnover_velocity_calc136_5d_jerk_v136_signal(equity, revenue):
    res = (((revenue / equity) / (revenue / equity).rolling(5).min())).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc136_5d_jerk_v136_signal'] = f57at_f57_asset_turnover_velocity_calc136_5d_jerk_v136_signal

def f57at_f57_asset_turnover_velocity_calc137_10d_jerk_v137_signal(equity, revenue):
    res = ((revenue / equity).rolling(10).mean()).diff(1).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc137_10d_jerk_v137_signal'] = f57at_f57_asset_turnover_velocity_calc137_10d_jerk_v137_signal

def f57at_f57_asset_turnover_velocity_calc138_5d_jerk_v138_signal(capex, revenue):
    res = ((revenue / capex).rolling(5).skew()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc138_5d_jerk_v138_signal'] = f57at_f57_asset_turnover_velocity_calc138_5d_jerk_v138_signal

def f57at_f57_asset_turnover_velocity_calc139_5d_jerk_v139_signal(assets, fcf):
    res = ((fcf / assets).rolling(5).skew()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc139_5d_jerk_v139_signal'] = f57at_f57_asset_turnover_velocity_calc139_5d_jerk_v139_signal

def f57at_f57_asset_turnover_velocity_calc140_5d_jerk_v140_signal(revenue, workingcapital):
    res = (((revenue / workingcapital) / (revenue / workingcapital).rolling(5).min())).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc140_5d_jerk_v140_signal'] = f57at_f57_asset_turnover_velocity_calc140_5d_jerk_v140_signal

def f57at_f57_asset_turnover_velocity_calc141_5d_jerk_v141_signal(revenue, workingcapital):
    res = (((revenue / workingcapital) - (revenue / workingcapital).rolling(5).mean()) / (revenue / workingcapital).rolling(5).std()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc141_5d_jerk_v141_signal'] = f57at_f57_asset_turnover_velocity_calc141_5d_jerk_v141_signal

def f57at_f57_asset_turnover_velocity_calc142_21d_jerk_v142_signal(assets, fcf):
    res = ((fcf / assets).rolling(21).quantile(0.5)).diff(1).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc142_21d_jerk_v142_signal'] = f57at_f57_asset_turnover_velocity_calc142_21d_jerk_v142_signal

def f57at_f57_asset_turnover_velocity_calc143_126d_jerk_v143_signal(capex, revenue):
    res = ((revenue / capex).rolling(126).skew()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc143_126d_jerk_v143_signal'] = f57at_f57_asset_turnover_velocity_calc143_126d_jerk_v143_signal

def f57at_f57_asset_turnover_velocity_calc144_63d_jerk_v144_signal(equity, gp):
    res = ((gp / equity).rolling(63).kurt()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc144_63d_jerk_v144_signal'] = f57at_f57_asset_turnover_velocity_calc144_63d_jerk_v144_signal

def f57at_f57_asset_turnover_velocity_calc145_252d_jerk_v145_signal(assets, fcf):
    res = ((fcf / assets).rolling(252).rank(pct=True)).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc145_252d_jerk_v145_signal'] = f57at_f57_asset_turnover_velocity_calc145_252d_jerk_v145_signal

def f57at_f57_asset_turnover_velocity_calc146_63d_jerk_v146_signal(assets, revenue):
    res = (((revenue / assets) / (revenue / assets).rolling(63).max())).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc146_63d_jerk_v146_signal'] = f57at_f57_asset_turnover_velocity_calc146_63d_jerk_v146_signal

def f57at_f57_asset_turnover_velocity_calc147_126d_jerk_v147_signal(equity, revenue):
    res = ((revenue / equity).rolling(126).var()).diff(1).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc147_126d_jerk_v147_signal'] = f57at_f57_asset_turnover_velocity_calc147_126d_jerk_v147_signal

def f57at_f57_asset_turnover_velocity_calc148_63d_jerk_v148_signal(assets, fcf):
    res = ((fcf / assets).rolling(63).min()).diff(1).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc148_63d_jerk_v148_signal'] = f57at_f57_asset_turnover_velocity_calc148_63d_jerk_v148_signal

def f57at_f57_asset_turnover_velocity_calc149_252d_jerk_v149_signal(capex, revenue):
    res = (((revenue / capex) / (revenue / capex).rolling(252).min())).diff(1).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc149_252d_jerk_v149_signal'] = f57at_f57_asset_turnover_velocity_calc149_252d_jerk_v149_signal

def f57at_f57_asset_turnover_velocity_calc150_5d_jerk_v150_signal(assets, fcf):
    res = ((fcf / assets).rolling(5).max()).diff(1).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f57at_f57_asset_turnover_velocity_calc150_5d_jerk_v150_signal'] = f57at_f57_asset_turnover_velocity_calc150_5d_jerk_v150_signal


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
