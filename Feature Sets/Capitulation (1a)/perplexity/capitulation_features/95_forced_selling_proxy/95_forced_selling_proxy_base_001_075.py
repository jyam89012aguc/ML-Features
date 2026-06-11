"""Generated capitulation features for 95_forced_selling_proxy: forced selling proxy.
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

def fsp_001_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _z(x, 63)

def fsp_002_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x, y)

def fsp_003_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x - y, y.abs())

def fsp_004_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _rank(x, 504)

def fsp_005_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def fsp_006_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def fsp_007_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x, _s(close))

def fsp_008_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def fsp_009_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def fsp_010_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def fsp_011_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def fsp_012_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def fsp_013_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def fsp_014_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _s(x).pct_change(126)

def fsp_015_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _z(x, 252)

def fsp_016_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(x, y)

def fsp_017_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x - y, y.abs())

def fsp_018_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _rank(x, 21)

def fsp_019_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def fsp_020_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def fsp_021_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(x, _s(close))

def fsp_022_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def fsp_023_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def fsp_024_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def fsp_025_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def fsp_026_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def fsp_027_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def fsp_028_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _s(x).pct_change(504)

def fsp_029_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _z(x, 756)

def fsp_030_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(x, y)

def fsp_031_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(x - y, y.abs())

def fsp_032_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _rank(x, 126)

def fsp_033_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def fsp_034_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def fsp_035_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(x, _s(close))

def fsp_036_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def fsp_037_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def fsp_038_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def fsp_039_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def fsp_040_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def fsp_041_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def fsp_042_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _s(x).pct_change(21)

def fsp_043_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _z(x, 63)

def fsp_044_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(x, y)

def fsp_045_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(x - y, y.abs())

def fsp_046_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _rank(x, 504)

def fsp_047_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def fsp_048_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def fsp_049_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(x, _s(close))

def fsp_050_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def fsp_051_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def fsp_052_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def fsp_053_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def fsp_054_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def fsp_055_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def fsp_056_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).pct_change(126)

def fsp_057_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _z(x, 252)

def fsp_058_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x, y)

def fsp_059_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(x - y, y.abs())

def fsp_060_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _rank(x, 21)

def fsp_061_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def fsp_062_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def fsp_063_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x, _s(close))

def fsp_064_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def fsp_065_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def fsp_066_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def fsp_067_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def fsp_068_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def fsp_069_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def fsp_070_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).pct_change(504)

def fsp_071_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _z(x, 756)

def fsp_072_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x, y)

def fsp_073_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x - y, y.abs())

def fsp_074_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _rank(x, 126)

def fsp_075_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

FORCED_SELLING_PROXY_REGISTRY_001_075 = {
    "fsp_001_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_001_capitulation_signal},
    "fsp_002_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_002_capitulation_signal},
    "fsp_003_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_003_capitulation_signal},
    "fsp_004_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_004_capitulation_signal},
    "fsp_005_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_005_capitulation_signal},
    "fsp_006_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_006_capitulation_signal},
    "fsp_007_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_007_capitulation_signal},
    "fsp_008_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_008_capitulation_signal},
    "fsp_009_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_009_capitulation_signal},
    "fsp_010_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_010_capitulation_signal},
    "fsp_011_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_011_capitulation_signal},
    "fsp_012_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_012_capitulation_signal},
    "fsp_013_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_013_capitulation_signal},
    "fsp_014_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_014_capitulation_signal},
    "fsp_015_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_015_capitulation_signal},
    "fsp_016_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_016_capitulation_signal},
    "fsp_017_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_017_capitulation_signal},
    "fsp_018_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_018_capitulation_signal},
    "fsp_019_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_019_capitulation_signal},
    "fsp_020_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_020_capitulation_signal},
    "fsp_021_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_021_capitulation_signal},
    "fsp_022_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_022_capitulation_signal},
    "fsp_023_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_023_capitulation_signal},
    "fsp_024_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_024_capitulation_signal},
    "fsp_025_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_025_capitulation_signal},
    "fsp_026_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_026_capitulation_signal},
    "fsp_027_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_027_capitulation_signal},
    "fsp_028_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_028_capitulation_signal},
    "fsp_029_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_029_capitulation_signal},
    "fsp_030_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_030_capitulation_signal},
    "fsp_031_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_031_capitulation_signal},
    "fsp_032_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_032_capitulation_signal},
    "fsp_033_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_033_capitulation_signal},
    "fsp_034_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_034_capitulation_signal},
    "fsp_035_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_035_capitulation_signal},
    "fsp_036_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_036_capitulation_signal},
    "fsp_037_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_037_capitulation_signal},
    "fsp_038_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_038_capitulation_signal},
    "fsp_039_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_039_capitulation_signal},
    "fsp_040_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_040_capitulation_signal},
    "fsp_041_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_041_capitulation_signal},
    "fsp_042_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_042_capitulation_signal},
    "fsp_043_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_043_capitulation_signal},
    "fsp_044_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_044_capitulation_signal},
    "fsp_045_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_045_capitulation_signal},
    "fsp_046_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_046_capitulation_signal},
    "fsp_047_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_047_capitulation_signal},
    "fsp_048_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_048_capitulation_signal},
    "fsp_049_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_049_capitulation_signal},
    "fsp_050_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_050_capitulation_signal},
    "fsp_051_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_051_capitulation_signal},
    "fsp_052_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_052_capitulation_signal},
    "fsp_053_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_053_capitulation_signal},
    "fsp_054_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_054_capitulation_signal},
    "fsp_055_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_055_capitulation_signal},
    "fsp_056_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_056_capitulation_signal},
    "fsp_057_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_057_capitulation_signal},
    "fsp_058_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_058_capitulation_signal},
    "fsp_059_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_059_capitulation_signal},
    "fsp_060_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_060_capitulation_signal},
    "fsp_061_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_061_capitulation_signal},
    "fsp_062_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_062_capitulation_signal},
    "fsp_063_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_063_capitulation_signal},
    "fsp_064_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_064_capitulation_signal},
    "fsp_065_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_065_capitulation_signal},
    "fsp_066_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_066_capitulation_signal},
    "fsp_067_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_067_capitulation_signal},
    "fsp_068_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_068_capitulation_signal},
    "fsp_069_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_069_capitulation_signal},
    "fsp_070_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_070_capitulation_signal},
    "fsp_071_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_071_capitulation_signal},
    "fsp_072_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_072_capitulation_signal},
    "fsp_073_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_073_capitulation_signal},
    "fsp_074_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_074_capitulation_signal},
    "fsp_075_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": fsp_075_capitulation_signal},
}
