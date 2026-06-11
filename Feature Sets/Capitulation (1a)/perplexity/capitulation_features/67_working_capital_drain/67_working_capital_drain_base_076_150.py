"""Generated capitulation features for 67_working_capital_drain: working capital depletion.
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

def wcd_076_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def wcd_077_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _div(x, _s(close))

def wcd_078_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def wcd_079_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def wcd_080_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def wcd_081_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def wcd_082_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def wcd_083_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def wcd_084_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _s(x).pct_change(21)

def wcd_085_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _z(x, 63)

def wcd_086_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(x, y)

def wcd_087_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _div(x - y, y.abs())

def wcd_088_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _rank(x, 504)

def wcd_089_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def wcd_090_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def wcd_091_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(x, _s(close))

def wcd_092_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def wcd_093_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def wcd_094_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def wcd_095_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def wcd_096_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def wcd_097_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def wcd_098_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _s(x).pct_change(126)

def wcd_099_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _z(x, 252)

def wcd_100_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _div(x, y)

def wcd_101_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(x - y, y.abs())

def wcd_102_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _rank(x, 21)

def wcd_103_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def wcd_104_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def wcd_105_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _div(x, _s(close))

def wcd_106_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def wcd_107_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def wcd_108_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def wcd_109_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def wcd_110_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def wcd_111_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def wcd_112_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _s(x).pct_change(504)

def wcd_113_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _z(x, 756)

def wcd_114_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, y)

def wcd_115_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _div(x - y, y.abs())

def wcd_116_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _rank(x, 126)

def wcd_117_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def wcd_118_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def wcd_119_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, _s(close))

def wcd_120_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def wcd_121_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def wcd_122_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def wcd_123_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def wcd_124_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def wcd_125_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def wcd_126_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _s(x).pct_change(21)

def wcd_127_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _z(x, 63)

def wcd_128_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(x, y)

def wcd_129_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _div(x - y, y.abs())

def wcd_130_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _rank(x, 504)

def wcd_131_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def wcd_132_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def wcd_133_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(x, _s(close))

def wcd_134_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def wcd_135_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def wcd_136_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def wcd_137_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def wcd_138_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def wcd_139_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def wcd_140_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _s(x).pct_change(126)

def wcd_141_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _z(x, 252)

def wcd_142_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _div(x, y)

def wcd_143_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(x - y, y.abs())

def wcd_144_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return _rank(x, 21)

def wcd_145_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def wcd_146_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(liabilitiesc, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def wcd_147_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(liabilitiesc, close)
    y = _align_to_close(inventory, close)
    return _div(x, _s(close))

def wcd_148_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(inventory, close)
    y = _align_to_close(receivables, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def wcd_149_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(workingcapital, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def wcd_150_capitulation_signal(close, workingcapital, assetsc, liabilitiesc, inventory, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(assetsc, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

WORKING_CAPITAL_DRAIN_REGISTRY_076_150 = {
    "wcd_076_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_076_capitulation_signal},
    "wcd_077_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_077_capitulation_signal},
    "wcd_078_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_078_capitulation_signal},
    "wcd_079_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_079_capitulation_signal},
    "wcd_080_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_080_capitulation_signal},
    "wcd_081_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_081_capitulation_signal},
    "wcd_082_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_082_capitulation_signal},
    "wcd_083_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_083_capitulation_signal},
    "wcd_084_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_084_capitulation_signal},
    "wcd_085_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_085_capitulation_signal},
    "wcd_086_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_086_capitulation_signal},
    "wcd_087_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_087_capitulation_signal},
    "wcd_088_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_088_capitulation_signal},
    "wcd_089_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_089_capitulation_signal},
    "wcd_090_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_090_capitulation_signal},
    "wcd_091_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_091_capitulation_signal},
    "wcd_092_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_092_capitulation_signal},
    "wcd_093_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_093_capitulation_signal},
    "wcd_094_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_094_capitulation_signal},
    "wcd_095_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_095_capitulation_signal},
    "wcd_096_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_096_capitulation_signal},
    "wcd_097_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_097_capitulation_signal},
    "wcd_098_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_098_capitulation_signal},
    "wcd_099_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_099_capitulation_signal},
    "wcd_100_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_100_capitulation_signal},
    "wcd_101_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_101_capitulation_signal},
    "wcd_102_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_102_capitulation_signal},
    "wcd_103_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_103_capitulation_signal},
    "wcd_104_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_104_capitulation_signal},
    "wcd_105_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_105_capitulation_signal},
    "wcd_106_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_106_capitulation_signal},
    "wcd_107_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_107_capitulation_signal},
    "wcd_108_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_108_capitulation_signal},
    "wcd_109_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_109_capitulation_signal},
    "wcd_110_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_110_capitulation_signal},
    "wcd_111_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_111_capitulation_signal},
    "wcd_112_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_112_capitulation_signal},
    "wcd_113_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_113_capitulation_signal},
    "wcd_114_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_114_capitulation_signal},
    "wcd_115_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_115_capitulation_signal},
    "wcd_116_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_116_capitulation_signal},
    "wcd_117_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_117_capitulation_signal},
    "wcd_118_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_118_capitulation_signal},
    "wcd_119_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_119_capitulation_signal},
    "wcd_120_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_120_capitulation_signal},
    "wcd_121_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_121_capitulation_signal},
    "wcd_122_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_122_capitulation_signal},
    "wcd_123_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_123_capitulation_signal},
    "wcd_124_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_124_capitulation_signal},
    "wcd_125_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_125_capitulation_signal},
    "wcd_126_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_126_capitulation_signal},
    "wcd_127_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_127_capitulation_signal},
    "wcd_128_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_128_capitulation_signal},
    "wcd_129_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_129_capitulation_signal},
    "wcd_130_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_130_capitulation_signal},
    "wcd_131_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_131_capitulation_signal},
    "wcd_132_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_132_capitulation_signal},
    "wcd_133_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_133_capitulation_signal},
    "wcd_134_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_134_capitulation_signal},
    "wcd_135_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_135_capitulation_signal},
    "wcd_136_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_136_capitulation_signal},
    "wcd_137_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_137_capitulation_signal},
    "wcd_138_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_138_capitulation_signal},
    "wcd_139_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_139_capitulation_signal},
    "wcd_140_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_140_capitulation_signal},
    "wcd_141_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_141_capitulation_signal},
    "wcd_142_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_142_capitulation_signal},
    "wcd_143_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_143_capitulation_signal},
    "wcd_144_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_144_capitulation_signal},
    "wcd_145_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_145_capitulation_signal},
    "wcd_146_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_146_capitulation_signal},
    "wcd_147_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_147_capitulation_signal},
    "wcd_148_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_148_capitulation_signal},
    "wcd_149_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_149_capitulation_signal},
    "wcd_150_capitulation_signal": {"inputs": ['close', 'workingcapital', 'assetsc', 'liabilitiesc', 'inventory', 'receivables'], "func": wcd_150_capitulation_signal},
}
