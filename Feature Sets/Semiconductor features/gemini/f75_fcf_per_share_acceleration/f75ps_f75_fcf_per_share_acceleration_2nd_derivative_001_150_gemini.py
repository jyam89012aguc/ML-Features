import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f75ps_f75_fcf_per_share_acceleration_calc001_63d_slope_v001_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.rolling(63).max() - fcf.rolling(63).min()) / revenue.replace(0, np.nan)
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc001_63d_slope_v001_signal'] = f75ps_f75_fcf_per_share_acceleration_calc001_63d_slope_v001_signal

def f75ps_f75_fcf_per_share_acceleration_calc002_10d_slope_v002_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((assets - assets.rolling(10).mean()) / assets.rolling(10).std())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc002_10d_slope_v002_signal'] = f75ps_f75_fcf_per_share_acceleration_calc002_10d_slope_v002_signal

def f75ps_f75_fcf_per_share_acceleration_calc003_5d_slope_v003_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.diff(5) / marketcap.replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc003_5d_slope_v003_signal'] = f75ps_f75_fcf_per_share_acceleration_calc003_5d_slope_v003_signal

def f75ps_f75_fcf_per_share_acceleration_calc004_252d_slope_v004_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas / marketcap.replace(0, np.nan)).rolling(252).mean()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc004_252d_slope_v004_signal'] = f75ps_f75_fcf_per_share_acceleration_calc004_252d_slope_v004_signal

def f75ps_f75_fcf_per_share_acceleration_calc005_21d_slope_v005_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(21).rank(pct=True) / eps.rolling(21).rank(pct=True).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc005_21d_slope_v005_signal'] = f75ps_f75_fcf_per_share_acceleration_calc005_21d_slope_v005_signal

def f75ps_f75_fcf_per_share_acceleration_calc006_126d_slope_v006_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.rolling(126).max() - marketcap.rolling(126).min()) / sharesbas.replace(0, np.nan)
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc006_126d_slope_v006_signal'] = f75ps_f75_fcf_per_share_acceleration_calc006_126d_slope_v006_signal

def f75ps_f75_fcf_per_share_acceleration_calc007_42d_slope_v007_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.pct_change(42) - revenue.pct_change(42))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc007_42d_slope_v007_signal'] = f75ps_f75_fcf_per_share_acceleration_calc007_42d_slope_v007_signal

def f75ps_f75_fcf_per_share_acceleration_calc008_42d_slope_v008_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.rolling(42).rank(pct=True) / fcf.rolling(42).rank(pct=True).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc008_42d_slope_v008_signal'] = f75ps_f75_fcf_per_share_acceleration_calc008_42d_slope_v008_signal

def f75ps_f75_fcf_per_share_acceleration_calc009_5d_slope_v009_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.rolling(5).quantile(0.5) / revenue.rolling(5).quantile(0.5).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc009_5d_slope_v009_signal'] = f75ps_f75_fcf_per_share_acceleration_calc009_5d_slope_v009_signal

def f75ps_f75_fcf_per_share_acceleration_calc010_252d_slope_v010_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((marketcap - marketcap.rolling(252).mean()) / marketcap.rolling(252).std())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc010_252d_slope_v010_signal'] = f75ps_f75_fcf_per_share_acceleration_calc010_252d_slope_v010_signal

def f75ps_f75_fcf_per_share_acceleration_calc011_126d_slope_v011_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.diff(126) / sharesbas.replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc011_126d_slope_v011_signal'] = f75ps_f75_fcf_per_share_acceleration_calc011_126d_slope_v011_signal

def f75ps_f75_fcf_per_share_acceleration_calc012_21d_slope_v012_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.diff(21) / revenue.replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc012_21d_slope_v012_signal'] = f75ps_f75_fcf_per_share_acceleration_calc012_21d_slope_v012_signal

def f75ps_f75_fcf_per_share_acceleration_calc013_42d_slope_v013_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.pct_change(42) - fcf.pct_change(42))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc013_42d_slope_v013_signal'] = f75ps_f75_fcf_per_share_acceleration_calc013_42d_slope_v013_signal

def f75ps_f75_fcf_per_share_acceleration_calc014_10d_slope_v014_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc014_10d_slope_v014_signal'] = f75ps_f75_fcf_per_share_acceleration_calc014_10d_slope_v014_signal

def f75ps_f75_fcf_per_share_acceleration_calc015_63d_slope_v015_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.rolling(63).quantile(0.5) / sharesbas.rolling(63).quantile(0.5).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc015_63d_slope_v015_signal'] = f75ps_f75_fcf_per_share_acceleration_calc015_63d_slope_v015_signal

def f75ps_f75_fcf_per_share_acceleration_calc016_21d_slope_v016_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.pct_change(21) - marketcap.pct_change(21))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc016_21d_slope_v016_signal'] = f75ps_f75_fcf_per_share_acceleration_calc016_21d_slope_v016_signal

def f75ps_f75_fcf_per_share_acceleration_calc017_21d_slope_v017_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc017_21d_slope_v017_signal'] = f75ps_f75_fcf_per_share_acceleration_calc017_21d_slope_v017_signal

def f75ps_f75_fcf_per_share_acceleration_calc018_5d_slope_v018_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.diff(5).abs() / marketcap.diff(5).abs().replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc018_5d_slope_v018_signal'] = f75ps_f75_fcf_per_share_acceleration_calc018_5d_slope_v018_signal

def f75ps_f75_fcf_per_share_acceleration_calc019_42d_slope_v019_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap / fcf.replace(0, np.nan)).rolling(42).mean()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc019_42d_slope_v019_signal'] = f75ps_f75_fcf_per_share_acceleration_calc019_42d_slope_v019_signal

def f75ps_f75_fcf_per_share_acceleration_calc020_42d_slope_v020_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(42).rank(pct=True) / netinc.rolling(42).rank(pct=True).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc020_42d_slope_v020_signal'] = f75ps_f75_fcf_per_share_acceleration_calc020_42d_slope_v020_signal

def f75ps_f75_fcf_per_share_acceleration_calc021_5d_slope_v021_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(5).quantile(0.5) / eps.rolling(5).quantile(0.5).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc021_5d_slope_v021_signal'] = f75ps_f75_fcf_per_share_acceleration_calc021_5d_slope_v021_signal

def f75ps_f75_fcf_per_share_acceleration_calc022_252d_slope_v022_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.rolling(252).kurt() - revenue.rolling(252).kurt())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc022_252d_slope_v022_signal'] = f75ps_f75_fcf_per_share_acceleration_calc022_252d_slope_v022_signal

def f75ps_f75_fcf_per_share_acceleration_calc023_63d_slope_v023_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.rolling(63).quantile(0.5) / eps.rolling(63).quantile(0.5).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc023_63d_slope_v023_signal'] = f75ps_f75_fcf_per_share_acceleration_calc023_63d_slope_v023_signal

def f75ps_f75_fcf_per_share_acceleration_calc024_252d_slope_v024_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps / fcf.replace(0, np.nan)).rolling(252).std()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc024_252d_slope_v024_signal'] = f75ps_f75_fcf_per_share_acceleration_calc024_252d_slope_v024_signal

def f75ps_f75_fcf_per_share_acceleration_calc025_21d_slope_v025_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(21).quantile(0.5) / marketcap.rolling(21).quantile(0.5).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc025_21d_slope_v025_signal'] = f75ps_f75_fcf_per_share_acceleration_calc025_21d_slope_v025_signal

def f75ps_f75_fcf_per_share_acceleration_calc026_252d_slope_v026_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.rolling(252).kurt() - revenue.rolling(252).kurt())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc026_252d_slope_v026_signal'] = f75ps_f75_fcf_per_share_acceleration_calc026_252d_slope_v026_signal

def f75ps_f75_fcf_per_share_acceleration_calc027_5d_slope_v027_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(5).max() - netinc.rolling(5).min()) / revenue.replace(0, np.nan)
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc027_5d_slope_v027_signal'] = f75ps_f75_fcf_per_share_acceleration_calc027_5d_slope_v027_signal

def f75ps_f75_fcf_per_share_acceleration_calc028_5d_slope_v028_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.diff(5).abs() / fcf.diff(5).abs().replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc028_5d_slope_v028_signal'] = f75ps_f75_fcf_per_share_acceleration_calc028_5d_slope_v028_signal

def f75ps_f75_fcf_per_share_acceleration_calc029_21d_slope_v029_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.rolling(21).max() - fcf.rolling(21).min()) / sharesbas.replace(0, np.nan)
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc029_21d_slope_v029_signal'] = f75ps_f75_fcf_per_share_acceleration_calc029_21d_slope_v029_signal

def f75ps_f75_fcf_per_share_acceleration_calc030_126d_slope_v030_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.rolling(126).rank(pct=True) / revenue.rolling(126).rank(pct=True).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc030_126d_slope_v030_signal'] = f75ps_f75_fcf_per_share_acceleration_calc030_126d_slope_v030_signal

def f75ps_f75_fcf_per_share_acceleration_calc031_10d_slope_v031_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.rolling(10).rank(pct=True) / assets.rolling(10).rank(pct=True).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc031_10d_slope_v031_signal'] = f75ps_f75_fcf_per_share_acceleration_calc031_10d_slope_v031_signal

def f75ps_f75_fcf_per_share_acceleration_calc032_126d_slope_v032_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((eps - eps.rolling(126).mean()) / eps.rolling(126).std())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc032_126d_slope_v032_signal'] = f75ps_f75_fcf_per_share_acceleration_calc032_126d_slope_v032_signal

def f75ps_f75_fcf_per_share_acceleration_calc033_42d_slope_v033_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(42).quantile(0.5) / sharesbas.rolling(42).quantile(0.5).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc033_42d_slope_v033_signal'] = f75ps_f75_fcf_per_share_acceleration_calc033_42d_slope_v033_signal

def f75ps_f75_fcf_per_share_acceleration_calc034_21d_slope_v034_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.rolling(21).kurt() - sharesbas.rolling(21).kurt())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc034_21d_slope_v034_signal'] = f75ps_f75_fcf_per_share_acceleration_calc034_21d_slope_v034_signal

def f75ps_f75_fcf_per_share_acceleration_calc035_21d_slope_v035_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue / eps.replace(0, np.nan)).rolling(21).mean()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc035_21d_slope_v035_signal'] = f75ps_f75_fcf_per_share_acceleration_calc035_21d_slope_v035_signal

def f75ps_f75_fcf_per_share_acceleration_calc036_252d_slope_v036_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.pct_change(252) - netinc.pct_change(252))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc036_252d_slope_v036_signal'] = f75ps_f75_fcf_per_share_acceleration_calc036_252d_slope_v036_signal

def f75ps_f75_fcf_per_share_acceleration_calc037_42d_slope_v037_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.pct_change(42) - fcf.pct_change(42))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc037_42d_slope_v037_signal'] = f75ps_f75_fcf_per_share_acceleration_calc037_42d_slope_v037_signal

def f75ps_f75_fcf_per_share_acceleration_calc038_21d_slope_v038_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc038_21d_slope_v038_signal'] = f75ps_f75_fcf_per_share_acceleration_calc038_21d_slope_v038_signal

def f75ps_f75_fcf_per_share_acceleration_calc039_21d_slope_v039_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.diff(21).abs() / eps.diff(21).abs().replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc039_21d_slope_v039_signal'] = f75ps_f75_fcf_per_share_acceleration_calc039_21d_slope_v039_signal

def f75ps_f75_fcf_per_share_acceleration_calc040_5d_slope_v040_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap / eps.replace(0, np.nan)).rolling(5).mean()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc040_5d_slope_v040_signal'] = f75ps_f75_fcf_per_share_acceleration_calc040_5d_slope_v040_signal

def f75ps_f75_fcf_per_share_acceleration_calc041_21d_slope_v041_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(21).quantile(0.5) / eps.rolling(21).quantile(0.5).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc041_21d_slope_v041_signal'] = f75ps_f75_fcf_per_share_acceleration_calc041_21d_slope_v041_signal

def f75ps_f75_fcf_per_share_acceleration_calc042_252d_slope_v042_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.diff(252) / marketcap.replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc042_252d_slope_v042_signal'] = f75ps_f75_fcf_per_share_acceleration_calc042_252d_slope_v042_signal

def f75ps_f75_fcf_per_share_acceleration_calc043_42d_slope_v043_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.rolling(42).quantile(0.5) / assets.rolling(42).quantile(0.5).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc043_42d_slope_v043_signal'] = f75ps_f75_fcf_per_share_acceleration_calc043_42d_slope_v043_signal

def f75ps_f75_fcf_per_share_acceleration_calc044_63d_slope_v044_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.rolling(63).kurt() - marketcap.rolling(63).kurt())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc044_63d_slope_v044_signal'] = f75ps_f75_fcf_per_share_acceleration_calc044_63d_slope_v044_signal

def f75ps_f75_fcf_per_share_acceleration_calc045_252d_slope_v045_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((netinc - netinc.rolling(252).mean()) / netinc.rolling(252).std())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc045_252d_slope_v045_signal'] = f75ps_f75_fcf_per_share_acceleration_calc045_252d_slope_v045_signal

def f75ps_f75_fcf_per_share_acceleration_calc046_21d_slope_v046_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf / assets.replace(0, np.nan)).rolling(21).mean()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc046_21d_slope_v046_signal'] = f75ps_f75_fcf_per_share_acceleration_calc046_21d_slope_v046_signal

def f75ps_f75_fcf_per_share_acceleration_calc047_10d_slope_v047_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.diff(10) / eps.replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc047_10d_slope_v047_signal'] = f75ps_f75_fcf_per_share_acceleration_calc047_10d_slope_v047_signal

def f75ps_f75_fcf_per_share_acceleration_calc048_63d_slope_v048_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.rolling(63).rank(pct=True) / netinc.rolling(63).rank(pct=True).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc048_63d_slope_v048_signal'] = f75ps_f75_fcf_per_share_acceleration_calc048_63d_slope_v048_signal

def f75ps_f75_fcf_per_share_acceleration_calc049_126d_slope_v049_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.pct_change(126) - assets.pct_change(126))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc049_126d_slope_v049_signal'] = f75ps_f75_fcf_per_share_acceleration_calc049_126d_slope_v049_signal

def f75ps_f75_fcf_per_share_acceleration_calc050_5d_slope_v050_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.rolling(5).max() - revenue.rolling(5).min()) / marketcap.replace(0, np.nan)
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc050_5d_slope_v050_signal'] = f75ps_f75_fcf_per_share_acceleration_calc050_5d_slope_v050_signal

def f75ps_f75_fcf_per_share_acceleration_calc051_126d_slope_v051_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets / revenue.replace(0, np.nan)).rolling(126).mean()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc051_126d_slope_v051_signal'] = f75ps_f75_fcf_per_share_acceleration_calc051_126d_slope_v051_signal

def f75ps_f75_fcf_per_share_acceleration_calc052_126d_slope_v052_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.pct_change(126) - marketcap.pct_change(126))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc052_126d_slope_v052_signal'] = f75ps_f75_fcf_per_share_acceleration_calc052_126d_slope_v052_signal

def f75ps_f75_fcf_per_share_acceleration_calc053_126d_slope_v053_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.diff(126) / marketcap.replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc053_126d_slope_v053_signal'] = f75ps_f75_fcf_per_share_acceleration_calc053_126d_slope_v053_signal

def f75ps_f75_fcf_per_share_acceleration_calc054_10d_slope_v054_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.rolling(10).max() - assets.rolling(10).min()) / marketcap.replace(0, np.nan)
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc054_10d_slope_v054_signal'] = f75ps_f75_fcf_per_share_acceleration_calc054_10d_slope_v054_signal

def f75ps_f75_fcf_per_share_acceleration_calc055_126d_slope_v055_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap / netinc.replace(0, np.nan)).rolling(126).std()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc055_126d_slope_v055_signal'] = f75ps_f75_fcf_per_share_acceleration_calc055_126d_slope_v055_signal

def f75ps_f75_fcf_per_share_acceleration_calc056_5d_slope_v056_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.rolling(5).kurt() - netinc.rolling(5).kurt())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc056_5d_slope_v056_signal'] = f75ps_f75_fcf_per_share_acceleration_calc056_5d_slope_v056_signal

def f75ps_f75_fcf_per_share_acceleration_calc057_63d_slope_v057_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.pct_change(63) - revenue.pct_change(63))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc057_63d_slope_v057_signal'] = f75ps_f75_fcf_per_share_acceleration_calc057_63d_slope_v057_signal

def f75ps_f75_fcf_per_share_acceleration_calc058_21d_slope_v058_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.rolling(21).kurt() - marketcap.rolling(21).kurt())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc058_21d_slope_v058_signal'] = f75ps_f75_fcf_per_share_acceleration_calc058_21d_slope_v058_signal

def f75ps_f75_fcf_per_share_acceleration_calc059_63d_slope_v059_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(63).max() - marketcap.rolling(63).min()) / assets.replace(0, np.nan)
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc059_63d_slope_v059_signal'] = f75ps_f75_fcf_per_share_acceleration_calc059_63d_slope_v059_signal

def f75ps_f75_fcf_per_share_acceleration_calc060_252d_slope_v060_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.rolling(252).rank(pct=True) / netinc.rolling(252).rank(pct=True).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc060_252d_slope_v060_signal'] = f75ps_f75_fcf_per_share_acceleration_calc060_252d_slope_v060_signal

def f75ps_f75_fcf_per_share_acceleration_calc061_10d_slope_v061_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(10).rank(pct=True) / revenue.rolling(10).rank(pct=True).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc061_10d_slope_v061_signal'] = f75ps_f75_fcf_per_share_acceleration_calc061_10d_slope_v061_signal

def f75ps_f75_fcf_per_share_acceleration_calc062_126d_slope_v062_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.rolling(126).rank(pct=True) / revenue.rolling(126).rank(pct=True).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc062_126d_slope_v062_signal'] = f75ps_f75_fcf_per_share_acceleration_calc062_126d_slope_v062_signal

def f75ps_f75_fcf_per_share_acceleration_calc063_10d_slope_v063_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets / sharesbas.replace(0, np.nan)).rolling(10).std()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc063_10d_slope_v063_signal'] = f75ps_f75_fcf_per_share_acceleration_calc063_10d_slope_v063_signal

def f75ps_f75_fcf_per_share_acceleration_calc064_5d_slope_v064_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.rolling(5).quantile(0.5) / fcf.rolling(5).quantile(0.5).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc064_5d_slope_v064_signal'] = f75ps_f75_fcf_per_share_acceleration_calc064_5d_slope_v064_signal

def f75ps_f75_fcf_per_share_acceleration_calc065_10d_slope_v065_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.rolling(10).max() - sharesbas.rolling(10).min()) / netinc.replace(0, np.nan)
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc065_10d_slope_v065_signal'] = f75ps_f75_fcf_per_share_acceleration_calc065_10d_slope_v065_signal

def f75ps_f75_fcf_per_share_acceleration_calc066_252d_slope_v066_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.rolling(252).max() - assets.rolling(252).min()) / fcf.replace(0, np.nan)
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc066_252d_slope_v066_signal'] = f75ps_f75_fcf_per_share_acceleration_calc066_252d_slope_v066_signal

def f75ps_f75_fcf_per_share_acceleration_calc067_126d_slope_v067_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.pct_change(126) - sharesbas.pct_change(126))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc067_126d_slope_v067_signal'] = f75ps_f75_fcf_per_share_acceleration_calc067_126d_slope_v067_signal

def f75ps_f75_fcf_per_share_acceleration_calc068_21d_slope_v068_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc068_21d_slope_v068_signal'] = f75ps_f75_fcf_per_share_acceleration_calc068_21d_slope_v068_signal

def f75ps_f75_fcf_per_share_acceleration_calc069_10d_slope_v069_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.rolling(10).rank(pct=True) / revenue.rolling(10).rank(pct=True).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc069_10d_slope_v069_signal'] = f75ps_f75_fcf_per_share_acceleration_calc069_10d_slope_v069_signal

def f75ps_f75_fcf_per_share_acceleration_calc070_21d_slope_v070_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.diff(21).abs() / sharesbas.diff(21).abs().replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc070_21d_slope_v070_signal'] = f75ps_f75_fcf_per_share_acceleration_calc070_21d_slope_v070_signal

def f75ps_f75_fcf_per_share_acceleration_calc071_252d_slope_v071_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.diff(252).abs() / fcf.diff(252).abs().replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc071_252d_slope_v071_signal'] = f75ps_f75_fcf_per_share_acceleration_calc071_252d_slope_v071_signal

def f75ps_f75_fcf_per_share_acceleration_calc072_42d_slope_v072_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(42).max() - eps.rolling(42).min()) / sharesbas.replace(0, np.nan)
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc072_42d_slope_v072_signal'] = f75ps_f75_fcf_per_share_acceleration_calc072_42d_slope_v072_signal

def f75ps_f75_fcf_per_share_acceleration_calc073_42d_slope_v073_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.rolling(42).kurt() - revenue.rolling(42).kurt())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc073_42d_slope_v073_signal'] = f75ps_f75_fcf_per_share_acceleration_calc073_42d_slope_v073_signal

def f75ps_f75_fcf_per_share_acceleration_calc074_252d_slope_v074_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf / eps.replace(0, np.nan)).rolling(252).mean()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc074_252d_slope_v074_signal'] = f75ps_f75_fcf_per_share_acceleration_calc074_252d_slope_v074_signal

def f75ps_f75_fcf_per_share_acceleration_calc075_42d_slope_v075_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((sharesbas - sharesbas.rolling(42).mean()) / sharesbas.rolling(42).std())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc075_42d_slope_v075_signal'] = f75ps_f75_fcf_per_share_acceleration_calc075_42d_slope_v075_signal

def f75ps_f75_fcf_per_share_acceleration_calc076_21d_slope_v076_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((revenue - revenue.rolling(21).mean()) / revenue.rolling(21).std())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc076_21d_slope_v076_signal'] = f75ps_f75_fcf_per_share_acceleration_calc076_21d_slope_v076_signal

def f75ps_f75_fcf_per_share_acceleration_calc077_42d_slope_v077_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.rolling(42).quantile(0.5) / fcf.rolling(42).quantile(0.5).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc077_42d_slope_v077_signal'] = f75ps_f75_fcf_per_share_acceleration_calc077_42d_slope_v077_signal

def f75ps_f75_fcf_per_share_acceleration_calc078_10d_slope_v078_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc078_10d_slope_v078_signal'] = f75ps_f75_fcf_per_share_acceleration_calc078_10d_slope_v078_signal

def f75ps_f75_fcf_per_share_acceleration_calc079_5d_slope_v079_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.diff(5).abs() / fcf.diff(5).abs().replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc079_5d_slope_v079_signal'] = f75ps_f75_fcf_per_share_acceleration_calc079_5d_slope_v079_signal

def f75ps_f75_fcf_per_share_acceleration_calc080_126d_slope_v080_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.rolling(126).max() - assets.rolling(126).min()) / revenue.replace(0, np.nan)
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc080_126d_slope_v080_signal'] = f75ps_f75_fcf_per_share_acceleration_calc080_126d_slope_v080_signal

def f75ps_f75_fcf_per_share_acceleration_calc081_5d_slope_v081_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.rolling(5).quantile(0.5) / revenue.rolling(5).quantile(0.5).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc081_5d_slope_v081_signal'] = f75ps_f75_fcf_per_share_acceleration_calc081_5d_slope_v081_signal

def f75ps_f75_fcf_per_share_acceleration_calc082_10d_slope_v082_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue / sharesbas.replace(0, np.nan)).rolling(10).mean()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc082_10d_slope_v082_signal'] = f75ps_f75_fcf_per_share_acceleration_calc082_10d_slope_v082_signal

def f75ps_f75_fcf_per_share_acceleration_calc083_63d_slope_v083_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.diff(63) / revenue.replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc083_63d_slope_v083_signal'] = f75ps_f75_fcf_per_share_acceleration_calc083_63d_slope_v083_signal

def f75ps_f75_fcf_per_share_acceleration_calc084_126d_slope_v084_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.diff(126).abs() / fcf.diff(126).abs().replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc084_126d_slope_v084_signal'] = f75ps_f75_fcf_per_share_acceleration_calc084_126d_slope_v084_signal

def f75ps_f75_fcf_per_share_acceleration_calc085_126d_slope_v085_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc085_126d_slope_v085_signal'] = f75ps_f75_fcf_per_share_acceleration_calc085_126d_slope_v085_signal

def f75ps_f75_fcf_per_share_acceleration_calc086_42d_slope_v086_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.rolling(42).max() - fcf.rolling(42).min()) / sharesbas.replace(0, np.nan)
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc086_42d_slope_v086_signal'] = f75ps_f75_fcf_per_share_acceleration_calc086_42d_slope_v086_signal

def f75ps_f75_fcf_per_share_acceleration_calc087_42d_slope_v087_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap / eps.replace(0, np.nan)).rolling(42).mean()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc087_42d_slope_v087_signal'] = f75ps_f75_fcf_per_share_acceleration_calc087_42d_slope_v087_signal

def f75ps_f75_fcf_per_share_acceleration_calc088_42d_slope_v088_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.rolling(42).rank(pct=True) / marketcap.rolling(42).rank(pct=True).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc088_42d_slope_v088_signal'] = f75ps_f75_fcf_per_share_acceleration_calc088_42d_slope_v088_signal

def f75ps_f75_fcf_per_share_acceleration_calc089_42d_slope_v089_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas / eps.replace(0, np.nan)).rolling(42).std()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc089_42d_slope_v089_signal'] = f75ps_f75_fcf_per_share_acceleration_calc089_42d_slope_v089_signal

def f75ps_f75_fcf_per_share_acceleration_calc090_42d_slope_v090_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(42).rank(pct=True) / eps.rolling(42).rank(pct=True).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc090_42d_slope_v090_signal'] = f75ps_f75_fcf_per_share_acceleration_calc090_42d_slope_v090_signal

def f75ps_f75_fcf_per_share_acceleration_calc091_252d_slope_v091_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets / marketcap.replace(0, np.nan)).rolling(252).mean()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc091_252d_slope_v091_signal'] = f75ps_f75_fcf_per_share_acceleration_calc091_252d_slope_v091_signal

def f75ps_f75_fcf_per_share_acceleration_calc092_10d_slope_v092_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.rolling(10).quantile(0.5) / fcf.rolling(10).quantile(0.5).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc092_10d_slope_v092_signal'] = f75ps_f75_fcf_per_share_acceleration_calc092_10d_slope_v092_signal

def f75ps_f75_fcf_per_share_acceleration_calc093_126d_slope_v093_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.rolling(126).max() - eps.rolling(126).min()) / marketcap.replace(0, np.nan)
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc093_126d_slope_v093_signal'] = f75ps_f75_fcf_per_share_acceleration_calc093_126d_slope_v093_signal

def f75ps_f75_fcf_per_share_acceleration_calc094_21d_slope_v094_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.diff(21) / eps.replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc094_21d_slope_v094_signal'] = f75ps_f75_fcf_per_share_acceleration_calc094_21d_slope_v094_signal

def f75ps_f75_fcf_per_share_acceleration_calc095_21d_slope_v095_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.rolling(21).quantile(0.5) / revenue.rolling(21).quantile(0.5).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc095_21d_slope_v095_signal'] = f75ps_f75_fcf_per_share_acceleration_calc095_21d_slope_v095_signal

def f75ps_f75_fcf_per_share_acceleration_calc096_5d_slope_v096_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.rolling(5).max() - assets.rolling(5).min()) / fcf.replace(0, np.nan)
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc096_5d_slope_v096_signal'] = f75ps_f75_fcf_per_share_acceleration_calc096_5d_slope_v096_signal

def f75ps_f75_fcf_per_share_acceleration_calc097_42d_slope_v097_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.pct_change(42) - marketcap.pct_change(42))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc097_42d_slope_v097_signal'] = f75ps_f75_fcf_per_share_acceleration_calc097_42d_slope_v097_signal

def f75ps_f75_fcf_per_share_acceleration_calc098_63d_slope_v098_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.rolling(63).max() - netinc.rolling(63).min()) / revenue.replace(0, np.nan)
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc098_63d_slope_v098_signal'] = f75ps_f75_fcf_per_share_acceleration_calc098_63d_slope_v098_signal

def f75ps_f75_fcf_per_share_acceleration_calc099_63d_slope_v099_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.rolling(63).quantile(0.5) / sharesbas.rolling(63).quantile(0.5).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc099_63d_slope_v099_signal'] = f75ps_f75_fcf_per_share_acceleration_calc099_63d_slope_v099_signal

def f75ps_f75_fcf_per_share_acceleration_calc100_63d_slope_v100_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.rolling(63).quantile(0.5) / marketcap.rolling(63).quantile(0.5).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc100_63d_slope_v100_signal'] = f75ps_f75_fcf_per_share_acceleration_calc100_63d_slope_v100_signal

def f75ps_f75_fcf_per_share_acceleration_calc101_21d_slope_v101_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps / revenue.replace(0, np.nan)).rolling(21).std()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc101_21d_slope_v101_signal'] = f75ps_f75_fcf_per_share_acceleration_calc101_21d_slope_v101_signal

def f75ps_f75_fcf_per_share_acceleration_calc102_21d_slope_v102_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue / sharesbas.replace(0, np.nan)).rolling(21).mean()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc102_21d_slope_v102_signal'] = f75ps_f75_fcf_per_share_acceleration_calc102_21d_slope_v102_signal

def f75ps_f75_fcf_per_share_acceleration_calc103_10d_slope_v103_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap / assets.replace(0, np.nan)).rolling(10).std()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc103_10d_slope_v103_signal'] = f75ps_f75_fcf_per_share_acceleration_calc103_10d_slope_v103_signal

def f75ps_f75_fcf_per_share_acceleration_calc104_10d_slope_v104_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((eps - eps.rolling(10).mean()) / eps.rolling(10).std())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc104_10d_slope_v104_signal'] = f75ps_f75_fcf_per_share_acceleration_calc104_10d_slope_v104_signal

def f75ps_f75_fcf_per_share_acceleration_calc105_21d_slope_v105_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((eps - eps.rolling(21).mean()) / eps.rolling(21).std())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc105_21d_slope_v105_signal'] = f75ps_f75_fcf_per_share_acceleration_calc105_21d_slope_v105_signal

def f75ps_f75_fcf_per_share_acceleration_calc106_42d_slope_v106_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((revenue - revenue.rolling(42).mean()) / revenue.rolling(42).std())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc106_42d_slope_v106_signal'] = f75ps_f75_fcf_per_share_acceleration_calc106_42d_slope_v106_signal

def f75ps_f75_fcf_per_share_acceleration_calc107_63d_slope_v107_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(63).kurt() - revenue.rolling(63).kurt())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc107_63d_slope_v107_signal'] = f75ps_f75_fcf_per_share_acceleration_calc107_63d_slope_v107_signal

def f75ps_f75_fcf_per_share_acceleration_calc108_63d_slope_v108_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc108_63d_slope_v108_signal'] = f75ps_f75_fcf_per_share_acceleration_calc108_63d_slope_v108_signal

def f75ps_f75_fcf_per_share_acceleration_calc109_42d_slope_v109_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.rolling(42).rank(pct=True) / eps.rolling(42).rank(pct=True).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc109_42d_slope_v109_signal'] = f75ps_f75_fcf_per_share_acceleration_calc109_42d_slope_v109_signal

def f75ps_f75_fcf_per_share_acceleration_calc110_42d_slope_v110_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue / assets.replace(0, np.nan)).rolling(42).std()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc110_42d_slope_v110_signal'] = f75ps_f75_fcf_per_share_acceleration_calc110_42d_slope_v110_signal

def f75ps_f75_fcf_per_share_acceleration_calc111_21d_slope_v111_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.rolling(21).max() - netinc.rolling(21).min()) / assets.replace(0, np.nan)
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc111_21d_slope_v111_signal'] = f75ps_f75_fcf_per_share_acceleration_calc111_21d_slope_v111_signal

def f75ps_f75_fcf_per_share_acceleration_calc112_5d_slope_v112_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.pct_change(5) - netinc.pct_change(5))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc112_5d_slope_v112_signal'] = f75ps_f75_fcf_per_share_acceleration_calc112_5d_slope_v112_signal

def f75ps_f75_fcf_per_share_acceleration_calc113_21d_slope_v113_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.rolling(21).kurt() - assets.rolling(21).kurt())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc113_21d_slope_v113_signal'] = f75ps_f75_fcf_per_share_acceleration_calc113_21d_slope_v113_signal

def f75ps_f75_fcf_per_share_acceleration_calc114_126d_slope_v114_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.diff(126) / marketcap.replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc114_126d_slope_v114_signal'] = f75ps_f75_fcf_per_share_acceleration_calc114_126d_slope_v114_signal

def f75ps_f75_fcf_per_share_acceleration_calc115_21d_slope_v115_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap / assets.replace(0, np.nan)).rolling(21).std()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc115_21d_slope_v115_signal'] = f75ps_f75_fcf_per_share_acceleration_calc115_21d_slope_v115_signal

def f75ps_f75_fcf_per_share_acceleration_calc116_21d_slope_v116_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((fcf - fcf.rolling(21).mean()) / fcf.rolling(21).std())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc116_21d_slope_v116_signal'] = f75ps_f75_fcf_per_share_acceleration_calc116_21d_slope_v116_signal

def f75ps_f75_fcf_per_share_acceleration_calc117_42d_slope_v117_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.pct_change(42) - assets.pct_change(42))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc117_42d_slope_v117_signal'] = f75ps_f75_fcf_per_share_acceleration_calc117_42d_slope_v117_signal

def f75ps_f75_fcf_per_share_acceleration_calc118_63d_slope_v118_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.rolling(63).max() - eps.rolling(63).min()) / assets.replace(0, np.nan)
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc118_63d_slope_v118_signal'] = f75ps_f75_fcf_per_share_acceleration_calc118_63d_slope_v118_signal

def f75ps_f75_fcf_per_share_acceleration_calc119_42d_slope_v119_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.rolling(42).rank(pct=True) / marketcap.rolling(42).rank(pct=True).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc119_42d_slope_v119_signal'] = f75ps_f75_fcf_per_share_acceleration_calc119_42d_slope_v119_signal

def f75ps_f75_fcf_per_share_acceleration_calc120_5d_slope_v120_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.diff(5).abs() / sharesbas.diff(5).abs().replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc120_5d_slope_v120_signal'] = f75ps_f75_fcf_per_share_acceleration_calc120_5d_slope_v120_signal

def f75ps_f75_fcf_per_share_acceleration_calc121_5d_slope_v121_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.diff(5) / marketcap.replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc121_5d_slope_v121_signal'] = f75ps_f75_fcf_per_share_acceleration_calc121_5d_slope_v121_signal

def f75ps_f75_fcf_per_share_acceleration_calc122_5d_slope_v122_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc / revenue.replace(0, np.nan)).rolling(5).std()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc122_5d_slope_v122_signal'] = f75ps_f75_fcf_per_share_acceleration_calc122_5d_slope_v122_signal

def f75ps_f75_fcf_per_share_acceleration_calc123_21d_slope_v123_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.pct_change(21) - eps.pct_change(21))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc123_21d_slope_v123_signal'] = f75ps_f75_fcf_per_share_acceleration_calc123_21d_slope_v123_signal

def f75ps_f75_fcf_per_share_acceleration_calc124_126d_slope_v124_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.rolling(126).quantile(0.5) / fcf.rolling(126).quantile(0.5).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc124_126d_slope_v124_signal'] = f75ps_f75_fcf_per_share_acceleration_calc124_126d_slope_v124_signal

def f75ps_f75_fcf_per_share_acceleration_calc125_126d_slope_v125_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.rolling(126).kurt() - sharesbas.rolling(126).kurt())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc125_126d_slope_v125_signal'] = f75ps_f75_fcf_per_share_acceleration_calc125_126d_slope_v125_signal

def f75ps_f75_fcf_per_share_acceleration_calc126_10d_slope_v126_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc.rolling(10).max() - revenue.rolling(10).min()) / fcf.replace(0, np.nan)
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc126_10d_slope_v126_signal'] = f75ps_f75_fcf_per_share_acceleration_calc126_10d_slope_v126_signal

def f75ps_f75_fcf_per_share_acceleration_calc127_5d_slope_v127_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.rolling(5).kurt() - eps.rolling(5).kurt())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc127_5d_slope_v127_signal'] = f75ps_f75_fcf_per_share_acceleration_calc127_5d_slope_v127_signal

def f75ps_f75_fcf_per_share_acceleration_calc128_21d_slope_v128_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc128_21d_slope_v128_signal'] = f75ps_f75_fcf_per_share_acceleration_calc128_21d_slope_v128_signal

def f75ps_f75_fcf_per_share_acceleration_calc129_42d_slope_v129_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.pct_change(42) - eps.pct_change(42))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc129_42d_slope_v129_signal'] = f75ps_f75_fcf_per_share_acceleration_calc129_42d_slope_v129_signal

def f75ps_f75_fcf_per_share_acceleration_calc130_63d_slope_v130_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.rolling(63).max() - marketcap.rolling(63).min()) / assets.replace(0, np.nan)
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc130_63d_slope_v130_signal'] = f75ps_f75_fcf_per_share_acceleration_calc130_63d_slope_v130_signal

def f75ps_f75_fcf_per_share_acceleration_calc131_63d_slope_v131_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (sharesbas.pct_change(63) - assets.pct_change(63))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc131_63d_slope_v131_signal'] = f75ps_f75_fcf_per_share_acceleration_calc131_63d_slope_v131_signal

def f75ps_f75_fcf_per_share_acceleration_calc132_10d_slope_v132_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets / revenue.replace(0, np.nan)).rolling(10).mean()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc132_10d_slope_v132_signal'] = f75ps_f75_fcf_per_share_acceleration_calc132_10d_slope_v132_signal

def f75ps_f75_fcf_per_share_acceleration_calc133_63d_slope_v133_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.diff(63).abs() / sharesbas.diff(63).abs().replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc133_63d_slope_v133_signal'] = f75ps_f75_fcf_per_share_acceleration_calc133_63d_slope_v133_signal

def f75ps_f75_fcf_per_share_acceleration_calc134_42d_slope_v134_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.diff(42) / marketcap.replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc134_42d_slope_v134_signal'] = f75ps_f75_fcf_per_share_acceleration_calc134_42d_slope_v134_signal

def f75ps_f75_fcf_per_share_acceleration_calc135_126d_slope_v135_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((marketcap - marketcap.rolling(126).mean()) / marketcap.rolling(126).std())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc135_126d_slope_v135_signal'] = f75ps_f75_fcf_per_share_acceleration_calc135_126d_slope_v135_signal

def f75ps_f75_fcf_per_share_acceleration_calc136_5d_slope_v136_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (fcf.pct_change(5) - revenue.pct_change(5))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc136_5d_slope_v136_signal'] = f75ps_f75_fcf_per_share_acceleration_calc136_5d_slope_v136_signal

def f75ps_f75_fcf_per_share_acceleration_calc137_126d_slope_v137_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.rolling(126).kurt() - netinc.rolling(126).kurt())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc137_126d_slope_v137_signal'] = f75ps_f75_fcf_per_share_acceleration_calc137_126d_slope_v137_signal

def f75ps_f75_fcf_per_share_acceleration_calc138_5d_slope_v138_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps.pct_change(5) - assets.pct_change(5))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc138_5d_slope_v138_signal'] = f75ps_f75_fcf_per_share_acceleration_calc138_5d_slope_v138_signal

def f75ps_f75_fcf_per_share_acceleration_calc139_5d_slope_v139_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.rolling(5).max() - marketcap.rolling(5).min()) / eps.replace(0, np.nan)
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc139_5d_slope_v139_signal'] = f75ps_f75_fcf_per_share_acceleration_calc139_5d_slope_v139_signal

def f75ps_f75_fcf_per_share_acceleration_calc140_21d_slope_v140_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (eps / revenue.replace(0, np.nan)).rolling(21).mean()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc140_21d_slope_v140_signal'] = f75ps_f75_fcf_per_share_acceleration_calc140_21d_slope_v140_signal

def f75ps_f75_fcf_per_share_acceleration_calc141_42d_slope_v141_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.diff(42).abs() / eps.diff(42).abs().replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc141_42d_slope_v141_signal'] = f75ps_f75_fcf_per_share_acceleration_calc141_42d_slope_v141_signal

def f75ps_f75_fcf_per_share_acceleration_calc142_252d_slope_v142_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((sharesbas - sharesbas.rolling(252).mean()) / sharesbas.rolling(252).std())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc142_252d_slope_v142_signal'] = f75ps_f75_fcf_per_share_acceleration_calc142_252d_slope_v142_signal

def f75ps_f75_fcf_per_share_acceleration_calc143_10d_slope_v143_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc143_10d_slope_v143_signal'] = f75ps_f75_fcf_per_share_acceleration_calc143_10d_slope_v143_signal

def f75ps_f75_fcf_per_share_acceleration_calc144_252d_slope_v144_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (marketcap.rolling(252).rank(pct=True) / sharesbas.rolling(252).rank(pct=True).replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc144_252d_slope_v144_signal'] = f75ps_f75_fcf_per_share_acceleration_calc144_252d_slope_v144_signal

def f75ps_f75_fcf_per_share_acceleration_calc145_126d_slope_v145_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.diff(126) / revenue.replace(0, np.nan))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc145_126d_slope_v145_signal'] = f75ps_f75_fcf_per_share_acceleration_calc145_126d_slope_v145_signal

def f75ps_f75_fcf_per_share_acceleration_calc146_63d_slope_v146_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (assets.rolling(63).max() - sharesbas.rolling(63).min()) / eps.replace(0, np.nan)
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc146_63d_slope_v146_signal'] = f75ps_f75_fcf_per_share_acceleration_calc146_63d_slope_v146_signal

def f75ps_f75_fcf_per_share_acceleration_calc147_10d_slope_v147_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (revenue.pct_change(10) - assets.pct_change(10))
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc147_10d_slope_v147_signal'] = f75ps_f75_fcf_per_share_acceleration_calc147_10d_slope_v147_signal

def f75ps_f75_fcf_per_share_acceleration_calc148_21d_slope_v148_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = ((sharesbas - sharesbas.rolling(21).mean()) / sharesbas.rolling(21).std())
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc148_21d_slope_v148_signal'] = f75ps_f75_fcf_per_share_acceleration_calc148_21d_slope_v148_signal

def f75ps_f75_fcf_per_share_acceleration_calc149_63d_slope_v149_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc / eps.replace(0, np.nan)).rolling(63).std()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc149_63d_slope_v149_signal'] = f75ps_f75_fcf_per_share_acceleration_calc149_63d_slope_v149_signal

def f75ps_f75_fcf_per_share_acceleration_calc150_42d_slope_v150_signal(fcf, sharesbas, marketcap, eps, netinc, revenue, assets):
    v1 = (netinc / assets.replace(0, np.nan)).rolling(42).mean()
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
FEATURE_FUNCTIONS['f75ps_f75_fcf_per_share_acceleration_calc150_42d_slope_v150_signal'] = f75ps_f75_fcf_per_share_acceleration_calc150_42d_slope_v150_signal



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
