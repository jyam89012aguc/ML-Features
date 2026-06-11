"""Generated capitulation features for 94_holder_count_dynamics: holder breadth vs peers.
All windows look backward only. Trading-day constants: 252/year, 63/quarter, 21/month, 5/week.
"""
import numpy as np
import pandas as pd


def _align_to_close(s, close):
    s = pd.Series(s).copy()
    close = pd.Series(close)
    return s.reindex(close.index).ffill()

def _peer_contract_note():
    return "peer_median_* inputs must be precomputed on the same daily index, then forward-filled/reindexed to close."

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

def hcd_001_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _z(x, 63)

def hcd_002_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _div(x, y)

def hcd_003_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _div(x - y, y.abs())

def hcd_004_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _rank(x, 504)

def hcd_005_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def hcd_006_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def hcd_007_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _div(x, _s(close))

def hcd_008_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def hcd_009_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def hcd_010_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def hcd_011_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def hcd_012_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def hcd_013_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def hcd_014_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _s(x).pct_change(126)

def hcd_015_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _z(x, 252)

def hcd_016_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _div(x, y)

def hcd_017_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _div(x - y, y.abs())

def hcd_018_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _rank(x, 21)

def hcd_019_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def hcd_020_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def hcd_021_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _div(x, _s(close))

def hcd_022_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def hcd_023_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def hcd_024_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def hcd_025_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def hcd_026_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def hcd_027_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def hcd_028_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _s(x).pct_change(504)

def hcd_029_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _z(x, 756)

def hcd_030_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _div(x, y)

def hcd_031_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _div(x - y, y.abs())

def hcd_032_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _rank(x, 126)

def hcd_033_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def hcd_034_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def hcd_035_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _div(x, _s(close))

def hcd_036_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def hcd_037_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def hcd_038_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def hcd_039_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def hcd_040_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def hcd_041_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def hcd_042_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _s(x).pct_change(21)

def hcd_043_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _z(x, 63)

def hcd_044_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _div(x, y)

def hcd_045_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _div(x - y, y.abs())

def hcd_046_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _rank(x, 504)

def hcd_047_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def hcd_048_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def hcd_049_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _div(x, _s(close))

def hcd_050_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def hcd_051_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def hcd_052_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def hcd_053_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def hcd_054_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def hcd_055_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def hcd_056_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _s(x).pct_change(126)

def hcd_057_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _z(x, 252)

def hcd_058_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _div(x, y)

def hcd_059_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _div(x - y, y.abs())

def hcd_060_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _rank(x, 21)

def hcd_061_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def hcd_062_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def hcd_063_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _div(x, _s(close))

def hcd_064_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def hcd_065_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def hcd_066_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def hcd_067_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def hcd_068_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def hcd_069_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def hcd_070_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _s(x).pct_change(504)

def hcd_071_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _z(x, 756)

def hcd_072_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _div(x, y)

def hcd_073_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _div(x - y, y.abs())

def hcd_074_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _rank(x, 126)

def hcd_075_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

HOLDER_COUNT_DYNAMICS_REGISTRY_001_075 = {
    "hcd_001_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_001_capitulation_signal},
    "hcd_002_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_002_capitulation_signal},
    "hcd_003_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_003_capitulation_signal},
    "hcd_004_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_004_capitulation_signal},
    "hcd_005_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_005_capitulation_signal},
    "hcd_006_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_006_capitulation_signal},
    "hcd_007_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_007_capitulation_signal},
    "hcd_008_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_008_capitulation_signal},
    "hcd_009_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_009_capitulation_signal},
    "hcd_010_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_010_capitulation_signal},
    "hcd_011_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_011_capitulation_signal},
    "hcd_012_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_012_capitulation_signal},
    "hcd_013_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_013_capitulation_signal},
    "hcd_014_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_014_capitulation_signal},
    "hcd_015_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_015_capitulation_signal},
    "hcd_016_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_016_capitulation_signal},
    "hcd_017_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_017_capitulation_signal},
    "hcd_018_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_018_capitulation_signal},
    "hcd_019_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_019_capitulation_signal},
    "hcd_020_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_020_capitulation_signal},
    "hcd_021_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_021_capitulation_signal},
    "hcd_022_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_022_capitulation_signal},
    "hcd_023_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_023_capitulation_signal},
    "hcd_024_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_024_capitulation_signal},
    "hcd_025_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_025_capitulation_signal},
    "hcd_026_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_026_capitulation_signal},
    "hcd_027_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_027_capitulation_signal},
    "hcd_028_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_028_capitulation_signal},
    "hcd_029_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_029_capitulation_signal},
    "hcd_030_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_030_capitulation_signal},
    "hcd_031_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_031_capitulation_signal},
    "hcd_032_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_032_capitulation_signal},
    "hcd_033_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_033_capitulation_signal},
    "hcd_034_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_034_capitulation_signal},
    "hcd_035_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_035_capitulation_signal},
    "hcd_036_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_036_capitulation_signal},
    "hcd_037_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_037_capitulation_signal},
    "hcd_038_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_038_capitulation_signal},
    "hcd_039_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_039_capitulation_signal},
    "hcd_040_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_040_capitulation_signal},
    "hcd_041_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_041_capitulation_signal},
    "hcd_042_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_042_capitulation_signal},
    "hcd_043_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_043_capitulation_signal},
    "hcd_044_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_044_capitulation_signal},
    "hcd_045_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_045_capitulation_signal},
    "hcd_046_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_046_capitulation_signal},
    "hcd_047_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_047_capitulation_signal},
    "hcd_048_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_048_capitulation_signal},
    "hcd_049_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_049_capitulation_signal},
    "hcd_050_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_050_capitulation_signal},
    "hcd_051_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_051_capitulation_signal},
    "hcd_052_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_052_capitulation_signal},
    "hcd_053_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_053_capitulation_signal},
    "hcd_054_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_054_capitulation_signal},
    "hcd_055_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_055_capitulation_signal},
    "hcd_056_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_056_capitulation_signal},
    "hcd_057_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_057_capitulation_signal},
    "hcd_058_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_058_capitulation_signal},
    "hcd_059_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_059_capitulation_signal},
    "hcd_060_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_060_capitulation_signal},
    "hcd_061_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_061_capitulation_signal},
    "hcd_062_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_062_capitulation_signal},
    "hcd_063_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_063_capitulation_signal},
    "hcd_064_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_064_capitulation_signal},
    "hcd_065_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_065_capitulation_signal},
    "hcd_066_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_066_capitulation_signal},
    "hcd_067_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_067_capitulation_signal},
    "hcd_068_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_068_capitulation_signal},
    "hcd_069_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_069_capitulation_signal},
    "hcd_070_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_070_capitulation_signal},
    "hcd_071_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_071_capitulation_signal},
    "hcd_072_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_072_capitulation_signal},
    "hcd_073_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_073_capitulation_signal},
    "hcd_074_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_074_capitulation_signal},
    "hcd_075_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_075_capitulation_signal},
}
