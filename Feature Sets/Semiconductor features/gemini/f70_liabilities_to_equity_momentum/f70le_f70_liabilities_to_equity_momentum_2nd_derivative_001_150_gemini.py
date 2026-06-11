import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f70le_f70_liabilities_to_equity_momentum_calc001_10d_2nd_derivative_v001_signal(liabilities, equity):
    res = ((liabilities.rolling(10).mean() / equity.replace(0, np.nan).rolling(10).mean()).pct_change(10)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc001_10d_2nd_derivative_v001_signal'] = f70le_f70_liabilities_to_equity_momentum_calc001_10d_2nd_derivative_v001_signal

def f70le_f70_liabilities_to_equity_momentum_calc002_21d_2nd_derivative_v002_signal(liabilities, equity):
    res = ((liabilities.rolling(21).mean() / equity.replace(0, np.nan).rolling(21).mean()).pct_change(21)).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc002_21d_2nd_derivative_v002_signal'] = f70le_f70_liabilities_to_equity_momentum_calc002_21d_2nd_derivative_v002_signal

def f70le_f70_liabilities_to_equity_momentum_calc003_42d_2nd_derivative_v003_signal(liabilities, equity):
    res = ((liabilities.rolling(42).mean() / equity.replace(0, np.nan).rolling(42).mean()).pct_change(42)).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc003_42d_2nd_derivative_v003_signal'] = f70le_f70_liabilities_to_equity_momentum_calc003_42d_2nd_derivative_v003_signal

def f70le_f70_liabilities_to_equity_momentum_calc004_63d_2nd_derivative_v004_signal(liabilities, equity):
    res = ((liabilities.rolling(63).mean() / equity.replace(0, np.nan).rolling(63).mean()).pct_change(63)).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc004_63d_2nd_derivative_v004_signal'] = f70le_f70_liabilities_to_equity_momentum_calc004_63d_2nd_derivative_v004_signal

def f70le_f70_liabilities_to_equity_momentum_calc005_126d_2nd_derivative_v005_signal(liabilities, equity):
    res = ((liabilities.rolling(126).mean() / equity.replace(0, np.nan).rolling(126).mean()).pct_change(126)).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc005_126d_2nd_derivative_v005_signal'] = f70le_f70_liabilities_to_equity_momentum_calc005_126d_2nd_derivative_v005_signal

def f70le_f70_liabilities_to_equity_momentum_calc006_252d_2nd_derivative_v006_signal(liabilities, equity):
    res = ((liabilities.rolling(252).mean() / equity.replace(0, np.nan).rolling(252).mean()).pct_change(252)).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc006_252d_2nd_derivative_v006_signal'] = f70le_f70_liabilities_to_equity_momentum_calc006_252d_2nd_derivative_v006_signal

def f70le_f70_liabilities_to_equity_momentum_calc007_5d_2nd_derivative_v007_signal(liabilities, equity):
    res = ((liabilities.rolling(5).mean() / equity.replace(0, np.nan).rolling(5).mean()).pct_change(5)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc007_5d_2nd_derivative_v007_signal'] = f70le_f70_liabilities_to_equity_momentum_calc007_5d_2nd_derivative_v007_signal

def f70le_f70_liabilities_to_equity_momentum_calc008_10d_2nd_derivative_v008_signal(liabilities, equity):
    res = ((liabilities.rolling(10).mean() / equity.replace(0, np.nan).rolling(10).mean()).pct_change(10)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc008_10d_2nd_derivative_v008_signal'] = f70le_f70_liabilities_to_equity_momentum_calc008_10d_2nd_derivative_v008_signal

def f70le_f70_liabilities_to_equity_momentum_calc009_21d_2nd_derivative_v009_signal(liabilities, equity):
    res = ((liabilities.rolling(21).mean() / equity.replace(0, np.nan).rolling(21).mean()).pct_change(21)).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc009_21d_2nd_derivative_v009_signal'] = f70le_f70_liabilities_to_equity_momentum_calc009_21d_2nd_derivative_v009_signal

def f70le_f70_liabilities_to_equity_momentum_calc010_42d_2nd_derivative_v010_signal(liabilities, equity):
    res = ((liabilities.rolling(42).mean() / equity.replace(0, np.nan).rolling(42).mean()).pct_change(42)).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc010_42d_2nd_derivative_v010_signal'] = f70le_f70_liabilities_to_equity_momentum_calc010_42d_2nd_derivative_v010_signal

def f70le_f70_liabilities_to_equity_momentum_calc011_63d_2nd_derivative_v011_signal(liabilities, equity, assets):
    res = ((liabilities / assets.replace(0, np.nan)).rolling(63).mean() / (equity / assets.replace(0, np.nan)).rolling(63).mean().replace(0, np.nan)).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc011_63d_2nd_derivative_v011_signal'] = f70le_f70_liabilities_to_equity_momentum_calc011_63d_2nd_derivative_v011_signal

def f70le_f70_liabilities_to_equity_momentum_calc012_126d_2nd_derivative_v012_signal(liabilities, equity, assets):
    res = ((liabilities / assets.replace(0, np.nan)).rolling(126).mean() / (equity / assets.replace(0, np.nan)).rolling(126).mean().replace(0, np.nan)).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc012_126d_2nd_derivative_v012_signal'] = f70le_f70_liabilities_to_equity_momentum_calc012_126d_2nd_derivative_v012_signal

def f70le_f70_liabilities_to_equity_momentum_calc013_252d_2nd_derivative_v013_signal(liabilities, equity, assets):
    res = ((liabilities / assets.replace(0, np.nan)).rolling(252).mean() / (equity / assets.replace(0, np.nan)).rolling(252).mean().replace(0, np.nan)).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc013_252d_2nd_derivative_v013_signal'] = f70le_f70_liabilities_to_equity_momentum_calc013_252d_2nd_derivative_v013_signal

def f70le_f70_liabilities_to_equity_momentum_calc014_5d_2nd_derivative_v014_signal(liabilities, equity, assets):
    res = ((liabilities / assets.replace(0, np.nan)).rolling(5).mean() / (equity / assets.replace(0, np.nan)).rolling(5).mean().replace(0, np.nan)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc014_5d_2nd_derivative_v014_signal'] = f70le_f70_liabilities_to_equity_momentum_calc014_5d_2nd_derivative_v014_signal

def f70le_f70_liabilities_to_equity_momentum_calc015_10d_2nd_derivative_v015_signal(liabilities, equity, assets):
    res = ((liabilities / assets.replace(0, np.nan)).rolling(10).mean() / (equity / assets.replace(0, np.nan)).rolling(10).mean().replace(0, np.nan)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc015_10d_2nd_derivative_v015_signal'] = f70le_f70_liabilities_to_equity_momentum_calc015_10d_2nd_derivative_v015_signal

def f70le_f70_liabilities_to_equity_momentum_calc016_21d_2nd_derivative_v016_signal(liabilities, equity, assets):
    res = ((liabilities / assets.replace(0, np.nan)).rolling(21).mean() / (equity / assets.replace(0, np.nan)).rolling(21).mean().replace(0, np.nan)).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc016_21d_2nd_derivative_v016_signal'] = f70le_f70_liabilities_to_equity_momentum_calc016_21d_2nd_derivative_v016_signal

def f70le_f70_liabilities_to_equity_momentum_calc017_42d_2nd_derivative_v017_signal(liabilities, equity, assets):
    res = ((liabilities / assets.replace(0, np.nan)).rolling(42).mean() / (equity / assets.replace(0, np.nan)).rolling(42).mean().replace(0, np.nan)).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc017_42d_2nd_derivative_v017_signal'] = f70le_f70_liabilities_to_equity_momentum_calc017_42d_2nd_derivative_v017_signal

def f70le_f70_liabilities_to_equity_momentum_calc018_63d_2nd_derivative_v018_signal(liabilities, equity, assets):
    res = ((liabilities / assets.replace(0, np.nan)).rolling(63).mean() / (equity / assets.replace(0, np.nan)).rolling(63).mean().replace(0, np.nan)).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc018_63d_2nd_derivative_v018_signal'] = f70le_f70_liabilities_to_equity_momentum_calc018_63d_2nd_derivative_v018_signal

def f70le_f70_liabilities_to_equity_momentum_calc019_126d_2nd_derivative_v019_signal(liabilities, equity, assets):
    res = ((liabilities / assets.replace(0, np.nan)).rolling(126).mean() / (equity / assets.replace(0, np.nan)).rolling(126).mean().replace(0, np.nan)).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc019_126d_2nd_derivative_v019_signal'] = f70le_f70_liabilities_to_equity_momentum_calc019_126d_2nd_derivative_v019_signal

def f70le_f70_liabilities_to_equity_momentum_calc020_252d_2nd_derivative_v020_signal(liabilities, equity, assets):
    res = ((liabilities / assets.replace(0, np.nan)).rolling(252).mean() / (equity / assets.replace(0, np.nan)).rolling(252).mean().replace(0, np.nan)).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc020_252d_2nd_derivative_v020_signal'] = f70le_f70_liabilities_to_equity_momentum_calc020_252d_2nd_derivative_v020_signal

def f70le_f70_liabilities_to_equity_momentum_calc021_5d_2nd_derivative_v021_signal(liabilities, equity):
    res = (liabilities.diff(5).rolling(5).std() / equity.replace(0, np.nan).diff(5).rolling(5).std().replace(0, np.nan)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc021_5d_2nd_derivative_v021_signal'] = f70le_f70_liabilities_to_equity_momentum_calc021_5d_2nd_derivative_v021_signal

def f70le_f70_liabilities_to_equity_momentum_calc022_10d_2nd_derivative_v022_signal(liabilities, equity):
    res = (liabilities.diff(10).rolling(10).std() / equity.replace(0, np.nan).diff(10).rolling(10).std().replace(0, np.nan)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc022_10d_2nd_derivative_v022_signal'] = f70le_f70_liabilities_to_equity_momentum_calc022_10d_2nd_derivative_v022_signal

def f70le_f70_liabilities_to_equity_momentum_calc023_21d_2nd_derivative_v023_signal(liabilities, equity):
    res = (liabilities.diff(21).rolling(21).std() / equity.replace(0, np.nan).diff(21).rolling(21).std().replace(0, np.nan)).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc023_21d_2nd_derivative_v023_signal'] = f70le_f70_liabilities_to_equity_momentum_calc023_21d_2nd_derivative_v023_signal

def f70le_f70_liabilities_to_equity_momentum_calc024_42d_2nd_derivative_v024_signal(liabilities, equity):
    res = (liabilities.diff(42).rolling(42).std() / equity.replace(0, np.nan).diff(42).rolling(42).std().replace(0, np.nan)).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc024_42d_2nd_derivative_v024_signal'] = f70le_f70_liabilities_to_equity_momentum_calc024_42d_2nd_derivative_v024_signal

def f70le_f70_liabilities_to_equity_momentum_calc025_63d_2nd_derivative_v025_signal(liabilities, equity):
    res = (liabilities.diff(63).rolling(63).std() / equity.replace(0, np.nan).diff(63).rolling(63).std().replace(0, np.nan)).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc025_63d_2nd_derivative_v025_signal'] = f70le_f70_liabilities_to_equity_momentum_calc025_63d_2nd_derivative_v025_signal

def f70le_f70_liabilities_to_equity_momentum_calc026_126d_2nd_derivative_v026_signal(liabilities, equity):
    res = (liabilities.diff(126).rolling(126).std() / equity.replace(0, np.nan).diff(126).rolling(126).std().replace(0, np.nan)).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc026_126d_2nd_derivative_v026_signal'] = f70le_f70_liabilities_to_equity_momentum_calc026_126d_2nd_derivative_v026_signal

def f70le_f70_liabilities_to_equity_momentum_calc027_252d_2nd_derivative_v027_signal(liabilities, equity):
    res = (liabilities.diff(252).rolling(252).std() / equity.replace(0, np.nan).diff(252).rolling(252).std().replace(0, np.nan)).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc027_252d_2nd_derivative_v027_signal'] = f70le_f70_liabilities_to_equity_momentum_calc027_252d_2nd_derivative_v027_signal

def f70le_f70_liabilities_to_equity_momentum_calc028_5d_2nd_derivative_v028_signal(liabilities, equity):
    res = (liabilities.diff(5).rolling(5).std() / equity.replace(0, np.nan).diff(5).rolling(5).std().replace(0, np.nan)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc028_5d_2nd_derivative_v028_signal'] = f70le_f70_liabilities_to_equity_momentum_calc028_5d_2nd_derivative_v028_signal

def f70le_f70_liabilities_to_equity_momentum_calc029_10d_2nd_derivative_v029_signal(liabilities, equity):
    res = (liabilities.diff(10).rolling(10).std() / equity.replace(0, np.nan).diff(10).rolling(10).std().replace(0, np.nan)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc029_10d_2nd_derivative_v029_signal'] = f70le_f70_liabilities_to_equity_momentum_calc029_10d_2nd_derivative_v029_signal

def f70le_f70_liabilities_to_equity_momentum_calc030_21d_2nd_derivative_v030_signal(liabilities, equity):
    res = (liabilities.diff(21).rolling(21).std() / equity.replace(0, np.nan).diff(21).rolling(21).std().replace(0, np.nan)).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc030_21d_2nd_derivative_v030_signal'] = f70le_f70_liabilities_to_equity_momentum_calc030_21d_2nd_derivative_v030_signal

def f70le_f70_liabilities_to_equity_momentum_calc031_42d_2nd_derivative_v031_signal(liabilities, equity):
    res = (np.log((liabilities.abs() + 1.1) / (equity.abs() + 1.1)).rolling(42).std().pct_change(5)).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc031_42d_2nd_derivative_v031_signal'] = f70le_f70_liabilities_to_equity_momentum_calc031_42d_2nd_derivative_v031_signal

def f70le_f70_liabilities_to_equity_momentum_calc032_63d_2nd_derivative_v032_signal(liabilities, equity):
    res = (np.log((liabilities.abs() + 1.1) / (equity.abs() + 1.1)).rolling(63).std().pct_change(5)).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc032_63d_2nd_derivative_v032_signal'] = f70le_f70_liabilities_to_equity_momentum_calc032_63d_2nd_derivative_v032_signal

def f70le_f70_liabilities_to_equity_momentum_calc033_126d_2nd_derivative_v033_signal(liabilities, equity):
    res = (np.log((liabilities.abs() + 1.1) / (equity.abs() + 1.1)).rolling(126).std().pct_change(5)).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc033_126d_2nd_derivative_v033_signal'] = f70le_f70_liabilities_to_equity_momentum_calc033_126d_2nd_derivative_v033_signal

def f70le_f70_liabilities_to_equity_momentum_calc034_252d_2nd_derivative_v034_signal(liabilities, equity):
    res = (np.log((liabilities.abs() + 1.1) / (equity.abs() + 1.1)).rolling(252).std().pct_change(5)).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc034_252d_2nd_derivative_v034_signal'] = f70le_f70_liabilities_to_equity_momentum_calc034_252d_2nd_derivative_v034_signal

def f70le_f70_liabilities_to_equity_momentum_calc035_5d_2nd_derivative_v035_signal(liabilities, equity):
    res = (np.log((liabilities.abs() + 1.1) / (equity.abs() + 1.1)).rolling(5).std().pct_change(5)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc035_5d_2nd_derivative_v035_signal'] = f70le_f70_liabilities_to_equity_momentum_calc035_5d_2nd_derivative_v035_signal

def f70le_f70_liabilities_to_equity_momentum_calc036_10d_2nd_derivative_v036_signal(liabilities, equity):
    res = (np.log((liabilities.abs() + 1.1) / (equity.abs() + 1.1)).rolling(10).std().pct_change(5)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc036_10d_2nd_derivative_v036_signal'] = f70le_f70_liabilities_to_equity_momentum_calc036_10d_2nd_derivative_v036_signal

def f70le_f70_liabilities_to_equity_momentum_calc037_21d_2nd_derivative_v037_signal(liabilities, equity):
    res = (np.log((liabilities.abs() + 1.1) / (equity.abs() + 1.1)).rolling(21).std().pct_change(5)).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc037_21d_2nd_derivative_v037_signal'] = f70le_f70_liabilities_to_equity_momentum_calc037_21d_2nd_derivative_v037_signal

def f70le_f70_liabilities_to_equity_momentum_calc038_42d_2nd_derivative_v038_signal(liabilities, equity):
    res = (np.log((liabilities.abs() + 1.1) / (equity.abs() + 1.1)).rolling(42).std().pct_change(5)).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc038_42d_2nd_derivative_v038_signal'] = f70le_f70_liabilities_to_equity_momentum_calc038_42d_2nd_derivative_v038_signal

def f70le_f70_liabilities_to_equity_momentum_calc039_63d_2nd_derivative_v039_signal(liabilities, equity):
    res = (np.log((liabilities.abs() + 1.1) / (equity.abs() + 1.1)).rolling(63).std().pct_change(5)).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc039_63d_2nd_derivative_v039_signal'] = f70le_f70_liabilities_to_equity_momentum_calc039_63d_2nd_derivative_v039_signal

def f70le_f70_liabilities_to_equity_momentum_calc040_126d_2nd_derivative_v040_signal(liabilities, equity):
    res = (np.log((liabilities.abs() + 1.1) / (equity.abs() + 1.1)).rolling(126).std().pct_change(5)).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc040_126d_2nd_derivative_v040_signal'] = f70le_f70_liabilities_to_equity_momentum_calc040_126d_2nd_derivative_v040_signal

def f70le_f70_liabilities_to_equity_momentum_calc041_252d_2nd_derivative_v041_signal(liabilities, equity):
    res = ((liabilities / equity.replace(0, np.nan)).rolling(252).skew().rolling(252).mean()).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc041_252d_2nd_derivative_v041_signal'] = f70le_f70_liabilities_to_equity_momentum_calc041_252d_2nd_derivative_v041_signal

def f70le_f70_liabilities_to_equity_momentum_calc042_5d_2nd_derivative_v042_signal(liabilities, equity):
    res = ((liabilities / equity.replace(0, np.nan)).rolling(5).skew().rolling(5).mean()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc042_5d_2nd_derivative_v042_signal'] = f70le_f70_liabilities_to_equity_momentum_calc042_5d_2nd_derivative_v042_signal

def f70le_f70_liabilities_to_equity_momentum_calc043_10d_2nd_derivative_v043_signal(liabilities, equity):
    res = ((liabilities / equity.replace(0, np.nan)).rolling(10).skew().rolling(10).mean()).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc043_10d_2nd_derivative_v043_signal'] = f70le_f70_liabilities_to_equity_momentum_calc043_10d_2nd_derivative_v043_signal

def f70le_f70_liabilities_to_equity_momentum_calc044_21d_2nd_derivative_v044_signal(liabilities, equity):
    res = ((liabilities / equity.replace(0, np.nan)).rolling(21).skew().rolling(21).mean()).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc044_21d_2nd_derivative_v044_signal'] = f70le_f70_liabilities_to_equity_momentum_calc044_21d_2nd_derivative_v044_signal

def f70le_f70_liabilities_to_equity_momentum_calc045_42d_2nd_derivative_v045_signal(liabilities, equity):
    res = ((liabilities / equity.replace(0, np.nan)).rolling(42).skew().rolling(42).mean()).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc045_42d_2nd_derivative_v045_signal'] = f70le_f70_liabilities_to_equity_momentum_calc045_42d_2nd_derivative_v045_signal

def f70le_f70_liabilities_to_equity_momentum_calc046_63d_2nd_derivative_v046_signal(liabilities, equity):
    res = ((liabilities / equity.replace(0, np.nan)).rolling(63).skew().rolling(63).mean()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc046_63d_2nd_derivative_v046_signal'] = f70le_f70_liabilities_to_equity_momentum_calc046_63d_2nd_derivative_v046_signal

def f70le_f70_liabilities_to_equity_momentum_calc047_126d_2nd_derivative_v047_signal(liabilities, equity):
    res = ((liabilities / equity.replace(0, np.nan)).rolling(126).skew().rolling(126).mean()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc047_126d_2nd_derivative_v047_signal'] = f70le_f70_liabilities_to_equity_momentum_calc047_126d_2nd_derivative_v047_signal

def f70le_f70_liabilities_to_equity_momentum_calc048_252d_2nd_derivative_v048_signal(liabilities, equity):
    res = ((liabilities / equity.replace(0, np.nan)).rolling(252).skew().rolling(252).mean()).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc048_252d_2nd_derivative_v048_signal'] = f70le_f70_liabilities_to_equity_momentum_calc048_252d_2nd_derivative_v048_signal

def f70le_f70_liabilities_to_equity_momentum_calc049_5d_2nd_derivative_v049_signal(liabilities, equity):
    res = ((liabilities / equity.replace(0, np.nan)).rolling(5).skew().rolling(5).mean()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc049_5d_2nd_derivative_v049_signal'] = f70le_f70_liabilities_to_equity_momentum_calc049_5d_2nd_derivative_v049_signal

def f70le_f70_liabilities_to_equity_momentum_calc050_10d_2nd_derivative_v050_signal(liabilities, equity):
    res = ((liabilities / equity.replace(0, np.nan)).rolling(10).skew().rolling(10).mean()).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc050_10d_2nd_derivative_v050_signal'] = f70le_f70_liabilities_to_equity_momentum_calc050_10d_2nd_derivative_v050_signal

def f70le_f70_liabilities_to_equity_momentum_calc051_21d_2nd_derivative_v051_signal(liabilities, equity):
    res = ((liabilities.rolling(21).mean() / equity.rolling(21).mean().replace(0, np.nan)).pct_change(50).rolling(21).std()).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc051_21d_2nd_derivative_v051_signal'] = f70le_f70_liabilities_to_equity_momentum_calc051_21d_2nd_derivative_v051_signal

def f70le_f70_liabilities_to_equity_momentum_calc052_42d_2nd_derivative_v052_signal(liabilities, equity):
    res = ((liabilities.rolling(42).mean() / equity.rolling(42).mean().replace(0, np.nan)).pct_change(80).rolling(42).std()).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc052_42d_2nd_derivative_v052_signal'] = f70le_f70_liabilities_to_equity_momentum_calc052_42d_2nd_derivative_v052_signal

def f70le_f70_liabilities_to_equity_momentum_calc053_63d_2nd_derivative_v053_signal(liabilities, equity):
    res = ((liabilities.rolling(63).mean() / equity.rolling(63).mean().replace(0, np.nan)).pct_change(100).rolling(63).std()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc053_63d_2nd_derivative_v053_signal'] = f70le_f70_liabilities_to_equity_momentum_calc053_63d_2nd_derivative_v053_signal

def f70le_f70_liabilities_to_equity_momentum_calc054_126d_2nd_derivative_v054_signal(liabilities, equity):
    res = ((liabilities.rolling(126).mean() / equity.rolling(126).mean().replace(0, np.nan)).pct_change(150).rolling(126).std()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc054_126d_2nd_derivative_v054_signal'] = f70le_f70_liabilities_to_equity_momentum_calc054_126d_2nd_derivative_v054_signal

def f70le_f70_liabilities_to_equity_momentum_calc055_252d_2nd_derivative_v055_signal(liabilities, equity):
    res = ((liabilities.rolling(252).mean() / equity.rolling(252).mean().replace(0, np.nan)).pct_change(200).rolling(252).std()).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc055_252d_2nd_derivative_v055_signal'] = f70le_f70_liabilities_to_equity_momentum_calc055_252d_2nd_derivative_v055_signal

def f70le_f70_liabilities_to_equity_momentum_calc056_5d_2nd_derivative_v056_signal(liabilities, equity):
    res = ((liabilities.rolling(5).mean() / equity.rolling(5).mean().replace(0, np.nan)).pct_change(15).rolling(5).std()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc056_5d_2nd_derivative_v056_signal'] = f70le_f70_liabilities_to_equity_momentum_calc056_5d_2nd_derivative_v056_signal

def f70le_f70_liabilities_to_equity_momentum_calc057_10d_2nd_derivative_v057_signal(liabilities, equity):
    res = ((liabilities.rolling(10).mean() / equity.rolling(10).mean().replace(0, np.nan)).pct_change(30).rolling(10).std()).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc057_10d_2nd_derivative_v057_signal'] = f70le_f70_liabilities_to_equity_momentum_calc057_10d_2nd_derivative_v057_signal

def f70le_f70_liabilities_to_equity_momentum_calc058_21d_2nd_derivative_v058_signal(liabilities, equity):
    res = ((liabilities.rolling(21).mean() / equity.rolling(21).mean().replace(0, np.nan)).pct_change(50).rolling(21).std()).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc058_21d_2nd_derivative_v058_signal'] = f70le_f70_liabilities_to_equity_momentum_calc058_21d_2nd_derivative_v058_signal

def f70le_f70_liabilities_to_equity_momentum_calc059_42d_2nd_derivative_v059_signal(liabilities, equity):
    res = ((liabilities.rolling(42).mean() / equity.rolling(42).mean().replace(0, np.nan)).pct_change(80).rolling(42).std()).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc059_42d_2nd_derivative_v059_signal'] = f70le_f70_liabilities_to_equity_momentum_calc059_42d_2nd_derivative_v059_signal

def f70le_f70_liabilities_to_equity_momentum_calc060_63d_2nd_derivative_v060_signal(liabilities, equity):
    res = ((liabilities.rolling(63).mean() / equity.rolling(63).mean().replace(0, np.nan)).pct_change(100).rolling(63).std()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc060_63d_2nd_derivative_v060_signal'] = f70le_f70_liabilities_to_equity_momentum_calc060_63d_2nd_derivative_v060_signal

def f70le_f70_liabilities_to_equity_momentum_calc061_126d_2nd_derivative_v061_signal(debt, equity):
    res = ((debt / equity.replace(0, np.nan)).rolling(126).kurt().diff(3).rolling(126).mean()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc061_126d_2nd_derivative_v061_signal'] = f70le_f70_liabilities_to_equity_momentum_calc061_126d_2nd_derivative_v061_signal

def f70le_f70_liabilities_to_equity_momentum_calc062_252d_2nd_derivative_v062_signal(debt, equity):
    res = ((debt / equity.replace(0, np.nan)).rolling(252).kurt().diff(3).rolling(252).mean()).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc062_252d_2nd_derivative_v062_signal'] = f70le_f70_liabilities_to_equity_momentum_calc062_252d_2nd_derivative_v062_signal

def f70le_f70_liabilities_to_equity_momentum_calc063_5d_2nd_derivative_v063_signal(debt, equity):
    res = ((debt / equity.replace(0, np.nan)).rolling(5).kurt().diff(3).rolling(5).mean()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc063_5d_2nd_derivative_v063_signal'] = f70le_f70_liabilities_to_equity_momentum_calc063_5d_2nd_derivative_v063_signal

def f70le_f70_liabilities_to_equity_momentum_calc064_10d_2nd_derivative_v064_signal(debt, equity):
    res = ((debt / equity.replace(0, np.nan)).rolling(10).kurt().diff(3).rolling(10).mean()).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc064_10d_2nd_derivative_v064_signal'] = f70le_f70_liabilities_to_equity_momentum_calc064_10d_2nd_derivative_v064_signal

def f70le_f70_liabilities_to_equity_momentum_calc065_21d_2nd_derivative_v065_signal(debt, equity):
    res = ((debt / equity.replace(0, np.nan)).rolling(21).kurt().diff(3).rolling(21).mean()).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc065_21d_2nd_derivative_v065_signal'] = f70le_f70_liabilities_to_equity_momentum_calc065_21d_2nd_derivative_v065_signal

def f70le_f70_liabilities_to_equity_momentum_calc066_42d_2nd_derivative_v066_signal(debt, equity):
    res = ((debt / equity.replace(0, np.nan)).rolling(42).kurt().diff(3).rolling(42).mean()).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc066_42d_2nd_derivative_v066_signal'] = f70le_f70_liabilities_to_equity_momentum_calc066_42d_2nd_derivative_v066_signal

def f70le_f70_liabilities_to_equity_momentum_calc067_63d_2nd_derivative_v067_signal(debt, equity):
    res = ((debt / equity.replace(0, np.nan)).rolling(63).kurt().diff(3).rolling(63).mean()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc067_63d_2nd_derivative_v067_signal'] = f70le_f70_liabilities_to_equity_momentum_calc067_63d_2nd_derivative_v067_signal

def f70le_f70_liabilities_to_equity_momentum_calc068_126d_2nd_derivative_v068_signal(debt, equity):
    res = ((debt / equity.replace(0, np.nan)).rolling(126).kurt().diff(3).rolling(126).mean()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc068_126d_2nd_derivative_v068_signal'] = f70le_f70_liabilities_to_equity_momentum_calc068_126d_2nd_derivative_v068_signal

def f70le_f70_liabilities_to_equity_momentum_calc069_252d_2nd_derivative_v069_signal(debt, equity):
    res = ((debt / equity.replace(0, np.nan)).rolling(252).kurt().diff(3).rolling(252).mean()).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc069_252d_2nd_derivative_v069_signal'] = f70le_f70_liabilities_to_equity_momentum_calc069_252d_2nd_derivative_v069_signal

def f70le_f70_liabilities_to_equity_momentum_calc070_5d_2nd_derivative_v070_signal(debt, equity):
    res = ((debt / equity.replace(0, np.nan)).rolling(5).kurt().diff(3).rolling(5).mean()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc070_5d_2nd_derivative_v070_signal'] = f70le_f70_liabilities_to_equity_momentum_calc070_5d_2nd_derivative_v070_signal

def f70le_f70_liabilities_to_equity_momentum_calc071_10d_2nd_derivative_v071_signal(liabilities, equity, marketcap):
    res = ((liabilities / marketcap.replace(0, np.nan)).rolling(10).std() / (equity / marketcap.replace(0, np.nan)).rolling(10).std().replace(0, np.nan)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc071_10d_2nd_derivative_v071_signal'] = f70le_f70_liabilities_to_equity_momentum_calc071_10d_2nd_derivative_v071_signal

def f70le_f70_liabilities_to_equity_momentum_calc072_21d_2nd_derivative_v072_signal(liabilities, equity, marketcap):
    res = ((liabilities / marketcap.replace(0, np.nan)).rolling(21).std() / (equity / marketcap.replace(0, np.nan)).rolling(21).std().replace(0, np.nan)).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc072_21d_2nd_derivative_v072_signal'] = f70le_f70_liabilities_to_equity_momentum_calc072_21d_2nd_derivative_v072_signal

def f70le_f70_liabilities_to_equity_momentum_calc073_42d_2nd_derivative_v073_signal(liabilities, equity, marketcap):
    res = ((liabilities / marketcap.replace(0, np.nan)).rolling(42).std() / (equity / marketcap.replace(0, np.nan)).rolling(42).std().replace(0, np.nan)).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc073_42d_2nd_derivative_v073_signal'] = f70le_f70_liabilities_to_equity_momentum_calc073_42d_2nd_derivative_v073_signal

def f70le_f70_liabilities_to_equity_momentum_calc074_63d_2nd_derivative_v074_signal(liabilities, equity, marketcap):
    res = ((liabilities / marketcap.replace(0, np.nan)).rolling(63).std() / (equity / marketcap.replace(0, np.nan)).rolling(63).std().replace(0, np.nan)).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc074_63d_2nd_derivative_v074_signal'] = f70le_f70_liabilities_to_equity_momentum_calc074_63d_2nd_derivative_v074_signal

def f70le_f70_liabilities_to_equity_momentum_calc075_126d_2nd_derivative_v075_signal(liabilities, equity, marketcap):
    res = ((liabilities / marketcap.replace(0, np.nan)).rolling(126).std() / (equity / marketcap.replace(0, np.nan)).rolling(126).std().replace(0, np.nan)).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc075_126d_2nd_derivative_v075_signal'] = f70le_f70_liabilities_to_equity_momentum_calc075_126d_2nd_derivative_v075_signal

def f70le_f70_liabilities_to_equity_momentum_calc076_252d_2nd_derivative_v076_signal(liabilities, equity, marketcap):
    res = ((liabilities / marketcap.replace(0, np.nan)).rolling(252).std() / (equity / marketcap.replace(0, np.nan)).rolling(252).std().replace(0, np.nan)).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc076_252d_2nd_derivative_v076_signal'] = f70le_f70_liabilities_to_equity_momentum_calc076_252d_2nd_derivative_v076_signal

def f70le_f70_liabilities_to_equity_momentum_calc077_5d_2nd_derivative_v077_signal(liabilities, equity, marketcap):
    res = ((liabilities / marketcap.replace(0, np.nan)).rolling(5).std() / (equity / marketcap.replace(0, np.nan)).rolling(5).std().replace(0, np.nan)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc077_5d_2nd_derivative_v077_signal'] = f70le_f70_liabilities_to_equity_momentum_calc077_5d_2nd_derivative_v077_signal

def f70le_f70_liabilities_to_equity_momentum_calc078_10d_2nd_derivative_v078_signal(liabilities, equity, marketcap):
    res = ((liabilities / marketcap.replace(0, np.nan)).rolling(10).std() / (equity / marketcap.replace(0, np.nan)).rolling(10).std().replace(0, np.nan)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc078_10d_2nd_derivative_v078_signal'] = f70le_f70_liabilities_to_equity_momentum_calc078_10d_2nd_derivative_v078_signal

def f70le_f70_liabilities_to_equity_momentum_calc079_21d_2nd_derivative_v079_signal(liabilities, equity, marketcap):
    res = ((liabilities / marketcap.replace(0, np.nan)).rolling(21).std() / (equity / marketcap.replace(0, np.nan)).rolling(21).std().replace(0, np.nan)).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc079_21d_2nd_derivative_v079_signal'] = f70le_f70_liabilities_to_equity_momentum_calc079_21d_2nd_derivative_v079_signal

def f70le_f70_liabilities_to_equity_momentum_calc080_42d_2nd_derivative_v080_signal(liabilities, equity, marketcap):
    res = ((liabilities / marketcap.replace(0, np.nan)).rolling(42).std() / (equity / marketcap.replace(0, np.nan)).rolling(42).std().replace(0, np.nan)).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc080_42d_2nd_derivative_v080_signal'] = f70le_f70_liabilities_to_equity_momentum_calc080_42d_2nd_derivative_v080_signal

def f70le_f70_liabilities_to_equity_momentum_calc081_63d_2nd_derivative_v081_signal(liabilities, equity, debt):
    res = (((liabilities + debt) / equity.replace(0, np.nan)).rolling(63).mean().diff(100).rolling(63).std()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc081_63d_2nd_derivative_v081_signal'] = f70le_f70_liabilities_to_equity_momentum_calc081_63d_2nd_derivative_v081_signal

def f70le_f70_liabilities_to_equity_momentum_calc082_126d_2nd_derivative_v082_signal(liabilities, equity, debt):
    res = (((liabilities + debt) / equity.replace(0, np.nan)).rolling(126).mean().diff(150).rolling(126).std()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc082_126d_2nd_derivative_v082_signal'] = f70le_f70_liabilities_to_equity_momentum_calc082_126d_2nd_derivative_v082_signal

def f70le_f70_liabilities_to_equity_momentum_calc083_252d_2nd_derivative_v083_signal(liabilities, equity, debt):
    res = (((liabilities + debt) / equity.replace(0, np.nan)).rolling(252).mean().diff(200).rolling(252).std()).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc083_252d_2nd_derivative_v083_signal'] = f70le_f70_liabilities_to_equity_momentum_calc083_252d_2nd_derivative_v083_signal

def f70le_f70_liabilities_to_equity_momentum_calc084_5d_2nd_derivative_v084_signal(liabilities, equity, debt):
    res = (((liabilities + debt) / equity.replace(0, np.nan)).rolling(5).mean().diff(15).rolling(5).std()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc084_5d_2nd_derivative_v084_signal'] = f70le_f70_liabilities_to_equity_momentum_calc084_5d_2nd_derivative_v084_signal

def f70le_f70_liabilities_to_equity_momentum_calc085_10d_2nd_derivative_v085_signal(liabilities, equity, debt):
    res = (((liabilities + debt) / equity.replace(0, np.nan)).rolling(10).mean().diff(30).rolling(10).std()).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc085_10d_2nd_derivative_v085_signal'] = f70le_f70_liabilities_to_equity_momentum_calc085_10d_2nd_derivative_v085_signal

def f70le_f70_liabilities_to_equity_momentum_calc086_21d_2nd_derivative_v086_signal(liabilities, equity, debt):
    res = (((liabilities + debt) / equity.replace(0, np.nan)).rolling(21).mean().diff(50).rolling(21).std()).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc086_21d_2nd_derivative_v086_signal'] = f70le_f70_liabilities_to_equity_momentum_calc086_21d_2nd_derivative_v086_signal

def f70le_f70_liabilities_to_equity_momentum_calc087_42d_2nd_derivative_v087_signal(liabilities, equity, debt):
    res = (((liabilities + debt) / equity.replace(0, np.nan)).rolling(42).mean().diff(80).rolling(42).std()).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc087_42d_2nd_derivative_v087_signal'] = f70le_f70_liabilities_to_equity_momentum_calc087_42d_2nd_derivative_v087_signal

def f70le_f70_liabilities_to_equity_momentum_calc088_63d_2nd_derivative_v088_signal(liabilities, equity, debt):
    res = (((liabilities + debt) / equity.replace(0, np.nan)).rolling(63).mean().diff(100).rolling(63).std()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc088_63d_2nd_derivative_v088_signal'] = f70le_f70_liabilities_to_equity_momentum_calc088_63d_2nd_derivative_v088_signal

def f70le_f70_liabilities_to_equity_momentum_calc089_126d_2nd_derivative_v089_signal(liabilities, equity, debt):
    res = (((liabilities + debt) / equity.replace(0, np.nan)).rolling(126).mean().diff(150).rolling(126).std()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc089_126d_2nd_derivative_v089_signal'] = f70le_f70_liabilities_to_equity_momentum_calc089_126d_2nd_derivative_v089_signal

def f70le_f70_liabilities_to_equity_momentum_calc090_252d_2nd_derivative_v090_signal(liabilities, equity, debt):
    res = (((liabilities + debt) / equity.replace(0, np.nan)).rolling(252).mean().diff(200).rolling(252).std()).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc090_252d_2nd_derivative_v090_signal'] = f70le_f70_liabilities_to_equity_momentum_calc090_252d_2nd_derivative_v090_signal

def f70le_f70_liabilities_to_equity_momentum_calc091_5d_2nd_derivative_v091_signal(liabilities, assets):
    res = ((liabilities / (assets - liabilities).replace(0, np.nan)).rolling(5).quantile(0.5).pct_change(10)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc091_5d_2nd_derivative_v091_signal'] = f70le_f70_liabilities_to_equity_momentum_calc091_5d_2nd_derivative_v091_signal

def f70le_f70_liabilities_to_equity_momentum_calc092_10d_2nd_derivative_v092_signal(liabilities, assets):
    res = ((liabilities / (assets - liabilities).replace(0, np.nan)).rolling(10).quantile(0.5).pct_change(10)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc092_10d_2nd_derivative_v092_signal'] = f70le_f70_liabilities_to_equity_momentum_calc092_10d_2nd_derivative_v092_signal

def f70le_f70_liabilities_to_equity_momentum_calc093_21d_2nd_derivative_v093_signal(liabilities, assets):
    res = ((liabilities / (assets - liabilities).replace(0, np.nan)).rolling(21).quantile(0.5).pct_change(10)).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc093_21d_2nd_derivative_v093_signal'] = f70le_f70_liabilities_to_equity_momentum_calc093_21d_2nd_derivative_v093_signal

def f70le_f70_liabilities_to_equity_momentum_calc094_42d_2nd_derivative_v094_signal(liabilities, assets):
    res = ((liabilities / (assets - liabilities).replace(0, np.nan)).rolling(42).quantile(0.5).pct_change(10)).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc094_42d_2nd_derivative_v094_signal'] = f70le_f70_liabilities_to_equity_momentum_calc094_42d_2nd_derivative_v094_signal

def f70le_f70_liabilities_to_equity_momentum_calc095_63d_2nd_derivative_v095_signal(liabilities, assets):
    res = ((liabilities / (assets - liabilities).replace(0, np.nan)).rolling(63).quantile(0.5).pct_change(10)).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc095_63d_2nd_derivative_v095_signal'] = f70le_f70_liabilities_to_equity_momentum_calc095_63d_2nd_derivative_v095_signal

def f70le_f70_liabilities_to_equity_momentum_calc096_126d_2nd_derivative_v096_signal(liabilities, assets):
    res = ((liabilities / (assets - liabilities).replace(0, np.nan)).rolling(126).quantile(0.5).pct_change(10)).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc096_126d_2nd_derivative_v096_signal'] = f70le_f70_liabilities_to_equity_momentum_calc096_126d_2nd_derivative_v096_signal

def f70le_f70_liabilities_to_equity_momentum_calc097_252d_2nd_derivative_v097_signal(liabilities, assets):
    res = ((liabilities / (assets - liabilities).replace(0, np.nan)).rolling(252).quantile(0.5).pct_change(10)).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc097_252d_2nd_derivative_v097_signal'] = f70le_f70_liabilities_to_equity_momentum_calc097_252d_2nd_derivative_v097_signal

def f70le_f70_liabilities_to_equity_momentum_calc098_5d_2nd_derivative_v098_signal(liabilities, assets):
    res = ((liabilities / (assets - liabilities).replace(0, np.nan)).rolling(5).quantile(0.5).pct_change(10)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc098_5d_2nd_derivative_v098_signal'] = f70le_f70_liabilities_to_equity_momentum_calc098_5d_2nd_derivative_v098_signal

def f70le_f70_liabilities_to_equity_momentum_calc099_10d_2nd_derivative_v099_signal(liabilities, assets):
    res = ((liabilities / (assets - liabilities).replace(0, np.nan)).rolling(10).quantile(0.5).pct_change(10)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc099_10d_2nd_derivative_v099_signal'] = f70le_f70_liabilities_to_equity_momentum_calc099_10d_2nd_derivative_v099_signal

def f70le_f70_liabilities_to_equity_momentum_calc100_21d_2nd_derivative_v100_signal(liabilities, assets):
    res = ((liabilities / (assets - liabilities).replace(0, np.nan)).rolling(21).quantile(0.5).pct_change(10)).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc100_21d_2nd_derivative_v100_signal'] = f70le_f70_liabilities_to_equity_momentum_calc100_21d_2nd_derivative_v100_signal

def f70le_f70_liabilities_to_equity_momentum_calc101_42d_2nd_derivative_v101_signal(liabilities, equity, revenue):
    res = ((liabilities / revenue.replace(0, np.nan)).pct_change(42) - (equity / revenue.replace(0, np.nan)).pct_change(42).rolling(42).mean()).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc101_42d_2nd_derivative_v101_signal'] = f70le_f70_liabilities_to_equity_momentum_calc101_42d_2nd_derivative_v101_signal

def f70le_f70_liabilities_to_equity_momentum_calc102_63d_2nd_derivative_v102_signal(liabilities, equity, revenue):
    res = ((liabilities / revenue.replace(0, np.nan)).pct_change(63) - (equity / revenue.replace(0, np.nan)).pct_change(63).rolling(63).mean()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc102_63d_2nd_derivative_v102_signal'] = f70le_f70_liabilities_to_equity_momentum_calc102_63d_2nd_derivative_v102_signal

def f70le_f70_liabilities_to_equity_momentum_calc103_126d_2nd_derivative_v103_signal(liabilities, equity, revenue):
    res = ((liabilities / revenue.replace(0, np.nan)).pct_change(126) - (equity / revenue.replace(0, np.nan)).pct_change(126).rolling(126).mean()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc103_126d_2nd_derivative_v103_signal'] = f70le_f70_liabilities_to_equity_momentum_calc103_126d_2nd_derivative_v103_signal

def f70le_f70_liabilities_to_equity_momentum_calc104_252d_2nd_derivative_v104_signal(liabilities, equity, revenue):
    res = ((liabilities / revenue.replace(0, np.nan)).pct_change(252) - (equity / revenue.replace(0, np.nan)).pct_change(252).rolling(252).mean()).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc104_252d_2nd_derivative_v104_signal'] = f70le_f70_liabilities_to_equity_momentum_calc104_252d_2nd_derivative_v104_signal

def f70le_f70_liabilities_to_equity_momentum_calc105_5d_2nd_derivative_v105_signal(liabilities, equity, revenue):
    res = ((liabilities / revenue.replace(0, np.nan)).pct_change(5) - (equity / revenue.replace(0, np.nan)).pct_change(5).rolling(5).mean()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc105_5d_2nd_derivative_v105_signal'] = f70le_f70_liabilities_to_equity_momentum_calc105_5d_2nd_derivative_v105_signal

def f70le_f70_liabilities_to_equity_momentum_calc106_10d_2nd_derivative_v106_signal(liabilities, equity, revenue):
    res = ((liabilities / revenue.replace(0, np.nan)).pct_change(10) - (equity / revenue.replace(0, np.nan)).pct_change(10).rolling(10).mean()).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc106_10d_2nd_derivative_v106_signal'] = f70le_f70_liabilities_to_equity_momentum_calc106_10d_2nd_derivative_v106_signal

def f70le_f70_liabilities_to_equity_momentum_calc107_21d_2nd_derivative_v107_signal(liabilities, equity, revenue):
    res = ((liabilities / revenue.replace(0, np.nan)).pct_change(21) - (equity / revenue.replace(0, np.nan)).pct_change(21).rolling(21).mean()).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc107_21d_2nd_derivative_v107_signal'] = f70le_f70_liabilities_to_equity_momentum_calc107_21d_2nd_derivative_v107_signal

def f70le_f70_liabilities_to_equity_momentum_calc108_42d_2nd_derivative_v108_signal(liabilities, equity, revenue):
    res = ((liabilities / revenue.replace(0, np.nan)).pct_change(42) - (equity / revenue.replace(0, np.nan)).pct_change(42).rolling(42).mean()).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc108_42d_2nd_derivative_v108_signal'] = f70le_f70_liabilities_to_equity_momentum_calc108_42d_2nd_derivative_v108_signal

def f70le_f70_liabilities_to_equity_momentum_calc109_63d_2nd_derivative_v109_signal(liabilities, equity, revenue):
    res = ((liabilities / revenue.replace(0, np.nan)).pct_change(63) - (equity / revenue.replace(0, np.nan)).pct_change(63).rolling(63).mean()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc109_63d_2nd_derivative_v109_signal'] = f70le_f70_liabilities_to_equity_momentum_calc109_63d_2nd_derivative_v109_signal

def f70le_f70_liabilities_to_equity_momentum_calc110_126d_2nd_derivative_v110_signal(liabilities, equity, revenue):
    res = ((liabilities / revenue.replace(0, np.nan)).pct_change(126) - (equity / revenue.replace(0, np.nan)).pct_change(126).rolling(126).mean()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc110_126d_2nd_derivative_v110_signal'] = f70le_f70_liabilities_to_equity_momentum_calc110_126d_2nd_derivative_v110_signal

def f70le_f70_liabilities_to_equity_momentum_calc111_252d_2nd_derivative_v111_signal(liabilities, equity, netinc):
    res = ((liabilities / netinc.replace(0, np.nan).abs()).rolling(252).mean() / (equity / netinc.replace(0, np.nan).abs()).rolling(252).mean().replace(0, np.nan)).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc111_252d_2nd_derivative_v111_signal'] = f70le_f70_liabilities_to_equity_momentum_calc111_252d_2nd_derivative_v111_signal

def f70le_f70_liabilities_to_equity_momentum_calc112_5d_2nd_derivative_v112_signal(liabilities, equity, netinc):
    res = ((liabilities / netinc.replace(0, np.nan).abs()).rolling(5).mean() / (equity / netinc.replace(0, np.nan).abs()).rolling(5).mean().replace(0, np.nan)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc112_5d_2nd_derivative_v112_signal'] = f70le_f70_liabilities_to_equity_momentum_calc112_5d_2nd_derivative_v112_signal

def f70le_f70_liabilities_to_equity_momentum_calc113_10d_2nd_derivative_v113_signal(liabilities, equity, netinc):
    res = ((liabilities / netinc.replace(0, np.nan).abs()).rolling(10).mean() / (equity / netinc.replace(0, np.nan).abs()).rolling(10).mean().replace(0, np.nan)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc113_10d_2nd_derivative_v113_signal'] = f70le_f70_liabilities_to_equity_momentum_calc113_10d_2nd_derivative_v113_signal

def f70le_f70_liabilities_to_equity_momentum_calc114_21d_2nd_derivative_v114_signal(liabilities, equity, netinc):
    res = ((liabilities / netinc.replace(0, np.nan).abs()).rolling(21).mean() / (equity / netinc.replace(0, np.nan).abs()).rolling(21).mean().replace(0, np.nan)).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc114_21d_2nd_derivative_v114_signal'] = f70le_f70_liabilities_to_equity_momentum_calc114_21d_2nd_derivative_v114_signal

def f70le_f70_liabilities_to_equity_momentum_calc115_42d_2nd_derivative_v115_signal(liabilities, equity, netinc):
    res = ((liabilities / netinc.replace(0, np.nan).abs()).rolling(42).mean() / (equity / netinc.replace(0, np.nan).abs()).rolling(42).mean().replace(0, np.nan)).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc115_42d_2nd_derivative_v115_signal'] = f70le_f70_liabilities_to_equity_momentum_calc115_42d_2nd_derivative_v115_signal

def f70le_f70_liabilities_to_equity_momentum_calc116_63d_2nd_derivative_v116_signal(liabilities, equity, netinc):
    res = ((liabilities / netinc.replace(0, np.nan).abs()).rolling(63).mean() / (equity / netinc.replace(0, np.nan).abs()).rolling(63).mean().replace(0, np.nan)).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc116_63d_2nd_derivative_v116_signal'] = f70le_f70_liabilities_to_equity_momentum_calc116_63d_2nd_derivative_v116_signal

def f70le_f70_liabilities_to_equity_momentum_calc117_126d_2nd_derivative_v117_signal(liabilities, equity, netinc):
    res = ((liabilities / netinc.replace(0, np.nan).abs()).rolling(126).mean() / (equity / netinc.replace(0, np.nan).abs()).rolling(126).mean().replace(0, np.nan)).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc117_126d_2nd_derivative_v117_signal'] = f70le_f70_liabilities_to_equity_momentum_calc117_126d_2nd_derivative_v117_signal

def f70le_f70_liabilities_to_equity_momentum_calc118_252d_2nd_derivative_v118_signal(liabilities, equity, netinc):
    res = ((liabilities / netinc.replace(0, np.nan).abs()).rolling(252).mean() / (equity / netinc.replace(0, np.nan).abs()).rolling(252).mean().replace(0, np.nan)).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc118_252d_2nd_derivative_v118_signal'] = f70le_f70_liabilities_to_equity_momentum_calc118_252d_2nd_derivative_v118_signal

def f70le_f70_liabilities_to_equity_momentum_calc119_5d_2nd_derivative_v119_signal(liabilities, equity, netinc):
    res = ((liabilities / netinc.replace(0, np.nan).abs()).rolling(5).mean() / (equity / netinc.replace(0, np.nan).abs()).rolling(5).mean().replace(0, np.nan)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc119_5d_2nd_derivative_v119_signal'] = f70le_f70_liabilities_to_equity_momentum_calc119_5d_2nd_derivative_v119_signal

def f70le_f70_liabilities_to_equity_momentum_calc120_10d_2nd_derivative_v120_signal(liabilities, equity, netinc):
    res = ((liabilities / netinc.replace(0, np.nan).abs()).rolling(10).mean() / (equity / netinc.replace(0, np.nan).abs()).rolling(10).mean().replace(0, np.nan)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc120_10d_2nd_derivative_v120_signal'] = f70le_f70_liabilities_to_equity_momentum_calc120_10d_2nd_derivative_v120_signal

def f70le_f70_liabilities_to_equity_momentum_calc121_21d_2nd_derivative_v121_signal(liabilities, ebitda):
    res = ((liabilities / ebitda.replace(0, np.nan).abs()).rolling(21).std().pct_change(50).rolling(21).mean()).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc121_21d_2nd_derivative_v121_signal'] = f70le_f70_liabilities_to_equity_momentum_calc121_21d_2nd_derivative_v121_signal

def f70le_f70_liabilities_to_equity_momentum_calc122_42d_2nd_derivative_v122_signal(liabilities, ebitda):
    res = ((liabilities / ebitda.replace(0, np.nan).abs()).rolling(42).std().pct_change(80).rolling(42).mean()).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc122_42d_2nd_derivative_v122_signal'] = f70le_f70_liabilities_to_equity_momentum_calc122_42d_2nd_derivative_v122_signal

def f70le_f70_liabilities_to_equity_momentum_calc123_63d_2nd_derivative_v123_signal(liabilities, ebitda):
    res = ((liabilities / ebitda.replace(0, np.nan).abs()).rolling(63).std().pct_change(100).rolling(63).mean()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc123_63d_2nd_derivative_v123_signal'] = f70le_f70_liabilities_to_equity_momentum_calc123_63d_2nd_derivative_v123_signal

def f70le_f70_liabilities_to_equity_momentum_calc124_126d_2nd_derivative_v124_signal(liabilities, ebitda):
    res = ((liabilities / ebitda.replace(0, np.nan).abs()).rolling(126).std().pct_change(150).rolling(126).mean()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc124_126d_2nd_derivative_v124_signal'] = f70le_f70_liabilities_to_equity_momentum_calc124_126d_2nd_derivative_v124_signal

def f70le_f70_liabilities_to_equity_momentum_calc125_252d_2nd_derivative_v125_signal(liabilities, ebitda):
    res = ((liabilities / ebitda.replace(0, np.nan).abs()).rolling(252).std().pct_change(200).rolling(252).mean()).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc125_252d_2nd_derivative_v125_signal'] = f70le_f70_liabilities_to_equity_momentum_calc125_252d_2nd_derivative_v125_signal

def f70le_f70_liabilities_to_equity_momentum_calc126_5d_2nd_derivative_v126_signal(liabilities, ebitda):
    res = ((liabilities / ebitda.replace(0, np.nan).abs()).rolling(5).std().pct_change(15).rolling(5).mean()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc126_5d_2nd_derivative_v126_signal'] = f70le_f70_liabilities_to_equity_momentum_calc126_5d_2nd_derivative_v126_signal

def f70le_f70_liabilities_to_equity_momentum_calc127_10d_2nd_derivative_v127_signal(liabilities, ebitda):
    res = ((liabilities / ebitda.replace(0, np.nan).abs()).rolling(10).std().pct_change(30).rolling(10).mean()).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc127_10d_2nd_derivative_v127_signal'] = f70le_f70_liabilities_to_equity_momentum_calc127_10d_2nd_derivative_v127_signal

def f70le_f70_liabilities_to_equity_momentum_calc128_21d_2nd_derivative_v128_signal(liabilities, ebitda):
    res = ((liabilities / ebitda.replace(0, np.nan).abs()).rolling(21).std().pct_change(50).rolling(21).mean()).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc128_21d_2nd_derivative_v128_signal'] = f70le_f70_liabilities_to_equity_momentum_calc128_21d_2nd_derivative_v128_signal

def f70le_f70_liabilities_to_equity_momentum_calc129_42d_2nd_derivative_v129_signal(liabilities, ebitda):
    res = ((liabilities / ebitda.replace(0, np.nan).abs()).rolling(42).std().pct_change(80).rolling(42).mean()).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc129_42d_2nd_derivative_v129_signal'] = f70le_f70_liabilities_to_equity_momentum_calc129_42d_2nd_derivative_v129_signal

def f70le_f70_liabilities_to_equity_momentum_calc130_63d_2nd_derivative_v130_signal(liabilities, ebitda):
    res = ((liabilities / ebitda.replace(0, np.nan).abs()).rolling(63).std().pct_change(100).rolling(63).mean()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc130_63d_2nd_derivative_v130_signal'] = f70le_f70_liabilities_to_equity_momentum_calc130_63d_2nd_derivative_v130_signal

def f70le_f70_liabilities_to_equity_momentum_calc131_126d_2nd_derivative_v131_signal(liabilities, equity, workingcapital):
    res = ((liabilities / workingcapital.replace(0, np.nan)).rolling(126).mean() - (equity / workingcapital.replace(0, np.nan)).rolling(126).mean().rolling(126).std()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc131_126d_2nd_derivative_v131_signal'] = f70le_f70_liabilities_to_equity_momentum_calc131_126d_2nd_derivative_v131_signal

def f70le_f70_liabilities_to_equity_momentum_calc132_252d_2nd_derivative_v132_signal(liabilities, equity, workingcapital):
    res = ((liabilities / workingcapital.replace(0, np.nan)).rolling(252).mean() - (equity / workingcapital.replace(0, np.nan)).rolling(252).mean().rolling(252).std()).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc132_252d_2nd_derivative_v132_signal'] = f70le_f70_liabilities_to_equity_momentum_calc132_252d_2nd_derivative_v132_signal

def f70le_f70_liabilities_to_equity_momentum_calc133_5d_2nd_derivative_v133_signal(liabilities, equity, workingcapital):
    res = ((liabilities / workingcapital.replace(0, np.nan)).rolling(5).mean() - (equity / workingcapital.replace(0, np.nan)).rolling(5).mean().rolling(5).std()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc133_5d_2nd_derivative_v133_signal'] = f70le_f70_liabilities_to_equity_momentum_calc133_5d_2nd_derivative_v133_signal

def f70le_f70_liabilities_to_equity_momentum_calc134_10d_2nd_derivative_v134_signal(liabilities, equity, workingcapital):
    res = ((liabilities / workingcapital.replace(0, np.nan)).rolling(10).mean() - (equity / workingcapital.replace(0, np.nan)).rolling(10).mean().rolling(10).std()).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc134_10d_2nd_derivative_v134_signal'] = f70le_f70_liabilities_to_equity_momentum_calc134_10d_2nd_derivative_v134_signal

def f70le_f70_liabilities_to_equity_momentum_calc135_21d_2nd_derivative_v135_signal(liabilities, equity, workingcapital):
    res = ((liabilities / workingcapital.replace(0, np.nan)).rolling(21).mean() - (equity / workingcapital.replace(0, np.nan)).rolling(21).mean().rolling(21).std()).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc135_21d_2nd_derivative_v135_signal'] = f70le_f70_liabilities_to_equity_momentum_calc135_21d_2nd_derivative_v135_signal

def f70le_f70_liabilities_to_equity_momentum_calc136_42d_2nd_derivative_v136_signal(liabilities, equity, workingcapital):
    res = ((liabilities / workingcapital.replace(0, np.nan)).rolling(42).mean() - (equity / workingcapital.replace(0, np.nan)).rolling(42).mean().rolling(42).std()).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc136_42d_2nd_derivative_v136_signal'] = f70le_f70_liabilities_to_equity_momentum_calc136_42d_2nd_derivative_v136_signal

def f70le_f70_liabilities_to_equity_momentum_calc137_63d_2nd_derivative_v137_signal(liabilities, equity, workingcapital):
    res = ((liabilities / workingcapital.replace(0, np.nan)).rolling(63).mean() - (equity / workingcapital.replace(0, np.nan)).rolling(63).mean().rolling(63).std()).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc137_63d_2nd_derivative_v137_signal'] = f70le_f70_liabilities_to_equity_momentum_calc137_63d_2nd_derivative_v137_signal

def f70le_f70_liabilities_to_equity_momentum_calc138_126d_2nd_derivative_v138_signal(liabilities, equity, workingcapital):
    res = ((liabilities / workingcapital.replace(0, np.nan)).rolling(126).mean() - (equity / workingcapital.replace(0, np.nan)).rolling(126).mean().rolling(126).std()).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc138_126d_2nd_derivative_v138_signal'] = f70le_f70_liabilities_to_equity_momentum_calc138_126d_2nd_derivative_v138_signal

def f70le_f70_liabilities_to_equity_momentum_calc139_252d_2nd_derivative_v139_signal(liabilities, equity, workingcapital):
    res = ((liabilities / workingcapital.replace(0, np.nan)).rolling(252).mean() - (equity / workingcapital.replace(0, np.nan)).rolling(252).mean().rolling(252).std()).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc139_252d_2nd_derivative_v139_signal'] = f70le_f70_liabilities_to_equity_momentum_calc139_252d_2nd_derivative_v139_signal

def f70le_f70_liabilities_to_equity_momentum_calc140_5d_2nd_derivative_v140_signal(liabilities, equity, workingcapital):
    res = ((liabilities / workingcapital.replace(0, np.nan)).rolling(5).mean() - (equity / workingcapital.replace(0, np.nan)).rolling(5).mean().rolling(5).std()).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc140_5d_2nd_derivative_v140_signal'] = f70le_f70_liabilities_to_equity_momentum_calc140_5d_2nd_derivative_v140_signal

def f70le_f70_liabilities_to_equity_momentum_calc141_10d_2nd_derivative_v141_signal(liabilities, equity):
    res = ((liabilities.pct_change(10) / equity.pct_change(10).replace(0, np.nan)).rolling(30).mean().diff(5)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc141_10d_2nd_derivative_v141_signal'] = f70le_f70_liabilities_to_equity_momentum_calc141_10d_2nd_derivative_v141_signal

def f70le_f70_liabilities_to_equity_momentum_calc142_21d_2nd_derivative_v142_signal(liabilities, equity):
    res = ((liabilities.pct_change(21) / equity.pct_change(21).replace(0, np.nan)).rolling(50).mean().diff(5)).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc142_21d_2nd_derivative_v142_signal'] = f70le_f70_liabilities_to_equity_momentum_calc142_21d_2nd_derivative_v142_signal

def f70le_f70_liabilities_to_equity_momentum_calc143_42d_2nd_derivative_v143_signal(liabilities, equity):
    res = ((liabilities.pct_change(42) / equity.pct_change(42).replace(0, np.nan)).rolling(80).mean().diff(5)).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc143_42d_2nd_derivative_v143_signal'] = f70le_f70_liabilities_to_equity_momentum_calc143_42d_2nd_derivative_v143_signal

def f70le_f70_liabilities_to_equity_momentum_calc144_63d_2nd_derivative_v144_signal(liabilities, equity):
    res = ((liabilities.pct_change(63) / equity.pct_change(63).replace(0, np.nan)).rolling(100).mean().diff(5)).diff(1).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc144_63d_2nd_derivative_v144_signal'] = f70le_f70_liabilities_to_equity_momentum_calc144_63d_2nd_derivative_v144_signal

def f70le_f70_liabilities_to_equity_momentum_calc145_126d_2nd_derivative_v145_signal(liabilities, equity):
    res = ((liabilities.pct_change(126) / equity.pct_change(126).replace(0, np.nan)).rolling(150).mean().diff(5)).diff(1).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc145_126d_2nd_derivative_v145_signal'] = f70le_f70_liabilities_to_equity_momentum_calc145_126d_2nd_derivative_v145_signal

def f70le_f70_liabilities_to_equity_momentum_calc146_252d_2nd_derivative_v146_signal(liabilities, equity):
    res = ((liabilities.pct_change(252) / equity.pct_change(252).replace(0, np.nan)).rolling(200).mean().diff(5)).diff(1).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc146_252d_2nd_derivative_v146_signal'] = f70le_f70_liabilities_to_equity_momentum_calc146_252d_2nd_derivative_v146_signal

def f70le_f70_liabilities_to_equity_momentum_calc147_5d_2nd_derivative_v147_signal(liabilities, equity):
    res = ((liabilities.pct_change(5) / equity.pct_change(5).replace(0, np.nan)).rolling(15).mean().diff(5)).diff(1).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc147_5d_2nd_derivative_v147_signal'] = f70le_f70_liabilities_to_equity_momentum_calc147_5d_2nd_derivative_v147_signal

def f70le_f70_liabilities_to_equity_momentum_calc148_10d_2nd_derivative_v148_signal(liabilities, equity):
    res = ((liabilities.pct_change(10) / equity.pct_change(10).replace(0, np.nan)).rolling(30).mean().diff(5)).diff(1).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc148_10d_2nd_derivative_v148_signal'] = f70le_f70_liabilities_to_equity_momentum_calc148_10d_2nd_derivative_v148_signal

def f70le_f70_liabilities_to_equity_momentum_calc149_21d_2nd_derivative_v149_signal(liabilities, equity):
    res = ((liabilities.pct_change(21) / equity.pct_change(21).replace(0, np.nan)).rolling(50).mean().diff(5)).diff(1).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc149_21d_2nd_derivative_v149_signal'] = f70le_f70_liabilities_to_equity_momentum_calc149_21d_2nd_derivative_v149_signal

def f70le_f70_liabilities_to_equity_momentum_calc150_42d_2nd_derivative_v150_signal(liabilities, equity):
    res = ((liabilities.pct_change(42) / equity.pct_change(42).replace(0, np.nan)).rolling(80).mean().diff(5)).diff(1).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f70le_f70_liabilities_to_equity_momentum_calc150_42d_2nd_derivative_v150_signal'] = f70le_f70_liabilities_to_equity_momentum_calc150_42d_2nd_derivative_v150_signal

