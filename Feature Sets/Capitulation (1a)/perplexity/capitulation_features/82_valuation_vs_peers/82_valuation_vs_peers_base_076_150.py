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

def vvp_076_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def vvp_077_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _div(x, _s(close))

def vvp_078_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def vvp_079_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def vvp_080_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def vvp_081_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def vvp_082_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vvp_083_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def vvp_084_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _s(x).pct_change(21)

def vvp_085_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _z(x, 63)

def vvp_086_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _div(x, y)

def vvp_087_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _div(x - y, y.abs())

def vvp_088_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _rank(x, 504)

def vvp_089_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def vvp_090_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def vvp_091_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _div(x, _s(close))

def vvp_092_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def vvp_093_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def vvp_094_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def vvp_095_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def vvp_096_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vvp_097_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def vvp_098_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _s(x).pct_change(126)

def vvp_099_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _z(x, 252)

def vvp_100_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _div(x, y)

def vvp_101_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _div(x - y, y.abs())

def vvp_102_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _rank(x, 21)

def vvp_103_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def vvp_104_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def vvp_105_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _div(x, _s(close))

def vvp_106_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def vvp_107_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def vvp_108_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def vvp_109_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def vvp_110_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vvp_111_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def vvp_112_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _s(x).pct_change(504)

def vvp_113_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _z(x, 756)

def vvp_114_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _div(x, y)

def vvp_115_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _div(x - y, y.abs())

def vvp_116_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _rank(x, 126)

def vvp_117_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def vvp_118_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def vvp_119_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _div(x, _s(close))

def vvp_120_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def vvp_121_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def vvp_122_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def vvp_123_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def vvp_124_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vvp_125_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def vvp_126_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _s(x).pct_change(21)

def vvp_127_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _z(x, 63)

def vvp_128_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _div(x, y)

def vvp_129_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _div(x - y, y.abs())

def vvp_130_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _rank(x, 504)

def vvp_131_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def vvp_132_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def vvp_133_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _div(x, _s(close))

def vvp_134_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def vvp_135_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def vvp_136_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def vvp_137_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def vvp_138_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vvp_139_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def vvp_140_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _s(x).pct_change(126)

def vvp_141_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return _z(x, 252)

def vvp_142_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _div(x, y)

def vvp_143_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _div(x - y, y.abs())

def vvp_144_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _rank(x, 21)

def vvp_145_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def vvp_146_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def vvp_147_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(evsales, close)
    y = _align_to_close(peer_median_evsales, close)
    return _div(x, _s(close))

def vvp_148_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pe, close)
    y = _align_to_close(peer_median_pe, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def vvp_149_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(pb, close)
    y = _align_to_close(peer_median_pb, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def vvp_150_capitulation_signal(close, pe, pb, ps, evsales, peer_median_pe, peer_median_pb, peer_median_ps, peer_median_evsales):
    x = _align_to_close(ps, close)
    y = _align_to_close(peer_median_ps, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

VALUATION_VS_PEERS_REGISTRY_076_150 = {
    "vvp_076_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_076_capitulation_signal},
    "vvp_077_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_077_capitulation_signal},
    "vvp_078_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_078_capitulation_signal},
    "vvp_079_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_079_capitulation_signal},
    "vvp_080_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_080_capitulation_signal},
    "vvp_081_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_081_capitulation_signal},
    "vvp_082_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_082_capitulation_signal},
    "vvp_083_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_083_capitulation_signal},
    "vvp_084_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_084_capitulation_signal},
    "vvp_085_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_085_capitulation_signal},
    "vvp_086_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_086_capitulation_signal},
    "vvp_087_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_087_capitulation_signal},
    "vvp_088_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_088_capitulation_signal},
    "vvp_089_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_089_capitulation_signal},
    "vvp_090_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_090_capitulation_signal},
    "vvp_091_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_091_capitulation_signal},
    "vvp_092_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_092_capitulation_signal},
    "vvp_093_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_093_capitulation_signal},
    "vvp_094_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_094_capitulation_signal},
    "vvp_095_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_095_capitulation_signal},
    "vvp_096_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_096_capitulation_signal},
    "vvp_097_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_097_capitulation_signal},
    "vvp_098_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_098_capitulation_signal},
    "vvp_099_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_099_capitulation_signal},
    "vvp_100_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_100_capitulation_signal},
    "vvp_101_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_101_capitulation_signal},
    "vvp_102_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_102_capitulation_signal},
    "vvp_103_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_103_capitulation_signal},
    "vvp_104_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_104_capitulation_signal},
    "vvp_105_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_105_capitulation_signal},
    "vvp_106_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_106_capitulation_signal},
    "vvp_107_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_107_capitulation_signal},
    "vvp_108_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_108_capitulation_signal},
    "vvp_109_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_109_capitulation_signal},
    "vvp_110_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_110_capitulation_signal},
    "vvp_111_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_111_capitulation_signal},
    "vvp_112_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_112_capitulation_signal},
    "vvp_113_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_113_capitulation_signal},
    "vvp_114_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_114_capitulation_signal},
    "vvp_115_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_115_capitulation_signal},
    "vvp_116_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_116_capitulation_signal},
    "vvp_117_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_117_capitulation_signal},
    "vvp_118_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_118_capitulation_signal},
    "vvp_119_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_119_capitulation_signal},
    "vvp_120_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_120_capitulation_signal},
    "vvp_121_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_121_capitulation_signal},
    "vvp_122_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_122_capitulation_signal},
    "vvp_123_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_123_capitulation_signal},
    "vvp_124_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_124_capitulation_signal},
    "vvp_125_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_125_capitulation_signal},
    "vvp_126_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_126_capitulation_signal},
    "vvp_127_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_127_capitulation_signal},
    "vvp_128_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_128_capitulation_signal},
    "vvp_129_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_129_capitulation_signal},
    "vvp_130_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_130_capitulation_signal},
    "vvp_131_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_131_capitulation_signal},
    "vvp_132_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_132_capitulation_signal},
    "vvp_133_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_133_capitulation_signal},
    "vvp_134_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_134_capitulation_signal},
    "vvp_135_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_135_capitulation_signal},
    "vvp_136_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_136_capitulation_signal},
    "vvp_137_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_137_capitulation_signal},
    "vvp_138_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_138_capitulation_signal},
    "vvp_139_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_139_capitulation_signal},
    "vvp_140_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_140_capitulation_signal},
    "vvp_141_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_141_capitulation_signal},
    "vvp_142_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_142_capitulation_signal},
    "vvp_143_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_143_capitulation_signal},
    "vvp_144_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_144_capitulation_signal},
    "vvp_145_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_145_capitulation_signal},
    "vvp_146_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_146_capitulation_signal},
    "vvp_147_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_147_capitulation_signal},
    "vvp_148_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_148_capitulation_signal},
    "vvp_149_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_149_capitulation_signal},
    "vvp_150_capitulation_signal": {"inputs": ['close', 'pe', 'pb', 'ps', 'evsales', 'peer_median_pe', 'peer_median_pb', 'peer_median_ps', 'peer_median_evsales'], "func": vvp_150_capitulation_signal},
}
