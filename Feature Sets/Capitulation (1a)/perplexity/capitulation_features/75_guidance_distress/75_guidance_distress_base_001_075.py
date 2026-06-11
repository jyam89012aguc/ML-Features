"""Generated capitulation features for 75_guidance_distress: guidance/miss distress.
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

def gds_001_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _z(x, 63)

def gds_002_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, y)

def gds_003_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(x - y, y.abs())

def gds_004_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _rank(x, 504)

def gds_005_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def gds_006_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def gds_007_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close))

def gds_008_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def gds_009_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def gds_010_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def gds_011_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def gds_012_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def gds_013_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def gds_014_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(126)

def gds_015_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _z(x, 252)

def gds_016_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(x, y)

def gds_017_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(x - y, y.abs())

def gds_018_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _rank(x, 21)

def gds_019_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def gds_020_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def gds_021_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(x, _s(close))

def gds_022_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def gds_023_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def gds_024_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def gds_025_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def gds_026_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def gds_027_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def gds_028_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).pct_change(504)

def gds_029_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _z(x, 756)

def gds_030_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x, y)

def gds_031_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(x - y, y.abs())

def gds_032_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _rank(x, 126)

def gds_033_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def gds_034_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def gds_035_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close))

def gds_036_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def gds_037_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def gds_038_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def gds_039_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def gds_040_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def gds_041_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def gds_042_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).pct_change(21)

def gds_043_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _z(x, 63)

def gds_044_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, y)

def gds_045_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(x - y, y.abs())

def gds_046_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _rank(x, 504)

def gds_047_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def gds_048_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def gds_049_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close))

def gds_050_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def gds_051_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def gds_052_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def gds_053_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def gds_054_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def gds_055_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def gds_056_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(126)

def gds_057_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _z(x, 252)

def gds_058_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(x, y)

def gds_059_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(x - y, y.abs())

def gds_060_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _rank(x, 21)

def gds_061_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def gds_062_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def gds_063_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(x, _s(close))

def gds_064_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def gds_065_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def gds_066_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def gds_067_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def gds_068_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def gds_069_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def gds_070_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).pct_change(504)

def gds_071_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _z(x, 756)

def gds_072_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x, y)

def gds_073_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(x - y, y.abs())

def gds_074_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _rank(x, 126)

def gds_075_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

GUIDANCE_DISTRESS_REGISTRY_001_075 = {
    "gds_001_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_001_capitulation_signal},
    "gds_002_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_002_capitulation_signal},
    "gds_003_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_003_capitulation_signal},
    "gds_004_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_004_capitulation_signal},
    "gds_005_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_005_capitulation_signal},
    "gds_006_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_006_capitulation_signal},
    "gds_007_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_007_capitulation_signal},
    "gds_008_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_008_capitulation_signal},
    "gds_009_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_009_capitulation_signal},
    "gds_010_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_010_capitulation_signal},
    "gds_011_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_011_capitulation_signal},
    "gds_012_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_012_capitulation_signal},
    "gds_013_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_013_capitulation_signal},
    "gds_014_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_014_capitulation_signal},
    "gds_015_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_015_capitulation_signal},
    "gds_016_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_016_capitulation_signal},
    "gds_017_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_017_capitulation_signal},
    "gds_018_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_018_capitulation_signal},
    "gds_019_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_019_capitulation_signal},
    "gds_020_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_020_capitulation_signal},
    "gds_021_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_021_capitulation_signal},
    "gds_022_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_022_capitulation_signal},
    "gds_023_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_023_capitulation_signal},
    "gds_024_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_024_capitulation_signal},
    "gds_025_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_025_capitulation_signal},
    "gds_026_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_026_capitulation_signal},
    "gds_027_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_027_capitulation_signal},
    "gds_028_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_028_capitulation_signal},
    "gds_029_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_029_capitulation_signal},
    "gds_030_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_030_capitulation_signal},
    "gds_031_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_031_capitulation_signal},
    "gds_032_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_032_capitulation_signal},
    "gds_033_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_033_capitulation_signal},
    "gds_034_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_034_capitulation_signal},
    "gds_035_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_035_capitulation_signal},
    "gds_036_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_036_capitulation_signal},
    "gds_037_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_037_capitulation_signal},
    "gds_038_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_038_capitulation_signal},
    "gds_039_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_039_capitulation_signal},
    "gds_040_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_040_capitulation_signal},
    "gds_041_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_041_capitulation_signal},
    "gds_042_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_042_capitulation_signal},
    "gds_043_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_043_capitulation_signal},
    "gds_044_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_044_capitulation_signal},
    "gds_045_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_045_capitulation_signal},
    "gds_046_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_046_capitulation_signal},
    "gds_047_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_047_capitulation_signal},
    "gds_048_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_048_capitulation_signal},
    "gds_049_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_049_capitulation_signal},
    "gds_050_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_050_capitulation_signal},
    "gds_051_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_051_capitulation_signal},
    "gds_052_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_052_capitulation_signal},
    "gds_053_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_053_capitulation_signal},
    "gds_054_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_054_capitulation_signal},
    "gds_055_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_055_capitulation_signal},
    "gds_056_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_056_capitulation_signal},
    "gds_057_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_057_capitulation_signal},
    "gds_058_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_058_capitulation_signal},
    "gds_059_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_059_capitulation_signal},
    "gds_060_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_060_capitulation_signal},
    "gds_061_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_061_capitulation_signal},
    "gds_062_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_062_capitulation_signal},
    "gds_063_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_063_capitulation_signal},
    "gds_064_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_064_capitulation_signal},
    "gds_065_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_065_capitulation_signal},
    "gds_066_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_066_capitulation_signal},
    "gds_067_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_067_capitulation_signal},
    "gds_068_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_068_capitulation_signal},
    "gds_069_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_069_capitulation_signal},
    "gds_070_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_070_capitulation_signal},
    "gds_071_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_071_capitulation_signal},
    "gds_072_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_072_capitulation_signal},
    "gds_073_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_073_capitulation_signal},
    "gds_074_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_074_capitulation_signal},
    "gds_075_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_075_capitulation_signal},
}
