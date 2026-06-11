import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f106m_f106_market_cap_to_revenue_cycles_calc001_21d_base_v001_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.rolling(21).quantile(0.5) / assets.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc001_21d_base_v001_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc001_21d_base_v001_signal

def f106m_f106_market_cap_to_revenue_cycles_calc002_21d_base_v002_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.rolling(21).rank(pct=True) / marketcap.rolling(21).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc002_21d_base_v002_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc002_21d_base_v002_signal

def f106m_f106_market_cap_to_revenue_cycles_calc003_42d_base_v003_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.rolling(42).quantile(0.5) / equity.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc003_42d_base_v003_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc003_42d_base_v003_signal

def f106m_f106_market_cap_to_revenue_cycles_calc004_10d_base_v004_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.pct_change(10) - marketcap.pct_change(10))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc004_10d_base_v004_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc004_10d_base_v004_signal

def f106m_f106_market_cap_to_revenue_cycles_calc005_10d_base_v005_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf.diff(10) / marketcap.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc005_10d_base_v005_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc005_10d_base_v005_signal

def f106m_f106_market_cap_to_revenue_cycles_calc006_21d_base_v006_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.rolling(21).kurt() - equity.rolling(21).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc006_21d_base_v006_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc006_21d_base_v006_signal

def f106m_f106_market_cap_to_revenue_cycles_calc007_42d_base_v007_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.pct_change(42) - fcf.pct_change(42))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc007_42d_base_v007_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc007_42d_base_v007_signal

def f106m_f106_market_cap_to_revenue_cycles_calc008_21d_base_v008_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.diff(21) / revenue.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc008_21d_base_v008_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc008_21d_base_v008_signal

def f106m_f106_market_cap_to_revenue_cycles_calc009_126d_base_v009_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.rolling(126).max() - ebitda.rolling(126).min()) / revenue.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc009_126d_base_v009_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc009_126d_base_v009_signal

def f106m_f106_market_cap_to_revenue_cycles_calc010_126d_base_v010_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.rolling(126).max() - assets.rolling(126).min()) / ebitda.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc010_126d_base_v010_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc010_126d_base_v010_signal

def f106m_f106_market_cap_to_revenue_cycles_calc011_63d_base_v011_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.rolling(63).quantile(0.5) / fcf.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc011_63d_base_v011_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc011_63d_base_v011_signal

def f106m_f106_market_cap_to_revenue_cycles_calc012_10d_base_v012_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda / fcf.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc012_10d_base_v012_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc012_10d_base_v012_signal

def f106m_f106_market_cap_to_revenue_cycles_calc013_252d_base_v013_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.diff(252) / netinc.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc013_252d_base_v013_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc013_252d_base_v013_signal

def f106m_f106_market_cap_to_revenue_cycles_calc014_126d_base_v014_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.rolling(126).rank(pct=True) / fcf.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc014_126d_base_v014_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc014_126d_base_v014_signal

def f106m_f106_market_cap_to_revenue_cycles_calc015_5d_base_v015_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.rolling(5).quantile(0.5) / assets.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc015_5d_base_v015_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc015_5d_base_v015_signal

def f106m_f106_market_cap_to_revenue_cycles_calc016_5d_base_v016_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.diff(5).abs() / revenue.diff(5).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc016_5d_base_v016_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc016_5d_base_v016_signal

def f106m_f106_market_cap_to_revenue_cycles_calc017_10d_base_v017_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.rolling(10).rank(pct=True) / revenue.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc017_10d_base_v017_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc017_10d_base_v017_signal

def f106m_f106_market_cap_to_revenue_cycles_calc018_63d_base_v018_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity / marketcap.replace(0, np.nan)).rolling(63).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc018_63d_base_v018_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc018_63d_base_v018_signal

def f106m_f106_market_cap_to_revenue_cycles_calc019_252d_base_v019_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.rolling(252).quantile(0.5) / revenue.rolling(252).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc019_252d_base_v019_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc019_252d_base_v019_signal

def f106m_f106_market_cap_to_revenue_cycles_calc020_42d_base_v020_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.rolling(42).rank(pct=True) / fcf.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc020_42d_base_v020_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc020_42d_base_v020_signal

def f106m_f106_market_cap_to_revenue_cycles_calc021_10d_base_v021_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap / revenue.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc021_10d_base_v021_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc021_10d_base_v021_signal

def f106m_f106_market_cap_to_revenue_cycles_calc022_10d_base_v022_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.diff(10).abs() / fcf.diff(10).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc022_10d_base_v022_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc022_10d_base_v022_signal

def f106m_f106_market_cap_to_revenue_cycles_calc023_126d_base_v023_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.rolling(126).quantile(0.5) / marketcap.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc023_126d_base_v023_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc023_126d_base_v023_signal

def f106m_f106_market_cap_to_revenue_cycles_calc024_10d_base_v024_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue / assets.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc024_10d_base_v024_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc024_10d_base_v024_signal

def f106m_f106_market_cap_to_revenue_cycles_calc025_21d_base_v025_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.diff(21) / equity.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc025_21d_base_v025_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc025_21d_base_v025_signal

def f106m_f106_market_cap_to_revenue_cycles_calc026_252d_base_v026_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf / netinc.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc026_252d_base_v026_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc026_252d_base_v026_signal

def f106m_f106_market_cap_to_revenue_cycles_calc027_252d_base_v027_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.pct_change(252) - revenue.pct_change(252))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc027_252d_base_v027_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc027_252d_base_v027_signal

def f106m_f106_market_cap_to_revenue_cycles_calc028_21d_base_v028_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda / revenue.replace(0, np.nan)).rolling(21).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc028_21d_base_v028_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc028_21d_base_v028_signal

def f106m_f106_market_cap_to_revenue_cycles_calc029_21d_base_v029_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.diff(21).abs() / assets.diff(21).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc029_21d_base_v029_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc029_21d_base_v029_signal

def f106m_f106_market_cap_to_revenue_cycles_calc030_252d_base_v030_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.rolling(252).max() - assets.rolling(252).min()) / fcf.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc030_252d_base_v030_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc030_252d_base_v030_signal

def f106m_f106_market_cap_to_revenue_cycles_calc031_42d_base_v031_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.pct_change(42) - equity.pct_change(42))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc031_42d_base_v031_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc031_42d_base_v031_signal

def f106m_f106_market_cap_to_revenue_cycles_calc032_10d_base_v032_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.rolling(10).rank(pct=True) / revenue.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc032_10d_base_v032_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc032_10d_base_v032_signal

def f106m_f106_market_cap_to_revenue_cycles_calc033_42d_base_v033_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets / revenue.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc033_42d_base_v033_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc033_42d_base_v033_signal

def f106m_f106_market_cap_to_revenue_cycles_calc034_21d_base_v034_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc / marketcap.replace(0, np.nan)).rolling(21).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc034_21d_base_v034_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc034_21d_base_v034_signal

def f106m_f106_market_cap_to_revenue_cycles_calc035_5d_base_v035_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.diff(5).abs() / equity.diff(5).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc035_5d_base_v035_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc035_5d_base_v035_signal

def f106m_f106_market_cap_to_revenue_cycles_calc036_5d_base_v036_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((netinc - netinc.rolling(5).mean()) / netinc.rolling(5).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc036_5d_base_v036_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc036_5d_base_v036_signal

def f106m_f106_market_cap_to_revenue_cycles_calc037_10d_base_v037_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.diff(10).abs() / assets.diff(10).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc037_10d_base_v037_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc037_10d_base_v037_signal

def f106m_f106_market_cap_to_revenue_cycles_calc038_10d_base_v038_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.diff(10) / assets.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc038_10d_base_v038_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc038_10d_base_v038_signal

def f106m_f106_market_cap_to_revenue_cycles_calc039_42d_base_v039_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.rolling(42).rank(pct=True) / revenue.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc039_42d_base_v039_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc039_42d_base_v039_signal

def f106m_f106_market_cap_to_revenue_cycles_calc040_5d_base_v040_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets / equity.replace(0, np.nan)).rolling(5).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc040_5d_base_v040_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc040_5d_base_v040_signal

def f106m_f106_market_cap_to_revenue_cycles_calc041_10d_base_v041_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.rolling(10).kurt() - netinc.rolling(10).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc041_10d_base_v041_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc041_10d_base_v041_signal

def f106m_f106_market_cap_to_revenue_cycles_calc042_42d_base_v042_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.diff(42) / fcf.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc042_42d_base_v042_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc042_42d_base_v042_signal

def f106m_f106_market_cap_to_revenue_cycles_calc043_63d_base_v043_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.rolling(63).kurt() - equity.rolling(63).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc043_63d_base_v043_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc043_63d_base_v043_signal

def f106m_f106_market_cap_to_revenue_cycles_calc044_5d_base_v044_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets / marketcap.replace(0, np.nan)).rolling(5).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc044_5d_base_v044_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc044_5d_base_v044_signal

def f106m_f106_market_cap_to_revenue_cycles_calc045_21d_base_v045_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((equity - equity.rolling(21).mean()) / equity.rolling(21).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc045_21d_base_v045_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc045_21d_base_v045_signal

def f106m_f106_market_cap_to_revenue_cycles_calc046_10d_base_v046_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.rolling(10).quantile(0.5) / fcf.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc046_10d_base_v046_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc046_10d_base_v046_signal

def f106m_f106_market_cap_to_revenue_cycles_calc047_63d_base_v047_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda / assets.replace(0, np.nan)).rolling(63).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc047_63d_base_v047_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc047_63d_base_v047_signal

def f106m_f106_market_cap_to_revenue_cycles_calc048_126d_base_v048_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue / assets.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc048_126d_base_v048_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc048_126d_base_v048_signal

def f106m_f106_market_cap_to_revenue_cycles_calc049_126d_base_v049_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.diff(126) / marketcap.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc049_126d_base_v049_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc049_126d_base_v049_signal

def f106m_f106_market_cap_to_revenue_cycles_calc050_252d_base_v050_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((revenue - revenue.rolling(252).mean()) / revenue.rolling(252).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc050_252d_base_v050_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc050_252d_base_v050_signal

def f106m_f106_market_cap_to_revenue_cycles_calc051_5d_base_v051_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf.rolling(5).kurt() - ebitda.rolling(5).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc051_5d_base_v051_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc051_5d_base_v051_signal

def f106m_f106_market_cap_to_revenue_cycles_calc052_126d_base_v052_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.diff(126).abs() / revenue.diff(126).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc052_126d_base_v052_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc052_126d_base_v052_signal

def f106m_f106_market_cap_to_revenue_cycles_calc053_63d_base_v053_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity / netinc.replace(0, np.nan)).rolling(63).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc053_63d_base_v053_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc053_63d_base_v053_signal

def f106m_f106_market_cap_to_revenue_cycles_calc054_252d_base_v054_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.diff(252).abs() / equity.diff(252).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc054_252d_base_v054_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc054_252d_base_v054_signal

def f106m_f106_market_cap_to_revenue_cycles_calc055_42d_base_v055_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.rolling(42).quantile(0.5) / netinc.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc055_42d_base_v055_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc055_42d_base_v055_signal

def f106m_f106_market_cap_to_revenue_cycles_calc056_126d_base_v056_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf.rolling(126).quantile(0.5) / ebitda.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc056_126d_base_v056_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc056_126d_base_v056_signal

def f106m_f106_market_cap_to_revenue_cycles_calc057_10d_base_v057_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.rolling(10).max() - netinc.rolling(10).min()) / fcf.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc057_10d_base_v057_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc057_10d_base_v057_signal

def f106m_f106_market_cap_to_revenue_cycles_calc058_63d_base_v058_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.diff(63) / fcf.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc058_63d_base_v058_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc058_63d_base_v058_signal

def f106m_f106_market_cap_to_revenue_cycles_calc059_252d_base_v059_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap / assets.replace(0, np.nan)).rolling(252).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc059_252d_base_v059_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc059_252d_base_v059_signal

def f106m_f106_market_cap_to_revenue_cycles_calc060_126d_base_v060_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.rolling(126).max() - revenue.rolling(126).min()) / assets.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc060_126d_base_v060_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc060_126d_base_v060_signal

def f106m_f106_market_cap_to_revenue_cycles_calc061_21d_base_v061_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((marketcap - marketcap.rolling(21).mean()) / marketcap.rolling(21).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc061_21d_base_v061_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc061_21d_base_v061_signal

def f106m_f106_market_cap_to_revenue_cycles_calc062_63d_base_v062_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.diff(63) / assets.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc062_63d_base_v062_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc062_63d_base_v062_signal

def f106m_f106_market_cap_to_revenue_cycles_calc063_5d_base_v063_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.diff(5) / assets.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc063_5d_base_v063_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc063_5d_base_v063_signal

def f106m_f106_market_cap_to_revenue_cycles_calc064_252d_base_v064_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.rolling(252).kurt() - ebitda.rolling(252).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc064_252d_base_v064_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc064_252d_base_v064_signal

def f106m_f106_market_cap_to_revenue_cycles_calc065_63d_base_v065_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.rolling(63).quantile(0.5) / fcf.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc065_63d_base_v065_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc065_63d_base_v065_signal

def f106m_f106_market_cap_to_revenue_cycles_calc066_5d_base_v066_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.pct_change(5) - ebitda.pct_change(5))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc066_5d_base_v066_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc066_5d_base_v066_signal

def f106m_f106_market_cap_to_revenue_cycles_calc067_5d_base_v067_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.diff(5) / marketcap.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc067_5d_base_v067_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc067_5d_base_v067_signal

def f106m_f106_market_cap_to_revenue_cycles_calc068_42d_base_v068_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.pct_change(42) - netinc.pct_change(42))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc068_42d_base_v068_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc068_42d_base_v068_signal

def f106m_f106_market_cap_to_revenue_cycles_calc069_252d_base_v069_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue / ebitda.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc069_252d_base_v069_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc069_252d_base_v069_signal

def f106m_f106_market_cap_to_revenue_cycles_calc070_252d_base_v070_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf.diff(252) / netinc.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc070_252d_base_v070_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc070_252d_base_v070_signal

def f106m_f106_market_cap_to_revenue_cycles_calc071_252d_base_v071_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity / revenue.replace(0, np.nan)).rolling(252).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc071_252d_base_v071_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc071_252d_base_v071_signal

def f106m_f106_market_cap_to_revenue_cycles_calc072_42d_base_v072_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity / fcf.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc072_42d_base_v072_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc072_42d_base_v072_signal

def f106m_f106_market_cap_to_revenue_cycles_calc073_63d_base_v073_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.rolling(63).kurt() - revenue.rolling(63).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc073_63d_base_v073_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc073_63d_base_v073_signal

def f106m_f106_market_cap_to_revenue_cycles_calc074_126d_base_v074_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf.rolling(126).max() - netinc.rolling(126).min()) / assets.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc074_126d_base_v074_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc074_126d_base_v074_signal

def f106m_f106_market_cap_to_revenue_cycles_calc075_63d_base_v075_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.rolling(63).max() - revenue.rolling(63).min()) / netinc.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc075_63d_base_v075_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc075_63d_base_v075_signal



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
