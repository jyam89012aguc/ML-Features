"""Generated capitulation features for 04_drawdown_velocity: speed of decline, slope of fall.
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

def dvel_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def dvel_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def dvel_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def dvel_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def dvel_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def dvel_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def dvel_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def dvel_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def dvel_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def dvel_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def dvel_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dvel_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def dvel_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def dvel_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def dvel_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def dvel_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def dvel_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def dvel_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def dvel_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def dvel_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def dvel_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def dvel_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def dvel_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def dvel_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def dvel_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def dvel_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dvel_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def dvel_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def dvel_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def dvel_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def dvel_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def dvel_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def dvel_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def dvel_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def dvel_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def dvel_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def dvel_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def dvel_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def dvel_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def dvel_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def dvel_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dvel_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def dvel_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def dvel_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def dvel_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def dvel_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def dvel_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def dvel_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def dvel_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def dvel_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def dvel_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def dvel_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def dvel_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def dvel_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def dvel_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def dvel_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dvel_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def dvel_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def dvel_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def dvel_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def dvel_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def dvel_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def dvel_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

DRAWDOWN_VELOCITY_REGISTRY_076_150 = {
    "dvel_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_076_capitulation_signal},
    "dvel_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_077_capitulation_signal},
    "dvel_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_078_capitulation_signal},
    "dvel_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_079_capitulation_signal},
    "dvel_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_080_capitulation_signal},
    "dvel_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_081_capitulation_signal},
    "dvel_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_082_capitulation_signal},
    "dvel_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_083_capitulation_signal},
    "dvel_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_084_capitulation_signal},
    "dvel_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_085_capitulation_signal},
    "dvel_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_086_capitulation_signal},
    "dvel_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_087_capitulation_signal},
    "dvel_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_088_capitulation_signal},
    "dvel_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_089_capitulation_signal},
    "dvel_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_090_capitulation_signal},
    "dvel_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_091_capitulation_signal},
    "dvel_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_092_capitulation_signal},
    "dvel_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_093_capitulation_signal},
    "dvel_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_094_capitulation_signal},
    "dvel_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_095_capitulation_signal},
    "dvel_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_096_capitulation_signal},
    "dvel_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_097_capitulation_signal},
    "dvel_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_098_capitulation_signal},
    "dvel_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_099_capitulation_signal},
    "dvel_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_100_capitulation_signal},
    "dvel_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_101_capitulation_signal},
    "dvel_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_102_capitulation_signal},
    "dvel_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_103_capitulation_signal},
    "dvel_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_104_capitulation_signal},
    "dvel_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_105_capitulation_signal},
    "dvel_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_106_capitulation_signal},
    "dvel_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_107_capitulation_signal},
    "dvel_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_108_capitulation_signal},
    "dvel_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_109_capitulation_signal},
    "dvel_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_110_capitulation_signal},
    "dvel_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_111_capitulation_signal},
    "dvel_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_112_capitulation_signal},
    "dvel_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_113_capitulation_signal},
    "dvel_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_114_capitulation_signal},
    "dvel_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_115_capitulation_signal},
    "dvel_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_116_capitulation_signal},
    "dvel_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_117_capitulation_signal},
    "dvel_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_118_capitulation_signal},
    "dvel_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_119_capitulation_signal},
    "dvel_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_120_capitulation_signal},
    "dvel_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_121_capitulation_signal},
    "dvel_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_122_capitulation_signal},
    "dvel_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_123_capitulation_signal},
    "dvel_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_124_capitulation_signal},
    "dvel_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_125_capitulation_signal},
    "dvel_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_126_capitulation_signal},
    "dvel_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_127_capitulation_signal},
    "dvel_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_128_capitulation_signal},
    "dvel_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_129_capitulation_signal},
    "dvel_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_130_capitulation_signal},
    "dvel_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_131_capitulation_signal},
    "dvel_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_132_capitulation_signal},
    "dvel_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_133_capitulation_signal},
    "dvel_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_134_capitulation_signal},
    "dvel_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_135_capitulation_signal},
    "dvel_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_136_capitulation_signal},
    "dvel_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_137_capitulation_signal},
    "dvel_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_138_capitulation_signal},
    "dvel_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_139_capitulation_signal},
    "dvel_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_140_capitulation_signal},
    "dvel_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_141_capitulation_signal},
    "dvel_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_142_capitulation_signal},
    "dvel_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_143_capitulation_signal},
    "dvel_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_144_capitulation_signal},
    "dvel_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_145_capitulation_signal},
    "dvel_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_146_capitulation_signal},
    "dvel_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_147_capitulation_signal},
    "dvel_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_148_capitulation_signal},
    "dvel_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_149_capitulation_signal},
    "dvel_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_150_capitulation_signal},
}
