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

def hcd_076_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def hcd_077_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _div(x, _s(close))

def hcd_078_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def hcd_079_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def hcd_080_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def hcd_081_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def hcd_082_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def hcd_083_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def hcd_084_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _s(x).pct_change(21)

def hcd_085_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _z(x, 63)

def hcd_086_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _div(x, y)

def hcd_087_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _div(x - y, y.abs())

def hcd_088_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _rank(x, 504)

def hcd_089_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def hcd_090_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def hcd_091_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _div(x, _s(close))

def hcd_092_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def hcd_093_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def hcd_094_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def hcd_095_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def hcd_096_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def hcd_097_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def hcd_098_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _s(x).pct_change(126)

def hcd_099_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _z(x, 252)

def hcd_100_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _div(x, y)

def hcd_101_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _div(x - y, y.abs())

def hcd_102_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _rank(x, 21)

def hcd_103_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def hcd_104_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def hcd_105_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _div(x, _s(close))

def hcd_106_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def hcd_107_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def hcd_108_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def hcd_109_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def hcd_110_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def hcd_111_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def hcd_112_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _s(x).pct_change(504)

def hcd_113_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _z(x, 756)

def hcd_114_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _div(x, y)

def hcd_115_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _div(x - y, y.abs())

def hcd_116_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _rank(x, 126)

def hcd_117_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def hcd_118_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def hcd_119_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _div(x, _s(close))

def hcd_120_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def hcd_121_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def hcd_122_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def hcd_123_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def hcd_124_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def hcd_125_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def hcd_126_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _s(x).pct_change(21)

def hcd_127_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _z(x, 63)

def hcd_128_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _div(x, y)

def hcd_129_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _div(x - y, y.abs())

def hcd_130_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _rank(x, 504)

def hcd_131_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def hcd_132_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def hcd_133_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _div(x, _s(close))

def hcd_134_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def hcd_135_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def hcd_136_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def hcd_137_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def hcd_138_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def hcd_139_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def hcd_140_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _s(x).pct_change(126)

def hcd_141_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _z(x, 252)

def hcd_142_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _div(x, y)

def hcd_143_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _div(x - y, y.abs())

def hcd_144_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _rank(x, 21)

def hcd_145_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def hcd_146_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def hcd_147_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _div(x, _s(close))

def hcd_148_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(peer_median_inst_holders, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def hcd_149_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(peer_median_inst_shares, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def hcd_150_capitulation_signal(close, holder_count, inst_holders, inst_shares, peer_median_holder_count, peer_median_inst_holders, peer_median_inst_shares):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(peer_median_holder_count, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

HOLDER_COUNT_DYNAMICS_REGISTRY_076_150 = {
    "hcd_076_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_076_capitulation_signal},
    "hcd_077_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_077_capitulation_signal},
    "hcd_078_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_078_capitulation_signal},
    "hcd_079_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_079_capitulation_signal},
    "hcd_080_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_080_capitulation_signal},
    "hcd_081_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_081_capitulation_signal},
    "hcd_082_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_082_capitulation_signal},
    "hcd_083_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_083_capitulation_signal},
    "hcd_084_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_084_capitulation_signal},
    "hcd_085_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_085_capitulation_signal},
    "hcd_086_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_086_capitulation_signal},
    "hcd_087_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_087_capitulation_signal},
    "hcd_088_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_088_capitulation_signal},
    "hcd_089_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_089_capitulation_signal},
    "hcd_090_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_090_capitulation_signal},
    "hcd_091_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_091_capitulation_signal},
    "hcd_092_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_092_capitulation_signal},
    "hcd_093_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_093_capitulation_signal},
    "hcd_094_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_094_capitulation_signal},
    "hcd_095_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_095_capitulation_signal},
    "hcd_096_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_096_capitulation_signal},
    "hcd_097_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_097_capitulation_signal},
    "hcd_098_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_098_capitulation_signal},
    "hcd_099_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_099_capitulation_signal},
    "hcd_100_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_100_capitulation_signal},
    "hcd_101_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_101_capitulation_signal},
    "hcd_102_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_102_capitulation_signal},
    "hcd_103_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_103_capitulation_signal},
    "hcd_104_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_104_capitulation_signal},
    "hcd_105_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_105_capitulation_signal},
    "hcd_106_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_106_capitulation_signal},
    "hcd_107_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_107_capitulation_signal},
    "hcd_108_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_108_capitulation_signal},
    "hcd_109_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_109_capitulation_signal},
    "hcd_110_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_110_capitulation_signal},
    "hcd_111_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_111_capitulation_signal},
    "hcd_112_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_112_capitulation_signal},
    "hcd_113_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_113_capitulation_signal},
    "hcd_114_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_114_capitulation_signal},
    "hcd_115_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_115_capitulation_signal},
    "hcd_116_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_116_capitulation_signal},
    "hcd_117_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_117_capitulation_signal},
    "hcd_118_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_118_capitulation_signal},
    "hcd_119_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_119_capitulation_signal},
    "hcd_120_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_120_capitulation_signal},
    "hcd_121_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_121_capitulation_signal},
    "hcd_122_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_122_capitulation_signal},
    "hcd_123_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_123_capitulation_signal},
    "hcd_124_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_124_capitulation_signal},
    "hcd_125_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_125_capitulation_signal},
    "hcd_126_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_126_capitulation_signal},
    "hcd_127_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_127_capitulation_signal},
    "hcd_128_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_128_capitulation_signal},
    "hcd_129_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_129_capitulation_signal},
    "hcd_130_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_130_capitulation_signal},
    "hcd_131_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_131_capitulation_signal},
    "hcd_132_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_132_capitulation_signal},
    "hcd_133_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_133_capitulation_signal},
    "hcd_134_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_134_capitulation_signal},
    "hcd_135_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_135_capitulation_signal},
    "hcd_136_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_136_capitulation_signal},
    "hcd_137_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_137_capitulation_signal},
    "hcd_138_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_138_capitulation_signal},
    "hcd_139_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_139_capitulation_signal},
    "hcd_140_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_140_capitulation_signal},
    "hcd_141_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_141_capitulation_signal},
    "hcd_142_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_142_capitulation_signal},
    "hcd_143_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_143_capitulation_signal},
    "hcd_144_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_144_capitulation_signal},
    "hcd_145_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_145_capitulation_signal},
    "hcd_146_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_146_capitulation_signal},
    "hcd_147_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_147_capitulation_signal},
    "hcd_148_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_148_capitulation_signal},
    "hcd_149_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_149_capitulation_signal},
    "hcd_150_capitulation_signal": {"inputs": ['close', 'holder_count', 'inst_holders', 'inst_shares', 'peer_median_holder_count', 'peer_median_inst_holders', 'peer_median_inst_shares'], "func": hcd_150_capitulation_signal},
}
