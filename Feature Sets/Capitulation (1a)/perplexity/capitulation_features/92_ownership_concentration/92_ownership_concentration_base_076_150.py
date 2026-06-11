"""Generated capitulation features for 92_ownership_concentration: holder concentration.
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

def ocn_076_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def ocn_077_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x, _s(close))

def ocn_078_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def ocn_079_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def ocn_080_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def ocn_081_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def ocn_082_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ocn_083_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def ocn_084_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _s(x).pct_change(21)

def ocn_085_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _z(x, 63)

def ocn_086_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(x, y)

def ocn_087_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x - y, y.abs())

def ocn_088_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _rank(x, 504)

def ocn_089_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def ocn_090_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def ocn_091_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(x, _s(close))

def ocn_092_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def ocn_093_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def ocn_094_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def ocn_095_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def ocn_096_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ocn_097_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def ocn_098_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _s(x).pct_change(126)

def ocn_099_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _z(x, 252)

def ocn_100_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(x, y)

def ocn_101_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(x - y, y.abs())

def ocn_102_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _rank(x, 21)

def ocn_103_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def ocn_104_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def ocn_105_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(x, _s(close))

def ocn_106_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def ocn_107_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def ocn_108_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def ocn_109_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def ocn_110_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ocn_111_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def ocn_112_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _s(x).pct_change(504)

def ocn_113_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _z(x, 756)

def ocn_114_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(x, y)

def ocn_115_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(x - y, y.abs())

def ocn_116_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _rank(x, 126)

def ocn_117_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def ocn_118_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def ocn_119_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(x, _s(close))

def ocn_120_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def ocn_121_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def ocn_122_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def ocn_123_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def ocn_124_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ocn_125_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def ocn_126_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).pct_change(21)

def ocn_127_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _z(x, 63)

def ocn_128_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x, y)

def ocn_129_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(x - y, y.abs())

def ocn_130_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _rank(x, 504)

def ocn_131_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def ocn_132_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def ocn_133_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x, _s(close))

def ocn_134_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def ocn_135_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def ocn_136_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def ocn_137_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def ocn_138_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ocn_139_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def ocn_140_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).pct_change(126)

def ocn_141_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _z(x, 252)

def ocn_142_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x, y)

def ocn_143_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x - y, y.abs())

def ocn_144_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return _rank(x, 21)

def ocn_145_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def ocn_146_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_shares, close)
    y = _align_to_close(inst_value, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def ocn_147_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_value, close)
    y = _align_to_close(top_holder_share, close)
    return _div(x, _s(close))

def ocn_148_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(top_holder_share, close)
    y = _align_to_close(holder_count, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def ocn_149_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(holder_count, close)
    y = _align_to_close(inst_holders, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def ocn_150_capitulation_signal(close, inst_holders, inst_shares, inst_value, top_holder_share, holder_count):
    x = _align_to_close(inst_holders, close)
    y = _align_to_close(inst_shares, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

OWNERSHIP_CONCENTRATION_REGISTRY_076_150 = {
    "ocn_076_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_076_capitulation_signal},
    "ocn_077_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_077_capitulation_signal},
    "ocn_078_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_078_capitulation_signal},
    "ocn_079_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_079_capitulation_signal},
    "ocn_080_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_080_capitulation_signal},
    "ocn_081_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_081_capitulation_signal},
    "ocn_082_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_082_capitulation_signal},
    "ocn_083_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_083_capitulation_signal},
    "ocn_084_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_084_capitulation_signal},
    "ocn_085_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_085_capitulation_signal},
    "ocn_086_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_086_capitulation_signal},
    "ocn_087_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_087_capitulation_signal},
    "ocn_088_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_088_capitulation_signal},
    "ocn_089_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_089_capitulation_signal},
    "ocn_090_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_090_capitulation_signal},
    "ocn_091_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_091_capitulation_signal},
    "ocn_092_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_092_capitulation_signal},
    "ocn_093_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_093_capitulation_signal},
    "ocn_094_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_094_capitulation_signal},
    "ocn_095_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_095_capitulation_signal},
    "ocn_096_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_096_capitulation_signal},
    "ocn_097_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_097_capitulation_signal},
    "ocn_098_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_098_capitulation_signal},
    "ocn_099_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_099_capitulation_signal},
    "ocn_100_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_100_capitulation_signal},
    "ocn_101_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_101_capitulation_signal},
    "ocn_102_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_102_capitulation_signal},
    "ocn_103_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_103_capitulation_signal},
    "ocn_104_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_104_capitulation_signal},
    "ocn_105_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_105_capitulation_signal},
    "ocn_106_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_106_capitulation_signal},
    "ocn_107_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_107_capitulation_signal},
    "ocn_108_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_108_capitulation_signal},
    "ocn_109_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_109_capitulation_signal},
    "ocn_110_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_110_capitulation_signal},
    "ocn_111_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_111_capitulation_signal},
    "ocn_112_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_112_capitulation_signal},
    "ocn_113_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_113_capitulation_signal},
    "ocn_114_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_114_capitulation_signal},
    "ocn_115_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_115_capitulation_signal},
    "ocn_116_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_116_capitulation_signal},
    "ocn_117_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_117_capitulation_signal},
    "ocn_118_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_118_capitulation_signal},
    "ocn_119_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_119_capitulation_signal},
    "ocn_120_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_120_capitulation_signal},
    "ocn_121_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_121_capitulation_signal},
    "ocn_122_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_122_capitulation_signal},
    "ocn_123_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_123_capitulation_signal},
    "ocn_124_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_124_capitulation_signal},
    "ocn_125_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_125_capitulation_signal},
    "ocn_126_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_126_capitulation_signal},
    "ocn_127_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_127_capitulation_signal},
    "ocn_128_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_128_capitulation_signal},
    "ocn_129_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_129_capitulation_signal},
    "ocn_130_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_130_capitulation_signal},
    "ocn_131_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_131_capitulation_signal},
    "ocn_132_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_132_capitulation_signal},
    "ocn_133_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_133_capitulation_signal},
    "ocn_134_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_134_capitulation_signal},
    "ocn_135_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_135_capitulation_signal},
    "ocn_136_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_136_capitulation_signal},
    "ocn_137_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_137_capitulation_signal},
    "ocn_138_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_138_capitulation_signal},
    "ocn_139_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_139_capitulation_signal},
    "ocn_140_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_140_capitulation_signal},
    "ocn_141_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_141_capitulation_signal},
    "ocn_142_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_142_capitulation_signal},
    "ocn_143_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_143_capitulation_signal},
    "ocn_144_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_144_capitulation_signal},
    "ocn_145_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_145_capitulation_signal},
    "ocn_146_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_146_capitulation_signal},
    "ocn_147_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_147_capitulation_signal},
    "ocn_148_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_148_capitulation_signal},
    "ocn_149_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_149_capitulation_signal},
    "ocn_150_capitulation_signal": {"inputs": ['close', 'inst_holders', 'inst_shares', 'inst_value', 'top_holder_share', 'holder_count'], "func": ocn_150_capitulation_signal},
}
