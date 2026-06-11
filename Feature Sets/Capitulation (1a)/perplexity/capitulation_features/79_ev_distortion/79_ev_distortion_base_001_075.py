"""Generated capitulation features for 79_ev_distortion: EV/equity distortion.
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

def evd_001_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _z(x, 63)

def evd_002_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _div(x, y)

def evd_003_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _div(x - y, y.abs())

def evd_004_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _rank(x, 504)

def evd_005_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def evd_006_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def evd_007_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _div(x, _s(close))

def evd_008_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def evd_009_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def evd_010_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def evd_011_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def evd_012_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def evd_013_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def evd_014_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _s(x).pct_change(126)

def evd_015_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _z(x, 252)

def evd_016_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _div(x, y)

def evd_017_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _div(x - y, y.abs())

def evd_018_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _rank(x, 21)

def evd_019_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def evd_020_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def evd_021_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _div(x, _s(close))

def evd_022_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def evd_023_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def evd_024_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def evd_025_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def evd_026_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def evd_027_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def evd_028_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _s(x).pct_change(504)

def evd_029_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _z(x, 756)

def evd_030_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _div(x, y)

def evd_031_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _div(x - y, y.abs())

def evd_032_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _rank(x, 126)

def evd_033_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def evd_034_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def evd_035_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _div(x, _s(close))

def evd_036_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def evd_037_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def evd_038_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def evd_039_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def evd_040_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def evd_041_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def evd_042_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(21)

def evd_043_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _z(x, 63)

def evd_044_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _div(x, y)

def evd_045_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _div(x - y, y.abs())

def evd_046_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _rank(x, 504)

def evd_047_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def evd_048_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def evd_049_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _div(x, _s(close))

def evd_050_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def evd_051_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def evd_052_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def evd_053_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def evd_054_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def evd_055_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def evd_056_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _s(x).pct_change(126)

def evd_057_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _z(x, 252)

def evd_058_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _div(x, y)

def evd_059_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _div(x - y, y.abs())

def evd_060_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _rank(x, 21)

def evd_061_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def evd_062_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def evd_063_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _div(x, _s(close))

def evd_064_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def evd_065_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def evd_066_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def evd_067_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def evd_068_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def evd_069_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def evd_070_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _s(x).pct_change(504)

def evd_071_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _z(x, 756)

def evd_072_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _div(x, y)

def evd_073_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _div(x - y, y.abs())

def evd_074_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _rank(x, 126)

def evd_075_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

EV_DISTORTION_REGISTRY_001_075 = {
    "evd_001_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_001_capitulation_signal},
    "evd_002_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_002_capitulation_signal},
    "evd_003_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_003_capitulation_signal},
    "evd_004_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_004_capitulation_signal},
    "evd_005_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_005_capitulation_signal},
    "evd_006_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_006_capitulation_signal},
    "evd_007_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_007_capitulation_signal},
    "evd_008_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_008_capitulation_signal},
    "evd_009_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_009_capitulation_signal},
    "evd_010_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_010_capitulation_signal},
    "evd_011_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_011_capitulation_signal},
    "evd_012_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_012_capitulation_signal},
    "evd_013_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_013_capitulation_signal},
    "evd_014_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_014_capitulation_signal},
    "evd_015_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_015_capitulation_signal},
    "evd_016_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_016_capitulation_signal},
    "evd_017_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_017_capitulation_signal},
    "evd_018_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_018_capitulation_signal},
    "evd_019_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_019_capitulation_signal},
    "evd_020_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_020_capitulation_signal},
    "evd_021_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_021_capitulation_signal},
    "evd_022_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_022_capitulation_signal},
    "evd_023_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_023_capitulation_signal},
    "evd_024_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_024_capitulation_signal},
    "evd_025_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_025_capitulation_signal},
    "evd_026_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_026_capitulation_signal},
    "evd_027_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_027_capitulation_signal},
    "evd_028_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_028_capitulation_signal},
    "evd_029_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_029_capitulation_signal},
    "evd_030_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_030_capitulation_signal},
    "evd_031_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_031_capitulation_signal},
    "evd_032_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_032_capitulation_signal},
    "evd_033_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_033_capitulation_signal},
    "evd_034_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_034_capitulation_signal},
    "evd_035_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_035_capitulation_signal},
    "evd_036_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_036_capitulation_signal},
    "evd_037_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_037_capitulation_signal},
    "evd_038_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_038_capitulation_signal},
    "evd_039_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_039_capitulation_signal},
    "evd_040_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_040_capitulation_signal},
    "evd_041_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_041_capitulation_signal},
    "evd_042_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_042_capitulation_signal},
    "evd_043_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_043_capitulation_signal},
    "evd_044_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_044_capitulation_signal},
    "evd_045_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_045_capitulation_signal},
    "evd_046_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_046_capitulation_signal},
    "evd_047_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_047_capitulation_signal},
    "evd_048_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_048_capitulation_signal},
    "evd_049_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_049_capitulation_signal},
    "evd_050_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_050_capitulation_signal},
    "evd_051_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_051_capitulation_signal},
    "evd_052_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_052_capitulation_signal},
    "evd_053_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_053_capitulation_signal},
    "evd_054_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_054_capitulation_signal},
    "evd_055_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_055_capitulation_signal},
    "evd_056_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_056_capitulation_signal},
    "evd_057_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_057_capitulation_signal},
    "evd_058_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_058_capitulation_signal},
    "evd_059_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_059_capitulation_signal},
    "evd_060_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_060_capitulation_signal},
    "evd_061_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_061_capitulation_signal},
    "evd_062_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_062_capitulation_signal},
    "evd_063_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_063_capitulation_signal},
    "evd_064_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_064_capitulation_signal},
    "evd_065_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_065_capitulation_signal},
    "evd_066_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_066_capitulation_signal},
    "evd_067_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_067_capitulation_signal},
    "evd_068_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_068_capitulation_signal},
    "evd_069_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_069_capitulation_signal},
    "evd_070_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_070_capitulation_signal},
    "evd_071_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_071_capitulation_signal},
    "evd_072_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_072_capitulation_signal},
    "evd_073_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_073_capitulation_signal},
    "evd_074_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_074_capitulation_signal},
    "evd_075_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": evd_075_capitulation_signal},
}
