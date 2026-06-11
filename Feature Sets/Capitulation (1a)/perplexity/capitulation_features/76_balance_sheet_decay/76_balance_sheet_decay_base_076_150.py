"""Generated capitulation features for 76_balance_sheet_decay: balance-sheet deterioration.
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

def bsd_076_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def bsd_077_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close))

def bsd_078_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def bsd_079_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def bsd_080_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def bsd_081_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def bsd_082_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def bsd_083_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def bsd_084_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _s(x).pct_change(21)

def bsd_085_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _z(x, 63)

def bsd_086_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _div(x, y)

def bsd_087_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x - y, y.abs())

def bsd_088_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _rank(x, 504)

def bsd_089_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def bsd_090_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def bsd_091_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close))

def bsd_092_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def bsd_093_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def bsd_094_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def bsd_095_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def bsd_096_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def bsd_097_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def bsd_098_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _s(x).pct_change(126)

def bsd_099_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _z(x, 252)

def bsd_100_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _div(x, y)

def bsd_101_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _div(x - y, y.abs())

def bsd_102_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _rank(x, 21)

def bsd_103_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def bsd_104_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def bsd_105_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _div(x, _s(close))

def bsd_106_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def bsd_107_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def bsd_108_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def bsd_109_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def bsd_110_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def bsd_111_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def bsd_112_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).pct_change(504)

def bsd_113_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _z(x, 756)

def bsd_114_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _div(x, y)

def bsd_115_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _div(x - y, y.abs())

def bsd_116_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _rank(x, 126)

def bsd_117_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def bsd_118_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def bsd_119_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _div(x, _s(close))

def bsd_120_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def bsd_121_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def bsd_122_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def bsd_123_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def bsd_124_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def bsd_125_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def bsd_126_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _s(x).pct_change(21)

def bsd_127_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _z(x, 63)

def bsd_128_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _div(x, y)

def bsd_129_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _div(x - y, y.abs())

def bsd_130_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _rank(x, 504)

def bsd_131_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def bsd_132_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def bsd_133_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close))

def bsd_134_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def bsd_135_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def bsd_136_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def bsd_137_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def bsd_138_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def bsd_139_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def bsd_140_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _s(x).pct_change(126)

def bsd_141_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _z(x, 252)

def bsd_142_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, y)

def bsd_143_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _div(x - y, y.abs())

def bsd_144_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _rank(x, 21)

def bsd_145_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def bsd_146_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def bsd_147_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close))

def bsd_148_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def bsd_149_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def bsd_150_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

BALANCE_SHEET_DECAY_REGISTRY_076_150 = {
    "bsd_076_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_076_capitulation_signal},
    "bsd_077_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_077_capitulation_signal},
    "bsd_078_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_078_capitulation_signal},
    "bsd_079_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_079_capitulation_signal},
    "bsd_080_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_080_capitulation_signal},
    "bsd_081_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_081_capitulation_signal},
    "bsd_082_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_082_capitulation_signal},
    "bsd_083_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_083_capitulation_signal},
    "bsd_084_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_084_capitulation_signal},
    "bsd_085_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_085_capitulation_signal},
    "bsd_086_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_086_capitulation_signal},
    "bsd_087_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_087_capitulation_signal},
    "bsd_088_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_088_capitulation_signal},
    "bsd_089_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_089_capitulation_signal},
    "bsd_090_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_090_capitulation_signal},
    "bsd_091_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_091_capitulation_signal},
    "bsd_092_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_092_capitulation_signal},
    "bsd_093_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_093_capitulation_signal},
    "bsd_094_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_094_capitulation_signal},
    "bsd_095_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_095_capitulation_signal},
    "bsd_096_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_096_capitulation_signal},
    "bsd_097_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_097_capitulation_signal},
    "bsd_098_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_098_capitulation_signal},
    "bsd_099_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_099_capitulation_signal},
    "bsd_100_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_100_capitulation_signal},
    "bsd_101_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_101_capitulation_signal},
    "bsd_102_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_102_capitulation_signal},
    "bsd_103_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_103_capitulation_signal},
    "bsd_104_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_104_capitulation_signal},
    "bsd_105_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_105_capitulation_signal},
    "bsd_106_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_106_capitulation_signal},
    "bsd_107_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_107_capitulation_signal},
    "bsd_108_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_108_capitulation_signal},
    "bsd_109_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_109_capitulation_signal},
    "bsd_110_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_110_capitulation_signal},
    "bsd_111_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_111_capitulation_signal},
    "bsd_112_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_112_capitulation_signal},
    "bsd_113_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_113_capitulation_signal},
    "bsd_114_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_114_capitulation_signal},
    "bsd_115_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_115_capitulation_signal},
    "bsd_116_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_116_capitulation_signal},
    "bsd_117_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_117_capitulation_signal},
    "bsd_118_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_118_capitulation_signal},
    "bsd_119_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_119_capitulation_signal},
    "bsd_120_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_120_capitulation_signal},
    "bsd_121_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_121_capitulation_signal},
    "bsd_122_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_122_capitulation_signal},
    "bsd_123_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_123_capitulation_signal},
    "bsd_124_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_124_capitulation_signal},
    "bsd_125_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_125_capitulation_signal},
    "bsd_126_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_126_capitulation_signal},
    "bsd_127_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_127_capitulation_signal},
    "bsd_128_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_128_capitulation_signal},
    "bsd_129_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_129_capitulation_signal},
    "bsd_130_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_130_capitulation_signal},
    "bsd_131_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_131_capitulation_signal},
    "bsd_132_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_132_capitulation_signal},
    "bsd_133_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_133_capitulation_signal},
    "bsd_134_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_134_capitulation_signal},
    "bsd_135_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_135_capitulation_signal},
    "bsd_136_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_136_capitulation_signal},
    "bsd_137_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_137_capitulation_signal},
    "bsd_138_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_138_capitulation_signal},
    "bsd_139_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_139_capitulation_signal},
    "bsd_140_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_140_capitulation_signal},
    "bsd_141_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_141_capitulation_signal},
    "bsd_142_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_142_capitulation_signal},
    "bsd_143_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_143_capitulation_signal},
    "bsd_144_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_144_capitulation_signal},
    "bsd_145_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_145_capitulation_signal},
    "bsd_146_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_146_capitulation_signal},
    "bsd_147_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_147_capitulation_signal},
    "bsd_148_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_148_capitulation_signal},
    "bsd_149_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_149_capitulation_signal},
    "bsd_150_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": bsd_150_capitulation_signal},
}
