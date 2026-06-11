"""Generated capitulation features for 80_yield_distress: yield spikes.
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

def yld_076_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def yld_077_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close))

def yld_078_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def yld_079_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def yld_080_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def yld_081_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def yld_082_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def yld_083_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def yld_084_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _s(x).pct_change(21)

def yld_085_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _z(x, 63)

def yld_086_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _div(x, y)

def yld_087_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _div(x - y, y.abs())

def yld_088_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _rank(x, 504)

def yld_089_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def yld_090_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def yld_091_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _div(x, _s(close))

def yld_092_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def yld_093_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def yld_094_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def yld_095_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def yld_096_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def yld_097_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def yld_098_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(126)

def yld_099_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _z(x, 252)

def yld_100_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _div(x, y)

def yld_101_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _div(x - y, y.abs())

def yld_102_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _rank(x, 21)

def yld_103_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def yld_104_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def yld_105_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _div(x, _s(close))

def yld_106_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def yld_107_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def yld_108_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def yld_109_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def yld_110_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def yld_111_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def yld_112_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(504)

def yld_113_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _z(x, 756)

def yld_114_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _div(x, y)

def yld_115_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _div(x - y, y.abs())

def yld_116_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _rank(x, 126)

def yld_117_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def yld_118_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def yld_119_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _div(x, _s(close))

def yld_120_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def yld_121_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def yld_122_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def yld_123_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def yld_124_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def yld_125_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def yld_126_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _s(x).pct_change(21)

def yld_127_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _z(x, 63)

def yld_128_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _div(x, y)

def yld_129_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _div(x - y, y.abs())

def yld_130_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _rank(x, 504)

def yld_131_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def yld_132_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def yld_133_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _div(x, _s(close))

def yld_134_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def yld_135_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def yld_136_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def yld_137_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def yld_138_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def yld_139_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def yld_140_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _s(x).pct_change(126)

def yld_141_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _z(x, 252)

def yld_142_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _div(x, y)

def yld_143_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _div(x - y, y.abs())

def yld_144_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _rank(x, 21)

def yld_145_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def yld_146_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def yld_147_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close))

def yld_148_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def yld_149_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def yld_150_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

YIELD_DISTRESS_REGISTRY_076_150 = {
    "yld_076_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_076_capitulation_signal},
    "yld_077_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_077_capitulation_signal},
    "yld_078_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_078_capitulation_signal},
    "yld_079_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_079_capitulation_signal},
    "yld_080_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_080_capitulation_signal},
    "yld_081_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_081_capitulation_signal},
    "yld_082_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_082_capitulation_signal},
    "yld_083_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_083_capitulation_signal},
    "yld_084_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_084_capitulation_signal},
    "yld_085_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_085_capitulation_signal},
    "yld_086_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_086_capitulation_signal},
    "yld_087_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_087_capitulation_signal},
    "yld_088_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_088_capitulation_signal},
    "yld_089_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_089_capitulation_signal},
    "yld_090_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_090_capitulation_signal},
    "yld_091_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_091_capitulation_signal},
    "yld_092_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_092_capitulation_signal},
    "yld_093_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_093_capitulation_signal},
    "yld_094_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_094_capitulation_signal},
    "yld_095_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_095_capitulation_signal},
    "yld_096_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_096_capitulation_signal},
    "yld_097_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_097_capitulation_signal},
    "yld_098_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_098_capitulation_signal},
    "yld_099_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_099_capitulation_signal},
    "yld_100_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_100_capitulation_signal},
    "yld_101_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_101_capitulation_signal},
    "yld_102_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_102_capitulation_signal},
    "yld_103_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_103_capitulation_signal},
    "yld_104_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_104_capitulation_signal},
    "yld_105_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_105_capitulation_signal},
    "yld_106_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_106_capitulation_signal},
    "yld_107_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_107_capitulation_signal},
    "yld_108_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_108_capitulation_signal},
    "yld_109_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_109_capitulation_signal},
    "yld_110_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_110_capitulation_signal},
    "yld_111_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_111_capitulation_signal},
    "yld_112_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_112_capitulation_signal},
    "yld_113_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_113_capitulation_signal},
    "yld_114_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_114_capitulation_signal},
    "yld_115_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_115_capitulation_signal},
    "yld_116_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_116_capitulation_signal},
    "yld_117_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_117_capitulation_signal},
    "yld_118_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_118_capitulation_signal},
    "yld_119_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_119_capitulation_signal},
    "yld_120_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_120_capitulation_signal},
    "yld_121_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_121_capitulation_signal},
    "yld_122_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_122_capitulation_signal},
    "yld_123_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_123_capitulation_signal},
    "yld_124_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_124_capitulation_signal},
    "yld_125_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_125_capitulation_signal},
    "yld_126_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_126_capitulation_signal},
    "yld_127_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_127_capitulation_signal},
    "yld_128_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_128_capitulation_signal},
    "yld_129_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_129_capitulation_signal},
    "yld_130_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_130_capitulation_signal},
    "yld_131_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_131_capitulation_signal},
    "yld_132_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_132_capitulation_signal},
    "yld_133_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_133_capitulation_signal},
    "yld_134_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_134_capitulation_signal},
    "yld_135_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_135_capitulation_signal},
    "yld_136_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_136_capitulation_signal},
    "yld_137_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_137_capitulation_signal},
    "yld_138_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_138_capitulation_signal},
    "yld_139_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_139_capitulation_signal},
    "yld_140_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_140_capitulation_signal},
    "yld_141_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_141_capitulation_signal},
    "yld_142_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_142_capitulation_signal},
    "yld_143_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_143_capitulation_signal},
    "yld_144_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_144_capitulation_signal},
    "yld_145_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_145_capitulation_signal},
    "yld_146_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_146_capitulation_signal},
    "yld_147_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_147_capitulation_signal},
    "yld_148_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_148_capitulation_signal},
    "yld_149_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_149_capitulation_signal},
    "yld_150_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_150_capitulation_signal},
}
