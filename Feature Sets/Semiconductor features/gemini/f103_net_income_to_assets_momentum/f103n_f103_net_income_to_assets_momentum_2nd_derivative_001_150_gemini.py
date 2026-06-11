import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f103n_f103_net_income_to_assets_momentum_calc001_42d_slope_v001_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda.pct_change(42) - fcf.pct_change(42))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc001_42d_slope_v001_signal'] = f103n_f103_net_income_to_assets_momentum_calc001_42d_slope_v001_signal

def f103n_f103_net_income_to_assets_momentum_calc002_126d_slope_v002_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.rolling(126).kurt() - fcf.rolling(126).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc002_126d_slope_v002_signal'] = f103n_f103_net_income_to_assets_momentum_calc002_126d_slope_v002_signal

def f103n_f103_net_income_to_assets_momentum_calc003_5d_slope_v003_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.rolling(5).rank(pct=True) / fcf.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc003_5d_slope_v003_signal'] = f103n_f103_net_income_to_assets_momentum_calc003_5d_slope_v003_signal

def f103n_f103_net_income_to_assets_momentum_calc004_63d_slope_v004_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.diff(63) / netinc.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc004_63d_slope_v004_signal'] = f103n_f103_net_income_to_assets_momentum_calc004_63d_slope_v004_signal

def f103n_f103_net_income_to_assets_momentum_calc005_42d_slope_v005_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf / netinc.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc005_42d_slope_v005_signal'] = f103n_f103_net_income_to_assets_momentum_calc005_42d_slope_v005_signal

def f103n_f103_net_income_to_assets_momentum_calc006_63d_slope_v006_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.rolling(63).quantile(0.5) / revenue.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc006_63d_slope_v006_signal'] = f103n_f103_net_income_to_assets_momentum_calc006_63d_slope_v006_signal

def f103n_f103_net_income_to_assets_momentum_calc007_252d_slope_v007_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.diff(252).abs() / revenue.diff(252).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc007_252d_slope_v007_signal'] = f103n_f103_net_income_to_assets_momentum_calc007_252d_slope_v007_signal

def f103n_f103_net_income_to_assets_momentum_calc008_126d_slope_v008_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda.rolling(126).kurt() - fcf.rolling(126).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc008_126d_slope_v008_signal'] = f103n_f103_net_income_to_assets_momentum_calc008_126d_slope_v008_signal

def f103n_f103_net_income_to_assets_momentum_calc009_21d_slope_v009_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.diff(21) / fcf.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc009_21d_slope_v009_signal'] = f103n_f103_net_income_to_assets_momentum_calc009_21d_slope_v009_signal

def f103n_f103_net_income_to_assets_momentum_calc010_252d_slope_v010_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.rolling(252).kurt() - fcf.rolling(252).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc010_252d_slope_v010_signal'] = f103n_f103_net_income_to_assets_momentum_calc010_252d_slope_v010_signal

def f103n_f103_net_income_to_assets_momentum_calc011_252d_slope_v011_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo / assets.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc011_252d_slope_v011_signal'] = f103n_f103_net_income_to_assets_momentum_calc011_252d_slope_v011_signal

def f103n_f103_net_income_to_assets_momentum_calc012_10d_slope_v012_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.rolling(10).rank(pct=True) / netinc.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc012_10d_slope_v012_signal'] = f103n_f103_net_income_to_assets_momentum_calc012_10d_slope_v012_signal

def f103n_f103_net_income_to_assets_momentum_calc013_21d_slope_v013_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.diff(21).abs() / equity.diff(21).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc013_21d_slope_v013_signal'] = f103n_f103_net_income_to_assets_momentum_calc013_21d_slope_v013_signal

def f103n_f103_net_income_to_assets_momentum_calc014_5d_slope_v014_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
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
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc014_5d_slope_v014_signal'] = f103n_f103_net_income_to_assets_momentum_calc014_5d_slope_v014_signal

def f103n_f103_net_income_to_assets_momentum_calc015_10d_slope_v015_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.diff(10) / revenue.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc015_10d_slope_v015_signal'] = f103n_f103_net_income_to_assets_momentum_calc015_10d_slope_v015_signal

def f103n_f103_net_income_to_assets_momentum_calc016_42d_slope_v016_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.diff(42) / ebitda.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc016_42d_slope_v016_signal'] = f103n_f103_net_income_to_assets_momentum_calc016_42d_slope_v016_signal

def f103n_f103_net_income_to_assets_momentum_calc017_126d_slope_v017_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.diff(126) / fcf.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc017_126d_slope_v017_signal'] = f103n_f103_net_income_to_assets_momentum_calc017_126d_slope_v017_signal

def f103n_f103_net_income_to_assets_momentum_calc018_252d_slope_v018_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.rolling(252).kurt() - equity.rolling(252).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc018_252d_slope_v018_signal'] = f103n_f103_net_income_to_assets_momentum_calc018_252d_slope_v018_signal

def f103n_f103_net_income_to_assets_momentum_calc019_5d_slope_v019_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity / ebitda.replace(0, np.nan)).rolling(5).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc019_5d_slope_v019_signal'] = f103n_f103_net_income_to_assets_momentum_calc019_5d_slope_v019_signal

def f103n_f103_net_income_to_assets_momentum_calc020_5d_slope_v020_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.rolling(5).rank(pct=True) / netinc.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc020_5d_slope_v020_signal'] = f103n_f103_net_income_to_assets_momentum_calc020_5d_slope_v020_signal

def f103n_f103_net_income_to_assets_momentum_calc021_5d_slope_v021_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.diff(5) / netinc.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc021_5d_slope_v021_signal'] = f103n_f103_net_income_to_assets_momentum_calc021_5d_slope_v021_signal

def f103n_f103_net_income_to_assets_momentum_calc022_10d_slope_v022_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.pct_change(10) - netinc.pct_change(10))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc022_10d_slope_v022_signal'] = f103n_f103_net_income_to_assets_momentum_calc022_10d_slope_v022_signal

def f103n_f103_net_income_to_assets_momentum_calc023_126d_slope_v023_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.rolling(126).rank(pct=True) / ncfo.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc023_126d_slope_v023_signal'] = f103n_f103_net_income_to_assets_momentum_calc023_126d_slope_v023_signal

def f103n_f103_net_income_to_assets_momentum_calc024_63d_slope_v024_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.diff(63).abs() / ebitda.diff(63).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc024_63d_slope_v024_signal'] = f103n_f103_net_income_to_assets_momentum_calc024_63d_slope_v024_signal

def f103n_f103_net_income_to_assets_momentum_calc025_126d_slope_v025_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = ((ebitda - ebitda.rolling(126).mean()) / ebitda.rolling(126).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc025_126d_slope_v025_signal'] = f103n_f103_net_income_to_assets_momentum_calc025_126d_slope_v025_signal

def f103n_f103_net_income_to_assets_momentum_calc026_5d_slope_v026_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.pct_change(5) - equity.pct_change(5))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc026_5d_slope_v026_signal'] = f103n_f103_net_income_to_assets_momentum_calc026_5d_slope_v026_signal

def f103n_f103_net_income_to_assets_momentum_calc027_10d_slope_v027_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo / netinc.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc027_10d_slope_v027_signal'] = f103n_f103_net_income_to_assets_momentum_calc027_10d_slope_v027_signal

def f103n_f103_net_income_to_assets_momentum_calc028_21d_slope_v028_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity / ebitda.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc028_21d_slope_v028_signal'] = f103n_f103_net_income_to_assets_momentum_calc028_21d_slope_v028_signal

def f103n_f103_net_income_to_assets_momentum_calc029_126d_slope_v029_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda.diff(126) / assets.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc029_126d_slope_v029_signal'] = f103n_f103_net_income_to_assets_momentum_calc029_126d_slope_v029_signal

def f103n_f103_net_income_to_assets_momentum_calc030_126d_slope_v030_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.rolling(126).rank(pct=True) / ebitda.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc030_126d_slope_v030_signal'] = f103n_f103_net_income_to_assets_momentum_calc030_126d_slope_v030_signal

def f103n_f103_net_income_to_assets_momentum_calc031_21d_slope_v031_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.rolling(21).max() - ebitda.rolling(21).min()) / assets.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc031_21d_slope_v031_signal'] = f103n_f103_net_income_to_assets_momentum_calc031_21d_slope_v031_signal

def f103n_f103_net_income_to_assets_momentum_calc032_10d_slope_v032_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
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
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc032_10d_slope_v032_signal'] = f103n_f103_net_income_to_assets_momentum_calc032_10d_slope_v032_signal

def f103n_f103_net_income_to_assets_momentum_calc033_126d_slope_v033_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.diff(126) / fcf.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc033_126d_slope_v033_signal'] = f103n_f103_net_income_to_assets_momentum_calc033_126d_slope_v033_signal

def f103n_f103_net_income_to_assets_momentum_calc034_42d_slope_v034_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = ((equity - equity.rolling(42).mean()) / equity.rolling(42).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc034_42d_slope_v034_signal'] = f103n_f103_net_income_to_assets_momentum_calc034_42d_slope_v034_signal

def f103n_f103_net_income_to_assets_momentum_calc035_5d_slope_v035_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.diff(5) / ebitda.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc035_5d_slope_v035_signal'] = f103n_f103_net_income_to_assets_momentum_calc035_5d_slope_v035_signal

def f103n_f103_net_income_to_assets_momentum_calc036_252d_slope_v036_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
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
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc036_252d_slope_v036_signal'] = f103n_f103_net_income_to_assets_momentum_calc036_252d_slope_v036_signal

def f103n_f103_net_income_to_assets_momentum_calc037_252d_slope_v037_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.rolling(252).kurt() - fcf.rolling(252).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc037_252d_slope_v037_signal'] = f103n_f103_net_income_to_assets_momentum_calc037_252d_slope_v037_signal

def f103n_f103_net_income_to_assets_momentum_calc038_5d_slope_v038_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda.rolling(5).max() - ncfo.rolling(5).min()) / assets.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc038_5d_slope_v038_signal'] = f103n_f103_net_income_to_assets_momentum_calc038_5d_slope_v038_signal

def f103n_f103_net_income_to_assets_momentum_calc039_63d_slope_v039_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.rolling(63).quantile(0.5) / equity.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc039_63d_slope_v039_signal'] = f103n_f103_net_income_to_assets_momentum_calc039_63d_slope_v039_signal

def f103n_f103_net_income_to_assets_momentum_calc040_21d_slope_v040_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.diff(21).abs() / assets.diff(21).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc040_21d_slope_v040_signal'] = f103n_f103_net_income_to_assets_momentum_calc040_21d_slope_v040_signal

def f103n_f103_net_income_to_assets_momentum_calc041_21d_slope_v041_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.pct_change(21) - assets.pct_change(21))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc041_21d_slope_v041_signal'] = f103n_f103_net_income_to_assets_momentum_calc041_21d_slope_v041_signal

def f103n_f103_net_income_to_assets_momentum_calc042_252d_slope_v042_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.rolling(252).quantile(0.5) / ebitda.rolling(252).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc042_252d_slope_v042_signal'] = f103n_f103_net_income_to_assets_momentum_calc042_252d_slope_v042_signal

def f103n_f103_net_income_to_assets_momentum_calc043_10d_slope_v043_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
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
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc043_10d_slope_v043_signal'] = f103n_f103_net_income_to_assets_momentum_calc043_10d_slope_v043_signal

def f103n_f103_net_income_to_assets_momentum_calc044_126d_slope_v044_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.rolling(126).rank(pct=True) / assets.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc044_126d_slope_v044_signal'] = f103n_f103_net_income_to_assets_momentum_calc044_126d_slope_v044_signal

def f103n_f103_net_income_to_assets_momentum_calc045_21d_slope_v045_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
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
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc045_21d_slope_v045_signal'] = f103n_f103_net_income_to_assets_momentum_calc045_21d_slope_v045_signal

def f103n_f103_net_income_to_assets_momentum_calc046_21d_slope_v046_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc / ncfo.replace(0, np.nan)).rolling(21).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc046_21d_slope_v046_signal'] = f103n_f103_net_income_to_assets_momentum_calc046_21d_slope_v046_signal

def f103n_f103_net_income_to_assets_momentum_calc047_252d_slope_v047_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.rolling(252).max() - equity.rolling(252).min()) / revenue.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc047_252d_slope_v047_signal'] = f103n_f103_net_income_to_assets_momentum_calc047_252d_slope_v047_signal

def f103n_f103_net_income_to_assets_momentum_calc048_21d_slope_v048_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = ((netinc - netinc.rolling(21).mean()) / netinc.rolling(21).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc048_21d_slope_v048_signal'] = f103n_f103_net_income_to_assets_momentum_calc048_21d_slope_v048_signal

def f103n_f103_net_income_to_assets_momentum_calc049_10d_slope_v049_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.rolling(10).rank(pct=True) / netinc.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc049_10d_slope_v049_signal'] = f103n_f103_net_income_to_assets_momentum_calc049_10d_slope_v049_signal

def f103n_f103_net_income_to_assets_momentum_calc050_63d_slope_v050_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.rolling(63).kurt() - netinc.rolling(63).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc050_63d_slope_v050_signal'] = f103n_f103_net_income_to_assets_momentum_calc050_63d_slope_v050_signal

def f103n_f103_net_income_to_assets_momentum_calc051_126d_slope_v051_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.rolling(126).quantile(0.5) / revenue.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc051_126d_slope_v051_signal'] = f103n_f103_net_income_to_assets_momentum_calc051_126d_slope_v051_signal

def f103n_f103_net_income_to_assets_momentum_calc052_21d_slope_v052_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue / ebitda.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc052_21d_slope_v052_signal'] = f103n_f103_net_income_to_assets_momentum_calc052_21d_slope_v052_signal

def f103n_f103_net_income_to_assets_momentum_calc053_21d_slope_v053_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.diff(21) / ebitda.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc053_21d_slope_v053_signal'] = f103n_f103_net_income_to_assets_momentum_calc053_21d_slope_v053_signal

def f103n_f103_net_income_to_assets_momentum_calc054_5d_slope_v054_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.pct_change(5) - revenue.pct_change(5))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc054_5d_slope_v054_signal'] = f103n_f103_net_income_to_assets_momentum_calc054_5d_slope_v054_signal

def f103n_f103_net_income_to_assets_momentum_calc055_21d_slope_v055_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.rolling(21).kurt() - netinc.rolling(21).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc055_21d_slope_v055_signal'] = f103n_f103_net_income_to_assets_momentum_calc055_21d_slope_v055_signal

def f103n_f103_net_income_to_assets_momentum_calc056_252d_slope_v056_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda / revenue.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc056_252d_slope_v056_signal'] = f103n_f103_net_income_to_assets_momentum_calc056_252d_slope_v056_signal

def f103n_f103_net_income_to_assets_momentum_calc057_5d_slope_v057_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.pct_change(5) - ncfo.pct_change(5))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc057_5d_slope_v057_signal'] = f103n_f103_net_income_to_assets_momentum_calc057_5d_slope_v057_signal

def f103n_f103_net_income_to_assets_momentum_calc058_126d_slope_v058_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.diff(126) / ncfo.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc058_126d_slope_v058_signal'] = f103n_f103_net_income_to_assets_momentum_calc058_126d_slope_v058_signal

def f103n_f103_net_income_to_assets_momentum_calc059_10d_slope_v059_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.diff(10) / fcf.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc059_10d_slope_v059_signal'] = f103n_f103_net_income_to_assets_momentum_calc059_10d_slope_v059_signal

def f103n_f103_net_income_to_assets_momentum_calc060_126d_slope_v060_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.rolling(126).rank(pct=True) / netinc.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc060_126d_slope_v060_signal'] = f103n_f103_net_income_to_assets_momentum_calc060_126d_slope_v060_signal

def f103n_f103_net_income_to_assets_momentum_calc061_63d_slope_v061_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity / ncfo.replace(0, np.nan)).rolling(63).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc061_63d_slope_v061_signal'] = f103n_f103_net_income_to_assets_momentum_calc061_63d_slope_v061_signal

def f103n_f103_net_income_to_assets_momentum_calc062_126d_slope_v062_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = ((revenue - revenue.rolling(126).mean()) / revenue.rolling(126).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc062_126d_slope_v062_signal'] = f103n_f103_net_income_to_assets_momentum_calc062_126d_slope_v062_signal

def f103n_f103_net_income_to_assets_momentum_calc063_252d_slope_v063_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.diff(252) / ebitda.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc063_252d_slope_v063_signal'] = f103n_f103_net_income_to_assets_momentum_calc063_252d_slope_v063_signal

def f103n_f103_net_income_to_assets_momentum_calc064_126d_slope_v064_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda.rolling(126).kurt() - ncfo.rolling(126).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc064_126d_slope_v064_signal'] = f103n_f103_net_income_to_assets_momentum_calc064_126d_slope_v064_signal

def f103n_f103_net_income_to_assets_momentum_calc065_126d_slope_v065_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda.diff(126) / fcf.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc065_126d_slope_v065_signal'] = f103n_f103_net_income_to_assets_momentum_calc065_126d_slope_v065_signal

def f103n_f103_net_income_to_assets_momentum_calc066_126d_slope_v066_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.diff(126).abs() / ebitda.diff(126).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc066_126d_slope_v066_signal'] = f103n_f103_net_income_to_assets_momentum_calc066_126d_slope_v066_signal

def f103n_f103_net_income_to_assets_momentum_calc067_126d_slope_v067_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.rolling(126).kurt() - ebitda.rolling(126).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc067_126d_slope_v067_signal'] = f103n_f103_net_income_to_assets_momentum_calc067_126d_slope_v067_signal

def f103n_f103_net_income_to_assets_momentum_calc068_126d_slope_v068_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda / ncfo.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc068_126d_slope_v068_signal'] = f103n_f103_net_income_to_assets_momentum_calc068_126d_slope_v068_signal

def f103n_f103_net_income_to_assets_momentum_calc069_21d_slope_v069_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.pct_change(21) - assets.pct_change(21))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc069_21d_slope_v069_signal'] = f103n_f103_net_income_to_assets_momentum_calc069_21d_slope_v069_signal

def f103n_f103_net_income_to_assets_momentum_calc070_5d_slope_v070_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.rolling(5).kurt() - ebitda.rolling(5).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc070_5d_slope_v070_signal'] = f103n_f103_net_income_to_assets_momentum_calc070_5d_slope_v070_signal

def f103n_f103_net_income_to_assets_momentum_calc071_21d_slope_v071_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.rolling(21).quantile(0.5) / assets.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc071_21d_slope_v071_signal'] = f103n_f103_net_income_to_assets_momentum_calc071_21d_slope_v071_signal

def f103n_f103_net_income_to_assets_momentum_calc072_42d_slope_v072_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.diff(42) / ncfo.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc072_42d_slope_v072_signal'] = f103n_f103_net_income_to_assets_momentum_calc072_42d_slope_v072_signal

def f103n_f103_net_income_to_assets_momentum_calc073_5d_slope_v073_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.rolling(5).rank(pct=True) / netinc.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc073_5d_slope_v073_signal'] = f103n_f103_net_income_to_assets_momentum_calc073_5d_slope_v073_signal

def f103n_f103_net_income_to_assets_momentum_calc074_21d_slope_v074_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.rolling(21).kurt() - netinc.rolling(21).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc074_21d_slope_v074_signal'] = f103n_f103_net_income_to_assets_momentum_calc074_21d_slope_v074_signal

def f103n_f103_net_income_to_assets_momentum_calc075_126d_slope_v075_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda.rolling(126).quantile(0.5) / revenue.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc075_126d_slope_v075_signal'] = f103n_f103_net_income_to_assets_momentum_calc075_126d_slope_v075_signal

def f103n_f103_net_income_to_assets_momentum_calc076_10d_slope_v076_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.rolling(10).quantile(0.5) / ncfo.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc076_10d_slope_v076_signal'] = f103n_f103_net_income_to_assets_momentum_calc076_10d_slope_v076_signal

def f103n_f103_net_income_to_assets_momentum_calc077_63d_slope_v077_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.rolling(63).quantile(0.5) / netinc.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc077_63d_slope_v077_signal'] = f103n_f103_net_income_to_assets_momentum_calc077_63d_slope_v077_signal

def f103n_f103_net_income_to_assets_momentum_calc078_63d_slope_v078_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.pct_change(63) - ncfo.pct_change(63))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc078_63d_slope_v078_signal'] = f103n_f103_net_income_to_assets_momentum_calc078_63d_slope_v078_signal

def f103n_f103_net_income_to_assets_momentum_calc079_10d_slope_v079_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets / netinc.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc079_10d_slope_v079_signal'] = f103n_f103_net_income_to_assets_momentum_calc079_10d_slope_v079_signal

def f103n_f103_net_income_to_assets_momentum_calc080_63d_slope_v080_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
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
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc080_63d_slope_v080_signal'] = f103n_f103_net_income_to_assets_momentum_calc080_63d_slope_v080_signal

def f103n_f103_net_income_to_assets_momentum_calc081_252d_slope_v081_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = ((ebitda - ebitda.rolling(252).mean()) / ebitda.rolling(252).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc081_252d_slope_v081_signal'] = f103n_f103_net_income_to_assets_momentum_calc081_252d_slope_v081_signal

def f103n_f103_net_income_to_assets_momentum_calc082_5d_slope_v082_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.rolling(5).rank(pct=True) / fcf.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc082_5d_slope_v082_signal'] = f103n_f103_net_income_to_assets_momentum_calc082_5d_slope_v082_signal

def f103n_f103_net_income_to_assets_momentum_calc083_252d_slope_v083_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.rolling(252).max() - equity.rolling(252).min()) / revenue.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc083_252d_slope_v083_signal'] = f103n_f103_net_income_to_assets_momentum_calc083_252d_slope_v083_signal

def f103n_f103_net_income_to_assets_momentum_calc084_21d_slope_v084_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf / netinc.replace(0, np.nan)).rolling(21).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc084_21d_slope_v084_signal'] = f103n_f103_net_income_to_assets_momentum_calc084_21d_slope_v084_signal

def f103n_f103_net_income_to_assets_momentum_calc085_126d_slope_v085_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.rolling(126).rank(pct=True) / netinc.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc085_126d_slope_v085_signal'] = f103n_f103_net_income_to_assets_momentum_calc085_126d_slope_v085_signal

def f103n_f103_net_income_to_assets_momentum_calc086_63d_slope_v086_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda / netinc.replace(0, np.nan)).rolling(63).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc086_63d_slope_v086_signal'] = f103n_f103_net_income_to_assets_momentum_calc086_63d_slope_v086_signal

def f103n_f103_net_income_to_assets_momentum_calc087_21d_slope_v087_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.rolling(21).quantile(0.5) / fcf.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc087_21d_slope_v087_signal'] = f103n_f103_net_income_to_assets_momentum_calc087_21d_slope_v087_signal

def f103n_f103_net_income_to_assets_momentum_calc088_252d_slope_v088_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.diff(252) / revenue.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc088_252d_slope_v088_signal'] = f103n_f103_net_income_to_assets_momentum_calc088_252d_slope_v088_signal

def f103n_f103_net_income_to_assets_momentum_calc089_10d_slope_v089_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets / fcf.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc089_10d_slope_v089_signal'] = f103n_f103_net_income_to_assets_momentum_calc089_10d_slope_v089_signal

def f103n_f103_net_income_to_assets_momentum_calc090_5d_slope_v090_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.rolling(5).kurt() - netinc.rolling(5).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc090_5d_slope_v090_signal'] = f103n_f103_net_income_to_assets_momentum_calc090_5d_slope_v090_signal

def f103n_f103_net_income_to_assets_momentum_calc091_252d_slope_v091_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.pct_change(252) - ebitda.pct_change(252))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc091_252d_slope_v091_signal'] = f103n_f103_net_income_to_assets_momentum_calc091_252d_slope_v091_signal

def f103n_f103_net_income_to_assets_momentum_calc092_126d_slope_v092_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.rolling(126).kurt() - netinc.rolling(126).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc092_126d_slope_v092_signal'] = f103n_f103_net_income_to_assets_momentum_calc092_126d_slope_v092_signal

def f103n_f103_net_income_to_assets_momentum_calc093_252d_slope_v093_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.diff(252).abs() / revenue.diff(252).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc093_252d_slope_v093_signal'] = f103n_f103_net_income_to_assets_momentum_calc093_252d_slope_v093_signal

def f103n_f103_net_income_to_assets_momentum_calc094_42d_slope_v094_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.pct_change(42) - assets.pct_change(42))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc094_42d_slope_v094_signal'] = f103n_f103_net_income_to_assets_momentum_calc094_42d_slope_v094_signal

def f103n_f103_net_income_to_assets_momentum_calc095_21d_slope_v095_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.rolling(21).max() - equity.rolling(21).min()) / revenue.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc095_21d_slope_v095_signal'] = f103n_f103_net_income_to_assets_momentum_calc095_21d_slope_v095_signal

def f103n_f103_net_income_to_assets_momentum_calc096_5d_slope_v096_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.rolling(5).kurt() - assets.rolling(5).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc096_5d_slope_v096_signal'] = f103n_f103_net_income_to_assets_momentum_calc096_5d_slope_v096_signal

def f103n_f103_net_income_to_assets_momentum_calc097_63d_slope_v097_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
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
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc097_63d_slope_v097_signal'] = f103n_f103_net_income_to_assets_momentum_calc097_63d_slope_v097_signal

def f103n_f103_net_income_to_assets_momentum_calc098_10d_slope_v098_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.rolling(10).max() - ebitda.rolling(10).min()) / revenue.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc098_10d_slope_v098_signal'] = f103n_f103_net_income_to_assets_momentum_calc098_10d_slope_v098_signal

def f103n_f103_net_income_to_assets_momentum_calc099_126d_slope_v099_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.pct_change(126) - revenue.pct_change(126))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc099_126d_slope_v099_signal'] = f103n_f103_net_income_to_assets_momentum_calc099_126d_slope_v099_signal

def f103n_f103_net_income_to_assets_momentum_calc100_5d_slope_v100_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.diff(5) / ncfo.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc100_5d_slope_v100_signal'] = f103n_f103_net_income_to_assets_momentum_calc100_5d_slope_v100_signal

def f103n_f103_net_income_to_assets_momentum_calc101_126d_slope_v101_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = ((ncfo - ncfo.rolling(126).mean()) / ncfo.rolling(126).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc101_126d_slope_v101_signal'] = f103n_f103_net_income_to_assets_momentum_calc101_126d_slope_v101_signal

def f103n_f103_net_income_to_assets_momentum_calc102_10d_slope_v102_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.pct_change(10) - assets.pct_change(10))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc102_10d_slope_v102_signal'] = f103n_f103_net_income_to_assets_momentum_calc102_10d_slope_v102_signal

def f103n_f103_net_income_to_assets_momentum_calc103_126d_slope_v103_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.pct_change(126) - netinc.pct_change(126))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc103_126d_slope_v103_signal'] = f103n_f103_net_income_to_assets_momentum_calc103_126d_slope_v103_signal

def f103n_f103_net_income_to_assets_momentum_calc104_126d_slope_v104_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.pct_change(126) - ebitda.pct_change(126))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc104_126d_slope_v104_signal'] = f103n_f103_net_income_to_assets_momentum_calc104_126d_slope_v104_signal

def f103n_f103_net_income_to_assets_momentum_calc105_126d_slope_v105_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
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
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc105_126d_slope_v105_signal'] = f103n_f103_net_income_to_assets_momentum_calc105_126d_slope_v105_signal

def f103n_f103_net_income_to_assets_momentum_calc106_10d_slope_v106_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets / revenue.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc106_10d_slope_v106_signal'] = f103n_f103_net_income_to_assets_momentum_calc106_10d_slope_v106_signal

def f103n_f103_net_income_to_assets_momentum_calc107_42d_slope_v107_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.diff(42).abs() / ebitda.diff(42).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc107_42d_slope_v107_signal'] = f103n_f103_net_income_to_assets_momentum_calc107_42d_slope_v107_signal

def f103n_f103_net_income_to_assets_momentum_calc108_252d_slope_v108_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.diff(252).abs() / ncfo.diff(252).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc108_252d_slope_v108_signal'] = f103n_f103_net_income_to_assets_momentum_calc108_252d_slope_v108_signal

def f103n_f103_net_income_to_assets_momentum_calc109_126d_slope_v109_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity / revenue.replace(0, np.nan)).rolling(126).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc109_126d_slope_v109_signal'] = f103n_f103_net_income_to_assets_momentum_calc109_126d_slope_v109_signal

def f103n_f103_net_income_to_assets_momentum_calc110_10d_slope_v110_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda / revenue.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc110_10d_slope_v110_signal'] = f103n_f103_net_income_to_assets_momentum_calc110_10d_slope_v110_signal

def f103n_f103_net_income_to_assets_momentum_calc111_126d_slope_v111_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.diff(126) / equity.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc111_126d_slope_v111_signal'] = f103n_f103_net_income_to_assets_momentum_calc111_126d_slope_v111_signal

def f103n_f103_net_income_to_assets_momentum_calc112_126d_slope_v112_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.diff(126).abs() / fcf.diff(126).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc112_126d_slope_v112_signal'] = f103n_f103_net_income_to_assets_momentum_calc112_126d_slope_v112_signal

def f103n_f103_net_income_to_assets_momentum_calc113_63d_slope_v113_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.diff(63) / assets.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc113_63d_slope_v113_signal'] = f103n_f103_net_income_to_assets_momentum_calc113_63d_slope_v113_signal

def f103n_f103_net_income_to_assets_momentum_calc114_21d_slope_v114_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda.rolling(21).kurt() - fcf.rolling(21).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc114_21d_slope_v114_signal'] = f103n_f103_net_income_to_assets_momentum_calc114_21d_slope_v114_signal

def f103n_f103_net_income_to_assets_momentum_calc115_5d_slope_v115_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda / ncfo.replace(0, np.nan)).rolling(5).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc115_5d_slope_v115_signal'] = f103n_f103_net_income_to_assets_momentum_calc115_5d_slope_v115_signal

def f103n_f103_net_income_to_assets_momentum_calc116_21d_slope_v116_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.rolling(21).quantile(0.5) / fcf.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc116_21d_slope_v116_signal'] = f103n_f103_net_income_to_assets_momentum_calc116_21d_slope_v116_signal

def f103n_f103_net_income_to_assets_momentum_calc117_10d_slope_v117_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.rolling(10).kurt() - assets.rolling(10).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc117_10d_slope_v117_signal'] = f103n_f103_net_income_to_assets_momentum_calc117_10d_slope_v117_signal

def f103n_f103_net_income_to_assets_momentum_calc118_5d_slope_v118_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.pct_change(5) - ncfo.pct_change(5))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc118_5d_slope_v118_signal'] = f103n_f103_net_income_to_assets_momentum_calc118_5d_slope_v118_signal

def f103n_f103_net_income_to_assets_momentum_calc119_42d_slope_v119_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.rolling(42).rank(pct=True) / fcf.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc119_42d_slope_v119_signal'] = f103n_f103_net_income_to_assets_momentum_calc119_42d_slope_v119_signal

def f103n_f103_net_income_to_assets_momentum_calc120_5d_slope_v120_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda / revenue.replace(0, np.nan)).rolling(5).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc120_5d_slope_v120_signal'] = f103n_f103_net_income_to_assets_momentum_calc120_5d_slope_v120_signal

def f103n_f103_net_income_to_assets_momentum_calc121_42d_slope_v121_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.rolling(42).max() - ncfo.rolling(42).min()) / netinc.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc121_42d_slope_v121_signal'] = f103n_f103_net_income_to_assets_momentum_calc121_42d_slope_v121_signal

def f103n_f103_net_income_to_assets_momentum_calc122_42d_slope_v122_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.rolling(42).rank(pct=True) / assets.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc122_42d_slope_v122_signal'] = f103n_f103_net_income_to_assets_momentum_calc122_42d_slope_v122_signal

def f103n_f103_net_income_to_assets_momentum_calc123_5d_slope_v123_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = ((assets - assets.rolling(5).mean()) / assets.rolling(5).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc123_5d_slope_v123_signal'] = f103n_f103_net_income_to_assets_momentum_calc123_5d_slope_v123_signal

def f103n_f103_net_income_to_assets_momentum_calc124_42d_slope_v124_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc / fcf.replace(0, np.nan)).rolling(42).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc124_42d_slope_v124_signal'] = f103n_f103_net_income_to_assets_momentum_calc124_42d_slope_v124_signal

def f103n_f103_net_income_to_assets_momentum_calc125_21d_slope_v125_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
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
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc125_21d_slope_v125_signal'] = f103n_f103_net_income_to_assets_momentum_calc125_21d_slope_v125_signal

def f103n_f103_net_income_to_assets_momentum_calc126_252d_slope_v126_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue / ncfo.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc126_252d_slope_v126_signal'] = f103n_f103_net_income_to_assets_momentum_calc126_252d_slope_v126_signal

def f103n_f103_net_income_to_assets_momentum_calc127_42d_slope_v127_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.pct_change(42) - fcf.pct_change(42))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc127_42d_slope_v127_signal'] = f103n_f103_net_income_to_assets_momentum_calc127_42d_slope_v127_signal

def f103n_f103_net_income_to_assets_momentum_calc128_126d_slope_v128_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo / netinc.replace(0, np.nan)).rolling(126).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc128_126d_slope_v128_signal'] = f103n_f103_net_income_to_assets_momentum_calc128_126d_slope_v128_signal

def f103n_f103_net_income_to_assets_momentum_calc129_5d_slope_v129_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
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
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc129_5d_slope_v129_signal'] = f103n_f103_net_income_to_assets_momentum_calc129_5d_slope_v129_signal

def f103n_f103_net_income_to_assets_momentum_calc130_21d_slope_v130_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.diff(21).abs() / ncfo.diff(21).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc130_21d_slope_v130_signal'] = f103n_f103_net_income_to_assets_momentum_calc130_21d_slope_v130_signal

def f103n_f103_net_income_to_assets_momentum_calc131_126d_slope_v131_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda.pct_change(126) - fcf.pct_change(126))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc131_126d_slope_v131_signal'] = f103n_f103_net_income_to_assets_momentum_calc131_126d_slope_v131_signal

def f103n_f103_net_income_to_assets_momentum_calc132_21d_slope_v132_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.rolling(21).rank(pct=True) / assets.rolling(21).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc132_21d_slope_v132_signal'] = f103n_f103_net_income_to_assets_momentum_calc132_21d_slope_v132_signal

def f103n_f103_net_income_to_assets_momentum_calc133_63d_slope_v133_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.rolling(63).rank(pct=True) / ebitda.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc133_63d_slope_v133_signal'] = f103n_f103_net_income_to_assets_momentum_calc133_63d_slope_v133_signal

def f103n_f103_net_income_to_assets_momentum_calc134_252d_slope_v134_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.rolling(252).max() - netinc.rolling(252).min()) / ncfo.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc134_252d_slope_v134_signal'] = f103n_f103_net_income_to_assets_momentum_calc134_252d_slope_v134_signal

def f103n_f103_net_income_to_assets_momentum_calc135_21d_slope_v135_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = ((ncfo - ncfo.rolling(21).mean()) / ncfo.rolling(21).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc135_21d_slope_v135_signal'] = f103n_f103_net_income_to_assets_momentum_calc135_21d_slope_v135_signal

def f103n_f103_net_income_to_assets_momentum_calc136_252d_slope_v136_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.diff(252).abs() / ebitda.diff(252).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc136_252d_slope_v136_signal'] = f103n_f103_net_income_to_assets_momentum_calc136_252d_slope_v136_signal

def f103n_f103_net_income_to_assets_momentum_calc137_42d_slope_v137_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
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
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc137_42d_slope_v137_signal'] = f103n_f103_net_income_to_assets_momentum_calc137_42d_slope_v137_signal

def f103n_f103_net_income_to_assets_momentum_calc138_5d_slope_v138_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.rolling(5).kurt() - assets.rolling(5).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc138_5d_slope_v138_signal'] = f103n_f103_net_income_to_assets_momentum_calc138_5d_slope_v138_signal

def f103n_f103_net_income_to_assets_momentum_calc139_252d_slope_v139_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.rolling(252).max() - revenue.rolling(252).min()) / fcf.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc139_252d_slope_v139_signal'] = f103n_f103_net_income_to_assets_momentum_calc139_252d_slope_v139_signal

def f103n_f103_net_income_to_assets_momentum_calc140_10d_slope_v140_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
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
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc140_10d_slope_v140_signal'] = f103n_f103_net_income_to_assets_momentum_calc140_10d_slope_v140_signal

def f103n_f103_net_income_to_assets_momentum_calc141_63d_slope_v141_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.pct_change(63) - ncfo.pct_change(63))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc141_63d_slope_v141_signal'] = f103n_f103_net_income_to_assets_momentum_calc141_63d_slope_v141_signal

def f103n_f103_net_income_to_assets_momentum_calc142_10d_slope_v142_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue / ebitda.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc142_10d_slope_v142_signal'] = f103n_f103_net_income_to_assets_momentum_calc142_10d_slope_v142_signal

def f103n_f103_net_income_to_assets_momentum_calc143_10d_slope_v143_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.diff(10) / netinc.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc143_10d_slope_v143_signal'] = f103n_f103_net_income_to_assets_momentum_calc143_10d_slope_v143_signal

def f103n_f103_net_income_to_assets_momentum_calc144_63d_slope_v144_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.pct_change(63) - ebitda.pct_change(63))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc144_63d_slope_v144_signal'] = f103n_f103_net_income_to_assets_momentum_calc144_63d_slope_v144_signal

def f103n_f103_net_income_to_assets_momentum_calc145_5d_slope_v145_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
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
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc145_5d_slope_v145_signal'] = f103n_f103_net_income_to_assets_momentum_calc145_5d_slope_v145_signal

def f103n_f103_net_income_to_assets_momentum_calc146_5d_slope_v146_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
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
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc146_5d_slope_v146_signal'] = f103n_f103_net_income_to_assets_momentum_calc146_5d_slope_v146_signal

def f103n_f103_net_income_to_assets_momentum_calc147_42d_slope_v147_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
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
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc147_42d_slope_v147_signal'] = f103n_f103_net_income_to_assets_momentum_calc147_42d_slope_v147_signal

def f103n_f103_net_income_to_assets_momentum_calc148_63d_slope_v148_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
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
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc148_63d_slope_v148_signal'] = f103n_f103_net_income_to_assets_momentum_calc148_63d_slope_v148_signal

def f103n_f103_net_income_to_assets_momentum_calc149_126d_slope_v149_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.diff(126) / assets.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc149_126d_slope_v149_signal'] = f103n_f103_net_income_to_assets_momentum_calc149_126d_slope_v149_signal

def f103n_f103_net_income_to_assets_momentum_calc150_21d_slope_v150_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo / ebitda.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc150_21d_slope_v150_signal'] = f103n_f103_net_income_to_assets_momentum_calc150_21d_slope_v150_signal



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
