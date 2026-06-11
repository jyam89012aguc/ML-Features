"""Generated capitulation features for 69_equity_erosion: book value/equity erosion.
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

def eqe_076_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def eqe_077_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close))

def eqe_078_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def eqe_079_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def eqe_080_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def eqe_081_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def eqe_082_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def eqe_083_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def eqe_084_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _s(x).pct_change(21)

def eqe_085_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _z(x, 63)

def eqe_086_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _div(x, y)

def eqe_087_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _div(x - y, y.abs())

def eqe_088_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _rank(x, 504)

def eqe_089_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def eqe_090_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def eqe_091_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _div(x, _s(close))

def eqe_092_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def eqe_093_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def eqe_094_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def eqe_095_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def eqe_096_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def eqe_097_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def eqe_098_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).pct_change(126)

def eqe_099_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _z(x, 252)

def eqe_100_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _div(x, y)

def eqe_101_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _div(x - y, y.abs())

def eqe_102_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _rank(x, 21)

def eqe_103_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def eqe_104_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def eqe_105_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _div(x, _s(close))

def eqe_106_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def eqe_107_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def eqe_108_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def eqe_109_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def eqe_110_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def eqe_111_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def eqe_112_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _s(x).pct_change(504)

def eqe_113_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _z(x, 756)

def eqe_114_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _div(x, y)

def eqe_115_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _div(x - y, y.abs())

def eqe_116_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _rank(x, 126)

def eqe_117_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def eqe_118_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def eqe_119_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _div(x, _s(close))

def eqe_120_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def eqe_121_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def eqe_122_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def eqe_123_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def eqe_124_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def eqe_125_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def eqe_126_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _s(x).pct_change(21)

def eqe_127_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _z(x, 63)

def eqe_128_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, y)

def eqe_129_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _div(x - y, y.abs())

def eqe_130_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _rank(x, 504)

def eqe_131_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def eqe_132_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def eqe_133_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close))

def eqe_134_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def eqe_135_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def eqe_136_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def eqe_137_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def eqe_138_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def eqe_139_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def eqe_140_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _s(x).pct_change(126)

def eqe_141_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _z(x, 252)

def eqe_142_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _div(x, y)

def eqe_143_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x - y, y.abs())

def eqe_144_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _rank(x, 21)

def eqe_145_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def eqe_146_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def eqe_147_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close))

def eqe_148_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def eqe_149_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def eqe_150_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

EQUITY_EROSION_REGISTRY_076_150 = {
    "eqe_076_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_076_capitulation_signal},
    "eqe_077_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_077_capitulation_signal},
    "eqe_078_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_078_capitulation_signal},
    "eqe_079_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_079_capitulation_signal},
    "eqe_080_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_080_capitulation_signal},
    "eqe_081_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_081_capitulation_signal},
    "eqe_082_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_082_capitulation_signal},
    "eqe_083_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_083_capitulation_signal},
    "eqe_084_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_084_capitulation_signal},
    "eqe_085_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_085_capitulation_signal},
    "eqe_086_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_086_capitulation_signal},
    "eqe_087_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_087_capitulation_signal},
    "eqe_088_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_088_capitulation_signal},
    "eqe_089_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_089_capitulation_signal},
    "eqe_090_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_090_capitulation_signal},
    "eqe_091_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_091_capitulation_signal},
    "eqe_092_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_092_capitulation_signal},
    "eqe_093_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_093_capitulation_signal},
    "eqe_094_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_094_capitulation_signal},
    "eqe_095_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_095_capitulation_signal},
    "eqe_096_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_096_capitulation_signal},
    "eqe_097_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_097_capitulation_signal},
    "eqe_098_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_098_capitulation_signal},
    "eqe_099_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_099_capitulation_signal},
    "eqe_100_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_100_capitulation_signal},
    "eqe_101_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_101_capitulation_signal},
    "eqe_102_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_102_capitulation_signal},
    "eqe_103_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_103_capitulation_signal},
    "eqe_104_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_104_capitulation_signal},
    "eqe_105_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_105_capitulation_signal},
    "eqe_106_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_106_capitulation_signal},
    "eqe_107_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_107_capitulation_signal},
    "eqe_108_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_108_capitulation_signal},
    "eqe_109_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_109_capitulation_signal},
    "eqe_110_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_110_capitulation_signal},
    "eqe_111_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_111_capitulation_signal},
    "eqe_112_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_112_capitulation_signal},
    "eqe_113_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_113_capitulation_signal},
    "eqe_114_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_114_capitulation_signal},
    "eqe_115_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_115_capitulation_signal},
    "eqe_116_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_116_capitulation_signal},
    "eqe_117_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_117_capitulation_signal},
    "eqe_118_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_118_capitulation_signal},
    "eqe_119_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_119_capitulation_signal},
    "eqe_120_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_120_capitulation_signal},
    "eqe_121_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_121_capitulation_signal},
    "eqe_122_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_122_capitulation_signal},
    "eqe_123_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_123_capitulation_signal},
    "eqe_124_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_124_capitulation_signal},
    "eqe_125_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_125_capitulation_signal},
    "eqe_126_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_126_capitulation_signal},
    "eqe_127_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_127_capitulation_signal},
    "eqe_128_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_128_capitulation_signal},
    "eqe_129_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_129_capitulation_signal},
    "eqe_130_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_130_capitulation_signal},
    "eqe_131_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_131_capitulation_signal},
    "eqe_132_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_132_capitulation_signal},
    "eqe_133_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_133_capitulation_signal},
    "eqe_134_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_134_capitulation_signal},
    "eqe_135_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_135_capitulation_signal},
    "eqe_136_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_136_capitulation_signal},
    "eqe_137_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_137_capitulation_signal},
    "eqe_138_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_138_capitulation_signal},
    "eqe_139_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_139_capitulation_signal},
    "eqe_140_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_140_capitulation_signal},
    "eqe_141_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_141_capitulation_signal},
    "eqe_142_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_142_capitulation_signal},
    "eqe_143_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_143_capitulation_signal},
    "eqe_144_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_144_capitulation_signal},
    "eqe_145_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_145_capitulation_signal},
    "eqe_146_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_146_capitulation_signal},
    "eqe_147_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_147_capitulation_signal},
    "eqe_148_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_148_capitulation_signal},
    "eqe_149_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_149_capitulation_signal},
    "eqe_150_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_150_capitulation_signal},
}
