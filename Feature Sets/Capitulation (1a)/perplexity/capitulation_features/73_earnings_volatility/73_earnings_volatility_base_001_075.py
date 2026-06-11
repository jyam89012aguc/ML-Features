"""Generated capitulation features for 73_earnings_volatility: earnings instability.
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

def evl_001_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _z(x, 63)

def evl_002_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, y)

def evl_003_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(x - y, y.abs())

def evl_004_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _rank(x, 504)

def evl_005_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def evl_006_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def evl_007_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close))

def evl_008_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def evl_009_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def evl_010_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def evl_011_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def evl_012_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def evl_013_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def evl_014_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(126)

def evl_015_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _z(x, 252)

def evl_016_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(x, y)

def evl_017_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(x - y, y.abs())

def evl_018_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _rank(x, 21)

def evl_019_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def evl_020_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def evl_021_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(x, _s(close))

def evl_022_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def evl_023_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def evl_024_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def evl_025_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def evl_026_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def evl_027_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def evl_028_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).pct_change(504)

def evl_029_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _z(x, 756)

def evl_030_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x, y)

def evl_031_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(x - y, y.abs())

def evl_032_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _rank(x, 126)

def evl_033_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def evl_034_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def evl_035_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close))

def evl_036_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def evl_037_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def evl_038_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def evl_039_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def evl_040_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def evl_041_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def evl_042_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).pct_change(21)

def evl_043_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _z(x, 63)

def evl_044_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, y)

def evl_045_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(x - y, y.abs())

def evl_046_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _rank(x, 504)

def evl_047_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def evl_048_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def evl_049_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close))

def evl_050_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def evl_051_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def evl_052_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def evl_053_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def evl_054_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def evl_055_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def evl_056_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(126)

def evl_057_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _z(x, 252)

def evl_058_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(x, y)

def evl_059_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(x - y, y.abs())

def evl_060_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _rank(x, 21)

def evl_061_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def evl_062_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def evl_063_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(x, _s(close))

def evl_064_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def evl_065_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def evl_066_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def evl_067_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def evl_068_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def evl_069_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def evl_070_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).pct_change(504)

def evl_071_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _z(x, 756)

def evl_072_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x, y)

def evl_073_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(x - y, y.abs())

def evl_074_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _rank(x, 126)

def evl_075_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

EARNINGS_VOLATILITY_REGISTRY_001_075 = {
    "evl_001_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_001_capitulation_signal},
    "evl_002_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_002_capitulation_signal},
    "evl_003_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_003_capitulation_signal},
    "evl_004_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_004_capitulation_signal},
    "evl_005_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_005_capitulation_signal},
    "evl_006_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_006_capitulation_signal},
    "evl_007_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_007_capitulation_signal},
    "evl_008_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_008_capitulation_signal},
    "evl_009_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_009_capitulation_signal},
    "evl_010_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_010_capitulation_signal},
    "evl_011_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_011_capitulation_signal},
    "evl_012_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_012_capitulation_signal},
    "evl_013_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_013_capitulation_signal},
    "evl_014_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_014_capitulation_signal},
    "evl_015_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_015_capitulation_signal},
    "evl_016_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_016_capitulation_signal},
    "evl_017_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_017_capitulation_signal},
    "evl_018_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_018_capitulation_signal},
    "evl_019_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_019_capitulation_signal},
    "evl_020_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_020_capitulation_signal},
    "evl_021_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_021_capitulation_signal},
    "evl_022_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_022_capitulation_signal},
    "evl_023_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_023_capitulation_signal},
    "evl_024_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_024_capitulation_signal},
    "evl_025_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_025_capitulation_signal},
    "evl_026_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_026_capitulation_signal},
    "evl_027_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_027_capitulation_signal},
    "evl_028_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_028_capitulation_signal},
    "evl_029_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_029_capitulation_signal},
    "evl_030_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_030_capitulation_signal},
    "evl_031_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_031_capitulation_signal},
    "evl_032_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_032_capitulation_signal},
    "evl_033_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_033_capitulation_signal},
    "evl_034_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_034_capitulation_signal},
    "evl_035_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_035_capitulation_signal},
    "evl_036_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_036_capitulation_signal},
    "evl_037_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_037_capitulation_signal},
    "evl_038_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_038_capitulation_signal},
    "evl_039_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_039_capitulation_signal},
    "evl_040_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_040_capitulation_signal},
    "evl_041_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_041_capitulation_signal},
    "evl_042_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_042_capitulation_signal},
    "evl_043_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_043_capitulation_signal},
    "evl_044_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_044_capitulation_signal},
    "evl_045_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_045_capitulation_signal},
    "evl_046_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_046_capitulation_signal},
    "evl_047_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_047_capitulation_signal},
    "evl_048_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_048_capitulation_signal},
    "evl_049_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_049_capitulation_signal},
    "evl_050_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_050_capitulation_signal},
    "evl_051_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_051_capitulation_signal},
    "evl_052_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_052_capitulation_signal},
    "evl_053_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_053_capitulation_signal},
    "evl_054_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_054_capitulation_signal},
    "evl_055_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_055_capitulation_signal},
    "evl_056_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_056_capitulation_signal},
    "evl_057_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_057_capitulation_signal},
    "evl_058_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_058_capitulation_signal},
    "evl_059_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_059_capitulation_signal},
    "evl_060_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_060_capitulation_signal},
    "evl_061_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_061_capitulation_signal},
    "evl_062_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_062_capitulation_signal},
    "evl_063_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_063_capitulation_signal},
    "evl_064_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_064_capitulation_signal},
    "evl_065_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_065_capitulation_signal},
    "evl_066_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_066_capitulation_signal},
    "evl_067_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_067_capitulation_signal},
    "evl_068_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_068_capitulation_signal},
    "evl_069_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_069_capitulation_signal},
    "evl_070_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_070_capitulation_signal},
    "evl_071_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_071_capitulation_signal},
    "evl_072_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_072_capitulation_signal},
    "evl_073_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_073_capitulation_signal},
    "evl_074_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_074_capitulation_signal},
    "evl_075_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_075_capitulation_signal},
}
