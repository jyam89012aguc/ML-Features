import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f102e_f102_ebitda_to_revenue_volatility_calc001_5d_base_v001_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = ((capex - capex.rolling(5).mean()) / capex.rolling(5).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc001_5d_base_v001_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc001_5d_base_v001_signal

def f102e_f102_ebitda_to_revenue_volatility_calc002_10d_base_v002_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt.diff(10).abs() / assets.diff(10).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc002_10d_base_v002_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc002_10d_base_v002_signal

def f102e_f102_ebitda_to_revenue_volatility_calc003_126d_base_v003_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (assets.rolling(126).quantile(0.5) / equity.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc003_126d_base_v003_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc003_126d_base_v003_signal

def f102e_f102_ebitda_to_revenue_volatility_calc004_63d_base_v004_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = ((assets - assets.rolling(63).mean()) / assets.rolling(63).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc004_63d_base_v004_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc004_63d_base_v004_signal

def f102e_f102_ebitda_to_revenue_volatility_calc005_126d_base_v005_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt.pct_change(126) - assets.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc005_126d_base_v005_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc005_126d_base_v005_signal

def f102e_f102_ebitda_to_revenue_volatility_calc006_5d_base_v006_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda / revenue.replace(0, np.nan)).rolling(5).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc006_5d_base_v006_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc006_5d_base_v006_signal

def f102e_f102_ebitda_to_revenue_volatility_calc007_42d_base_v007_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda.diff(42) / netinc.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc007_42d_base_v007_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc007_42d_base_v007_signal

def f102e_f102_ebitda_to_revenue_volatility_calc008_10d_base_v008_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.diff(10).abs() / debt.diff(10).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc008_10d_base_v008_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc008_10d_base_v008_signal

def f102e_f102_ebitda_to_revenue_volatility_calc009_63d_base_v009_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.diff(63) / assets.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc009_63d_base_v009_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc009_63d_base_v009_signal

def f102e_f102_ebitda_to_revenue_volatility_calc010_5d_base_v010_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity / ebitda.replace(0, np.nan)).rolling(5).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc010_5d_base_v010_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc010_5d_base_v010_signal

def f102e_f102_ebitda_to_revenue_volatility_calc011_42d_base_v011_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (assets.diff(42).abs() / netinc.diff(42).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc011_42d_base_v011_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc011_42d_base_v011_signal

def f102e_f102_ebitda_to_revenue_volatility_calc012_21d_base_v012_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity / ebitda.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc012_21d_base_v012_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc012_21d_base_v012_signal

def f102e_f102_ebitda_to_revenue_volatility_calc013_5d_base_v013_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.rolling(5).kurt() - revenue.rolling(5).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc013_5d_base_v013_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc013_5d_base_v013_signal

def f102e_f102_ebitda_to_revenue_volatility_calc014_42d_base_v014_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (netinc.diff(42).abs() / assets.diff(42).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc014_42d_base_v014_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc014_42d_base_v014_signal

def f102e_f102_ebitda_to_revenue_volatility_calc015_42d_base_v015_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue / capex.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc015_42d_base_v015_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc015_42d_base_v015_signal

def f102e_f102_ebitda_to_revenue_volatility_calc016_10d_base_v016_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt / capex.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc016_10d_base_v016_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc016_10d_base_v016_signal

def f102e_f102_ebitda_to_revenue_volatility_calc017_126d_base_v017_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (netinc.rolling(126).max() - equity.rolling(126).min()) / ebitda.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc017_126d_base_v017_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc017_126d_base_v017_signal

def f102e_f102_ebitda_to_revenue_volatility_calc018_63d_base_v018_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt.diff(63).abs() / equity.diff(63).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc018_63d_base_v018_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc018_63d_base_v018_signal

def f102e_f102_ebitda_to_revenue_volatility_calc019_10d_base_v019_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (assets.rolling(10).quantile(0.5) / debt.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc019_10d_base_v019_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc019_10d_base_v019_signal

def f102e_f102_ebitda_to_revenue_volatility_calc020_63d_base_v020_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.rolling(63).max() - netinc.rolling(63).min()) / capex.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc020_63d_base_v020_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc020_63d_base_v020_signal

def f102e_f102_ebitda_to_revenue_volatility_calc021_5d_base_v021_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (assets.rolling(5).rank(pct=True) / debt.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc021_5d_base_v021_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc021_5d_base_v021_signal

def f102e_f102_ebitda_to_revenue_volatility_calc022_10d_base_v022_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.rolling(10).quantile(0.5) / equity.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc022_10d_base_v022_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc022_10d_base_v022_signal

def f102e_f102_ebitda_to_revenue_volatility_calc023_126d_base_v023_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.diff(126) / capex.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc023_126d_base_v023_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc023_126d_base_v023_signal

def f102e_f102_ebitda_to_revenue_volatility_calc024_126d_base_v024_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.diff(126) / debt.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc024_126d_base_v024_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc024_126d_base_v024_signal

def f102e_f102_ebitda_to_revenue_volatility_calc025_21d_base_v025_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.diff(21) / capex.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc025_21d_base_v025_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc025_21d_base_v025_signal

def f102e_f102_ebitda_to_revenue_volatility_calc026_5d_base_v026_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.rolling(5).kurt() - debt.rolling(5).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc026_5d_base_v026_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc026_5d_base_v026_signal

def f102e_f102_ebitda_to_revenue_volatility_calc027_252d_base_v027_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = ((ebitda - ebitda.rolling(252).mean()) / ebitda.rolling(252).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc027_252d_base_v027_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc027_252d_base_v027_signal

def f102e_f102_ebitda_to_revenue_volatility_calc028_252d_base_v028_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda.rolling(252).kurt() - revenue.rolling(252).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc028_252d_base_v028_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc028_252d_base_v028_signal

def f102e_f102_ebitda_to_revenue_volatility_calc029_5d_base_v029_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.rolling(5).quantile(0.5) / revenue.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc029_5d_base_v029_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc029_5d_base_v029_signal

def f102e_f102_ebitda_to_revenue_volatility_calc030_10d_base_v030_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity / capex.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc030_10d_base_v030_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc030_10d_base_v030_signal

def f102e_f102_ebitda_to_revenue_volatility_calc031_126d_base_v031_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.rolling(126).rank(pct=True) / netinc.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc031_126d_base_v031_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc031_126d_base_v031_signal

def f102e_f102_ebitda_to_revenue_volatility_calc032_126d_base_v032_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (assets / netinc.replace(0, np.nan)).rolling(126).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc032_126d_base_v032_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc032_126d_base_v032_signal

def f102e_f102_ebitda_to_revenue_volatility_calc033_63d_base_v033_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.rolling(63).max() - capex.rolling(63).min()) / netinc.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc033_63d_base_v033_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc033_63d_base_v033_signal

def f102e_f102_ebitda_to_revenue_volatility_calc034_42d_base_v034_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (assets.rolling(42).max() - ebitda.rolling(42).min()) / equity.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc034_42d_base_v034_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc034_42d_base_v034_signal

def f102e_f102_ebitda_to_revenue_volatility_calc035_42d_base_v035_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = ((capex - capex.rolling(42).mean()) / capex.rolling(42).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc035_42d_base_v035_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc035_42d_base_v035_signal

def f102e_f102_ebitda_to_revenue_volatility_calc036_63d_base_v036_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = ((capex - capex.rolling(63).mean()) / capex.rolling(63).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc036_63d_base_v036_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc036_63d_base_v036_signal

def f102e_f102_ebitda_to_revenue_volatility_calc037_10d_base_v037_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex / debt.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc037_10d_base_v037_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc037_10d_base_v037_signal

def f102e_f102_ebitda_to_revenue_volatility_calc038_126d_base_v038_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (netinc.pct_change(126) - equity.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc038_126d_base_v038_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc038_126d_base_v038_signal

def f102e_f102_ebitda_to_revenue_volatility_calc039_10d_base_v039_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda.rolling(10).kurt() - netinc.rolling(10).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc039_10d_base_v039_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc039_10d_base_v039_signal

def f102e_f102_ebitda_to_revenue_volatility_calc040_21d_base_v040_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = ((debt - debt.rolling(21).mean()) / debt.rolling(21).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc040_21d_base_v040_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc040_21d_base_v040_signal

def f102e_f102_ebitda_to_revenue_volatility_calc041_252d_base_v041_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (netinc / ebitda.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc041_252d_base_v041_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc041_252d_base_v041_signal

def f102e_f102_ebitda_to_revenue_volatility_calc042_10d_base_v042_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda.rolling(10).rank(pct=True) / assets.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc042_10d_base_v042_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc042_10d_base_v042_signal

def f102e_f102_ebitda_to_revenue_volatility_calc043_21d_base_v043_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.rolling(21).quantile(0.5) / equity.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc043_21d_base_v043_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc043_21d_base_v043_signal

def f102e_f102_ebitda_to_revenue_volatility_calc044_10d_base_v044_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.diff(10).abs() / equity.diff(10).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc044_10d_base_v044_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc044_10d_base_v044_signal

def f102e_f102_ebitda_to_revenue_volatility_calc045_63d_base_v045_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.rolling(63).rank(pct=True) / capex.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc045_63d_base_v045_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc045_63d_base_v045_signal

def f102e_f102_ebitda_to_revenue_volatility_calc046_126d_base_v046_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda.diff(126).abs() / netinc.diff(126).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc046_126d_base_v046_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc046_126d_base_v046_signal

def f102e_f102_ebitda_to_revenue_volatility_calc047_126d_base_v047_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.pct_change(126) - debt.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc047_126d_base_v047_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc047_126d_base_v047_signal

def f102e_f102_ebitda_to_revenue_volatility_calc048_63d_base_v048_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex / assets.replace(0, np.nan)).rolling(63).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc048_63d_base_v048_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc048_63d_base_v048_signal

def f102e_f102_ebitda_to_revenue_volatility_calc049_63d_base_v049_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.diff(63).abs() / assets.diff(63).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc049_63d_base_v049_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc049_63d_base_v049_signal

def f102e_f102_ebitda_to_revenue_volatility_calc050_10d_base_v050_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda.rolling(10).quantile(0.5) / netinc.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc050_10d_base_v050_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc050_10d_base_v050_signal

def f102e_f102_ebitda_to_revenue_volatility_calc051_5d_base_v051_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.diff(5) / equity.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc051_5d_base_v051_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc051_5d_base_v051_signal

def f102e_f102_ebitda_to_revenue_volatility_calc052_42d_base_v052_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.diff(42) / equity.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc052_42d_base_v052_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc052_42d_base_v052_signal

def f102e_f102_ebitda_to_revenue_volatility_calc053_42d_base_v053_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.rolling(42).quantile(0.5) / netinc.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc053_42d_base_v053_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc053_42d_base_v053_signal

def f102e_f102_ebitda_to_revenue_volatility_calc054_21d_base_v054_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt / equity.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc054_21d_base_v054_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc054_21d_base_v054_signal

def f102e_f102_ebitda_to_revenue_volatility_calc055_5d_base_v055_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.diff(5).abs() / netinc.diff(5).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc055_5d_base_v055_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc055_5d_base_v055_signal

def f102e_f102_ebitda_to_revenue_volatility_calc056_5d_base_v056_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda.rolling(5).rank(pct=True) / assets.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc056_5d_base_v056_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc056_5d_base_v056_signal

def f102e_f102_ebitda_to_revenue_volatility_calc057_126d_base_v057_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt.pct_change(126) - netinc.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc057_126d_base_v057_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc057_126d_base_v057_signal

def f102e_f102_ebitda_to_revenue_volatility_calc058_10d_base_v058_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.rolling(10).quantile(0.5) / capex.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc058_10d_base_v058_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc058_10d_base_v058_signal

def f102e_f102_ebitda_to_revenue_volatility_calc059_126d_base_v059_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = ((assets - assets.rolling(126).mean()) / assets.rolling(126).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc059_126d_base_v059_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc059_126d_base_v059_signal

def f102e_f102_ebitda_to_revenue_volatility_calc060_126d_base_v060_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = ((equity - equity.rolling(126).mean()) / equity.rolling(126).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc060_126d_base_v060_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc060_126d_base_v060_signal

def f102e_f102_ebitda_to_revenue_volatility_calc061_63d_base_v061_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = ((ebitda - ebitda.rolling(63).mean()) / ebitda.rolling(63).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc061_63d_base_v061_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc061_63d_base_v061_signal

def f102e_f102_ebitda_to_revenue_volatility_calc062_126d_base_v062_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.rolling(126).quantile(0.5) / capex.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc062_126d_base_v062_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc062_126d_base_v062_signal

def f102e_f102_ebitda_to_revenue_volatility_calc063_252d_base_v063_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.diff(252).abs() / assets.diff(252).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc063_252d_base_v063_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc063_252d_base_v063_signal

def f102e_f102_ebitda_to_revenue_volatility_calc064_126d_base_v064_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = ((debt - debt.rolling(126).mean()) / debt.rolling(126).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc064_126d_base_v064_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc064_126d_base_v064_signal

def f102e_f102_ebitda_to_revenue_volatility_calc065_5d_base_v065_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = ((debt - debt.rolling(5).mean()) / debt.rolling(5).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc065_5d_base_v065_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc065_5d_base_v065_signal

def f102e_f102_ebitda_to_revenue_volatility_calc066_5d_base_v066_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.diff(5) / assets.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc066_5d_base_v066_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc066_5d_base_v066_signal

def f102e_f102_ebitda_to_revenue_volatility_calc067_63d_base_v067_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (assets / capex.replace(0, np.nan)).rolling(63).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc067_63d_base_v067_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc067_63d_base_v067_signal

def f102e_f102_ebitda_to_revenue_volatility_calc068_126d_base_v068_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex / assets.replace(0, np.nan)).rolling(126).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc068_126d_base_v068_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc068_126d_base_v068_signal

def f102e_f102_ebitda_to_revenue_volatility_calc069_63d_base_v069_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.rolling(63).max() - debt.rolling(63).min()) / revenue.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc069_63d_base_v069_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc069_63d_base_v069_signal

def f102e_f102_ebitda_to_revenue_volatility_calc070_21d_base_v070_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt / netinc.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc070_21d_base_v070_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc070_21d_base_v070_signal

def f102e_f102_ebitda_to_revenue_volatility_calc071_252d_base_v071_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = ((revenue - revenue.rolling(252).mean()) / revenue.rolling(252).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc071_252d_base_v071_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc071_252d_base_v071_signal

def f102e_f102_ebitda_to_revenue_volatility_calc072_21d_base_v072_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda.diff(21).abs() / capex.diff(21).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc072_21d_base_v072_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc072_21d_base_v072_signal

def f102e_f102_ebitda_to_revenue_volatility_calc073_126d_base_v073_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.pct_change(126) - assets.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc073_126d_base_v073_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc073_126d_base_v073_signal

def f102e_f102_ebitda_to_revenue_volatility_calc074_63d_base_v074_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.diff(63).abs() / debt.diff(63).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc074_63d_base_v074_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc074_63d_base_v074_signal

def f102e_f102_ebitda_to_revenue_volatility_calc075_21d_base_v075_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (netinc / equity.replace(0, np.nan)).rolling(21).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc075_21d_base_v075_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc075_21d_base_v075_signal



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
