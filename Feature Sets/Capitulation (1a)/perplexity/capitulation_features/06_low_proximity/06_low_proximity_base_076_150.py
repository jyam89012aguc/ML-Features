"""Generated capitulation features for 06_low_proximity: closeness to trailing min, new-low frequency.
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

def lp_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def lp_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def lp_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def lp_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def lp_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def lp_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def lp_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def lp_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def lp_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def lp_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def lp_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def lp_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def lp_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def lp_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def lp_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def lp_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def lp_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def lp_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def lp_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def lp_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def lp_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def lp_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def lp_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def lp_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def lp_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def lp_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def lp_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def lp_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def lp_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def lp_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def lp_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def lp_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def lp_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def lp_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def lp_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def lp_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def lp_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def lp_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def lp_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def lp_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def lp_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def lp_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def lp_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def lp_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def lp_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def lp_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def lp_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def lp_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def lp_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def lp_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def lp_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def lp_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def lp_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def lp_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def lp_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def lp_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def lp_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def lp_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def lp_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def lp_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def lp_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def lp_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def lp_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def lp_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def lp_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def lp_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def lp_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def lp_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def lp_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def lp_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def lp_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def lp_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def lp_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def lp_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def lp_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

LOW_PROXIMITY_REGISTRY_076_150 = {
    "lp_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_076_capitulation_signal},
    "lp_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_077_capitulation_signal},
    "lp_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_078_capitulation_signal},
    "lp_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_079_capitulation_signal},
    "lp_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_080_capitulation_signal},
    "lp_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_081_capitulation_signal},
    "lp_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_082_capitulation_signal},
    "lp_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_083_capitulation_signal},
    "lp_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_084_capitulation_signal},
    "lp_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_085_capitulation_signal},
    "lp_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_086_capitulation_signal},
    "lp_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_087_capitulation_signal},
    "lp_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_088_capitulation_signal},
    "lp_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_089_capitulation_signal},
    "lp_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_090_capitulation_signal},
    "lp_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_091_capitulation_signal},
    "lp_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_092_capitulation_signal},
    "lp_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_093_capitulation_signal},
    "lp_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_094_capitulation_signal},
    "lp_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_095_capitulation_signal},
    "lp_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_096_capitulation_signal},
    "lp_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_097_capitulation_signal},
    "lp_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_098_capitulation_signal},
    "lp_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_099_capitulation_signal},
    "lp_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_100_capitulation_signal},
    "lp_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_101_capitulation_signal},
    "lp_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_102_capitulation_signal},
    "lp_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_103_capitulation_signal},
    "lp_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_104_capitulation_signal},
    "lp_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_105_capitulation_signal},
    "lp_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_106_capitulation_signal},
    "lp_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_107_capitulation_signal},
    "lp_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_108_capitulation_signal},
    "lp_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_109_capitulation_signal},
    "lp_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_110_capitulation_signal},
    "lp_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_111_capitulation_signal},
    "lp_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_112_capitulation_signal},
    "lp_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_113_capitulation_signal},
    "lp_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_114_capitulation_signal},
    "lp_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_115_capitulation_signal},
    "lp_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_116_capitulation_signal},
    "lp_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_117_capitulation_signal},
    "lp_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_118_capitulation_signal},
    "lp_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_119_capitulation_signal},
    "lp_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_120_capitulation_signal},
    "lp_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_121_capitulation_signal},
    "lp_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_122_capitulation_signal},
    "lp_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_123_capitulation_signal},
    "lp_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_124_capitulation_signal},
    "lp_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_125_capitulation_signal},
    "lp_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_126_capitulation_signal},
    "lp_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_127_capitulation_signal},
    "lp_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_128_capitulation_signal},
    "lp_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_129_capitulation_signal},
    "lp_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_130_capitulation_signal},
    "lp_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_131_capitulation_signal},
    "lp_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_132_capitulation_signal},
    "lp_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_133_capitulation_signal},
    "lp_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_134_capitulation_signal},
    "lp_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_135_capitulation_signal},
    "lp_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_136_capitulation_signal},
    "lp_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_137_capitulation_signal},
    "lp_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_138_capitulation_signal},
    "lp_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_139_capitulation_signal},
    "lp_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_140_capitulation_signal},
    "lp_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_141_capitulation_signal},
    "lp_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_142_capitulation_signal},
    "lp_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_143_capitulation_signal},
    "lp_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_144_capitulation_signal},
    "lp_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_145_capitulation_signal},
    "lp_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_146_capitulation_signal},
    "lp_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_147_capitulation_signal},
    "lp_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_148_capitulation_signal},
    "lp_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_149_capitulation_signal},
    "lp_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_150_capitulation_signal},
}
