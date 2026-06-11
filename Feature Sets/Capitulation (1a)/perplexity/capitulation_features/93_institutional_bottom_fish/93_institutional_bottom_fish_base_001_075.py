"""Generated capitulation features for 93_institutional_bottom_fish: institutional bottom fishing.
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

def ibf_001_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _z(x, 63)

def ibf_002_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x, y)

def ibf_003_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x - y, y.abs())

def ibf_004_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _rank(x, 504)

def ibf_005_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def ibf_006_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def ibf_007_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x, _s(close))

def ibf_008_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def ibf_009_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def ibf_010_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def ibf_011_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def ibf_012_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ibf_013_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def ibf_014_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _s(x).pct_change(126)

def ibf_015_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _z(x, 252)

def ibf_016_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(x, y)

def ibf_017_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x - y, y.abs())

def ibf_018_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _rank(x, 21)

def ibf_019_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def ibf_020_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def ibf_021_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(x, _s(close))

def ibf_022_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def ibf_023_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def ibf_024_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def ibf_025_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def ibf_026_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ibf_027_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def ibf_028_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _s(x).pct_change(504)

def ibf_029_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _z(x, 756)

def ibf_030_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(x, y)

def ibf_031_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(x - y, y.abs())

def ibf_032_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _rank(x, 126)

def ibf_033_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def ibf_034_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def ibf_035_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(x, _s(close))

def ibf_036_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def ibf_037_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def ibf_038_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def ibf_039_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def ibf_040_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ibf_041_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def ibf_042_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _s(x).pct_change(21)

def ibf_043_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _z(x, 63)

def ibf_044_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(x, y)

def ibf_045_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(x - y, y.abs())

def ibf_046_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _rank(x, 504)

def ibf_047_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def ibf_048_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def ibf_049_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(x, _s(close))

def ibf_050_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def ibf_051_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def ibf_052_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def ibf_053_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def ibf_054_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ibf_055_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def ibf_056_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).pct_change(126)

def ibf_057_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _z(x, 252)

def ibf_058_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x, y)

def ibf_059_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(x - y, y.abs())

def ibf_060_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _rank(x, 21)

def ibf_061_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def ibf_062_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def ibf_063_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x, _s(close))

def ibf_064_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def ibf_065_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def ibf_066_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def ibf_067_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def ibf_068_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ibf_069_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def ibf_070_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).pct_change(504)

def ibf_071_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _z(x, 756)

def ibf_072_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x, y)

def ibf_073_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x - y, y.abs())

def ibf_074_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _rank(x, 126)

def ibf_075_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

INSTITUTIONAL_BOTTOM_FISH_REGISTRY_001_075 = {
    "ibf_001_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_001_capitulation_signal},
    "ibf_002_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_002_capitulation_signal},
    "ibf_003_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_003_capitulation_signal},
    "ibf_004_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_004_capitulation_signal},
    "ibf_005_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_005_capitulation_signal},
    "ibf_006_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_006_capitulation_signal},
    "ibf_007_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_007_capitulation_signal},
    "ibf_008_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_008_capitulation_signal},
    "ibf_009_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_009_capitulation_signal},
    "ibf_010_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_010_capitulation_signal},
    "ibf_011_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_011_capitulation_signal},
    "ibf_012_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_012_capitulation_signal},
    "ibf_013_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_013_capitulation_signal},
    "ibf_014_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_014_capitulation_signal},
    "ibf_015_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_015_capitulation_signal},
    "ibf_016_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_016_capitulation_signal},
    "ibf_017_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_017_capitulation_signal},
    "ibf_018_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_018_capitulation_signal},
    "ibf_019_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_019_capitulation_signal},
    "ibf_020_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_020_capitulation_signal},
    "ibf_021_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_021_capitulation_signal},
    "ibf_022_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_022_capitulation_signal},
    "ibf_023_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_023_capitulation_signal},
    "ibf_024_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_024_capitulation_signal},
    "ibf_025_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_025_capitulation_signal},
    "ibf_026_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_026_capitulation_signal},
    "ibf_027_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_027_capitulation_signal},
    "ibf_028_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_028_capitulation_signal},
    "ibf_029_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_029_capitulation_signal},
    "ibf_030_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_030_capitulation_signal},
    "ibf_031_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_031_capitulation_signal},
    "ibf_032_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_032_capitulation_signal},
    "ibf_033_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_033_capitulation_signal},
    "ibf_034_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_034_capitulation_signal},
    "ibf_035_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_035_capitulation_signal},
    "ibf_036_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_036_capitulation_signal},
    "ibf_037_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_037_capitulation_signal},
    "ibf_038_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_038_capitulation_signal},
    "ibf_039_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_039_capitulation_signal},
    "ibf_040_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_040_capitulation_signal},
    "ibf_041_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_041_capitulation_signal},
    "ibf_042_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_042_capitulation_signal},
    "ibf_043_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_043_capitulation_signal},
    "ibf_044_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_044_capitulation_signal},
    "ibf_045_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_045_capitulation_signal},
    "ibf_046_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_046_capitulation_signal},
    "ibf_047_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_047_capitulation_signal},
    "ibf_048_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_048_capitulation_signal},
    "ibf_049_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_049_capitulation_signal},
    "ibf_050_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_050_capitulation_signal},
    "ibf_051_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_051_capitulation_signal},
    "ibf_052_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_052_capitulation_signal},
    "ibf_053_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_053_capitulation_signal},
    "ibf_054_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_054_capitulation_signal},
    "ibf_055_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_055_capitulation_signal},
    "ibf_056_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_056_capitulation_signal},
    "ibf_057_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_057_capitulation_signal},
    "ibf_058_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_058_capitulation_signal},
    "ibf_059_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_059_capitulation_signal},
    "ibf_060_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_060_capitulation_signal},
    "ibf_061_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_061_capitulation_signal},
    "ibf_062_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_062_capitulation_signal},
    "ibf_063_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_063_capitulation_signal},
    "ibf_064_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_064_capitulation_signal},
    "ibf_065_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_065_capitulation_signal},
    "ibf_066_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_066_capitulation_signal},
    "ibf_067_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_067_capitulation_signal},
    "ibf_068_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_068_capitulation_signal},
    "ibf_069_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_069_capitulation_signal},
    "ibf_070_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_070_capitulation_signal},
    "ibf_071_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_071_capitulation_signal},
    "ibf_072_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_072_capitulation_signal},
    "ibf_073_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_073_capitulation_signal},
    "ibf_074_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_074_capitulation_signal},
    "ibf_075_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_075_capitulation_signal},
}
