"""Generated capitulation features for 61_revenue_deterioration: revenue contraction.
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

def rvd_001_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _z(x, 63)

def rvd_002_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _div(x, y)

def rvd_003_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _div(x - y, y.abs())

def rvd_004_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _rank(x, 504)

def rvd_005_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def rvd_006_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def rvd_007_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close))

def rvd_008_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def rvd_009_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def rvd_010_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def rvd_011_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def rvd_012_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def rvd_013_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def rvd_014_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(126)

def rvd_015_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _z(x, 252)

def rvd_016_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _div(x, y)

def rvd_017_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _div(x - y, y.abs())

def rvd_018_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _rank(x, 21)

def rvd_019_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def rvd_020_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def rvd_021_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close))

def rvd_022_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def rvd_023_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def rvd_024_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def rvd_025_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def rvd_026_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def rvd_027_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def rvd_028_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _s(x).pct_change(504)

def rvd_029_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _z(x, 756)

def rvd_030_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(x, y)

def rvd_031_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _div(x - y, y.abs())

def rvd_032_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _rank(x, 126)

def rvd_033_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def rvd_034_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def rvd_035_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(x, _s(close))

def rvd_036_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def rvd_037_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def rvd_038_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def rvd_039_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def rvd_040_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def rvd_041_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def rvd_042_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _s(x).pct_change(21)

def rvd_043_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _z(x, 63)

def rvd_044_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _div(x, y)

def rvd_045_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(x - y, y.abs())

def rvd_046_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _rank(x, 504)

def rvd_047_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def rvd_048_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def rvd_049_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close))

def rvd_050_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def rvd_051_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def rvd_052_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def rvd_053_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def rvd_054_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def rvd_055_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def rvd_056_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(126)

def rvd_057_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _z(x, 252)

def rvd_058_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _div(x, y)

def rvd_059_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _div(x - y, y.abs())

def rvd_060_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _rank(x, 21)

def rvd_061_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def rvd_062_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def rvd_063_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _div(x, _s(close))

def rvd_064_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def rvd_065_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def rvd_066_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def rvd_067_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def rvd_068_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def rvd_069_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def rvd_070_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _s(x).pct_change(504)

def rvd_071_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _z(x, 756)

def rvd_072_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _div(x, y)

def rvd_073_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _div(x - y, y.abs())

def rvd_074_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _rank(x, 126)

def rvd_075_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

REVENUE_DETERIORATION_REGISTRY_001_075 = {
    "rvd_001_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_001_capitulation_signal},
    "rvd_002_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_002_capitulation_signal},
    "rvd_003_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_003_capitulation_signal},
    "rvd_004_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_004_capitulation_signal},
    "rvd_005_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_005_capitulation_signal},
    "rvd_006_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_006_capitulation_signal},
    "rvd_007_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_007_capitulation_signal},
    "rvd_008_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_008_capitulation_signal},
    "rvd_009_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_009_capitulation_signal},
    "rvd_010_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_010_capitulation_signal},
    "rvd_011_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_011_capitulation_signal},
    "rvd_012_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_012_capitulation_signal},
    "rvd_013_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_013_capitulation_signal},
    "rvd_014_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_014_capitulation_signal},
    "rvd_015_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_015_capitulation_signal},
    "rvd_016_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_016_capitulation_signal},
    "rvd_017_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_017_capitulation_signal},
    "rvd_018_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_018_capitulation_signal},
    "rvd_019_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_019_capitulation_signal},
    "rvd_020_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_020_capitulation_signal},
    "rvd_021_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_021_capitulation_signal},
    "rvd_022_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_022_capitulation_signal},
    "rvd_023_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_023_capitulation_signal},
    "rvd_024_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_024_capitulation_signal},
    "rvd_025_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_025_capitulation_signal},
    "rvd_026_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_026_capitulation_signal},
    "rvd_027_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_027_capitulation_signal},
    "rvd_028_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_028_capitulation_signal},
    "rvd_029_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_029_capitulation_signal},
    "rvd_030_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_030_capitulation_signal},
    "rvd_031_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_031_capitulation_signal},
    "rvd_032_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_032_capitulation_signal},
    "rvd_033_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_033_capitulation_signal},
    "rvd_034_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_034_capitulation_signal},
    "rvd_035_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_035_capitulation_signal},
    "rvd_036_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_036_capitulation_signal},
    "rvd_037_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_037_capitulation_signal},
    "rvd_038_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_038_capitulation_signal},
    "rvd_039_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_039_capitulation_signal},
    "rvd_040_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_040_capitulation_signal},
    "rvd_041_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_041_capitulation_signal},
    "rvd_042_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_042_capitulation_signal},
    "rvd_043_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_043_capitulation_signal},
    "rvd_044_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_044_capitulation_signal},
    "rvd_045_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_045_capitulation_signal},
    "rvd_046_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_046_capitulation_signal},
    "rvd_047_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_047_capitulation_signal},
    "rvd_048_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_048_capitulation_signal},
    "rvd_049_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_049_capitulation_signal},
    "rvd_050_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_050_capitulation_signal},
    "rvd_051_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_051_capitulation_signal},
    "rvd_052_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_052_capitulation_signal},
    "rvd_053_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_053_capitulation_signal},
    "rvd_054_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_054_capitulation_signal},
    "rvd_055_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_055_capitulation_signal},
    "rvd_056_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_056_capitulation_signal},
    "rvd_057_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_057_capitulation_signal},
    "rvd_058_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_058_capitulation_signal},
    "rvd_059_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_059_capitulation_signal},
    "rvd_060_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_060_capitulation_signal},
    "rvd_061_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_061_capitulation_signal},
    "rvd_062_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_062_capitulation_signal},
    "rvd_063_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_063_capitulation_signal},
    "rvd_064_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_064_capitulation_signal},
    "rvd_065_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_065_capitulation_signal},
    "rvd_066_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_066_capitulation_signal},
    "rvd_067_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_067_capitulation_signal},
    "rvd_068_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_068_capitulation_signal},
    "rvd_069_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_069_capitulation_signal},
    "rvd_070_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_070_capitulation_signal},
    "rvd_071_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_071_capitulation_signal},
    "rvd_072_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_072_capitulation_signal},
    "rvd_073_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_073_capitulation_signal},
    "rvd_074_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_074_capitulation_signal},
    "rvd_075_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_075_capitulation_signal},
}
