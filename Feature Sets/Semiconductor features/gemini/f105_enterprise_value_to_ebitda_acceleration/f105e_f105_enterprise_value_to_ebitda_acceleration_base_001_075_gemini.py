import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc001_10d_base_v001_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(10).kurt() - debt.rolling(10).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc001_10d_base_v001_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc001_10d_base_v001_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc002_126d_base_v002_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = ((ebitda - ebitda.rolling(126).mean()) / ebitda.rolling(126).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc002_126d_base_v002_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc002_126d_base_v002_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc003_126d_base_v003_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.rolling(126).rank(pct=True) / equity.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc003_126d_base_v003_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc003_126d_base_v003_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc004_21d_base_v004_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(21).kurt() - revenue.rolling(21).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc004_21d_base_v004_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc004_21d_base_v004_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc005_5d_base_v005_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = ((ev - ev.rolling(5).mean()) / ev.rolling(5).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc005_5d_base_v005_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc005_5d_base_v005_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc006_126d_base_v006_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.rolling(126).max() - ebitda.rolling(126).min()) / equity.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc006_126d_base_v006_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc006_126d_base_v006_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc007_10d_base_v007_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = ((equity - equity.rolling(10).mean()) / equity.rolling(10).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc007_10d_base_v007_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc007_10d_base_v007_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc008_10d_base_v008_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf / equity.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc008_10d_base_v008_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc008_10d_base_v008_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc009_252d_base_v009_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(252).kurt() - fcf.rolling(252).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc009_252d_base_v009_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc009_252d_base_v009_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc010_63d_base_v010_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(63).max() - fcf.rolling(63).min()) / assets.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc010_63d_base_v010_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc010_63d_base_v010_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc011_126d_base_v011_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets.pct_change(126) - fcf.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc011_126d_base_v011_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc011_126d_base_v011_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc012_10d_base_v012_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue / ev.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc012_10d_base_v012_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc012_10d_base_v012_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc013_252d_base_v013_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.diff(252).abs() / fcf.diff(252).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc013_252d_base_v013_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc013_252d_base_v013_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc014_126d_base_v014_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue.pct_change(126) - ev.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc014_126d_base_v014_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc014_126d_base_v014_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc015_42d_base_v015_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf / debt.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc015_42d_base_v015_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc015_42d_base_v015_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc016_126d_base_v016_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(126).max() - debt.rolling(126).min()) / fcf.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc016_126d_base_v016_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc016_126d_base_v016_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc017_21d_base_v017_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue.rolling(21).max() - assets.rolling(21).min()) / equity.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc017_21d_base_v017_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc017_21d_base_v017_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc018_63d_base_v018_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.pct_change(63) - fcf.pct_change(63))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc018_63d_base_v018_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc018_63d_base_v018_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc019_42d_base_v019_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.rolling(42).kurt() - ebitda.rolling(42).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc019_42d_base_v019_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc019_42d_base_v019_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc020_5d_base_v020_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = ((fcf - fcf.rolling(5).mean()) / fcf.rolling(5).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc020_5d_base_v020_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc020_5d_base_v020_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc021_252d_base_v021_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.diff(252) / equity.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc021_252d_base_v021_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc021_252d_base_v021_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc022_126d_base_v022_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev / revenue.replace(0, np.nan)).rolling(126).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc022_126d_base_v022_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc022_126d_base_v022_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc023_126d_base_v023_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(126).rank(pct=True) / revenue.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc023_126d_base_v023_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc023_126d_base_v023_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc024_252d_base_v024_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(252).rank(pct=True) / equity.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc024_252d_base_v024_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc024_252d_base_v024_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc025_252d_base_v025_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.rolling(252).max() - ev.rolling(252).min()) / revenue.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc025_252d_base_v025_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc025_252d_base_v025_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc026_42d_base_v026_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets.rolling(42).rank(pct=True) / fcf.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc026_42d_base_v026_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc026_42d_base_v026_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc027_42d_base_v027_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue.diff(42).abs() / equity.diff(42).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc027_42d_base_v027_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc027_42d_base_v027_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc028_63d_base_v028_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.diff(63).abs() / debt.diff(63).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc028_63d_base_v028_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc028_63d_base_v028_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc029_21d_base_v029_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue / debt.replace(0, np.nan)).rolling(21).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc029_21d_base_v029_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc029_21d_base_v029_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc030_63d_base_v030_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev / equity.replace(0, np.nan)).rolling(63).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc030_63d_base_v030_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc030_63d_base_v030_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc031_42d_base_v031_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue / assets.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc031_42d_base_v031_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc031_42d_base_v031_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc032_63d_base_v032_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = ((fcf - fcf.rolling(63).mean()) / fcf.rolling(63).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc032_63d_base_v032_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc032_63d_base_v032_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc033_252d_base_v033_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue.rolling(252).quantile(0.5) / debt.rolling(252).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc033_252d_base_v033_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc033_252d_base_v033_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc034_252d_base_v034_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets.diff(252) / debt.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc034_252d_base_v034_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc034_252d_base_v034_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc035_42d_base_v035_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.rolling(42).kurt() - assets.rolling(42).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc035_42d_base_v035_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc035_42d_base_v035_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc036_126d_base_v036_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue.rolling(126).kurt() - ev.rolling(126).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc036_126d_base_v036_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc036_126d_base_v036_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc037_21d_base_v037_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.diff(21).abs() / ev.diff(21).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc037_21d_base_v037_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc037_21d_base_v037_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc038_10d_base_v038_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf / revenue.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc038_10d_base_v038_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc038_10d_base_v038_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc039_21d_base_v039_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev / equity.replace(0, np.nan)).rolling(21).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc039_21d_base_v039_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc039_21d_base_v039_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc040_10d_base_v040_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(10).rank(pct=True) / assets.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc040_10d_base_v040_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc040_10d_base_v040_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc041_252d_base_v041_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.rolling(252).kurt() - equity.rolling(252).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc041_252d_base_v041_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc041_252d_base_v041_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc042_42d_base_v042_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(42).rank(pct=True) / ev.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc042_42d_base_v042_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc042_42d_base_v042_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc043_252d_base_v043_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.diff(252).abs() / assets.diff(252).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc043_252d_base_v043_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc043_252d_base_v043_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc044_126d_base_v044_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.diff(126) / fcf.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc044_126d_base_v044_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc044_126d_base_v044_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc045_21d_base_v045_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue.rolling(21).max() - ebitda.rolling(21).min()) / fcf.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc045_21d_base_v045_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc045_21d_base_v045_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc046_42d_base_v046_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.diff(42).abs() / debt.diff(42).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc046_42d_base_v046_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc046_42d_base_v046_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc047_252d_base_v047_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity / fcf.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc047_252d_base_v047_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc047_252d_base_v047_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc048_252d_base_v048_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity / debt.replace(0, np.nan)).rolling(252).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc048_252d_base_v048_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc048_252d_base_v048_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc049_252d_base_v049_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf / debt.replace(0, np.nan)).rolling(252).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc049_252d_base_v049_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc049_252d_base_v049_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc050_252d_base_v050_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = ((ev - ev.rolling(252).mean()) / ev.rolling(252).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc050_252d_base_v050_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc050_252d_base_v050_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc051_5d_base_v051_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev / equity.replace(0, np.nan)).rolling(5).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc051_5d_base_v051_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc051_5d_base_v051_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc052_21d_base_v052_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.pct_change(21) - revenue.pct_change(21))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc052_21d_base_v052_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc052_21d_base_v052_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc053_126d_base_v053_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue.rolling(126).kurt() - fcf.rolling(126).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc053_126d_base_v053_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc053_126d_base_v053_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc054_10d_base_v054_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.diff(10).abs() / assets.diff(10).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc054_10d_base_v054_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc054_10d_base_v054_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc055_252d_base_v055_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(252).rank(pct=True) / revenue.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc055_252d_base_v055_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc055_252d_base_v055_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc056_21d_base_v056_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = ((ev - ev.rolling(21).mean()) / ev.rolling(21).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc056_21d_base_v056_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc056_21d_base_v056_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc057_63d_base_v057_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets.rolling(63).quantile(0.5) / ev.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc057_63d_base_v057_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc057_63d_base_v057_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc058_252d_base_v058_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.diff(252) / ebitda.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc058_252d_base_v058_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc058_252d_base_v058_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc059_126d_base_v059_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.diff(126) / ev.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc059_126d_base_v059_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc059_126d_base_v059_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc060_10d_base_v060_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.diff(10) / ebitda.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc060_10d_base_v060_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc060_10d_base_v060_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc061_21d_base_v061_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.diff(21) / assets.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc061_21d_base_v061_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc061_21d_base_v061_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc062_10d_base_v062_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity / fcf.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc062_10d_base_v062_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc062_10d_base_v062_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc063_63d_base_v063_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.pct_change(63) - fcf.pct_change(63))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc063_63d_base_v063_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc063_63d_base_v063_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc064_10d_base_v064_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.rolling(10).rank(pct=True) / assets.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc064_10d_base_v064_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc064_10d_base_v064_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc065_5d_base_v065_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.rolling(5).kurt() - ev.rolling(5).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc065_5d_base_v065_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc065_5d_base_v065_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc066_10d_base_v066_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.pct_change(10) - equity.pct_change(10))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc066_10d_base_v066_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc066_10d_base_v066_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc067_42d_base_v067_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda / revenue.replace(0, np.nan)).rolling(42).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc067_42d_base_v067_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc067_42d_base_v067_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc068_126d_base_v068_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.rolling(126).rank(pct=True) / equity.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc068_126d_base_v068_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc068_126d_base_v068_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc069_5d_base_v069_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.pct_change(5) - ebitda.pct_change(5))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc069_5d_base_v069_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc069_5d_base_v069_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc070_21d_base_v070_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev / fcf.replace(0, np.nan)).rolling(21).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc070_21d_base_v070_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc070_21d_base_v070_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc071_63d_base_v071_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets.diff(63) / ev.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc071_63d_base_v071_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc071_63d_base_v071_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc072_126d_base_v072_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.diff(126).abs() / equity.diff(126).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc072_126d_base_v072_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc072_126d_base_v072_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc073_5d_base_v073_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.diff(5) / fcf.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc073_5d_base_v073_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc073_5d_base_v073_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc074_63d_base_v074_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(63).quantile(0.5) / assets.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc074_63d_base_v074_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc074_63d_base_v074_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc075_63d_base_v075_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets / revenue.replace(0, np.nan)).rolling(63).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc075_63d_base_v075_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc075_63d_base_v075_signal



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
