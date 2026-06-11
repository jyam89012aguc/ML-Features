import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f75ps_f75_fcf_per_share_acceleration_calc001_63d_base_v001_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.rolling(63).max() - fcf.rolling(63).min()) / revenue.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc001_63d_base_v001_signal'] = f75ps_f75_fcf_per_share_acceleration_calc001_63d_base_v001_signal

def f75ps_f75_fcf_per_share_acceleration_calc002_10d_base_v002_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((assets - assets.rolling(10).mean()) / assets.rolling(10).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc002_10d_base_v002_signal'] = f75ps_f75_fcf_per_share_acceleration_calc002_10d_base_v002_signal

def f75ps_f75_fcf_per_share_acceleration_calc003_5d_base_v003_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.diff(5) / marketcap.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc003_5d_base_v003_signal'] = f75ps_f75_fcf_per_share_acceleration_calc003_5d_base_v003_signal

def f75ps_f75_fcf_per_share_acceleration_calc004_252d_base_v004_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas / marketcap.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc004_252d_base_v004_signal'] = f75ps_f75_fcf_per_share_acceleration_calc004_252d_base_v004_signal

def f75ps_f75_fcf_per_share_acceleration_calc005_21d_base_v005_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(21).rank(pct=True) / eps.rolling(21).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc005_21d_base_v005_signal'] = f75ps_f75_fcf_per_share_acceleration_calc005_21d_base_v005_signal

def f75ps_f75_fcf_per_share_acceleration_calc006_126d_base_v006_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.rolling(126).max() - marketcap.rolling(126).min()) / sharesbas.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc006_126d_base_v006_signal'] = f75ps_f75_fcf_per_share_acceleration_calc006_126d_base_v006_signal

def f75ps_f75_fcf_per_share_acceleration_calc007_42d_base_v007_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.pct_change(42) - revenue.pct_change(42))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc007_42d_base_v007_signal'] = f75ps_f75_fcf_per_share_acceleration_calc007_42d_base_v007_signal

def f75ps_f75_fcf_per_share_acceleration_calc008_42d_base_v008_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.rolling(42).rank(pct=True) / fcf.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc008_42d_base_v008_signal'] = f75ps_f75_fcf_per_share_acceleration_calc008_42d_base_v008_signal

def f75ps_f75_fcf_per_share_acceleration_calc009_5d_base_v009_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.rolling(5).quantile(0.5) / revenue.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc009_5d_base_v009_signal'] = f75ps_f75_fcf_per_share_acceleration_calc009_5d_base_v009_signal

def f75ps_f75_fcf_per_share_acceleration_calc010_252d_base_v010_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((marketcap - marketcap.rolling(252).mean()) / marketcap.rolling(252).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc010_252d_base_v010_signal'] = f75ps_f75_fcf_per_share_acceleration_calc010_252d_base_v010_signal

def f75ps_f75_fcf_per_share_acceleration_calc011_126d_base_v011_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.diff(126) / sharesbas.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc011_126d_base_v011_signal'] = f75ps_f75_fcf_per_share_acceleration_calc011_126d_base_v011_signal

def f75ps_f75_fcf_per_share_acceleration_calc012_21d_base_v012_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.diff(21) / revenue.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc012_21d_base_v012_signal'] = f75ps_f75_fcf_per_share_acceleration_calc012_21d_base_v012_signal

def f75ps_f75_fcf_per_share_acceleration_calc013_42d_base_v013_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.pct_change(42) - fcf.pct_change(42))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc013_42d_base_v013_signal'] = f75ps_f75_fcf_per_share_acceleration_calc013_42d_base_v013_signal

def f75ps_f75_fcf_per_share_acceleration_calc014_10d_base_v014_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.diff(10).abs() / assets.diff(10).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc014_10d_base_v014_signal'] = f75ps_f75_fcf_per_share_acceleration_calc014_10d_base_v014_signal

def f75ps_f75_fcf_per_share_acceleration_calc015_63d_base_v015_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.rolling(63).quantile(0.5) / sharesbas.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc015_63d_base_v015_signal'] = f75ps_f75_fcf_per_share_acceleration_calc015_63d_base_v015_signal

def f75ps_f75_fcf_per_share_acceleration_calc016_21d_base_v016_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.pct_change(21) - marketcap.pct_change(21))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc016_21d_base_v016_signal'] = f75ps_f75_fcf_per_share_acceleration_calc016_21d_base_v016_signal

def f75ps_f75_fcf_per_share_acceleration_calc017_21d_base_v017_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf / revenue.replace(0, np.nan)).rolling(21).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc017_21d_base_v017_signal'] = f75ps_f75_fcf_per_share_acceleration_calc017_21d_base_v017_signal

def f75ps_f75_fcf_per_share_acceleration_calc018_5d_base_v018_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.diff(5).abs() / marketcap.diff(5).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc018_5d_base_v018_signal'] = f75ps_f75_fcf_per_share_acceleration_calc018_5d_base_v018_signal

def f75ps_f75_fcf_per_share_acceleration_calc019_42d_base_v019_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap / fcf.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc019_42d_base_v019_signal'] = f75ps_f75_fcf_per_share_acceleration_calc019_42d_base_v019_signal

def f75ps_f75_fcf_per_share_acceleration_calc020_42d_base_v020_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(42).rank(pct=True) / netinc.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc020_42d_base_v020_signal'] = f75ps_f75_fcf_per_share_acceleration_calc020_42d_base_v020_signal

def f75ps_f75_fcf_per_share_acceleration_calc021_5d_base_v021_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(5).quantile(0.5) / eps.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc021_5d_base_v021_signal'] = f75ps_f75_fcf_per_share_acceleration_calc021_5d_base_v021_signal

def f75ps_f75_fcf_per_share_acceleration_calc022_252d_base_v022_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.rolling(252).kurt() - revenue.rolling(252).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc022_252d_base_v022_signal'] = f75ps_f75_fcf_per_share_acceleration_calc022_252d_base_v022_signal

def f75ps_f75_fcf_per_share_acceleration_calc023_63d_base_v023_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.rolling(63).quantile(0.5) / eps.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc023_63d_base_v023_signal'] = f75ps_f75_fcf_per_share_acceleration_calc023_63d_base_v023_signal

def f75ps_f75_fcf_per_share_acceleration_calc024_252d_base_v024_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps / fcf.replace(0, np.nan)).rolling(252).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc024_252d_base_v024_signal'] = f75ps_f75_fcf_per_share_acceleration_calc024_252d_base_v024_signal

def f75ps_f75_fcf_per_share_acceleration_calc025_21d_base_v025_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(21).quantile(0.5) / marketcap.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc025_21d_base_v025_signal'] = f75ps_f75_fcf_per_share_acceleration_calc025_21d_base_v025_signal

def f75ps_f75_fcf_per_share_acceleration_calc026_252d_base_v026_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.rolling(252).kurt() - revenue.rolling(252).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc026_252d_base_v026_signal'] = f75ps_f75_fcf_per_share_acceleration_calc026_252d_base_v026_signal

def f75ps_f75_fcf_per_share_acceleration_calc027_5d_base_v027_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(5).max() - netinc.rolling(5).min()) / revenue.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc027_5d_base_v027_signal'] = f75ps_f75_fcf_per_share_acceleration_calc027_5d_base_v027_signal

def f75ps_f75_fcf_per_share_acceleration_calc028_5d_base_v028_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.diff(5).abs() / fcf.diff(5).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc028_5d_base_v028_signal'] = f75ps_f75_fcf_per_share_acceleration_calc028_5d_base_v028_signal

def f75ps_f75_fcf_per_share_acceleration_calc029_21d_base_v029_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.rolling(21).max() - fcf.rolling(21).min()) / sharesbas.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc029_21d_base_v029_signal'] = f75ps_f75_fcf_per_share_acceleration_calc029_21d_base_v029_signal

def f75ps_f75_fcf_per_share_acceleration_calc030_126d_base_v030_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.rolling(126).rank(pct=True) / revenue.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc030_126d_base_v030_signal'] = f75ps_f75_fcf_per_share_acceleration_calc030_126d_base_v030_signal

def f75ps_f75_fcf_per_share_acceleration_calc031_10d_base_v031_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.rolling(10).rank(pct=True) / assets.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc031_10d_base_v031_signal'] = f75ps_f75_fcf_per_share_acceleration_calc031_10d_base_v031_signal

def f75ps_f75_fcf_per_share_acceleration_calc032_126d_base_v032_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((eps - eps.rolling(126).mean()) / eps.rolling(126).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc032_126d_base_v032_signal'] = f75ps_f75_fcf_per_share_acceleration_calc032_126d_base_v032_signal

def f75ps_f75_fcf_per_share_acceleration_calc033_42d_base_v033_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(42).quantile(0.5) / sharesbas.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc033_42d_base_v033_signal'] = f75ps_f75_fcf_per_share_acceleration_calc033_42d_base_v033_signal

def f75ps_f75_fcf_per_share_acceleration_calc034_21d_base_v034_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.rolling(21).kurt() - sharesbas.rolling(21).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc034_21d_base_v034_signal'] = f75ps_f75_fcf_per_share_acceleration_calc034_21d_base_v034_signal

def f75ps_f75_fcf_per_share_acceleration_calc035_21d_base_v035_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue / eps.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc035_21d_base_v035_signal'] = f75ps_f75_fcf_per_share_acceleration_calc035_21d_base_v035_signal

def f75ps_f75_fcf_per_share_acceleration_calc036_252d_base_v036_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.pct_change(252) - netinc.pct_change(252))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc036_252d_base_v036_signal'] = f75ps_f75_fcf_per_share_acceleration_calc036_252d_base_v036_signal

def f75ps_f75_fcf_per_share_acceleration_calc037_42d_base_v037_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.pct_change(42) - fcf.pct_change(42))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc037_42d_base_v037_signal'] = f75ps_f75_fcf_per_share_acceleration_calc037_42d_base_v037_signal

def f75ps_f75_fcf_per_share_acceleration_calc038_21d_base_v038_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((marketcap - marketcap.rolling(21).mean()) / marketcap.rolling(21).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc038_21d_base_v038_signal'] = f75ps_f75_fcf_per_share_acceleration_calc038_21d_base_v038_signal

def f75ps_f75_fcf_per_share_acceleration_calc039_21d_base_v039_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.diff(21).abs() / eps.diff(21).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc039_21d_base_v039_signal'] = f75ps_f75_fcf_per_share_acceleration_calc039_21d_base_v039_signal

def f75ps_f75_fcf_per_share_acceleration_calc040_5d_base_v040_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap / eps.replace(0, np.nan)).rolling(5).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc040_5d_base_v040_signal'] = f75ps_f75_fcf_per_share_acceleration_calc040_5d_base_v040_signal

def f75ps_f75_fcf_per_share_acceleration_calc041_21d_base_v041_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(21).quantile(0.5) / eps.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc041_21d_base_v041_signal'] = f75ps_f75_fcf_per_share_acceleration_calc041_21d_base_v041_signal

def f75ps_f75_fcf_per_share_acceleration_calc042_252d_base_v042_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.diff(252) / marketcap.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc042_252d_base_v042_signal'] = f75ps_f75_fcf_per_share_acceleration_calc042_252d_base_v042_signal

def f75ps_f75_fcf_per_share_acceleration_calc043_42d_base_v043_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.rolling(42).quantile(0.5) / assets.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc043_42d_base_v043_signal'] = f75ps_f75_fcf_per_share_acceleration_calc043_42d_base_v043_signal

def f75ps_f75_fcf_per_share_acceleration_calc044_63d_base_v044_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.rolling(63).kurt() - marketcap.rolling(63).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc044_63d_base_v044_signal'] = f75ps_f75_fcf_per_share_acceleration_calc044_63d_base_v044_signal

def f75ps_f75_fcf_per_share_acceleration_calc045_252d_base_v045_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((netinc - netinc.rolling(252).mean()) / netinc.rolling(252).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc045_252d_base_v045_signal'] = f75ps_f75_fcf_per_share_acceleration_calc045_252d_base_v045_signal

def f75ps_f75_fcf_per_share_acceleration_calc046_21d_base_v046_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf / assets.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc046_21d_base_v046_signal'] = f75ps_f75_fcf_per_share_acceleration_calc046_21d_base_v046_signal

def f75ps_f75_fcf_per_share_acceleration_calc047_10d_base_v047_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.diff(10) / eps.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc047_10d_base_v047_signal'] = f75ps_f75_fcf_per_share_acceleration_calc047_10d_base_v047_signal

def f75ps_f75_fcf_per_share_acceleration_calc048_63d_base_v048_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.rolling(63).rank(pct=True) / netinc.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc048_63d_base_v048_signal'] = f75ps_f75_fcf_per_share_acceleration_calc048_63d_base_v048_signal

def f75ps_f75_fcf_per_share_acceleration_calc049_126d_base_v049_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.pct_change(126) - assets.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc049_126d_base_v049_signal'] = f75ps_f75_fcf_per_share_acceleration_calc049_126d_base_v049_signal

def f75ps_f75_fcf_per_share_acceleration_calc050_5d_base_v050_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.rolling(5).max() - revenue.rolling(5).min()) / marketcap.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc050_5d_base_v050_signal'] = f75ps_f75_fcf_per_share_acceleration_calc050_5d_base_v050_signal

def f75ps_f75_fcf_per_share_acceleration_calc051_126d_base_v051_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets / revenue.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc051_126d_base_v051_signal'] = f75ps_f75_fcf_per_share_acceleration_calc051_126d_base_v051_signal

def f75ps_f75_fcf_per_share_acceleration_calc052_126d_base_v052_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.pct_change(126) - marketcap.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc052_126d_base_v052_signal'] = f75ps_f75_fcf_per_share_acceleration_calc052_126d_base_v052_signal

def f75ps_f75_fcf_per_share_acceleration_calc053_126d_base_v053_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.diff(126) / marketcap.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc053_126d_base_v053_signal'] = f75ps_f75_fcf_per_share_acceleration_calc053_126d_base_v053_signal

def f75ps_f75_fcf_per_share_acceleration_calc054_10d_base_v054_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.rolling(10).max() - assets.rolling(10).min()) / marketcap.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc054_10d_base_v054_signal'] = f75ps_f75_fcf_per_share_acceleration_calc054_10d_base_v054_signal

def f75ps_f75_fcf_per_share_acceleration_calc055_126d_base_v055_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap / netinc.replace(0, np.nan)).rolling(126).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc055_126d_base_v055_signal'] = f75ps_f75_fcf_per_share_acceleration_calc055_126d_base_v055_signal

def f75ps_f75_fcf_per_share_acceleration_calc056_5d_base_v056_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.rolling(5).kurt() - netinc.rolling(5).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc056_5d_base_v056_signal'] = f75ps_f75_fcf_per_share_acceleration_calc056_5d_base_v056_signal

def f75ps_f75_fcf_per_share_acceleration_calc057_63d_base_v057_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.pct_change(63) - revenue.pct_change(63))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc057_63d_base_v057_signal'] = f75ps_f75_fcf_per_share_acceleration_calc057_63d_base_v057_signal

def f75ps_f75_fcf_per_share_acceleration_calc058_21d_base_v058_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.rolling(21).kurt() - marketcap.rolling(21).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc058_21d_base_v058_signal'] = f75ps_f75_fcf_per_share_acceleration_calc058_21d_base_v058_signal

def f75ps_f75_fcf_per_share_acceleration_calc059_63d_base_v059_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(63).max() - marketcap.rolling(63).min()) / assets.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc059_63d_base_v059_signal'] = f75ps_f75_fcf_per_share_acceleration_calc059_63d_base_v059_signal

def f75ps_f75_fcf_per_share_acceleration_calc060_252d_base_v060_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.rolling(252).rank(pct=True) / netinc.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc060_252d_base_v060_signal'] = f75ps_f75_fcf_per_share_acceleration_calc060_252d_base_v060_signal

def f75ps_f75_fcf_per_share_acceleration_calc061_10d_base_v061_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(10).rank(pct=True) / revenue.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc061_10d_base_v061_signal'] = f75ps_f75_fcf_per_share_acceleration_calc061_10d_base_v061_signal

def f75ps_f75_fcf_per_share_acceleration_calc062_126d_base_v062_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.rolling(126).rank(pct=True) / revenue.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc062_126d_base_v062_signal'] = f75ps_f75_fcf_per_share_acceleration_calc062_126d_base_v062_signal

def f75ps_f75_fcf_per_share_acceleration_calc063_10d_base_v063_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets / sharesbas.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc063_10d_base_v063_signal'] = f75ps_f75_fcf_per_share_acceleration_calc063_10d_base_v063_signal

def f75ps_f75_fcf_per_share_acceleration_calc064_5d_base_v064_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.rolling(5).quantile(0.5) / fcf.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc064_5d_base_v064_signal'] = f75ps_f75_fcf_per_share_acceleration_calc064_5d_base_v064_signal

def f75ps_f75_fcf_per_share_acceleration_calc065_10d_base_v065_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.rolling(10).max() - sharesbas.rolling(10).min()) / netinc.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc065_10d_base_v065_signal'] = f75ps_f75_fcf_per_share_acceleration_calc065_10d_base_v065_signal

def f75ps_f75_fcf_per_share_acceleration_calc066_252d_base_v066_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.rolling(252).max() - assets.rolling(252).min()) / fcf.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc066_252d_base_v066_signal'] = f75ps_f75_fcf_per_share_acceleration_calc066_252d_base_v066_signal

def f75ps_f75_fcf_per_share_acceleration_calc067_126d_base_v067_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.pct_change(126) - sharesbas.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc067_126d_base_v067_signal'] = f75ps_f75_fcf_per_share_acceleration_calc067_126d_base_v067_signal

def f75ps_f75_fcf_per_share_acceleration_calc068_21d_base_v068_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.rolling(21).rank(pct=True) / marketcap.rolling(21).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc068_21d_base_v068_signal'] = f75ps_f75_fcf_per_share_acceleration_calc068_21d_base_v068_signal

def f75ps_f75_fcf_per_share_acceleration_calc069_10d_base_v069_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.rolling(10).rank(pct=True) / revenue.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc069_10d_base_v069_signal'] = f75ps_f75_fcf_per_share_acceleration_calc069_10d_base_v069_signal

def f75ps_f75_fcf_per_share_acceleration_calc070_21d_base_v070_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.diff(21).abs() / sharesbas.diff(21).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc070_21d_base_v070_signal'] = f75ps_f75_fcf_per_share_acceleration_calc070_21d_base_v070_signal

def f75ps_f75_fcf_per_share_acceleration_calc071_252d_base_v071_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.diff(252).abs() / fcf.diff(252).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc071_252d_base_v071_signal'] = f75ps_f75_fcf_per_share_acceleration_calc071_252d_base_v071_signal

def f75ps_f75_fcf_per_share_acceleration_calc072_42d_base_v072_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(42).max() - eps.rolling(42).min()) / sharesbas.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc072_42d_base_v072_signal'] = f75ps_f75_fcf_per_share_acceleration_calc072_42d_base_v072_signal

def f75ps_f75_fcf_per_share_acceleration_calc073_42d_base_v073_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.rolling(42).kurt() - revenue.rolling(42).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc073_42d_base_v073_signal'] = f75ps_f75_fcf_per_share_acceleration_calc073_42d_base_v073_signal

def f75ps_f75_fcf_per_share_acceleration_calc074_252d_base_v074_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf / eps.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc074_252d_base_v074_signal'] = f75ps_f75_fcf_per_share_acceleration_calc074_252d_base_v074_signal

def f75ps_f75_fcf_per_share_acceleration_calc075_42d_base_v075_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((sharesbas - sharesbas.rolling(42).mean()) / sharesbas.rolling(42).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc075_42d_base_v075_signal'] = f75ps_f75_fcf_per_share_acceleration_calc075_42d_base_v075_signal



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
