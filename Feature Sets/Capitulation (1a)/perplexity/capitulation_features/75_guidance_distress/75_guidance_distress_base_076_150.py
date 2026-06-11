"""Generated capitulation features for 75_guidance_distress: guidance/miss distress.
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

def gds_076_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def gds_077_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close))

def gds_078_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def gds_079_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def gds_080_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def gds_081_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def gds_082_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def gds_083_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def gds_084_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).pct_change(21)

def gds_085_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _z(x, 63)

def gds_086_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, y)

def gds_087_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(x - y, y.abs())

def gds_088_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _rank(x, 504)

def gds_089_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def gds_090_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def gds_091_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close))

def gds_092_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def gds_093_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def gds_094_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def gds_095_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def gds_096_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def gds_097_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def gds_098_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(126)

def gds_099_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _z(x, 252)

def gds_100_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(x, y)

def gds_101_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(x - y, y.abs())

def gds_102_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _rank(x, 21)

def gds_103_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def gds_104_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def gds_105_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(x, _s(close))

def gds_106_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def gds_107_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def gds_108_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def gds_109_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def gds_110_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def gds_111_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def gds_112_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).pct_change(504)

def gds_113_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _z(x, 756)

def gds_114_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x, y)

def gds_115_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(x - y, y.abs())

def gds_116_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _rank(x, 126)

def gds_117_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def gds_118_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def gds_119_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close))

def gds_120_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def gds_121_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def gds_122_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def gds_123_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def gds_124_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def gds_125_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def gds_126_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).pct_change(21)

def gds_127_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _z(x, 63)

def gds_128_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, y)

def gds_129_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(x - y, y.abs())

def gds_130_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _rank(x, 504)

def gds_131_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def gds_132_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def gds_133_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close))

def gds_134_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def gds_135_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def gds_136_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def gds_137_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def gds_138_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def gds_139_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def gds_140_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(126)

def gds_141_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _z(x, 252)

def gds_142_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(x, y)

def gds_143_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return _div(x - y, y.abs())

def gds_144_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _rank(x, 21)

def gds_145_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebit, close)
    y = _align_to_close(ebitda, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def gds_146_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(revenue, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def gds_147_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(revenue, close)
    y = _align_to_close(opex, close)
    return _div(x, _s(close))

def gds_148_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(opex, close)
    y = _align_to_close(taxexp, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def gds_149_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(taxexp, close)
    y = _align_to_close(netinc, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def gds_150_capitulation_signal(close, netinc, ebit, ebitda, revenue, opex, taxexp):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

GUIDANCE_DISTRESS_REGISTRY_076_150 = {
    "gds_076_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_076_capitulation_signal},
    "gds_077_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_077_capitulation_signal},
    "gds_078_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_078_capitulation_signal},
    "gds_079_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_079_capitulation_signal},
    "gds_080_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_080_capitulation_signal},
    "gds_081_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_081_capitulation_signal},
    "gds_082_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_082_capitulation_signal},
    "gds_083_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_083_capitulation_signal},
    "gds_084_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_084_capitulation_signal},
    "gds_085_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_085_capitulation_signal},
    "gds_086_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_086_capitulation_signal},
    "gds_087_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_087_capitulation_signal},
    "gds_088_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_088_capitulation_signal},
    "gds_089_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_089_capitulation_signal},
    "gds_090_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_090_capitulation_signal},
    "gds_091_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_091_capitulation_signal},
    "gds_092_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_092_capitulation_signal},
    "gds_093_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_093_capitulation_signal},
    "gds_094_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_094_capitulation_signal},
    "gds_095_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_095_capitulation_signal},
    "gds_096_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_096_capitulation_signal},
    "gds_097_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_097_capitulation_signal},
    "gds_098_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_098_capitulation_signal},
    "gds_099_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_099_capitulation_signal},
    "gds_100_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_100_capitulation_signal},
    "gds_101_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_101_capitulation_signal},
    "gds_102_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_102_capitulation_signal},
    "gds_103_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_103_capitulation_signal},
    "gds_104_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_104_capitulation_signal},
    "gds_105_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_105_capitulation_signal},
    "gds_106_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_106_capitulation_signal},
    "gds_107_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_107_capitulation_signal},
    "gds_108_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_108_capitulation_signal},
    "gds_109_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_109_capitulation_signal},
    "gds_110_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_110_capitulation_signal},
    "gds_111_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_111_capitulation_signal},
    "gds_112_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_112_capitulation_signal},
    "gds_113_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_113_capitulation_signal},
    "gds_114_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_114_capitulation_signal},
    "gds_115_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_115_capitulation_signal},
    "gds_116_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_116_capitulation_signal},
    "gds_117_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_117_capitulation_signal},
    "gds_118_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_118_capitulation_signal},
    "gds_119_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_119_capitulation_signal},
    "gds_120_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_120_capitulation_signal},
    "gds_121_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_121_capitulation_signal},
    "gds_122_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_122_capitulation_signal},
    "gds_123_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_123_capitulation_signal},
    "gds_124_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_124_capitulation_signal},
    "gds_125_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_125_capitulation_signal},
    "gds_126_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_126_capitulation_signal},
    "gds_127_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_127_capitulation_signal},
    "gds_128_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_128_capitulation_signal},
    "gds_129_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_129_capitulation_signal},
    "gds_130_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_130_capitulation_signal},
    "gds_131_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_131_capitulation_signal},
    "gds_132_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_132_capitulation_signal},
    "gds_133_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_133_capitulation_signal},
    "gds_134_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_134_capitulation_signal},
    "gds_135_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_135_capitulation_signal},
    "gds_136_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_136_capitulation_signal},
    "gds_137_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_137_capitulation_signal},
    "gds_138_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_138_capitulation_signal},
    "gds_139_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_139_capitulation_signal},
    "gds_140_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_140_capitulation_signal},
    "gds_141_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_141_capitulation_signal},
    "gds_142_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_142_capitulation_signal},
    "gds_143_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_143_capitulation_signal},
    "gds_144_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_144_capitulation_signal},
    "gds_145_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_145_capitulation_signal},
    "gds_146_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_146_capitulation_signal},
    "gds_147_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_147_capitulation_signal},
    "gds_148_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_148_capitulation_signal},
    "gds_149_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_149_capitulation_signal},
    "gds_150_capitulation_signal": {"inputs": ['close', 'netinc', 'ebit', 'ebitda', 'revenue', 'opex', 'taxexp'], "func": gds_150_capitulation_signal},
}
