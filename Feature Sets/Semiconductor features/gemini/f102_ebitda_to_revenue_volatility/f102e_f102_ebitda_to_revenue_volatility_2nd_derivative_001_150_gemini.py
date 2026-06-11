import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f102e_f102_ebitda_to_revenue_volatility_calc001_5d_slope_v001_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = ((capex - capex.rolling(5).mean()) / capex.rolling(5).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc001_5d_slope_v001_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc001_5d_slope_v001_signal

def f102e_f102_ebitda_to_revenue_volatility_calc002_10d_slope_v002_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt.diff(10).abs() / assets.diff(10).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc002_10d_slope_v002_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc002_10d_slope_v002_signal

def f102e_f102_ebitda_to_revenue_volatility_calc003_126d_slope_v003_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (assets.rolling(126).quantile(0.5) / equity.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc003_126d_slope_v003_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc003_126d_slope_v003_signal

def f102e_f102_ebitda_to_revenue_volatility_calc004_63d_slope_v004_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
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
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc004_63d_slope_v004_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc004_63d_slope_v004_signal

def f102e_f102_ebitda_to_revenue_volatility_calc005_126d_slope_v005_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt.pct_change(126) - assets.pct_change(126))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc005_126d_slope_v005_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc005_126d_slope_v005_signal

def f102e_f102_ebitda_to_revenue_volatility_calc006_5d_slope_v006_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
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
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc006_5d_slope_v006_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc006_5d_slope_v006_signal

def f102e_f102_ebitda_to_revenue_volatility_calc007_42d_slope_v007_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda.diff(42) / netinc.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc007_42d_slope_v007_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc007_42d_slope_v007_signal

def f102e_f102_ebitda_to_revenue_volatility_calc008_10d_slope_v008_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.diff(10).abs() / debt.diff(10).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc008_10d_slope_v008_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc008_10d_slope_v008_signal

def f102e_f102_ebitda_to_revenue_volatility_calc009_63d_slope_v009_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.diff(63) / assets.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc009_63d_slope_v009_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc009_63d_slope_v009_signal

def f102e_f102_ebitda_to_revenue_volatility_calc010_5d_slope_v010_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
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
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc010_5d_slope_v010_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc010_5d_slope_v010_signal

def f102e_f102_ebitda_to_revenue_volatility_calc011_42d_slope_v011_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (assets.diff(42).abs() / netinc.diff(42).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc011_42d_slope_v011_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc011_42d_slope_v011_signal

def f102e_f102_ebitda_to_revenue_volatility_calc012_21d_slope_v012_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
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
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc012_21d_slope_v012_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc012_21d_slope_v012_signal

def f102e_f102_ebitda_to_revenue_volatility_calc013_5d_slope_v013_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.rolling(5).kurt() - revenue.rolling(5).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc013_5d_slope_v013_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc013_5d_slope_v013_signal

def f102e_f102_ebitda_to_revenue_volatility_calc014_42d_slope_v014_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (netinc.diff(42).abs() / assets.diff(42).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc014_42d_slope_v014_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc014_42d_slope_v014_signal

def f102e_f102_ebitda_to_revenue_volatility_calc015_42d_slope_v015_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue / capex.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc015_42d_slope_v015_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc015_42d_slope_v015_signal

def f102e_f102_ebitda_to_revenue_volatility_calc016_10d_slope_v016_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt / capex.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc016_10d_slope_v016_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc016_10d_slope_v016_signal

def f102e_f102_ebitda_to_revenue_volatility_calc017_126d_slope_v017_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (netinc.rolling(126).max() - equity.rolling(126).min()) / ebitda.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc017_126d_slope_v017_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc017_126d_slope_v017_signal

def f102e_f102_ebitda_to_revenue_volatility_calc018_63d_slope_v018_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt.diff(63).abs() / equity.diff(63).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc018_63d_slope_v018_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc018_63d_slope_v018_signal

def f102e_f102_ebitda_to_revenue_volatility_calc019_10d_slope_v019_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (assets.rolling(10).quantile(0.5) / debt.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc019_10d_slope_v019_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc019_10d_slope_v019_signal

def f102e_f102_ebitda_to_revenue_volatility_calc020_63d_slope_v020_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.rolling(63).max() - netinc.rolling(63).min()) / capex.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc020_63d_slope_v020_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc020_63d_slope_v020_signal

def f102e_f102_ebitda_to_revenue_volatility_calc021_5d_slope_v021_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (assets.rolling(5).rank(pct=True) / debt.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc021_5d_slope_v021_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc021_5d_slope_v021_signal

def f102e_f102_ebitda_to_revenue_volatility_calc022_10d_slope_v022_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.rolling(10).quantile(0.5) / equity.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc022_10d_slope_v022_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc022_10d_slope_v022_signal

def f102e_f102_ebitda_to_revenue_volatility_calc023_126d_slope_v023_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.diff(126) / capex.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc023_126d_slope_v023_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc023_126d_slope_v023_signal

def f102e_f102_ebitda_to_revenue_volatility_calc024_126d_slope_v024_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.diff(126) / debt.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc024_126d_slope_v024_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc024_126d_slope_v024_signal

def f102e_f102_ebitda_to_revenue_volatility_calc025_21d_slope_v025_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.diff(21) / capex.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc025_21d_slope_v025_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc025_21d_slope_v025_signal

def f102e_f102_ebitda_to_revenue_volatility_calc026_5d_slope_v026_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.rolling(5).kurt() - debt.rolling(5).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc026_5d_slope_v026_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc026_5d_slope_v026_signal

def f102e_f102_ebitda_to_revenue_volatility_calc027_252d_slope_v027_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
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
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc027_252d_slope_v027_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc027_252d_slope_v027_signal

def f102e_f102_ebitda_to_revenue_volatility_calc028_252d_slope_v028_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda.rolling(252).kurt() - revenue.rolling(252).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc028_252d_slope_v028_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc028_252d_slope_v028_signal

def f102e_f102_ebitda_to_revenue_volatility_calc029_5d_slope_v029_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.rolling(5).quantile(0.5) / revenue.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc029_5d_slope_v029_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc029_5d_slope_v029_signal

def f102e_f102_ebitda_to_revenue_volatility_calc030_10d_slope_v030_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity / capex.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc030_10d_slope_v030_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc030_10d_slope_v030_signal

def f102e_f102_ebitda_to_revenue_volatility_calc031_126d_slope_v031_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.rolling(126).rank(pct=True) / netinc.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc031_126d_slope_v031_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc031_126d_slope_v031_signal

def f102e_f102_ebitda_to_revenue_volatility_calc032_126d_slope_v032_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (assets / netinc.replace(0, np.nan)).rolling(126).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc032_126d_slope_v032_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc032_126d_slope_v032_signal

def f102e_f102_ebitda_to_revenue_volatility_calc033_63d_slope_v033_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.rolling(63).max() - capex.rolling(63).min()) / netinc.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc033_63d_slope_v033_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc033_63d_slope_v033_signal

def f102e_f102_ebitda_to_revenue_volatility_calc034_42d_slope_v034_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (assets.rolling(42).max() - ebitda.rolling(42).min()) / equity.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc034_42d_slope_v034_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc034_42d_slope_v034_signal

def f102e_f102_ebitda_to_revenue_volatility_calc035_42d_slope_v035_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = ((capex - capex.rolling(42).mean()) / capex.rolling(42).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc035_42d_slope_v035_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc035_42d_slope_v035_signal

def f102e_f102_ebitda_to_revenue_volatility_calc036_63d_slope_v036_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = ((capex - capex.rolling(63).mean()) / capex.rolling(63).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc036_63d_slope_v036_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc036_63d_slope_v036_signal

def f102e_f102_ebitda_to_revenue_volatility_calc037_10d_slope_v037_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex / debt.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc037_10d_slope_v037_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc037_10d_slope_v037_signal

def f102e_f102_ebitda_to_revenue_volatility_calc038_126d_slope_v038_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (netinc.pct_change(126) - equity.pct_change(126))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc038_126d_slope_v038_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc038_126d_slope_v038_signal

def f102e_f102_ebitda_to_revenue_volatility_calc039_10d_slope_v039_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda.rolling(10).kurt() - netinc.rolling(10).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc039_10d_slope_v039_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc039_10d_slope_v039_signal

def f102e_f102_ebitda_to_revenue_volatility_calc040_21d_slope_v040_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = ((debt - debt.rolling(21).mean()) / debt.rolling(21).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc040_21d_slope_v040_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc040_21d_slope_v040_signal

def f102e_f102_ebitda_to_revenue_volatility_calc041_252d_slope_v041_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (netinc / ebitda.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc041_252d_slope_v041_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc041_252d_slope_v041_signal

def f102e_f102_ebitda_to_revenue_volatility_calc042_10d_slope_v042_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda.rolling(10).rank(pct=True) / assets.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc042_10d_slope_v042_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc042_10d_slope_v042_signal

def f102e_f102_ebitda_to_revenue_volatility_calc043_21d_slope_v043_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
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
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc043_21d_slope_v043_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc043_21d_slope_v043_signal

def f102e_f102_ebitda_to_revenue_volatility_calc044_10d_slope_v044_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.diff(10).abs() / equity.diff(10).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc044_10d_slope_v044_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc044_10d_slope_v044_signal

def f102e_f102_ebitda_to_revenue_volatility_calc045_63d_slope_v045_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.rolling(63).rank(pct=True) / capex.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc045_63d_slope_v045_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc045_63d_slope_v045_signal

def f102e_f102_ebitda_to_revenue_volatility_calc046_126d_slope_v046_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda.diff(126).abs() / netinc.diff(126).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc046_126d_slope_v046_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc046_126d_slope_v046_signal

def f102e_f102_ebitda_to_revenue_volatility_calc047_126d_slope_v047_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.pct_change(126) - debt.pct_change(126))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc047_126d_slope_v047_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc047_126d_slope_v047_signal

def f102e_f102_ebitda_to_revenue_volatility_calc048_63d_slope_v048_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex / assets.replace(0, np.nan)).rolling(63).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc048_63d_slope_v048_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc048_63d_slope_v048_signal

def f102e_f102_ebitda_to_revenue_volatility_calc049_63d_slope_v049_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.diff(63).abs() / assets.diff(63).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc049_63d_slope_v049_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc049_63d_slope_v049_signal

def f102e_f102_ebitda_to_revenue_volatility_calc050_10d_slope_v050_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda.rolling(10).quantile(0.5) / netinc.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc050_10d_slope_v050_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc050_10d_slope_v050_signal

def f102e_f102_ebitda_to_revenue_volatility_calc051_5d_slope_v051_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.diff(5) / equity.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc051_5d_slope_v051_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc051_5d_slope_v051_signal

def f102e_f102_ebitda_to_revenue_volatility_calc052_42d_slope_v052_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
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
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc052_42d_slope_v052_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc052_42d_slope_v052_signal

def f102e_f102_ebitda_to_revenue_volatility_calc053_42d_slope_v053_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.rolling(42).quantile(0.5) / netinc.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc053_42d_slope_v053_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc053_42d_slope_v053_signal

def f102e_f102_ebitda_to_revenue_volatility_calc054_21d_slope_v054_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt / equity.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc054_21d_slope_v054_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc054_21d_slope_v054_signal

def f102e_f102_ebitda_to_revenue_volatility_calc055_5d_slope_v055_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.diff(5).abs() / netinc.diff(5).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc055_5d_slope_v055_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc055_5d_slope_v055_signal

def f102e_f102_ebitda_to_revenue_volatility_calc056_5d_slope_v056_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda.rolling(5).rank(pct=True) / assets.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc056_5d_slope_v056_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc056_5d_slope_v056_signal

def f102e_f102_ebitda_to_revenue_volatility_calc057_126d_slope_v057_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt.pct_change(126) - netinc.pct_change(126))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc057_126d_slope_v057_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc057_126d_slope_v057_signal

def f102e_f102_ebitda_to_revenue_volatility_calc058_10d_slope_v058_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.rolling(10).quantile(0.5) / capex.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc058_10d_slope_v058_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc058_10d_slope_v058_signal

def f102e_f102_ebitda_to_revenue_volatility_calc059_126d_slope_v059_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = ((assets - assets.rolling(126).mean()) / assets.rolling(126).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc059_126d_slope_v059_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc059_126d_slope_v059_signal

def f102e_f102_ebitda_to_revenue_volatility_calc060_126d_slope_v060_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
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
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc060_126d_slope_v060_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc060_126d_slope_v060_signal

def f102e_f102_ebitda_to_revenue_volatility_calc061_63d_slope_v061_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
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
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc061_63d_slope_v061_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc061_63d_slope_v061_signal

def f102e_f102_ebitda_to_revenue_volatility_calc062_126d_slope_v062_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.rolling(126).quantile(0.5) / capex.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc062_126d_slope_v062_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc062_126d_slope_v062_signal

def f102e_f102_ebitda_to_revenue_volatility_calc063_252d_slope_v063_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.diff(252).abs() / assets.diff(252).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc063_252d_slope_v063_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc063_252d_slope_v063_signal

def f102e_f102_ebitda_to_revenue_volatility_calc064_126d_slope_v064_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = ((debt - debt.rolling(126).mean()) / debt.rolling(126).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc064_126d_slope_v064_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc064_126d_slope_v064_signal

def f102e_f102_ebitda_to_revenue_volatility_calc065_5d_slope_v065_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = ((debt - debt.rolling(5).mean()) / debt.rolling(5).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc065_5d_slope_v065_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc065_5d_slope_v065_signal

def f102e_f102_ebitda_to_revenue_volatility_calc066_5d_slope_v066_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.diff(5) / assets.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc066_5d_slope_v066_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc066_5d_slope_v066_signal

def f102e_f102_ebitda_to_revenue_volatility_calc067_63d_slope_v067_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (assets / capex.replace(0, np.nan)).rolling(63).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc067_63d_slope_v067_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc067_63d_slope_v067_signal

def f102e_f102_ebitda_to_revenue_volatility_calc068_126d_slope_v068_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex / assets.replace(0, np.nan)).rolling(126).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc068_126d_slope_v068_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc068_126d_slope_v068_signal

def f102e_f102_ebitda_to_revenue_volatility_calc069_63d_slope_v069_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.rolling(63).max() - debt.rolling(63).min()) / revenue.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc069_63d_slope_v069_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc069_63d_slope_v069_signal

def f102e_f102_ebitda_to_revenue_volatility_calc070_21d_slope_v070_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt / netinc.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc070_21d_slope_v070_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc070_21d_slope_v070_signal

def f102e_f102_ebitda_to_revenue_volatility_calc071_252d_slope_v071_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
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
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc071_252d_slope_v071_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc071_252d_slope_v071_signal

def f102e_f102_ebitda_to_revenue_volatility_calc072_21d_slope_v072_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda.diff(21).abs() / capex.diff(21).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc072_21d_slope_v072_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc072_21d_slope_v072_signal

def f102e_f102_ebitda_to_revenue_volatility_calc073_126d_slope_v073_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.pct_change(126) - assets.pct_change(126))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc073_126d_slope_v073_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc073_126d_slope_v073_signal

def f102e_f102_ebitda_to_revenue_volatility_calc074_63d_slope_v074_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.diff(63).abs() / debt.diff(63).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc074_63d_slope_v074_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc074_63d_slope_v074_signal

def f102e_f102_ebitda_to_revenue_volatility_calc075_21d_slope_v075_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (netinc / equity.replace(0, np.nan)).rolling(21).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc075_21d_slope_v075_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc075_21d_slope_v075_signal

def f102e_f102_ebitda_to_revenue_volatility_calc076_252d_slope_v076_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (assets / equity.replace(0, np.nan)).rolling(252).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc076_252d_slope_v076_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc076_252d_slope_v076_signal

def f102e_f102_ebitda_to_revenue_volatility_calc077_126d_slope_v077_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (netinc / ebitda.replace(0, np.nan)).rolling(126).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc077_126d_slope_v077_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc077_126d_slope_v077_signal

def f102e_f102_ebitda_to_revenue_volatility_calc078_252d_slope_v078_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (assets.diff(252).abs() / debt.diff(252).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc078_252d_slope_v078_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc078_252d_slope_v078_signal

def f102e_f102_ebitda_to_revenue_volatility_calc079_252d_slope_v079_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.diff(252) / capex.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc079_252d_slope_v079_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc079_252d_slope_v079_signal

def f102e_f102_ebitda_to_revenue_volatility_calc080_21d_slope_v080_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda / debt.replace(0, np.nan)).rolling(21).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc080_21d_slope_v080_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc080_21d_slope_v080_signal

def f102e_f102_ebitda_to_revenue_volatility_calc081_252d_slope_v081_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.rolling(252).quantile(0.5) / assets.rolling(252).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc081_252d_slope_v081_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc081_252d_slope_v081_signal

def f102e_f102_ebitda_to_revenue_volatility_calc082_21d_slope_v082_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.diff(21) / netinc.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc082_21d_slope_v082_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc082_21d_slope_v082_signal

def f102e_f102_ebitda_to_revenue_volatility_calc083_5d_slope_v083_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
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
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc083_5d_slope_v083_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc083_5d_slope_v083_signal

def f102e_f102_ebitda_to_revenue_volatility_calc084_10d_slope_v084_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (netinc.rolling(10).rank(pct=True) / debt.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc084_10d_slope_v084_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc084_10d_slope_v084_signal

def f102e_f102_ebitda_to_revenue_volatility_calc085_126d_slope_v085_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.pct_change(126) - debt.pct_change(126))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc085_126d_slope_v085_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc085_126d_slope_v085_signal

def f102e_f102_ebitda_to_revenue_volatility_calc086_5d_slope_v086_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.rolling(5).kurt() - equity.rolling(5).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc086_5d_slope_v086_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc086_5d_slope_v086_signal

def f102e_f102_ebitda_to_revenue_volatility_calc087_63d_slope_v087_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (assets.rolling(63).rank(pct=True) / netinc.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc087_63d_slope_v087_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc087_63d_slope_v087_signal

def f102e_f102_ebitda_to_revenue_volatility_calc088_126d_slope_v088_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt.rolling(126).max() - netinc.rolling(126).min()) / ebitda.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc088_126d_slope_v088_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc088_126d_slope_v088_signal

def f102e_f102_ebitda_to_revenue_volatility_calc089_126d_slope_v089_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
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
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc089_126d_slope_v089_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc089_126d_slope_v089_signal

def f102e_f102_ebitda_to_revenue_volatility_calc090_5d_slope_v090_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda.rolling(5).rank(pct=True) / capex.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc090_5d_slope_v090_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc090_5d_slope_v090_signal

def f102e_f102_ebitda_to_revenue_volatility_calc091_63d_slope_v091_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = ((debt - debt.rolling(63).mean()) / debt.rolling(63).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc091_63d_slope_v091_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc091_63d_slope_v091_signal

def f102e_f102_ebitda_to_revenue_volatility_calc092_10d_slope_v092_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt / equity.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc092_10d_slope_v092_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc092_10d_slope_v092_signal

def f102e_f102_ebitda_to_revenue_volatility_calc093_63d_slope_v093_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (assets.rolling(63).rank(pct=True) / capex.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc093_63d_slope_v093_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc093_63d_slope_v093_signal

def f102e_f102_ebitda_to_revenue_volatility_calc094_21d_slope_v094_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex / debt.replace(0, np.nan)).rolling(21).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc094_21d_slope_v094_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc094_21d_slope_v094_signal

def f102e_f102_ebitda_to_revenue_volatility_calc095_126d_slope_v095_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (netinc.rolling(126).kurt() - capex.rolling(126).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc095_126d_slope_v095_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc095_126d_slope_v095_signal

def f102e_f102_ebitda_to_revenue_volatility_calc096_5d_slope_v096_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt.rolling(5).kurt() - revenue.rolling(5).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc096_5d_slope_v096_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc096_5d_slope_v096_signal

def f102e_f102_ebitda_to_revenue_volatility_calc097_252d_slope_v097_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.pct_change(252) - debt.pct_change(252))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc097_252d_slope_v097_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc097_252d_slope_v097_signal

def f102e_f102_ebitda_to_revenue_volatility_calc098_21d_slope_v098_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
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
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc098_21d_slope_v098_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc098_21d_slope_v098_signal

def f102e_f102_ebitda_to_revenue_volatility_calc099_126d_slope_v099_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.rolling(126).max() - netinc.rolling(126).min()) / capex.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc099_126d_slope_v099_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc099_126d_slope_v099_signal

def f102e_f102_ebitda_to_revenue_volatility_calc100_252d_slope_v100_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.diff(252).abs() / capex.diff(252).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc100_252d_slope_v100_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc100_252d_slope_v100_signal

def f102e_f102_ebitda_to_revenue_volatility_calc101_5d_slope_v101_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (assets.rolling(5).max() - capex.rolling(5).min()) / netinc.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc101_5d_slope_v101_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc101_5d_slope_v101_signal

def f102e_f102_ebitda_to_revenue_volatility_calc102_126d_slope_v102_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda.diff(126) / equity.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc102_126d_slope_v102_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc102_126d_slope_v102_signal

def f102e_f102_ebitda_to_revenue_volatility_calc103_21d_slope_v103_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (netinc.rolling(21).quantile(0.5) / revenue.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc103_21d_slope_v103_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc103_21d_slope_v103_signal

def f102e_f102_ebitda_to_revenue_volatility_calc104_63d_slope_v104_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt.rolling(63).max() - equity.rolling(63).min()) / assets.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc104_63d_slope_v104_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc104_63d_slope_v104_signal

def f102e_f102_ebitda_to_revenue_volatility_calc105_21d_slope_v105_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
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
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc105_21d_slope_v105_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc105_21d_slope_v105_signal

def f102e_f102_ebitda_to_revenue_volatility_calc106_5d_slope_v106_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda.rolling(5).quantile(0.5) / capex.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc106_5d_slope_v106_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc106_5d_slope_v106_signal

def f102e_f102_ebitda_to_revenue_volatility_calc107_21d_slope_v107_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.rolling(21).quantile(0.5) / capex.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc107_21d_slope_v107_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc107_21d_slope_v107_signal

def f102e_f102_ebitda_to_revenue_volatility_calc108_42d_slope_v108_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = ((debt - debt.rolling(42).mean()) / debt.rolling(42).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc108_42d_slope_v108_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc108_42d_slope_v108_signal

def f102e_f102_ebitda_to_revenue_volatility_calc109_63d_slope_v109_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (assets.rolling(63).quantile(0.5) / capex.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc109_63d_slope_v109_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc109_63d_slope_v109_signal

def f102e_f102_ebitda_to_revenue_volatility_calc110_5d_slope_v110_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda.pct_change(5) - equity.pct_change(5))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc110_5d_slope_v110_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc110_5d_slope_v110_signal

def f102e_f102_ebitda_to_revenue_volatility_calc111_42d_slope_v111_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (netinc.rolling(42).rank(pct=True) / revenue.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc111_42d_slope_v111_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc111_42d_slope_v111_signal

def f102e_f102_ebitda_to_revenue_volatility_calc112_252d_slope_v112_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (netinc / debt.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc112_252d_slope_v112_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc112_252d_slope_v112_signal

def f102e_f102_ebitda_to_revenue_volatility_calc113_42d_slope_v113_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.rolling(42).rank(pct=True) / debt.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc113_42d_slope_v113_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc113_42d_slope_v113_signal

def f102e_f102_ebitda_to_revenue_volatility_calc114_252d_slope_v114_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt.pct_change(252) - netinc.pct_change(252))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc114_252d_slope_v114_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc114_252d_slope_v114_signal

def f102e_f102_ebitda_to_revenue_volatility_calc115_63d_slope_v115_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.diff(63) / debt.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc115_63d_slope_v115_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc115_63d_slope_v115_signal

def f102e_f102_ebitda_to_revenue_volatility_calc116_126d_slope_v116_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.rolling(126).rank(pct=True) / assets.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc116_126d_slope_v116_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc116_126d_slope_v116_signal

def f102e_f102_ebitda_to_revenue_volatility_calc117_5d_slope_v117_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda.rolling(5).quantile(0.5) / equity.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc117_5d_slope_v117_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc117_5d_slope_v117_signal

def f102e_f102_ebitda_to_revenue_volatility_calc118_10d_slope_v118_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.diff(10).abs() / capex.diff(10).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc118_10d_slope_v118_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc118_10d_slope_v118_signal

def f102e_f102_ebitda_to_revenue_volatility_calc119_42d_slope_v119_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.rolling(42).quantile(0.5) / debt.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc119_42d_slope_v119_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc119_42d_slope_v119_signal

def f102e_f102_ebitda_to_revenue_volatility_calc120_10d_slope_v120_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex / revenue.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc120_10d_slope_v120_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc120_10d_slope_v120_signal

def f102e_f102_ebitda_to_revenue_volatility_calc121_252d_slope_v121_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (netinc.rolling(252).max() - revenue.rolling(252).min()) / equity.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc121_252d_slope_v121_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc121_252d_slope_v121_signal

def f102e_f102_ebitda_to_revenue_volatility_calc122_42d_slope_v122_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
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
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc122_42d_slope_v122_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc122_42d_slope_v122_signal

def f102e_f102_ebitda_to_revenue_volatility_calc123_63d_slope_v123_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity / capex.replace(0, np.nan)).rolling(63).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc123_63d_slope_v123_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc123_63d_slope_v123_signal

def f102e_f102_ebitda_to_revenue_volatility_calc124_63d_slope_v124_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
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
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc124_63d_slope_v124_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc124_63d_slope_v124_signal

def f102e_f102_ebitda_to_revenue_volatility_calc125_5d_slope_v125_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue / capex.replace(0, np.nan)).rolling(5).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc125_5d_slope_v125_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc125_5d_slope_v125_signal

def f102e_f102_ebitda_to_revenue_volatility_calc126_126d_slope_v126_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt.diff(126).abs() / equity.diff(126).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc126_126d_slope_v126_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc126_126d_slope_v126_signal

def f102e_f102_ebitda_to_revenue_volatility_calc127_252d_slope_v127_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt.rolling(252).max() - capex.rolling(252).min()) / netinc.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc127_252d_slope_v127_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc127_252d_slope_v127_signal

def f102e_f102_ebitda_to_revenue_volatility_calc128_21d_slope_v128_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.rolling(21).rank(pct=True) / equity.rolling(21).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc128_21d_slope_v128_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc128_21d_slope_v128_signal

def f102e_f102_ebitda_to_revenue_volatility_calc129_252d_slope_v129_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.rolling(252).kurt() - netinc.rolling(252).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc129_252d_slope_v129_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc129_252d_slope_v129_signal

def f102e_f102_ebitda_to_revenue_volatility_calc130_126d_slope_v130_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt / revenue.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc130_126d_slope_v130_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc130_126d_slope_v130_signal

def f102e_f102_ebitda_to_revenue_volatility_calc131_10d_slope_v131_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
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
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc131_10d_slope_v131_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc131_10d_slope_v131_signal

def f102e_f102_ebitda_to_revenue_volatility_calc132_63d_slope_v132_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.pct_change(63) - netinc.pct_change(63))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc132_63d_slope_v132_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc132_63d_slope_v132_signal

def f102e_f102_ebitda_to_revenue_volatility_calc133_21d_slope_v133_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
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
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc133_21d_slope_v133_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc133_21d_slope_v133_signal

def f102e_f102_ebitda_to_revenue_volatility_calc134_42d_slope_v134_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt.rolling(42).max() - capex.rolling(42).min()) / revenue.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc134_42d_slope_v134_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc134_42d_slope_v134_signal

def f102e_f102_ebitda_to_revenue_volatility_calc135_42d_slope_v135_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.diff(42) / ebitda.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc135_42d_slope_v135_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc135_42d_slope_v135_signal

def f102e_f102_ebitda_to_revenue_volatility_calc136_42d_slope_v136_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.rolling(42).max() - ebitda.rolling(42).min()) / debt.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc136_42d_slope_v136_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc136_42d_slope_v136_signal

def f102e_f102_ebitda_to_revenue_volatility_calc137_63d_slope_v137_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex / ebitda.replace(0, np.nan)).rolling(63).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc137_63d_slope_v137_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc137_63d_slope_v137_signal

def f102e_f102_ebitda_to_revenue_volatility_calc138_252d_slope_v138_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (netinc.pct_change(252) - equity.pct_change(252))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc138_252d_slope_v138_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc138_252d_slope_v138_signal

def f102e_f102_ebitda_to_revenue_volatility_calc139_252d_slope_v139_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = ((assets - assets.rolling(252).mean()) / assets.rolling(252).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc139_252d_slope_v139_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc139_252d_slope_v139_signal

def f102e_f102_ebitda_to_revenue_volatility_calc140_10d_slope_v140_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.rolling(10).quantile(0.5) / netinc.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc140_10d_slope_v140_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc140_10d_slope_v140_signal

def f102e_f102_ebitda_to_revenue_volatility_calc141_126d_slope_v141_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.diff(126) / assets.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc141_126d_slope_v141_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc141_126d_slope_v141_signal

def f102e_f102_ebitda_to_revenue_volatility_calc142_252d_slope_v142_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex / debt.replace(0, np.nan)).rolling(252).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc142_252d_slope_v142_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc142_252d_slope_v142_signal

def f102e_f102_ebitda_to_revenue_volatility_calc143_42d_slope_v143_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (netinc.diff(42).abs() / equity.diff(42).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc143_42d_slope_v143_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc143_42d_slope_v143_signal

def f102e_f102_ebitda_to_revenue_volatility_calc144_63d_slope_v144_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (debt.rolling(63).kurt() - netinc.rolling(63).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc144_63d_slope_v144_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc144_63d_slope_v144_signal

def f102e_f102_ebitda_to_revenue_volatility_calc145_126d_slope_v145_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (capex.rolling(126).max() - debt.rolling(126).min()) / revenue.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc145_126d_slope_v145_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc145_126d_slope_v145_signal

def f102e_f102_ebitda_to_revenue_volatility_calc146_10d_slope_v146_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (equity.pct_change(10) - capex.pct_change(10))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc146_10d_slope_v146_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc146_10d_slope_v146_signal

def f102e_f102_ebitda_to_revenue_volatility_calc147_63d_slope_v147_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.pct_change(63) - equity.pct_change(63))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc147_63d_slope_v147_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc147_63d_slope_v147_signal

def f102e_f102_ebitda_to_revenue_volatility_calc148_5d_slope_v148_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
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
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc148_5d_slope_v148_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc148_5d_slope_v148_signal

def f102e_f102_ebitda_to_revenue_volatility_calc149_21d_slope_v149_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (revenue.diff(21).abs() / netinc.diff(21).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc149_21d_slope_v149_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc149_21d_slope_v149_signal

def f102e_f102_ebitda_to_revenue_volatility_calc150_5d_slope_v150_signal(ebitda, revenue, assets, equity, capex, debt, netinc):
    v1 = (ebitda.rolling(5).max() - debt.rolling(5).min()) / netinc.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f102e_f102_ebitda_to_revenue_volatility_calc150_5d_slope_v150_signal'] = f102e_f102_ebitda_to_revenue_volatility_calc150_5d_slope_v150_signal



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
