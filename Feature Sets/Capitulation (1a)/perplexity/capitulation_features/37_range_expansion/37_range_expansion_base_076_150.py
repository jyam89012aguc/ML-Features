"""Generated capitulation features for 37_range_expansion: true-range expansion.
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

def rex_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def rex_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def rex_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rex_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def rex_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def rex_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def rex_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def rex_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def rex_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def rex_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def rex_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rex_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rex_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def rex_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rex_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def rex_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def rex_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def rex_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def rex_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def rex_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def rex_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rex_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def rex_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def rex_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def rex_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def rex_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def rex_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def rex_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def rex_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rex_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rex_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def rex_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rex_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def rex_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def rex_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def rex_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def rex_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def rex_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def rex_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rex_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def rex_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def rex_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def rex_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def rex_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def rex_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def rex_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def rex_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rex_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rex_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def rex_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rex_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def rex_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def rex_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def rex_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def rex_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def rex_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def rex_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rex_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def rex_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def rex_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def rex_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def rex_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def rex_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def rex_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def rex_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rex_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rex_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def rex_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rex_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def rex_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def rex_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def rex_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def rex_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def rex_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def rex_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

RANGE_EXPANSION_REGISTRY_076_150 = {
    "rex_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_076_capitulation_signal},
    "rex_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_077_capitulation_signal},
    "rex_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_078_capitulation_signal},
    "rex_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_079_capitulation_signal},
    "rex_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_080_capitulation_signal},
    "rex_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_081_capitulation_signal},
    "rex_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_082_capitulation_signal},
    "rex_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_083_capitulation_signal},
    "rex_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_084_capitulation_signal},
    "rex_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_085_capitulation_signal},
    "rex_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_086_capitulation_signal},
    "rex_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_087_capitulation_signal},
    "rex_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_088_capitulation_signal},
    "rex_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_089_capitulation_signal},
    "rex_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_090_capitulation_signal},
    "rex_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_091_capitulation_signal},
    "rex_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_092_capitulation_signal},
    "rex_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_093_capitulation_signal},
    "rex_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_094_capitulation_signal},
    "rex_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_095_capitulation_signal},
    "rex_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_096_capitulation_signal},
    "rex_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_097_capitulation_signal},
    "rex_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_098_capitulation_signal},
    "rex_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_099_capitulation_signal},
    "rex_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_100_capitulation_signal},
    "rex_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_101_capitulation_signal},
    "rex_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_102_capitulation_signal},
    "rex_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_103_capitulation_signal},
    "rex_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_104_capitulation_signal},
    "rex_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_105_capitulation_signal},
    "rex_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_106_capitulation_signal},
    "rex_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_107_capitulation_signal},
    "rex_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_108_capitulation_signal},
    "rex_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_109_capitulation_signal},
    "rex_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_110_capitulation_signal},
    "rex_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_111_capitulation_signal},
    "rex_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_112_capitulation_signal},
    "rex_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_113_capitulation_signal},
    "rex_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_114_capitulation_signal},
    "rex_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_115_capitulation_signal},
    "rex_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_116_capitulation_signal},
    "rex_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_117_capitulation_signal},
    "rex_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_118_capitulation_signal},
    "rex_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_119_capitulation_signal},
    "rex_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_120_capitulation_signal},
    "rex_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_121_capitulation_signal},
    "rex_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_122_capitulation_signal},
    "rex_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_123_capitulation_signal},
    "rex_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_124_capitulation_signal},
    "rex_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_125_capitulation_signal},
    "rex_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_126_capitulation_signal},
    "rex_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_127_capitulation_signal},
    "rex_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_128_capitulation_signal},
    "rex_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_129_capitulation_signal},
    "rex_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_130_capitulation_signal},
    "rex_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_131_capitulation_signal},
    "rex_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_132_capitulation_signal},
    "rex_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_133_capitulation_signal},
    "rex_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_134_capitulation_signal},
    "rex_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_135_capitulation_signal},
    "rex_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_136_capitulation_signal},
    "rex_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_137_capitulation_signal},
    "rex_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_138_capitulation_signal},
    "rex_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_139_capitulation_signal},
    "rex_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_140_capitulation_signal},
    "rex_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_141_capitulation_signal},
    "rex_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_142_capitulation_signal},
    "rex_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_143_capitulation_signal},
    "rex_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_144_capitulation_signal},
    "rex_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_145_capitulation_signal},
    "rex_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_146_capitulation_signal},
    "rex_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_147_capitulation_signal},
    "rex_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_148_capitulation_signal},
    "rex_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_149_capitulation_signal},
    "rex_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_150_capitulation_signal},
}
