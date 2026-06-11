"""Generated capitulation features for 61_revenue_deterioration: revenue contraction.
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

def rvd_076_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def rvd_077_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close))

def rvd_078_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def rvd_079_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def rvd_080_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def rvd_081_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def rvd_082_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def rvd_083_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def rvd_084_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(21)

def rvd_085_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _z(x, 63)

def rvd_086_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _div(x, y)

def rvd_087_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _div(x - y, y.abs())

def rvd_088_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _rank(x, 504)

def rvd_089_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def rvd_090_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def rvd_091_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close))

def rvd_092_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def rvd_093_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def rvd_094_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def rvd_095_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def rvd_096_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def rvd_097_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def rvd_098_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _s(x).pct_change(126)

def rvd_099_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _z(x, 252)

def rvd_100_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(x, y)

def rvd_101_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _div(x - y, y.abs())

def rvd_102_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _rank(x, 21)

def rvd_103_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def rvd_104_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def rvd_105_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(x, _s(close))

def rvd_106_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def rvd_107_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def rvd_108_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def rvd_109_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def rvd_110_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def rvd_111_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def rvd_112_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _s(x).pct_change(504)

def rvd_113_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _z(x, 756)

def rvd_114_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _div(x, y)

def rvd_115_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(x - y, y.abs())

def rvd_116_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _rank(x, 126)

def rvd_117_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def rvd_118_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def rvd_119_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close))

def rvd_120_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def rvd_121_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def rvd_122_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def rvd_123_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def rvd_124_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def rvd_125_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def rvd_126_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(21)

def rvd_127_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _z(x, 63)

def rvd_128_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _div(x, y)

def rvd_129_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _div(x - y, y.abs())

def rvd_130_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _rank(x, 504)

def rvd_131_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def rvd_132_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def rvd_133_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _div(x, _s(close))

def rvd_134_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def rvd_135_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def rvd_136_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def rvd_137_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def rvd_138_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def rvd_139_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def rvd_140_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _s(x).pct_change(126)

def rvd_141_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _z(x, 252)

def rvd_142_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _div(x, y)

def rvd_143_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _div(x - y, y.abs())

def rvd_144_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return _rank(x, 21)

def rvd_145_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def rvd_146_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(netinc, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def rvd_147_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close))

def rvd_148_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(receivables, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def rvd_149_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(revenue, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def rvd_150_capitulation_signal(close, revenue, grossprofit, netinc, assets, receivables):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

REVENUE_DETERIORATION_REGISTRY_076_150 = {
    "rvd_076_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_076_capitulation_signal},
    "rvd_077_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_077_capitulation_signal},
    "rvd_078_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_078_capitulation_signal},
    "rvd_079_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_079_capitulation_signal},
    "rvd_080_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_080_capitulation_signal},
    "rvd_081_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_081_capitulation_signal},
    "rvd_082_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_082_capitulation_signal},
    "rvd_083_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_083_capitulation_signal},
    "rvd_084_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_084_capitulation_signal},
    "rvd_085_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_085_capitulation_signal},
    "rvd_086_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_086_capitulation_signal},
    "rvd_087_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_087_capitulation_signal},
    "rvd_088_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_088_capitulation_signal},
    "rvd_089_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_089_capitulation_signal},
    "rvd_090_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_090_capitulation_signal},
    "rvd_091_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_091_capitulation_signal},
    "rvd_092_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_092_capitulation_signal},
    "rvd_093_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_093_capitulation_signal},
    "rvd_094_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_094_capitulation_signal},
    "rvd_095_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_095_capitulation_signal},
    "rvd_096_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_096_capitulation_signal},
    "rvd_097_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_097_capitulation_signal},
    "rvd_098_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_098_capitulation_signal},
    "rvd_099_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_099_capitulation_signal},
    "rvd_100_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_100_capitulation_signal},
    "rvd_101_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_101_capitulation_signal},
    "rvd_102_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_102_capitulation_signal},
    "rvd_103_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_103_capitulation_signal},
    "rvd_104_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_104_capitulation_signal},
    "rvd_105_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_105_capitulation_signal},
    "rvd_106_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_106_capitulation_signal},
    "rvd_107_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_107_capitulation_signal},
    "rvd_108_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_108_capitulation_signal},
    "rvd_109_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_109_capitulation_signal},
    "rvd_110_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_110_capitulation_signal},
    "rvd_111_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_111_capitulation_signal},
    "rvd_112_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_112_capitulation_signal},
    "rvd_113_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_113_capitulation_signal},
    "rvd_114_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_114_capitulation_signal},
    "rvd_115_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_115_capitulation_signal},
    "rvd_116_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_116_capitulation_signal},
    "rvd_117_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_117_capitulation_signal},
    "rvd_118_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_118_capitulation_signal},
    "rvd_119_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_119_capitulation_signal},
    "rvd_120_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_120_capitulation_signal},
    "rvd_121_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_121_capitulation_signal},
    "rvd_122_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_122_capitulation_signal},
    "rvd_123_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_123_capitulation_signal},
    "rvd_124_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_124_capitulation_signal},
    "rvd_125_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_125_capitulation_signal},
    "rvd_126_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_126_capitulation_signal},
    "rvd_127_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_127_capitulation_signal},
    "rvd_128_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_128_capitulation_signal},
    "rvd_129_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_129_capitulation_signal},
    "rvd_130_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_130_capitulation_signal},
    "rvd_131_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_131_capitulation_signal},
    "rvd_132_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_132_capitulation_signal},
    "rvd_133_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_133_capitulation_signal},
    "rvd_134_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_134_capitulation_signal},
    "rvd_135_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_135_capitulation_signal},
    "rvd_136_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_136_capitulation_signal},
    "rvd_137_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_137_capitulation_signal},
    "rvd_138_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_138_capitulation_signal},
    "rvd_139_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_139_capitulation_signal},
    "rvd_140_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_140_capitulation_signal},
    "rvd_141_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_141_capitulation_signal},
    "rvd_142_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_142_capitulation_signal},
    "rvd_143_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_143_capitulation_signal},
    "rvd_144_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_144_capitulation_signal},
    "rvd_145_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_145_capitulation_signal},
    "rvd_146_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_146_capitulation_signal},
    "rvd_147_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_147_capitulation_signal},
    "rvd_148_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_148_capitulation_signal},
    "rvd_149_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_149_capitulation_signal},
    "rvd_150_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'netinc', 'assets', 'receivables'], "func": rvd_150_capitulation_signal},
}
