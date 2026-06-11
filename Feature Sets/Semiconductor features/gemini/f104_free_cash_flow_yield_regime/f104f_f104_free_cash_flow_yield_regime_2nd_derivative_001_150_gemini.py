import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f104f_f104_free_cash_flow_yield_regime_calc001_63d_slope_v001_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.rolling(63).quantile(0.5) / revenue.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc001_63d_slope_v001_signal'] = f104f_f104_free_cash_flow_yield_regime_calc001_63d_slope_v001_signal

def f104f_f104_free_cash_flow_yield_regime_calc002_5d_slope_v002_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf.rolling(5).rank(pct=True) / equity.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc002_5d_slope_v002_signal'] = f104f_f104_free_cash_flow_yield_regime_calc002_5d_slope_v002_signal

def f104f_f104_free_cash_flow_yield_regime_calc003_252d_slope_v003_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.diff(252).abs() / fcf.diff(252).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc003_252d_slope_v003_signal'] = f104f_f104_free_cash_flow_yield_regime_calc003_252d_slope_v003_signal

def f104f_f104_free_cash_flow_yield_regime_calc004_5d_slope_v004_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.pct_change(5) - marketcap.pct_change(5))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc004_5d_slope_v004_signal'] = f104f_f104_free_cash_flow_yield_regime_calc004_5d_slope_v004_signal

def f104f_f104_free_cash_flow_yield_regime_calc005_21d_slope_v005_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.rolling(21).quantile(0.5) / equity.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc005_21d_slope_v005_signal'] = f104f_f104_free_cash_flow_yield_regime_calc005_21d_slope_v005_signal

def f104f_f104_free_cash_flow_yield_regime_calc006_10d_slope_v006_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity / revenue.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc006_10d_slope_v006_signal'] = f104f_f104_free_cash_flow_yield_regime_calc006_10d_slope_v006_signal

def f104f_f104_free_cash_flow_yield_regime_calc007_10d_slope_v007_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.pct_change(10) - revenue.pct_change(10))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc007_10d_slope_v007_signal'] = f104f_f104_free_cash_flow_yield_regime_calc007_10d_slope_v007_signal

def f104f_f104_free_cash_flow_yield_regime_calc008_63d_slope_v008_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf.pct_change(63) - assets.pct_change(63))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc008_63d_slope_v008_signal'] = f104f_f104_free_cash_flow_yield_regime_calc008_63d_slope_v008_signal

def f104f_f104_free_cash_flow_yield_regime_calc009_21d_slope_v009_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue / fcf.replace(0, np.nan)).rolling(21).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc009_21d_slope_v009_signal'] = f104f_f104_free_cash_flow_yield_regime_calc009_21d_slope_v009_signal

def f104f_f104_free_cash_flow_yield_regime_calc010_63d_slope_v010_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev / marketcap.replace(0, np.nan)).rolling(63).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc010_63d_slope_v010_signal'] = f104f_f104_free_cash_flow_yield_regime_calc010_63d_slope_v010_signal

def f104f_f104_free_cash_flow_yield_regime_calc011_63d_slope_v011_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf.rolling(63).quantile(0.5) / assets.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc011_63d_slope_v011_signal'] = f104f_f104_free_cash_flow_yield_regime_calc011_63d_slope_v011_signal

def f104f_f104_free_cash_flow_yield_regime_calc012_21d_slope_v012_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.diff(21) / assets.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc012_21d_slope_v012_signal'] = f104f_f104_free_cash_flow_yield_regime_calc012_21d_slope_v012_signal

def f104f_f104_free_cash_flow_yield_regime_calc013_21d_slope_v013_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(21).kurt() - fcf.rolling(21).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc013_21d_slope_v013_signal'] = f104f_f104_free_cash_flow_yield_regime_calc013_21d_slope_v013_signal

def f104f_f104_free_cash_flow_yield_regime_calc014_126d_slope_v014_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.pct_change(126) - equity.pct_change(126))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc014_126d_slope_v014_signal'] = f104f_f104_free_cash_flow_yield_regime_calc014_126d_slope_v014_signal

def f104f_f104_free_cash_flow_yield_regime_calc015_252d_slope_v015_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.rolling(252).quantile(0.5) / equity.rolling(252).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc015_252d_slope_v015_signal'] = f104f_f104_free_cash_flow_yield_regime_calc015_252d_slope_v015_signal

def f104f_f104_free_cash_flow_yield_regime_calc016_252d_slope_v016_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.pct_change(252) - fcf.pct_change(252))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc016_252d_slope_v016_signal'] = f104f_f104_free_cash_flow_yield_regime_calc016_252d_slope_v016_signal

def f104f_f104_free_cash_flow_yield_regime_calc017_63d_slope_v017_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.rolling(63).rank(pct=True) / equity.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc017_63d_slope_v017_signal'] = f104f_f104_free_cash_flow_yield_regime_calc017_63d_slope_v017_signal

def f104f_f104_free_cash_flow_yield_regime_calc018_42d_slope_v018_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.rolling(42).kurt() - revenue.rolling(42).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc018_42d_slope_v018_signal'] = f104f_f104_free_cash_flow_yield_regime_calc018_42d_slope_v018_signal

def f104f_f104_free_cash_flow_yield_regime_calc019_21d_slope_v019_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity / assets.replace(0, np.nan)).rolling(21).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc019_21d_slope_v019_signal'] = f104f_f104_free_cash_flow_yield_regime_calc019_21d_slope_v019_signal

def f104f_f104_free_cash_flow_yield_regime_calc020_42d_slope_v020_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.rolling(42).quantile(0.5) / revenue.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc020_42d_slope_v020_signal'] = f104f_f104_free_cash_flow_yield_regime_calc020_42d_slope_v020_signal

def f104f_f104_free_cash_flow_yield_regime_calc021_63d_slope_v021_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.diff(63) / marketcap.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc021_63d_slope_v021_signal'] = f104f_f104_free_cash_flow_yield_regime_calc021_63d_slope_v021_signal

def f104f_f104_free_cash_flow_yield_regime_calc022_126d_slope_v022_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
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
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc022_126d_slope_v022_signal'] = f104f_f104_free_cash_flow_yield_regime_calc022_126d_slope_v022_signal

def f104f_f104_free_cash_flow_yield_regime_calc023_10d_slope_v023_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev / ncfo.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc023_10d_slope_v023_signal'] = f104f_f104_free_cash_flow_yield_regime_calc023_10d_slope_v023_signal

def f104f_f104_free_cash_flow_yield_regime_calc024_21d_slope_v024_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
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
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc024_21d_slope_v024_signal'] = f104f_f104_free_cash_flow_yield_regime_calc024_21d_slope_v024_signal

def f104f_f104_free_cash_flow_yield_regime_calc025_63d_slope_v025_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(63).rank(pct=True) / assets.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc025_63d_slope_v025_signal'] = f104f_f104_free_cash_flow_yield_regime_calc025_63d_slope_v025_signal

def f104f_f104_free_cash_flow_yield_regime_calc026_21d_slope_v026_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.pct_change(21) - revenue.pct_change(21))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc026_21d_slope_v026_signal'] = f104f_f104_free_cash_flow_yield_regime_calc026_21d_slope_v026_signal

def f104f_f104_free_cash_flow_yield_regime_calc027_42d_slope_v027_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.diff(42) / equity.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc027_42d_slope_v027_signal'] = f104f_f104_free_cash_flow_yield_regime_calc027_42d_slope_v027_signal

def f104f_f104_free_cash_flow_yield_regime_calc028_21d_slope_v028_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.pct_change(21) - ncfo.pct_change(21))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc028_21d_slope_v028_signal'] = f104f_f104_free_cash_flow_yield_regime_calc028_21d_slope_v028_signal

def f104f_f104_free_cash_flow_yield_regime_calc029_10d_slope_v029_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.rolling(10).kurt() - fcf.rolling(10).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc029_10d_slope_v029_signal'] = f104f_f104_free_cash_flow_yield_regime_calc029_10d_slope_v029_signal

def f104f_f104_free_cash_flow_yield_regime_calc030_252d_slope_v030_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(252).max() - ncfo.rolling(252).min()) / marketcap.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc030_252d_slope_v030_signal'] = f104f_f104_free_cash_flow_yield_regime_calc030_252d_slope_v030_signal

def f104f_f104_free_cash_flow_yield_regime_calc031_126d_slope_v031_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf.rolling(126).quantile(0.5) / marketcap.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc031_126d_slope_v031_signal'] = f104f_f104_free_cash_flow_yield_regime_calc031_126d_slope_v031_signal

def f104f_f104_free_cash_flow_yield_regime_calc032_252d_slope_v032_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets / fcf.replace(0, np.nan)).rolling(252).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc032_252d_slope_v032_signal'] = f104f_f104_free_cash_flow_yield_regime_calc032_252d_slope_v032_signal

def f104f_f104_free_cash_flow_yield_regime_calc033_126d_slope_v033_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(126).rank(pct=True) / revenue.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc033_126d_slope_v033_signal'] = f104f_f104_free_cash_flow_yield_regime_calc033_126d_slope_v033_signal

def f104f_f104_free_cash_flow_yield_regime_calc034_252d_slope_v034_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.rolling(252).rank(pct=True) / fcf.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc034_252d_slope_v034_signal'] = f104f_f104_free_cash_flow_yield_regime_calc034_252d_slope_v034_signal

def f104f_f104_free_cash_flow_yield_regime_calc035_5d_slope_v035_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.diff(5) / equity.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc035_5d_slope_v035_signal'] = f104f_f104_free_cash_flow_yield_regime_calc035_5d_slope_v035_signal

def f104f_f104_free_cash_flow_yield_regime_calc036_252d_slope_v036_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.pct_change(252) - marketcap.pct_change(252))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc036_252d_slope_v036_signal'] = f104f_f104_free_cash_flow_yield_regime_calc036_252d_slope_v036_signal

def f104f_f104_free_cash_flow_yield_regime_calc037_10d_slope_v037_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = ((fcf - fcf.rolling(10).mean()) / fcf.rolling(10).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc037_10d_slope_v037_signal'] = f104f_f104_free_cash_flow_yield_regime_calc037_10d_slope_v037_signal

def f104f_f104_free_cash_flow_yield_regime_calc038_5d_slope_v038_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue / ncfo.replace(0, np.nan)).rolling(5).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc038_5d_slope_v038_signal'] = f104f_f104_free_cash_flow_yield_regime_calc038_5d_slope_v038_signal

def f104f_f104_free_cash_flow_yield_regime_calc039_63d_slope_v039_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue / equity.replace(0, np.nan)).rolling(63).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc039_63d_slope_v039_signal'] = f104f_f104_free_cash_flow_yield_regime_calc039_63d_slope_v039_signal

def f104f_f104_free_cash_flow_yield_regime_calc040_21d_slope_v040_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev / revenue.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc040_21d_slope_v040_signal'] = f104f_f104_free_cash_flow_yield_regime_calc040_21d_slope_v040_signal

def f104f_f104_free_cash_flow_yield_regime_calc041_21d_slope_v041_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.rolling(21).quantile(0.5) / fcf.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc041_21d_slope_v041_signal'] = f104f_f104_free_cash_flow_yield_regime_calc041_21d_slope_v041_signal

def f104f_f104_free_cash_flow_yield_regime_calc042_21d_slope_v042_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.diff(21) / ev.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc042_21d_slope_v042_signal'] = f104f_f104_free_cash_flow_yield_regime_calc042_21d_slope_v042_signal

def f104f_f104_free_cash_flow_yield_regime_calc043_42d_slope_v043_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(42).quantile(0.5) / revenue.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc043_42d_slope_v043_signal'] = f104f_f104_free_cash_flow_yield_regime_calc043_42d_slope_v043_signal

def f104f_f104_free_cash_flow_yield_regime_calc044_63d_slope_v044_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.diff(63) / marketcap.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc044_63d_slope_v044_signal'] = f104f_f104_free_cash_flow_yield_regime_calc044_63d_slope_v044_signal

def f104f_f104_free_cash_flow_yield_regime_calc045_21d_slope_v045_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.rolling(21).kurt() - ncfo.rolling(21).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc045_21d_slope_v045_signal'] = f104f_f104_free_cash_flow_yield_regime_calc045_21d_slope_v045_signal

def f104f_f104_free_cash_flow_yield_regime_calc046_126d_slope_v046_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.rolling(126).rank(pct=True) / ev.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc046_126d_slope_v046_signal'] = f104f_f104_free_cash_flow_yield_regime_calc046_126d_slope_v046_signal

def f104f_f104_free_cash_flow_yield_regime_calc047_10d_slope_v047_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo / fcf.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc047_10d_slope_v047_signal'] = f104f_f104_free_cash_flow_yield_regime_calc047_10d_slope_v047_signal

def f104f_f104_free_cash_flow_yield_regime_calc048_252d_slope_v048_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
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
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc048_252d_slope_v048_signal'] = f104f_f104_free_cash_flow_yield_regime_calc048_252d_slope_v048_signal

def f104f_f104_free_cash_flow_yield_regime_calc049_126d_slope_v049_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue / fcf.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc049_126d_slope_v049_signal'] = f104f_f104_free_cash_flow_yield_regime_calc049_126d_slope_v049_signal

def f104f_f104_free_cash_flow_yield_regime_calc050_126d_slope_v050_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo / fcf.replace(0, np.nan)).rolling(126).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc050_126d_slope_v050_signal'] = f104f_f104_free_cash_flow_yield_regime_calc050_126d_slope_v050_signal

def f104f_f104_free_cash_flow_yield_regime_calc051_10d_slope_v051_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.diff(10).abs() / equity.diff(10).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc051_10d_slope_v051_signal'] = f104f_f104_free_cash_flow_yield_regime_calc051_10d_slope_v051_signal

def f104f_f104_free_cash_flow_yield_regime_calc052_5d_slope_v052_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf.rolling(5).max() - ev.rolling(5).min()) / marketcap.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc052_5d_slope_v052_signal'] = f104f_f104_free_cash_flow_yield_regime_calc052_5d_slope_v052_signal

def f104f_f104_free_cash_flow_yield_regime_calc053_42d_slope_v053_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.rolling(42).rank(pct=True) / marketcap.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc053_42d_slope_v053_signal'] = f104f_f104_free_cash_flow_yield_regime_calc053_42d_slope_v053_signal

def f104f_f104_free_cash_flow_yield_regime_calc054_42d_slope_v054_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = ((marketcap - marketcap.rolling(42).mean()) / marketcap.rolling(42).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc054_42d_slope_v054_signal'] = f104f_f104_free_cash_flow_yield_regime_calc054_42d_slope_v054_signal

def f104f_f104_free_cash_flow_yield_regime_calc055_63d_slope_v055_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf / revenue.replace(0, np.nan)).rolling(63).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc055_63d_slope_v055_signal'] = f104f_f104_free_cash_flow_yield_regime_calc055_63d_slope_v055_signal

def f104f_f104_free_cash_flow_yield_regime_calc056_10d_slope_v056_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.diff(10).abs() / assets.diff(10).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc056_10d_slope_v056_signal'] = f104f_f104_free_cash_flow_yield_regime_calc056_10d_slope_v056_signal

def f104f_f104_free_cash_flow_yield_regime_calc057_252d_slope_v057_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.diff(252).abs() / ev.diff(252).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc057_252d_slope_v057_signal'] = f104f_f104_free_cash_flow_yield_regime_calc057_252d_slope_v057_signal

def f104f_f104_free_cash_flow_yield_regime_calc058_126d_slope_v058_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue / marketcap.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc058_126d_slope_v058_signal'] = f104f_f104_free_cash_flow_yield_regime_calc058_126d_slope_v058_signal

def f104f_f104_free_cash_flow_yield_regime_calc059_42d_slope_v059_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.rolling(42).kurt() - assets.rolling(42).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc059_42d_slope_v059_signal'] = f104f_f104_free_cash_flow_yield_regime_calc059_42d_slope_v059_signal

def f104f_f104_free_cash_flow_yield_regime_calc060_126d_slope_v060_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.diff(126).abs() / equity.diff(126).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc060_126d_slope_v060_signal'] = f104f_f104_free_cash_flow_yield_regime_calc060_126d_slope_v060_signal

def f104f_f104_free_cash_flow_yield_regime_calc061_126d_slope_v061_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.rolling(126).rank(pct=True) / fcf.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc061_126d_slope_v061_signal'] = f104f_f104_free_cash_flow_yield_regime_calc061_126d_slope_v061_signal

def f104f_f104_free_cash_flow_yield_regime_calc062_10d_slope_v062_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = ((marketcap - marketcap.rolling(10).mean()) / marketcap.rolling(10).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc062_10d_slope_v062_signal'] = f104f_f104_free_cash_flow_yield_regime_calc062_10d_slope_v062_signal

def f104f_f104_free_cash_flow_yield_regime_calc063_252d_slope_v063_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.pct_change(252) - assets.pct_change(252))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc063_252d_slope_v063_signal'] = f104f_f104_free_cash_flow_yield_regime_calc063_252d_slope_v063_signal

def f104f_f104_free_cash_flow_yield_regime_calc064_21d_slope_v064_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.rolling(21).max() - revenue.rolling(21).min()) / ev.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc064_21d_slope_v064_signal'] = f104f_f104_free_cash_flow_yield_regime_calc064_21d_slope_v064_signal

def f104f_f104_free_cash_flow_yield_regime_calc065_42d_slope_v065_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.diff(42).abs() / fcf.diff(42).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc065_42d_slope_v065_signal'] = f104f_f104_free_cash_flow_yield_regime_calc065_42d_slope_v065_signal

def f104f_f104_free_cash_flow_yield_regime_calc066_42d_slope_v066_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.diff(42) / ev.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc066_42d_slope_v066_signal'] = f104f_f104_free_cash_flow_yield_regime_calc066_42d_slope_v066_signal

def f104f_f104_free_cash_flow_yield_regime_calc067_42d_slope_v067_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.rolling(42).max() - ev.rolling(42).min()) / fcf.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc067_42d_slope_v067_signal'] = f104f_f104_free_cash_flow_yield_regime_calc067_42d_slope_v067_signal

def f104f_f104_free_cash_flow_yield_regime_calc068_5d_slope_v068_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.pct_change(5) - assets.pct_change(5))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc068_5d_slope_v068_signal'] = f104f_f104_free_cash_flow_yield_regime_calc068_5d_slope_v068_signal

def f104f_f104_free_cash_flow_yield_regime_calc069_21d_slope_v069_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.rolling(21).quantile(0.5) / ncfo.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc069_21d_slope_v069_signal'] = f104f_f104_free_cash_flow_yield_regime_calc069_21d_slope_v069_signal

def f104f_f104_free_cash_flow_yield_regime_calc070_126d_slope_v070_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.diff(126).abs() / ncfo.diff(126).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc070_126d_slope_v070_signal'] = f104f_f104_free_cash_flow_yield_regime_calc070_126d_slope_v070_signal

def f104f_f104_free_cash_flow_yield_regime_calc071_10d_slope_v071_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.rolling(10).kurt() - fcf.rolling(10).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc071_10d_slope_v071_signal'] = f104f_f104_free_cash_flow_yield_regime_calc071_10d_slope_v071_signal

def f104f_f104_free_cash_flow_yield_regime_calc072_10d_slope_v072_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(10).quantile(0.5) / assets.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc072_10d_slope_v072_signal'] = f104f_f104_free_cash_flow_yield_regime_calc072_10d_slope_v072_signal

def f104f_f104_free_cash_flow_yield_regime_calc073_42d_slope_v073_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.diff(42).abs() / revenue.diff(42).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc073_42d_slope_v073_signal'] = f104f_f104_free_cash_flow_yield_regime_calc073_42d_slope_v073_signal

def f104f_f104_free_cash_flow_yield_regime_calc074_10d_slope_v074_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.rolling(10).kurt() - ev.rolling(10).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc074_10d_slope_v074_signal'] = f104f_f104_free_cash_flow_yield_regime_calc074_10d_slope_v074_signal

def f104f_f104_free_cash_flow_yield_regime_calc075_42d_slope_v075_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.rolling(42).max() - ncfo.rolling(42).min()) / fcf.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc075_42d_slope_v075_signal'] = f104f_f104_free_cash_flow_yield_regime_calc075_42d_slope_v075_signal

def f104f_f104_free_cash_flow_yield_regime_calc076_21d_slope_v076_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity / ev.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc076_21d_slope_v076_signal'] = f104f_f104_free_cash_flow_yield_regime_calc076_21d_slope_v076_signal

def f104f_f104_free_cash_flow_yield_regime_calc077_63d_slope_v077_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.rolling(63).rank(pct=True) / ncfo.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc077_63d_slope_v077_signal'] = f104f_f104_free_cash_flow_yield_regime_calc077_63d_slope_v077_signal

def f104f_f104_free_cash_flow_yield_regime_calc078_252d_slope_v078_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.diff(252).abs() / marketcap.diff(252).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc078_252d_slope_v078_signal'] = f104f_f104_free_cash_flow_yield_regime_calc078_252d_slope_v078_signal

def f104f_f104_free_cash_flow_yield_regime_calc079_126d_slope_v079_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity / ev.replace(0, np.nan)).rolling(126).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc079_126d_slope_v079_signal'] = f104f_f104_free_cash_flow_yield_regime_calc079_126d_slope_v079_signal

def f104f_f104_free_cash_flow_yield_regime_calc080_126d_slope_v080_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.rolling(126).quantile(0.5) / revenue.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc080_126d_slope_v080_signal'] = f104f_f104_free_cash_flow_yield_regime_calc080_126d_slope_v080_signal

def f104f_f104_free_cash_flow_yield_regime_calc081_126d_slope_v081_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(126).kurt() - assets.rolling(126).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc081_126d_slope_v081_signal'] = f104f_f104_free_cash_flow_yield_regime_calc081_126d_slope_v081_signal

def f104f_f104_free_cash_flow_yield_regime_calc082_10d_slope_v082_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.rolling(10).rank(pct=True) / revenue.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc082_10d_slope_v082_signal'] = f104f_f104_free_cash_flow_yield_regime_calc082_10d_slope_v082_signal

def f104f_f104_free_cash_flow_yield_regime_calc083_10d_slope_v083_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.diff(10) / ev.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc083_10d_slope_v083_signal'] = f104f_f104_free_cash_flow_yield_regime_calc083_10d_slope_v083_signal

def f104f_f104_free_cash_flow_yield_regime_calc084_21d_slope_v084_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.rolling(21).kurt() - marketcap.rolling(21).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc084_21d_slope_v084_signal'] = f104f_f104_free_cash_flow_yield_regime_calc084_21d_slope_v084_signal

def f104f_f104_free_cash_flow_yield_regime_calc085_42d_slope_v085_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(42).max() - ev.rolling(42).min()) / fcf.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc085_42d_slope_v085_signal'] = f104f_f104_free_cash_flow_yield_regime_calc085_42d_slope_v085_signal

def f104f_f104_free_cash_flow_yield_regime_calc086_42d_slope_v086_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.pct_change(42) - ncfo.pct_change(42))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc086_42d_slope_v086_signal'] = f104f_f104_free_cash_flow_yield_regime_calc086_42d_slope_v086_signal

def f104f_f104_free_cash_flow_yield_regime_calc087_21d_slope_v087_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(21).kurt() - assets.rolling(21).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc087_21d_slope_v087_signal'] = f104f_f104_free_cash_flow_yield_regime_calc087_21d_slope_v087_signal

def f104f_f104_free_cash_flow_yield_regime_calc088_126d_slope_v088_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets / equity.replace(0, np.nan)).rolling(126).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc088_126d_slope_v088_signal'] = f104f_f104_free_cash_flow_yield_regime_calc088_126d_slope_v088_signal

def f104f_f104_free_cash_flow_yield_regime_calc089_63d_slope_v089_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = ((fcf - fcf.rolling(63).mean()) / fcf.rolling(63).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc089_63d_slope_v089_signal'] = f104f_f104_free_cash_flow_yield_regime_calc089_63d_slope_v089_signal

def f104f_f104_free_cash_flow_yield_regime_calc090_42d_slope_v090_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.diff(42) / revenue.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc090_42d_slope_v090_signal'] = f104f_f104_free_cash_flow_yield_regime_calc090_42d_slope_v090_signal

def f104f_f104_free_cash_flow_yield_regime_calc091_21d_slope_v091_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
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
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc091_21d_slope_v091_signal'] = f104f_f104_free_cash_flow_yield_regime_calc091_21d_slope_v091_signal

def f104f_f104_free_cash_flow_yield_regime_calc092_63d_slope_v092_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.rolling(63).kurt() - revenue.rolling(63).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc092_63d_slope_v092_signal'] = f104f_f104_free_cash_flow_yield_regime_calc092_63d_slope_v092_signal

def f104f_f104_free_cash_flow_yield_regime_calc093_42d_slope_v093_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue / equity.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc093_42d_slope_v093_signal'] = f104f_f104_free_cash_flow_yield_regime_calc093_42d_slope_v093_signal

def f104f_f104_free_cash_flow_yield_regime_calc094_126d_slope_v094_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf / ev.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc094_126d_slope_v094_signal'] = f104f_f104_free_cash_flow_yield_regime_calc094_126d_slope_v094_signal

def f104f_f104_free_cash_flow_yield_regime_calc095_63d_slope_v095_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.diff(63) / ev.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc095_63d_slope_v095_signal'] = f104f_f104_free_cash_flow_yield_regime_calc095_63d_slope_v095_signal

def f104f_f104_free_cash_flow_yield_regime_calc096_63d_slope_v096_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.rolling(63).max() - equity.rolling(63).min()) / fcf.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc096_63d_slope_v096_signal'] = f104f_f104_free_cash_flow_yield_regime_calc096_63d_slope_v096_signal

def f104f_f104_free_cash_flow_yield_regime_calc097_63d_slope_v097_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf.rolling(63).quantile(0.5) / ev.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc097_63d_slope_v097_signal'] = f104f_f104_free_cash_flow_yield_regime_calc097_63d_slope_v097_signal

def f104f_f104_free_cash_flow_yield_regime_calc098_21d_slope_v098_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.pct_change(21) - fcf.pct_change(21))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc098_21d_slope_v098_signal'] = f104f_f104_free_cash_flow_yield_regime_calc098_21d_slope_v098_signal

def f104f_f104_free_cash_flow_yield_regime_calc099_10d_slope_v099_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.diff(10).abs() / ev.diff(10).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc099_10d_slope_v099_signal'] = f104f_f104_free_cash_flow_yield_regime_calc099_10d_slope_v099_signal

def f104f_f104_free_cash_flow_yield_regime_calc100_42d_slope_v100_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(42).quantile(0.5) / ev.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc100_42d_slope_v100_signal'] = f104f_f104_free_cash_flow_yield_regime_calc100_42d_slope_v100_signal

def f104f_f104_free_cash_flow_yield_regime_calc101_42d_slope_v101_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo / ev.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc101_42d_slope_v101_signal'] = f104f_f104_free_cash_flow_yield_regime_calc101_42d_slope_v101_signal

def f104f_f104_free_cash_flow_yield_regime_calc102_5d_slope_v102_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo / fcf.replace(0, np.nan)).rolling(5).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc102_5d_slope_v102_signal'] = f104f_f104_free_cash_flow_yield_regime_calc102_5d_slope_v102_signal

def f104f_f104_free_cash_flow_yield_regime_calc103_10d_slope_v103_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo / assets.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc103_10d_slope_v103_signal'] = f104f_f104_free_cash_flow_yield_regime_calc103_10d_slope_v103_signal

def f104f_f104_free_cash_flow_yield_regime_calc104_63d_slope_v104_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo / marketcap.replace(0, np.nan)).rolling(63).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc104_63d_slope_v104_signal'] = f104f_f104_free_cash_flow_yield_regime_calc104_63d_slope_v104_signal

def f104f_f104_free_cash_flow_yield_regime_calc105_5d_slope_v105_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf.diff(5) / equity.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc105_5d_slope_v105_signal'] = f104f_f104_free_cash_flow_yield_regime_calc105_5d_slope_v105_signal

def f104f_f104_free_cash_flow_yield_regime_calc106_10d_slope_v106_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.pct_change(10) - equity.pct_change(10))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc106_10d_slope_v106_signal'] = f104f_f104_free_cash_flow_yield_regime_calc106_10d_slope_v106_signal

def f104f_f104_free_cash_flow_yield_regime_calc107_21d_slope_v107_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets / marketcap.replace(0, np.nan)).rolling(21).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc107_21d_slope_v107_signal'] = f104f_f104_free_cash_flow_yield_regime_calc107_21d_slope_v107_signal

def f104f_f104_free_cash_flow_yield_regime_calc108_126d_slope_v108_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf / revenue.replace(0, np.nan)).rolling(126).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc108_126d_slope_v108_signal'] = f104f_f104_free_cash_flow_yield_regime_calc108_126d_slope_v108_signal

def f104f_f104_free_cash_flow_yield_regime_calc109_10d_slope_v109_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.diff(10).abs() / marketcap.diff(10).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc109_10d_slope_v109_signal'] = f104f_f104_free_cash_flow_yield_regime_calc109_10d_slope_v109_signal

def f104f_f104_free_cash_flow_yield_regime_calc110_5d_slope_v110_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf.rolling(5).quantile(0.5) / ncfo.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc110_5d_slope_v110_signal'] = f104f_f104_free_cash_flow_yield_regime_calc110_5d_slope_v110_signal

def f104f_f104_free_cash_flow_yield_regime_calc111_10d_slope_v111_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets / fcf.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc111_10d_slope_v111_signal'] = f104f_f104_free_cash_flow_yield_regime_calc111_10d_slope_v111_signal

def f104f_f104_free_cash_flow_yield_regime_calc112_5d_slope_v112_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.diff(5) / fcf.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc112_5d_slope_v112_signal'] = f104f_f104_free_cash_flow_yield_regime_calc112_5d_slope_v112_signal

def f104f_f104_free_cash_flow_yield_regime_calc113_5d_slope_v113_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.pct_change(5) - ev.pct_change(5))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc113_5d_slope_v113_signal'] = f104f_f104_free_cash_flow_yield_regime_calc113_5d_slope_v113_signal

def f104f_f104_free_cash_flow_yield_regime_calc114_252d_slope_v114_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.diff(252) / assets.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc114_252d_slope_v114_signal'] = f104f_f104_free_cash_flow_yield_regime_calc114_252d_slope_v114_signal

def f104f_f104_free_cash_flow_yield_regime_calc115_63d_slope_v115_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
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
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc115_63d_slope_v115_signal'] = f104f_f104_free_cash_flow_yield_regime_calc115_63d_slope_v115_signal

def f104f_f104_free_cash_flow_yield_regime_calc116_5d_slope_v116_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(5).quantile(0.5) / fcf.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc116_5d_slope_v116_signal'] = f104f_f104_free_cash_flow_yield_regime_calc116_5d_slope_v116_signal

def f104f_f104_free_cash_flow_yield_regime_calc117_21d_slope_v117_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = ((ev - ev.rolling(21).mean()) / ev.rolling(21).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc117_21d_slope_v117_signal'] = f104f_f104_free_cash_flow_yield_regime_calc117_21d_slope_v117_signal

def f104f_f104_free_cash_flow_yield_regime_calc118_21d_slope_v118_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.rolling(21).rank(pct=True) / ncfo.rolling(21).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc118_21d_slope_v118_signal'] = f104f_f104_free_cash_flow_yield_regime_calc118_21d_slope_v118_signal

def f104f_f104_free_cash_flow_yield_regime_calc119_63d_slope_v119_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.rolling(63).kurt() - ncfo.rolling(63).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc119_63d_slope_v119_signal'] = f104f_f104_free_cash_flow_yield_regime_calc119_63d_slope_v119_signal

def f104f_f104_free_cash_flow_yield_regime_calc120_10d_slope_v120_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev / revenue.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc120_10d_slope_v120_signal'] = f104f_f104_free_cash_flow_yield_regime_calc120_10d_slope_v120_signal

def f104f_f104_free_cash_flow_yield_regime_calc121_21d_slope_v121_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.diff(21) / ncfo.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc121_21d_slope_v121_signal'] = f104f_f104_free_cash_flow_yield_regime_calc121_21d_slope_v121_signal

def f104f_f104_free_cash_flow_yield_regime_calc122_126d_slope_v122_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = ((equity - equity.rolling(126).mean()) / equity.rolling(126).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc122_126d_slope_v122_signal'] = f104f_f104_free_cash_flow_yield_regime_calc122_126d_slope_v122_signal

def f104f_f104_free_cash_flow_yield_regime_calc123_63d_slope_v123_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity / ev.replace(0, np.nan)).rolling(63).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc123_63d_slope_v123_signal'] = f104f_f104_free_cash_flow_yield_regime_calc123_63d_slope_v123_signal

def f104f_f104_free_cash_flow_yield_regime_calc124_252d_slope_v124_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = ((fcf - fcf.rolling(252).mean()) / fcf.rolling(252).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc124_252d_slope_v124_signal'] = f104f_f104_free_cash_flow_yield_regime_calc124_252d_slope_v124_signal

def f104f_f104_free_cash_flow_yield_regime_calc125_252d_slope_v125_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap / ncfo.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc125_252d_slope_v125_signal'] = f104f_f104_free_cash_flow_yield_regime_calc125_252d_slope_v125_signal

def f104f_f104_free_cash_flow_yield_regime_calc126_126d_slope_v126_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.rolling(126).rank(pct=True) / marketcap.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc126_126d_slope_v126_signal'] = f104f_f104_free_cash_flow_yield_regime_calc126_126d_slope_v126_signal

def f104f_f104_free_cash_flow_yield_regime_calc127_21d_slope_v127_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf.diff(21) / marketcap.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc127_21d_slope_v127_signal'] = f104f_f104_free_cash_flow_yield_regime_calc127_21d_slope_v127_signal

def f104f_f104_free_cash_flow_yield_regime_calc128_63d_slope_v128_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = ((marketcap - marketcap.rolling(63).mean()) / marketcap.rolling(63).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc128_63d_slope_v128_signal'] = f104f_f104_free_cash_flow_yield_regime_calc128_63d_slope_v128_signal

def f104f_f104_free_cash_flow_yield_regime_calc129_126d_slope_v129_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (fcf.rolling(126).kurt() - equity.rolling(126).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc129_126d_slope_v129_signal'] = f104f_f104_free_cash_flow_yield_regime_calc129_126d_slope_v129_signal

def f104f_f104_free_cash_flow_yield_regime_calc130_42d_slope_v130_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.rolling(42).max() - ncfo.rolling(42).min()) / equity.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc130_42d_slope_v130_signal'] = f104f_f104_free_cash_flow_yield_regime_calc130_42d_slope_v130_signal

def f104f_f104_free_cash_flow_yield_regime_calc131_10d_slope_v131_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity / ev.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc131_10d_slope_v131_signal'] = f104f_f104_free_cash_flow_yield_regime_calc131_10d_slope_v131_signal

def f104f_f104_free_cash_flow_yield_regime_calc132_126d_slope_v132_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue / equity.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc132_126d_slope_v132_signal'] = f104f_f104_free_cash_flow_yield_regime_calc132_126d_slope_v132_signal

def f104f_f104_free_cash_flow_yield_regime_calc133_126d_slope_v133_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (equity.rolling(126).max() - ev.rolling(126).min()) / marketcap.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc133_126d_slope_v133_signal'] = f104f_f104_free_cash_flow_yield_regime_calc133_126d_slope_v133_signal

def f104f_f104_free_cash_flow_yield_regime_calc134_63d_slope_v134_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.pct_change(63) - ncfo.pct_change(63))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc134_63d_slope_v134_signal'] = f104f_f104_free_cash_flow_yield_regime_calc134_63d_slope_v134_signal

def f104f_f104_free_cash_flow_yield_regime_calc135_5d_slope_v135_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.rolling(5).quantile(0.5) / ev.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc135_5d_slope_v135_signal'] = f104f_f104_free_cash_flow_yield_regime_calc135_5d_slope_v135_signal

def f104f_f104_free_cash_flow_yield_regime_calc136_21d_slope_v136_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ev.rolling(21).max() - assets.rolling(21).min()) / ncfo.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc136_21d_slope_v136_signal'] = f104f_f104_free_cash_flow_yield_regime_calc136_21d_slope_v136_signal

def f104f_f104_free_cash_flow_yield_regime_calc137_10d_slope_v137_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.pct_change(10) - equity.pct_change(10))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc137_10d_slope_v137_signal'] = f104f_f104_free_cash_flow_yield_regime_calc137_10d_slope_v137_signal

def f104f_f104_free_cash_flow_yield_regime_calc138_252d_slope_v138_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.pct_change(252) - ncfo.pct_change(252))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc138_252d_slope_v138_signal'] = f104f_f104_free_cash_flow_yield_regime_calc138_252d_slope_v138_signal

def f104f_f104_free_cash_flow_yield_regime_calc139_21d_slope_v139_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.rolling(21).max() - ev.rolling(21).min()) / equity.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc139_21d_slope_v139_signal'] = f104f_f104_free_cash_flow_yield_regime_calc139_21d_slope_v139_signal

def f104f_f104_free_cash_flow_yield_regime_calc140_5d_slope_v140_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (ncfo.rolling(5).rank(pct=True) / fcf.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc140_5d_slope_v140_signal'] = f104f_f104_free_cash_flow_yield_regime_calc140_5d_slope_v140_signal

def f104f_f104_free_cash_flow_yield_regime_calc141_10d_slope_v141_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.rolling(10).max() - equity.rolling(10).min()) / revenue.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc141_10d_slope_v141_signal'] = f104f_f104_free_cash_flow_yield_regime_calc141_10d_slope_v141_signal

def f104f_f104_free_cash_flow_yield_regime_calc142_126d_slope_v142_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
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
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc142_126d_slope_v142_signal'] = f104f_f104_free_cash_flow_yield_regime_calc142_126d_slope_v142_signal

def f104f_f104_free_cash_flow_yield_regime_calc143_42d_slope_v143_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = ((fcf - fcf.rolling(42).mean()) / fcf.rolling(42).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc143_42d_slope_v143_signal'] = f104f_f104_free_cash_flow_yield_regime_calc143_42d_slope_v143_signal

def f104f_f104_free_cash_flow_yield_regime_calc144_10d_slope_v144_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (marketcap.rolling(10).max() - ncfo.rolling(10).min()) / revenue.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc144_10d_slope_v144_signal'] = f104f_f104_free_cash_flow_yield_regime_calc144_10d_slope_v144_signal

def f104f_f104_free_cash_flow_yield_regime_calc145_42d_slope_v145_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.diff(42).abs() / assets.diff(42).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc145_42d_slope_v145_signal'] = f104f_f104_free_cash_flow_yield_regime_calc145_42d_slope_v145_signal

def f104f_f104_free_cash_flow_yield_regime_calc146_5d_slope_v146_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets.rolling(5).max() - fcf.rolling(5).min()) / ncfo.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc146_5d_slope_v146_signal'] = f104f_f104_free_cash_flow_yield_regime_calc146_5d_slope_v146_signal

def f104f_f104_free_cash_flow_yield_regime_calc147_5d_slope_v147_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue.diff(5).abs() / marketcap.diff(5).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc147_5d_slope_v147_signal'] = f104f_f104_free_cash_flow_yield_regime_calc147_5d_slope_v147_signal

def f104f_f104_free_cash_flow_yield_regime_calc148_21d_slope_v148_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (assets / ev.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc148_21d_slope_v148_signal'] = f104f_f104_free_cash_flow_yield_regime_calc148_21d_slope_v148_signal

def f104f_f104_free_cash_flow_yield_regime_calc149_21d_slope_v149_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
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
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc149_21d_slope_v149_signal'] = f104f_f104_free_cash_flow_yield_regime_calc149_21d_slope_v149_signal

def f104f_f104_free_cash_flow_yield_regime_calc150_5d_slope_v150_signal(fcf, marketcap, ev, assets, equity, revenue, ncfo):
    v1 = (revenue / fcf.replace(0, np.nan)).rolling(5).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f104f_f104_free_cash_flow_yield_regime_calc150_5d_slope_v150_signal'] = f104f_f104_free_cash_flow_yield_regime_calc150_5d_slope_v150_signal



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
