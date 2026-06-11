"""Generated capitulation features for 77_valuation_collapse: valuation multiple collapse.
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

def vcl_076_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def vcl_077_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _div(x, _s(close))

def vcl_078_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def vcl_079_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def vcl_080_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def vcl_081_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def vcl_082_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vcl_083_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def vcl_084_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _s(x).pct_change(21)

def vcl_085_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _z(x, 63)

def vcl_086_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _div(x, y)

def vcl_087_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x - y, y.abs())

def vcl_088_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _rank(x, 504)

def vcl_089_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def vcl_090_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def vcl_091_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _div(x, _s(close))

def vcl_092_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def vcl_093_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def vcl_094_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def vcl_095_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def vcl_096_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vcl_097_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def vcl_098_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(126)

def vcl_099_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _z(x, 252)

def vcl_100_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _div(x, y)

def vcl_101_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _div(x - y, y.abs())

def vcl_102_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _rank(x, 21)

def vcl_103_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def vcl_104_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def vcl_105_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close))

def vcl_106_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def vcl_107_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def vcl_108_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def vcl_109_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def vcl_110_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vcl_111_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def vcl_112_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _s(x).pct_change(504)

def vcl_113_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _z(x, 756)

def vcl_114_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, y)

def vcl_115_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _div(x - y, y.abs())

def vcl_116_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _rank(x, 126)

def vcl_117_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def vcl_118_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def vcl_119_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _div(x, _s(close))

def vcl_120_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def vcl_121_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def vcl_122_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def vcl_123_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def vcl_124_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vcl_125_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def vcl_126_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _s(x).pct_change(21)

def vcl_127_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _z(x, 63)

def vcl_128_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _div(x, y)

def vcl_129_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _div(x - y, y.abs())

def vcl_130_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _rank(x, 504)

def vcl_131_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def vcl_132_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def vcl_133_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _div(x, _s(close))

def vcl_134_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def vcl_135_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def vcl_136_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def vcl_137_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def vcl_138_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vcl_139_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def vcl_140_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _s(x).pct_change(126)

def vcl_141_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _z(x, 252)

def vcl_142_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _div(x, y)

def vcl_143_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _div(x - y, y.abs())

def vcl_144_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _rank(x, 21)

def vcl_145_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def vcl_146_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def vcl_147_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _div(x, _s(close))

def vcl_148_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def vcl_149_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def vcl_150_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

VALUATION_COLLAPSE_REGISTRY_076_150 = {
    "vcl_076_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_076_capitulation_signal},
    "vcl_077_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_077_capitulation_signal},
    "vcl_078_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_078_capitulation_signal},
    "vcl_079_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_079_capitulation_signal},
    "vcl_080_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_080_capitulation_signal},
    "vcl_081_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_081_capitulation_signal},
    "vcl_082_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_082_capitulation_signal},
    "vcl_083_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_083_capitulation_signal},
    "vcl_084_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_084_capitulation_signal},
    "vcl_085_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_085_capitulation_signal},
    "vcl_086_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_086_capitulation_signal},
    "vcl_087_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_087_capitulation_signal},
    "vcl_088_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_088_capitulation_signal},
    "vcl_089_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_089_capitulation_signal},
    "vcl_090_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_090_capitulation_signal},
    "vcl_091_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_091_capitulation_signal},
    "vcl_092_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_092_capitulation_signal},
    "vcl_093_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_093_capitulation_signal},
    "vcl_094_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_094_capitulation_signal},
    "vcl_095_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_095_capitulation_signal},
    "vcl_096_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_096_capitulation_signal},
    "vcl_097_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_097_capitulation_signal},
    "vcl_098_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_098_capitulation_signal},
    "vcl_099_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_099_capitulation_signal},
    "vcl_100_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_100_capitulation_signal},
    "vcl_101_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_101_capitulation_signal},
    "vcl_102_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_102_capitulation_signal},
    "vcl_103_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_103_capitulation_signal},
    "vcl_104_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_104_capitulation_signal},
    "vcl_105_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_105_capitulation_signal},
    "vcl_106_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_106_capitulation_signal},
    "vcl_107_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_107_capitulation_signal},
    "vcl_108_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_108_capitulation_signal},
    "vcl_109_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_109_capitulation_signal},
    "vcl_110_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_110_capitulation_signal},
    "vcl_111_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_111_capitulation_signal},
    "vcl_112_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_112_capitulation_signal},
    "vcl_113_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_113_capitulation_signal},
    "vcl_114_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_114_capitulation_signal},
    "vcl_115_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_115_capitulation_signal},
    "vcl_116_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_116_capitulation_signal},
    "vcl_117_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_117_capitulation_signal},
    "vcl_118_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_118_capitulation_signal},
    "vcl_119_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_119_capitulation_signal},
    "vcl_120_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_120_capitulation_signal},
    "vcl_121_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_121_capitulation_signal},
    "vcl_122_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_122_capitulation_signal},
    "vcl_123_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_123_capitulation_signal},
    "vcl_124_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_124_capitulation_signal},
    "vcl_125_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_125_capitulation_signal},
    "vcl_126_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_126_capitulation_signal},
    "vcl_127_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_127_capitulation_signal},
    "vcl_128_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_128_capitulation_signal},
    "vcl_129_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_129_capitulation_signal},
    "vcl_130_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_130_capitulation_signal},
    "vcl_131_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_131_capitulation_signal},
    "vcl_132_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_132_capitulation_signal},
    "vcl_133_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_133_capitulation_signal},
    "vcl_134_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_134_capitulation_signal},
    "vcl_135_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_135_capitulation_signal},
    "vcl_136_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_136_capitulation_signal},
    "vcl_137_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_137_capitulation_signal},
    "vcl_138_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_138_capitulation_signal},
    "vcl_139_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_139_capitulation_signal},
    "vcl_140_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_140_capitulation_signal},
    "vcl_141_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_141_capitulation_signal},
    "vcl_142_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_142_capitulation_signal},
    "vcl_143_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_143_capitulation_signal},
    "vcl_144_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_144_capitulation_signal},
    "vcl_145_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_145_capitulation_signal},
    "vcl_146_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_146_capitulation_signal},
    "vcl_147_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_147_capitulation_signal},
    "vcl_148_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_148_capitulation_signal},
    "vcl_149_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_149_capitulation_signal},
    "vcl_150_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vcl_150_capitulation_signal},
}
