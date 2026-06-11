"""Generated capitulation features for 78_marketcap_destruction: market-cap destruction.
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

def mcd_001_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _z(x, 63)

def mcd_002_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _div(x, y)

def mcd_003_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _div(x - y, y.abs())

def mcd_004_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _rank(x, 504)

def mcd_005_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def mcd_006_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def mcd_007_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _div(x, _s(close))

def mcd_008_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def mcd_009_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def mcd_010_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def mcd_011_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def mcd_012_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def mcd_013_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def mcd_014_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _s(x).pct_change(126)

def mcd_015_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _z(x, 252)

def mcd_016_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _div(x, y)

def mcd_017_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _div(x - y, y.abs())

def mcd_018_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _rank(x, 21)

def mcd_019_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def mcd_020_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def mcd_021_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _div(x, _s(close))

def mcd_022_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def mcd_023_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def mcd_024_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def mcd_025_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def mcd_026_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def mcd_027_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def mcd_028_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _s(x).pct_change(504)

def mcd_029_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _z(x, 756)

def mcd_030_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _div(x, y)

def mcd_031_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _div(x - y, y.abs())

def mcd_032_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _rank(x, 126)

def mcd_033_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def mcd_034_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def mcd_035_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _div(x, _s(close))

def mcd_036_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def mcd_037_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def mcd_038_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def mcd_039_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def mcd_040_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def mcd_041_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def mcd_042_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(21)

def mcd_043_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _z(x, 63)

def mcd_044_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _div(x, y)

def mcd_045_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _div(x - y, y.abs())

def mcd_046_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _rank(x, 504)

def mcd_047_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def mcd_048_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def mcd_049_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _div(x, _s(close))

def mcd_050_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def mcd_051_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def mcd_052_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def mcd_053_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def mcd_054_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def mcd_055_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def mcd_056_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _s(x).pct_change(126)

def mcd_057_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _z(x, 252)

def mcd_058_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _div(x, y)

def mcd_059_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _div(x - y, y.abs())

def mcd_060_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _rank(x, 21)

def mcd_061_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def mcd_062_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def mcd_063_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _div(x, _s(close))

def mcd_064_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def mcd_065_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def mcd_066_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def mcd_067_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def mcd_068_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def mcd_069_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def mcd_070_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _s(x).pct_change(504)

def mcd_071_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _z(x, 756)

def mcd_072_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _div(x, y)

def mcd_073_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _div(x - y, y.abs())

def mcd_074_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _rank(x, 126)

def mcd_075_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

MARKETCAP_DESTRUCTION_REGISTRY_001_075 = {
    "mcd_001_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_001_capitulation_signal},
    "mcd_002_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_002_capitulation_signal},
    "mcd_003_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_003_capitulation_signal},
    "mcd_004_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_004_capitulation_signal},
    "mcd_005_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_005_capitulation_signal},
    "mcd_006_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_006_capitulation_signal},
    "mcd_007_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_007_capitulation_signal},
    "mcd_008_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_008_capitulation_signal},
    "mcd_009_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_009_capitulation_signal},
    "mcd_010_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_010_capitulation_signal},
    "mcd_011_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_011_capitulation_signal},
    "mcd_012_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_012_capitulation_signal},
    "mcd_013_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_013_capitulation_signal},
    "mcd_014_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_014_capitulation_signal},
    "mcd_015_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_015_capitulation_signal},
    "mcd_016_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_016_capitulation_signal},
    "mcd_017_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_017_capitulation_signal},
    "mcd_018_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_018_capitulation_signal},
    "mcd_019_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_019_capitulation_signal},
    "mcd_020_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_020_capitulation_signal},
    "mcd_021_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_021_capitulation_signal},
    "mcd_022_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_022_capitulation_signal},
    "mcd_023_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_023_capitulation_signal},
    "mcd_024_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_024_capitulation_signal},
    "mcd_025_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_025_capitulation_signal},
    "mcd_026_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_026_capitulation_signal},
    "mcd_027_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_027_capitulation_signal},
    "mcd_028_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_028_capitulation_signal},
    "mcd_029_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_029_capitulation_signal},
    "mcd_030_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_030_capitulation_signal},
    "mcd_031_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_031_capitulation_signal},
    "mcd_032_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_032_capitulation_signal},
    "mcd_033_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_033_capitulation_signal},
    "mcd_034_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_034_capitulation_signal},
    "mcd_035_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_035_capitulation_signal},
    "mcd_036_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_036_capitulation_signal},
    "mcd_037_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_037_capitulation_signal},
    "mcd_038_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_038_capitulation_signal},
    "mcd_039_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_039_capitulation_signal},
    "mcd_040_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_040_capitulation_signal},
    "mcd_041_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_041_capitulation_signal},
    "mcd_042_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_042_capitulation_signal},
    "mcd_043_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_043_capitulation_signal},
    "mcd_044_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_044_capitulation_signal},
    "mcd_045_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_045_capitulation_signal},
    "mcd_046_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_046_capitulation_signal},
    "mcd_047_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_047_capitulation_signal},
    "mcd_048_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_048_capitulation_signal},
    "mcd_049_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_049_capitulation_signal},
    "mcd_050_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_050_capitulation_signal},
    "mcd_051_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_051_capitulation_signal},
    "mcd_052_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_052_capitulation_signal},
    "mcd_053_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_053_capitulation_signal},
    "mcd_054_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_054_capitulation_signal},
    "mcd_055_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_055_capitulation_signal},
    "mcd_056_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_056_capitulation_signal},
    "mcd_057_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_057_capitulation_signal},
    "mcd_058_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_058_capitulation_signal},
    "mcd_059_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_059_capitulation_signal},
    "mcd_060_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_060_capitulation_signal},
    "mcd_061_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_061_capitulation_signal},
    "mcd_062_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_062_capitulation_signal},
    "mcd_063_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_063_capitulation_signal},
    "mcd_064_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_064_capitulation_signal},
    "mcd_065_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_065_capitulation_signal},
    "mcd_066_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_066_capitulation_signal},
    "mcd_067_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_067_capitulation_signal},
    "mcd_068_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_068_capitulation_signal},
    "mcd_069_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_069_capitulation_signal},
    "mcd_070_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_070_capitulation_signal},
    "mcd_071_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_071_capitulation_signal},
    "mcd_072_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_072_capitulation_signal},
    "mcd_073_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_073_capitulation_signal},
    "mcd_074_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_074_capitulation_signal},
    "mcd_075_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": mcd_075_capitulation_signal},
}
