"""Generated capitulation features for 81_valuation_vs_history: multiples vs own history.
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

def vvh_076_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def vvh_077_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _div(x, _s(close))

def vvh_078_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def vvh_079_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def vvh_080_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def vvh_081_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def vvh_082_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vvh_083_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def vvh_084_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _s(x).pct_change(21)

def vvh_085_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _z(x, 63)

def vvh_086_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _div(x, y)

def vvh_087_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x - y, y.abs())

def vvh_088_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _rank(x, 504)

def vvh_089_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def vvh_090_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def vvh_091_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _div(x, _s(close))

def vvh_092_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def vvh_093_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def vvh_094_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def vvh_095_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def vvh_096_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vvh_097_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def vvh_098_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(126)

def vvh_099_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _z(x, 252)

def vvh_100_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _div(x, y)

def vvh_101_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _div(x - y, y.abs())

def vvh_102_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _rank(x, 21)

def vvh_103_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def vvh_104_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def vvh_105_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close))

def vvh_106_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def vvh_107_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def vvh_108_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def vvh_109_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def vvh_110_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vvh_111_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def vvh_112_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _s(x).pct_change(504)

def vvh_113_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _z(x, 756)

def vvh_114_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, y)

def vvh_115_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _div(x - y, y.abs())

def vvh_116_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _rank(x, 126)

def vvh_117_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def vvh_118_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def vvh_119_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _div(x, _s(close))

def vvh_120_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def vvh_121_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def vvh_122_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def vvh_123_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def vvh_124_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vvh_125_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def vvh_126_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _s(x).pct_change(21)

def vvh_127_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _z(x, 63)

def vvh_128_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _div(x, y)

def vvh_129_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _div(x - y, y.abs())

def vvh_130_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _rank(x, 504)

def vvh_131_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def vvh_132_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def vvh_133_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _div(x, _s(close))

def vvh_134_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def vvh_135_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def vvh_136_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def vvh_137_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def vvh_138_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def vvh_139_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def vvh_140_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return _s(x).pct_change(126)

def vvh_141_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _z(x, 252)

def vvh_142_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(revenue, close)
    y = _align_to_close(equity, close)
    return _div(x, y)

def vvh_143_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(marketcap, close)
    return _div(x - y, y.abs())

def vvh_144_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(ev, close)
    return _rank(x, 21)

def vvh_145_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ev, close)
    y = _align_to_close(pe, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def vvh_146_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pe, close)
    y = _align_to_close(pb, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def vvh_147_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(pb, close)
    y = _align_to_close(ps, close)
    return _div(x, _s(close))

def vvh_148_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(ps, close)
    y = _align_to_close(evsales, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def vvh_149_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evsales, close)
    y = _align_to_close(evebitda, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def vvh_150_capitulation_signal(close, marketcap, ev, pe, pb, ps, evsales, evebitda, revenue, equity):
    x = _align_to_close(evebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

VALUATION_VS_HISTORY_REGISTRY_076_150 = {
    "vvh_076_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_076_capitulation_signal},
    "vvh_077_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_077_capitulation_signal},
    "vvh_078_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_078_capitulation_signal},
    "vvh_079_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_079_capitulation_signal},
    "vvh_080_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_080_capitulation_signal},
    "vvh_081_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_081_capitulation_signal},
    "vvh_082_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_082_capitulation_signal},
    "vvh_083_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_083_capitulation_signal},
    "vvh_084_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_084_capitulation_signal},
    "vvh_085_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_085_capitulation_signal},
    "vvh_086_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_086_capitulation_signal},
    "vvh_087_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_087_capitulation_signal},
    "vvh_088_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_088_capitulation_signal},
    "vvh_089_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_089_capitulation_signal},
    "vvh_090_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_090_capitulation_signal},
    "vvh_091_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_091_capitulation_signal},
    "vvh_092_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_092_capitulation_signal},
    "vvh_093_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_093_capitulation_signal},
    "vvh_094_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_094_capitulation_signal},
    "vvh_095_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_095_capitulation_signal},
    "vvh_096_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_096_capitulation_signal},
    "vvh_097_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_097_capitulation_signal},
    "vvh_098_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_098_capitulation_signal},
    "vvh_099_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_099_capitulation_signal},
    "vvh_100_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_100_capitulation_signal},
    "vvh_101_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_101_capitulation_signal},
    "vvh_102_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_102_capitulation_signal},
    "vvh_103_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_103_capitulation_signal},
    "vvh_104_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_104_capitulation_signal},
    "vvh_105_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_105_capitulation_signal},
    "vvh_106_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_106_capitulation_signal},
    "vvh_107_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_107_capitulation_signal},
    "vvh_108_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_108_capitulation_signal},
    "vvh_109_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_109_capitulation_signal},
    "vvh_110_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_110_capitulation_signal},
    "vvh_111_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_111_capitulation_signal},
    "vvh_112_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_112_capitulation_signal},
    "vvh_113_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_113_capitulation_signal},
    "vvh_114_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_114_capitulation_signal},
    "vvh_115_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_115_capitulation_signal},
    "vvh_116_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_116_capitulation_signal},
    "vvh_117_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_117_capitulation_signal},
    "vvh_118_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_118_capitulation_signal},
    "vvh_119_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_119_capitulation_signal},
    "vvh_120_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_120_capitulation_signal},
    "vvh_121_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_121_capitulation_signal},
    "vvh_122_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_122_capitulation_signal},
    "vvh_123_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_123_capitulation_signal},
    "vvh_124_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_124_capitulation_signal},
    "vvh_125_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_125_capitulation_signal},
    "vvh_126_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_126_capitulation_signal},
    "vvh_127_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_127_capitulation_signal},
    "vvh_128_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_128_capitulation_signal},
    "vvh_129_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_129_capitulation_signal},
    "vvh_130_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_130_capitulation_signal},
    "vvh_131_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_131_capitulation_signal},
    "vvh_132_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_132_capitulation_signal},
    "vvh_133_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_133_capitulation_signal},
    "vvh_134_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_134_capitulation_signal},
    "vvh_135_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_135_capitulation_signal},
    "vvh_136_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_136_capitulation_signal},
    "vvh_137_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_137_capitulation_signal},
    "vvh_138_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_138_capitulation_signal},
    "vvh_139_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_139_capitulation_signal},
    "vvh_140_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_140_capitulation_signal},
    "vvh_141_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_141_capitulation_signal},
    "vvh_142_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_142_capitulation_signal},
    "vvh_143_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_143_capitulation_signal},
    "vvh_144_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_144_capitulation_signal},
    "vvh_145_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_145_capitulation_signal},
    "vvh_146_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_146_capitulation_signal},
    "vvh_147_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_147_capitulation_signal},
    "vvh_148_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_148_capitulation_signal},
    "vvh_149_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_149_capitulation_signal},
    "vvh_150_capitulation_signal": {"inputs": ['close', 'marketcap', 'ev', 'pe', 'pb', 'ps', 'evsales', 'evebitda', 'revenue', 'equity'], "func": vvh_150_capitulation_signal},
}
