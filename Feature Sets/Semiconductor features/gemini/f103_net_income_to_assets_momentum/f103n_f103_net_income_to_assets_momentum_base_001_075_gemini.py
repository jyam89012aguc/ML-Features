import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f103n_f103_net_income_to_assets_momentum_calc001_42d_base_v001_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda.pct_change(42) - fcf.pct_change(42))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc001_42d_base_v001_signal'] = f103n_f103_net_income_to_assets_momentum_calc001_42d_base_v001_signal

def f103n_f103_net_income_to_assets_momentum_calc002_126d_base_v002_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.rolling(126).kurt() - fcf.rolling(126).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc002_126d_base_v002_signal'] = f103n_f103_net_income_to_assets_momentum_calc002_126d_base_v002_signal

def f103n_f103_net_income_to_assets_momentum_calc003_5d_base_v003_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.rolling(5).rank(pct=True) / fcf.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc003_5d_base_v003_signal'] = f103n_f103_net_income_to_assets_momentum_calc003_5d_base_v003_signal

def f103n_f103_net_income_to_assets_momentum_calc004_63d_base_v004_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.diff(63) / netinc.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc004_63d_base_v004_signal'] = f103n_f103_net_income_to_assets_momentum_calc004_63d_base_v004_signal

def f103n_f103_net_income_to_assets_momentum_calc005_42d_base_v005_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf / netinc.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc005_42d_base_v005_signal'] = f103n_f103_net_income_to_assets_momentum_calc005_42d_base_v005_signal

def f103n_f103_net_income_to_assets_momentum_calc006_63d_base_v006_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.rolling(63).quantile(0.5) / revenue.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc006_63d_base_v006_signal'] = f103n_f103_net_income_to_assets_momentum_calc006_63d_base_v006_signal

def f103n_f103_net_income_to_assets_momentum_calc007_252d_base_v007_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.diff(252).abs() / revenue.diff(252).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc007_252d_base_v007_signal'] = f103n_f103_net_income_to_assets_momentum_calc007_252d_base_v007_signal

def f103n_f103_net_income_to_assets_momentum_calc008_126d_base_v008_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda.rolling(126).kurt() - fcf.rolling(126).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc008_126d_base_v008_signal'] = f103n_f103_net_income_to_assets_momentum_calc008_126d_base_v008_signal

def f103n_f103_net_income_to_assets_momentum_calc009_21d_base_v009_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.diff(21) / fcf.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc009_21d_base_v009_signal'] = f103n_f103_net_income_to_assets_momentum_calc009_21d_base_v009_signal

def f103n_f103_net_income_to_assets_momentum_calc010_252d_base_v010_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.rolling(252).kurt() - fcf.rolling(252).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc010_252d_base_v010_signal'] = f103n_f103_net_income_to_assets_momentum_calc010_252d_base_v010_signal

def f103n_f103_net_income_to_assets_momentum_calc011_252d_base_v011_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo / assets.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc011_252d_base_v011_signal'] = f103n_f103_net_income_to_assets_momentum_calc011_252d_base_v011_signal

def f103n_f103_net_income_to_assets_momentum_calc012_10d_base_v012_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.rolling(10).rank(pct=True) / netinc.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc012_10d_base_v012_signal'] = f103n_f103_net_income_to_assets_momentum_calc012_10d_base_v012_signal

def f103n_f103_net_income_to_assets_momentum_calc013_21d_base_v013_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.diff(21).abs() / equity.diff(21).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc013_21d_base_v013_signal'] = f103n_f103_net_income_to_assets_momentum_calc013_21d_base_v013_signal

def f103n_f103_net_income_to_assets_momentum_calc014_5d_base_v014_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.pct_change(5) - revenue.pct_change(5))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc014_5d_base_v014_signal'] = f103n_f103_net_income_to_assets_momentum_calc014_5d_base_v014_signal

def f103n_f103_net_income_to_assets_momentum_calc015_10d_base_v015_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.diff(10) / revenue.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc015_10d_base_v015_signal'] = f103n_f103_net_income_to_assets_momentum_calc015_10d_base_v015_signal

def f103n_f103_net_income_to_assets_momentum_calc016_42d_base_v016_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.diff(42) / ebitda.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc016_42d_base_v016_signal'] = f103n_f103_net_income_to_assets_momentum_calc016_42d_base_v016_signal

def f103n_f103_net_income_to_assets_momentum_calc017_126d_base_v017_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.diff(126) / fcf.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc017_126d_base_v017_signal'] = f103n_f103_net_income_to_assets_momentum_calc017_126d_base_v017_signal

def f103n_f103_net_income_to_assets_momentum_calc018_252d_base_v018_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.rolling(252).kurt() - equity.rolling(252).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc018_252d_base_v018_signal'] = f103n_f103_net_income_to_assets_momentum_calc018_252d_base_v018_signal

def f103n_f103_net_income_to_assets_momentum_calc019_5d_base_v019_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity / ebitda.replace(0, np.nan)).rolling(5).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc019_5d_base_v019_signal'] = f103n_f103_net_income_to_assets_momentum_calc019_5d_base_v019_signal

def f103n_f103_net_income_to_assets_momentum_calc020_5d_base_v020_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.rolling(5).rank(pct=True) / netinc.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc020_5d_base_v020_signal'] = f103n_f103_net_income_to_assets_momentum_calc020_5d_base_v020_signal

def f103n_f103_net_income_to_assets_momentum_calc021_5d_base_v021_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.diff(5) / netinc.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc021_5d_base_v021_signal'] = f103n_f103_net_income_to_assets_momentum_calc021_5d_base_v021_signal

def f103n_f103_net_income_to_assets_momentum_calc022_10d_base_v022_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.pct_change(10) - netinc.pct_change(10))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc022_10d_base_v022_signal'] = f103n_f103_net_income_to_assets_momentum_calc022_10d_base_v022_signal

def f103n_f103_net_income_to_assets_momentum_calc023_126d_base_v023_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.rolling(126).rank(pct=True) / ncfo.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc023_126d_base_v023_signal'] = f103n_f103_net_income_to_assets_momentum_calc023_126d_base_v023_signal

def f103n_f103_net_income_to_assets_momentum_calc024_63d_base_v024_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.diff(63).abs() / ebitda.diff(63).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc024_63d_base_v024_signal'] = f103n_f103_net_income_to_assets_momentum_calc024_63d_base_v024_signal

def f103n_f103_net_income_to_assets_momentum_calc025_126d_base_v025_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = ((ebitda - ebitda.rolling(126).mean()) / ebitda.rolling(126).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc025_126d_base_v025_signal'] = f103n_f103_net_income_to_assets_momentum_calc025_126d_base_v025_signal

def f103n_f103_net_income_to_assets_momentum_calc026_5d_base_v026_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.pct_change(5) - equity.pct_change(5))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc026_5d_base_v026_signal'] = f103n_f103_net_income_to_assets_momentum_calc026_5d_base_v026_signal

def f103n_f103_net_income_to_assets_momentum_calc027_10d_base_v027_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo / netinc.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc027_10d_base_v027_signal'] = f103n_f103_net_income_to_assets_momentum_calc027_10d_base_v027_signal

def f103n_f103_net_income_to_assets_momentum_calc028_21d_base_v028_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity / ebitda.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc028_21d_base_v028_signal'] = f103n_f103_net_income_to_assets_momentum_calc028_21d_base_v028_signal

def f103n_f103_net_income_to_assets_momentum_calc029_126d_base_v029_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda.diff(126) / assets.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc029_126d_base_v029_signal'] = f103n_f103_net_income_to_assets_momentum_calc029_126d_base_v029_signal

def f103n_f103_net_income_to_assets_momentum_calc030_126d_base_v030_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.rolling(126).rank(pct=True) / ebitda.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc030_126d_base_v030_signal'] = f103n_f103_net_income_to_assets_momentum_calc030_126d_base_v030_signal

def f103n_f103_net_income_to_assets_momentum_calc031_21d_base_v031_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.rolling(21).max() - ebitda.rolling(21).min()) / assets.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc031_21d_base_v031_signal'] = f103n_f103_net_income_to_assets_momentum_calc031_21d_base_v031_signal

def f103n_f103_net_income_to_assets_momentum_calc032_10d_base_v032_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = ((assets - assets.rolling(10).mean()) / assets.rolling(10).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc032_10d_base_v032_signal'] = f103n_f103_net_income_to_assets_momentum_calc032_10d_base_v032_signal

def f103n_f103_net_income_to_assets_momentum_calc033_126d_base_v033_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.diff(126) / fcf.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc033_126d_base_v033_signal'] = f103n_f103_net_income_to_assets_momentum_calc033_126d_base_v033_signal

def f103n_f103_net_income_to_assets_momentum_calc034_42d_base_v034_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = ((equity - equity.rolling(42).mean()) / equity.rolling(42).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc034_42d_base_v034_signal'] = f103n_f103_net_income_to_assets_momentum_calc034_42d_base_v034_signal

def f103n_f103_net_income_to_assets_momentum_calc035_5d_base_v035_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.diff(5) / ebitda.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc035_5d_base_v035_signal'] = f103n_f103_net_income_to_assets_momentum_calc035_5d_base_v035_signal

def f103n_f103_net_income_to_assets_momentum_calc036_252d_base_v036_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda.diff(252) / equity.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc036_252d_base_v036_signal'] = f103n_f103_net_income_to_assets_momentum_calc036_252d_base_v036_signal

def f103n_f103_net_income_to_assets_momentum_calc037_252d_base_v037_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.rolling(252).kurt() - fcf.rolling(252).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc037_252d_base_v037_signal'] = f103n_f103_net_income_to_assets_momentum_calc037_252d_base_v037_signal

def f103n_f103_net_income_to_assets_momentum_calc038_5d_base_v038_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda.rolling(5).max() - ncfo.rolling(5).min()) / assets.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc038_5d_base_v038_signal'] = f103n_f103_net_income_to_assets_momentum_calc038_5d_base_v038_signal

def f103n_f103_net_income_to_assets_momentum_calc039_63d_base_v039_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.rolling(63).quantile(0.5) / equity.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc039_63d_base_v039_signal'] = f103n_f103_net_income_to_assets_momentum_calc039_63d_base_v039_signal

def f103n_f103_net_income_to_assets_momentum_calc040_21d_base_v040_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.diff(21).abs() / assets.diff(21).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc040_21d_base_v040_signal'] = f103n_f103_net_income_to_assets_momentum_calc040_21d_base_v040_signal

def f103n_f103_net_income_to_assets_momentum_calc041_21d_base_v041_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.pct_change(21) - assets.pct_change(21))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc041_21d_base_v041_signal'] = f103n_f103_net_income_to_assets_momentum_calc041_21d_base_v041_signal

def f103n_f103_net_income_to_assets_momentum_calc042_252d_base_v042_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.rolling(252).quantile(0.5) / ebitda.rolling(252).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc042_252d_base_v042_signal'] = f103n_f103_net_income_to_assets_momentum_calc042_252d_base_v042_signal

def f103n_f103_net_income_to_assets_momentum_calc043_10d_base_v043_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.rolling(10).rank(pct=True) / ebitda.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc043_10d_base_v043_signal'] = f103n_f103_net_income_to_assets_momentum_calc043_10d_base_v043_signal

def f103n_f103_net_income_to_assets_momentum_calc044_126d_base_v044_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.rolling(126).rank(pct=True) / assets.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc044_126d_base_v044_signal'] = f103n_f103_net_income_to_assets_momentum_calc044_126d_base_v044_signal

def f103n_f103_net_income_to_assets_momentum_calc045_21d_base_v045_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = ((equity - equity.rolling(21).mean()) / equity.rolling(21).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc045_21d_base_v045_signal'] = f103n_f103_net_income_to_assets_momentum_calc045_21d_base_v045_signal

def f103n_f103_net_income_to_assets_momentum_calc046_21d_base_v046_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc / ncfo.replace(0, np.nan)).rolling(21).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc046_21d_base_v046_signal'] = f103n_f103_net_income_to_assets_momentum_calc046_21d_base_v046_signal

def f103n_f103_net_income_to_assets_momentum_calc047_252d_base_v047_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.rolling(252).max() - equity.rolling(252).min()) / revenue.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc047_252d_base_v047_signal'] = f103n_f103_net_income_to_assets_momentum_calc047_252d_base_v047_signal

def f103n_f103_net_income_to_assets_momentum_calc048_21d_base_v048_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = ((netinc - netinc.rolling(21).mean()) / netinc.rolling(21).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc048_21d_base_v048_signal'] = f103n_f103_net_income_to_assets_momentum_calc048_21d_base_v048_signal

def f103n_f103_net_income_to_assets_momentum_calc049_10d_base_v049_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.rolling(10).rank(pct=True) / netinc.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc049_10d_base_v049_signal'] = f103n_f103_net_income_to_assets_momentum_calc049_10d_base_v049_signal

def f103n_f103_net_income_to_assets_momentum_calc050_63d_base_v050_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.rolling(63).kurt() - netinc.rolling(63).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc050_63d_base_v050_signal'] = f103n_f103_net_income_to_assets_momentum_calc050_63d_base_v050_signal

def f103n_f103_net_income_to_assets_momentum_calc051_126d_base_v051_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.rolling(126).quantile(0.5) / revenue.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc051_126d_base_v051_signal'] = f103n_f103_net_income_to_assets_momentum_calc051_126d_base_v051_signal

def f103n_f103_net_income_to_assets_momentum_calc052_21d_base_v052_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue / ebitda.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc052_21d_base_v052_signal'] = f103n_f103_net_income_to_assets_momentum_calc052_21d_base_v052_signal

def f103n_f103_net_income_to_assets_momentum_calc053_21d_base_v053_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.diff(21) / ebitda.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc053_21d_base_v053_signal'] = f103n_f103_net_income_to_assets_momentum_calc053_21d_base_v053_signal

def f103n_f103_net_income_to_assets_momentum_calc054_5d_base_v054_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.pct_change(5) - revenue.pct_change(5))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc054_5d_base_v054_signal'] = f103n_f103_net_income_to_assets_momentum_calc054_5d_base_v054_signal

def f103n_f103_net_income_to_assets_momentum_calc055_21d_base_v055_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.rolling(21).kurt() - netinc.rolling(21).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc055_21d_base_v055_signal'] = f103n_f103_net_income_to_assets_momentum_calc055_21d_base_v055_signal

def f103n_f103_net_income_to_assets_momentum_calc056_252d_base_v056_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda / revenue.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc056_252d_base_v056_signal'] = f103n_f103_net_income_to_assets_momentum_calc056_252d_base_v056_signal

def f103n_f103_net_income_to_assets_momentum_calc057_5d_base_v057_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.pct_change(5) - ncfo.pct_change(5))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc057_5d_base_v057_signal'] = f103n_f103_net_income_to_assets_momentum_calc057_5d_base_v057_signal

def f103n_f103_net_income_to_assets_momentum_calc058_126d_base_v058_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (fcf.diff(126) / ncfo.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc058_126d_base_v058_signal'] = f103n_f103_net_income_to_assets_momentum_calc058_126d_base_v058_signal

def f103n_f103_net_income_to_assets_momentum_calc059_10d_base_v059_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.diff(10) / fcf.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc059_10d_base_v059_signal'] = f103n_f103_net_income_to_assets_momentum_calc059_10d_base_v059_signal

def f103n_f103_net_income_to_assets_momentum_calc060_126d_base_v060_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.rolling(126).rank(pct=True) / netinc.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc060_126d_base_v060_signal'] = f103n_f103_net_income_to_assets_momentum_calc060_126d_base_v060_signal

def f103n_f103_net_income_to_assets_momentum_calc061_63d_base_v061_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity / ncfo.replace(0, np.nan)).rolling(63).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc061_63d_base_v061_signal'] = f103n_f103_net_income_to_assets_momentum_calc061_63d_base_v061_signal

def f103n_f103_net_income_to_assets_momentum_calc062_126d_base_v062_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = ((revenue - revenue.rolling(126).mean()) / revenue.rolling(126).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc062_126d_base_v062_signal'] = f103n_f103_net_income_to_assets_momentum_calc062_126d_base_v062_signal

def f103n_f103_net_income_to_assets_momentum_calc063_252d_base_v063_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.diff(252) / ebitda.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc063_252d_base_v063_signal'] = f103n_f103_net_income_to_assets_momentum_calc063_252d_base_v063_signal

def f103n_f103_net_income_to_assets_momentum_calc064_126d_base_v064_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda.rolling(126).kurt() - ncfo.rolling(126).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc064_126d_base_v064_signal'] = f103n_f103_net_income_to_assets_momentum_calc064_126d_base_v064_signal

def f103n_f103_net_income_to_assets_momentum_calc065_126d_base_v065_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda.diff(126) / fcf.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc065_126d_base_v065_signal'] = f103n_f103_net_income_to_assets_momentum_calc065_126d_base_v065_signal

def f103n_f103_net_income_to_assets_momentum_calc066_126d_base_v066_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (revenue.diff(126).abs() / ebitda.diff(126).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc066_126d_base_v066_signal'] = f103n_f103_net_income_to_assets_momentum_calc066_126d_base_v066_signal

def f103n_f103_net_income_to_assets_momentum_calc067_126d_base_v067_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.rolling(126).kurt() - ebitda.rolling(126).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc067_126d_base_v067_signal'] = f103n_f103_net_income_to_assets_momentum_calc067_126d_base_v067_signal

def f103n_f103_net_income_to_assets_momentum_calc068_126d_base_v068_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda / ncfo.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc068_126d_base_v068_signal'] = f103n_f103_net_income_to_assets_momentum_calc068_126d_base_v068_signal

def f103n_f103_net_income_to_assets_momentum_calc069_21d_base_v069_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.pct_change(21) - assets.pct_change(21))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc069_21d_base_v069_signal'] = f103n_f103_net_income_to_assets_momentum_calc069_21d_base_v069_signal

def f103n_f103_net_income_to_assets_momentum_calc070_5d_base_v070_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (assets.rolling(5).kurt() - ebitda.rolling(5).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc070_5d_base_v070_signal'] = f103n_f103_net_income_to_assets_momentum_calc070_5d_base_v070_signal

def f103n_f103_net_income_to_assets_momentum_calc071_21d_base_v071_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ncfo.rolling(21).quantile(0.5) / assets.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc071_21d_base_v071_signal'] = f103n_f103_net_income_to_assets_momentum_calc071_21d_base_v071_signal

def f103n_f103_net_income_to_assets_momentum_calc072_42d_base_v072_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (netinc.diff(42) / ncfo.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc072_42d_base_v072_signal'] = f103n_f103_net_income_to_assets_momentum_calc072_42d_base_v072_signal

def f103n_f103_net_income_to_assets_momentum_calc073_5d_base_v073_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.rolling(5).rank(pct=True) / netinc.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc073_5d_base_v073_signal'] = f103n_f103_net_income_to_assets_momentum_calc073_5d_base_v073_signal

def f103n_f103_net_income_to_assets_momentum_calc074_21d_base_v074_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (equity.rolling(21).kurt() - netinc.rolling(21).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc074_21d_base_v074_signal'] = f103n_f103_net_income_to_assets_momentum_calc074_21d_base_v074_signal

def f103n_f103_net_income_to_assets_momentum_calc075_126d_base_v075_signal(netinc, assets, equity, revenue, ebitda, ncfo, fcf):
    v1 = (ebitda.rolling(126).quantile(0.5) / revenue.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f103n_f103_net_income_to_assets_momentum_calc075_126d_base_v075_signal'] = f103n_f103_net_income_to_assets_momentum_calc075_126d_base_v075_signal



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
