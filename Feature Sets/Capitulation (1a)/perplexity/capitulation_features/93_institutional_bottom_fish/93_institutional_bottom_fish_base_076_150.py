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

def ibf_076_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def ibf_077_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x, _s(close))

def ibf_078_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def ibf_079_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def ibf_080_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def ibf_081_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def ibf_082_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ibf_083_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def ibf_084_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _s(x).pct_change(21)

def ibf_085_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _z(x, 63)

def ibf_086_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(x, y)

def ibf_087_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x - y, y.abs())

def ibf_088_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _rank(x, 504)

def ibf_089_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def ibf_090_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def ibf_091_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(x, _s(close))

def ibf_092_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def ibf_093_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def ibf_094_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def ibf_095_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def ibf_096_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ibf_097_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def ibf_098_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _s(x).pct_change(126)

def ibf_099_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _z(x, 252)

def ibf_100_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(x, y)

def ibf_101_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(x - y, y.abs())

def ibf_102_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _rank(x, 21)

def ibf_103_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def ibf_104_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def ibf_105_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(x, _s(close))

def ibf_106_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def ibf_107_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def ibf_108_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def ibf_109_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def ibf_110_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ibf_111_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def ibf_112_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _s(x).pct_change(504)

def ibf_113_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _z(x, 756)

def ibf_114_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(x, y)

def ibf_115_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(x - y, y.abs())

def ibf_116_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _rank(x, 126)

def ibf_117_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def ibf_118_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def ibf_119_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(x, _s(close))

def ibf_120_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def ibf_121_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def ibf_122_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def ibf_123_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def ibf_124_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ibf_125_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def ibf_126_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).pct_change(21)

def ibf_127_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _z(x, 63)

def ibf_128_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x, y)

def ibf_129_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(x - y, y.abs())

def ibf_130_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _rank(x, 504)

def ibf_131_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def ibf_132_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def ibf_133_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x, _s(close))

def ibf_134_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def ibf_135_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def ibf_136_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def ibf_137_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def ibf_138_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ibf_139_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def ibf_140_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).pct_change(126)

def ibf_141_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _z(x, 252)

def ibf_142_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x, y)

def ibf_143_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x - y, y.abs())

def ibf_144_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _rank(x, 21)

def ibf_145_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def ibf_146_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def ibf_147_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x, _s(close))

def ibf_148_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def ibf_149_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def ibf_150_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

INSTITUTIONAL_BOTTOM_FISH_REGISTRY_076_150 = {
    "ibf_076_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_076_capitulation_signal},
    "ibf_077_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_077_capitulation_signal},
    "ibf_078_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_078_capitulation_signal},
    "ibf_079_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_079_capitulation_signal},
    "ibf_080_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_080_capitulation_signal},
    "ibf_081_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_081_capitulation_signal},
    "ibf_082_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_082_capitulation_signal},
    "ibf_083_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_083_capitulation_signal},
    "ibf_084_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_084_capitulation_signal},
    "ibf_085_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_085_capitulation_signal},
    "ibf_086_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_086_capitulation_signal},
    "ibf_087_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_087_capitulation_signal},
    "ibf_088_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_088_capitulation_signal},
    "ibf_089_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_089_capitulation_signal},
    "ibf_090_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_090_capitulation_signal},
    "ibf_091_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_091_capitulation_signal},
    "ibf_092_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_092_capitulation_signal},
    "ibf_093_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_093_capitulation_signal},
    "ibf_094_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_094_capitulation_signal},
    "ibf_095_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_095_capitulation_signal},
    "ibf_096_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_096_capitulation_signal},
    "ibf_097_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_097_capitulation_signal},
    "ibf_098_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_098_capitulation_signal},
    "ibf_099_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_099_capitulation_signal},
    "ibf_100_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_100_capitulation_signal},
    "ibf_101_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_101_capitulation_signal},
    "ibf_102_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_102_capitulation_signal},
    "ibf_103_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_103_capitulation_signal},
    "ibf_104_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_104_capitulation_signal},
    "ibf_105_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_105_capitulation_signal},
    "ibf_106_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_106_capitulation_signal},
    "ibf_107_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_107_capitulation_signal},
    "ibf_108_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_108_capitulation_signal},
    "ibf_109_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_109_capitulation_signal},
    "ibf_110_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_110_capitulation_signal},
    "ibf_111_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_111_capitulation_signal},
    "ibf_112_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_112_capitulation_signal},
    "ibf_113_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_113_capitulation_signal},
    "ibf_114_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_114_capitulation_signal},
    "ibf_115_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_115_capitulation_signal},
    "ibf_116_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_116_capitulation_signal},
    "ibf_117_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_117_capitulation_signal},
    "ibf_118_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_118_capitulation_signal},
    "ibf_119_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_119_capitulation_signal},
    "ibf_120_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_120_capitulation_signal},
    "ibf_121_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_121_capitulation_signal},
    "ibf_122_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_122_capitulation_signal},
    "ibf_123_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_123_capitulation_signal},
    "ibf_124_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_124_capitulation_signal},
    "ibf_125_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_125_capitulation_signal},
    "ibf_126_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_126_capitulation_signal},
    "ibf_127_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_127_capitulation_signal},
    "ibf_128_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_128_capitulation_signal},
    "ibf_129_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_129_capitulation_signal},
    "ibf_130_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_130_capitulation_signal},
    "ibf_131_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_131_capitulation_signal},
    "ibf_132_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_132_capitulation_signal},
    "ibf_133_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_133_capitulation_signal},
    "ibf_134_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_134_capitulation_signal},
    "ibf_135_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_135_capitulation_signal},
    "ibf_136_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_136_capitulation_signal},
    "ibf_137_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_137_capitulation_signal},
    "ibf_138_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_138_capitulation_signal},
    "ibf_139_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_139_capitulation_signal},
    "ibf_140_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_140_capitulation_signal},
    "ibf_141_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_141_capitulation_signal},
    "ibf_142_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_142_capitulation_signal},
    "ibf_143_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_143_capitulation_signal},
    "ibf_144_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_144_capitulation_signal},
    "ibf_145_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_145_capitulation_signal},
    "ibf_146_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_146_capitulation_signal},
    "ibf_147_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_147_capitulation_signal},
    "ibf_148_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_148_capitulation_signal},
    "ibf_149_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_149_capitulation_signal},
    "ibf_150_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ibf_150_capitulation_signal},
}
