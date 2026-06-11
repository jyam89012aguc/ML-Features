"""Generated capitulation features for 64_liquidity_distress: current/quick ratio collapse.
All windows look backward only. Trading-day constants: 252/year, 63/quarter, 21/month, 5/week.
"""
import numpy as np
import pandas as pd


def _align_to_close(s, close):
    s = pd.Series(s).copy()
    close = pd.Series(close)
    return s.reindex(close.index).ffill()

def _s(s):
    return pd.Series(s).replace([np.inf, -np.inf], np.nan)

def _div(a, b):
    return _s(a) / _s(b).replace(0, np.nan)

def _z(s, w):
    x = _s(s)
    return _div(x - x.rolling(w, min_periods=max(3, w // 4)).mean(), x.rolling(w, min_periods=max(3, w // 4)).std())

def _rank(s, w):
    x = _s(s)
    return x.rolling(w, min_periods=max(3, w // 4)).rank(pct=True)

def _true_range(high, low, close):
    pc = _s(close).shift(1)
    return pd.concat([_s(high) - _s(low), (_s(high) - pc).abs(), (_s(low) - pc).abs()], axis=1).max(axis=1)

def lqd_001_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _z(x, 63)

def lqd_002_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _div(x, y)

def lqd_003_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(x - y, y.abs())

def lqd_004_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _rank(x, 504)

def lqd_005_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def lqd_006_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def lqd_007_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _div(x, _s(close))

def lqd_008_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def lqd_009_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def lqd_010_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def lqd_011_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def lqd_012_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lqd_013_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def lqd_014_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _s(x).pct_change(126)

def lqd_015_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _z(x, 252)

def lqd_016_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _div(x, y)

def lqd_017_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _div(x - y, y.abs())

def lqd_018_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _rank(x, 21)

def lqd_019_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def lqd_020_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def lqd_021_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _div(x, _s(close))

def lqd_022_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def lqd_023_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def lqd_024_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def lqd_025_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def lqd_026_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lqd_027_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def lqd_028_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _s(x).pct_change(504)

def lqd_029_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _z(x, 756)

def lqd_030_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(x, y)

def lqd_031_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _div(x - y, y.abs())

def lqd_032_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _rank(x, 126)

def lqd_033_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def lqd_034_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def lqd_035_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(x, _s(close))

def lqd_036_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def lqd_037_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def lqd_038_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def lqd_039_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def lqd_040_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lqd_041_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def lqd_042_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _s(x).pct_change(21)

def lqd_043_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _z(x, 63)

def lqd_044_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _div(x, y)

def lqd_045_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(x - y, y.abs())

def lqd_046_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _rank(x, 504)

def lqd_047_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def lqd_048_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def lqd_049_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _div(x, _s(close))

def lqd_050_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def lqd_051_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def lqd_052_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def lqd_053_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def lqd_054_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lqd_055_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def lqd_056_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _s(x).pct_change(126)

def lqd_057_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _z(x, 252)

def lqd_058_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(x, y)

def lqd_059_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _div(x - y, y.abs())

def lqd_060_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _rank(x, 21)

def lqd_061_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def lqd_062_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def lqd_063_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(x, _s(close))

def lqd_064_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def lqd_065_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def lqd_066_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def lqd_067_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def lqd_068_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lqd_069_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def lqd_070_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _s(x).pct_change(504)

def lqd_071_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _z(x, 756)

def lqd_072_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _div(x, y)

def lqd_073_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(x - y, y.abs())

def lqd_074_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _rank(x, 126)

def lqd_075_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

LIQUIDITY_DISTRESS_REGISTRY_001_075 = {
    "lqd_001_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_001_capitulation_signal},
    "lqd_002_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_002_capitulation_signal},
    "lqd_003_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_003_capitulation_signal},
    "lqd_004_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_004_capitulation_signal},
    "lqd_005_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_005_capitulation_signal},
    "lqd_006_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_006_capitulation_signal},
    "lqd_007_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_007_capitulation_signal},
    "lqd_008_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_008_capitulation_signal},
    "lqd_009_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_009_capitulation_signal},
    "lqd_010_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_010_capitulation_signal},
    "lqd_011_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_011_capitulation_signal},
    "lqd_012_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_012_capitulation_signal},
    "lqd_013_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_013_capitulation_signal},
    "lqd_014_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_014_capitulation_signal},
    "lqd_015_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_015_capitulation_signal},
    "lqd_016_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_016_capitulation_signal},
    "lqd_017_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_017_capitulation_signal},
    "lqd_018_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_018_capitulation_signal},
    "lqd_019_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_019_capitulation_signal},
    "lqd_020_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_020_capitulation_signal},
    "lqd_021_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_021_capitulation_signal},
    "lqd_022_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_022_capitulation_signal},
    "lqd_023_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_023_capitulation_signal},
    "lqd_024_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_024_capitulation_signal},
    "lqd_025_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_025_capitulation_signal},
    "lqd_026_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_026_capitulation_signal},
    "lqd_027_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_027_capitulation_signal},
    "lqd_028_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_028_capitulation_signal},
    "lqd_029_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_029_capitulation_signal},
    "lqd_030_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_030_capitulation_signal},
    "lqd_031_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_031_capitulation_signal},
    "lqd_032_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_032_capitulation_signal},
    "lqd_033_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_033_capitulation_signal},
    "lqd_034_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_034_capitulation_signal},
    "lqd_035_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_035_capitulation_signal},
    "lqd_036_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_036_capitulation_signal},
    "lqd_037_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_037_capitulation_signal},
    "lqd_038_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_038_capitulation_signal},
    "lqd_039_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_039_capitulation_signal},
    "lqd_040_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_040_capitulation_signal},
    "lqd_041_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_041_capitulation_signal},
    "lqd_042_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_042_capitulation_signal},
    "lqd_043_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_043_capitulation_signal},
    "lqd_044_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_044_capitulation_signal},
    "lqd_045_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_045_capitulation_signal},
    "lqd_046_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_046_capitulation_signal},
    "lqd_047_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_047_capitulation_signal},
    "lqd_048_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_048_capitulation_signal},
    "lqd_049_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_049_capitulation_signal},
    "lqd_050_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_050_capitulation_signal},
    "lqd_051_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_051_capitulation_signal},
    "lqd_052_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_052_capitulation_signal},
    "lqd_053_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_053_capitulation_signal},
    "lqd_054_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_054_capitulation_signal},
    "lqd_055_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_055_capitulation_signal},
    "lqd_056_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_056_capitulation_signal},
    "lqd_057_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_057_capitulation_signal},
    "lqd_058_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_058_capitulation_signal},
    "lqd_059_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_059_capitulation_signal},
    "lqd_060_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_060_capitulation_signal},
    "lqd_061_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_061_capitulation_signal},
    "lqd_062_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_062_capitulation_signal},
    "lqd_063_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_063_capitulation_signal},
    "lqd_064_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_064_capitulation_signal},
    "lqd_065_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_065_capitulation_signal},
    "lqd_066_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_066_capitulation_signal},
    "lqd_067_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_067_capitulation_signal},
    "lqd_068_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_068_capitulation_signal},
    "lqd_069_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_069_capitulation_signal},
    "lqd_070_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_070_capitulation_signal},
    "lqd_071_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_071_capitulation_signal},
    "lqd_072_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_072_capitulation_signal},
    "lqd_073_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_073_capitulation_signal},
    "lqd_074_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_074_capitulation_signal},
    "lqd_075_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_075_capitulation_signal},
}
