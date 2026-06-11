"""Generated capitulation features for 60_earnings_collapse: net income collapse.
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

def ecl_076_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def ecl_077_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close))

def ecl_078_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def ecl_079_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def ecl_080_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def ecl_081_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def ecl_082_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ecl_083_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def ecl_084_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).pct_change(21)

def ecl_085_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _z(x, 63)

def ecl_086_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, y)

def ecl_087_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(x - y, y.abs())

def ecl_088_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _rank(x, 504)

def ecl_089_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def ecl_090_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def ecl_091_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close))

def ecl_092_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def ecl_093_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def ecl_094_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def ecl_095_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def ecl_096_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ecl_097_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def ecl_098_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(126)

def ecl_099_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _z(x, 252)

def ecl_100_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(x, y)

def ecl_101_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(x - y, y.abs())

def ecl_102_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _rank(x, 21)

def ecl_103_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def ecl_104_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def ecl_105_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(x, _s(close))

def ecl_106_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def ecl_107_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def ecl_108_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def ecl_109_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def ecl_110_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ecl_111_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def ecl_112_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).pct_change(504)

def ecl_113_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _z(x, 756)

def ecl_114_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x, y)

def ecl_115_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(x - y, y.abs())

def ecl_116_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _rank(x, 126)

def ecl_117_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def ecl_118_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def ecl_119_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close))

def ecl_120_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def ecl_121_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def ecl_122_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def ecl_123_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def ecl_124_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ecl_125_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def ecl_126_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).pct_change(21)

def ecl_127_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _z(x, 63)

def ecl_128_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, y)

def ecl_129_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(x - y, y.abs())

def ecl_130_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _rank(x, 504)

def ecl_131_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def ecl_132_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def ecl_133_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close))

def ecl_134_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def ecl_135_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def ecl_136_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def ecl_137_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def ecl_138_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ecl_139_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def ecl_140_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(126)

def ecl_141_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _z(x, 252)

def ecl_142_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(x, y)

def ecl_143_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(x - y, y.abs())

def ecl_144_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _rank(x, 21)

def ecl_145_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def ecl_146_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def ecl_147_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(x, _s(close))

def ecl_148_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def ecl_149_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def ecl_150_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

EARNINGS_COLLAPSE_REGISTRY_076_150 = {
    "ecl_076_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_076_capitulation_signal},
    "ecl_077_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_077_capitulation_signal},
    "ecl_078_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_078_capitulation_signal},
    "ecl_079_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_079_capitulation_signal},
    "ecl_080_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_080_capitulation_signal},
    "ecl_081_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_081_capitulation_signal},
    "ecl_082_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_082_capitulation_signal},
    "ecl_083_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_083_capitulation_signal},
    "ecl_084_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_084_capitulation_signal},
    "ecl_085_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_085_capitulation_signal},
    "ecl_086_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_086_capitulation_signal},
    "ecl_087_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_087_capitulation_signal},
    "ecl_088_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_088_capitulation_signal},
    "ecl_089_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_089_capitulation_signal},
    "ecl_090_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_090_capitulation_signal},
    "ecl_091_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_091_capitulation_signal},
    "ecl_092_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_092_capitulation_signal},
    "ecl_093_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_093_capitulation_signal},
    "ecl_094_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_094_capitulation_signal},
    "ecl_095_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_095_capitulation_signal},
    "ecl_096_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_096_capitulation_signal},
    "ecl_097_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_097_capitulation_signal},
    "ecl_098_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_098_capitulation_signal},
    "ecl_099_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_099_capitulation_signal},
    "ecl_100_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_100_capitulation_signal},
    "ecl_101_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_101_capitulation_signal},
    "ecl_102_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_102_capitulation_signal},
    "ecl_103_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_103_capitulation_signal},
    "ecl_104_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_104_capitulation_signal},
    "ecl_105_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_105_capitulation_signal},
    "ecl_106_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_106_capitulation_signal},
    "ecl_107_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_107_capitulation_signal},
    "ecl_108_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_108_capitulation_signal},
    "ecl_109_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_109_capitulation_signal},
    "ecl_110_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_110_capitulation_signal},
    "ecl_111_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_111_capitulation_signal},
    "ecl_112_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_112_capitulation_signal},
    "ecl_113_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_113_capitulation_signal},
    "ecl_114_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_114_capitulation_signal},
    "ecl_115_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_115_capitulation_signal},
    "ecl_116_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_116_capitulation_signal},
    "ecl_117_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_117_capitulation_signal},
    "ecl_118_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_118_capitulation_signal},
    "ecl_119_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_119_capitulation_signal},
    "ecl_120_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_120_capitulation_signal},
    "ecl_121_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_121_capitulation_signal},
    "ecl_122_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_122_capitulation_signal},
    "ecl_123_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_123_capitulation_signal},
    "ecl_124_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_124_capitulation_signal},
    "ecl_125_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_125_capitulation_signal},
    "ecl_126_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_126_capitulation_signal},
    "ecl_127_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_127_capitulation_signal},
    "ecl_128_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_128_capitulation_signal},
    "ecl_129_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_129_capitulation_signal},
    "ecl_130_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_130_capitulation_signal},
    "ecl_131_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_131_capitulation_signal},
    "ecl_132_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_132_capitulation_signal},
    "ecl_133_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_133_capitulation_signal},
    "ecl_134_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_134_capitulation_signal},
    "ecl_135_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_135_capitulation_signal},
    "ecl_136_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_136_capitulation_signal},
    "ecl_137_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_137_capitulation_signal},
    "ecl_138_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_138_capitulation_signal},
    "ecl_139_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_139_capitulation_signal},
    "ecl_140_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_140_capitulation_signal},
    "ecl_141_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_141_capitulation_signal},
    "ecl_142_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_142_capitulation_signal},
    "ecl_143_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_143_capitulation_signal},
    "ecl_144_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_144_capitulation_signal},
    "ecl_145_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_145_capitulation_signal},
    "ecl_146_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_146_capitulation_signal},
    "ecl_147_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_147_capitulation_signal},
    "ecl_148_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_148_capitulation_signal},
    "ecl_149_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_149_capitulation_signal},
    "ecl_150_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": ecl_150_capitulation_signal},
}
