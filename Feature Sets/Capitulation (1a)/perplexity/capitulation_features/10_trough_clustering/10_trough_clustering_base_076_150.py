"""Generated capitulation features for 10_trough_clustering: density of local minima, repeated bottoms.
All windows look backward only. Trading-day constants: 252/year, 63/quarter, 21/month, 5/week.
"""
import numpy as np
import pandas as pd


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

def tcl_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def tcl_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def tcl_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def tcl_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def tcl_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def tcl_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def tcl_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def tcl_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def tcl_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def tcl_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def tcl_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tcl_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def tcl_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def tcl_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def tcl_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def tcl_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def tcl_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def tcl_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def tcl_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def tcl_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def tcl_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def tcl_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def tcl_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def tcl_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def tcl_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def tcl_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tcl_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def tcl_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def tcl_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def tcl_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def tcl_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def tcl_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def tcl_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def tcl_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def tcl_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def tcl_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def tcl_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def tcl_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def tcl_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def tcl_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def tcl_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tcl_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def tcl_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def tcl_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def tcl_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def tcl_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def tcl_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def tcl_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def tcl_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def tcl_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def tcl_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def tcl_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def tcl_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def tcl_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def tcl_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def tcl_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tcl_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def tcl_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def tcl_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def tcl_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def tcl_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def tcl_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def tcl_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

TROUGH_CLUSTERING_REGISTRY_076_150 = {
    "tcl_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_076_capitulation_signal},
    "tcl_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_077_capitulation_signal},
    "tcl_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_078_capitulation_signal},
    "tcl_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_079_capitulation_signal},
    "tcl_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_080_capitulation_signal},
    "tcl_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_081_capitulation_signal},
    "tcl_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_082_capitulation_signal},
    "tcl_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_083_capitulation_signal},
    "tcl_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_084_capitulation_signal},
    "tcl_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_085_capitulation_signal},
    "tcl_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_086_capitulation_signal},
    "tcl_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_087_capitulation_signal},
    "tcl_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_088_capitulation_signal},
    "tcl_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_089_capitulation_signal},
    "tcl_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_090_capitulation_signal},
    "tcl_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_091_capitulation_signal},
    "tcl_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_092_capitulation_signal},
    "tcl_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_093_capitulation_signal},
    "tcl_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_094_capitulation_signal},
    "tcl_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_095_capitulation_signal},
    "tcl_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_096_capitulation_signal},
    "tcl_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_097_capitulation_signal},
    "tcl_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_098_capitulation_signal},
    "tcl_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_099_capitulation_signal},
    "tcl_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_100_capitulation_signal},
    "tcl_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_101_capitulation_signal},
    "tcl_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_102_capitulation_signal},
    "tcl_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_103_capitulation_signal},
    "tcl_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_104_capitulation_signal},
    "tcl_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_105_capitulation_signal},
    "tcl_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_106_capitulation_signal},
    "tcl_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_107_capitulation_signal},
    "tcl_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_108_capitulation_signal},
    "tcl_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_109_capitulation_signal},
    "tcl_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_110_capitulation_signal},
    "tcl_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_111_capitulation_signal},
    "tcl_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_112_capitulation_signal},
    "tcl_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_113_capitulation_signal},
    "tcl_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_114_capitulation_signal},
    "tcl_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_115_capitulation_signal},
    "tcl_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_116_capitulation_signal},
    "tcl_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_117_capitulation_signal},
    "tcl_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_118_capitulation_signal},
    "tcl_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_119_capitulation_signal},
    "tcl_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_120_capitulation_signal},
    "tcl_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_121_capitulation_signal},
    "tcl_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_122_capitulation_signal},
    "tcl_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_123_capitulation_signal},
    "tcl_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_124_capitulation_signal},
    "tcl_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_125_capitulation_signal},
    "tcl_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_126_capitulation_signal},
    "tcl_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_127_capitulation_signal},
    "tcl_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_128_capitulation_signal},
    "tcl_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_129_capitulation_signal},
    "tcl_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_130_capitulation_signal},
    "tcl_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_131_capitulation_signal},
    "tcl_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_132_capitulation_signal},
    "tcl_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_133_capitulation_signal},
    "tcl_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_134_capitulation_signal},
    "tcl_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_135_capitulation_signal},
    "tcl_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_136_capitulation_signal},
    "tcl_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_137_capitulation_signal},
    "tcl_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_138_capitulation_signal},
    "tcl_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_139_capitulation_signal},
    "tcl_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_140_capitulation_signal},
    "tcl_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_141_capitulation_signal},
    "tcl_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_142_capitulation_signal},
    "tcl_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_143_capitulation_signal},
    "tcl_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_144_capitulation_signal},
    "tcl_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_145_capitulation_signal},
    "tcl_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_146_capitulation_signal},
    "tcl_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_147_capitulation_signal},
    "tcl_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_148_capitulation_signal},
    "tcl_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_149_capitulation_signal},
    "tcl_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_150_capitulation_signal},
}
