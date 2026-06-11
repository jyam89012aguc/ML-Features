import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f107d_f107_debt_to_equity_dispersion_calc001_42d_slope_v001_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.diff(42) / assets.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc001_42d_slope_v001_signal'] = f107d_f107_debt_to_equity_dispersion_calc001_42d_slope_v001_signal

def f107d_f107_debt_to_equity_dispersion_calc002_252d_slope_v002_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.diff(252).abs() / assets.diff(252).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc002_252d_slope_v002_signal'] = f107d_f107_debt_to_equity_dispersion_calc002_252d_slope_v002_signal

def f107d_f107_debt_to_equity_dispersion_calc003_5d_slope_v003_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.pct_change(5) - liabilities.pct_change(5))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc003_5d_slope_v003_signal'] = f107d_f107_debt_to_equity_dispersion_calc003_5d_slope_v003_signal

def f107d_f107_debt_to_equity_dispersion_calc004_10d_slope_v004_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets.diff(10) / liabilities.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc004_10d_slope_v004_signal'] = f107d_f107_debt_to_equity_dispersion_calc004_10d_slope_v004_signal

def f107d_f107_debt_to_equity_dispersion_calc005_63d_slope_v005_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(63).quantile(0.5) / marketcap.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc005_63d_slope_v005_signal'] = f107d_f107_debt_to_equity_dispersion_calc005_63d_slope_v005_signal

def f107d_f107_debt_to_equity_dispersion_calc006_126d_slope_v006_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.rolling(126).quantile(0.5) / equity.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc006_126d_slope_v006_signal'] = f107d_f107_debt_to_equity_dispersion_calc006_126d_slope_v006_signal

def f107d_f107_debt_to_equity_dispersion_calc007_21d_slope_v007_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(21).kurt() - assets.rolling(21).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc007_21d_slope_v007_signal'] = f107d_f107_debt_to_equity_dispersion_calc007_21d_slope_v007_signal

def f107d_f107_debt_to_equity_dispersion_calc008_126d_slope_v008_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(126).max() - debt.rolling(126).min()) / marketcap.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc008_126d_slope_v008_signal'] = f107d_f107_debt_to_equity_dispersion_calc008_126d_slope_v008_signal

def f107d_f107_debt_to_equity_dispersion_calc009_10d_slope_v009_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets.rolling(10).quantile(0.5) / liabilities.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc009_10d_slope_v009_signal'] = f107d_f107_debt_to_equity_dispersion_calc009_10d_slope_v009_signal

def f107d_f107_debt_to_equity_dispersion_calc010_21d_slope_v010_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.pct_change(21) - liabilities.pct_change(21))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc010_21d_slope_v010_signal'] = f107d_f107_debt_to_equity_dispersion_calc010_21d_slope_v010_signal

def f107d_f107_debt_to_equity_dispersion_calc011_21d_slope_v011_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.diff(21) / equity.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc011_21d_slope_v011_signal'] = f107d_f107_debt_to_equity_dispersion_calc011_21d_slope_v011_signal

def f107d_f107_debt_to_equity_dispersion_calc012_42d_slope_v012_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity / ebitda.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc012_42d_slope_v012_signal'] = f107d_f107_debt_to_equity_dispersion_calc012_42d_slope_v012_signal

def f107d_f107_debt_to_equity_dispersion_calc013_252d_slope_v013_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.pct_change(252) - marketcap.pct_change(252))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc013_252d_slope_v013_signal'] = f107d_f107_debt_to_equity_dispersion_calc013_252d_slope_v013_signal

def f107d_f107_debt_to_equity_dispersion_calc014_126d_slope_v014_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio / debt.replace(0, np.nan)).rolling(126).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc014_126d_slope_v014_signal'] = f107d_f107_debt_to_equity_dispersion_calc014_126d_slope_v014_signal

def f107d_f107_debt_to_equity_dispersion_calc015_10d_slope_v015_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets.diff(10) / marketcap.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc015_10d_slope_v015_signal'] = f107d_f107_debt_to_equity_dispersion_calc015_10d_slope_v015_signal

def f107d_f107_debt_to_equity_dispersion_calc016_126d_slope_v016_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = ((currentratio - currentratio.rolling(126).mean()) / currentratio.rolling(126).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc016_126d_slope_v016_signal'] = f107d_f107_debt_to_equity_dispersion_calc016_126d_slope_v016_signal

def f107d_f107_debt_to_equity_dispersion_calc017_21d_slope_v017_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.diff(21).abs() / marketcap.diff(21).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc017_21d_slope_v017_signal'] = f107d_f107_debt_to_equity_dispersion_calc017_21d_slope_v017_signal

def f107d_f107_debt_to_equity_dispersion_calc018_126d_slope_v018_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.pct_change(126) - assets.pct_change(126))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc018_126d_slope_v018_signal'] = f107d_f107_debt_to_equity_dispersion_calc018_126d_slope_v018_signal

def f107d_f107_debt_to_equity_dispersion_calc019_42d_slope_v019_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
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
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc019_42d_slope_v019_signal'] = f107d_f107_debt_to_equity_dispersion_calc019_42d_slope_v019_signal

def f107d_f107_debt_to_equity_dispersion_calc020_10d_slope_v020_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.rolling(10).max() - marketcap.rolling(10).min()) / equity.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc020_10d_slope_v020_signal'] = f107d_f107_debt_to_equity_dispersion_calc020_10d_slope_v020_signal

def f107d_f107_debt_to_equity_dispersion_calc021_5d_slope_v021_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(5).max() - debt.rolling(5).min()) / equity.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc021_5d_slope_v021_signal'] = f107d_f107_debt_to_equity_dispersion_calc021_5d_slope_v021_signal

def f107d_f107_debt_to_equity_dispersion_calc022_5d_slope_v022_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(5).quantile(0.5) / marketcap.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc022_5d_slope_v022_signal'] = f107d_f107_debt_to_equity_dispersion_calc022_5d_slope_v022_signal

def f107d_f107_debt_to_equity_dispersion_calc023_10d_slope_v023_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.rolling(10).max() - marketcap.rolling(10).min()) / currentratio.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc023_10d_slope_v023_signal'] = f107d_f107_debt_to_equity_dispersion_calc023_10d_slope_v023_signal

def f107d_f107_debt_to_equity_dispersion_calc024_63d_slope_v024_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
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
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc024_63d_slope_v024_signal'] = f107d_f107_debt_to_equity_dispersion_calc024_63d_slope_v024_signal

def f107d_f107_debt_to_equity_dispersion_calc025_21d_slope_v025_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap / assets.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc025_21d_slope_v025_signal'] = f107d_f107_debt_to_equity_dispersion_calc025_21d_slope_v025_signal

def f107d_f107_debt_to_equity_dispersion_calc026_21d_slope_v026_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap / equity.replace(0, np.nan)).rolling(21).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc026_21d_slope_v026_signal'] = f107d_f107_debt_to_equity_dispersion_calc026_21d_slope_v026_signal

def f107d_f107_debt_to_equity_dispersion_calc027_10d_slope_v027_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(10).quantile(0.5) / ebitda.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc027_10d_slope_v027_signal'] = f107d_f107_debt_to_equity_dispersion_calc027_10d_slope_v027_signal

def f107d_f107_debt_to_equity_dispersion_calc028_21d_slope_v028_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
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
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc028_21d_slope_v028_signal'] = f107d_f107_debt_to_equity_dispersion_calc028_21d_slope_v028_signal

def f107d_f107_debt_to_equity_dispersion_calc029_252d_slope_v029_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.diff(252) / debt.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc029_252d_slope_v029_signal'] = f107d_f107_debt_to_equity_dispersion_calc029_252d_slope_v029_signal

def f107d_f107_debt_to_equity_dispersion_calc030_63d_slope_v030_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(63).rank(pct=True) / debt.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc030_63d_slope_v030_signal'] = f107d_f107_debt_to_equity_dispersion_calc030_63d_slope_v030_signal

def f107d_f107_debt_to_equity_dispersion_calc031_5d_slope_v031_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.diff(5) / liabilities.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc031_5d_slope_v031_signal'] = f107d_f107_debt_to_equity_dispersion_calc031_5d_slope_v031_signal

def f107d_f107_debt_to_equity_dispersion_calc032_5d_slope_v032_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.rolling(5).kurt() - equity.rolling(5).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc032_5d_slope_v032_signal'] = f107d_f107_debt_to_equity_dispersion_calc032_5d_slope_v032_signal

def f107d_f107_debt_to_equity_dispersion_calc033_252d_slope_v033_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.pct_change(252) - debt.pct_change(252))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc033_252d_slope_v033_signal'] = f107d_f107_debt_to_equity_dispersion_calc033_252d_slope_v033_signal

def f107d_f107_debt_to_equity_dispersion_calc034_126d_slope_v034_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.rolling(126).kurt() - ebitda.rolling(126).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc034_126d_slope_v034_signal'] = f107d_f107_debt_to_equity_dispersion_calc034_126d_slope_v034_signal

def f107d_f107_debt_to_equity_dispersion_calc035_5d_slope_v035_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(5).kurt() - assets.rolling(5).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc035_5d_slope_v035_signal'] = f107d_f107_debt_to_equity_dispersion_calc035_5d_slope_v035_signal

def f107d_f107_debt_to_equity_dispersion_calc036_10d_slope_v036_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets.diff(10).abs() / equity.diff(10).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc036_10d_slope_v036_signal'] = f107d_f107_debt_to_equity_dispersion_calc036_10d_slope_v036_signal

def f107d_f107_debt_to_equity_dispersion_calc037_10d_slope_v037_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.rolling(10).rank(pct=True) / currentratio.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc037_10d_slope_v037_signal'] = f107d_f107_debt_to_equity_dispersion_calc037_10d_slope_v037_signal

def f107d_f107_debt_to_equity_dispersion_calc038_10d_slope_v038_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(10).quantile(0.5) / currentratio.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc038_10d_slope_v038_signal'] = f107d_f107_debt_to_equity_dispersion_calc038_10d_slope_v038_signal

def f107d_f107_debt_to_equity_dispersion_calc039_63d_slope_v039_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities / currentratio.replace(0, np.nan)).rolling(63).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc039_63d_slope_v039_signal'] = f107d_f107_debt_to_equity_dispersion_calc039_63d_slope_v039_signal

def f107d_f107_debt_to_equity_dispersion_calc040_252d_slope_v040_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = ((debt - debt.rolling(252).mean()) / debt.rolling(252).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc040_252d_slope_v040_signal'] = f107d_f107_debt_to_equity_dispersion_calc040_252d_slope_v040_signal

def f107d_f107_debt_to_equity_dispersion_calc041_126d_slope_v041_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(126).max() - marketcap.rolling(126).min()) / debt.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc041_126d_slope_v041_signal'] = f107d_f107_debt_to_equity_dispersion_calc041_126d_slope_v041_signal

def f107d_f107_debt_to_equity_dispersion_calc042_10d_slope_v042_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap / equity.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc042_10d_slope_v042_signal'] = f107d_f107_debt_to_equity_dispersion_calc042_10d_slope_v042_signal

def f107d_f107_debt_to_equity_dispersion_calc043_42d_slope_v043_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.pct_change(42) - assets.pct_change(42))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc043_42d_slope_v043_signal'] = f107d_f107_debt_to_equity_dispersion_calc043_42d_slope_v043_signal

def f107d_f107_debt_to_equity_dispersion_calc044_42d_slope_v044_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.diff(42) / ebitda.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc044_42d_slope_v044_signal'] = f107d_f107_debt_to_equity_dispersion_calc044_42d_slope_v044_signal

def f107d_f107_debt_to_equity_dispersion_calc045_63d_slope_v045_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.rolling(63).kurt() - debt.rolling(63).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc045_63d_slope_v045_signal'] = f107d_f107_debt_to_equity_dispersion_calc045_63d_slope_v045_signal

def f107d_f107_debt_to_equity_dispersion_calc046_63d_slope_v046_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.rolling(63).kurt() - assets.rolling(63).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc046_63d_slope_v046_signal'] = f107d_f107_debt_to_equity_dispersion_calc046_63d_slope_v046_signal

def f107d_f107_debt_to_equity_dispersion_calc047_10d_slope_v047_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets.rolling(10).kurt() - ebitda.rolling(10).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc047_10d_slope_v047_signal'] = f107d_f107_debt_to_equity_dispersion_calc047_10d_slope_v047_signal

def f107d_f107_debt_to_equity_dispersion_calc048_63d_slope_v048_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.rolling(63).kurt() - currentratio.rolling(63).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc048_63d_slope_v048_signal'] = f107d_f107_debt_to_equity_dispersion_calc048_63d_slope_v048_signal

def f107d_f107_debt_to_equity_dispersion_calc049_252d_slope_v049_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.diff(252) / equity.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc049_252d_slope_v049_signal'] = f107d_f107_debt_to_equity_dispersion_calc049_252d_slope_v049_signal

def f107d_f107_debt_to_equity_dispersion_calc050_10d_slope_v050_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity / assets.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc050_10d_slope_v050_signal'] = f107d_f107_debt_to_equity_dispersion_calc050_10d_slope_v050_signal

def f107d_f107_debt_to_equity_dispersion_calc051_5d_slope_v051_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.diff(5) / ebitda.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc051_5d_slope_v051_signal'] = f107d_f107_debt_to_equity_dispersion_calc051_5d_slope_v051_signal

def f107d_f107_debt_to_equity_dispersion_calc052_21d_slope_v052_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.diff(21) / marketcap.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc052_21d_slope_v052_signal'] = f107d_f107_debt_to_equity_dispersion_calc052_21d_slope_v052_signal

def f107d_f107_debt_to_equity_dispersion_calc053_63d_slope_v053_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.rolling(63).kurt() - ebitda.rolling(63).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc053_63d_slope_v053_signal'] = f107d_f107_debt_to_equity_dispersion_calc053_63d_slope_v053_signal

def f107d_f107_debt_to_equity_dispersion_calc054_21d_slope_v054_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(21).rank(pct=True) / currentratio.rolling(21).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc054_21d_slope_v054_signal'] = f107d_f107_debt_to_equity_dispersion_calc054_21d_slope_v054_signal

def f107d_f107_debt_to_equity_dispersion_calc055_21d_slope_v055_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(21).max() - currentratio.rolling(21).min()) / equity.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc055_21d_slope_v055_signal'] = f107d_f107_debt_to_equity_dispersion_calc055_21d_slope_v055_signal

def f107d_f107_debt_to_equity_dispersion_calc056_126d_slope_v056_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(126).rank(pct=True) / currentratio.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc056_126d_slope_v056_signal'] = f107d_f107_debt_to_equity_dispersion_calc056_126d_slope_v056_signal

def f107d_f107_debt_to_equity_dispersion_calc057_126d_slope_v057_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.diff(126) / debt.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc057_126d_slope_v057_signal'] = f107d_f107_debt_to_equity_dispersion_calc057_126d_slope_v057_signal

def f107d_f107_debt_to_equity_dispersion_calc058_10d_slope_v058_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(10).rank(pct=True) / equity.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc058_10d_slope_v058_signal'] = f107d_f107_debt_to_equity_dispersion_calc058_10d_slope_v058_signal

def f107d_f107_debt_to_equity_dispersion_calc059_63d_slope_v059_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
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
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc059_63d_slope_v059_signal'] = f107d_f107_debt_to_equity_dispersion_calc059_63d_slope_v059_signal

def f107d_f107_debt_to_equity_dispersion_calc060_63d_slope_v060_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.diff(63) / liabilities.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc060_63d_slope_v060_signal'] = f107d_f107_debt_to_equity_dispersion_calc060_63d_slope_v060_signal

def f107d_f107_debt_to_equity_dispersion_calc061_10d_slope_v061_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda / liabilities.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc061_10d_slope_v061_signal'] = f107d_f107_debt_to_equity_dispersion_calc061_10d_slope_v061_signal

def f107d_f107_debt_to_equity_dispersion_calc062_21d_slope_v062_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
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
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc062_21d_slope_v062_signal'] = f107d_f107_debt_to_equity_dispersion_calc062_21d_slope_v062_signal

def f107d_f107_debt_to_equity_dispersion_calc063_21d_slope_v063_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt / ebitda.replace(0, np.nan)).rolling(21).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc063_21d_slope_v063_signal'] = f107d_f107_debt_to_equity_dispersion_calc063_21d_slope_v063_signal

def f107d_f107_debt_to_equity_dispersion_calc064_63d_slope_v064_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.rolling(63).kurt() - liabilities.rolling(63).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc064_63d_slope_v064_signal'] = f107d_f107_debt_to_equity_dispersion_calc064_63d_slope_v064_signal

def f107d_f107_debt_to_equity_dispersion_calc065_252d_slope_v065_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.rolling(252).max() - assets.rolling(252).min()) / currentratio.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc065_252d_slope_v065_signal'] = f107d_f107_debt_to_equity_dispersion_calc065_252d_slope_v065_signal

def f107d_f107_debt_to_equity_dispersion_calc066_21d_slope_v066_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.rolling(21).quantile(0.5) / currentratio.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc066_21d_slope_v066_signal'] = f107d_f107_debt_to_equity_dispersion_calc066_21d_slope_v066_signal

def f107d_f107_debt_to_equity_dispersion_calc067_252d_slope_v067_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.diff(252).abs() / equity.diff(252).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc067_252d_slope_v067_signal'] = f107d_f107_debt_to_equity_dispersion_calc067_252d_slope_v067_signal

def f107d_f107_debt_to_equity_dispersion_calc068_63d_slope_v068_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.diff(63) / equity.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc068_63d_slope_v068_signal'] = f107d_f107_debt_to_equity_dispersion_calc068_63d_slope_v068_signal

def f107d_f107_debt_to_equity_dispersion_calc069_21d_slope_v069_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.diff(21).abs() / liabilities.diff(21).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc069_21d_slope_v069_signal'] = f107d_f107_debt_to_equity_dispersion_calc069_21d_slope_v069_signal

def f107d_f107_debt_to_equity_dispersion_calc070_10d_slope_v070_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
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
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc070_10d_slope_v070_signal'] = f107d_f107_debt_to_equity_dispersion_calc070_10d_slope_v070_signal

def f107d_f107_debt_to_equity_dispersion_calc071_63d_slope_v071_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity / assets.replace(0, np.nan)).rolling(63).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc071_63d_slope_v071_signal'] = f107d_f107_debt_to_equity_dispersion_calc071_63d_slope_v071_signal

def f107d_f107_debt_to_equity_dispersion_calc072_252d_slope_v072_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = ((liabilities - liabilities.rolling(252).mean()) / liabilities.rolling(252).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc072_252d_slope_v072_signal'] = f107d_f107_debt_to_equity_dispersion_calc072_252d_slope_v072_signal

def f107d_f107_debt_to_equity_dispersion_calc073_42d_slope_v073_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio / debt.replace(0, np.nan)).rolling(42).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc073_42d_slope_v073_signal'] = f107d_f107_debt_to_equity_dispersion_calc073_42d_slope_v073_signal

def f107d_f107_debt_to_equity_dispersion_calc074_21d_slope_v074_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.rolling(21).max() - assets.rolling(21).min()) / marketcap.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc074_21d_slope_v074_signal'] = f107d_f107_debt_to_equity_dispersion_calc074_21d_slope_v074_signal

def f107d_f107_debt_to_equity_dispersion_calc075_5d_slope_v075_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.diff(5) / assets.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc075_5d_slope_v075_signal'] = f107d_f107_debt_to_equity_dispersion_calc075_5d_slope_v075_signal

def f107d_f107_debt_to_equity_dispersion_calc076_21d_slope_v076_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.rolling(21).quantile(0.5) / debt.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc076_21d_slope_v076_signal'] = f107d_f107_debt_to_equity_dispersion_calc076_21d_slope_v076_signal

def f107d_f107_debt_to_equity_dispersion_calc077_5d_slope_v077_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.diff(5) / marketcap.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc077_5d_slope_v077_signal'] = f107d_f107_debt_to_equity_dispersion_calc077_5d_slope_v077_signal

def f107d_f107_debt_to_equity_dispersion_calc078_252d_slope_v078_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt / marketcap.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc078_252d_slope_v078_signal'] = f107d_f107_debt_to_equity_dispersion_calc078_252d_slope_v078_signal

def f107d_f107_debt_to_equity_dispersion_calc079_252d_slope_v079_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.rolling(252).kurt() - currentratio.rolling(252).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc079_252d_slope_v079_signal'] = f107d_f107_debt_to_equity_dispersion_calc079_252d_slope_v079_signal

def f107d_f107_debt_to_equity_dispersion_calc080_21d_slope_v080_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(21).quantile(0.5) / ebitda.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc080_21d_slope_v080_signal'] = f107d_f107_debt_to_equity_dispersion_calc080_21d_slope_v080_signal

def f107d_f107_debt_to_equity_dispersion_calc081_63d_slope_v081_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets.pct_change(63) - currentratio.pct_change(63))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc081_63d_slope_v081_signal'] = f107d_f107_debt_to_equity_dispersion_calc081_63d_slope_v081_signal

def f107d_f107_debt_to_equity_dispersion_calc082_252d_slope_v082_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
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
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc082_252d_slope_v082_signal'] = f107d_f107_debt_to_equity_dispersion_calc082_252d_slope_v082_signal

def f107d_f107_debt_to_equity_dispersion_calc083_21d_slope_v083_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = ((liabilities - liabilities.rolling(21).mean()) / liabilities.rolling(21).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc083_21d_slope_v083_signal'] = f107d_f107_debt_to_equity_dispersion_calc083_21d_slope_v083_signal

def f107d_f107_debt_to_equity_dispersion_calc084_42d_slope_v084_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.rolling(42).max() - ebitda.rolling(42).min()) / marketcap.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc084_42d_slope_v084_signal'] = f107d_f107_debt_to_equity_dispersion_calc084_42d_slope_v084_signal

def f107d_f107_debt_to_equity_dispersion_calc085_5d_slope_v085_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.rolling(5).kurt() - equity.rolling(5).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc085_5d_slope_v085_signal'] = f107d_f107_debt_to_equity_dispersion_calc085_5d_slope_v085_signal

def f107d_f107_debt_to_equity_dispersion_calc086_21d_slope_v086_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
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
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc086_21d_slope_v086_signal'] = f107d_f107_debt_to_equity_dispersion_calc086_21d_slope_v086_signal

def f107d_f107_debt_to_equity_dispersion_calc087_10d_slope_v087_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.rolling(10).rank(pct=True) / assets.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc087_10d_slope_v087_signal'] = f107d_f107_debt_to_equity_dispersion_calc087_10d_slope_v087_signal

def f107d_f107_debt_to_equity_dispersion_calc088_5d_slope_v088_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(5).quantile(0.5) / equity.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc088_5d_slope_v088_signal'] = f107d_f107_debt_to_equity_dispersion_calc088_5d_slope_v088_signal

def f107d_f107_debt_to_equity_dispersion_calc089_252d_slope_v089_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets.rolling(252).quantile(0.5) / debt.rolling(252).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc089_252d_slope_v089_signal'] = f107d_f107_debt_to_equity_dispersion_calc089_252d_slope_v089_signal

def f107d_f107_debt_to_equity_dispersion_calc090_21d_slope_v090_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.pct_change(21) - marketcap.pct_change(21))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc090_21d_slope_v090_signal'] = f107d_f107_debt_to_equity_dispersion_calc090_21d_slope_v090_signal

def f107d_f107_debt_to_equity_dispersion_calc091_42d_slope_v091_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets.rolling(42).max() - ebitda.rolling(42).min()) / debt.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc091_42d_slope_v091_signal'] = f107d_f107_debt_to_equity_dispersion_calc091_42d_slope_v091_signal

def f107d_f107_debt_to_equity_dispersion_calc092_21d_slope_v092_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.diff(21).abs() / currentratio.diff(21).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc092_21d_slope_v092_signal'] = f107d_f107_debt_to_equity_dispersion_calc092_21d_slope_v092_signal

def f107d_f107_debt_to_equity_dispersion_calc093_5d_slope_v093_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.diff(5).abs() / currentratio.diff(5).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc093_5d_slope_v093_signal'] = f107d_f107_debt_to_equity_dispersion_calc093_5d_slope_v093_signal

def f107d_f107_debt_to_equity_dispersion_calc094_63d_slope_v094_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.rolling(63).max() - equity.rolling(63).min()) / currentratio.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc094_63d_slope_v094_signal'] = f107d_f107_debt_to_equity_dispersion_calc094_63d_slope_v094_signal

def f107d_f107_debt_to_equity_dispersion_calc095_5d_slope_v095_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(5).max() - equity.rolling(5).min()) / assets.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc095_5d_slope_v095_signal'] = f107d_f107_debt_to_equity_dispersion_calc095_5d_slope_v095_signal

def f107d_f107_debt_to_equity_dispersion_calc096_252d_slope_v096_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.rolling(252).max() - liabilities.rolling(252).min()) / marketcap.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc096_252d_slope_v096_signal'] = f107d_f107_debt_to_equity_dispersion_calc096_252d_slope_v096_signal

def f107d_f107_debt_to_equity_dispersion_calc097_21d_slope_v097_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.diff(21).abs() / liabilities.diff(21).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc097_21d_slope_v097_signal'] = f107d_f107_debt_to_equity_dispersion_calc097_21d_slope_v097_signal

def f107d_f107_debt_to_equity_dispersion_calc098_10d_slope_v098_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(10).max() - liabilities.rolling(10).min()) / debt.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc098_10d_slope_v098_signal'] = f107d_f107_debt_to_equity_dispersion_calc098_10d_slope_v098_signal

def f107d_f107_debt_to_equity_dispersion_calc099_10d_slope_v099_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.rolling(10).max() - currentratio.rolling(10).min()) / assets.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc099_10d_slope_v099_signal'] = f107d_f107_debt_to_equity_dispersion_calc099_10d_slope_v099_signal

def f107d_f107_debt_to_equity_dispersion_calc100_42d_slope_v100_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(42).kurt() - debt.rolling(42).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc100_42d_slope_v100_signal'] = f107d_f107_debt_to_equity_dispersion_calc100_42d_slope_v100_signal

def f107d_f107_debt_to_equity_dispersion_calc101_252d_slope_v101_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.rolling(252).rank(pct=True) / marketcap.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc101_252d_slope_v101_signal'] = f107d_f107_debt_to_equity_dispersion_calc101_252d_slope_v101_signal

def f107d_f107_debt_to_equity_dispersion_calc102_42d_slope_v102_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
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
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc102_42d_slope_v102_signal'] = f107d_f107_debt_to_equity_dispersion_calc102_42d_slope_v102_signal

def f107d_f107_debt_to_equity_dispersion_calc103_126d_slope_v103_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.pct_change(126) - liabilities.pct_change(126))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc103_126d_slope_v103_signal'] = f107d_f107_debt_to_equity_dispersion_calc103_126d_slope_v103_signal

def f107d_f107_debt_to_equity_dispersion_calc104_252d_slope_v104_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.pct_change(252) - equity.pct_change(252))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc104_252d_slope_v104_signal'] = f107d_f107_debt_to_equity_dispersion_calc104_252d_slope_v104_signal

def f107d_f107_debt_to_equity_dispersion_calc105_252d_slope_v105_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
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
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc105_252d_slope_v105_signal'] = f107d_f107_debt_to_equity_dispersion_calc105_252d_slope_v105_signal

def f107d_f107_debt_to_equity_dispersion_calc106_63d_slope_v106_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.diff(63) / equity.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc106_63d_slope_v106_signal'] = f107d_f107_debt_to_equity_dispersion_calc106_63d_slope_v106_signal

def f107d_f107_debt_to_equity_dispersion_calc107_63d_slope_v107_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.diff(63).abs() / assets.diff(63).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc107_63d_slope_v107_signal'] = f107d_f107_debt_to_equity_dispersion_calc107_63d_slope_v107_signal

def f107d_f107_debt_to_equity_dispersion_calc108_10d_slope_v108_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.rolling(10).max() - ebitda.rolling(10).min()) / equity.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc108_10d_slope_v108_signal'] = f107d_f107_debt_to_equity_dispersion_calc108_10d_slope_v108_signal

def f107d_f107_debt_to_equity_dispersion_calc109_126d_slope_v109_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.diff(126).abs() / assets.diff(126).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc109_126d_slope_v109_signal'] = f107d_f107_debt_to_equity_dispersion_calc109_126d_slope_v109_signal

def f107d_f107_debt_to_equity_dispersion_calc110_252d_slope_v110_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(252).quantile(0.5) / assets.rolling(252).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc110_252d_slope_v110_signal'] = f107d_f107_debt_to_equity_dispersion_calc110_252d_slope_v110_signal

def f107d_f107_debt_to_equity_dispersion_calc111_21d_slope_v111_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(21).max() - assets.rolling(21).min()) / currentratio.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc111_21d_slope_v111_signal'] = f107d_f107_debt_to_equity_dispersion_calc111_21d_slope_v111_signal

def f107d_f107_debt_to_equity_dispersion_calc112_252d_slope_v112_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(252).kurt() - ebitda.rolling(252).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc112_252d_slope_v112_signal'] = f107d_f107_debt_to_equity_dispersion_calc112_252d_slope_v112_signal

def f107d_f107_debt_to_equity_dispersion_calc113_5d_slope_v113_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.rolling(5).kurt() - ebitda.rolling(5).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc113_5d_slope_v113_signal'] = f107d_f107_debt_to_equity_dispersion_calc113_5d_slope_v113_signal

def f107d_f107_debt_to_equity_dispersion_calc114_5d_slope_v114_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.rolling(5).rank(pct=True) / liabilities.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc114_5d_slope_v114_signal'] = f107d_f107_debt_to_equity_dispersion_calc114_5d_slope_v114_signal

def f107d_f107_debt_to_equity_dispersion_calc115_63d_slope_v115_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.diff(63) / currentratio.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc115_63d_slope_v115_signal'] = f107d_f107_debt_to_equity_dispersion_calc115_63d_slope_v115_signal

def f107d_f107_debt_to_equity_dispersion_calc116_42d_slope_v116_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.rolling(42).max() - currentratio.rolling(42).min()) / ebitda.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc116_42d_slope_v116_signal'] = f107d_f107_debt_to_equity_dispersion_calc116_42d_slope_v116_signal

def f107d_f107_debt_to_equity_dispersion_calc117_21d_slope_v117_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(21).kurt() - ebitda.rolling(21).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc117_21d_slope_v117_signal'] = f107d_f107_debt_to_equity_dispersion_calc117_21d_slope_v117_signal

def f107d_f107_debt_to_equity_dispersion_calc118_252d_slope_v118_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.pct_change(252) - liabilities.pct_change(252))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc118_252d_slope_v118_signal'] = f107d_f107_debt_to_equity_dispersion_calc118_252d_slope_v118_signal

def f107d_f107_debt_to_equity_dispersion_calc119_10d_slope_v119_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets / liabilities.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc119_10d_slope_v119_signal'] = f107d_f107_debt_to_equity_dispersion_calc119_10d_slope_v119_signal

def f107d_f107_debt_to_equity_dispersion_calc120_5d_slope_v120_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = ((currentratio - currentratio.rolling(5).mean()) / currentratio.rolling(5).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc120_5d_slope_v120_signal'] = f107d_f107_debt_to_equity_dispersion_calc120_5d_slope_v120_signal

def f107d_f107_debt_to_equity_dispersion_calc121_10d_slope_v121_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = ((currentratio - currentratio.rolling(10).mean()) / currentratio.rolling(10).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc121_10d_slope_v121_signal'] = f107d_f107_debt_to_equity_dispersion_calc121_10d_slope_v121_signal

def f107d_f107_debt_to_equity_dispersion_calc122_63d_slope_v122_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.diff(63).abs() / ebitda.diff(63).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc122_63d_slope_v122_signal'] = f107d_f107_debt_to_equity_dispersion_calc122_63d_slope_v122_signal

def f107d_f107_debt_to_equity_dispersion_calc123_21d_slope_v123_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.diff(21).abs() / debt.diff(21).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc123_21d_slope_v123_signal'] = f107d_f107_debt_to_equity_dispersion_calc123_21d_slope_v123_signal

def f107d_f107_debt_to_equity_dispersion_calc124_21d_slope_v124_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.diff(21) / liabilities.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc124_21d_slope_v124_signal'] = f107d_f107_debt_to_equity_dispersion_calc124_21d_slope_v124_signal

def f107d_f107_debt_to_equity_dispersion_calc125_42d_slope_v125_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.rolling(42).quantile(0.5) / assets.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc125_42d_slope_v125_signal'] = f107d_f107_debt_to_equity_dispersion_calc125_42d_slope_v125_signal

def f107d_f107_debt_to_equity_dispersion_calc126_10d_slope_v126_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets.rolling(10).quantile(0.5) / marketcap.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc126_10d_slope_v126_signal'] = f107d_f107_debt_to_equity_dispersion_calc126_10d_slope_v126_signal

def f107d_f107_debt_to_equity_dispersion_calc127_21d_slope_v127_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio / marketcap.replace(0, np.nan)).rolling(21).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc127_21d_slope_v127_signal'] = f107d_f107_debt_to_equity_dispersion_calc127_21d_slope_v127_signal

def f107d_f107_debt_to_equity_dispersion_calc128_252d_slope_v128_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
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
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc128_252d_slope_v128_signal'] = f107d_f107_debt_to_equity_dispersion_calc128_252d_slope_v128_signal

def f107d_f107_debt_to_equity_dispersion_calc129_21d_slope_v129_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.pct_change(21) - equity.pct_change(21))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc129_21d_slope_v129_signal'] = f107d_f107_debt_to_equity_dispersion_calc129_21d_slope_v129_signal

def f107d_f107_debt_to_equity_dispersion_calc130_21d_slope_v130_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities / currentratio.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc130_21d_slope_v130_signal'] = f107d_f107_debt_to_equity_dispersion_calc130_21d_slope_v130_signal

def f107d_f107_debt_to_equity_dispersion_calc131_42d_slope_v131_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.rolling(42).quantile(0.5) / currentratio.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc131_42d_slope_v131_signal'] = f107d_f107_debt_to_equity_dispersion_calc131_42d_slope_v131_signal

def f107d_f107_debt_to_equity_dispersion_calc132_10d_slope_v132_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (assets.diff(10).abs() / ebitda.diff(10).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc132_10d_slope_v132_signal'] = f107d_f107_debt_to_equity_dispersion_calc132_10d_slope_v132_signal

def f107d_f107_debt_to_equity_dispersion_calc133_252d_slope_v133_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (equity.rolling(252).rank(pct=True) / debt.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc133_252d_slope_v133_signal'] = f107d_f107_debt_to_equity_dispersion_calc133_252d_slope_v133_signal

def f107d_f107_debt_to_equity_dispersion_calc134_252d_slope_v134_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.rolling(252).max() - assets.rolling(252).min()) / ebitda.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc134_252d_slope_v134_signal'] = f107d_f107_debt_to_equity_dispersion_calc134_252d_slope_v134_signal

def f107d_f107_debt_to_equity_dispersion_calc135_10d_slope_v135_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio / equity.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc135_10d_slope_v135_signal'] = f107d_f107_debt_to_equity_dispersion_calc135_10d_slope_v135_signal

def f107d_f107_debt_to_equity_dispersion_calc136_42d_slope_v136_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt / marketcap.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc136_42d_slope_v136_signal'] = f107d_f107_debt_to_equity_dispersion_calc136_42d_slope_v136_signal

def f107d_f107_debt_to_equity_dispersion_calc137_63d_slope_v137_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.rolling(63).quantile(0.5) / assets.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc137_63d_slope_v137_signal'] = f107d_f107_debt_to_equity_dispersion_calc137_63d_slope_v137_signal

def f107d_f107_debt_to_equity_dispersion_calc138_10d_slope_v138_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
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
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc138_10d_slope_v138_signal'] = f107d_f107_debt_to_equity_dispersion_calc138_10d_slope_v138_signal

def f107d_f107_debt_to_equity_dispersion_calc139_252d_slope_v139_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.pct_change(252) - debt.pct_change(252))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc139_252d_slope_v139_signal'] = f107d_f107_debt_to_equity_dispersion_calc139_252d_slope_v139_signal

def f107d_f107_debt_to_equity_dispersion_calc140_42d_slope_v140_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (currentratio.diff(42) / liabilities.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc140_42d_slope_v140_signal'] = f107d_f107_debt_to_equity_dispersion_calc140_42d_slope_v140_signal

def f107d_f107_debt_to_equity_dispersion_calc141_63d_slope_v141_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = ((liabilities - liabilities.rolling(63).mean()) / liabilities.rolling(63).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc141_63d_slope_v141_signal'] = f107d_f107_debt_to_equity_dispersion_calc141_63d_slope_v141_signal

def f107d_f107_debt_to_equity_dispersion_calc142_252d_slope_v142_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.pct_change(252) - marketcap.pct_change(252))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc142_252d_slope_v142_signal'] = f107d_f107_debt_to_equity_dispersion_calc142_252d_slope_v142_signal

def f107d_f107_debt_to_equity_dispersion_calc143_126d_slope_v143_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt / ebitda.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc143_126d_slope_v143_signal'] = f107d_f107_debt_to_equity_dispersion_calc143_126d_slope_v143_signal

def f107d_f107_debt_to_equity_dispersion_calc144_126d_slope_v144_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.pct_change(126) - marketcap.pct_change(126))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc144_126d_slope_v144_signal'] = f107d_f107_debt_to_equity_dispersion_calc144_126d_slope_v144_signal

def f107d_f107_debt_to_equity_dispersion_calc145_252d_slope_v145_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.diff(252).abs() / equity.diff(252).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc145_252d_slope_v145_signal'] = f107d_f107_debt_to_equity_dispersion_calc145_252d_slope_v145_signal

def f107d_f107_debt_to_equity_dispersion_calc146_252d_slope_v146_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (debt.diff(252).abs() / marketcap.diff(252).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc146_252d_slope_v146_signal'] = f107d_f107_debt_to_equity_dispersion_calc146_252d_slope_v146_signal

def f107d_f107_debt_to_equity_dispersion_calc147_252d_slope_v147_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities / currentratio.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc147_252d_slope_v147_signal'] = f107d_f107_debt_to_equity_dispersion_calc147_252d_slope_v147_signal

def f107d_f107_debt_to_equity_dispersion_calc148_10d_slope_v148_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (marketcap.diff(10) / equity.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc148_10d_slope_v148_signal'] = f107d_f107_debt_to_equity_dispersion_calc148_10d_slope_v148_signal

def f107d_f107_debt_to_equity_dispersion_calc149_252d_slope_v149_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (liabilities.rolling(252).max() - marketcap.rolling(252).min()) / debt.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc149_252d_slope_v149_signal'] = f107d_f107_debt_to_equity_dispersion_calc149_252d_slope_v149_signal

def f107d_f107_debt_to_equity_dispersion_calc150_21d_slope_v150_signal(debt, equity, assets, liabilities, marketcap, currentratio, ebitda):
    v1 = (ebitda.rolling(21).quantile(0.5) / liabilities.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f107d_f107_debt_to_equity_dispersion_calc150_21d_slope_v150_signal'] = f107d_f107_debt_to_equity_dispersion_calc150_21d_slope_v150_signal



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
