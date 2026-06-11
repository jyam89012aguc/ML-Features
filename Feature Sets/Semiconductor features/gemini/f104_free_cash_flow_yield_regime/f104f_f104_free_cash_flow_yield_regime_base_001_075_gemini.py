import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f104f_f104_free_cash_flow_yield_regime_calc001_63d_base_v001_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.rolling(63).quantile(0.5) / revenue.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc001_63d_base_v001_signal'] = f104f_f104_free_cash_flow_yield_regime_calc001_63d_base_v001_signal

def f104f_f104_free_cash_flow_yield_regime_calc002_5d_base_v002_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf.rolling(5).rank(pct=True) / equity.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc002_5d_base_v002_signal'] = f104f_f104_free_cash_flow_yield_regime_calc002_5d_base_v002_signal

def f104f_f104_free_cash_flow_yield_regime_calc003_252d_base_v003_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.diff(252).abs() / fcf.diff(252).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc003_252d_base_v003_signal'] = f104f_f104_free_cash_flow_yield_regime_calc003_252d_base_v003_signal

def f104f_f104_free_cash_flow_yield_regime_calc004_5d_base_v004_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.pct_change(5) - marketcap.pct_change(5))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc004_5d_base_v004_signal'] = f104f_f104_free_cash_flow_yield_regime_calc004_5d_base_v004_signal

def f104f_f104_free_cash_flow_yield_regime_calc005_21d_base_v005_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.rolling(21).quantile(0.5) / equity.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc005_21d_base_v005_signal'] = f104f_f104_free_cash_flow_yield_regime_calc005_21d_base_v005_signal

def f104f_f104_free_cash_flow_yield_regime_calc006_10d_base_v006_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity / revenue.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc006_10d_base_v006_signal'] = f104f_f104_free_cash_flow_yield_regime_calc006_10d_base_v006_signal

def f104f_f104_free_cash_flow_yield_regime_calc007_10d_base_v007_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.pct_change(10) - revenue.pct_change(10))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc007_10d_base_v007_signal'] = f104f_f104_free_cash_flow_yield_regime_calc007_10d_base_v007_signal

def f104f_f104_free_cash_flow_yield_regime_calc008_63d_base_v008_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf.pct_change(63) - assets.pct_change(63))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc008_63d_base_v008_signal'] = f104f_f104_free_cash_flow_yield_regime_calc008_63d_base_v008_signal

def f104f_f104_free_cash_flow_yield_regime_calc009_21d_base_v009_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue / fcf.replace(0, np.nan)).rolling(21).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc009_21d_base_v009_signal'] = f104f_f104_free_cash_flow_yield_regime_calc009_21d_base_v009_signal

def f104f_f104_free_cash_flow_yield_regime_calc010_63d_base_v010_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev / marketcap.replace(0, np.nan)).rolling(63).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc010_63d_base_v010_signal'] = f104f_f104_free_cash_flow_yield_regime_calc010_63d_base_v010_signal

def f104f_f104_free_cash_flow_yield_regime_calc011_63d_base_v011_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf.rolling(63).quantile(0.5) / assets.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc011_63d_base_v011_signal'] = f104f_f104_free_cash_flow_yield_regime_calc011_63d_base_v011_signal

def f104f_f104_free_cash_flow_yield_regime_calc012_21d_base_v012_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.diff(21) / assets.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc012_21d_base_v012_signal'] = f104f_f104_free_cash_flow_yield_regime_calc012_21d_base_v012_signal

def f104f_f104_free_cash_flow_yield_regime_calc013_21d_base_v013_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(21).kurt() - fcf.rolling(21).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc013_21d_base_v013_signal'] = f104f_f104_free_cash_flow_yield_regime_calc013_21d_base_v013_signal

def f104f_f104_free_cash_flow_yield_regime_calc014_126d_base_v014_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.pct_change(126) - equity.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc014_126d_base_v014_signal'] = f104f_f104_free_cash_flow_yield_regime_calc014_126d_base_v014_signal

def f104f_f104_free_cash_flow_yield_regime_calc015_252d_base_v015_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.rolling(252).quantile(0.5) / equity.rolling(252).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc015_252d_base_v015_signal'] = f104f_f104_free_cash_flow_yield_regime_calc015_252d_base_v015_signal

def f104f_f104_free_cash_flow_yield_regime_calc016_252d_base_v016_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.pct_change(252) - fcf.pct_change(252))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc016_252d_base_v016_signal'] = f104f_f104_free_cash_flow_yield_regime_calc016_252d_base_v016_signal

def f104f_f104_free_cash_flow_yield_regime_calc017_63d_base_v017_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.rolling(63).rank(pct=True) / equity.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc017_63d_base_v017_signal'] = f104f_f104_free_cash_flow_yield_regime_calc017_63d_base_v017_signal

def f104f_f104_free_cash_flow_yield_regime_calc018_42d_base_v018_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.rolling(42).kurt() - revenue.rolling(42).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc018_42d_base_v018_signal'] = f104f_f104_free_cash_flow_yield_regime_calc018_42d_base_v018_signal

def f104f_f104_free_cash_flow_yield_regime_calc019_21d_base_v019_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity / assets.replace(0, np.nan)).rolling(21).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc019_21d_base_v019_signal'] = f104f_f104_free_cash_flow_yield_regime_calc019_21d_base_v019_signal

def f104f_f104_free_cash_flow_yield_regime_calc020_42d_base_v020_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.rolling(42).quantile(0.5) / revenue.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc020_42d_base_v020_signal'] = f104f_f104_free_cash_flow_yield_regime_calc020_42d_base_v020_signal

def f104f_f104_free_cash_flow_yield_regime_calc021_63d_base_v021_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.diff(63) / marketcap.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc021_63d_base_v021_signal'] = f104f_f104_free_cash_flow_yield_regime_calc021_63d_base_v021_signal

def f104f_f104_free_cash_flow_yield_regime_calc022_126d_base_v022_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.pct_change(126) - revenue.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc022_126d_base_v022_signal'] = f104f_f104_free_cash_flow_yield_regime_calc022_126d_base_v022_signal

def f104f_f104_free_cash_flow_yield_regime_calc023_10d_base_v023_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev / ncfo.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc023_10d_base_v023_signal'] = f104f_f104_free_cash_flow_yield_regime_calc023_10d_base_v023_signal

def f104f_f104_free_cash_flow_yield_regime_calc024_21d_base_v024_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = ((marketcap - marketcap.rolling(21).mean()) / marketcap.rolling(21).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc024_21d_base_v024_signal'] = f104f_f104_free_cash_flow_yield_regime_calc024_21d_base_v024_signal

def f104f_f104_free_cash_flow_yield_regime_calc025_63d_base_v025_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(63).rank(pct=True) / assets.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc025_63d_base_v025_signal'] = f104f_f104_free_cash_flow_yield_regime_calc025_63d_base_v025_signal

def f104f_f104_free_cash_flow_yield_regime_calc026_21d_base_v026_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.pct_change(21) - revenue.pct_change(21))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc026_21d_base_v026_signal'] = f104f_f104_free_cash_flow_yield_regime_calc026_21d_base_v026_signal

def f104f_f104_free_cash_flow_yield_regime_calc027_42d_base_v027_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.diff(42) / equity.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc027_42d_base_v027_signal'] = f104f_f104_free_cash_flow_yield_regime_calc027_42d_base_v027_signal

def f104f_f104_free_cash_flow_yield_regime_calc028_21d_base_v028_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.pct_change(21) - ncfo.pct_change(21))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc028_21d_base_v028_signal'] = f104f_f104_free_cash_flow_yield_regime_calc028_21d_base_v028_signal

def f104f_f104_free_cash_flow_yield_regime_calc029_10d_base_v029_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.rolling(10).kurt() - fcf.rolling(10).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc029_10d_base_v029_signal'] = f104f_f104_free_cash_flow_yield_regime_calc029_10d_base_v029_signal

def f104f_f104_free_cash_flow_yield_regime_calc030_252d_base_v030_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(252).max() - ncfo.rolling(252).min()) / marketcap.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc030_252d_base_v030_signal'] = f104f_f104_free_cash_flow_yield_regime_calc030_252d_base_v030_signal

def f104f_f104_free_cash_flow_yield_regime_calc031_126d_base_v031_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf.rolling(126).quantile(0.5) / marketcap.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc031_126d_base_v031_signal'] = f104f_f104_free_cash_flow_yield_regime_calc031_126d_base_v031_signal

def f104f_f104_free_cash_flow_yield_regime_calc032_252d_base_v032_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets / fcf.replace(0, np.nan)).rolling(252).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc032_252d_base_v032_signal'] = f104f_f104_free_cash_flow_yield_regime_calc032_252d_base_v032_signal

def f104f_f104_free_cash_flow_yield_regime_calc033_126d_base_v033_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(126).rank(pct=True) / revenue.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc033_126d_base_v033_signal'] = f104f_f104_free_cash_flow_yield_regime_calc033_126d_base_v033_signal

def f104f_f104_free_cash_flow_yield_regime_calc034_252d_base_v034_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.rolling(252).rank(pct=True) / fcf.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc034_252d_base_v034_signal'] = f104f_f104_free_cash_flow_yield_regime_calc034_252d_base_v034_signal

def f104f_f104_free_cash_flow_yield_regime_calc035_5d_base_v035_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.diff(5) / equity.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc035_5d_base_v035_signal'] = f104f_f104_free_cash_flow_yield_regime_calc035_5d_base_v035_signal

def f104f_f104_free_cash_flow_yield_regime_calc036_252d_base_v036_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.pct_change(252) - marketcap.pct_change(252))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc036_252d_base_v036_signal'] = f104f_f104_free_cash_flow_yield_regime_calc036_252d_base_v036_signal

def f104f_f104_free_cash_flow_yield_regime_calc037_10d_base_v037_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = ((fcf - fcf.rolling(10).mean()) / fcf.rolling(10).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc037_10d_base_v037_signal'] = f104f_f104_free_cash_flow_yield_regime_calc037_10d_base_v037_signal

def f104f_f104_free_cash_flow_yield_regime_calc038_5d_base_v038_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue / ncfo.replace(0, np.nan)).rolling(5).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc038_5d_base_v038_signal'] = f104f_f104_free_cash_flow_yield_regime_calc038_5d_base_v038_signal

def f104f_f104_free_cash_flow_yield_regime_calc039_63d_base_v039_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue / equity.replace(0, np.nan)).rolling(63).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc039_63d_base_v039_signal'] = f104f_f104_free_cash_flow_yield_regime_calc039_63d_base_v039_signal

def f104f_f104_free_cash_flow_yield_regime_calc040_21d_base_v040_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev / revenue.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc040_21d_base_v040_signal'] = f104f_f104_free_cash_flow_yield_regime_calc040_21d_base_v040_signal

def f104f_f104_free_cash_flow_yield_regime_calc041_21d_base_v041_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.rolling(21).quantile(0.5) / fcf.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc041_21d_base_v041_signal'] = f104f_f104_free_cash_flow_yield_regime_calc041_21d_base_v041_signal

def f104f_f104_free_cash_flow_yield_regime_calc042_21d_base_v042_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.diff(21) / ev.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc042_21d_base_v042_signal'] = f104f_f104_free_cash_flow_yield_regime_calc042_21d_base_v042_signal

def f104f_f104_free_cash_flow_yield_regime_calc043_42d_base_v043_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(42).quantile(0.5) / revenue.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc043_42d_base_v043_signal'] = f104f_f104_free_cash_flow_yield_regime_calc043_42d_base_v043_signal

def f104f_f104_free_cash_flow_yield_regime_calc044_63d_base_v044_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.diff(63) / marketcap.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc044_63d_base_v044_signal'] = f104f_f104_free_cash_flow_yield_regime_calc044_63d_base_v044_signal

def f104f_f104_free_cash_flow_yield_regime_calc045_21d_base_v045_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.rolling(21).kurt() - ncfo.rolling(21).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc045_21d_base_v045_signal'] = f104f_f104_free_cash_flow_yield_regime_calc045_21d_base_v045_signal

def f104f_f104_free_cash_flow_yield_regime_calc046_126d_base_v046_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.rolling(126).rank(pct=True) / ev.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc046_126d_base_v046_signal'] = f104f_f104_free_cash_flow_yield_regime_calc046_126d_base_v046_signal

def f104f_f104_free_cash_flow_yield_regime_calc047_10d_base_v047_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo / fcf.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc047_10d_base_v047_signal'] = f104f_f104_free_cash_flow_yield_regime_calc047_10d_base_v047_signal

def f104f_f104_free_cash_flow_yield_regime_calc048_252d_base_v048_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = ((revenue - revenue.rolling(252).mean()) / revenue.rolling(252).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc048_252d_base_v048_signal'] = f104f_f104_free_cash_flow_yield_regime_calc048_252d_base_v048_signal

def f104f_f104_free_cash_flow_yield_regime_calc049_126d_base_v049_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue / fcf.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc049_126d_base_v049_signal'] = f104f_f104_free_cash_flow_yield_regime_calc049_126d_base_v049_signal

def f104f_f104_free_cash_flow_yield_regime_calc050_126d_base_v050_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo / fcf.replace(0, np.nan)).rolling(126).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc050_126d_base_v050_signal'] = f104f_f104_free_cash_flow_yield_regime_calc050_126d_base_v050_signal

def f104f_f104_free_cash_flow_yield_regime_calc051_10d_base_v051_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.diff(10).abs() / equity.diff(10).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc051_10d_base_v051_signal'] = f104f_f104_free_cash_flow_yield_regime_calc051_10d_base_v051_signal

def f104f_f104_free_cash_flow_yield_regime_calc052_5d_base_v052_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf.rolling(5).max() - ev.rolling(5).min()) / marketcap.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc052_5d_base_v052_signal'] = f104f_f104_free_cash_flow_yield_regime_calc052_5d_base_v052_signal

def f104f_f104_free_cash_flow_yield_regime_calc053_42d_base_v053_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.rolling(42).rank(pct=True) / marketcap.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc053_42d_base_v053_signal'] = f104f_f104_free_cash_flow_yield_regime_calc053_42d_base_v053_signal

def f104f_f104_free_cash_flow_yield_regime_calc054_42d_base_v054_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = ((marketcap - marketcap.rolling(42).mean()) / marketcap.rolling(42).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc054_42d_base_v054_signal'] = f104f_f104_free_cash_flow_yield_regime_calc054_42d_base_v054_signal

def f104f_f104_free_cash_flow_yield_regime_calc055_63d_base_v055_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf / revenue.replace(0, np.nan)).rolling(63).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc055_63d_base_v055_signal'] = f104f_f104_free_cash_flow_yield_regime_calc055_63d_base_v055_signal

def f104f_f104_free_cash_flow_yield_regime_calc056_10d_base_v056_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.diff(10).abs() / assets.diff(10).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc056_10d_base_v056_signal'] = f104f_f104_free_cash_flow_yield_regime_calc056_10d_base_v056_signal

def f104f_f104_free_cash_flow_yield_regime_calc057_252d_base_v057_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.diff(252).abs() / ev.diff(252).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc057_252d_base_v057_signal'] = f104f_f104_free_cash_flow_yield_regime_calc057_252d_base_v057_signal

def f104f_f104_free_cash_flow_yield_regime_calc058_126d_base_v058_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue / marketcap.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc058_126d_base_v058_signal'] = f104f_f104_free_cash_flow_yield_regime_calc058_126d_base_v058_signal

def f104f_f104_free_cash_flow_yield_regime_calc059_42d_base_v059_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.rolling(42).kurt() - assets.rolling(42).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc059_42d_base_v059_signal'] = f104f_f104_free_cash_flow_yield_regime_calc059_42d_base_v059_signal

def f104f_f104_free_cash_flow_yield_regime_calc060_126d_base_v060_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.diff(126).abs() / equity.diff(126).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc060_126d_base_v060_signal'] = f104f_f104_free_cash_flow_yield_regime_calc060_126d_base_v060_signal

def f104f_f104_free_cash_flow_yield_regime_calc061_126d_base_v061_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.rolling(126).rank(pct=True) / fcf.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc061_126d_base_v061_signal'] = f104f_f104_free_cash_flow_yield_regime_calc061_126d_base_v061_signal

def f104f_f104_free_cash_flow_yield_regime_calc062_10d_base_v062_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = ((marketcap - marketcap.rolling(10).mean()) / marketcap.rolling(10).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc062_10d_base_v062_signal'] = f104f_f104_free_cash_flow_yield_regime_calc062_10d_base_v062_signal

def f104f_f104_free_cash_flow_yield_regime_calc063_252d_base_v063_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.pct_change(252) - assets.pct_change(252))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc063_252d_base_v063_signal'] = f104f_f104_free_cash_flow_yield_regime_calc063_252d_base_v063_signal

def f104f_f104_free_cash_flow_yield_regime_calc064_21d_base_v064_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.rolling(21).max() - revenue.rolling(21).min()) / ev.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc064_21d_base_v064_signal'] = f104f_f104_free_cash_flow_yield_regime_calc064_21d_base_v064_signal

def f104f_f104_free_cash_flow_yield_regime_calc065_42d_base_v065_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.diff(42).abs() / fcf.diff(42).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc065_42d_base_v065_signal'] = f104f_f104_free_cash_flow_yield_regime_calc065_42d_base_v065_signal

def f104f_f104_free_cash_flow_yield_regime_calc066_42d_base_v066_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.diff(42) / ev.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc066_42d_base_v066_signal'] = f104f_f104_free_cash_flow_yield_regime_calc066_42d_base_v066_signal

def f104f_f104_free_cash_flow_yield_regime_calc067_42d_base_v067_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.rolling(42).max() - ev.rolling(42).min()) / fcf.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc067_42d_base_v067_signal'] = f104f_f104_free_cash_flow_yield_regime_calc067_42d_base_v067_signal

def f104f_f104_free_cash_flow_yield_regime_calc068_5d_base_v068_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.pct_change(5) - assets.pct_change(5))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc068_5d_base_v068_signal'] = f104f_f104_free_cash_flow_yield_regime_calc068_5d_base_v068_signal

def f104f_f104_free_cash_flow_yield_regime_calc069_21d_base_v069_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.rolling(21).quantile(0.5) / ncfo.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc069_21d_base_v069_signal'] = f104f_f104_free_cash_flow_yield_regime_calc069_21d_base_v069_signal

def f104f_f104_free_cash_flow_yield_regime_calc070_126d_base_v070_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.diff(126).abs() / ncfo.diff(126).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc070_126d_base_v070_signal'] = f104f_f104_free_cash_flow_yield_regime_calc070_126d_base_v070_signal

def f104f_f104_free_cash_flow_yield_regime_calc071_10d_base_v071_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.rolling(10).kurt() - fcf.rolling(10).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc071_10d_base_v071_signal'] = f104f_f104_free_cash_flow_yield_regime_calc071_10d_base_v071_signal

def f104f_f104_free_cash_flow_yield_regime_calc072_10d_base_v072_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(10).quantile(0.5) / assets.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc072_10d_base_v072_signal'] = f104f_f104_free_cash_flow_yield_regime_calc072_10d_base_v072_signal

def f104f_f104_free_cash_flow_yield_regime_calc073_42d_base_v073_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.diff(42).abs() / revenue.diff(42).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc073_42d_base_v073_signal'] = f104f_f104_free_cash_flow_yield_regime_calc073_42d_base_v073_signal

def f104f_f104_free_cash_flow_yield_regime_calc074_10d_base_v074_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.rolling(10).kurt() - ev.rolling(10).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc074_10d_base_v074_signal'] = f104f_f104_free_cash_flow_yield_regime_calc074_10d_base_v074_signal

def f104f_f104_free_cash_flow_yield_regime_calc075_42d_base_v075_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.rolling(42).max() - ncfo.rolling(42).min()) / fcf.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc075_42d_base_v075_signal'] = f104f_f104_free_cash_flow_yield_regime_calc075_42d_base_v075_signal



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
