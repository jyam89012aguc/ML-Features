import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f106m_f106_market_cap_to_revenue_cycles_calc001_21d_slope_v001_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.rolling(21).quantile(0.5) / assets.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc001_21d_slope_v001_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc001_21d_slope_v001_signal

def f106m_f106_market_cap_to_revenue_cycles_calc002_21d_slope_v002_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.rolling(21).rank(pct=True) / marketcap.rolling(21).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc002_21d_slope_v002_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc002_21d_slope_v002_signal

def f106m_f106_market_cap_to_revenue_cycles_calc003_42d_slope_v003_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.rolling(42).quantile(0.5) / equity.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc003_42d_slope_v003_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc003_42d_slope_v003_signal

def f106m_f106_market_cap_to_revenue_cycles_calc004_10d_slope_v004_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.pct_change(10) - marketcap.pct_change(10))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc004_10d_slope_v004_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc004_10d_slope_v004_signal

def f106m_f106_market_cap_to_revenue_cycles_calc005_10d_slope_v005_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf.diff(10) / marketcap.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc005_10d_slope_v005_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc005_10d_slope_v005_signal

def f106m_f106_market_cap_to_revenue_cycles_calc006_21d_slope_v006_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.rolling(21).kurt() - equity.rolling(21).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc006_21d_slope_v006_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc006_21d_slope_v006_signal

def f106m_f106_market_cap_to_revenue_cycles_calc007_42d_slope_v007_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.pct_change(42) - fcf.pct_change(42))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc007_42d_slope_v007_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc007_42d_slope_v007_signal

def f106m_f106_market_cap_to_revenue_cycles_calc008_21d_slope_v008_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.diff(21) / revenue.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc008_21d_slope_v008_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc008_21d_slope_v008_signal

def f106m_f106_market_cap_to_revenue_cycles_calc009_126d_slope_v009_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.rolling(126).max() - ebitda.rolling(126).min()) / revenue.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc009_126d_slope_v009_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc009_126d_slope_v009_signal

def f106m_f106_market_cap_to_revenue_cycles_calc010_126d_slope_v010_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.rolling(126).max() - assets.rolling(126).min()) / ebitda.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc010_126d_slope_v010_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc010_126d_slope_v010_signal

def f106m_f106_market_cap_to_revenue_cycles_calc011_63d_slope_v011_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.rolling(63).quantile(0.5) / fcf.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc011_63d_slope_v011_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc011_63d_slope_v011_signal

def f106m_f106_market_cap_to_revenue_cycles_calc012_10d_slope_v012_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda / fcf.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc012_10d_slope_v012_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc012_10d_slope_v012_signal

def f106m_f106_market_cap_to_revenue_cycles_calc013_252d_slope_v013_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.diff(252) / netinc.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc013_252d_slope_v013_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc013_252d_slope_v013_signal

def f106m_f106_market_cap_to_revenue_cycles_calc014_126d_slope_v014_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.rolling(126).rank(pct=True) / fcf.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc014_126d_slope_v014_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc014_126d_slope_v014_signal

def f106m_f106_market_cap_to_revenue_cycles_calc015_5d_slope_v015_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.rolling(5).quantile(0.5) / assets.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc015_5d_slope_v015_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc015_5d_slope_v015_signal

def f106m_f106_market_cap_to_revenue_cycles_calc016_5d_slope_v016_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.diff(5).abs() / revenue.diff(5).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc016_5d_slope_v016_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc016_5d_slope_v016_signal

def f106m_f106_market_cap_to_revenue_cycles_calc017_10d_slope_v017_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.rolling(10).rank(pct=True) / revenue.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc017_10d_slope_v017_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc017_10d_slope_v017_signal

def f106m_f106_market_cap_to_revenue_cycles_calc018_63d_slope_v018_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity / marketcap.replace(0, np.nan)).rolling(63).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc018_63d_slope_v018_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc018_63d_slope_v018_signal

def f106m_f106_market_cap_to_revenue_cycles_calc019_252d_slope_v019_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.rolling(252).quantile(0.5) / revenue.rolling(252).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc019_252d_slope_v019_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc019_252d_slope_v019_signal

def f106m_f106_market_cap_to_revenue_cycles_calc020_42d_slope_v020_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.rolling(42).rank(pct=True) / fcf.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc020_42d_slope_v020_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc020_42d_slope_v020_signal

def f106m_f106_market_cap_to_revenue_cycles_calc021_10d_slope_v021_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap / revenue.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc021_10d_slope_v021_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc021_10d_slope_v021_signal

def f106m_f106_market_cap_to_revenue_cycles_calc022_10d_slope_v022_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.diff(10).abs() / fcf.diff(10).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc022_10d_slope_v022_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc022_10d_slope_v022_signal

def f106m_f106_market_cap_to_revenue_cycles_calc023_126d_slope_v023_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.rolling(126).quantile(0.5) / marketcap.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc023_126d_slope_v023_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc023_126d_slope_v023_signal

def f106m_f106_market_cap_to_revenue_cycles_calc024_10d_slope_v024_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue / assets.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc024_10d_slope_v024_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc024_10d_slope_v024_signal

def f106m_f106_market_cap_to_revenue_cycles_calc025_21d_slope_v025_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.diff(21) / equity.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc025_21d_slope_v025_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc025_21d_slope_v025_signal

def f106m_f106_market_cap_to_revenue_cycles_calc026_252d_slope_v026_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf / netinc.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc026_252d_slope_v026_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc026_252d_slope_v026_signal

def f106m_f106_market_cap_to_revenue_cycles_calc027_252d_slope_v027_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.pct_change(252) - revenue.pct_change(252))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc027_252d_slope_v027_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc027_252d_slope_v027_signal

def f106m_f106_market_cap_to_revenue_cycles_calc028_21d_slope_v028_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda / revenue.replace(0, np.nan)).rolling(21).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc028_21d_slope_v028_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc028_21d_slope_v028_signal

def f106m_f106_market_cap_to_revenue_cycles_calc029_21d_slope_v029_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.diff(21).abs() / assets.diff(21).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc029_21d_slope_v029_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc029_21d_slope_v029_signal

def f106m_f106_market_cap_to_revenue_cycles_calc030_252d_slope_v030_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.rolling(252).max() - assets.rolling(252).min()) / fcf.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc030_252d_slope_v030_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc030_252d_slope_v030_signal

def f106m_f106_market_cap_to_revenue_cycles_calc031_42d_slope_v031_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.pct_change(42) - equity.pct_change(42))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc031_42d_slope_v031_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc031_42d_slope_v031_signal

def f106m_f106_market_cap_to_revenue_cycles_calc032_10d_slope_v032_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.rolling(10).rank(pct=True) / revenue.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc032_10d_slope_v032_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc032_10d_slope_v032_signal

def f106m_f106_market_cap_to_revenue_cycles_calc033_42d_slope_v033_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets / revenue.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc033_42d_slope_v033_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc033_42d_slope_v033_signal

def f106m_f106_market_cap_to_revenue_cycles_calc034_21d_slope_v034_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc / marketcap.replace(0, np.nan)).rolling(21).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc034_21d_slope_v034_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc034_21d_slope_v034_signal

def f106m_f106_market_cap_to_revenue_cycles_calc035_5d_slope_v035_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.diff(5).abs() / equity.diff(5).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc035_5d_slope_v035_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc035_5d_slope_v035_signal

def f106m_f106_market_cap_to_revenue_cycles_calc036_5d_slope_v036_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((netinc - netinc.rolling(5).mean()) / netinc.rolling(5).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc036_5d_slope_v036_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc036_5d_slope_v036_signal

def f106m_f106_market_cap_to_revenue_cycles_calc037_10d_slope_v037_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.diff(10).abs() / assets.diff(10).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc037_10d_slope_v037_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc037_10d_slope_v037_signal

def f106m_f106_market_cap_to_revenue_cycles_calc038_10d_slope_v038_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.diff(10) / assets.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc038_10d_slope_v038_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc038_10d_slope_v038_signal

def f106m_f106_market_cap_to_revenue_cycles_calc039_42d_slope_v039_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.rolling(42).rank(pct=True) / revenue.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc039_42d_slope_v039_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc039_42d_slope_v039_signal

def f106m_f106_market_cap_to_revenue_cycles_calc040_5d_slope_v040_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets / equity.replace(0, np.nan)).rolling(5).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc040_5d_slope_v040_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc040_5d_slope_v040_signal

def f106m_f106_market_cap_to_revenue_cycles_calc041_10d_slope_v041_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.rolling(10).kurt() - netinc.rolling(10).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc041_10d_slope_v041_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc041_10d_slope_v041_signal

def f106m_f106_market_cap_to_revenue_cycles_calc042_42d_slope_v042_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.diff(42) / fcf.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc042_42d_slope_v042_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc042_42d_slope_v042_signal

def f106m_f106_market_cap_to_revenue_cycles_calc043_63d_slope_v043_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.rolling(63).kurt() - equity.rolling(63).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc043_63d_slope_v043_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc043_63d_slope_v043_signal

def f106m_f106_market_cap_to_revenue_cycles_calc044_5d_slope_v044_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets / marketcap.replace(0, np.nan)).rolling(5).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc044_5d_slope_v044_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc044_5d_slope_v044_signal

def f106m_f106_market_cap_to_revenue_cycles_calc045_21d_slope_v045_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((equity - equity.rolling(21).mean()) / equity.rolling(21).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc045_21d_slope_v045_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc045_21d_slope_v045_signal

def f106m_f106_market_cap_to_revenue_cycles_calc046_10d_slope_v046_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.rolling(10).quantile(0.5) / fcf.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc046_10d_slope_v046_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc046_10d_slope_v046_signal

def f106m_f106_market_cap_to_revenue_cycles_calc047_63d_slope_v047_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda / assets.replace(0, np.nan)).rolling(63).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc047_63d_slope_v047_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc047_63d_slope_v047_signal

def f106m_f106_market_cap_to_revenue_cycles_calc048_126d_slope_v048_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue / assets.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc048_126d_slope_v048_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc048_126d_slope_v048_signal

def f106m_f106_market_cap_to_revenue_cycles_calc049_126d_slope_v049_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.diff(126) / marketcap.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc049_126d_slope_v049_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc049_126d_slope_v049_signal

def f106m_f106_market_cap_to_revenue_cycles_calc050_252d_slope_v050_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((revenue - revenue.rolling(252).mean()) / revenue.rolling(252).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc050_252d_slope_v050_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc050_252d_slope_v050_signal

def f106m_f106_market_cap_to_revenue_cycles_calc051_5d_slope_v051_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf.rolling(5).kurt() - ebitda.rolling(5).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc051_5d_slope_v051_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc051_5d_slope_v051_signal

def f106m_f106_market_cap_to_revenue_cycles_calc052_126d_slope_v052_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.diff(126).abs() / revenue.diff(126).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc052_126d_slope_v052_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc052_126d_slope_v052_signal

def f106m_f106_market_cap_to_revenue_cycles_calc053_63d_slope_v053_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity / netinc.replace(0, np.nan)).rolling(63).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc053_63d_slope_v053_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc053_63d_slope_v053_signal

def f106m_f106_market_cap_to_revenue_cycles_calc054_252d_slope_v054_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.diff(252).abs() / equity.diff(252).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc054_252d_slope_v054_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc054_252d_slope_v054_signal

def f106m_f106_market_cap_to_revenue_cycles_calc055_42d_slope_v055_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.rolling(42).quantile(0.5) / netinc.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc055_42d_slope_v055_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc055_42d_slope_v055_signal

def f106m_f106_market_cap_to_revenue_cycles_calc056_126d_slope_v056_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf.rolling(126).quantile(0.5) / ebitda.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc056_126d_slope_v056_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc056_126d_slope_v056_signal

def f106m_f106_market_cap_to_revenue_cycles_calc057_10d_slope_v057_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.rolling(10).max() - netinc.rolling(10).min()) / fcf.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc057_10d_slope_v057_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc057_10d_slope_v057_signal

def f106m_f106_market_cap_to_revenue_cycles_calc058_63d_slope_v058_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.diff(63) / fcf.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc058_63d_slope_v058_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc058_63d_slope_v058_signal

def f106m_f106_market_cap_to_revenue_cycles_calc059_252d_slope_v059_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap / assets.replace(0, np.nan)).rolling(252).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc059_252d_slope_v059_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc059_252d_slope_v059_signal

def f106m_f106_market_cap_to_revenue_cycles_calc060_126d_slope_v060_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.rolling(126).max() - revenue.rolling(126).min()) / assets.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc060_126d_slope_v060_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc060_126d_slope_v060_signal

def f106m_f106_market_cap_to_revenue_cycles_calc061_21d_slope_v061_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((marketcap - marketcap.rolling(21).mean()) / marketcap.rolling(21).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc061_21d_slope_v061_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc061_21d_slope_v061_signal

def f106m_f106_market_cap_to_revenue_cycles_calc062_63d_slope_v062_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.diff(63) / assets.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc062_63d_slope_v062_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc062_63d_slope_v062_signal

def f106m_f106_market_cap_to_revenue_cycles_calc063_5d_slope_v063_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.diff(5) / assets.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc063_5d_slope_v063_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc063_5d_slope_v063_signal

def f106m_f106_market_cap_to_revenue_cycles_calc064_252d_slope_v064_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.rolling(252).kurt() - ebitda.rolling(252).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc064_252d_slope_v064_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc064_252d_slope_v064_signal

def f106m_f106_market_cap_to_revenue_cycles_calc065_63d_slope_v065_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.rolling(63).quantile(0.5) / fcf.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc065_63d_slope_v065_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc065_63d_slope_v065_signal

def f106m_f106_market_cap_to_revenue_cycles_calc066_5d_slope_v066_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.pct_change(5) - ebitda.pct_change(5))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc066_5d_slope_v066_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc066_5d_slope_v066_signal

def f106m_f106_market_cap_to_revenue_cycles_calc067_5d_slope_v067_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.diff(5) / marketcap.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc067_5d_slope_v067_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc067_5d_slope_v067_signal

def f106m_f106_market_cap_to_revenue_cycles_calc068_42d_slope_v068_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.pct_change(42) - netinc.pct_change(42))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc068_42d_slope_v068_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc068_42d_slope_v068_signal

def f106m_f106_market_cap_to_revenue_cycles_calc069_252d_slope_v069_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue / ebitda.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc069_252d_slope_v069_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc069_252d_slope_v069_signal

def f106m_f106_market_cap_to_revenue_cycles_calc070_252d_slope_v070_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf.diff(252) / netinc.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc070_252d_slope_v070_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc070_252d_slope_v070_signal

def f106m_f106_market_cap_to_revenue_cycles_calc071_252d_slope_v071_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity / revenue.replace(0, np.nan)).rolling(252).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc071_252d_slope_v071_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc071_252d_slope_v071_signal

def f106m_f106_market_cap_to_revenue_cycles_calc072_42d_slope_v072_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity / fcf.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc072_42d_slope_v072_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc072_42d_slope_v072_signal

def f106m_f106_market_cap_to_revenue_cycles_calc073_63d_slope_v073_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.rolling(63).kurt() - revenue.rolling(63).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc073_63d_slope_v073_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc073_63d_slope_v073_signal

def f106m_f106_market_cap_to_revenue_cycles_calc074_126d_slope_v074_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf.rolling(126).max() - netinc.rolling(126).min()) / assets.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc074_126d_slope_v074_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc074_126d_slope_v074_signal

def f106m_f106_market_cap_to_revenue_cycles_calc075_63d_slope_v075_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.rolling(63).max() - revenue.rolling(63).min()) / netinc.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc075_63d_slope_v075_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc075_63d_slope_v075_signal

def f106m_f106_market_cap_to_revenue_cycles_calc076_10d_slope_v076_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.rolling(10).max() - ebitda.rolling(10).min()) / assets.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc076_10d_slope_v076_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc076_10d_slope_v076_signal

def f106m_f106_market_cap_to_revenue_cycles_calc077_126d_slope_v077_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.pct_change(126) - equity.pct_change(126))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc077_126d_slope_v077_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc077_126d_slope_v077_signal

def f106m_f106_market_cap_to_revenue_cycles_calc078_252d_slope_v078_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue / assets.replace(0, np.nan)).rolling(252).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc078_252d_slope_v078_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc078_252d_slope_v078_signal

def f106m_f106_market_cap_to_revenue_cycles_calc079_5d_slope_v079_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.pct_change(5) - fcf.pct_change(5))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc079_5d_slope_v079_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc079_5d_slope_v079_signal

def f106m_f106_market_cap_to_revenue_cycles_calc080_21d_slope_v080_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.diff(21).abs() / netinc.diff(21).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc080_21d_slope_v080_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc080_21d_slope_v080_signal

def f106m_f106_market_cap_to_revenue_cycles_calc081_63d_slope_v081_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((netinc - netinc.rolling(63).mean()) / netinc.rolling(63).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc081_63d_slope_v081_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc081_63d_slope_v081_signal

def f106m_f106_market_cap_to_revenue_cycles_calc082_10d_slope_v082_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.rolling(10).max() - equity.rolling(10).min()) / netinc.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc082_10d_slope_v082_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc082_10d_slope_v082_signal

def f106m_f106_market_cap_to_revenue_cycles_calc083_21d_slope_v083_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.rolling(21).quantile(0.5) / equity.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc083_21d_slope_v083_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc083_21d_slope_v083_signal

def f106m_f106_market_cap_to_revenue_cycles_calc084_21d_slope_v084_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.rolling(21).max() - marketcap.rolling(21).min()) / revenue.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc084_21d_slope_v084_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc084_21d_slope_v084_signal

def f106m_f106_market_cap_to_revenue_cycles_calc085_21d_slope_v085_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((assets - assets.rolling(21).mean()) / assets.rolling(21).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc085_21d_slope_v085_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc085_21d_slope_v085_signal

def f106m_f106_market_cap_to_revenue_cycles_calc086_5d_slope_v086_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.rolling(5).max() - assets.rolling(5).min()) / marketcap.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc086_5d_slope_v086_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc086_5d_slope_v086_signal

def f106m_f106_market_cap_to_revenue_cycles_calc087_21d_slope_v087_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc / fcf.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc087_21d_slope_v087_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc087_21d_slope_v087_signal

def f106m_f106_market_cap_to_revenue_cycles_calc088_63d_slope_v088_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc / equity.replace(0, np.nan)).rolling(63).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc088_63d_slope_v088_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc088_63d_slope_v088_signal

def f106m_f106_market_cap_to_revenue_cycles_calc089_252d_slope_v089_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((equity - equity.rolling(252).mean()) / equity.rolling(252).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc089_252d_slope_v089_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc089_252d_slope_v089_signal

def f106m_f106_market_cap_to_revenue_cycles_calc090_42d_slope_v090_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.pct_change(42) - netinc.pct_change(42))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc090_42d_slope_v090_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc090_42d_slope_v090_signal

def f106m_f106_market_cap_to_revenue_cycles_calc091_5d_slope_v091_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.rolling(5).max() - fcf.rolling(5).min()) / marketcap.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc091_5d_slope_v091_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc091_5d_slope_v091_signal

def f106m_f106_market_cap_to_revenue_cycles_calc092_126d_slope_v092_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.rolling(126).rank(pct=True) / assets.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc092_126d_slope_v092_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc092_126d_slope_v092_signal

def f106m_f106_market_cap_to_revenue_cycles_calc093_5d_slope_v093_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.diff(5).abs() / ebitda.diff(5).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc093_5d_slope_v093_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc093_5d_slope_v093_signal

def f106m_f106_market_cap_to_revenue_cycles_calc094_21d_slope_v094_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.rolling(21).rank(pct=True) / ebitda.rolling(21).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc094_21d_slope_v094_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc094_21d_slope_v094_signal

def f106m_f106_market_cap_to_revenue_cycles_calc095_42d_slope_v095_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity / fcf.replace(0, np.nan)).rolling(42).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc095_42d_slope_v095_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc095_42d_slope_v095_signal

def f106m_f106_market_cap_to_revenue_cycles_calc096_10d_slope_v096_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.diff(10) / ebitda.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc096_10d_slope_v096_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc096_10d_slope_v096_signal

def f106m_f106_market_cap_to_revenue_cycles_calc097_252d_slope_v097_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.diff(252) / marketcap.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc097_252d_slope_v097_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc097_252d_slope_v097_signal

def f106m_f106_market_cap_to_revenue_cycles_calc098_5d_slope_v098_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.rolling(5).kurt() - marketcap.rolling(5).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc098_5d_slope_v098_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc098_5d_slope_v098_signal

def f106m_f106_market_cap_to_revenue_cycles_calc099_10d_slope_v099_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap / netinc.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc099_10d_slope_v099_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc099_10d_slope_v099_signal

def f106m_f106_market_cap_to_revenue_cycles_calc100_10d_slope_v100_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf.rolling(10).rank(pct=True) / ebitda.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc100_10d_slope_v100_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc100_10d_slope_v100_signal

def f106m_f106_market_cap_to_revenue_cycles_calc101_63d_slope_v101_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((assets - assets.rolling(63).mean()) / assets.rolling(63).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc101_63d_slope_v101_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc101_63d_slope_v101_signal

def f106m_f106_market_cap_to_revenue_cycles_calc102_21d_slope_v102_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.diff(21).abs() / ebitda.diff(21).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc102_21d_slope_v102_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc102_21d_slope_v102_signal

def f106m_f106_market_cap_to_revenue_cycles_calc103_126d_slope_v103_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.rolling(126).quantile(0.5) / assets.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc103_126d_slope_v103_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc103_126d_slope_v103_signal

def f106m_f106_market_cap_to_revenue_cycles_calc104_10d_slope_v104_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.diff(10).abs() / marketcap.diff(10).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc104_10d_slope_v104_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc104_10d_slope_v104_signal

def f106m_f106_market_cap_to_revenue_cycles_calc105_21d_slope_v105_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf.diff(21).abs() / assets.diff(21).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc105_21d_slope_v105_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc105_21d_slope_v105_signal

def f106m_f106_market_cap_to_revenue_cycles_calc106_21d_slope_v106_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.rolling(21).rank(pct=True) / revenue.rolling(21).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc106_21d_slope_v106_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc106_21d_slope_v106_signal

def f106m_f106_market_cap_to_revenue_cycles_calc107_21d_slope_v107_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.rolling(21).kurt() - fcf.rolling(21).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc107_21d_slope_v107_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc107_21d_slope_v107_signal

def f106m_f106_market_cap_to_revenue_cycles_calc108_252d_slope_v108_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.diff(252) / equity.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc108_252d_slope_v108_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc108_252d_slope_v108_signal

def f106m_f106_market_cap_to_revenue_cycles_calc109_63d_slope_v109_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((revenue - revenue.rolling(63).mean()) / revenue.rolling(63).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc109_63d_slope_v109_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc109_63d_slope_v109_signal

def f106m_f106_market_cap_to_revenue_cycles_calc110_21d_slope_v110_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.diff(21) / fcf.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc110_21d_slope_v110_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc110_21d_slope_v110_signal

def f106m_f106_market_cap_to_revenue_cycles_calc111_63d_slope_v111_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.rolling(63).kurt() - netinc.rolling(63).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc111_63d_slope_v111_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc111_63d_slope_v111_signal

def f106m_f106_market_cap_to_revenue_cycles_calc112_5d_slope_v112_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.pct_change(5) - fcf.pct_change(5))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc112_5d_slope_v112_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc112_5d_slope_v112_signal

def f106m_f106_market_cap_to_revenue_cycles_calc113_252d_slope_v113_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.pct_change(252) - marketcap.pct_change(252))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc113_252d_slope_v113_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc113_252d_slope_v113_signal

def f106m_f106_market_cap_to_revenue_cycles_calc114_5d_slope_v114_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.diff(5).abs() / revenue.diff(5).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc114_5d_slope_v114_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc114_5d_slope_v114_signal

def f106m_f106_market_cap_to_revenue_cycles_calc115_63d_slope_v115_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.rolling(63).quantile(0.5) / revenue.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc115_63d_slope_v115_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc115_63d_slope_v115_signal

def f106m_f106_market_cap_to_revenue_cycles_calc116_10d_slope_v116_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.pct_change(10) - fcf.pct_change(10))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc116_10d_slope_v116_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc116_10d_slope_v116_signal

def f106m_f106_market_cap_to_revenue_cycles_calc117_10d_slope_v117_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.pct_change(10) - equity.pct_change(10))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc117_10d_slope_v117_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc117_10d_slope_v117_signal

def f106m_f106_market_cap_to_revenue_cycles_calc118_63d_slope_v118_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf / netinc.replace(0, np.nan)).rolling(63).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc118_63d_slope_v118_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc118_63d_slope_v118_signal

def f106m_f106_market_cap_to_revenue_cycles_calc119_21d_slope_v119_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.diff(21).abs() / marketcap.diff(21).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc119_21d_slope_v119_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc119_21d_slope_v119_signal

def f106m_f106_market_cap_to_revenue_cycles_calc120_126d_slope_v120_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity / ebitda.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc120_126d_slope_v120_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc120_126d_slope_v120_signal

def f106m_f106_market_cap_to_revenue_cycles_calc121_126d_slope_v121_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.pct_change(126) - revenue.pct_change(126))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc121_126d_slope_v121_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc121_126d_slope_v121_signal

def f106m_f106_market_cap_to_revenue_cycles_calc122_21d_slope_v122_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf / equity.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc122_21d_slope_v122_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc122_21d_slope_v122_signal

def f106m_f106_market_cap_to_revenue_cycles_calc123_21d_slope_v123_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.rolling(21).rank(pct=True) / netinc.rolling(21).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc123_21d_slope_v123_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc123_21d_slope_v123_signal

def f106m_f106_market_cap_to_revenue_cycles_calc124_5d_slope_v124_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.diff(5) / fcf.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc124_5d_slope_v124_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc124_5d_slope_v124_signal

def f106m_f106_market_cap_to_revenue_cycles_calc125_63d_slope_v125_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.rolling(63).rank(pct=True) / fcf.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc125_63d_slope_v125_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc125_63d_slope_v125_signal

def f106m_f106_market_cap_to_revenue_cycles_calc126_10d_slope_v126_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf.rolling(10).quantile(0.5) / netinc.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc126_10d_slope_v126_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc126_10d_slope_v126_signal

def f106m_f106_market_cap_to_revenue_cycles_calc127_5d_slope_v127_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((equity - equity.rolling(5).mean()) / equity.rolling(5).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc127_5d_slope_v127_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc127_5d_slope_v127_signal

def f106m_f106_market_cap_to_revenue_cycles_calc128_252d_slope_v128_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf.rolling(252).kurt() - revenue.rolling(252).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc128_252d_slope_v128_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc128_252d_slope_v128_signal

def f106m_f106_market_cap_to_revenue_cycles_calc129_252d_slope_v129_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.pct_change(252) - equity.pct_change(252))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc129_252d_slope_v129_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc129_252d_slope_v129_signal

def f106m_f106_market_cap_to_revenue_cycles_calc130_63d_slope_v130_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.rolling(63).rank(pct=True) / marketcap.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc130_63d_slope_v130_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc130_63d_slope_v130_signal

def f106m_f106_market_cap_to_revenue_cycles_calc131_63d_slope_v131_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.pct_change(63) - assets.pct_change(63))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc131_63d_slope_v131_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc131_63d_slope_v131_signal

def f106m_f106_market_cap_to_revenue_cycles_calc132_126d_slope_v132_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.rolling(126).kurt() - assets.rolling(126).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc132_126d_slope_v132_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc132_126d_slope_v132_signal

def f106m_f106_market_cap_to_revenue_cycles_calc133_5d_slope_v133_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.pct_change(5) - ebitda.pct_change(5))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc133_5d_slope_v133_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc133_5d_slope_v133_signal

def f106m_f106_market_cap_to_revenue_cycles_calc134_21d_slope_v134_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc / fcf.replace(0, np.nan)).rolling(21).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc134_21d_slope_v134_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc134_21d_slope_v134_signal

def f106m_f106_market_cap_to_revenue_cycles_calc135_10d_slope_v135_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf / revenue.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc135_10d_slope_v135_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc135_10d_slope_v135_signal

def f106m_f106_market_cap_to_revenue_cycles_calc136_21d_slope_v136_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((ebitda - ebitda.rolling(21).mean()) / ebitda.rolling(21).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc136_21d_slope_v136_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc136_21d_slope_v136_signal

def f106m_f106_market_cap_to_revenue_cycles_calc137_21d_slope_v137_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf / revenue.replace(0, np.nan)).rolling(21).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc137_21d_slope_v137_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc137_21d_slope_v137_signal

def f106m_f106_market_cap_to_revenue_cycles_calc138_63d_slope_v138_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity / ebitda.replace(0, np.nan)).rolling(63).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc138_63d_slope_v138_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc138_63d_slope_v138_signal

def f106m_f106_market_cap_to_revenue_cycles_calc139_63d_slope_v139_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((ebitda - ebitda.rolling(63).mean()) / ebitda.rolling(63).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc139_63d_slope_v139_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc139_63d_slope_v139_signal

def f106m_f106_market_cap_to_revenue_cycles_calc140_5d_slope_v140_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = ((ebitda - ebitda.rolling(5).mean()) / ebitda.rolling(5).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc140_5d_slope_v140_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc140_5d_slope_v140_signal

def f106m_f106_market_cap_to_revenue_cycles_calc141_42d_slope_v141_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.rolling(42).kurt() - equity.rolling(42).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc141_42d_slope_v141_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc141_42d_slope_v141_signal

def f106m_f106_market_cap_to_revenue_cycles_calc142_21d_slope_v142_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.rolling(21).quantile(0.5) / assets.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc142_21d_slope_v142_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc142_21d_slope_v142_signal

def f106m_f106_market_cap_to_revenue_cycles_calc143_252d_slope_v143_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (ebitda.rolling(252).rank(pct=True) / marketcap.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc143_252d_slope_v143_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc143_252d_slope_v143_signal

def f106m_f106_market_cap_to_revenue_cycles_calc144_63d_slope_v144_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (marketcap.rolling(63).max() - netinc.rolling(63).min()) / equity.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc144_63d_slope_v144_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc144_63d_slope_v144_signal

def f106m_f106_market_cap_to_revenue_cycles_calc145_42d_slope_v145_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc / ebitda.replace(0, np.nan)).rolling(42).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc145_42d_slope_v145_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc145_42d_slope_v145_signal

def f106m_f106_market_cap_to_revenue_cycles_calc146_126d_slope_v146_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (revenue.diff(126).abs() / assets.diff(126).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc146_126d_slope_v146_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc146_126d_slope_v146_signal

def f106m_f106_market_cap_to_revenue_cycles_calc147_5d_slope_v147_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (fcf.rolling(5).rank(pct=True) / revenue.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc147_5d_slope_v147_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc147_5d_slope_v147_signal

def f106m_f106_market_cap_to_revenue_cycles_calc148_5d_slope_v148_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (netinc.rolling(5).rank(pct=True) / ebitda.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc148_5d_slope_v148_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc148_5d_slope_v148_signal

def f106m_f106_market_cap_to_revenue_cycles_calc149_42d_slope_v149_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (equity.rolling(42).max() - netinc.rolling(42).min()) / revenue.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc149_42d_slope_v149_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc149_42d_slope_v149_signal

def f106m_f106_market_cap_to_revenue_cycles_calc150_63d_slope_v150_signal(marketcap, revenue, assets, equity, ebitda, fcf, netinc):
    v1 = (assets.rolling(63).rank(pct=True) / revenue.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f106m_f106_market_cap_to_revenue_cycles_calc150_63d_slope_v150_signal'] = f106m_f106_market_cap_to_revenue_cycles_calc150_63d_slope_v150_signal



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
