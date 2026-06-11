"""Generated capitulation features for 62_margin_compression: margin erosion.
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

def mgc_076_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def mgc_077_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close))

def mgc_078_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def mgc_079_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def mgc_080_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def mgc_081_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def mgc_082_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def mgc_083_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def mgc_084_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(21)

def mgc_085_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _z(x, 63)

def mgc_086_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _div(x, y)

def mgc_087_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _div(x - y, y.abs())

def mgc_088_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _rank(x, 504)

def mgc_089_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def mgc_090_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def mgc_091_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _div(x, _s(close))

def mgc_092_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def mgc_093_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def mgc_094_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def mgc_095_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def mgc_096_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def mgc_097_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def mgc_098_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).pct_change(126)

def mgc_099_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _z(x, 252)

def mgc_100_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(x, y)

def mgc_101_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _div(x - y, y.abs())

def mgc_102_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _rank(x, 21)

def mgc_103_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def mgc_104_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def mgc_105_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(x, _s(close))

def mgc_106_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def mgc_107_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def mgc_108_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def mgc_109_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def mgc_110_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def mgc_111_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def mgc_112_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(504)

def mgc_113_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _z(x, 756)

def mgc_114_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _div(x, y)

def mgc_115_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(x - y, y.abs())

def mgc_116_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _rank(x, 126)

def mgc_117_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def mgc_118_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def mgc_119_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close))

def mgc_120_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def mgc_121_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def mgc_122_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def mgc_123_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def mgc_124_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def mgc_125_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def mgc_126_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _s(x).pct_change(21)

def mgc_127_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _z(x, 63)

def mgc_128_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x, y)

def mgc_129_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _div(x - y, y.abs())

def mgc_130_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _rank(x, 504)

def mgc_131_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def mgc_132_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def mgc_133_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x, _s(close))

def mgc_134_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def mgc_135_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def mgc_136_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def mgc_137_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def mgc_138_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def mgc_139_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def mgc_140_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _s(x).pct_change(126)

def mgc_141_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _z(x, 252)

def mgc_142_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _div(x, y)

def mgc_143_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x - y, y.abs())

def mgc_144_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _rank(x, 21)

def mgc_145_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def mgc_146_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def mgc_147_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close))

def mgc_148_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def mgc_149_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def mgc_150_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

MARGIN_COMPRESSION_REGISTRY_076_150 = {
    "mgc_076_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_076_capitulation_signal},
    "mgc_077_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_077_capitulation_signal},
    "mgc_078_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_078_capitulation_signal},
    "mgc_079_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_079_capitulation_signal},
    "mgc_080_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_080_capitulation_signal},
    "mgc_081_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_081_capitulation_signal},
    "mgc_082_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_082_capitulation_signal},
    "mgc_083_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_083_capitulation_signal},
    "mgc_084_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_084_capitulation_signal},
    "mgc_085_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_085_capitulation_signal},
    "mgc_086_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_086_capitulation_signal},
    "mgc_087_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_087_capitulation_signal},
    "mgc_088_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_088_capitulation_signal},
    "mgc_089_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_089_capitulation_signal},
    "mgc_090_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_090_capitulation_signal},
    "mgc_091_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_091_capitulation_signal},
    "mgc_092_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_092_capitulation_signal},
    "mgc_093_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_093_capitulation_signal},
    "mgc_094_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_094_capitulation_signal},
    "mgc_095_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_095_capitulation_signal},
    "mgc_096_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_096_capitulation_signal},
    "mgc_097_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_097_capitulation_signal},
    "mgc_098_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_098_capitulation_signal},
    "mgc_099_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_099_capitulation_signal},
    "mgc_100_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_100_capitulation_signal},
    "mgc_101_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_101_capitulation_signal},
    "mgc_102_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_102_capitulation_signal},
    "mgc_103_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_103_capitulation_signal},
    "mgc_104_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_104_capitulation_signal},
    "mgc_105_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_105_capitulation_signal},
    "mgc_106_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_106_capitulation_signal},
    "mgc_107_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_107_capitulation_signal},
    "mgc_108_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_108_capitulation_signal},
    "mgc_109_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_109_capitulation_signal},
    "mgc_110_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_110_capitulation_signal},
    "mgc_111_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_111_capitulation_signal},
    "mgc_112_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_112_capitulation_signal},
    "mgc_113_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_113_capitulation_signal},
    "mgc_114_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_114_capitulation_signal},
    "mgc_115_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_115_capitulation_signal},
    "mgc_116_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_116_capitulation_signal},
    "mgc_117_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_117_capitulation_signal},
    "mgc_118_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_118_capitulation_signal},
    "mgc_119_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_119_capitulation_signal},
    "mgc_120_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_120_capitulation_signal},
    "mgc_121_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_121_capitulation_signal},
    "mgc_122_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_122_capitulation_signal},
    "mgc_123_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_123_capitulation_signal},
    "mgc_124_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_124_capitulation_signal},
    "mgc_125_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_125_capitulation_signal},
    "mgc_126_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_126_capitulation_signal},
    "mgc_127_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_127_capitulation_signal},
    "mgc_128_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_128_capitulation_signal},
    "mgc_129_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_129_capitulation_signal},
    "mgc_130_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_130_capitulation_signal},
    "mgc_131_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_131_capitulation_signal},
    "mgc_132_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_132_capitulation_signal},
    "mgc_133_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_133_capitulation_signal},
    "mgc_134_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_134_capitulation_signal},
    "mgc_135_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_135_capitulation_signal},
    "mgc_136_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_136_capitulation_signal},
    "mgc_137_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_137_capitulation_signal},
    "mgc_138_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_138_capitulation_signal},
    "mgc_139_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_139_capitulation_signal},
    "mgc_140_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_140_capitulation_signal},
    "mgc_141_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_141_capitulation_signal},
    "mgc_142_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_142_capitulation_signal},
    "mgc_143_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_143_capitulation_signal},
    "mgc_144_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_144_capitulation_signal},
    "mgc_145_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_145_capitulation_signal},
    "mgc_146_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_146_capitulation_signal},
    "mgc_147_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_147_capitulation_signal},
    "mgc_148_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_148_capitulation_signal},
    "mgc_149_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_149_capitulation_signal},
    "mgc_150_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_150_capitulation_signal},
}
