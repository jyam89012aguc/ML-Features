"""Generated capitulation features for 66_interest_coverage: interest coverage deterioration.
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

def icv_076_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def icv_077_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close))

def icv_078_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def icv_079_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def icv_080_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def icv_081_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def icv_082_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def icv_083_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def icv_084_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _s(x).pct_change(21)

def icv_085_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _z(x, 63)

def icv_086_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _div(x, y)

def icv_087_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _div(x - y, y.abs())

def icv_088_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _rank(x, 504)

def icv_089_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def icv_090_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def icv_091_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _div(x, _s(close))

def icv_092_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def icv_093_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def icv_094_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def icv_095_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def icv_096_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def icv_097_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def icv_098_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _s(x).pct_change(126)

def icv_099_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _z(x, 252)

def icv_100_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _div(x, y)

def icv_101_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _div(x - y, y.abs())

def icv_102_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _rank(x, 21)

def icv_103_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def icv_104_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def icv_105_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _div(x, _s(close))

def icv_106_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def icv_107_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def icv_108_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def icv_109_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def icv_110_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def icv_111_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def icv_112_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _s(x).pct_change(504)

def icv_113_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _z(x, 756)

def icv_114_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _div(x, y)

def icv_115_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _div(x - y, y.abs())

def icv_116_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _rank(x, 126)

def icv_117_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def icv_118_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def icv_119_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _div(x, _s(close))

def icv_120_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def icv_121_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def icv_122_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def icv_123_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def icv_124_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def icv_125_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def icv_126_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _s(x).pct_change(21)

def icv_127_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _z(x, 63)

def icv_128_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _div(x, y)

def icv_129_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _div(x - y, y.abs())

def icv_130_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _rank(x, 504)

def icv_131_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def icv_132_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def icv_133_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _div(x, _s(close))

def icv_134_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def icv_135_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def icv_136_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def icv_137_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def icv_138_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def icv_139_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def icv_140_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _s(x).pct_change(126)

def icv_141_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _z(x, 252)

def icv_142_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _div(x, y)

def icv_143_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _div(x - y, y.abs())

def icv_144_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _rank(x, 21)

def icv_145_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def icv_146_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def icv_147_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close))

def icv_148_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def icv_149_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def icv_150_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

INTEREST_COVERAGE_REGISTRY_076_150 = {
    "icv_076_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_076_capitulation_signal},
    "icv_077_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_077_capitulation_signal},
    "icv_078_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_078_capitulation_signal},
    "icv_079_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_079_capitulation_signal},
    "icv_080_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_080_capitulation_signal},
    "icv_081_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_081_capitulation_signal},
    "icv_082_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_082_capitulation_signal},
    "icv_083_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_083_capitulation_signal},
    "icv_084_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_084_capitulation_signal},
    "icv_085_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_085_capitulation_signal},
    "icv_086_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_086_capitulation_signal},
    "icv_087_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_087_capitulation_signal},
    "icv_088_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_088_capitulation_signal},
    "icv_089_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_089_capitulation_signal},
    "icv_090_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_090_capitulation_signal},
    "icv_091_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_091_capitulation_signal},
    "icv_092_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_092_capitulation_signal},
    "icv_093_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_093_capitulation_signal},
    "icv_094_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_094_capitulation_signal},
    "icv_095_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_095_capitulation_signal},
    "icv_096_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_096_capitulation_signal},
    "icv_097_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_097_capitulation_signal},
    "icv_098_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_098_capitulation_signal},
    "icv_099_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_099_capitulation_signal},
    "icv_100_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_100_capitulation_signal},
    "icv_101_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_101_capitulation_signal},
    "icv_102_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_102_capitulation_signal},
    "icv_103_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_103_capitulation_signal},
    "icv_104_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_104_capitulation_signal},
    "icv_105_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_105_capitulation_signal},
    "icv_106_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_106_capitulation_signal},
    "icv_107_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_107_capitulation_signal},
    "icv_108_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_108_capitulation_signal},
    "icv_109_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_109_capitulation_signal},
    "icv_110_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_110_capitulation_signal},
    "icv_111_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_111_capitulation_signal},
    "icv_112_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_112_capitulation_signal},
    "icv_113_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_113_capitulation_signal},
    "icv_114_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_114_capitulation_signal},
    "icv_115_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_115_capitulation_signal},
    "icv_116_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_116_capitulation_signal},
    "icv_117_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_117_capitulation_signal},
    "icv_118_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_118_capitulation_signal},
    "icv_119_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_119_capitulation_signal},
    "icv_120_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_120_capitulation_signal},
    "icv_121_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_121_capitulation_signal},
    "icv_122_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_122_capitulation_signal},
    "icv_123_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_123_capitulation_signal},
    "icv_124_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_124_capitulation_signal},
    "icv_125_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_125_capitulation_signal},
    "icv_126_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_126_capitulation_signal},
    "icv_127_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_127_capitulation_signal},
    "icv_128_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_128_capitulation_signal},
    "icv_129_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_129_capitulation_signal},
    "icv_130_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_130_capitulation_signal},
    "icv_131_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_131_capitulation_signal},
    "icv_132_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_132_capitulation_signal},
    "icv_133_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_133_capitulation_signal},
    "icv_134_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_134_capitulation_signal},
    "icv_135_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_135_capitulation_signal},
    "icv_136_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_136_capitulation_signal},
    "icv_137_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_137_capitulation_signal},
    "icv_138_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_138_capitulation_signal},
    "icv_139_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_139_capitulation_signal},
    "icv_140_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_140_capitulation_signal},
    "icv_141_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_141_capitulation_signal},
    "icv_142_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_142_capitulation_signal},
    "icv_143_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_143_capitulation_signal},
    "icv_144_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_144_capitulation_signal},
    "icv_145_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_145_capitulation_signal},
    "icv_146_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_146_capitulation_signal},
    "icv_147_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_147_capitulation_signal},
    "icv_148_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_148_capitulation_signal},
    "icv_149_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_149_capitulation_signal},
    "icv_150_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_150_capitulation_signal},
}
