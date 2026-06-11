import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f70le_f70_liabilities_to_equity_momentum_calc001_10d_base_v001_signal(liabilities, equity):
    res = (liabilities.rolling(10).mean() / equity.replace(0, np.nan).rolling(10).mean()).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc001_10d_base_v001_signal'] = f70le_f70_liabilities_to_equity_momentum_calc001_10d_base_v001_signal

def f70le_f70_liabilities_to_equity_momentum_calc002_21d_base_v002_signal(liabilities, equity):
    res = (liabilities.rolling(21).mean() / equity.replace(0, np.nan).rolling(21).mean()).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc002_21d_base_v002_signal'] = f70le_f70_liabilities_to_equity_momentum_calc002_21d_base_v002_signal

def f70le_f70_liabilities_to_equity_momentum_calc003_42d_base_v003_signal(liabilities, equity):
    res = (liabilities.rolling(42).mean() / equity.replace(0, np.nan).rolling(42).mean()).pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc003_42d_base_v003_signal'] = f70le_f70_liabilities_to_equity_momentum_calc003_42d_base_v003_signal

def f70le_f70_liabilities_to_equity_momentum_calc004_63d_base_v004_signal(liabilities, equity):
    res = (liabilities.rolling(63).mean() / equity.replace(0, np.nan).rolling(63).mean()).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc004_63d_base_v004_signal'] = f70le_f70_liabilities_to_equity_momentum_calc004_63d_base_v004_signal

def f70le_f70_liabilities_to_equity_momentum_calc005_126d_base_v005_signal(liabilities, equity):
    res = (liabilities.rolling(126).mean() / equity.replace(0, np.nan).rolling(126).mean()).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc005_126d_base_v005_signal'] = f70le_f70_liabilities_to_equity_momentum_calc005_126d_base_v005_signal

def f70le_f70_liabilities_to_equity_momentum_calc006_252d_base_v006_signal(liabilities, equity):
    res = (liabilities.rolling(252).mean() / equity.replace(0, np.nan).rolling(252).mean()).pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc006_252d_base_v006_signal'] = f70le_f70_liabilities_to_equity_momentum_calc006_252d_base_v006_signal

def f70le_f70_liabilities_to_equity_momentum_calc007_5d_base_v007_signal(liabilities, equity):
    res = (liabilities.rolling(5).mean() / equity.replace(0, np.nan).rolling(5).mean()).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc007_5d_base_v007_signal'] = f70le_f70_liabilities_to_equity_momentum_calc007_5d_base_v007_signal

def f70le_f70_liabilities_to_equity_momentum_calc008_10d_base_v008_signal(liabilities, equity):
    res = (liabilities.rolling(10).mean() / equity.replace(0, np.nan).rolling(10).mean()).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc008_10d_base_v008_signal'] = f70le_f70_liabilities_to_equity_momentum_calc008_10d_base_v008_signal

def f70le_f70_liabilities_to_equity_momentum_calc009_21d_base_v009_signal(liabilities, equity):
    res = (liabilities.rolling(21).mean() / equity.replace(0, np.nan).rolling(21).mean()).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc009_21d_base_v009_signal'] = f70le_f70_liabilities_to_equity_momentum_calc009_21d_base_v009_signal

def f70le_f70_liabilities_to_equity_momentum_calc010_42d_base_v010_signal(liabilities, equity):
    res = (liabilities.rolling(42).mean() / equity.replace(0, np.nan).rolling(42).mean()).pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc010_42d_base_v010_signal'] = f70le_f70_liabilities_to_equity_momentum_calc010_42d_base_v010_signal

def f70le_f70_liabilities_to_equity_momentum_calc011_63d_base_v011_signal(liabilities, equity, assets):
    res = (liabilities / assets.replace(0, np.nan)).rolling(63).mean() / (equity / assets.replace(0, np.nan)).rolling(63).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc011_63d_base_v011_signal'] = f70le_f70_liabilities_to_equity_momentum_calc011_63d_base_v011_signal

def f70le_f70_liabilities_to_equity_momentum_calc012_126d_base_v012_signal(liabilities, equity, assets):
    res = (liabilities / assets.replace(0, np.nan)).rolling(126).mean() / (equity / assets.replace(0, np.nan)).rolling(126).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc012_126d_base_v012_signal'] = f70le_f70_liabilities_to_equity_momentum_calc012_126d_base_v012_signal

def f70le_f70_liabilities_to_equity_momentum_calc013_252d_base_v013_signal(liabilities, equity, assets):
    res = (liabilities / assets.replace(0, np.nan)).rolling(252).mean() / (equity / assets.replace(0, np.nan)).rolling(252).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc013_252d_base_v013_signal'] = f70le_f70_liabilities_to_equity_momentum_calc013_252d_base_v013_signal

def f70le_f70_liabilities_to_equity_momentum_calc014_5d_base_v014_signal(liabilities, equity, assets):
    res = (liabilities / assets.replace(0, np.nan)).rolling(5).mean() / (equity / assets.replace(0, np.nan)).rolling(5).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc014_5d_base_v014_signal'] = f70le_f70_liabilities_to_equity_momentum_calc014_5d_base_v014_signal

def f70le_f70_liabilities_to_equity_momentum_calc015_10d_base_v015_signal(liabilities, equity, assets):
    res = (liabilities / assets.replace(0, np.nan)).rolling(10).mean() / (equity / assets.replace(0, np.nan)).rolling(10).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc015_10d_base_v015_signal'] = f70le_f70_liabilities_to_equity_momentum_calc015_10d_base_v015_signal

def f70le_f70_liabilities_to_equity_momentum_calc016_21d_base_v016_signal(liabilities, equity, assets):
    res = (liabilities / assets.replace(0, np.nan)).rolling(21).mean() / (equity / assets.replace(0, np.nan)).rolling(21).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc016_21d_base_v016_signal'] = f70le_f70_liabilities_to_equity_momentum_calc016_21d_base_v016_signal

def f70le_f70_liabilities_to_equity_momentum_calc017_42d_base_v017_signal(liabilities, equity, assets):
    res = (liabilities / assets.replace(0, np.nan)).rolling(42).mean() / (equity / assets.replace(0, np.nan)).rolling(42).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc017_42d_base_v017_signal'] = f70le_f70_liabilities_to_equity_momentum_calc017_42d_base_v017_signal

def f70le_f70_liabilities_to_equity_momentum_calc018_63d_base_v018_signal(liabilities, equity, assets):
    res = (liabilities / assets.replace(0, np.nan)).rolling(63).mean() / (equity / assets.replace(0, np.nan)).rolling(63).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc018_63d_base_v018_signal'] = f70le_f70_liabilities_to_equity_momentum_calc018_63d_base_v018_signal

def f70le_f70_liabilities_to_equity_momentum_calc019_126d_base_v019_signal(liabilities, equity, assets):
    res = (liabilities / assets.replace(0, np.nan)).rolling(126).mean() / (equity / assets.replace(0, np.nan)).rolling(126).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc019_126d_base_v019_signal'] = f70le_f70_liabilities_to_equity_momentum_calc019_126d_base_v019_signal

def f70le_f70_liabilities_to_equity_momentum_calc020_252d_base_v020_signal(liabilities, equity, assets):
    res = (liabilities / assets.replace(0, np.nan)).rolling(252).mean() / (equity / assets.replace(0, np.nan)).rolling(252).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc020_252d_base_v020_signal'] = f70le_f70_liabilities_to_equity_momentum_calc020_252d_base_v020_signal

def f70le_f70_liabilities_to_equity_momentum_calc021_5d_base_v021_signal(liabilities, equity):
    res = liabilities.diff(5).rolling(5).std() / equity.replace(0, np.nan).diff(5).rolling(5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc021_5d_base_v021_signal'] = f70le_f70_liabilities_to_equity_momentum_calc021_5d_base_v021_signal

def f70le_f70_liabilities_to_equity_momentum_calc022_10d_base_v022_signal(liabilities, equity):
    res = liabilities.diff(10).rolling(10).std() / equity.replace(0, np.nan).diff(10).rolling(10).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc022_10d_base_v022_signal'] = f70le_f70_liabilities_to_equity_momentum_calc022_10d_base_v022_signal

def f70le_f70_liabilities_to_equity_momentum_calc023_21d_base_v023_signal(liabilities, equity):
    res = liabilities.diff(21).rolling(21).std() / equity.replace(0, np.nan).diff(21).rolling(21).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc023_21d_base_v023_signal'] = f70le_f70_liabilities_to_equity_momentum_calc023_21d_base_v023_signal

def f70le_f70_liabilities_to_equity_momentum_calc024_42d_base_v024_signal(liabilities, equity):
    res = liabilities.diff(42).rolling(42).std() / equity.replace(0, np.nan).diff(42).rolling(42).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc024_42d_base_v024_signal'] = f70le_f70_liabilities_to_equity_momentum_calc024_42d_base_v024_signal

def f70le_f70_liabilities_to_equity_momentum_calc025_63d_base_v025_signal(liabilities, equity):
    res = liabilities.diff(63).rolling(63).std() / equity.replace(0, np.nan).diff(63).rolling(63).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc025_63d_base_v025_signal'] = f70le_f70_liabilities_to_equity_momentum_calc025_63d_base_v025_signal

def f70le_f70_liabilities_to_equity_momentum_calc026_126d_base_v026_signal(liabilities, equity):
    res = liabilities.diff(126).rolling(126).std() / equity.replace(0, np.nan).diff(126).rolling(126).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc026_126d_base_v026_signal'] = f70le_f70_liabilities_to_equity_momentum_calc026_126d_base_v026_signal

def f70le_f70_liabilities_to_equity_momentum_calc027_252d_base_v027_signal(liabilities, equity):
    res = liabilities.diff(252).rolling(252).std() / equity.replace(0, np.nan).diff(252).rolling(252).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc027_252d_base_v027_signal'] = f70le_f70_liabilities_to_equity_momentum_calc027_252d_base_v027_signal

def f70le_f70_liabilities_to_equity_momentum_calc028_5d_base_v028_signal(liabilities, equity):
    res = liabilities.diff(5).rolling(5).std() / equity.replace(0, np.nan).diff(5).rolling(5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc028_5d_base_v028_signal'] = f70le_f70_liabilities_to_equity_momentum_calc028_5d_base_v028_signal

def f70le_f70_liabilities_to_equity_momentum_calc029_10d_base_v029_signal(liabilities, equity):
    res = liabilities.diff(10).rolling(10).std() / equity.replace(0, np.nan).diff(10).rolling(10).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc029_10d_base_v029_signal'] = f70le_f70_liabilities_to_equity_momentum_calc029_10d_base_v029_signal

def f70le_f70_liabilities_to_equity_momentum_calc030_21d_base_v030_signal(liabilities, equity):
    res = liabilities.diff(21).rolling(21).std() / equity.replace(0, np.nan).diff(21).rolling(21).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc030_21d_base_v030_signal'] = f70le_f70_liabilities_to_equity_momentum_calc030_21d_base_v030_signal

def f70le_f70_liabilities_to_equity_momentum_calc031_42d_base_v031_signal(liabilities, equity):
    res = np.log((liabilities.abs() + 1.1) / (equity.abs() + 1.1)).rolling(42).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc031_42d_base_v031_signal'] = f70le_f70_liabilities_to_equity_momentum_calc031_42d_base_v031_signal

def f70le_f70_liabilities_to_equity_momentum_calc032_63d_base_v032_signal(liabilities, equity):
    res = np.log((liabilities.abs() + 1.1) / (equity.abs() + 1.1)).rolling(63).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc032_63d_base_v032_signal'] = f70le_f70_liabilities_to_equity_momentum_calc032_63d_base_v032_signal

def f70le_f70_liabilities_to_equity_momentum_calc033_126d_base_v033_signal(liabilities, equity):
    res = np.log((liabilities.abs() + 1.1) / (equity.abs() + 1.1)).rolling(126).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc033_126d_base_v033_signal'] = f70le_f70_liabilities_to_equity_momentum_calc033_126d_base_v033_signal

def f70le_f70_liabilities_to_equity_momentum_calc034_252d_base_v034_signal(liabilities, equity):
    res = np.log((liabilities.abs() + 1.1) / (equity.abs() + 1.1)).rolling(252).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc034_252d_base_v034_signal'] = f70le_f70_liabilities_to_equity_momentum_calc034_252d_base_v034_signal

def f70le_f70_liabilities_to_equity_momentum_calc035_5d_base_v035_signal(liabilities, equity):
    res = np.log((liabilities.abs() + 1.1) / (equity.abs() + 1.1)).rolling(5).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc035_5d_base_v035_signal'] = f70le_f70_liabilities_to_equity_momentum_calc035_5d_base_v035_signal

def f70le_f70_liabilities_to_equity_momentum_calc036_10d_base_v036_signal(liabilities, equity):
    res = np.log((liabilities.abs() + 1.1) / (equity.abs() + 1.1)).rolling(10).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc036_10d_base_v036_signal'] = f70le_f70_liabilities_to_equity_momentum_calc036_10d_base_v036_signal

def f70le_f70_liabilities_to_equity_momentum_calc037_21d_base_v037_signal(liabilities, equity):
    res = np.log((liabilities.abs() + 1.1) / (equity.abs() + 1.1)).rolling(21).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc037_21d_base_v037_signal'] = f70le_f70_liabilities_to_equity_momentum_calc037_21d_base_v037_signal

def f70le_f70_liabilities_to_equity_momentum_calc038_42d_base_v038_signal(liabilities, equity):
    res = np.log((liabilities.abs() + 1.1) / (equity.abs() + 1.1)).rolling(42).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc038_42d_base_v038_signal'] = f70le_f70_liabilities_to_equity_momentum_calc038_42d_base_v038_signal

def f70le_f70_liabilities_to_equity_momentum_calc039_63d_base_v039_signal(liabilities, equity):
    res = np.log((liabilities.abs() + 1.1) / (equity.abs() + 1.1)).rolling(63).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc039_63d_base_v039_signal'] = f70le_f70_liabilities_to_equity_momentum_calc039_63d_base_v039_signal

def f70le_f70_liabilities_to_equity_momentum_calc040_126d_base_v040_signal(liabilities, equity):
    res = np.log((liabilities.abs() + 1.1) / (equity.abs() + 1.1)).rolling(126).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc040_126d_base_v040_signal'] = f70le_f70_liabilities_to_equity_momentum_calc040_126d_base_v040_signal

def f70le_f70_liabilities_to_equity_momentum_calc041_252d_base_v041_signal(liabilities, equity):
    res = (liabilities / equity.replace(0, np.nan)).rolling(252).skew().rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc041_252d_base_v041_signal'] = f70le_f70_liabilities_to_equity_momentum_calc041_252d_base_v041_signal

def f70le_f70_liabilities_to_equity_momentum_calc042_5d_base_v042_signal(liabilities, equity):
    res = (liabilities / equity.replace(0, np.nan)).rolling(5).skew().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc042_5d_base_v042_signal'] = f70le_f70_liabilities_to_equity_momentum_calc042_5d_base_v042_signal

def f70le_f70_liabilities_to_equity_momentum_calc043_10d_base_v043_signal(liabilities, equity):
    res = (liabilities / equity.replace(0, np.nan)).rolling(10).skew().rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc043_10d_base_v043_signal'] = f70le_f70_liabilities_to_equity_momentum_calc043_10d_base_v043_signal

def f70le_f70_liabilities_to_equity_momentum_calc044_21d_base_v044_signal(liabilities, equity):
    res = (liabilities / equity.replace(0, np.nan)).rolling(21).skew().rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc044_21d_base_v044_signal'] = f70le_f70_liabilities_to_equity_momentum_calc044_21d_base_v044_signal

def f70le_f70_liabilities_to_equity_momentum_calc045_42d_base_v045_signal(liabilities, equity):
    res = (liabilities / equity.replace(0, np.nan)).rolling(42).skew().rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc045_42d_base_v045_signal'] = f70le_f70_liabilities_to_equity_momentum_calc045_42d_base_v045_signal

def f70le_f70_liabilities_to_equity_momentum_calc046_63d_base_v046_signal(liabilities, equity):
    res = (liabilities / equity.replace(0, np.nan)).rolling(63).skew().rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc046_63d_base_v046_signal'] = f70le_f70_liabilities_to_equity_momentum_calc046_63d_base_v046_signal

def f70le_f70_liabilities_to_equity_momentum_calc047_126d_base_v047_signal(liabilities, equity):
    res = (liabilities / equity.replace(0, np.nan)).rolling(126).skew().rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc047_126d_base_v047_signal'] = f70le_f70_liabilities_to_equity_momentum_calc047_126d_base_v047_signal

def f70le_f70_liabilities_to_equity_momentum_calc048_252d_base_v048_signal(liabilities, equity):
    res = (liabilities / equity.replace(0, np.nan)).rolling(252).skew().rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc048_252d_base_v048_signal'] = f70le_f70_liabilities_to_equity_momentum_calc048_252d_base_v048_signal

def f70le_f70_liabilities_to_equity_momentum_calc049_5d_base_v049_signal(liabilities, equity):
    res = (liabilities / equity.replace(0, np.nan)).rolling(5).skew().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc049_5d_base_v049_signal'] = f70le_f70_liabilities_to_equity_momentum_calc049_5d_base_v049_signal

def f70le_f70_liabilities_to_equity_momentum_calc050_10d_base_v050_signal(liabilities, equity):
    res = (liabilities / equity.replace(0, np.nan)).rolling(10).skew().rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc050_10d_base_v050_signal'] = f70le_f70_liabilities_to_equity_momentum_calc050_10d_base_v050_signal

def f70le_f70_liabilities_to_equity_momentum_calc051_21d_base_v051_signal(liabilities, equity):
    res = (liabilities.rolling(21).mean() / equity.rolling(21).mean().replace(0, np.nan)).pct_change(50).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc051_21d_base_v051_signal'] = f70le_f70_liabilities_to_equity_momentum_calc051_21d_base_v051_signal

def f70le_f70_liabilities_to_equity_momentum_calc052_42d_base_v052_signal(liabilities, equity):
    res = (liabilities.rolling(42).mean() / equity.rolling(42).mean().replace(0, np.nan)).pct_change(80).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc052_42d_base_v052_signal'] = f70le_f70_liabilities_to_equity_momentum_calc052_42d_base_v052_signal

def f70le_f70_liabilities_to_equity_momentum_calc053_63d_base_v053_signal(liabilities, equity):
    res = (liabilities.rolling(63).mean() / equity.rolling(63).mean().replace(0, np.nan)).pct_change(100).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc053_63d_base_v053_signal'] = f70le_f70_liabilities_to_equity_momentum_calc053_63d_base_v053_signal

def f70le_f70_liabilities_to_equity_momentum_calc054_126d_base_v054_signal(liabilities, equity):
    res = (liabilities.rolling(126).mean() / equity.rolling(126).mean().replace(0, np.nan)).pct_change(150).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc054_126d_base_v054_signal'] = f70le_f70_liabilities_to_equity_momentum_calc054_126d_base_v054_signal

def f70le_f70_liabilities_to_equity_momentum_calc055_252d_base_v055_signal(liabilities, equity):
    res = (liabilities.rolling(252).mean() / equity.rolling(252).mean().replace(0, np.nan)).pct_change(200).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc055_252d_base_v055_signal'] = f70le_f70_liabilities_to_equity_momentum_calc055_252d_base_v055_signal

def f70le_f70_liabilities_to_equity_momentum_calc056_5d_base_v056_signal(liabilities, equity):
    res = (liabilities.rolling(5).mean() / equity.rolling(5).mean().replace(0, np.nan)).pct_change(15).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc056_5d_base_v056_signal'] = f70le_f70_liabilities_to_equity_momentum_calc056_5d_base_v056_signal

def f70le_f70_liabilities_to_equity_momentum_calc057_10d_base_v057_signal(liabilities, equity):
    res = (liabilities.rolling(10).mean() / equity.rolling(10).mean().replace(0, np.nan)).pct_change(30).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc057_10d_base_v057_signal'] = f70le_f70_liabilities_to_equity_momentum_calc057_10d_base_v057_signal

def f70le_f70_liabilities_to_equity_momentum_calc058_21d_base_v058_signal(liabilities, equity):
    res = (liabilities.rolling(21).mean() / equity.rolling(21).mean().replace(0, np.nan)).pct_change(50).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc058_21d_base_v058_signal'] = f70le_f70_liabilities_to_equity_momentum_calc058_21d_base_v058_signal

def f70le_f70_liabilities_to_equity_momentum_calc059_42d_base_v059_signal(liabilities, equity):
    res = (liabilities.rolling(42).mean() / equity.rolling(42).mean().replace(0, np.nan)).pct_change(80).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc059_42d_base_v059_signal'] = f70le_f70_liabilities_to_equity_momentum_calc059_42d_base_v059_signal

def f70le_f70_liabilities_to_equity_momentum_calc060_63d_base_v060_signal(liabilities, equity):
    res = (liabilities.rolling(63).mean() / equity.rolling(63).mean().replace(0, np.nan)).pct_change(100).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc060_63d_base_v060_signal'] = f70le_f70_liabilities_to_equity_momentum_calc060_63d_base_v060_signal

def f70le_f70_liabilities_to_equity_momentum_calc061_126d_base_v061_signal(debt, equity):
    res = (debt / equity.replace(0, np.nan)).rolling(126).kurt().diff(3).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc061_126d_base_v061_signal'] = f70le_f70_liabilities_to_equity_momentum_calc061_126d_base_v061_signal

def f70le_f70_liabilities_to_equity_momentum_calc062_252d_base_v062_signal(debt, equity):
    res = (debt / equity.replace(0, np.nan)).rolling(252).kurt().diff(3).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc062_252d_base_v062_signal'] = f70le_f70_liabilities_to_equity_momentum_calc062_252d_base_v062_signal

def f70le_f70_liabilities_to_equity_momentum_calc063_5d_base_v063_signal(debt, equity):
    res = (debt / equity.replace(0, np.nan)).rolling(5).kurt().diff(3).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc063_5d_base_v063_signal'] = f70le_f70_liabilities_to_equity_momentum_calc063_5d_base_v063_signal

def f70le_f70_liabilities_to_equity_momentum_calc064_10d_base_v064_signal(debt, equity):
    res = (debt / equity.replace(0, np.nan)).rolling(10).kurt().diff(3).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc064_10d_base_v064_signal'] = f70le_f70_liabilities_to_equity_momentum_calc064_10d_base_v064_signal

def f70le_f70_liabilities_to_equity_momentum_calc065_21d_base_v065_signal(debt, equity):
    res = (debt / equity.replace(0, np.nan)).rolling(21).kurt().diff(3).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc065_21d_base_v065_signal'] = f70le_f70_liabilities_to_equity_momentum_calc065_21d_base_v065_signal

def f70le_f70_liabilities_to_equity_momentum_calc066_42d_base_v066_signal(debt, equity):
    res = (debt / equity.replace(0, np.nan)).rolling(42).kurt().diff(3).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc066_42d_base_v066_signal'] = f70le_f70_liabilities_to_equity_momentum_calc066_42d_base_v066_signal

def f70le_f70_liabilities_to_equity_momentum_calc067_63d_base_v067_signal(debt, equity):
    res = (debt / equity.replace(0, np.nan)).rolling(63).kurt().diff(3).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc067_63d_base_v067_signal'] = f70le_f70_liabilities_to_equity_momentum_calc067_63d_base_v067_signal

def f70le_f70_liabilities_to_equity_momentum_calc068_126d_base_v068_signal(debt, equity):
    res = (debt / equity.replace(0, np.nan)).rolling(126).kurt().diff(3).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc068_126d_base_v068_signal'] = f70le_f70_liabilities_to_equity_momentum_calc068_126d_base_v068_signal

def f70le_f70_liabilities_to_equity_momentum_calc069_252d_base_v069_signal(debt, equity):
    res = (debt / equity.replace(0, np.nan)).rolling(252).kurt().diff(3).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc069_252d_base_v069_signal'] = f70le_f70_liabilities_to_equity_momentum_calc069_252d_base_v069_signal

def f70le_f70_liabilities_to_equity_momentum_calc070_5d_base_v070_signal(debt, equity):
    res = (debt / equity.replace(0, np.nan)).rolling(5).kurt().diff(3).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc070_5d_base_v070_signal'] = f70le_f70_liabilities_to_equity_momentum_calc070_5d_base_v070_signal

def f70le_f70_liabilities_to_equity_momentum_calc071_10d_base_v071_signal(liabilities, equity, marketcap):
    res = (liabilities / marketcap.replace(0, np.nan)).rolling(10).std() / (equity / marketcap.replace(0, np.nan)).rolling(10).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc071_10d_base_v071_signal'] = f70le_f70_liabilities_to_equity_momentum_calc071_10d_base_v071_signal

def f70le_f70_liabilities_to_equity_momentum_calc072_21d_base_v072_signal(liabilities, equity, marketcap):
    res = (liabilities / marketcap.replace(0, np.nan)).rolling(21).std() / (equity / marketcap.replace(0, np.nan)).rolling(21).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc072_21d_base_v072_signal'] = f70le_f70_liabilities_to_equity_momentum_calc072_21d_base_v072_signal

def f70le_f70_liabilities_to_equity_momentum_calc073_42d_base_v073_signal(liabilities, equity, marketcap):
    res = (liabilities / marketcap.replace(0, np.nan)).rolling(42).std() / (equity / marketcap.replace(0, np.nan)).rolling(42).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc073_42d_base_v073_signal'] = f70le_f70_liabilities_to_equity_momentum_calc073_42d_base_v073_signal

def f70le_f70_liabilities_to_equity_momentum_calc074_63d_base_v074_signal(liabilities, equity, marketcap):
    res = (liabilities / marketcap.replace(0, np.nan)).rolling(63).std() / (equity / marketcap.replace(0, np.nan)).rolling(63).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc074_63d_base_v074_signal'] = f70le_f70_liabilities_to_equity_momentum_calc074_63d_base_v074_signal

def f70le_f70_liabilities_to_equity_momentum_calc075_126d_base_v075_signal(liabilities, equity, marketcap):
    res = (liabilities / marketcap.replace(0, np.nan)).rolling(126).std() / (equity / marketcap.replace(0, np.nan)).rolling(126).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc075_126d_base_v075_signal'] = f70le_f70_liabilities_to_equity_momentum_calc075_126d_base_v075_signal

