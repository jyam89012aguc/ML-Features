"""Generated capitulation features for 67_working_capital_drain: working capital depletion.
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

def wcd_001_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _z(x, 63)

def wcd_002_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _div(x, y)

def wcd_003_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(x - y, y.abs())

def wcd_004_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _rank(x, 504)

def wcd_005_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def wcd_006_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def wcd_007_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _div(x, _s(close))

def wcd_008_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def wcd_009_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def wcd_010_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def wcd_011_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def wcd_012_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def wcd_013_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def wcd_014_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _s(x).pct_change(126)

def wcd_015_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _z(x, 252)

def wcd_016_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(x, y)

def wcd_017_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _div(x - y, y.abs())

def wcd_018_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _rank(x, 21)

def wcd_019_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def wcd_020_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def wcd_021_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(x, _s(close))

def wcd_022_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def wcd_023_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def wcd_024_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def wcd_025_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def wcd_026_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def wcd_027_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def wcd_028_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _s(x).pct_change(504)

def wcd_029_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _z(x, 756)

def wcd_030_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _div(x, y)

def wcd_031_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(x - y, y.abs())

def wcd_032_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _rank(x, 126)

def wcd_033_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def wcd_034_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def wcd_035_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _div(x, _s(close))

def wcd_036_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def wcd_037_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def wcd_038_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def wcd_039_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def wcd_040_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def wcd_041_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def wcd_042_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _s(x).pct_change(21)

def wcd_043_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _z(x, 63)

def wcd_044_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, y)

def wcd_045_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _div(x - y, y.abs())

def wcd_046_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _rank(x, 504)

def wcd_047_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def wcd_048_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def wcd_049_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, _s(close))

def wcd_050_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def wcd_051_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def wcd_052_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def wcd_053_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def wcd_054_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def wcd_055_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def wcd_056_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _s(x).pct_change(126)

def wcd_057_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _z(x, 252)

def wcd_058_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(x, y)

def wcd_059_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _div(x - y, y.abs())

def wcd_060_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _rank(x, 21)

def wcd_061_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def wcd_062_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def wcd_063_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(x, _s(close))

def wcd_064_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def wcd_065_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def wcd_066_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def wcd_067_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def wcd_068_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def wcd_069_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def wcd_070_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _s(x).pct_change(504)

def wcd_071_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _z(x, 756)

def wcd_072_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _div(x, y)

def wcd_073_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(x - y, y.abs())

def wcd_074_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _rank(x, 126)

def wcd_075_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

WORKING_CAPITAL_DRAIN_REGISTRY_001_075 = {
    "wcd_001_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_001_capitulation_signal},
    "wcd_002_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_002_capitulation_signal},
    "wcd_003_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_003_capitulation_signal},
    "wcd_004_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_004_capitulation_signal},
    "wcd_005_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_005_capitulation_signal},
    "wcd_006_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_006_capitulation_signal},
    "wcd_007_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_007_capitulation_signal},
    "wcd_008_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_008_capitulation_signal},
    "wcd_009_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_009_capitulation_signal},
    "wcd_010_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_010_capitulation_signal},
    "wcd_011_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_011_capitulation_signal},
    "wcd_012_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_012_capitulation_signal},
    "wcd_013_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_013_capitulation_signal},
    "wcd_014_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_014_capitulation_signal},
    "wcd_015_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_015_capitulation_signal},
    "wcd_016_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_016_capitulation_signal},
    "wcd_017_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_017_capitulation_signal},
    "wcd_018_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_018_capitulation_signal},
    "wcd_019_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_019_capitulation_signal},
    "wcd_020_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_020_capitulation_signal},
    "wcd_021_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_021_capitulation_signal},
    "wcd_022_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_022_capitulation_signal},
    "wcd_023_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_023_capitulation_signal},
    "wcd_024_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_024_capitulation_signal},
    "wcd_025_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_025_capitulation_signal},
    "wcd_026_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_026_capitulation_signal},
    "wcd_027_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_027_capitulation_signal},
    "wcd_028_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_028_capitulation_signal},
    "wcd_029_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_029_capitulation_signal},
    "wcd_030_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_030_capitulation_signal},
    "wcd_031_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_031_capitulation_signal},
    "wcd_032_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_032_capitulation_signal},
    "wcd_033_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_033_capitulation_signal},
    "wcd_034_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_034_capitulation_signal},
    "wcd_035_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_035_capitulation_signal},
    "wcd_036_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_036_capitulation_signal},
    "wcd_037_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_037_capitulation_signal},
    "wcd_038_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_038_capitulation_signal},
    "wcd_039_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_039_capitulation_signal},
    "wcd_040_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_040_capitulation_signal},
    "wcd_041_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_041_capitulation_signal},
    "wcd_042_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_042_capitulation_signal},
    "wcd_043_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_043_capitulation_signal},
    "wcd_044_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_044_capitulation_signal},
    "wcd_045_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_045_capitulation_signal},
    "wcd_046_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_046_capitulation_signal},
    "wcd_047_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_047_capitulation_signal},
    "wcd_048_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_048_capitulation_signal},
    "wcd_049_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_049_capitulation_signal},
    "wcd_050_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_050_capitulation_signal},
    "wcd_051_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_051_capitulation_signal},
    "wcd_052_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_052_capitulation_signal},
    "wcd_053_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_053_capitulation_signal},
    "wcd_054_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_054_capitulation_signal},
    "wcd_055_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_055_capitulation_signal},
    "wcd_056_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_056_capitulation_signal},
    "wcd_057_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_057_capitulation_signal},
    "wcd_058_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_058_capitulation_signal},
    "wcd_059_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_059_capitulation_signal},
    "wcd_060_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_060_capitulation_signal},
    "wcd_061_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_061_capitulation_signal},
    "wcd_062_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_062_capitulation_signal},
    "wcd_063_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_063_capitulation_signal},
    "wcd_064_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_064_capitulation_signal},
    "wcd_065_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_065_capitulation_signal},
    "wcd_066_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_066_capitulation_signal},
    "wcd_067_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_067_capitulation_signal},
    "wcd_068_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_068_capitulation_signal},
    "wcd_069_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_069_capitulation_signal},
    "wcd_070_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_070_capitulation_signal},
    "wcd_071_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_071_capitulation_signal},
    "wcd_072_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_072_capitulation_signal},
    "wcd_073_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_073_capitulation_signal},
    "wcd_074_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_074_capitulation_signal},
    "wcd_075_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_075_capitulation_signal},
}
