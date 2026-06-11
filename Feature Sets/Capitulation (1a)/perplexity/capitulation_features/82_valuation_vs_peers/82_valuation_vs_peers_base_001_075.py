"""Generated capitulation features for 82_valuation_vs_peers: multiples vs peer medians.
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

def vvp_001_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _z(x, 63)

def vvp_002_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _div(x, y)

def vvp_003_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _div(x - y, y.abs())

def vvp_004_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _rank(x, 504)

def vvp_005_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def vvp_006_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def vvp_007_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _div(x, _s(close))

def vvp_008_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def vvp_009_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def vvp_010_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def vvp_011_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def vvp_012_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vvp_013_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def vvp_014_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _s(x).pct_change(126)

def vvp_015_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _z(x, 252)

def vvp_016_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _div(x, y)

def vvp_017_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _div(x - y, y.abs())

def vvp_018_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _rank(x, 21)

def vvp_019_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def vvp_020_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def vvp_021_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _div(x, _s(close))

def vvp_022_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def vvp_023_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def vvp_024_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def vvp_025_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def vvp_026_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vvp_027_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def vvp_028_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _s(x).pct_change(504)

def vvp_029_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _z(x, 756)

def vvp_030_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _div(x, y)

def vvp_031_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _div(x - y, y.abs())

def vvp_032_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _rank(x, 126)

def vvp_033_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def vvp_034_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def vvp_035_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _div(x, _s(close))

def vvp_036_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def vvp_037_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def vvp_038_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def vvp_039_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def vvp_040_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vvp_041_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def vvp_042_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _s(x).pct_change(21)

def vvp_043_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _z(x, 63)

def vvp_044_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _div(x, y)

def vvp_045_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _div(x - y, y.abs())

def vvp_046_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _rank(x, 504)

def vvp_047_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def vvp_048_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def vvp_049_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _div(x, _s(close))

def vvp_050_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def vvp_051_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def vvp_052_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def vvp_053_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def vvp_054_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vvp_055_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def vvp_056_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _s(x).pct_change(126)

def vvp_057_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _z(x, 252)

def vvp_058_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _div(x, y)

def vvp_059_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _div(x - y, y.abs())

def vvp_060_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _rank(x, 21)

def vvp_061_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def vvp_062_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def vvp_063_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _div(x, _s(close))

def vvp_064_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def vvp_065_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def vvp_066_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def vvp_067_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def vvp_068_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vvp_069_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def vvp_070_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _s(x).pct_change(504)

def vvp_071_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _z(x, 756)

def vvp_072_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _div(x, y)

def vvp_073_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _div(x - y, y.abs())

def vvp_074_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _rank(x, 126)

def vvp_075_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

VALUATION_VS_PEERS_REGISTRY_001_075 = {
    "vvp_001_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_001_capitulation_signal},
    "vvp_002_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_002_capitulation_signal},
    "vvp_003_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_003_capitulation_signal},
    "vvp_004_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_004_capitulation_signal},
    "vvp_005_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_005_capitulation_signal},
    "vvp_006_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_006_capitulation_signal},
    "vvp_007_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_007_capitulation_signal},
    "vvp_008_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_008_capitulation_signal},
    "vvp_009_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_009_capitulation_signal},
    "vvp_010_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_010_capitulation_signal},
    "vvp_011_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_011_capitulation_signal},
    "vvp_012_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_012_capitulation_signal},
    "vvp_013_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_013_capitulation_signal},
    "vvp_014_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_014_capitulation_signal},
    "vvp_015_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_015_capitulation_signal},
    "vvp_016_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_016_capitulation_signal},
    "vvp_017_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_017_capitulation_signal},
    "vvp_018_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_018_capitulation_signal},
    "vvp_019_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_019_capitulation_signal},
    "vvp_020_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_020_capitulation_signal},
    "vvp_021_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_021_capitulation_signal},
    "vvp_022_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_022_capitulation_signal},
    "vvp_023_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_023_capitulation_signal},
    "vvp_024_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_024_capitulation_signal},
    "vvp_025_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_025_capitulation_signal},
    "vvp_026_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_026_capitulation_signal},
    "vvp_027_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_027_capitulation_signal},
    "vvp_028_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_028_capitulation_signal},
    "vvp_029_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_029_capitulation_signal},
    "vvp_030_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_030_capitulation_signal},
    "vvp_031_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_031_capitulation_signal},
    "vvp_032_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_032_capitulation_signal},
    "vvp_033_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_033_capitulation_signal},
    "vvp_034_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_034_capitulation_signal},
    "vvp_035_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_035_capitulation_signal},
    "vvp_036_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_036_capitulation_signal},
    "vvp_037_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_037_capitulation_signal},
    "vvp_038_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_038_capitulation_signal},
    "vvp_039_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_039_capitulation_signal},
    "vvp_040_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_040_capitulation_signal},
    "vvp_041_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_041_capitulation_signal},
    "vvp_042_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_042_capitulation_signal},
    "vvp_043_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_043_capitulation_signal},
    "vvp_044_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_044_capitulation_signal},
    "vvp_045_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_045_capitulation_signal},
    "vvp_046_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_046_capitulation_signal},
    "vvp_047_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_047_capitulation_signal},
    "vvp_048_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_048_capitulation_signal},
    "vvp_049_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_049_capitulation_signal},
    "vvp_050_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_050_capitulation_signal},
    "vvp_051_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_051_capitulation_signal},
    "vvp_052_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_052_capitulation_signal},
    "vvp_053_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_053_capitulation_signal},
    "vvp_054_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_054_capitulation_signal},
    "vvp_055_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_055_capitulation_signal},
    "vvp_056_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_056_capitulation_signal},
    "vvp_057_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_057_capitulation_signal},
    "vvp_058_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_058_capitulation_signal},
    "vvp_059_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_059_capitulation_signal},
    "vvp_060_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_060_capitulation_signal},
    "vvp_061_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_061_capitulation_signal},
    "vvp_062_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_062_capitulation_signal},
    "vvp_063_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_063_capitulation_signal},
    "vvp_064_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_064_capitulation_signal},
    "vvp_065_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_065_capitulation_signal},
    "vvp_066_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_066_capitulation_signal},
    "vvp_067_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_067_capitulation_signal},
    "vvp_068_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_068_capitulation_signal},
    "vvp_069_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_069_capitulation_signal},
    "vvp_070_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_070_capitulation_signal},
    "vvp_071_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_071_capitulation_signal},
    "vvp_072_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_072_capitulation_signal},
    "vvp_073_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_073_capitulation_signal},
    "vvp_074_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_074_capitulation_signal},
    "vvp_075_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_075_capitulation_signal},
}
