"""Generated capitulation features for 96_dividend_distress: dividend cuts/omissions.
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

def dvd_001_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _z(x, 63)

def dvd_002_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x, y)

def dvd_003_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x - y, y.abs())

def dvd_004_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _rank(x, 504)

def dvd_005_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def dvd_006_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def dvd_007_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x, _s(close))

def dvd_008_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def dvd_009_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def dvd_010_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def dvd_011_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def dvd_012_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def dvd_013_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def dvd_014_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _s(x).pct_change(126)

def dvd_015_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _z(x, 252)

def dvd_016_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(x, y)

def dvd_017_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x - y, y.abs())

def dvd_018_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _rank(x, 21)

def dvd_019_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def dvd_020_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def dvd_021_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(x, _s(close))

def dvd_022_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def dvd_023_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def dvd_024_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def dvd_025_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def dvd_026_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def dvd_027_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def dvd_028_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _s(x).pct_change(504)

def dvd_029_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _z(x, 756)

def dvd_030_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(x, y)

def dvd_031_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(x - y, y.abs())

def dvd_032_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _rank(x, 126)

def dvd_033_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def dvd_034_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def dvd_035_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(x, _s(close))

def dvd_036_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def dvd_037_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def dvd_038_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def dvd_039_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def dvd_040_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def dvd_041_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def dvd_042_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _s(x).pct_change(21)

def dvd_043_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _z(x, 63)

def dvd_044_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(x, y)

def dvd_045_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(x - y, y.abs())

def dvd_046_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _rank(x, 504)

def dvd_047_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def dvd_048_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def dvd_049_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(x, _s(close))

def dvd_050_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def dvd_051_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def dvd_052_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def dvd_053_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def dvd_054_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def dvd_055_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def dvd_056_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _s(x).pct_change(126)

def dvd_057_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _z(x, 252)

def dvd_058_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x, y)

def dvd_059_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(x - y, y.abs())

def dvd_060_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _rank(x, 21)

def dvd_061_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def dvd_062_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def dvd_063_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x, _s(close))

def dvd_064_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def dvd_065_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def dvd_066_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def dvd_067_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def dvd_068_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def dvd_069_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def dvd_070_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _s(x).pct_change(504)

def dvd_071_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _z(x, 756)

def dvd_072_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x, y)

def dvd_073_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x - y, y.abs())

def dvd_074_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _rank(x, 126)

def dvd_075_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

DIVIDEND_DISTRESS_REGISTRY_001_075 = {
    "dvd_001_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_001_capitulation_signal},
    "dvd_002_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_002_capitulation_signal},
    "dvd_003_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_003_capitulation_signal},
    "dvd_004_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_004_capitulation_signal},
    "dvd_005_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_005_capitulation_signal},
    "dvd_006_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_006_capitulation_signal},
    "dvd_007_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_007_capitulation_signal},
    "dvd_008_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_008_capitulation_signal},
    "dvd_009_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_009_capitulation_signal},
    "dvd_010_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_010_capitulation_signal},
    "dvd_011_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_011_capitulation_signal},
    "dvd_012_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_012_capitulation_signal},
    "dvd_013_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_013_capitulation_signal},
    "dvd_014_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_014_capitulation_signal},
    "dvd_015_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_015_capitulation_signal},
    "dvd_016_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_016_capitulation_signal},
    "dvd_017_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_017_capitulation_signal},
    "dvd_018_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_018_capitulation_signal},
    "dvd_019_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_019_capitulation_signal},
    "dvd_020_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_020_capitulation_signal},
    "dvd_021_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_021_capitulation_signal},
    "dvd_022_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_022_capitulation_signal},
    "dvd_023_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_023_capitulation_signal},
    "dvd_024_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_024_capitulation_signal},
    "dvd_025_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_025_capitulation_signal},
    "dvd_026_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_026_capitulation_signal},
    "dvd_027_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_027_capitulation_signal},
    "dvd_028_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_028_capitulation_signal},
    "dvd_029_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_029_capitulation_signal},
    "dvd_030_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_030_capitulation_signal},
    "dvd_031_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_031_capitulation_signal},
    "dvd_032_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_032_capitulation_signal},
    "dvd_033_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_033_capitulation_signal},
    "dvd_034_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_034_capitulation_signal},
    "dvd_035_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_035_capitulation_signal},
    "dvd_036_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_036_capitulation_signal},
    "dvd_037_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_037_capitulation_signal},
    "dvd_038_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_038_capitulation_signal},
    "dvd_039_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_039_capitulation_signal},
    "dvd_040_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_040_capitulation_signal},
    "dvd_041_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_041_capitulation_signal},
    "dvd_042_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_042_capitulation_signal},
    "dvd_043_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_043_capitulation_signal},
    "dvd_044_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_044_capitulation_signal},
    "dvd_045_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_045_capitulation_signal},
    "dvd_046_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_046_capitulation_signal},
    "dvd_047_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_047_capitulation_signal},
    "dvd_048_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_048_capitulation_signal},
    "dvd_049_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_049_capitulation_signal},
    "dvd_050_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_050_capitulation_signal},
    "dvd_051_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_051_capitulation_signal},
    "dvd_052_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_052_capitulation_signal},
    "dvd_053_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_053_capitulation_signal},
    "dvd_054_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_054_capitulation_signal},
    "dvd_055_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_055_capitulation_signal},
    "dvd_056_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_056_capitulation_signal},
    "dvd_057_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_057_capitulation_signal},
    "dvd_058_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_058_capitulation_signal},
    "dvd_059_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_059_capitulation_signal},
    "dvd_060_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_060_capitulation_signal},
    "dvd_061_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_061_capitulation_signal},
    "dvd_062_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_062_capitulation_signal},
    "dvd_063_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_063_capitulation_signal},
    "dvd_064_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_064_capitulation_signal},
    "dvd_065_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_065_capitulation_signal},
    "dvd_066_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_066_capitulation_signal},
    "dvd_067_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_067_capitulation_signal},
    "dvd_068_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_068_capitulation_signal},
    "dvd_069_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_069_capitulation_signal},
    "dvd_070_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_070_capitulation_signal},
    "dvd_071_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_071_capitulation_signal},
    "dvd_072_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_072_capitulation_signal},
    "dvd_073_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_073_capitulation_signal},
    "dvd_074_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_074_capitulation_signal},
    "dvd_075_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": dvd_075_capitulation_signal},
}
