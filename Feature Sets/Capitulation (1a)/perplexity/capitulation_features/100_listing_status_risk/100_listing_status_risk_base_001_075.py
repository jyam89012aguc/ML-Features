"""Generated capitulation features for 100_listing_status_risk: listing/delisting risk.
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

def lsr_001_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _z(x, 63)

def lsr_002_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x, y)

def lsr_003_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x - y, y.abs())

def lsr_004_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _rank(x, 504)

def lsr_005_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def lsr_006_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def lsr_007_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x, _s(close))

def lsr_008_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def lsr_009_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def lsr_010_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def lsr_011_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def lsr_012_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lsr_013_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def lsr_014_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _s(x).pct_change(126)

def lsr_015_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _z(x, 252)

def lsr_016_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(x, y)

def lsr_017_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x - y, y.abs())

def lsr_018_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _rank(x, 21)

def lsr_019_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def lsr_020_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def lsr_021_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(x, _s(close))

def lsr_022_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def lsr_023_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def lsr_024_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def lsr_025_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def lsr_026_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lsr_027_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def lsr_028_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _s(x).pct_change(504)

def lsr_029_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _z(x, 756)

def lsr_030_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(x, y)

def lsr_031_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(x - y, y.abs())

def lsr_032_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _rank(x, 126)

def lsr_033_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def lsr_034_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def lsr_035_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(x, _s(close))

def lsr_036_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def lsr_037_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def lsr_038_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def lsr_039_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def lsr_040_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lsr_041_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def lsr_042_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _s(x).pct_change(21)

def lsr_043_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _z(x, 63)

def lsr_044_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(x, y)

def lsr_045_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(x - y, y.abs())

def lsr_046_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _rank(x, 504)

def lsr_047_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def lsr_048_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def lsr_049_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(x, _s(close))

def lsr_050_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def lsr_051_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def lsr_052_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def lsr_053_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def lsr_054_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lsr_055_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def lsr_056_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _s(x).pct_change(126)

def lsr_057_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _z(x, 252)

def lsr_058_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x, y)

def lsr_059_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(x - y, y.abs())

def lsr_060_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _rank(x, 21)

def lsr_061_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def lsr_062_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def lsr_063_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x, _s(close))

def lsr_064_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def lsr_065_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def lsr_066_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def lsr_067_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def lsr_068_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lsr_069_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def lsr_070_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _s(x).pct_change(504)

def lsr_071_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _z(x, 756)

def lsr_072_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x, y)

def lsr_073_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x - y, y.abs())

def lsr_074_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _rank(x, 126)

def lsr_075_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

LISTING_STATUS_RISK_REGISTRY_001_075 = {
    "lsr_001_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_001_capitulation_signal},
    "lsr_002_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_002_capitulation_signal},
    "lsr_003_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_003_capitulation_signal},
    "lsr_004_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_004_capitulation_signal},
    "lsr_005_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_005_capitulation_signal},
    "lsr_006_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_006_capitulation_signal},
    "lsr_007_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_007_capitulation_signal},
    "lsr_008_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_008_capitulation_signal},
    "lsr_009_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_009_capitulation_signal},
    "lsr_010_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_010_capitulation_signal},
    "lsr_011_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_011_capitulation_signal},
    "lsr_012_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_012_capitulation_signal},
    "lsr_013_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_013_capitulation_signal},
    "lsr_014_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_014_capitulation_signal},
    "lsr_015_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_015_capitulation_signal},
    "lsr_016_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_016_capitulation_signal},
    "lsr_017_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_017_capitulation_signal},
    "lsr_018_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_018_capitulation_signal},
    "lsr_019_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_019_capitulation_signal},
    "lsr_020_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_020_capitulation_signal},
    "lsr_021_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_021_capitulation_signal},
    "lsr_022_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_022_capitulation_signal},
    "lsr_023_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_023_capitulation_signal},
    "lsr_024_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_024_capitulation_signal},
    "lsr_025_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_025_capitulation_signal},
    "lsr_026_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_026_capitulation_signal},
    "lsr_027_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_027_capitulation_signal},
    "lsr_028_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_028_capitulation_signal},
    "lsr_029_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_029_capitulation_signal},
    "lsr_030_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_030_capitulation_signal},
    "lsr_031_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_031_capitulation_signal},
    "lsr_032_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_032_capitulation_signal},
    "lsr_033_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_033_capitulation_signal},
    "lsr_034_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_034_capitulation_signal},
    "lsr_035_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_035_capitulation_signal},
    "lsr_036_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_036_capitulation_signal},
    "lsr_037_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_037_capitulation_signal},
    "lsr_038_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_038_capitulation_signal},
    "lsr_039_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_039_capitulation_signal},
    "lsr_040_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_040_capitulation_signal},
    "lsr_041_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_041_capitulation_signal},
    "lsr_042_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_042_capitulation_signal},
    "lsr_043_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_043_capitulation_signal},
    "lsr_044_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_044_capitulation_signal},
    "lsr_045_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_045_capitulation_signal},
    "lsr_046_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_046_capitulation_signal},
    "lsr_047_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_047_capitulation_signal},
    "lsr_048_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_048_capitulation_signal},
    "lsr_049_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_049_capitulation_signal},
    "lsr_050_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_050_capitulation_signal},
    "lsr_051_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_051_capitulation_signal},
    "lsr_052_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_052_capitulation_signal},
    "lsr_053_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_053_capitulation_signal},
    "lsr_054_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_054_capitulation_signal},
    "lsr_055_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_055_capitulation_signal},
    "lsr_056_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_056_capitulation_signal},
    "lsr_057_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_057_capitulation_signal},
    "lsr_058_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_058_capitulation_signal},
    "lsr_059_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_059_capitulation_signal},
    "lsr_060_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_060_capitulation_signal},
    "lsr_061_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_061_capitulation_signal},
    "lsr_062_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_062_capitulation_signal},
    "lsr_063_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_063_capitulation_signal},
    "lsr_064_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_064_capitulation_signal},
    "lsr_065_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_065_capitulation_signal},
    "lsr_066_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_066_capitulation_signal},
    "lsr_067_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_067_capitulation_signal},
    "lsr_068_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_068_capitulation_signal},
    "lsr_069_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_069_capitulation_signal},
    "lsr_070_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_070_capitulation_signal},
    "lsr_071_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_071_capitulation_signal},
    "lsr_072_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_072_capitulation_signal},
    "lsr_073_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_073_capitulation_signal},
    "lsr_074_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_074_capitulation_signal},
    "lsr_075_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": lsr_075_capitulation_signal},
}
