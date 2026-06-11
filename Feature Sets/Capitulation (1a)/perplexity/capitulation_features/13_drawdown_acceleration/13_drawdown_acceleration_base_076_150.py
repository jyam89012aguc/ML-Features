"""Generated capitulation features for 13_drawdown_acceleration: whether decline is speeding up.
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

def dacc_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def dacc_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def dacc_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def dacc_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def dacc_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def dacc_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def dacc_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def dacc_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def dacc_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def dacc_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def dacc_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dacc_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def dacc_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def dacc_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def dacc_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def dacc_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def dacc_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def dacc_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def dacc_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def dacc_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def dacc_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def dacc_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def dacc_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def dacc_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def dacc_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def dacc_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dacc_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def dacc_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def dacc_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def dacc_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def dacc_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def dacc_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def dacc_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def dacc_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def dacc_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def dacc_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def dacc_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def dacc_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def dacc_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def dacc_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def dacc_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dacc_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def dacc_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def dacc_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def dacc_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def dacc_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def dacc_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def dacc_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def dacc_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def dacc_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def dacc_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def dacc_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def dacc_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def dacc_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def dacc_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def dacc_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dacc_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def dacc_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def dacc_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def dacc_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def dacc_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def dacc_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def dacc_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

DRAWDOWN_ACCELERATION_REGISTRY_076_150 = {
    "dacc_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_076_capitulation_signal},
    "dacc_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_077_capitulation_signal},
    "dacc_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_078_capitulation_signal},
    "dacc_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_079_capitulation_signal},
    "dacc_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_080_capitulation_signal},
    "dacc_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_081_capitulation_signal},
    "dacc_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_082_capitulation_signal},
    "dacc_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_083_capitulation_signal},
    "dacc_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_084_capitulation_signal},
    "dacc_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_085_capitulation_signal},
    "dacc_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_086_capitulation_signal},
    "dacc_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_087_capitulation_signal},
    "dacc_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_088_capitulation_signal},
    "dacc_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_089_capitulation_signal},
    "dacc_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_090_capitulation_signal},
    "dacc_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_091_capitulation_signal},
    "dacc_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_092_capitulation_signal},
    "dacc_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_093_capitulation_signal},
    "dacc_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_094_capitulation_signal},
    "dacc_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_095_capitulation_signal},
    "dacc_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_096_capitulation_signal},
    "dacc_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_097_capitulation_signal},
    "dacc_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_098_capitulation_signal},
    "dacc_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_099_capitulation_signal},
    "dacc_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_100_capitulation_signal},
    "dacc_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_101_capitulation_signal},
    "dacc_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_102_capitulation_signal},
    "dacc_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_103_capitulation_signal},
    "dacc_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_104_capitulation_signal},
    "dacc_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_105_capitulation_signal},
    "dacc_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_106_capitulation_signal},
    "dacc_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_107_capitulation_signal},
    "dacc_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_108_capitulation_signal},
    "dacc_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_109_capitulation_signal},
    "dacc_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_110_capitulation_signal},
    "dacc_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_111_capitulation_signal},
    "dacc_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_112_capitulation_signal},
    "dacc_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_113_capitulation_signal},
    "dacc_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_114_capitulation_signal},
    "dacc_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_115_capitulation_signal},
    "dacc_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_116_capitulation_signal},
    "dacc_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_117_capitulation_signal},
    "dacc_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_118_capitulation_signal},
    "dacc_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_119_capitulation_signal},
    "dacc_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_120_capitulation_signal},
    "dacc_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_121_capitulation_signal},
    "dacc_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_122_capitulation_signal},
    "dacc_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_123_capitulation_signal},
    "dacc_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_124_capitulation_signal},
    "dacc_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_125_capitulation_signal},
    "dacc_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_126_capitulation_signal},
    "dacc_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_127_capitulation_signal},
    "dacc_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_128_capitulation_signal},
    "dacc_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_129_capitulation_signal},
    "dacc_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_130_capitulation_signal},
    "dacc_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_131_capitulation_signal},
    "dacc_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_132_capitulation_signal},
    "dacc_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_133_capitulation_signal},
    "dacc_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_134_capitulation_signal},
    "dacc_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_135_capitulation_signal},
    "dacc_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_136_capitulation_signal},
    "dacc_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_137_capitulation_signal},
    "dacc_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_138_capitulation_signal},
    "dacc_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_139_capitulation_signal},
    "dacc_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_140_capitulation_signal},
    "dacc_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_141_capitulation_signal},
    "dacc_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_142_capitulation_signal},
    "dacc_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_143_capitulation_signal},
    "dacc_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_144_capitulation_signal},
    "dacc_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_145_capitulation_signal},
    "dacc_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_146_capitulation_signal},
    "dacc_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_147_capitulation_signal},
    "dacc_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_148_capitulation_signal},
    "dacc_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_149_capitulation_signal},
    "dacc_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_150_capitulation_signal},
}
