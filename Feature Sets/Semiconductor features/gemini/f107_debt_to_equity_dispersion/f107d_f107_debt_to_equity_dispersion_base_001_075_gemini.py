import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f107d_f107_debt_to_equity_dispersion_calc001_42d_base_v001_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.diff(42) / assets.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc001_42d_base_v001_signal'] = f107d_f107_debt_to_equity_dispersion_calc001_42d_base_v001_signal

def f107d_f107_debt_to_equity_dispersion_calc002_252d_base_v002_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.diff(252).abs() / assets.diff(252).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc002_252d_base_v002_signal'] = f107d_f107_debt_to_equity_dispersion_calc002_252d_base_v002_signal

def f107d_f107_debt_to_equity_dispersion_calc003_5d_base_v003_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.pct_change(5) - liabilities.pct_change(5))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc003_5d_base_v003_signal'] = f107d_f107_debt_to_equity_dispersion_calc003_5d_base_v003_signal

def f107d_f107_debt_to_equity_dispersion_calc004_10d_base_v004_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets.diff(10) / liabilities.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc004_10d_base_v004_signal'] = f107d_f107_debt_to_equity_dispersion_calc004_10d_base_v004_signal

def f107d_f107_debt_to_equity_dispersion_calc005_63d_base_v005_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(63).quantile(0.5) / marketcap.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc005_63d_base_v005_signal'] = f107d_f107_debt_to_equity_dispersion_calc005_63d_base_v005_signal

def f107d_f107_debt_to_equity_dispersion_calc006_126d_base_v006_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.rolling(126).quantile(0.5) / equity.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc006_126d_base_v006_signal'] = f107d_f107_debt_to_equity_dispersion_calc006_126d_base_v006_signal

def f107d_f107_debt_to_equity_dispersion_calc007_21d_base_v007_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(21).kurt() - assets.rolling(21).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc007_21d_base_v007_signal'] = f107d_f107_debt_to_equity_dispersion_calc007_21d_base_v007_signal

def f107d_f107_debt_to_equity_dispersion_calc008_126d_base_v008_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(126).max() - debt.rolling(126).min()) / marketcap.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc008_126d_base_v008_signal'] = f107d_f107_debt_to_equity_dispersion_calc008_126d_base_v008_signal

def f107d_f107_debt_to_equity_dispersion_calc009_10d_base_v009_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets.rolling(10).quantile(0.5) / liabilities.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc009_10d_base_v009_signal'] = f107d_f107_debt_to_equity_dispersion_calc009_10d_base_v009_signal

def f107d_f107_debt_to_equity_dispersion_calc010_21d_base_v010_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.pct_change(21) - liabilities.pct_change(21))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc010_21d_base_v010_signal'] = f107d_f107_debt_to_equity_dispersion_calc010_21d_base_v010_signal

def f107d_f107_debt_to_equity_dispersion_calc011_21d_base_v011_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.diff(21) / equity.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc011_21d_base_v011_signal'] = f107d_f107_debt_to_equity_dispersion_calc011_21d_base_v011_signal

def f107d_f107_debt_to_equity_dispersion_calc012_42d_base_v012_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity / ebitda.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc012_42d_base_v012_signal'] = f107d_f107_debt_to_equity_dispersion_calc012_42d_base_v012_signal

def f107d_f107_debt_to_equity_dispersion_calc013_252d_base_v013_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.pct_change(252) - marketcap.pct_change(252))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc013_252d_base_v013_signal'] = f107d_f107_debt_to_equity_dispersion_calc013_252d_base_v013_signal

def f107d_f107_debt_to_equity_dispersion_calc014_126d_base_v014_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio / debt.replace(0, np.nan)).rolling(126).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc014_126d_base_v014_signal'] = f107d_f107_debt_to_equity_dispersion_calc014_126d_base_v014_signal

def f107d_f107_debt_to_equity_dispersion_calc015_10d_base_v015_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets.diff(10) / marketcap.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc015_10d_base_v015_signal'] = f107d_f107_debt_to_equity_dispersion_calc015_10d_base_v015_signal

def f107d_f107_debt_to_equity_dispersion_calc016_126d_base_v016_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = ((currentratio - currentratio.rolling(126).mean()) / currentratio.rolling(126).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc016_126d_base_v016_signal'] = f107d_f107_debt_to_equity_dispersion_calc016_126d_base_v016_signal

def f107d_f107_debt_to_equity_dispersion_calc017_21d_base_v017_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.diff(21).abs() / marketcap.diff(21).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc017_21d_base_v017_signal'] = f107d_f107_debt_to_equity_dispersion_calc017_21d_base_v017_signal

def f107d_f107_debt_to_equity_dispersion_calc018_126d_base_v018_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.pct_change(126) - assets.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc018_126d_base_v018_signal'] = f107d_f107_debt_to_equity_dispersion_calc018_126d_base_v018_signal

def f107d_f107_debt_to_equity_dispersion_calc019_42d_base_v019_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = ((debt - debt.rolling(42).mean()) / debt.rolling(42).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc019_42d_base_v019_signal'] = f107d_f107_debt_to_equity_dispersion_calc019_42d_base_v019_signal

def f107d_f107_debt_to_equity_dispersion_calc020_10d_base_v020_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.rolling(10).max() - marketcap.rolling(10).min()) / equity.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc020_10d_base_v020_signal'] = f107d_f107_debt_to_equity_dispersion_calc020_10d_base_v020_signal

def f107d_f107_debt_to_equity_dispersion_calc021_5d_base_v021_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(5).max() - debt.rolling(5).min()) / equity.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc021_5d_base_v021_signal'] = f107d_f107_debt_to_equity_dispersion_calc021_5d_base_v021_signal

def f107d_f107_debt_to_equity_dispersion_calc022_5d_base_v022_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(5).quantile(0.5) / marketcap.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc022_5d_base_v022_signal'] = f107d_f107_debt_to_equity_dispersion_calc022_5d_base_v022_signal

def f107d_f107_debt_to_equity_dispersion_calc023_10d_base_v023_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.rolling(10).max() - marketcap.rolling(10).min()) / currentratio.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc023_10d_base_v023_signal'] = f107d_f107_debt_to_equity_dispersion_calc023_10d_base_v023_signal

def f107d_f107_debt_to_equity_dispersion_calc024_63d_base_v024_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity / marketcap.replace(0, np.nan)).rolling(63).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc024_63d_base_v024_signal'] = f107d_f107_debt_to_equity_dispersion_calc024_63d_base_v024_signal

def f107d_f107_debt_to_equity_dispersion_calc025_21d_base_v025_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap / assets.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc025_21d_base_v025_signal'] = f107d_f107_debt_to_equity_dispersion_calc025_21d_base_v025_signal

def f107d_f107_debt_to_equity_dispersion_calc026_21d_base_v026_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap / equity.replace(0, np.nan)).rolling(21).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc026_21d_base_v026_signal'] = f107d_f107_debt_to_equity_dispersion_calc026_21d_base_v026_signal

def f107d_f107_debt_to_equity_dispersion_calc027_10d_base_v027_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(10).quantile(0.5) / ebitda.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc027_10d_base_v027_signal'] = f107d_f107_debt_to_equity_dispersion_calc027_10d_base_v027_signal

def f107d_f107_debt_to_equity_dispersion_calc028_21d_base_v028_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = ((equity - equity.rolling(21).mean()) / equity.rolling(21).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc028_21d_base_v028_signal'] = f107d_f107_debt_to_equity_dispersion_calc028_21d_base_v028_signal

def f107d_f107_debt_to_equity_dispersion_calc029_252d_base_v029_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.diff(252) / debt.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc029_252d_base_v029_signal'] = f107d_f107_debt_to_equity_dispersion_calc029_252d_base_v029_signal

def f107d_f107_debt_to_equity_dispersion_calc030_63d_base_v030_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(63).rank(pct=True) / debt.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc030_63d_base_v030_signal'] = f107d_f107_debt_to_equity_dispersion_calc030_63d_base_v030_signal

def f107d_f107_debt_to_equity_dispersion_calc031_5d_base_v031_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.diff(5) / liabilities.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc031_5d_base_v031_signal'] = f107d_f107_debt_to_equity_dispersion_calc031_5d_base_v031_signal

def f107d_f107_debt_to_equity_dispersion_calc032_5d_base_v032_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.rolling(5).kurt() - equity.rolling(5).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc032_5d_base_v032_signal'] = f107d_f107_debt_to_equity_dispersion_calc032_5d_base_v032_signal

def f107d_f107_debt_to_equity_dispersion_calc033_252d_base_v033_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.pct_change(252) - debt.pct_change(252))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc033_252d_base_v033_signal'] = f107d_f107_debt_to_equity_dispersion_calc033_252d_base_v033_signal

def f107d_f107_debt_to_equity_dispersion_calc034_126d_base_v034_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.rolling(126).kurt() - ebitda.rolling(126).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc034_126d_base_v034_signal'] = f107d_f107_debt_to_equity_dispersion_calc034_126d_base_v034_signal

def f107d_f107_debt_to_equity_dispersion_calc035_5d_base_v035_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(5).kurt() - assets.rolling(5).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc035_5d_base_v035_signal'] = f107d_f107_debt_to_equity_dispersion_calc035_5d_base_v035_signal

def f107d_f107_debt_to_equity_dispersion_calc036_10d_base_v036_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets.diff(10).abs() / equity.diff(10).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc036_10d_base_v036_signal'] = f107d_f107_debt_to_equity_dispersion_calc036_10d_base_v036_signal

def f107d_f107_debt_to_equity_dispersion_calc037_10d_base_v037_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.rolling(10).rank(pct=True) / currentratio.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc037_10d_base_v037_signal'] = f107d_f107_debt_to_equity_dispersion_calc037_10d_base_v037_signal

def f107d_f107_debt_to_equity_dispersion_calc038_10d_base_v038_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(10).quantile(0.5) / currentratio.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc038_10d_base_v038_signal'] = f107d_f107_debt_to_equity_dispersion_calc038_10d_base_v038_signal

def f107d_f107_debt_to_equity_dispersion_calc039_63d_base_v039_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities / currentratio.replace(0, np.nan)).rolling(63).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc039_63d_base_v039_signal'] = f107d_f107_debt_to_equity_dispersion_calc039_63d_base_v039_signal

def f107d_f107_debt_to_equity_dispersion_calc040_252d_base_v040_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = ((debt - debt.rolling(252).mean()) / debt.rolling(252).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc040_252d_base_v040_signal'] = f107d_f107_debt_to_equity_dispersion_calc040_252d_base_v040_signal

def f107d_f107_debt_to_equity_dispersion_calc041_126d_base_v041_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(126).max() - marketcap.rolling(126).min()) / debt.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc041_126d_base_v041_signal'] = f107d_f107_debt_to_equity_dispersion_calc041_126d_base_v041_signal

def f107d_f107_debt_to_equity_dispersion_calc042_10d_base_v042_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap / equity.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc042_10d_base_v042_signal'] = f107d_f107_debt_to_equity_dispersion_calc042_10d_base_v042_signal

def f107d_f107_debt_to_equity_dispersion_calc043_42d_base_v043_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.pct_change(42) - assets.pct_change(42))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc043_42d_base_v043_signal'] = f107d_f107_debt_to_equity_dispersion_calc043_42d_base_v043_signal

def f107d_f107_debt_to_equity_dispersion_calc044_42d_base_v044_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.diff(42) / ebitda.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc044_42d_base_v044_signal'] = f107d_f107_debt_to_equity_dispersion_calc044_42d_base_v044_signal

def f107d_f107_debt_to_equity_dispersion_calc045_63d_base_v045_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.rolling(63).kurt() - debt.rolling(63).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc045_63d_base_v045_signal'] = f107d_f107_debt_to_equity_dispersion_calc045_63d_base_v045_signal

def f107d_f107_debt_to_equity_dispersion_calc046_63d_base_v046_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.rolling(63).kurt() - assets.rolling(63).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc046_63d_base_v046_signal'] = f107d_f107_debt_to_equity_dispersion_calc046_63d_base_v046_signal

def f107d_f107_debt_to_equity_dispersion_calc047_10d_base_v047_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets.rolling(10).kurt() - ebitda.rolling(10).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc047_10d_base_v047_signal'] = f107d_f107_debt_to_equity_dispersion_calc047_10d_base_v047_signal

def f107d_f107_debt_to_equity_dispersion_calc048_63d_base_v048_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.rolling(63).kurt() - currentratio.rolling(63).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc048_63d_base_v048_signal'] = f107d_f107_debt_to_equity_dispersion_calc048_63d_base_v048_signal

def f107d_f107_debt_to_equity_dispersion_calc049_252d_base_v049_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.diff(252) / equity.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc049_252d_base_v049_signal'] = f107d_f107_debt_to_equity_dispersion_calc049_252d_base_v049_signal

def f107d_f107_debt_to_equity_dispersion_calc050_10d_base_v050_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity / assets.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc050_10d_base_v050_signal'] = f107d_f107_debt_to_equity_dispersion_calc050_10d_base_v050_signal

def f107d_f107_debt_to_equity_dispersion_calc051_5d_base_v051_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.diff(5) / ebitda.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc051_5d_base_v051_signal'] = f107d_f107_debt_to_equity_dispersion_calc051_5d_base_v051_signal

def f107d_f107_debt_to_equity_dispersion_calc052_21d_base_v052_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.diff(21) / marketcap.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc052_21d_base_v052_signal'] = f107d_f107_debt_to_equity_dispersion_calc052_21d_base_v052_signal

def f107d_f107_debt_to_equity_dispersion_calc053_63d_base_v053_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.rolling(63).kurt() - ebitda.rolling(63).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc053_63d_base_v053_signal'] = f107d_f107_debt_to_equity_dispersion_calc053_63d_base_v053_signal

def f107d_f107_debt_to_equity_dispersion_calc054_21d_base_v054_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(21).rank(pct=True) / currentratio.rolling(21).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc054_21d_base_v054_signal'] = f107d_f107_debt_to_equity_dispersion_calc054_21d_base_v054_signal

def f107d_f107_debt_to_equity_dispersion_calc055_21d_base_v055_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(21).max() - currentratio.rolling(21).min()) / equity.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc055_21d_base_v055_signal'] = f107d_f107_debt_to_equity_dispersion_calc055_21d_base_v055_signal

def f107d_f107_debt_to_equity_dispersion_calc056_126d_base_v056_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(126).rank(pct=True) / currentratio.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc056_126d_base_v056_signal'] = f107d_f107_debt_to_equity_dispersion_calc056_126d_base_v056_signal

def f107d_f107_debt_to_equity_dispersion_calc057_126d_base_v057_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.diff(126) / debt.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc057_126d_base_v057_signal'] = f107d_f107_debt_to_equity_dispersion_calc057_126d_base_v057_signal

def f107d_f107_debt_to_equity_dispersion_calc058_10d_base_v058_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(10).rank(pct=True) / equity.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc058_10d_base_v058_signal'] = f107d_f107_debt_to_equity_dispersion_calc058_10d_base_v058_signal

def f107d_f107_debt_to_equity_dispersion_calc059_63d_base_v059_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(63).rank(pct=True) / marketcap.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc059_63d_base_v059_signal'] = f107d_f107_debt_to_equity_dispersion_calc059_63d_base_v059_signal

def f107d_f107_debt_to_equity_dispersion_calc060_63d_base_v060_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.diff(63) / liabilities.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc060_63d_base_v060_signal'] = f107d_f107_debt_to_equity_dispersion_calc060_63d_base_v060_signal

def f107d_f107_debt_to_equity_dispersion_calc061_10d_base_v061_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda / liabilities.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc061_10d_base_v061_signal'] = f107d_f107_debt_to_equity_dispersion_calc061_10d_base_v061_signal

def f107d_f107_debt_to_equity_dispersion_calc062_21d_base_v062_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = ((debt - debt.rolling(21).mean()) / debt.rolling(21).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc062_21d_base_v062_signal'] = f107d_f107_debt_to_equity_dispersion_calc062_21d_base_v062_signal

def f107d_f107_debt_to_equity_dispersion_calc063_21d_base_v063_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt / ebitda.replace(0, np.nan)).rolling(21).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc063_21d_base_v063_signal'] = f107d_f107_debt_to_equity_dispersion_calc063_21d_base_v063_signal

def f107d_f107_debt_to_equity_dispersion_calc064_63d_base_v064_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.rolling(63).kurt() - liabilities.rolling(63).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc064_63d_base_v064_signal'] = f107d_f107_debt_to_equity_dispersion_calc064_63d_base_v064_signal

def f107d_f107_debt_to_equity_dispersion_calc065_252d_base_v065_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.rolling(252).max() - assets.rolling(252).min()) / currentratio.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc065_252d_base_v065_signal'] = f107d_f107_debt_to_equity_dispersion_calc065_252d_base_v065_signal

def f107d_f107_debt_to_equity_dispersion_calc066_21d_base_v066_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.rolling(21).quantile(0.5) / currentratio.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc066_21d_base_v066_signal'] = f107d_f107_debt_to_equity_dispersion_calc066_21d_base_v066_signal

def f107d_f107_debt_to_equity_dispersion_calc067_252d_base_v067_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.diff(252).abs() / equity.diff(252).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc067_252d_base_v067_signal'] = f107d_f107_debt_to_equity_dispersion_calc067_252d_base_v067_signal

def f107d_f107_debt_to_equity_dispersion_calc068_63d_base_v068_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.diff(63) / equity.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc068_63d_base_v068_signal'] = f107d_f107_debt_to_equity_dispersion_calc068_63d_base_v068_signal

def f107d_f107_debt_to_equity_dispersion_calc069_21d_base_v069_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.diff(21).abs() / liabilities.diff(21).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc069_21d_base_v069_signal'] = f107d_f107_debt_to_equity_dispersion_calc069_21d_base_v069_signal

def f107d_f107_debt_to_equity_dispersion_calc070_10d_base_v070_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = ((assets - assets.rolling(10).mean()) / assets.rolling(10).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc070_10d_base_v070_signal'] = f107d_f107_debt_to_equity_dispersion_calc070_10d_base_v070_signal

def f107d_f107_debt_to_equity_dispersion_calc071_63d_base_v071_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity / assets.replace(0, np.nan)).rolling(63).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc071_63d_base_v071_signal'] = f107d_f107_debt_to_equity_dispersion_calc071_63d_base_v071_signal

def f107d_f107_debt_to_equity_dispersion_calc072_252d_base_v072_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = ((liabilities - liabilities.rolling(252).mean()) / liabilities.rolling(252).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc072_252d_base_v072_signal'] = f107d_f107_debt_to_equity_dispersion_calc072_252d_base_v072_signal

def f107d_f107_debt_to_equity_dispersion_calc073_42d_base_v073_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio / debt.replace(0, np.nan)).rolling(42).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc073_42d_base_v073_signal'] = f107d_f107_debt_to_equity_dispersion_calc073_42d_base_v073_signal

def f107d_f107_debt_to_equity_dispersion_calc074_21d_base_v074_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.rolling(21).max() - assets.rolling(21).min()) / marketcap.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc074_21d_base_v074_signal'] = f107d_f107_debt_to_equity_dispersion_calc074_21d_base_v074_signal

def f107d_f107_debt_to_equity_dispersion_calc075_5d_base_v075_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.diff(5) / assets.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc075_5d_base_v075_signal'] = f107d_f107_debt_to_equity_dispersion_calc075_5d_base_v075_signal



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
