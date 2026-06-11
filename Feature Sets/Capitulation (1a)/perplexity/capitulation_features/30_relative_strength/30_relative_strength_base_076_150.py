"""Generated capitulation features for 30_relative_strength: price vs moving averages.
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

def rst_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def rst_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def rst_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rst_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def rst_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def rst_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def rst_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def rst_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def rst_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def rst_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def rst_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rst_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rst_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def rst_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rst_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def rst_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def rst_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def rst_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def rst_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def rst_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def rst_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rst_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def rst_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def rst_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def rst_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def rst_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def rst_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def rst_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def rst_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rst_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rst_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def rst_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rst_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def rst_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def rst_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def rst_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def rst_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def rst_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def rst_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rst_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def rst_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def rst_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def rst_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def rst_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def rst_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def rst_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def rst_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rst_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rst_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def rst_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rst_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def rst_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def rst_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def rst_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def rst_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def rst_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def rst_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rst_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def rst_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def rst_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def rst_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def rst_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def rst_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def rst_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def rst_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rst_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rst_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def rst_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rst_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def rst_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def rst_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def rst_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def rst_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def rst_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def rst_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

RELATIVE_STRENGTH_REGISTRY_076_150 = {
    "rst_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_076_capitulation_signal},
    "rst_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_077_capitulation_signal},
    "rst_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_078_capitulation_signal},
    "rst_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_079_capitulation_signal},
    "rst_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_080_capitulation_signal},
    "rst_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_081_capitulation_signal},
    "rst_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_082_capitulation_signal},
    "rst_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_083_capitulation_signal},
    "rst_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_084_capitulation_signal},
    "rst_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_085_capitulation_signal},
    "rst_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_086_capitulation_signal},
    "rst_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_087_capitulation_signal},
    "rst_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_088_capitulation_signal},
    "rst_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_089_capitulation_signal},
    "rst_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_090_capitulation_signal},
    "rst_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_091_capitulation_signal},
    "rst_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_092_capitulation_signal},
    "rst_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_093_capitulation_signal},
    "rst_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_094_capitulation_signal},
    "rst_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_095_capitulation_signal},
    "rst_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_096_capitulation_signal},
    "rst_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_097_capitulation_signal},
    "rst_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_098_capitulation_signal},
    "rst_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_099_capitulation_signal},
    "rst_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_100_capitulation_signal},
    "rst_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_101_capitulation_signal},
    "rst_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_102_capitulation_signal},
    "rst_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_103_capitulation_signal},
    "rst_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_104_capitulation_signal},
    "rst_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_105_capitulation_signal},
    "rst_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_106_capitulation_signal},
    "rst_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_107_capitulation_signal},
    "rst_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_108_capitulation_signal},
    "rst_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_109_capitulation_signal},
    "rst_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_110_capitulation_signal},
    "rst_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_111_capitulation_signal},
    "rst_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_112_capitulation_signal},
    "rst_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_113_capitulation_signal},
    "rst_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_114_capitulation_signal},
    "rst_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_115_capitulation_signal},
    "rst_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_116_capitulation_signal},
    "rst_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_117_capitulation_signal},
    "rst_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_118_capitulation_signal},
    "rst_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_119_capitulation_signal},
    "rst_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_120_capitulation_signal},
    "rst_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_121_capitulation_signal},
    "rst_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_122_capitulation_signal},
    "rst_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_123_capitulation_signal},
    "rst_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_124_capitulation_signal},
    "rst_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_125_capitulation_signal},
    "rst_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_126_capitulation_signal},
    "rst_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_127_capitulation_signal},
    "rst_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_128_capitulation_signal},
    "rst_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_129_capitulation_signal},
    "rst_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_130_capitulation_signal},
    "rst_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_131_capitulation_signal},
    "rst_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_132_capitulation_signal},
    "rst_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_133_capitulation_signal},
    "rst_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_134_capitulation_signal},
    "rst_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_135_capitulation_signal},
    "rst_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_136_capitulation_signal},
    "rst_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_137_capitulation_signal},
    "rst_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_138_capitulation_signal},
    "rst_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_139_capitulation_signal},
    "rst_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_140_capitulation_signal},
    "rst_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_141_capitulation_signal},
    "rst_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_142_capitulation_signal},
    "rst_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_143_capitulation_signal},
    "rst_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_144_capitulation_signal},
    "rst_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_145_capitulation_signal},
    "rst_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_146_capitulation_signal},
    "rst_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_147_capitulation_signal},
    "rst_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_148_capitulation_signal},
    "rst_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_149_capitulation_signal},
    "rst_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_150_capitulation_signal},
}
