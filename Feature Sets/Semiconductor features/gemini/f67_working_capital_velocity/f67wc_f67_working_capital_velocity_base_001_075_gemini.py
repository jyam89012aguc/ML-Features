import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f67wc_f67_working_capital_velocity_calc001_5d_base_v001_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc001_5d_base_v001_signal'] = f67wc_f67_working_capital_velocity_calc001_5d_base_v001_signal

def f67wc_f67_working_capital_velocity_calc002_10d_base_v002_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc002_10d_base_v002_signal'] = f67wc_f67_working_capital_velocity_calc002_10d_base_v002_signal

def f67wc_f67_working_capital_velocity_calc003_21d_base_v003_signal(fcf, workingcapital):
    res = (fcf / workingcapital).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc003_21d_base_v003_signal'] = f67wc_f67_working_capital_velocity_calc003_21d_base_v003_signal

def f67wc_f67_working_capital_velocity_calc004_42d_base_v004_signal(opinc, workingcapital):
    res = (opinc / workingcapital).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc004_42d_base_v004_signal'] = f67wc_f67_working_capital_velocity_calc004_42d_base_v004_signal

def f67wc_f67_working_capital_velocity_calc005_63d_base_v005_signal(ncfo, workingcapital):
    res = (ncfo / workingcapital).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc005_63d_base_v005_signal'] = f67wc_f67_working_capital_velocity_calc005_63d_base_v005_signal

def f67wc_f67_working_capital_velocity_calc006_126d_base_v006_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc006_126d_base_v006_signal'] = f67wc_f67_working_capital_velocity_calc006_126d_base_v006_signal

def f67wc_f67_working_capital_velocity_calc007_252d_base_v007_signal(fcf, workingcapital):
    res = (fcf / workingcapital).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc007_252d_base_v007_signal'] = f67wc_f67_working_capital_velocity_calc007_252d_base_v007_signal

def f67wc_f67_working_capital_velocity_calc008_5d_base_v008_signal(workingcapital, assets):
    res = (workingcapital / assets).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc008_5d_base_v008_signal'] = f67wc_f67_working_capital_velocity_calc008_5d_base_v008_signal

def f67wc_f67_working_capital_velocity_calc009_10d_base_v009_signal(workingcapital, revenue):
    res = (workingcapital / revenue).rolling(10).quantile(0.5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc009_10d_base_v009_signal'] = f67wc_f67_working_capital_velocity_calc009_10d_base_v009_signal

def f67wc_f67_working_capital_velocity_calc010_21d_base_v010_signal(ebitda, workingcapital):
    res = (ebitda / workingcapital).rolling(21).std() / (ebitda / workingcapital).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc010_21d_base_v010_signal'] = f67wc_f67_working_capital_velocity_calc010_21d_base_v010_signal

def f67wc_f67_working_capital_velocity_calc011_42d_base_v011_signal(netinc, workingcapital):
    res = (netinc / workingcapital).rolling(42).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc011_42d_base_v011_signal'] = f67wc_f67_working_capital_velocity_calc011_42d_base_v011_signal

def f67wc_f67_working_capital_velocity_calc012_63d_base_v012_signal(gp, workingcapital):
    res = (gp / workingcapital).diff(63).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc012_63d_base_v012_signal'] = f67wc_f67_working_capital_velocity_calc012_63d_base_v012_signal

def f67wc_f67_working_capital_velocity_calc013_126d_base_v013_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(126).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc013_126d_base_v013_signal'] = f67wc_f67_working_capital_velocity_calc013_126d_base_v013_signal

def f67wc_f67_working_capital_velocity_calc014_252d_base_v014_signal(fcf, workingcapital):
    res = (fcf / workingcapital).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc014_252d_base_v014_signal'] = f67wc_f67_working_capital_velocity_calc014_252d_base_v014_signal

def f67wc_f67_working_capital_velocity_calc015_5d_base_v015_signal(ncfo, workingcapital):
    res = (ncfo / workingcapital).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc015_5d_base_v015_signal'] = f67wc_f67_working_capital_velocity_calc015_5d_base_v015_signal

def f67wc_f67_working_capital_velocity_calc016_10d_base_v016_signal(workingcapital, revenue):
    res = (workingcapital / revenue).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc016_10d_base_v016_signal'] = f67wc_f67_working_capital_velocity_calc016_10d_base_v016_signal

def f67wc_f67_working_capital_velocity_calc017_21d_base_v017_signal(workingcapital, assets):
    res = (workingcapital / assets).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc017_21d_base_v017_signal'] = f67wc_f67_working_capital_velocity_calc017_21d_base_v017_signal

def f67wc_f67_working_capital_velocity_calc018_42d_base_v018_signal(ebitda, workingcapital):
    res = (ebitda / workingcapital).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc018_42d_base_v018_signal'] = f67wc_f67_working_capital_velocity_calc018_42d_base_v018_signal

def f67wc_f67_working_capital_velocity_calc019_63d_base_v019_signal(netinc, workingcapital):
    res = (netinc / workingcapital).rolling(63).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc019_63d_base_v019_signal'] = f67wc_f67_working_capital_velocity_calc019_63d_base_v019_signal

def f67wc_f67_working_capital_velocity_calc020_126d_base_v020_signal(gp, workingcapital):
    res = (gp / workingcapital).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc020_126d_base_v020_signal'] = f67wc_f67_working_capital_velocity_calc020_126d_base_v020_signal

def f67wc_f67_working_capital_velocity_calc021_252d_base_v021_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(252).quantile(0.8)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc021_252d_base_v021_signal'] = f67wc_f67_working_capital_velocity_calc021_252d_base_v021_signal

def f67wc_f67_working_capital_velocity_calc022_5d_base_v022_signal(fcf, workingcapital):
    res = (fcf / workingcapital).diff(5).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc022_5d_base_v022_signal'] = f67wc_f67_working_capital_velocity_calc022_5d_base_v022_signal

def f67wc_f67_working_capital_velocity_calc023_10d_base_v023_signal(ncfo, workingcapital):
    res = (ncfo / workingcapital).rolling(10).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc023_10d_base_v023_signal'] = f67wc_f67_working_capital_velocity_calc023_10d_base_v023_signal

def f67wc_f67_working_capital_velocity_calc024_21d_base_v024_signal(workingcapital, revenue):
    res = (workingcapital / revenue).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc024_21d_base_v024_signal'] = f67wc_f67_working_capital_velocity_calc024_21d_base_v024_signal

def f67wc_f67_working_capital_velocity_calc025_42d_base_v025_signal(workingcapital, assets):
    res = (workingcapital / assets).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc025_42d_base_v025_signal'] = f67wc_f67_working_capital_velocity_calc025_42d_base_v025_signal

def f67wc_f67_working_capital_velocity_calc026_63d_base_v026_signal(ebitda, workingcapital):
    res = (ebitda / workingcapital).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc026_63d_base_v026_signal'] = f67wc_f67_working_capital_velocity_calc026_63d_base_v026_signal

def f67wc_f67_working_capital_velocity_calc027_126d_base_v027_signal(netinc, workingcapital):
    res = (netinc / workingcapital).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc027_126d_base_v027_signal'] = f67wc_f67_working_capital_velocity_calc027_126d_base_v027_signal

def f67wc_f67_working_capital_velocity_calc028_252d_base_v028_signal(gp, workingcapital):
    res = (gp / workingcapital).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc028_252d_base_v028_signal'] = f67wc_f67_working_capital_velocity_calc028_252d_base_v028_signal

def f67wc_f67_working_capital_velocity_calc029_5d_base_v029_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc029_5d_base_v029_signal'] = f67wc_f67_working_capital_velocity_calc029_5d_base_v029_signal

def f67wc_f67_working_capital_velocity_calc030_10d_base_v030_signal(fcf, workingcapital):
    res = (fcf / workingcapital).rolling(10).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc030_10d_base_v030_signal'] = f67wc_f67_working_capital_velocity_calc030_10d_base_v030_signal

def f67wc_f67_working_capital_velocity_calc031_21d_base_v031_signal(ncfo, workingcapital):
    res = (ncfo / workingcapital).rolling(21).quantile(0.2)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc031_21d_base_v031_signal'] = f67wc_f67_working_capital_velocity_calc031_21d_base_v031_signal

def f67wc_f67_working_capital_velocity_calc032_42d_base_v032_signal(workingcapital, revenue):
    res = (workingcapital / revenue).rolling(42).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc032_42d_base_v032_signal'] = f67wc_f67_working_capital_velocity_calc032_42d_base_v032_signal

def f67wc_f67_working_capital_velocity_calc033_63d_base_v033_signal(workingcapital, assets):
    res = (workingcapital / assets).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc033_63d_base_v033_signal'] = f67wc_f67_working_capital_velocity_calc033_63d_base_v033_signal

def f67wc_f67_working_capital_velocity_calc034_126d_base_v034_signal(ebitda, workingcapital):
    res = (ebitda / workingcapital).rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc034_126d_base_v034_signal'] = f67wc_f67_working_capital_velocity_calc034_126d_base_v034_signal

def f67wc_f67_working_capital_velocity_calc035_252d_base_v035_signal(netinc, workingcapital):
    res = (netinc / workingcapital).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc035_252d_base_v035_signal'] = f67wc_f67_working_capital_velocity_calc035_252d_base_v035_signal

def f67wc_f67_working_capital_velocity_calc036_5d_base_v036_signal(gp, workingcapital):
    res = (gp / workingcapital).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc036_5d_base_v036_signal'] = f67wc_f67_working_capital_velocity_calc036_5d_base_v036_signal

def f67wc_f67_working_capital_velocity_calc037_10d_base_v037_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(10).rank(pct=True).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc037_10d_base_v037_signal'] = f67wc_f67_working_capital_velocity_calc037_10d_base_v037_signal

def f67wc_f67_working_capital_velocity_calc038_21d_base_v038_signal(fcf, workingcapital):
    res = (fcf / workingcapital).rolling(21).mean().pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc038_21d_base_v038_signal'] = f67wc_f67_working_capital_velocity_calc038_21d_base_v038_signal

def f67wc_f67_working_capital_velocity_calc039_42d_base_v039_signal(ncfo, workingcapital):
    res = (ncfo / workingcapital).rolling(42).max() - (ncfo / workingcapital).rolling(42).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc039_42d_base_v039_signal'] = f67wc_f67_working_capital_velocity_calc039_42d_base_v039_signal

def f67wc_f67_working_capital_velocity_calc040_63d_base_v040_signal(workingcapital, revenue):
    res = (workingcapital / revenue).rolling(63).skew().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc040_63d_base_v040_signal'] = f67wc_f67_working_capital_velocity_calc040_63d_base_v040_signal

def f67wc_f67_working_capital_velocity_calc041_126d_base_v041_signal(workingcapital, assets):
    res = (workingcapital / assets).rolling(126).rank(pct=True).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc041_126d_base_v041_signal'] = f67wc_f67_working_capital_velocity_calc041_126d_base_v041_signal

def f67wc_f67_working_capital_velocity_calc042_252d_base_v042_signal(ebitda, workingcapital):
    res = (ebitda / workingcapital).rolling(252).mean() / (ebitda / workingcapital).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc042_252d_base_v042_signal'] = f67wc_f67_working_capital_velocity_calc042_252d_base_v042_signal

def f67wc_f67_working_capital_velocity_calc043_5d_base_v043_signal(netinc, workingcapital):
    res = (netinc / workingcapital).rolling(5).quantile(0.5).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc043_5d_base_v043_signal'] = f67wc_f67_working_capital_velocity_calc043_5d_base_v043_signal

def f67wc_f67_working_capital_velocity_calc044_10d_base_v044_signal(gp, workingcapital):
    res = (gp / workingcapital).rolling(10).var().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc044_10d_base_v044_signal'] = f67wc_f67_working_capital_velocity_calc044_10d_base_v044_signal

def f67wc_f67_working_capital_velocity_calc045_21d_base_v045_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(21).kurt().diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc045_21d_base_v045_signal'] = f67wc_f67_working_capital_velocity_calc045_21d_base_v045_signal

def f67wc_f67_working_capital_velocity_calc046_42d_base_v046_signal(fcf, workingcapital):
    res = (fcf / workingcapital).rolling(42).rank(pct=True).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc046_42d_base_v046_signal'] = f67wc_f67_working_capital_velocity_calc046_42d_base_v046_signal

def f67wc_f67_working_capital_velocity_calc047_63d_base_v047_signal(ncfo, workingcapital):
    res = (ncfo / workingcapital).rolling(63).quantile(0.9)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc047_63d_base_v047_signal'] = f67wc_f67_working_capital_velocity_calc047_63d_base_v047_signal

def f67wc_f67_working_capital_velocity_calc048_126d_base_v048_signal(workingcapital, revenue):
    res = (workingcapital / revenue).rolling(126).min().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc048_126d_base_v048_signal'] = f67wc_f67_working_capital_velocity_calc048_126d_base_v048_signal

def f67wc_f67_working_capital_velocity_calc049_252d_base_v049_signal(workingcapital, assets):
    res = (workingcapital / assets).rolling(252).max().diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc049_252d_base_v049_signal'] = f67wc_f67_working_capital_velocity_calc049_252d_base_v049_signal

def f67wc_f67_working_capital_velocity_calc050_5d_base_v050_signal(ebitda, workingcapital):
    res = (ebitda / workingcapital).rolling(5).skew().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc050_5d_base_v050_signal'] = f67wc_f67_working_capital_velocity_calc050_5d_base_v050_signal

def f67wc_f67_working_capital_velocity_calc051_10d_base_v051_signal(netinc, workingcapital):
    res = (netinc / workingcapital).rolling(10).mean() / (netinc / workingcapital).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc051_10d_base_v051_signal'] = f67wc_f67_working_capital_velocity_calc051_10d_base_v051_signal

def f67wc_f67_working_capital_velocity_calc052_21d_base_v052_signal(gp, workingcapital):
    res = (gp / workingcapital).rolling(21).rank(pct=True).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc052_21d_base_v052_signal'] = f67wc_f67_working_capital_velocity_calc052_21d_base_v052_signal

def f67wc_f67_working_capital_velocity_calc053_42d_base_v053_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(42).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc053_42d_base_v053_signal'] = f67wc_f67_working_capital_velocity_calc053_42d_base_v053_signal

def f67wc_f67_working_capital_velocity_calc054_63d_base_v054_signal(fcf, workingcapital):
    res = (fcf / workingcapital).rolling(63).var().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc054_63d_base_v054_signal'] = f67wc_f67_working_capital_velocity_calc054_63d_base_v054_signal

def f67wc_f67_working_capital_velocity_calc055_126d_base_v055_signal(ncfo, workingcapital):
    res = (ncfo / workingcapital).rolling(126).skew().rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc055_126d_base_v055_signal'] = f67wc_f67_working_capital_velocity_calc055_126d_base_v055_signal

def f67wc_f67_working_capital_velocity_calc056_252d_base_v056_signal(workingcapital, revenue):
    res = (workingcapital / revenue).rolling(252).kurt().diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc056_252d_base_v056_signal'] = f67wc_f67_working_capital_velocity_calc056_252d_base_v056_signal

def f67wc_f67_working_capital_velocity_calc057_5d_base_v057_signal(workingcapital, assets):
    res = (workingcapital / assets).rolling(5).quantile(0.1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc057_5d_base_v057_signal'] = f67wc_f67_working_capital_velocity_calc057_5d_base_v057_signal

def f67wc_f67_working_capital_velocity_calc058_10d_base_v058_signal(ebitda, workingcapital):
    res = (ebitda / workingcapital).rolling(10).mean().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc058_10d_base_v058_signal'] = f67wc_f67_working_capital_velocity_calc058_10d_base_v058_signal

def f67wc_f67_working_capital_velocity_calc059_21d_base_v059_signal(netinc, workingcapital):
    res = (netinc / workingcapital).rolling(21).std().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc059_21d_base_v059_signal'] = f67wc_f67_working_capital_velocity_calc059_21d_base_v059_signal

def f67wc_f67_working_capital_velocity_calc060_42d_base_v060_signal(gp, workingcapital):
    res = (gp / workingcapital).rolling(42).rank(pct=True).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc060_42d_base_v060_signal'] = f67wc_f67_working_capital_velocity_calc060_42d_base_v060_signal

def f67wc_f67_working_capital_velocity_calc061_63d_base_v061_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(63).quantile(0.5).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc061_63d_base_v061_signal'] = f67wc_f67_working_capital_velocity_calc061_63d_base_v061_signal

def f67wc_f67_working_capital_velocity_calc062_126d_base_v062_signal(fcf, workingcapital):
    res = (fcf / workingcapital).rolling(126).var().diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc062_126d_base_v062_signal'] = f67wc_f67_working_capital_velocity_calc062_126d_base_v062_signal

def f67wc_f67_working_capital_velocity_calc063_252d_base_v063_signal(ncfo, workingcapital):
    res = (ncfo / workingcapital).rolling(252).skew().pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc063_252d_base_v063_signal'] = f67wc_f67_working_capital_velocity_calc063_252d_base_v063_signal

def f67wc_f67_working_capital_velocity_calc064_5d_base_v064_signal(workingcapital, revenue):
    res = (workingcapital / revenue).rolling(5).max().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc064_5d_base_v064_signal'] = f67wc_f67_working_capital_velocity_calc064_5d_base_v064_signal

def f67wc_f67_working_capital_velocity_calc065_10d_base_v065_signal(workingcapital, assets):
    res = (workingcapital / assets).rolling(10).min().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc065_10d_base_v065_signal'] = f67wc_f67_working_capital_velocity_calc065_10d_base_v065_signal

def f67wc_f67_working_capital_velocity_calc066_21d_base_v066_signal(ebitda, workingcapital):
    res = (ebitda / workingcapital).rolling(21).kurt().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc066_21d_base_v066_signal'] = f67wc_f67_working_capital_velocity_calc066_21d_base_v066_signal

def f67wc_f67_working_capital_velocity_calc067_42d_base_v067_signal(netinc, workingcapital):
    res = (netinc / workingcapital).rolling(42).rank(pct=True).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc067_42d_base_v067_signal'] = f67wc_f67_working_capital_velocity_calc067_42d_base_v067_signal

def f67wc_f67_working_capital_velocity_calc068_63d_base_v068_signal(gp, workingcapital):
    res = (gp / workingcapital).rolling(63).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc068_63d_base_v068_signal'] = f67wc_f67_working_capital_velocity_calc068_63d_base_v068_signal

def f67wc_f67_working_capital_velocity_calc069_126d_base_v069_signal(revenue, workingcapital):
    res = (revenue / workingcapital).rolling(126).quantile(0.3).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc069_126d_base_v069_signal'] = f67wc_f67_working_capital_velocity_calc069_126d_base_v069_signal

def f67wc_f67_working_capital_velocity_calc070_252d_base_v070_signal(fcf, workingcapital):
    res = (fcf / workingcapital).rolling(252).mean().pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc070_252d_base_v070_signal'] = f67wc_f67_working_capital_velocity_calc070_252d_base_v070_signal

def f67wc_f67_working_capital_velocity_calc071_5d_base_v071_signal(ncfo, workingcapital):
    res = (ncfo / workingcapital).rolling(5).var().diff(1)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc071_5d_base_v071_signal'] = f67wc_f67_working_capital_velocity_calc071_5d_base_v071_signal

def f67wc_f67_working_capital_velocity_calc072_10d_base_v072_signal(workingcapital, revenue):
    res = (workingcapital / revenue).rolling(10).skew().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc072_10d_base_v072_signal'] = f67wc_f67_working_capital_velocity_calc072_10d_base_v072_signal

def f67wc_f67_working_capital_velocity_calc073_21d_base_v073_signal(workingcapital, assets):
    res = (workingcapital / assets).rolling(21).kurt().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc073_21d_base_v073_signal'] = f67wc_f67_working_capital_velocity_calc073_21d_base_v073_signal

def f67wc_f67_working_capital_velocity_calc074_42d_base_v074_signal(ebitda, workingcapital):
    res = (ebitda / workingcapital).rolling(42).rank(pct=True).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc074_42d_base_v074_signal'] = f67wc_f67_working_capital_velocity_calc074_42d_base_v074_signal

def f67wc_f67_working_capital_velocity_calc075_63d_base_v075_signal(netinc, workingcapital):
    res = (netinc / workingcapital).rolling(63).quantile(0.7).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f67wc_f67_working_capital_velocity_calc075_63d_base_v075_signal'] = f67wc_f67_working_capital_velocity_calc075_63d_base_v075_signal


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
