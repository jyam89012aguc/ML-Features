"""Generated capitulation features for 97_reverse_split_signal: reverse-split distress.
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

def rss_076_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def rss_077_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x, _s(close))

def rss_078_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def rss_079_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def rss_080_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def rss_081_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def rss_082_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def rss_083_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def rss_084_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _s(x).pct_change(21)

def rss_085_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _z(x, 63)

def rss_086_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(x, y)

def rss_087_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x - y, y.abs())

def rss_088_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _rank(x, 504)

def rss_089_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def rss_090_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def rss_091_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(x, _s(close))

def rss_092_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def rss_093_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def rss_094_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def rss_095_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def rss_096_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def rss_097_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def rss_098_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _s(x).pct_change(126)

def rss_099_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _z(x, 252)

def rss_100_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(x, y)

def rss_101_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(x - y, y.abs())

def rss_102_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _rank(x, 21)

def rss_103_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def rss_104_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def rss_105_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(x, _s(close))

def rss_106_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def rss_107_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def rss_108_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def rss_109_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def rss_110_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def rss_111_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def rss_112_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _s(x).pct_change(504)

def rss_113_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _z(x, 756)

def rss_114_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(x, y)

def rss_115_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(x - y, y.abs())

def rss_116_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _rank(x, 126)

def rss_117_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def rss_118_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def rss_119_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(x, _s(close))

def rss_120_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def rss_121_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def rss_122_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def rss_123_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def rss_124_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def rss_125_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def rss_126_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _s(x).pct_change(21)

def rss_127_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _z(x, 63)

def rss_128_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x, y)

def rss_129_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(x - y, y.abs())

def rss_130_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _rank(x, 504)

def rss_131_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def rss_132_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def rss_133_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x, _s(close))

def rss_134_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def rss_135_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def rss_136_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def rss_137_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def rss_138_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def rss_139_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def rss_140_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _s(x).pct_change(126)

def rss_141_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _z(x, 252)

def rss_142_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x, y)

def rss_143_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x - y, y.abs())

def rss_144_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return _rank(x, 21)

def rss_145_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def rss_146_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(dividend_cut_flag, close)
    y = _align_to_close(reverse_split_flag, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def rss_147_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(reverse_split_flag, close)
    y = _align_to_close(going_concern_flag, close)
    return _div(x, _s(close))

def rss_148_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(going_concern_flag, close)
    y = _align_to_close(listing_risk_flag, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def rss_149_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(listing_risk_flag, close)
    y = _align_to_close(event_count, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def rss_150_capitulation_signal(close, event_count, dividend_cut_flag, reverse_split_flag, going_concern_flag, listing_risk_flag):
    x = _align_to_close(event_count, close)
    y = _align_to_close(dividend_cut_flag, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

REVERSE_SPLIT_SIGNAL_REGISTRY_076_150 = {
    "rss_076_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_076_capitulation_signal},
    "rss_077_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_077_capitulation_signal},
    "rss_078_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_078_capitulation_signal},
    "rss_079_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_079_capitulation_signal},
    "rss_080_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_080_capitulation_signal},
    "rss_081_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_081_capitulation_signal},
    "rss_082_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_082_capitulation_signal},
    "rss_083_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_083_capitulation_signal},
    "rss_084_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_084_capitulation_signal},
    "rss_085_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_085_capitulation_signal},
    "rss_086_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_086_capitulation_signal},
    "rss_087_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_087_capitulation_signal},
    "rss_088_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_088_capitulation_signal},
    "rss_089_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_089_capitulation_signal},
    "rss_090_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_090_capitulation_signal},
    "rss_091_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_091_capitulation_signal},
    "rss_092_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_092_capitulation_signal},
    "rss_093_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_093_capitulation_signal},
    "rss_094_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_094_capitulation_signal},
    "rss_095_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_095_capitulation_signal},
    "rss_096_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_096_capitulation_signal},
    "rss_097_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_097_capitulation_signal},
    "rss_098_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_098_capitulation_signal},
    "rss_099_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_099_capitulation_signal},
    "rss_100_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_100_capitulation_signal},
    "rss_101_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_101_capitulation_signal},
    "rss_102_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_102_capitulation_signal},
    "rss_103_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_103_capitulation_signal},
    "rss_104_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_104_capitulation_signal},
    "rss_105_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_105_capitulation_signal},
    "rss_106_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_106_capitulation_signal},
    "rss_107_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_107_capitulation_signal},
    "rss_108_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_108_capitulation_signal},
    "rss_109_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_109_capitulation_signal},
    "rss_110_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_110_capitulation_signal},
    "rss_111_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_111_capitulation_signal},
    "rss_112_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_112_capitulation_signal},
    "rss_113_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_113_capitulation_signal},
    "rss_114_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_114_capitulation_signal},
    "rss_115_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_115_capitulation_signal},
    "rss_116_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_116_capitulation_signal},
    "rss_117_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_117_capitulation_signal},
    "rss_118_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_118_capitulation_signal},
    "rss_119_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_119_capitulation_signal},
    "rss_120_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_120_capitulation_signal},
    "rss_121_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_121_capitulation_signal},
    "rss_122_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_122_capitulation_signal},
    "rss_123_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_123_capitulation_signal},
    "rss_124_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_124_capitulation_signal},
    "rss_125_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_125_capitulation_signal},
    "rss_126_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_126_capitulation_signal},
    "rss_127_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_127_capitulation_signal},
    "rss_128_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_128_capitulation_signal},
    "rss_129_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_129_capitulation_signal},
    "rss_130_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_130_capitulation_signal},
    "rss_131_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_131_capitulation_signal},
    "rss_132_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_132_capitulation_signal},
    "rss_133_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_133_capitulation_signal},
    "rss_134_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_134_capitulation_signal},
    "rss_135_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_135_capitulation_signal},
    "rss_136_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_136_capitulation_signal},
    "rss_137_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_137_capitulation_signal},
    "rss_138_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_138_capitulation_signal},
    "rss_139_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_139_capitulation_signal},
    "rss_140_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_140_capitulation_signal},
    "rss_141_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_141_capitulation_signal},
    "rss_142_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_142_capitulation_signal},
    "rss_143_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_143_capitulation_signal},
    "rss_144_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_144_capitulation_signal},
    "rss_145_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_145_capitulation_signal},
    "rss_146_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_146_capitulation_signal},
    "rss_147_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_147_capitulation_signal},
    "rss_148_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_148_capitulation_signal},
    "rss_149_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_149_capitulation_signal},
    "rss_150_capitulation_signal": {"inputs": ['close', 'event_count', 'dividend_cut_flag', 'reverse_split_flag', 'going_concern_flag', 'listing_risk_flag'], "func": rss_150_capitulation_signal},
}
