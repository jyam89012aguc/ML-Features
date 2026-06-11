"""Generated capitulation features for 81_valuation_vs_history: multiples vs own history.
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

def vvh_001_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _z(x, 63)

def vvh_002_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _div(x, y)

def vvh_003_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _div(x - y, y.abs())

def vvh_004_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _rank(x, 504)

def vvh_005_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def vvh_006_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def vvh_007_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _div(x, _s(close))

def vvh_008_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def vvh_009_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def vvh_010_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def vvh_011_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def vvh_012_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vvh_013_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def vvh_014_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _s(x).pct_change(126)

def vvh_015_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _z(x, 252)

def vvh_016_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _div(x, y)

def vvh_017_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _div(x - y, y.abs())

def vvh_018_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _rank(x, 21)

def vvh_019_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def vvh_020_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def vvh_021_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _div(x, _s(close))

def vvh_022_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def vvh_023_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def vvh_024_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def vvh_025_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def vvh_026_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vvh_027_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def vvh_028_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _s(x).pct_change(504)

def vvh_029_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _z(x, 756)

def vvh_030_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _div(x, y)

def vvh_031_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _div(x - y, y.abs())

def vvh_032_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _rank(x, 126)

def vvh_033_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def vvh_034_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def vvh_035_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _div(x, _s(close))

def vvh_036_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def vvh_037_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def vvh_038_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def vvh_039_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def vvh_040_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vvh_041_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def vvh_042_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(21)

def vvh_043_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _z(x, 63)

def vvh_044_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _div(x, y)

def vvh_045_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _div(x - y, y.abs())

def vvh_046_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _rank(x, 504)

def vvh_047_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def vvh_048_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def vvh_049_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _div(x, _s(close))

def vvh_050_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def vvh_051_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def vvh_052_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def vvh_053_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def vvh_054_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vvh_055_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def vvh_056_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _s(x).pct_change(126)

def vvh_057_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _z(x, 252)

def vvh_058_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _div(x, y)

def vvh_059_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _div(x - y, y.abs())

def vvh_060_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _rank(x, 21)

def vvh_061_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def vvh_062_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def vvh_063_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _div(x, _s(close))

def vvh_064_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def vvh_065_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def vvh_066_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def vvh_067_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def vvh_068_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vvh_069_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def vvh_070_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _s(x).pct_change(504)

def vvh_071_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _z(x, 756)

def vvh_072_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _div(x, y)

def vvh_073_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _div(x - y, y.abs())

def vvh_074_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _rank(x, 126)

def vvh_075_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

VALUATION_VS_HISTORY_REGISTRY_001_075 = {
    "vvh_001_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_001_capitulation_signal},
    "vvh_002_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_002_capitulation_signal},
    "vvh_003_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_003_capitulation_signal},
    "vvh_004_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_004_capitulation_signal},
    "vvh_005_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_005_capitulation_signal},
    "vvh_006_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_006_capitulation_signal},
    "vvh_007_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_007_capitulation_signal},
    "vvh_008_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_008_capitulation_signal},
    "vvh_009_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_009_capitulation_signal},
    "vvh_010_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_010_capitulation_signal},
    "vvh_011_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_011_capitulation_signal},
    "vvh_012_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_012_capitulation_signal},
    "vvh_013_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_013_capitulation_signal},
    "vvh_014_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_014_capitulation_signal},
    "vvh_015_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_015_capitulation_signal},
    "vvh_016_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_016_capitulation_signal},
    "vvh_017_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_017_capitulation_signal},
    "vvh_018_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_018_capitulation_signal},
    "vvh_019_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_019_capitulation_signal},
    "vvh_020_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_020_capitulation_signal},
    "vvh_021_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_021_capitulation_signal},
    "vvh_022_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_022_capitulation_signal},
    "vvh_023_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_023_capitulation_signal},
    "vvh_024_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_024_capitulation_signal},
    "vvh_025_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_025_capitulation_signal},
    "vvh_026_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_026_capitulation_signal},
    "vvh_027_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_027_capitulation_signal},
    "vvh_028_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_028_capitulation_signal},
    "vvh_029_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_029_capitulation_signal},
    "vvh_030_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_030_capitulation_signal},
    "vvh_031_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_031_capitulation_signal},
    "vvh_032_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_032_capitulation_signal},
    "vvh_033_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_033_capitulation_signal},
    "vvh_034_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_034_capitulation_signal},
    "vvh_035_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_035_capitulation_signal},
    "vvh_036_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_036_capitulation_signal},
    "vvh_037_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_037_capitulation_signal},
    "vvh_038_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_038_capitulation_signal},
    "vvh_039_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_039_capitulation_signal},
    "vvh_040_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_040_capitulation_signal},
    "vvh_041_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_041_capitulation_signal},
    "vvh_042_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_042_capitulation_signal},
    "vvh_043_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_043_capitulation_signal},
    "vvh_044_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_044_capitulation_signal},
    "vvh_045_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_045_capitulation_signal},
    "vvh_046_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_046_capitulation_signal},
    "vvh_047_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_047_capitulation_signal},
    "vvh_048_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_048_capitulation_signal},
    "vvh_049_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_049_capitulation_signal},
    "vvh_050_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_050_capitulation_signal},
    "vvh_051_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_051_capitulation_signal},
    "vvh_052_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_052_capitulation_signal},
    "vvh_053_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_053_capitulation_signal},
    "vvh_054_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_054_capitulation_signal},
    "vvh_055_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_055_capitulation_signal},
    "vvh_056_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_056_capitulation_signal},
    "vvh_057_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_057_capitulation_signal},
    "vvh_058_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_058_capitulation_signal},
    "vvh_059_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_059_capitulation_signal},
    "vvh_060_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_060_capitulation_signal},
    "vvh_061_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_061_capitulation_signal},
    "vvh_062_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_062_capitulation_signal},
    "vvh_063_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_063_capitulation_signal},
    "vvh_064_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_064_capitulation_signal},
    "vvh_065_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_065_capitulation_signal},
    "vvh_066_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_066_capitulation_signal},
    "vvh_067_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_067_capitulation_signal},
    "vvh_068_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_068_capitulation_signal},
    "vvh_069_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_069_capitulation_signal},
    "vvh_070_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_070_capitulation_signal},
    "vvh_071_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_071_capitulation_signal},
    "vvh_072_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_072_capitulation_signal},
    "vvh_073_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_073_capitulation_signal},
    "vvh_074_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_074_capitulation_signal},
    "vvh_075_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_075_capitulation_signal},
}
