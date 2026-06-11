"""Generated capitulation features for 46_gap_structure: overnight gap frequency.
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

def gap_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def gap_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def gap_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def gap_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def gap_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def gap_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def gap_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def gap_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def gap_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def gap_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def gap_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def gap_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def gap_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def gap_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def gap_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def gap_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def gap_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def gap_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def gap_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def gap_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def gap_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def gap_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def gap_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def gap_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def gap_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def gap_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def gap_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def gap_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def gap_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def gap_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def gap_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def gap_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def gap_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def gap_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def gap_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def gap_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def gap_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def gap_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def gap_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def gap_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def gap_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def gap_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def gap_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def gap_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def gap_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def gap_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def gap_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def gap_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def gap_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def gap_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def gap_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def gap_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def gap_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def gap_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def gap_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def gap_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def gap_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def gap_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def gap_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def gap_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def gap_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def gap_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def gap_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def gap_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def gap_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def gap_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def gap_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def gap_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def gap_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def gap_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def gap_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def gap_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def gap_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def gap_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def gap_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

GAP_STRUCTURE_REGISTRY_076_150 = {
    "gap_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_076_capitulation_signal},
    "gap_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_077_capitulation_signal},
    "gap_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_078_capitulation_signal},
    "gap_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_079_capitulation_signal},
    "gap_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_080_capitulation_signal},
    "gap_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_081_capitulation_signal},
    "gap_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_082_capitulation_signal},
    "gap_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_083_capitulation_signal},
    "gap_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_084_capitulation_signal},
    "gap_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_085_capitulation_signal},
    "gap_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_086_capitulation_signal},
    "gap_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_087_capitulation_signal},
    "gap_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_088_capitulation_signal},
    "gap_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_089_capitulation_signal},
    "gap_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_090_capitulation_signal},
    "gap_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_091_capitulation_signal},
    "gap_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_092_capitulation_signal},
    "gap_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_093_capitulation_signal},
    "gap_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_094_capitulation_signal},
    "gap_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_095_capitulation_signal},
    "gap_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_096_capitulation_signal},
    "gap_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_097_capitulation_signal},
    "gap_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_098_capitulation_signal},
    "gap_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_099_capitulation_signal},
    "gap_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_100_capitulation_signal},
    "gap_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_101_capitulation_signal},
    "gap_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_102_capitulation_signal},
    "gap_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_103_capitulation_signal},
    "gap_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_104_capitulation_signal},
    "gap_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_105_capitulation_signal},
    "gap_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_106_capitulation_signal},
    "gap_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_107_capitulation_signal},
    "gap_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_108_capitulation_signal},
    "gap_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_109_capitulation_signal},
    "gap_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_110_capitulation_signal},
    "gap_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_111_capitulation_signal},
    "gap_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_112_capitulation_signal},
    "gap_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_113_capitulation_signal},
    "gap_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_114_capitulation_signal},
    "gap_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_115_capitulation_signal},
    "gap_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_116_capitulation_signal},
    "gap_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_117_capitulation_signal},
    "gap_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_118_capitulation_signal},
    "gap_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_119_capitulation_signal},
    "gap_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_120_capitulation_signal},
    "gap_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_121_capitulation_signal},
    "gap_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_122_capitulation_signal},
    "gap_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_123_capitulation_signal},
    "gap_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_124_capitulation_signal},
    "gap_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_125_capitulation_signal},
    "gap_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_126_capitulation_signal},
    "gap_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_127_capitulation_signal},
    "gap_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_128_capitulation_signal},
    "gap_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_129_capitulation_signal},
    "gap_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_130_capitulation_signal},
    "gap_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_131_capitulation_signal},
    "gap_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_132_capitulation_signal},
    "gap_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_133_capitulation_signal},
    "gap_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_134_capitulation_signal},
    "gap_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_135_capitulation_signal},
    "gap_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_136_capitulation_signal},
    "gap_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_137_capitulation_signal},
    "gap_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_138_capitulation_signal},
    "gap_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_139_capitulation_signal},
    "gap_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_140_capitulation_signal},
    "gap_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_141_capitulation_signal},
    "gap_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_142_capitulation_signal},
    "gap_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_143_capitulation_signal},
    "gap_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_144_capitulation_signal},
    "gap_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_145_capitulation_signal},
    "gap_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_146_capitulation_signal},
    "gap_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_147_capitulation_signal},
    "gap_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_148_capitulation_signal},
    "gap_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_149_capitulation_signal},
    "gap_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_150_capitulation_signal},
}
