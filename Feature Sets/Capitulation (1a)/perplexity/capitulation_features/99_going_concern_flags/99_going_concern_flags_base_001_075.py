"""Generated capitulation features for 99_going_concern_flags: going-concern flags.
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

def gcf_001_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _z(x, 63)

def gcf_002_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x, y)

def gcf_003_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x - y, y.abs())

def gcf_004_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _rank(x, 504)

def gcf_005_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def gcf_006_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def gcf_007_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x, _s(close))

def gcf_008_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def gcf_009_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def gcf_010_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def gcf_011_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def gcf_012_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def gcf_013_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def gcf_014_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _s(x).pct_change(126)

def gcf_015_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _z(x, 252)

def gcf_016_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(x, y)

def gcf_017_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x - y, y.abs())

def gcf_018_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _rank(x, 21)

def gcf_019_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def gcf_020_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def gcf_021_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(x, _s(close))

def gcf_022_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def gcf_023_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def gcf_024_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def gcf_025_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def gcf_026_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def gcf_027_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def gcf_028_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _s(x).pct_change(504)

def gcf_029_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _z(x, 756)

def gcf_030_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(x, y)

def gcf_031_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(x - y, y.abs())

def gcf_032_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _rank(x, 126)

def gcf_033_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def gcf_034_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def gcf_035_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(x, _s(close))

def gcf_036_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def gcf_037_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def gcf_038_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def gcf_039_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def gcf_040_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def gcf_041_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def gcf_042_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _s(x).pct_change(21)

def gcf_043_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _z(x, 63)

def gcf_044_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(x, y)

def gcf_045_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(x - y, y.abs())

def gcf_046_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _rank(x, 504)

def gcf_047_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def gcf_048_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def gcf_049_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(x, _s(close))

def gcf_050_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def gcf_051_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def gcf_052_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def gcf_053_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def gcf_054_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def gcf_055_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def gcf_056_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _s(x).pct_change(126)

def gcf_057_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _z(x, 252)

def gcf_058_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x, y)

def gcf_059_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(x - y, y.abs())

def gcf_060_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _rank(x, 21)

def gcf_061_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def gcf_062_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def gcf_063_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x, _s(close))

def gcf_064_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def gcf_065_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def gcf_066_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def gcf_067_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def gcf_068_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def gcf_069_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def gcf_070_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _s(x).pct_change(504)

def gcf_071_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _z(x, 756)

def gcf_072_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x, y)

def gcf_073_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x - y, y.abs())

def gcf_074_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _rank(x, 126)

def gcf_075_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

GOING_CONCERN_FLAGS_REGISTRY_001_075 = {
    "gcf_001_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_001_capitulation_signal},
    "gcf_002_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_002_capitulation_signal},
    "gcf_003_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_003_capitulation_signal},
    "gcf_004_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_004_capitulation_signal},
    "gcf_005_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_005_capitulation_signal},
    "gcf_006_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_006_capitulation_signal},
    "gcf_007_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_007_capitulation_signal},
    "gcf_008_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_008_capitulation_signal},
    "gcf_009_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_009_capitulation_signal},
    "gcf_010_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_010_capitulation_signal},
    "gcf_011_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_011_capitulation_signal},
    "gcf_012_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_012_capitulation_signal},
    "gcf_013_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_013_capitulation_signal},
    "gcf_014_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_014_capitulation_signal},
    "gcf_015_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_015_capitulation_signal},
    "gcf_016_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_016_capitulation_signal},
    "gcf_017_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_017_capitulation_signal},
    "gcf_018_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_018_capitulation_signal},
    "gcf_019_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_019_capitulation_signal},
    "gcf_020_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_020_capitulation_signal},
    "gcf_021_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_021_capitulation_signal},
    "gcf_022_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_022_capitulation_signal},
    "gcf_023_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_023_capitulation_signal},
    "gcf_024_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_024_capitulation_signal},
    "gcf_025_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_025_capitulation_signal},
    "gcf_026_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_026_capitulation_signal},
    "gcf_027_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_027_capitulation_signal},
    "gcf_028_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_028_capitulation_signal},
    "gcf_029_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_029_capitulation_signal},
    "gcf_030_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_030_capitulation_signal},
    "gcf_031_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_031_capitulation_signal},
    "gcf_032_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_032_capitulation_signal},
    "gcf_033_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_033_capitulation_signal},
    "gcf_034_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_034_capitulation_signal},
    "gcf_035_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_035_capitulation_signal},
    "gcf_036_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_036_capitulation_signal},
    "gcf_037_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_037_capitulation_signal},
    "gcf_038_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_038_capitulation_signal},
    "gcf_039_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_039_capitulation_signal},
    "gcf_040_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_040_capitulation_signal},
    "gcf_041_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_041_capitulation_signal},
    "gcf_042_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_042_capitulation_signal},
    "gcf_043_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_043_capitulation_signal},
    "gcf_044_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_044_capitulation_signal},
    "gcf_045_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_045_capitulation_signal},
    "gcf_046_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_046_capitulation_signal},
    "gcf_047_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_047_capitulation_signal},
    "gcf_048_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_048_capitulation_signal},
    "gcf_049_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_049_capitulation_signal},
    "gcf_050_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_050_capitulation_signal},
    "gcf_051_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_051_capitulation_signal},
    "gcf_052_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_052_capitulation_signal},
    "gcf_053_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_053_capitulation_signal},
    "gcf_054_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_054_capitulation_signal},
    "gcf_055_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_055_capitulation_signal},
    "gcf_056_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_056_capitulation_signal},
    "gcf_057_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_057_capitulation_signal},
    "gcf_058_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_058_capitulation_signal},
    "gcf_059_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_059_capitulation_signal},
    "gcf_060_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_060_capitulation_signal},
    "gcf_061_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_061_capitulation_signal},
    "gcf_062_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_062_capitulation_signal},
    "gcf_063_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_063_capitulation_signal},
    "gcf_064_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_064_capitulation_signal},
    "gcf_065_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_065_capitulation_signal},
    "gcf_066_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_066_capitulation_signal},
    "gcf_067_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_067_capitulation_signal},
    "gcf_068_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_068_capitulation_signal},
    "gcf_069_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_069_capitulation_signal},
    "gcf_070_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_070_capitulation_signal},
    "gcf_071_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_071_capitulation_signal},
    "gcf_072_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_072_capitulation_signal},
    "gcf_073_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_073_capitulation_signal},
    "gcf_074_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_074_capitulation_signal},
    "gcf_075_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": gcf_075_capitulation_signal},
}
