"""Generated capitulation features for 73_earnings_volatility: earnings instability.
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

def evl_076_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def evl_077_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close))

def evl_078_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def evl_079_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def evl_080_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def evl_081_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def evl_082_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def evl_083_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def evl_084_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).pct_change(21)

def evl_085_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _z(x, 63)

def evl_086_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, y)

def evl_087_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(x - y, y.abs())

def evl_088_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _rank(x, 504)

def evl_089_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def evl_090_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def evl_091_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close))

def evl_092_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def evl_093_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def evl_094_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def evl_095_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def evl_096_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def evl_097_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def evl_098_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(126)

def evl_099_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _z(x, 252)

def evl_100_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(x, y)

def evl_101_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(x - y, y.abs())

def evl_102_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _rank(x, 21)

def evl_103_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def evl_104_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def evl_105_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(x, _s(close))

def evl_106_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def evl_107_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def evl_108_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def evl_109_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def evl_110_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def evl_111_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def evl_112_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).pct_change(504)

def evl_113_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _z(x, 756)

def evl_114_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x, y)

def evl_115_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(x - y, y.abs())

def evl_116_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _rank(x, 126)

def evl_117_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def evl_118_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def evl_119_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close))

def evl_120_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def evl_121_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def evl_122_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def evl_123_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def evl_124_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def evl_125_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def evl_126_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).pct_change(21)

def evl_127_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _z(x, 63)

def evl_128_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, y)

def evl_129_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(x - y, y.abs())

def evl_130_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _rank(x, 504)

def evl_131_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def evl_132_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def evl_133_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close))

def evl_134_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def evl_135_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def evl_136_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def evl_137_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def evl_138_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def evl_139_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def evl_140_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(126)

def evl_141_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _z(x, 252)

def evl_142_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(x, y)

def evl_143_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(x - y, y.abs())

def evl_144_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _rank(x, 21)

def evl_145_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def evl_146_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def evl_147_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(x, _s(close))

def evl_148_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def evl_149_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def evl_150_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

EARNINGS_VOLATILITY_REGISTRY_076_150 = {
    "evl_076_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_076_capitulation_signal},
    "evl_077_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_077_capitulation_signal},
    "evl_078_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_078_capitulation_signal},
    "evl_079_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_079_capitulation_signal},
    "evl_080_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_080_capitulation_signal},
    "evl_081_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_081_capitulation_signal},
    "evl_082_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_082_capitulation_signal},
    "evl_083_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_083_capitulation_signal},
    "evl_084_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_084_capitulation_signal},
    "evl_085_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_085_capitulation_signal},
    "evl_086_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_086_capitulation_signal},
    "evl_087_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_087_capitulation_signal},
    "evl_088_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_088_capitulation_signal},
    "evl_089_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_089_capitulation_signal},
    "evl_090_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_090_capitulation_signal},
    "evl_091_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_091_capitulation_signal},
    "evl_092_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_092_capitulation_signal},
    "evl_093_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_093_capitulation_signal},
    "evl_094_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_094_capitulation_signal},
    "evl_095_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_095_capitulation_signal},
    "evl_096_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_096_capitulation_signal},
    "evl_097_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_097_capitulation_signal},
    "evl_098_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_098_capitulation_signal},
    "evl_099_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_099_capitulation_signal},
    "evl_100_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_100_capitulation_signal},
    "evl_101_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_101_capitulation_signal},
    "evl_102_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_102_capitulation_signal},
    "evl_103_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_103_capitulation_signal},
    "evl_104_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_104_capitulation_signal},
    "evl_105_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_105_capitulation_signal},
    "evl_106_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_106_capitulation_signal},
    "evl_107_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_107_capitulation_signal},
    "evl_108_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_108_capitulation_signal},
    "evl_109_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_109_capitulation_signal},
    "evl_110_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_110_capitulation_signal},
    "evl_111_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_111_capitulation_signal},
    "evl_112_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_112_capitulation_signal},
    "evl_113_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_113_capitulation_signal},
    "evl_114_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_114_capitulation_signal},
    "evl_115_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_115_capitulation_signal},
    "evl_116_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_116_capitulation_signal},
    "evl_117_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_117_capitulation_signal},
    "evl_118_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_118_capitulation_signal},
    "evl_119_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_119_capitulation_signal},
    "evl_120_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_120_capitulation_signal},
    "evl_121_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_121_capitulation_signal},
    "evl_122_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_122_capitulation_signal},
    "evl_123_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_123_capitulation_signal},
    "evl_124_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_124_capitulation_signal},
    "evl_125_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_125_capitulation_signal},
    "evl_126_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_126_capitulation_signal},
    "evl_127_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_127_capitulation_signal},
    "evl_128_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_128_capitulation_signal},
    "evl_129_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_129_capitulation_signal},
    "evl_130_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_130_capitulation_signal},
    "evl_131_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_131_capitulation_signal},
    "evl_132_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_132_capitulation_signal},
    "evl_133_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_133_capitulation_signal},
    "evl_134_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_134_capitulation_signal},
    "evl_135_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_135_capitulation_signal},
    "evl_136_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_136_capitulation_signal},
    "evl_137_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_137_capitulation_signal},
    "evl_138_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_138_capitulation_signal},
    "evl_139_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_139_capitulation_signal},
    "evl_140_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_140_capitulation_signal},
    "evl_141_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_141_capitulation_signal},
    "evl_142_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_142_capitulation_signal},
    "evl_143_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_143_capitulation_signal},
    "evl_144_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_144_capitulation_signal},
    "evl_145_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_145_capitulation_signal},
    "evl_146_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_146_capitulation_signal},
    "evl_147_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_147_capitulation_signal},
    "evl_148_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_148_capitulation_signal},
    "evl_149_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_149_capitulation_signal},
    "evl_150_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": evl_150_capitulation_signal},
}
