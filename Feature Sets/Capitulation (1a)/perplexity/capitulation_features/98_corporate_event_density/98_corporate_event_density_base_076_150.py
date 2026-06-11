"""Generated capitulation features for 98_corporate_event_density: event filing spikes.
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

def ced_076_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def ced_077_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x, _s(close))

def ced_078_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def ced_079_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def ced_080_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def ced_081_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def ced_082_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ced_083_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def ced_084_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _s(x).pct_change(21)

def ced_085_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _z(x, 63)

def ced_086_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(x, y)

def ced_087_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x - y, y.abs())

def ced_088_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _rank(x, 504)

def ced_089_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def ced_090_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def ced_091_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(x, _s(close))

def ced_092_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def ced_093_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def ced_094_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def ced_095_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def ced_096_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ced_097_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def ced_098_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _s(x).pct_change(126)

def ced_099_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _z(x, 252)

def ced_100_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(x, y)

def ced_101_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(x - y, y.abs())

def ced_102_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _rank(x, 21)

def ced_103_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def ced_104_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def ced_105_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(x, _s(close))

def ced_106_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def ced_107_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def ced_108_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def ced_109_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def ced_110_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ced_111_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def ced_112_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _s(x).pct_change(504)

def ced_113_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _z(x, 756)

def ced_114_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(x, y)

def ced_115_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(x - y, y.abs())

def ced_116_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _rank(x, 126)

def ced_117_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def ced_118_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def ced_119_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(x, _s(close))

def ced_120_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def ced_121_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def ced_122_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def ced_123_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def ced_124_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ced_125_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def ced_126_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _s(x).pct_change(21)

def ced_127_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _z(x, 63)

def ced_128_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x, y)

def ced_129_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(x - y, y.abs())

def ced_130_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _rank(x, 504)

def ced_131_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def ced_132_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def ced_133_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x, _s(close))

def ced_134_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def ced_135_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def ced_136_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def ced_137_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def ced_138_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ced_139_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def ced_140_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _s(x).pct_change(126)

def ced_141_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _z(x, 252)

def ced_142_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x, y)

def ced_143_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x - y, y.abs())

def ced_144_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _rank(x, 21)

def ced_145_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def ced_146_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def ced_147_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x, _s(close))

def ced_148_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def ced_149_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def ced_150_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

CORPORATE_EVENT_DENSITY_REGISTRY_076_150 = {
    "ced_076_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_076_capitulation_signal},
    "ced_077_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_077_capitulation_signal},
    "ced_078_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_078_capitulation_signal},
    "ced_079_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_079_capitulation_signal},
    "ced_080_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_080_capitulation_signal},
    "ced_081_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_081_capitulation_signal},
    "ced_082_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_082_capitulation_signal},
    "ced_083_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_083_capitulation_signal},
    "ced_084_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_084_capitulation_signal},
    "ced_085_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_085_capitulation_signal},
    "ced_086_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_086_capitulation_signal},
    "ced_087_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_087_capitulation_signal},
    "ced_088_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_088_capitulation_signal},
    "ced_089_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_089_capitulation_signal},
    "ced_090_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_090_capitulation_signal},
    "ced_091_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_091_capitulation_signal},
    "ced_092_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_092_capitulation_signal},
    "ced_093_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_093_capitulation_signal},
    "ced_094_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_094_capitulation_signal},
    "ced_095_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_095_capitulation_signal},
    "ced_096_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_096_capitulation_signal},
    "ced_097_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_097_capitulation_signal},
    "ced_098_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_098_capitulation_signal},
    "ced_099_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_099_capitulation_signal},
    "ced_100_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_100_capitulation_signal},
    "ced_101_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_101_capitulation_signal},
    "ced_102_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_102_capitulation_signal},
    "ced_103_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_103_capitulation_signal},
    "ced_104_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_104_capitulation_signal},
    "ced_105_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_105_capitulation_signal},
    "ced_106_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_106_capitulation_signal},
    "ced_107_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_107_capitulation_signal},
    "ced_108_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_108_capitulation_signal},
    "ced_109_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_109_capitulation_signal},
    "ced_110_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_110_capitulation_signal},
    "ced_111_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_111_capitulation_signal},
    "ced_112_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_112_capitulation_signal},
    "ced_113_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_113_capitulation_signal},
    "ced_114_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_114_capitulation_signal},
    "ced_115_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_115_capitulation_signal},
    "ced_116_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_116_capitulation_signal},
    "ced_117_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_117_capitulation_signal},
    "ced_118_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_118_capitulation_signal},
    "ced_119_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_119_capitulation_signal},
    "ced_120_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_120_capitulation_signal},
    "ced_121_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_121_capitulation_signal},
    "ced_122_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_122_capitulation_signal},
    "ced_123_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_123_capitulation_signal},
    "ced_124_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_124_capitulation_signal},
    "ced_125_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_125_capitulation_signal},
    "ced_126_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_126_capitulation_signal},
    "ced_127_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_127_capitulation_signal},
    "ced_128_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_128_capitulation_signal},
    "ced_129_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_129_capitulation_signal},
    "ced_130_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_130_capitulation_signal},
    "ced_131_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_131_capitulation_signal},
    "ced_132_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_132_capitulation_signal},
    "ced_133_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_133_capitulation_signal},
    "ced_134_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_134_capitulation_signal},
    "ced_135_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_135_capitulation_signal},
    "ced_136_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_136_capitulation_signal},
    "ced_137_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_137_capitulation_signal},
    "ced_138_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_138_capitulation_signal},
    "ced_139_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_139_capitulation_signal},
    "ced_140_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_140_capitulation_signal},
    "ced_141_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_141_capitulation_signal},
    "ced_142_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_142_capitulation_signal},
    "ced_143_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_143_capitulation_signal},
    "ced_144_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_144_capitulation_signal},
    "ced_145_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_145_capitulation_signal},
    "ced_146_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_146_capitulation_signal},
    "ced_147_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_147_capitulation_signal},
    "ced_148_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_148_capitulation_signal},
    "ced_149_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_149_capitulation_signal},
    "ced_150_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": ced_150_capitulation_signal},
}
