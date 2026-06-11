"""Generated capitulation features for 72_solvency_scores: solvency composites.
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

def slv_076_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def slv_077_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close))

def slv_078_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def slv_079_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(retainedearnings, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def slv_080_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def slv_081_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(ebit, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def slv_082_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def slv_083_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def slv_084_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).pct_change(21)

def slv_085_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(workingcapital, close)
    return _z(x, 63)

def slv_086_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(retainedearnings, close)
    return _div(x, y)

def slv_087_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(ebit, close)
    return _div(x - y, y.abs())

def slv_088_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(ebit, close)
    y = _align_to_close(marketcap, close)
    return _rank(x, 504)

def slv_089_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(revenue, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def slv_090_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def slv_091_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close))

def slv_092_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def slv_093_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(retainedearnings, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def slv_094_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def slv_095_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(ebit, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def slv_096_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def slv_097_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def slv_098_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).pct_change(126)

def slv_099_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(workingcapital, close)
    return _z(x, 252)

def slv_100_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(retainedearnings, close)
    return _div(x, y)

def slv_101_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(ebit, close)
    return _div(x - y, y.abs())

def slv_102_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(ebit, close)
    y = _align_to_close(marketcap, close)
    return _rank(x, 21)

def slv_103_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(revenue, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def slv_104_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def slv_105_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close))

def slv_106_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def slv_107_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(retainedearnings, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def slv_108_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def slv_109_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(ebit, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def slv_110_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def slv_111_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def slv_112_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).pct_change(504)

def slv_113_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(workingcapital, close)
    return _z(x, 756)

def slv_114_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(retainedearnings, close)
    return _div(x, y)

def slv_115_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(ebit, close)
    return _div(x - y, y.abs())

def slv_116_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(ebit, close)
    y = _align_to_close(marketcap, close)
    return _rank(x, 126)

def slv_117_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(revenue, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def slv_118_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def slv_119_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close))

def slv_120_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def slv_121_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(retainedearnings, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def slv_122_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def slv_123_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(ebit, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def slv_124_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def slv_125_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def slv_126_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).pct_change(21)

def slv_127_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(workingcapital, close)
    return _z(x, 63)

def slv_128_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(retainedearnings, close)
    return _div(x, y)

def slv_129_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(ebit, close)
    return _div(x - y, y.abs())

def slv_130_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(ebit, close)
    y = _align_to_close(marketcap, close)
    return _rank(x, 504)

def slv_131_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(revenue, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def slv_132_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def slv_133_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close))

def slv_134_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def slv_135_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(retainedearnings, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def slv_136_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def slv_137_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(ebit, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def slv_138_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def slv_139_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def slv_140_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).pct_change(126)

def slv_141_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(workingcapital, close)
    return _z(x, 252)

def slv_142_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(retainedearnings, close)
    return _div(x, y)

def slv_143_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(ebit, close)
    return _div(x - y, y.abs())

def slv_144_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(ebit, close)
    y = _align_to_close(marketcap, close)
    return _rank(x, 21)

def slv_145_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(revenue, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def slv_146_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def slv_147_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close))

def slv_148_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def slv_149_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(retainedearnings, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def slv_150_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

SOLVENCY_SCORES_REGISTRY_076_150 = {
    "slv_076_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_076_capitulation_signal},
    "slv_077_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_077_capitulation_signal},
    "slv_078_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_078_capitulation_signal},
    "slv_079_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_079_capitulation_signal},
    "slv_080_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_080_capitulation_signal},
    "slv_081_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_081_capitulation_signal},
    "slv_082_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_082_capitulation_signal},
    "slv_083_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_083_capitulation_signal},
    "slv_084_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_084_capitulation_signal},
    "slv_085_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_085_capitulation_signal},
    "slv_086_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_086_capitulation_signal},
    "slv_087_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_087_capitulation_signal},
    "slv_088_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_088_capitulation_signal},
    "slv_089_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_089_capitulation_signal},
    "slv_090_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_090_capitulation_signal},
    "slv_091_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_091_capitulation_signal},
    "slv_092_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_092_capitulation_signal},
    "slv_093_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_093_capitulation_signal},
    "slv_094_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_094_capitulation_signal},
    "slv_095_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_095_capitulation_signal},
    "slv_096_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_096_capitulation_signal},
    "slv_097_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_097_capitulation_signal},
    "slv_098_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_098_capitulation_signal},
    "slv_099_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_099_capitulation_signal},
    "slv_100_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_100_capitulation_signal},
    "slv_101_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_101_capitulation_signal},
    "slv_102_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_102_capitulation_signal},
    "slv_103_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_103_capitulation_signal},
    "slv_104_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_104_capitulation_signal},
    "slv_105_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_105_capitulation_signal},
    "slv_106_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_106_capitulation_signal},
    "slv_107_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_107_capitulation_signal},
    "slv_108_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_108_capitulation_signal},
    "slv_109_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_109_capitulation_signal},
    "slv_110_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_110_capitulation_signal},
    "slv_111_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_111_capitulation_signal},
    "slv_112_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_112_capitulation_signal},
    "slv_113_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_113_capitulation_signal},
    "slv_114_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_114_capitulation_signal},
    "slv_115_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_115_capitulation_signal},
    "slv_116_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_116_capitulation_signal},
    "slv_117_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_117_capitulation_signal},
    "slv_118_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_118_capitulation_signal},
    "slv_119_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_119_capitulation_signal},
    "slv_120_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_120_capitulation_signal},
    "slv_121_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_121_capitulation_signal},
    "slv_122_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_122_capitulation_signal},
    "slv_123_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_123_capitulation_signal},
    "slv_124_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_124_capitulation_signal},
    "slv_125_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_125_capitulation_signal},
    "slv_126_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_126_capitulation_signal},
    "slv_127_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_127_capitulation_signal},
    "slv_128_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_128_capitulation_signal},
    "slv_129_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_129_capitulation_signal},
    "slv_130_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_130_capitulation_signal},
    "slv_131_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_131_capitulation_signal},
    "slv_132_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_132_capitulation_signal},
    "slv_133_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_133_capitulation_signal},
    "slv_134_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_134_capitulation_signal},
    "slv_135_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_135_capitulation_signal},
    "slv_136_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_136_capitulation_signal},
    "slv_137_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_137_capitulation_signal},
    "slv_138_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_138_capitulation_signal},
    "slv_139_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_139_capitulation_signal},
    "slv_140_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_140_capitulation_signal},
    "slv_141_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_141_capitulation_signal},
    "slv_142_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_142_capitulation_signal},
    "slv_143_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_143_capitulation_signal},
    "slv_144_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_144_capitulation_signal},
    "slv_145_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_145_capitulation_signal},
    "slv_146_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_146_capitulation_signal},
    "slv_147_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_147_capitulation_signal},
    "slv_148_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_148_capitulation_signal},
    "slv_149_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_149_capitulation_signal},
    "slv_150_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_150_capitulation_signal},
}
