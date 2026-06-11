"""Generated capitulation features for 91_institutional_exit: institutional holder exits.
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

def iex_076_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def iex_077_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x, _s(close))

def iex_078_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def iex_079_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def iex_080_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def iex_081_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def iex_082_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def iex_083_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def iex_084_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _s(x).pct_change(21)

def iex_085_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _z(x, 63)

def iex_086_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(x, y)

def iex_087_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x - y, y.abs())

def iex_088_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _rank(x, 504)

def iex_089_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def iex_090_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def iex_091_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(x, _s(close))

def iex_092_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def iex_093_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def iex_094_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def iex_095_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def iex_096_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def iex_097_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def iex_098_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _s(x).pct_change(126)

def iex_099_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _z(x, 252)

def iex_100_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(x, y)

def iex_101_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(x - y, y.abs())

def iex_102_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _rank(x, 21)

def iex_103_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def iex_104_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def iex_105_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(x, _s(close))

def iex_106_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def iex_107_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def iex_108_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def iex_109_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def iex_110_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def iex_111_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def iex_112_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _s(x).pct_change(504)

def iex_113_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _z(x, 756)

def iex_114_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(x, y)

def iex_115_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(x - y, y.abs())

def iex_116_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _rank(x, 126)

def iex_117_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def iex_118_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def iex_119_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(x, _s(close))

def iex_120_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def iex_121_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def iex_122_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def iex_123_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def iex_124_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def iex_125_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def iex_126_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).pct_change(21)

def iex_127_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _z(x, 63)

def iex_128_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x, y)

def iex_129_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(x - y, y.abs())

def iex_130_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _rank(x, 504)

def iex_131_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def iex_132_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def iex_133_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x, _s(close))

def iex_134_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def iex_135_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def iex_136_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def iex_137_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def iex_138_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def iex_139_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def iex_140_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).pct_change(126)

def iex_141_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _z(x, 252)

def iex_142_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x, y)

def iex_143_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x - y, y.abs())

def iex_144_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _rank(x, 21)

def iex_145_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def iex_146_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def iex_147_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x, _s(close))

def iex_148_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def iex_149_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def iex_150_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

INSTITUTIONAL_EXIT_REGISTRY_076_150 = {
    "iex_076_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_076_capitulation_signal},
    "iex_077_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_077_capitulation_signal},
    "iex_078_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_078_capitulation_signal},
    "iex_079_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_079_capitulation_signal},
    "iex_080_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_080_capitulation_signal},
    "iex_081_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_081_capitulation_signal},
    "iex_082_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_082_capitulation_signal},
    "iex_083_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_083_capitulation_signal},
    "iex_084_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_084_capitulation_signal},
    "iex_085_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_085_capitulation_signal},
    "iex_086_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_086_capitulation_signal},
    "iex_087_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_087_capitulation_signal},
    "iex_088_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_088_capitulation_signal},
    "iex_089_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_089_capitulation_signal},
    "iex_090_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_090_capitulation_signal},
    "iex_091_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_091_capitulation_signal},
    "iex_092_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_092_capitulation_signal},
    "iex_093_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_093_capitulation_signal},
    "iex_094_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_094_capitulation_signal},
    "iex_095_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_095_capitulation_signal},
    "iex_096_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_096_capitulation_signal},
    "iex_097_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_097_capitulation_signal},
    "iex_098_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_098_capitulation_signal},
    "iex_099_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_099_capitulation_signal},
    "iex_100_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_100_capitulation_signal},
    "iex_101_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_101_capitulation_signal},
    "iex_102_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_102_capitulation_signal},
    "iex_103_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_103_capitulation_signal},
    "iex_104_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_104_capitulation_signal},
    "iex_105_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_105_capitulation_signal},
    "iex_106_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_106_capitulation_signal},
    "iex_107_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_107_capitulation_signal},
    "iex_108_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_108_capitulation_signal},
    "iex_109_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_109_capitulation_signal},
    "iex_110_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_110_capitulation_signal},
    "iex_111_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_111_capitulation_signal},
    "iex_112_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_112_capitulation_signal},
    "iex_113_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_113_capitulation_signal},
    "iex_114_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_114_capitulation_signal},
    "iex_115_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_115_capitulation_signal},
    "iex_116_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_116_capitulation_signal},
    "iex_117_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_117_capitulation_signal},
    "iex_118_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_118_capitulation_signal},
    "iex_119_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_119_capitulation_signal},
    "iex_120_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_120_capitulation_signal},
    "iex_121_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_121_capitulation_signal},
    "iex_122_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_122_capitulation_signal},
    "iex_123_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_123_capitulation_signal},
    "iex_124_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_124_capitulation_signal},
    "iex_125_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_125_capitulation_signal},
    "iex_126_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_126_capitulation_signal},
    "iex_127_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_127_capitulation_signal},
    "iex_128_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_128_capitulation_signal},
    "iex_129_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_129_capitulation_signal},
    "iex_130_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_130_capitulation_signal},
    "iex_131_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_131_capitulation_signal},
    "iex_132_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_132_capitulation_signal},
    "iex_133_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_133_capitulation_signal},
    "iex_134_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_134_capitulation_signal},
    "iex_135_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_135_capitulation_signal},
    "iex_136_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_136_capitulation_signal},
    "iex_137_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_137_capitulation_signal},
    "iex_138_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_138_capitulation_signal},
    "iex_139_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_139_capitulation_signal},
    "iex_140_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_140_capitulation_signal},
    "iex_141_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_141_capitulation_signal},
    "iex_142_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_142_capitulation_signal},
    "iex_143_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_143_capitulation_signal},
    "iex_144_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_144_capitulation_signal},
    "iex_145_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_145_capitulation_signal},
    "iex_146_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_146_capitulation_signal},
    "iex_147_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_147_capitulation_signal},
    "iex_148_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_148_capitulation_signal},
    "iex_149_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_149_capitulation_signal},
    "iex_150_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": iex_150_capitulation_signal},
}
