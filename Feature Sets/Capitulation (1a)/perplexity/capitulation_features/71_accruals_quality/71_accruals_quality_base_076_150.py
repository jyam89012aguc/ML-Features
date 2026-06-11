"""Generated capitulation features for 71_accruals_quality: accrual/cash divergence.
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

def acq_076_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def acq_077_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, _s(close))

def acq_078_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def acq_079_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def acq_080_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def acq_081_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def acq_082_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def acq_083_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def acq_084_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(21)

def acq_085_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _z(x, 63)

def acq_086_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _div(x, y)

def acq_087_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _div(x - y, y.abs())

def acq_088_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _rank(x, 504)

def acq_089_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def acq_090_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def acq_091_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close))

def acq_092_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def acq_093_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def acq_094_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def acq_095_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def acq_096_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def acq_097_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def acq_098_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _s(x).pct_change(126)

def acq_099_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _z(x, 252)

def acq_100_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _div(x, y)

def acq_101_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _div(x - y, y.abs())

def acq_102_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _rank(x, 21)

def acq_103_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def acq_104_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def acq_105_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _div(x, _s(close))

def acq_106_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def acq_107_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def acq_108_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def acq_109_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def acq_110_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def acq_111_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def acq_112_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _s(x).pct_change(504)

def acq_113_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _z(x, 756)

def acq_114_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _div(x, y)

def acq_115_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _div(x - y, y.abs())

def acq_116_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _rank(x, 126)

def acq_117_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def acq_118_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def acq_119_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close))

def acq_120_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def acq_121_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def acq_122_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def acq_123_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def acq_124_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def acq_125_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def acq_126_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _s(x).pct_change(21)

def acq_127_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _z(x, 63)

def acq_128_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _div(x, y)

def acq_129_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _div(x - y, y.abs())

def acq_130_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _rank(x, 504)

def acq_131_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def acq_132_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def acq_133_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _div(x, _s(close))

def acq_134_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def acq_135_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def acq_136_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def acq_137_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def acq_138_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def acq_139_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def acq_140_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _s(x).pct_change(126)

def acq_141_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _z(x, 252)

def acq_142_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, y)

def acq_143_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _div(x - y, y.abs())

def acq_144_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _rank(x, 21)

def acq_145_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def acq_146_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def acq_147_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, _s(close))

def acq_148_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def acq_149_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def acq_150_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

ACCRUALS_QUALITY_REGISTRY_076_150 = {
    "acq_076_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_076_capitulation_signal},
    "acq_077_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_077_capitulation_signal},
    "acq_078_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_078_capitulation_signal},
    "acq_079_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_079_capitulation_signal},
    "acq_080_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_080_capitulation_signal},
    "acq_081_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_081_capitulation_signal},
    "acq_082_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_082_capitulation_signal},
    "acq_083_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_083_capitulation_signal},
    "acq_084_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_084_capitulation_signal},
    "acq_085_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_085_capitulation_signal},
    "acq_086_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_086_capitulation_signal},
    "acq_087_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_087_capitulation_signal},
    "acq_088_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_088_capitulation_signal},
    "acq_089_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_089_capitulation_signal},
    "acq_090_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_090_capitulation_signal},
    "acq_091_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_091_capitulation_signal},
    "acq_092_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_092_capitulation_signal},
    "acq_093_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_093_capitulation_signal},
    "acq_094_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_094_capitulation_signal},
    "acq_095_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_095_capitulation_signal},
    "acq_096_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_096_capitulation_signal},
    "acq_097_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_097_capitulation_signal},
    "acq_098_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_098_capitulation_signal},
    "acq_099_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_099_capitulation_signal},
    "acq_100_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_100_capitulation_signal},
    "acq_101_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_101_capitulation_signal},
    "acq_102_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_102_capitulation_signal},
    "acq_103_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_103_capitulation_signal},
    "acq_104_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_104_capitulation_signal},
    "acq_105_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_105_capitulation_signal},
    "acq_106_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_106_capitulation_signal},
    "acq_107_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_107_capitulation_signal},
    "acq_108_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_108_capitulation_signal},
    "acq_109_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_109_capitulation_signal},
    "acq_110_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_110_capitulation_signal},
    "acq_111_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_111_capitulation_signal},
    "acq_112_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_112_capitulation_signal},
    "acq_113_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_113_capitulation_signal},
    "acq_114_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_114_capitulation_signal},
    "acq_115_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_115_capitulation_signal},
    "acq_116_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_116_capitulation_signal},
    "acq_117_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_117_capitulation_signal},
    "acq_118_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_118_capitulation_signal},
    "acq_119_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_119_capitulation_signal},
    "acq_120_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_120_capitulation_signal},
    "acq_121_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_121_capitulation_signal},
    "acq_122_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_122_capitulation_signal},
    "acq_123_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_123_capitulation_signal},
    "acq_124_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_124_capitulation_signal},
    "acq_125_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_125_capitulation_signal},
    "acq_126_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_126_capitulation_signal},
    "acq_127_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_127_capitulation_signal},
    "acq_128_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_128_capitulation_signal},
    "acq_129_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_129_capitulation_signal},
    "acq_130_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_130_capitulation_signal},
    "acq_131_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_131_capitulation_signal},
    "acq_132_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_132_capitulation_signal},
    "acq_133_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_133_capitulation_signal},
    "acq_134_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_134_capitulation_signal},
    "acq_135_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_135_capitulation_signal},
    "acq_136_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_136_capitulation_signal},
    "acq_137_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_137_capitulation_signal},
    "acq_138_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_138_capitulation_signal},
    "acq_139_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_139_capitulation_signal},
    "acq_140_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_140_capitulation_signal},
    "acq_141_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_141_capitulation_signal},
    "acq_142_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_142_capitulation_signal},
    "acq_143_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_143_capitulation_signal},
    "acq_144_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_144_capitulation_signal},
    "acq_145_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_145_capitulation_signal},
    "acq_146_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_146_capitulation_signal},
    "acq_147_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_147_capitulation_signal},
    "acq_148_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_148_capitulation_signal},
    "acq_149_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_149_capitulation_signal},
    "acq_150_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_150_capitulation_signal},
}
