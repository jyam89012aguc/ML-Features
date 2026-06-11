"""Generated capitulation features for 64_liquidity_distress: current/quick ratio collapse.
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

def lqd_076_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def lqd_077_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _div(x, _s(close))

def lqd_078_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def lqd_079_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def lqd_080_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def lqd_081_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def lqd_082_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lqd_083_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def lqd_084_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _s(x).pct_change(21)

def lqd_085_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _z(x, 63)

def lqd_086_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _div(x, y)

def lqd_087_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _div(x - y, y.abs())

def lqd_088_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _rank(x, 504)

def lqd_089_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def lqd_090_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def lqd_091_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _div(x, _s(close))

def lqd_092_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def lqd_093_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def lqd_094_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def lqd_095_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def lqd_096_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lqd_097_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def lqd_098_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _s(x).pct_change(126)

def lqd_099_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _z(x, 252)

def lqd_100_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(x, y)

def lqd_101_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _div(x - y, y.abs())

def lqd_102_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _rank(x, 21)

def lqd_103_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def lqd_104_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def lqd_105_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(x, _s(close))

def lqd_106_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def lqd_107_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def lqd_108_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def lqd_109_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def lqd_110_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lqd_111_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def lqd_112_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _s(x).pct_change(504)

def lqd_113_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _z(x, 756)

def lqd_114_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _div(x, y)

def lqd_115_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(x - y, y.abs())

def lqd_116_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _rank(x, 126)

def lqd_117_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def lqd_118_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def lqd_119_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _div(x, _s(close))

def lqd_120_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def lqd_121_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def lqd_122_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def lqd_123_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def lqd_124_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lqd_125_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def lqd_126_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _s(x).pct_change(21)

def lqd_127_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _z(x, 63)

def lqd_128_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(x, y)

def lqd_129_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _div(x - y, y.abs())

def lqd_130_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _rank(x, 504)

def lqd_131_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def lqd_132_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def lqd_133_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(x, _s(close))

def lqd_134_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def lqd_135_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def lqd_136_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def lqd_137_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def lqd_138_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lqd_139_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def lqd_140_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _s(x).pct_change(126)

def lqd_141_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _z(x, 252)

def lqd_142_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _div(x, y)

def lqd_143_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(x - y, y.abs())

def lqd_144_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return _rank(x, 21)

def lqd_145_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def lqd_146_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(cashneq, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def lqd_147_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(inventory, close)
    return _div(x, _s(close))

def lqd_148_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def lqd_149_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(assetsc, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def lqd_150_capitulation_signal(close, assetsc, liabilitiesc, cashneq, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

LIQUIDITY_DISTRESS_REGISTRY_076_150 = {
    "lqd_076_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_076_capitulation_signal},
    "lqd_077_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_077_capitulation_signal},
    "lqd_078_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_078_capitulation_signal},
    "lqd_079_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_079_capitulation_signal},
    "lqd_080_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_080_capitulation_signal},
    "lqd_081_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_081_capitulation_signal},
    "lqd_082_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_082_capitulation_signal},
    "lqd_083_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_083_capitulation_signal},
    "lqd_084_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_084_capitulation_signal},
    "lqd_085_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_085_capitulation_signal},
    "lqd_086_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_086_capitulation_signal},
    "lqd_087_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_087_capitulation_signal},
    "lqd_088_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_088_capitulation_signal},
    "lqd_089_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_089_capitulation_signal},
    "lqd_090_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_090_capitulation_signal},
    "lqd_091_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_091_capitulation_signal},
    "lqd_092_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_092_capitulation_signal},
    "lqd_093_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_093_capitulation_signal},
    "lqd_094_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_094_capitulation_signal},
    "lqd_095_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_095_capitulation_signal},
    "lqd_096_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_096_capitulation_signal},
    "lqd_097_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_097_capitulation_signal},
    "lqd_098_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_098_capitulation_signal},
    "lqd_099_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_099_capitulation_signal},
    "lqd_100_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_100_capitulation_signal},
    "lqd_101_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_101_capitulation_signal},
    "lqd_102_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_102_capitulation_signal},
    "lqd_103_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_103_capitulation_signal},
    "lqd_104_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_104_capitulation_signal},
    "lqd_105_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_105_capitulation_signal},
    "lqd_106_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_106_capitulation_signal},
    "lqd_107_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_107_capitulation_signal},
    "lqd_108_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_108_capitulation_signal},
    "lqd_109_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_109_capitulation_signal},
    "lqd_110_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_110_capitulation_signal},
    "lqd_111_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_111_capitulation_signal},
    "lqd_112_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_112_capitulation_signal},
    "lqd_113_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_113_capitulation_signal},
    "lqd_114_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_114_capitulation_signal},
    "lqd_115_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_115_capitulation_signal},
    "lqd_116_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_116_capitulation_signal},
    "lqd_117_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_117_capitulation_signal},
    "lqd_118_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_118_capitulation_signal},
    "lqd_119_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_119_capitulation_signal},
    "lqd_120_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_120_capitulation_signal},
    "lqd_121_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_121_capitulation_signal},
    "lqd_122_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_122_capitulation_signal},
    "lqd_123_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_123_capitulation_signal},
    "lqd_124_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_124_capitulation_signal},
    "lqd_125_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_125_capitulation_signal},
    "lqd_126_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_126_capitulation_signal},
    "lqd_127_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_127_capitulation_signal},
    "lqd_128_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_128_capitulation_signal},
    "lqd_129_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_129_capitulation_signal},
    "lqd_130_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_130_capitulation_signal},
    "lqd_131_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_131_capitulation_signal},
    "lqd_132_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_132_capitulation_signal},
    "lqd_133_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_133_capitulation_signal},
    "lqd_134_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_134_capitulation_signal},
    "lqd_135_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_135_capitulation_signal},
    "lqd_136_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_136_capitulation_signal},
    "lqd_137_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_137_capitulation_signal},
    "lqd_138_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_138_capitulation_signal},
    "lqd_139_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_139_capitulation_signal},
    "lqd_140_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_140_capitulation_signal},
    "lqd_141_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_141_capitulation_signal},
    "lqd_142_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_142_capitulation_signal},
    "lqd_143_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_143_capitulation_signal},
    "lqd_144_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_144_capitulation_signal},
    "lqd_145_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_145_capitulation_signal},
    "lqd_146_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_146_capitulation_signal},
    "lqd_147_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_147_capitulation_signal},
    "lqd_148_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_148_capitulation_signal},
    "lqd_149_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_149_capitulation_signal},
    "lqd_150_capitulation_signal": {"inputs": ['close', 'assetsc', 'liabilitiesc', 'cashneq', 'inventory', 'receivables'], "func": lqd_150_capitulation_signal},
}
