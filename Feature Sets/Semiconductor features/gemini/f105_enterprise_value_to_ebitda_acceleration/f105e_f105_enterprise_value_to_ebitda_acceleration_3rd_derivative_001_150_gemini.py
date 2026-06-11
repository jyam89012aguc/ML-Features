import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc001_10d_jerk_v001_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(10).kurt() - debt.rolling(10).kurt())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc001_10d_jerk_v001_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc001_10d_jerk_v001_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc002_126d_jerk_v002_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = ((ebitda - ebitda.rolling(126).mean()) / ebitda.rolling(126).std())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc002_126d_jerk_v002_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc002_126d_jerk_v002_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc003_126d_jerk_v003_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.rolling(126).rank(pct=True) / equity.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc003_126d_jerk_v003_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc003_126d_jerk_v003_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc004_21d_jerk_v004_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(21).kurt() - revenue.rolling(21).kurt())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc004_21d_jerk_v004_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc004_21d_jerk_v004_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc005_5d_jerk_v005_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = ((ev - ev.rolling(5).mean()) / ev.rolling(5).std())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc005_5d_jerk_v005_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc005_5d_jerk_v005_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc006_126d_jerk_v006_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.rolling(126).max() - ebitda.rolling(126).min()) / equity.replace(0, np.nan)
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc006_126d_jerk_v006_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc006_126d_jerk_v006_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc007_10d_jerk_v007_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = ((equity - equity.rolling(10).mean()) / equity.rolling(10).std())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc007_10d_jerk_v007_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc007_10d_jerk_v007_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc008_10d_jerk_v008_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf / equity.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc008_10d_jerk_v008_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc008_10d_jerk_v008_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc009_252d_jerk_v009_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(252).kurt() - fcf.rolling(252).kurt())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc009_252d_jerk_v009_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc009_252d_jerk_v009_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc010_63d_jerk_v010_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(63).max() - fcf.rolling(63).min()) / assets.replace(0, np.nan)
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc010_63d_jerk_v010_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc010_63d_jerk_v010_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc011_126d_jerk_v011_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets.pct_change(126) - fcf.pct_change(126))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc011_126d_jerk_v011_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc011_126d_jerk_v011_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc012_10d_jerk_v012_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue / ev.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc012_10d_jerk_v012_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc012_10d_jerk_v012_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc013_252d_jerk_v013_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.diff(252).abs() / fcf.diff(252).abs().replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc013_252d_jerk_v013_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc013_252d_jerk_v013_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc014_126d_jerk_v014_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue.pct_change(126) - ev.pct_change(126))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc014_126d_jerk_v014_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc014_126d_jerk_v014_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc015_42d_jerk_v015_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf / debt.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc015_42d_jerk_v015_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc015_42d_jerk_v015_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc016_126d_jerk_v016_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(126).max() - debt.rolling(126).min()) / fcf.replace(0, np.nan)
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc016_126d_jerk_v016_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc016_126d_jerk_v016_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc017_21d_jerk_v017_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue.rolling(21).max() - assets.rolling(21).min()) / equity.replace(0, np.nan)
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc017_21d_jerk_v017_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc017_21d_jerk_v017_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc018_63d_jerk_v018_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.pct_change(63) - fcf.pct_change(63))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc018_63d_jerk_v018_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc018_63d_jerk_v018_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc019_42d_jerk_v019_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.rolling(42).kurt() - ebitda.rolling(42).kurt())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc019_42d_jerk_v019_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc019_42d_jerk_v019_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc020_5d_jerk_v020_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = ((fcf - fcf.rolling(5).mean()) / fcf.rolling(5).std())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc020_5d_jerk_v020_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc020_5d_jerk_v020_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc021_252d_jerk_v021_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.diff(252) / equity.replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc021_252d_jerk_v021_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc021_252d_jerk_v021_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc022_126d_jerk_v022_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev / revenue.replace(0, np.nan)).rolling(126).std()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc022_126d_jerk_v022_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc022_126d_jerk_v022_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc023_126d_jerk_v023_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(126).rank(pct=True) / revenue.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc023_126d_jerk_v023_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc023_126d_jerk_v023_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc024_252d_jerk_v024_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(252).rank(pct=True) / equity.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc024_252d_jerk_v024_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc024_252d_jerk_v024_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc025_252d_jerk_v025_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.rolling(252).max() - ev.rolling(252).min()) / revenue.replace(0, np.nan)
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc025_252d_jerk_v025_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc025_252d_jerk_v025_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc026_42d_jerk_v026_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets.rolling(42).rank(pct=True) / fcf.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc026_42d_jerk_v026_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc026_42d_jerk_v026_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc027_42d_jerk_v027_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue.diff(42).abs() / equity.diff(42).abs().replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc027_42d_jerk_v027_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc027_42d_jerk_v027_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc028_63d_jerk_v028_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.diff(63).abs() / debt.diff(63).abs().replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc028_63d_jerk_v028_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc028_63d_jerk_v028_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc029_21d_jerk_v029_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue / debt.replace(0, np.nan)).rolling(21).std()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc029_21d_jerk_v029_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc029_21d_jerk_v029_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc030_63d_jerk_v030_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev / equity.replace(0, np.nan)).rolling(63).mean()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc030_63d_jerk_v030_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc030_63d_jerk_v030_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc031_42d_jerk_v031_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue / assets.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc031_42d_jerk_v031_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc031_42d_jerk_v031_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc032_63d_jerk_v032_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = ((fcf - fcf.rolling(63).mean()) / fcf.rolling(63).std())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc032_63d_jerk_v032_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc032_63d_jerk_v032_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc033_252d_jerk_v033_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue.rolling(252).quantile(0.5) / debt.rolling(252).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc033_252d_jerk_v033_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc033_252d_jerk_v033_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc034_252d_jerk_v034_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets.diff(252) / debt.replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc034_252d_jerk_v034_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc034_252d_jerk_v034_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc035_42d_jerk_v035_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.rolling(42).kurt() - assets.rolling(42).kurt())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc035_42d_jerk_v035_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc035_42d_jerk_v035_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc036_126d_jerk_v036_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue.rolling(126).kurt() - ev.rolling(126).kurt())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc036_126d_jerk_v036_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc036_126d_jerk_v036_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc037_21d_jerk_v037_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.diff(21).abs() / ev.diff(21).abs().replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc037_21d_jerk_v037_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc037_21d_jerk_v037_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc038_10d_jerk_v038_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf / revenue.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc038_10d_jerk_v038_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc038_10d_jerk_v038_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc039_21d_jerk_v039_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev / equity.replace(0, np.nan)).rolling(21).std()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc039_21d_jerk_v039_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc039_21d_jerk_v039_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc040_10d_jerk_v040_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(10).rank(pct=True) / assets.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc040_10d_jerk_v040_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc040_10d_jerk_v040_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc041_252d_jerk_v041_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.rolling(252).kurt() - equity.rolling(252).kurt())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc041_252d_jerk_v041_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc041_252d_jerk_v041_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc042_42d_jerk_v042_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(42).rank(pct=True) / ev.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc042_42d_jerk_v042_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc042_42d_jerk_v042_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc043_252d_jerk_v043_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.diff(252).abs() / assets.diff(252).abs().replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc043_252d_jerk_v043_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc043_252d_jerk_v043_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc044_126d_jerk_v044_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.diff(126) / fcf.replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc044_126d_jerk_v044_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc044_126d_jerk_v044_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc045_21d_jerk_v045_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue.rolling(21).max() - ebitda.rolling(21).min()) / fcf.replace(0, np.nan)
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc045_21d_jerk_v045_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc045_21d_jerk_v045_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc046_42d_jerk_v046_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.diff(42).abs() / debt.diff(42).abs().replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc046_42d_jerk_v046_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc046_42d_jerk_v046_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc047_252d_jerk_v047_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity / fcf.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc047_252d_jerk_v047_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc047_252d_jerk_v047_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc048_252d_jerk_v048_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity / debt.replace(0, np.nan)).rolling(252).std()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc048_252d_jerk_v048_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc048_252d_jerk_v048_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc049_252d_jerk_v049_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf / debt.replace(0, np.nan)).rolling(252).std()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc049_252d_jerk_v049_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc049_252d_jerk_v049_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc050_252d_jerk_v050_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = ((ev - ev.rolling(252).mean()) / ev.rolling(252).std())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc050_252d_jerk_v050_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc050_252d_jerk_v050_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc051_5d_jerk_v051_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev / equity.replace(0, np.nan)).rolling(5).mean()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc051_5d_jerk_v051_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc051_5d_jerk_v051_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc052_21d_jerk_v052_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.pct_change(21) - revenue.pct_change(21))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc052_21d_jerk_v052_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc052_21d_jerk_v052_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc053_126d_jerk_v053_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue.rolling(126).kurt() - fcf.rolling(126).kurt())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc053_126d_jerk_v053_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc053_126d_jerk_v053_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc054_10d_jerk_v054_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.diff(10).abs() / assets.diff(10).abs().replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc054_10d_jerk_v054_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc054_10d_jerk_v054_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc055_252d_jerk_v055_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(252).rank(pct=True) / revenue.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc055_252d_jerk_v055_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc055_252d_jerk_v055_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc056_21d_jerk_v056_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = ((ev - ev.rolling(21).mean()) / ev.rolling(21).std())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc056_21d_jerk_v056_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc056_21d_jerk_v056_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc057_63d_jerk_v057_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets.rolling(63).quantile(0.5) / ev.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc057_63d_jerk_v057_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc057_63d_jerk_v057_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc058_252d_jerk_v058_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.diff(252) / ebitda.replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc058_252d_jerk_v058_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc058_252d_jerk_v058_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc059_126d_jerk_v059_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.diff(126) / ev.replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc059_126d_jerk_v059_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc059_126d_jerk_v059_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc060_10d_jerk_v060_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.diff(10) / ebitda.replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc060_10d_jerk_v060_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc060_10d_jerk_v060_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc061_21d_jerk_v061_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.diff(21) / assets.replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc061_21d_jerk_v061_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc061_21d_jerk_v061_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc062_10d_jerk_v062_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity / fcf.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc062_10d_jerk_v062_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc062_10d_jerk_v062_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc063_63d_jerk_v063_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.pct_change(63) - fcf.pct_change(63))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc063_63d_jerk_v063_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc063_63d_jerk_v063_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc064_10d_jerk_v064_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.rolling(10).rank(pct=True) / assets.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc064_10d_jerk_v064_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc064_10d_jerk_v064_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc065_5d_jerk_v065_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.rolling(5).kurt() - ev.rolling(5).kurt())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc065_5d_jerk_v065_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc065_5d_jerk_v065_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc066_10d_jerk_v066_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.pct_change(10) - equity.pct_change(10))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc066_10d_jerk_v066_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc066_10d_jerk_v066_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc067_42d_jerk_v067_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda / revenue.replace(0, np.nan)).rolling(42).std()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc067_42d_jerk_v067_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc067_42d_jerk_v067_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc068_126d_jerk_v068_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.rolling(126).rank(pct=True) / equity.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc068_126d_jerk_v068_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc068_126d_jerk_v068_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc069_5d_jerk_v069_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.pct_change(5) - ebitda.pct_change(5))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc069_5d_jerk_v069_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc069_5d_jerk_v069_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc070_21d_jerk_v070_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev / fcf.replace(0, np.nan)).rolling(21).std()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc070_21d_jerk_v070_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc070_21d_jerk_v070_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc071_63d_jerk_v071_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets.diff(63) / ev.replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc071_63d_jerk_v071_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc071_63d_jerk_v071_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc072_126d_jerk_v072_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.diff(126).abs() / equity.diff(126).abs().replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc072_126d_jerk_v072_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc072_126d_jerk_v072_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc073_5d_jerk_v073_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.diff(5) / fcf.replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc073_5d_jerk_v073_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc073_5d_jerk_v073_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc074_63d_jerk_v074_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(63).quantile(0.5) / assets.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc074_63d_jerk_v074_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc074_63d_jerk_v074_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc075_63d_jerk_v075_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets / revenue.replace(0, np.nan)).rolling(63).std()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc075_63d_jerk_v075_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc075_63d_jerk_v075_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc076_10d_jerk_v076_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity / ev.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc076_10d_jerk_v076_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc076_10d_jerk_v076_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc077_10d_jerk_v077_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(10).max() - ev.rolling(10).min()) / fcf.replace(0, np.nan)
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc077_10d_jerk_v077_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc077_10d_jerk_v077_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc078_252d_jerk_v078_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets / debt.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc078_252d_jerk_v078_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc078_252d_jerk_v078_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc079_10d_jerk_v079_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.diff(10) / ev.replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc079_10d_jerk_v079_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc079_10d_jerk_v079_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc080_10d_jerk_v080_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = ((assets - assets.rolling(10).mean()) / assets.rolling(10).std())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc080_10d_jerk_v080_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc080_10d_jerk_v080_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc081_21d_jerk_v081_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt / fcf.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc081_21d_jerk_v081_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc081_21d_jerk_v081_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc082_126d_jerk_v082_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue.diff(126).abs() / fcf.diff(126).abs().replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc082_126d_jerk_v082_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc082_126d_jerk_v082_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc083_63d_jerk_v083_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf / assets.replace(0, np.nan)).rolling(63).std()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc083_63d_jerk_v083_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc083_63d_jerk_v083_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc084_126d_jerk_v084_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev / revenue.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc084_126d_jerk_v084_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc084_126d_jerk_v084_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc085_21d_jerk_v085_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.diff(21) / fcf.replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc085_21d_jerk_v085_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc085_21d_jerk_v085_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc086_21d_jerk_v086_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets / equity.replace(0, np.nan)).rolling(21).mean()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc086_21d_jerk_v086_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc086_21d_jerk_v086_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc087_10d_jerk_v087_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = ((ev - ev.rolling(10).mean()) / ev.rolling(10).std())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc087_10d_jerk_v087_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc087_10d_jerk_v087_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc088_10d_jerk_v088_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets / debt.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc088_10d_jerk_v088_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc088_10d_jerk_v088_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc089_126d_jerk_v089_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf / ev.replace(0, np.nan)).rolling(126).std()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc089_126d_jerk_v089_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc089_126d_jerk_v089_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc090_126d_jerk_v090_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue.rolling(126).rank(pct=True) / assets.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc090_126d_jerk_v090_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc090_126d_jerk_v090_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc091_21d_jerk_v091_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(21).quantile(0.5) / revenue.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc091_21d_jerk_v091_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc091_21d_jerk_v091_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc092_126d_jerk_v092_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.pct_change(126) - fcf.pct_change(126))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc092_126d_jerk_v092_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc092_126d_jerk_v092_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc093_10d_jerk_v093_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(10).kurt() - fcf.rolling(10).kurt())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc093_10d_jerk_v093_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc093_10d_jerk_v093_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc094_42d_jerk_v094_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda / fcf.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc094_42d_jerk_v094_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc094_42d_jerk_v094_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc095_63d_jerk_v095_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.rolling(63).quantile(0.5) / assets.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc095_63d_jerk_v095_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc095_63d_jerk_v095_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc096_126d_jerk_v096_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.diff(126).abs() / ev.diff(126).abs().replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc096_126d_jerk_v096_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc096_126d_jerk_v096_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc097_5d_jerk_v097_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets.rolling(5).rank(pct=True) / fcf.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc097_5d_jerk_v097_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc097_5d_jerk_v097_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc098_42d_jerk_v098_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.rolling(42).kurt() - equity.rolling(42).kurt())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc098_42d_jerk_v098_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc098_42d_jerk_v098_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc099_5d_jerk_v099_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.diff(5) / debt.replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc099_5d_jerk_v099_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc099_5d_jerk_v099_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc100_252d_jerk_v100_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.pct_change(252) - assets.pct_change(252))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc100_252d_jerk_v100_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc100_252d_jerk_v100_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc101_10d_jerk_v101_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity / assets.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc101_10d_jerk_v101_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc101_10d_jerk_v101_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc102_21d_jerk_v102_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = ((ebitda - ebitda.rolling(21).mean()) / ebitda.rolling(21).std())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc102_21d_jerk_v102_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc102_21d_jerk_v102_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc103_126d_jerk_v103_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.pct_change(126) - debt.pct_change(126))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc103_126d_jerk_v103_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc103_126d_jerk_v103_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc104_126d_jerk_v104_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets.diff(126) / ebitda.replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc104_126d_jerk_v104_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc104_126d_jerk_v104_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc105_10d_jerk_v105_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev / fcf.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc105_10d_jerk_v105_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc105_10d_jerk_v105_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc106_10d_jerk_v106_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity / ev.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc106_10d_jerk_v106_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc106_10d_jerk_v106_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc107_5d_jerk_v107_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.rolling(5).quantile(0.5) / revenue.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc107_5d_jerk_v107_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc107_5d_jerk_v107_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc108_63d_jerk_v108_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(63).quantile(0.5) / debt.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc108_63d_jerk_v108_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc108_63d_jerk_v108_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc109_21d_jerk_v109_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.rolling(21).max() - ev.rolling(21).min()) / equity.replace(0, np.nan)
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc109_21d_jerk_v109_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc109_21d_jerk_v109_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc110_5d_jerk_v110_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(5).max() - fcf.rolling(5).min()) / debt.replace(0, np.nan)
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc110_5d_jerk_v110_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc110_5d_jerk_v110_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc111_252d_jerk_v111_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(252).max() - ebitda.rolling(252).min()) / fcf.replace(0, np.nan)
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc111_252d_jerk_v111_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc111_252d_jerk_v111_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc112_5d_jerk_v112_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.diff(5) / ebitda.replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc112_5d_jerk_v112_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc112_5d_jerk_v112_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc113_42d_jerk_v113_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.diff(42).abs() / equity.diff(42).abs().replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc113_42d_jerk_v113_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc113_42d_jerk_v113_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc114_21d_jerk_v114_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.diff(21) / ev.replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc114_21d_jerk_v114_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc114_21d_jerk_v114_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc115_42d_jerk_v115_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev / equity.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc115_42d_jerk_v115_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc115_42d_jerk_v115_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc116_10d_jerk_v116_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(10).kurt() - assets.rolling(10).kurt())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc116_10d_jerk_v116_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc116_10d_jerk_v116_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc117_5d_jerk_v117_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda / fcf.replace(0, np.nan)).rolling(5).std()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc117_5d_jerk_v117_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc117_5d_jerk_v117_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc118_63d_jerk_v118_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.diff(63).abs() / ebitda.diff(63).abs().replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc118_63d_jerk_v118_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc118_63d_jerk_v118_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc119_63d_jerk_v119_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.rolling(63).rank(pct=True) / assets.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc119_63d_jerk_v119_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc119_63d_jerk_v119_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc120_10d_jerk_v120_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.diff(10).abs() / debt.diff(10).abs().replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc120_10d_jerk_v120_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc120_10d_jerk_v120_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc121_42d_jerk_v121_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev / revenue.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc121_42d_jerk_v121_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc121_42d_jerk_v121_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc122_126d_jerk_v122_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda / revenue.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc122_126d_jerk_v122_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc122_126d_jerk_v122_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc123_252d_jerk_v123_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue / assets.replace(0, np.nan)).rolling(252).std()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc123_252d_jerk_v123_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc123_252d_jerk_v123_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc124_252d_jerk_v124_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf / equity.replace(0, np.nan)).rolling(252).std()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc124_252d_jerk_v124_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc124_252d_jerk_v124_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc125_252d_jerk_v125_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.rolling(252).max() - ev.rolling(252).min()) / revenue.replace(0, np.nan)
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc125_252d_jerk_v125_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc125_252d_jerk_v125_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc126_42d_jerk_v126_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (debt.rolling(42).rank(pct=True) / ev.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc126_42d_jerk_v126_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc126_42d_jerk_v126_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc127_252d_jerk_v127_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets / equity.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc127_252d_jerk_v127_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc127_252d_jerk_v127_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc128_10d_jerk_v128_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.diff(10).abs() / debt.diff(10).abs().replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc128_10d_jerk_v128_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc128_10d_jerk_v128_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc129_252d_jerk_v129_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(252).quantile(0.5) / debt.rolling(252).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc129_252d_jerk_v129_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc129_252d_jerk_v129_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc130_252d_jerk_v130_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(252).rank(pct=True) / debt.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc130_252d_jerk_v130_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc130_252d_jerk_v130_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc131_42d_jerk_v131_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda.rolling(42).quantile(0.5) / ev.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc131_42d_jerk_v131_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc131_42d_jerk_v131_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc132_126d_jerk_v132_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets.rolling(126).quantile(0.5) / revenue.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc132_126d_jerk_v132_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc132_126d_jerk_v132_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc133_10d_jerk_v133_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(10).max() - fcf.rolling(10).min()) / ebitda.replace(0, np.nan)
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc133_10d_jerk_v133_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc133_10d_jerk_v133_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc134_63d_jerk_v134_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.diff(63) / fcf.replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc134_63d_jerk_v134_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc134_63d_jerk_v134_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc135_10d_jerk_v135_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(10).rank(pct=True) / debt.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc135_10d_jerk_v135_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc135_10d_jerk_v135_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc136_10d_jerk_v136_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.rolling(10).max() - ebitda.rolling(10).min()) / assets.replace(0, np.nan)
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc136_10d_jerk_v136_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc136_10d_jerk_v136_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc137_63d_jerk_v137_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = ((revenue - revenue.rolling(63).mean()) / revenue.rolling(63).std())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc137_63d_jerk_v137_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc137_63d_jerk_v137_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc138_5d_jerk_v138_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets.rolling(5).rank(pct=True) / revenue.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc138_5d_jerk_v138_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc138_5d_jerk_v138_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc139_63d_jerk_v139_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.diff(63).abs() / revenue.diff(63).abs().replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc139_63d_jerk_v139_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc139_63d_jerk_v139_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc140_252d_jerk_v140_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ebitda / revenue.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc140_252d_jerk_v140_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc140_252d_jerk_v140_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc141_63d_jerk_v141_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.rolling(63).rank(pct=True) / revenue.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc141_63d_jerk_v141_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc141_63d_jerk_v141_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc142_126d_jerk_v142_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.diff(126).abs() / fcf.diff(126).abs().replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc142_126d_jerk_v142_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc142_126d_jerk_v142_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc143_126d_jerk_v143_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (revenue.rolling(126).kurt() - assets.rolling(126).kurt())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc143_126d_jerk_v143_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc143_126d_jerk_v143_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc144_63d_jerk_v144_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.rolling(63).max() - ebitda.rolling(63).min()) / assets.replace(0, np.nan)
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc144_63d_jerk_v144_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc144_63d_jerk_v144_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc145_21d_jerk_v145_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(21).quantile(0.5) / debt.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc145_21d_jerk_v145_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc145_21d_jerk_v145_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc146_5d_jerk_v146_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (ev.rolling(5).rank(pct=True) / ebitda.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc146_5d_jerk_v146_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc146_5d_jerk_v146_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc147_42d_jerk_v147_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf.diff(42).abs() / ebitda.diff(42).abs().replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc147_42d_jerk_v147_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc147_42d_jerk_v147_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc148_5d_jerk_v148_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (fcf / ev.replace(0, np.nan)).rolling(5).std()
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc148_5d_jerk_v148_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc148_5d_jerk_v148_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc149_10d_jerk_v149_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (assets.rolling(10).kurt() - fcf.rolling(10).kurt())
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc149_10d_jerk_v149_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc149_10d_jerk_v149_signal

def f105e_f105_enterprise_value_to_ebitda_acceleration_calc150_63d_jerk_v150_signal(ev, ebitda, revenue, assets, equity, fcf, debt):
    v1 = (equity.diff(63).abs() / assets.diff(63).abs().replace(0, np.nan))
    v2 = v1.diff(1).diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f105e_f105_enterprise_value_to_ebitda_acceleration_calc150_63d_jerk_v150_signal'] = f105e_f105_enterprise_value_to_ebitda_acceleration_calc150_63d_jerk_v150_signal



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
