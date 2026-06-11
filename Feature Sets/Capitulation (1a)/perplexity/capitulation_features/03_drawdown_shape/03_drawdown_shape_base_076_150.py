"""Generated capitulation features for 03_drawdown_shape: convexity/concavity of decline path.
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

def dsh_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def dsh_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def dsh_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def dsh_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def dsh_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def dsh_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def dsh_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def dsh_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def dsh_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def dsh_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def dsh_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dsh_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def dsh_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def dsh_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def dsh_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def dsh_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def dsh_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def dsh_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def dsh_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def dsh_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def dsh_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def dsh_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def dsh_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def dsh_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def dsh_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def dsh_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dsh_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def dsh_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def dsh_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def dsh_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def dsh_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def dsh_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def dsh_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def dsh_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def dsh_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def dsh_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def dsh_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def dsh_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def dsh_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def dsh_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def dsh_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dsh_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def dsh_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def dsh_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def dsh_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def dsh_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def dsh_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def dsh_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def dsh_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def dsh_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def dsh_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def dsh_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def dsh_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def dsh_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def dsh_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def dsh_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dsh_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def dsh_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def dsh_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def dsh_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def dsh_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def dsh_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def dsh_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

DRAWDOWN_SHAPE_REGISTRY_076_150 = {
    "dsh_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_076_capitulation_signal},
    "dsh_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_077_capitulation_signal},
    "dsh_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_078_capitulation_signal},
    "dsh_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_079_capitulation_signal},
    "dsh_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_080_capitulation_signal},
    "dsh_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_081_capitulation_signal},
    "dsh_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_082_capitulation_signal},
    "dsh_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_083_capitulation_signal},
    "dsh_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_084_capitulation_signal},
    "dsh_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_085_capitulation_signal},
    "dsh_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_086_capitulation_signal},
    "dsh_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_087_capitulation_signal},
    "dsh_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_088_capitulation_signal},
    "dsh_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_089_capitulation_signal},
    "dsh_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_090_capitulation_signal},
    "dsh_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_091_capitulation_signal},
    "dsh_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_092_capitulation_signal},
    "dsh_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_093_capitulation_signal},
    "dsh_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_094_capitulation_signal},
    "dsh_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_095_capitulation_signal},
    "dsh_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_096_capitulation_signal},
    "dsh_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_097_capitulation_signal},
    "dsh_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_098_capitulation_signal},
    "dsh_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_099_capitulation_signal},
    "dsh_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_100_capitulation_signal},
    "dsh_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_101_capitulation_signal},
    "dsh_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_102_capitulation_signal},
    "dsh_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_103_capitulation_signal},
    "dsh_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_104_capitulation_signal},
    "dsh_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_105_capitulation_signal},
    "dsh_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_106_capitulation_signal},
    "dsh_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_107_capitulation_signal},
    "dsh_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_108_capitulation_signal},
    "dsh_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_109_capitulation_signal},
    "dsh_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_110_capitulation_signal},
    "dsh_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_111_capitulation_signal},
    "dsh_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_112_capitulation_signal},
    "dsh_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_113_capitulation_signal},
    "dsh_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_114_capitulation_signal},
    "dsh_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_115_capitulation_signal},
    "dsh_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_116_capitulation_signal},
    "dsh_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_117_capitulation_signal},
    "dsh_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_118_capitulation_signal},
    "dsh_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_119_capitulation_signal},
    "dsh_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_120_capitulation_signal},
    "dsh_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_121_capitulation_signal},
    "dsh_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_122_capitulation_signal},
    "dsh_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_123_capitulation_signal},
    "dsh_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_124_capitulation_signal},
    "dsh_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_125_capitulation_signal},
    "dsh_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_126_capitulation_signal},
    "dsh_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_127_capitulation_signal},
    "dsh_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_128_capitulation_signal},
    "dsh_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_129_capitulation_signal},
    "dsh_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_130_capitulation_signal},
    "dsh_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_131_capitulation_signal},
    "dsh_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_132_capitulation_signal},
    "dsh_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_133_capitulation_signal},
    "dsh_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_134_capitulation_signal},
    "dsh_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_135_capitulation_signal},
    "dsh_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_136_capitulation_signal},
    "dsh_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_137_capitulation_signal},
    "dsh_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_138_capitulation_signal},
    "dsh_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_139_capitulation_signal},
    "dsh_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_140_capitulation_signal},
    "dsh_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_141_capitulation_signal},
    "dsh_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_142_capitulation_signal},
    "dsh_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_143_capitulation_signal},
    "dsh_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_144_capitulation_signal},
    "dsh_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_145_capitulation_signal},
    "dsh_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_146_capitulation_signal},
    "dsh_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_147_capitulation_signal},
    "dsh_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_148_capitulation_signal},
    "dsh_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_149_capitulation_signal},
    "dsh_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_150_capitulation_signal},
}
