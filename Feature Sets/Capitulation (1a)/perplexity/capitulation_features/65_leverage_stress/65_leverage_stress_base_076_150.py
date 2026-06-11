"""Generated capitulation features for 65_leverage_stress: debt escalation.
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

def lvs_076_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def lvs_077_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close))

def lvs_078_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def lvs_079_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def lvs_080_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def lvs_081_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def lvs_082_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lvs_083_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def lvs_084_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _s(x).pct_change(21)

def lvs_085_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _z(x, 63)

def lvs_086_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _div(x, y)

def lvs_087_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x - y, y.abs())

def lvs_088_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _rank(x, 504)

def lvs_089_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def lvs_090_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def lvs_091_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close))

def lvs_092_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def lvs_093_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def lvs_094_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def lvs_095_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def lvs_096_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lvs_097_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def lvs_098_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _s(x).pct_change(126)

def lvs_099_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _z(x, 252)

def lvs_100_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _div(x, y)

def lvs_101_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _div(x - y, y.abs())

def lvs_102_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _rank(x, 21)

def lvs_103_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def lvs_104_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def lvs_105_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _div(x, _s(close))

def lvs_106_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def lvs_107_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def lvs_108_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def lvs_109_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def lvs_110_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lvs_111_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def lvs_112_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).pct_change(504)

def lvs_113_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _z(x, 756)

def lvs_114_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _div(x, y)

def lvs_115_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _div(x - y, y.abs())

def lvs_116_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _rank(x, 126)

def lvs_117_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def lvs_118_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def lvs_119_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _div(x, _s(close))

def lvs_120_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def lvs_121_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def lvs_122_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def lvs_123_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def lvs_124_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lvs_125_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def lvs_126_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _s(x).pct_change(21)

def lvs_127_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _z(x, 63)

def lvs_128_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _div(x, y)

def lvs_129_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _div(x - y, y.abs())

def lvs_130_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _rank(x, 504)

def lvs_131_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def lvs_132_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def lvs_133_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close))

def lvs_134_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def lvs_135_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def lvs_136_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def lvs_137_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def lvs_138_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lvs_139_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def lvs_140_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _s(x).pct_change(126)

def lvs_141_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _z(x, 252)

def lvs_142_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, y)

def lvs_143_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _div(x - y, y.abs())

def lvs_144_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _rank(x, 21)

def lvs_145_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def lvs_146_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def lvs_147_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close))

def lvs_148_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def lvs_149_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def lvs_150_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

LEVERAGE_STRESS_REGISTRY_076_150 = {
    "lvs_076_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_076_capitulation_signal},
    "lvs_077_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_077_capitulation_signal},
    "lvs_078_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_078_capitulation_signal},
    "lvs_079_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_079_capitulation_signal},
    "lvs_080_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_080_capitulation_signal},
    "lvs_081_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_081_capitulation_signal},
    "lvs_082_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_082_capitulation_signal},
    "lvs_083_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_083_capitulation_signal},
    "lvs_084_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_084_capitulation_signal},
    "lvs_085_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_085_capitulation_signal},
    "lvs_086_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_086_capitulation_signal},
    "lvs_087_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_087_capitulation_signal},
    "lvs_088_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_088_capitulation_signal},
    "lvs_089_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_089_capitulation_signal},
    "lvs_090_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_090_capitulation_signal},
    "lvs_091_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_091_capitulation_signal},
    "lvs_092_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_092_capitulation_signal},
    "lvs_093_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_093_capitulation_signal},
    "lvs_094_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_094_capitulation_signal},
    "lvs_095_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_095_capitulation_signal},
    "lvs_096_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_096_capitulation_signal},
    "lvs_097_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_097_capitulation_signal},
    "lvs_098_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_098_capitulation_signal},
    "lvs_099_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_099_capitulation_signal},
    "lvs_100_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_100_capitulation_signal},
    "lvs_101_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_101_capitulation_signal},
    "lvs_102_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_102_capitulation_signal},
    "lvs_103_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_103_capitulation_signal},
    "lvs_104_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_104_capitulation_signal},
    "lvs_105_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_105_capitulation_signal},
    "lvs_106_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_106_capitulation_signal},
    "lvs_107_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_107_capitulation_signal},
    "lvs_108_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_108_capitulation_signal},
    "lvs_109_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_109_capitulation_signal},
    "lvs_110_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_110_capitulation_signal},
    "lvs_111_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_111_capitulation_signal},
    "lvs_112_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_112_capitulation_signal},
    "lvs_113_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_113_capitulation_signal},
    "lvs_114_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_114_capitulation_signal},
    "lvs_115_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_115_capitulation_signal},
    "lvs_116_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_116_capitulation_signal},
    "lvs_117_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_117_capitulation_signal},
    "lvs_118_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_118_capitulation_signal},
    "lvs_119_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_119_capitulation_signal},
    "lvs_120_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_120_capitulation_signal},
    "lvs_121_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_121_capitulation_signal},
    "lvs_122_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_122_capitulation_signal},
    "lvs_123_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_123_capitulation_signal},
    "lvs_124_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_124_capitulation_signal},
    "lvs_125_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_125_capitulation_signal},
    "lvs_126_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_126_capitulation_signal},
    "lvs_127_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_127_capitulation_signal},
    "lvs_128_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_128_capitulation_signal},
    "lvs_129_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_129_capitulation_signal},
    "lvs_130_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_130_capitulation_signal},
    "lvs_131_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_131_capitulation_signal},
    "lvs_132_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_132_capitulation_signal},
    "lvs_133_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_133_capitulation_signal},
    "lvs_134_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_134_capitulation_signal},
    "lvs_135_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_135_capitulation_signal},
    "lvs_136_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_136_capitulation_signal},
    "lvs_137_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_137_capitulation_signal},
    "lvs_138_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_138_capitulation_signal},
    "lvs_139_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_139_capitulation_signal},
    "lvs_140_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_140_capitulation_signal},
    "lvs_141_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_141_capitulation_signal},
    "lvs_142_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_142_capitulation_signal},
    "lvs_143_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_143_capitulation_signal},
    "lvs_144_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_144_capitulation_signal},
    "lvs_145_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_145_capitulation_signal},
    "lvs_146_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_146_capitulation_signal},
    "lvs_147_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_147_capitulation_signal},
    "lvs_148_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_148_capitulation_signal},
    "lvs_149_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_149_capitulation_signal},
    "lvs_150_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_150_capitulation_signal},
}
