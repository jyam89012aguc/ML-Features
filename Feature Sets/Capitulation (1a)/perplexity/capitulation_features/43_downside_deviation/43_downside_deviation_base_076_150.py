"""Generated capitulation features for 43_downside_deviation: downside-only dispersion.
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

def dsd_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def dsd_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def dsd_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def dsd_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def dsd_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def dsd_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def dsd_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def dsd_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def dsd_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def dsd_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def dsd_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dsd_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def dsd_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def dsd_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def dsd_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def dsd_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def dsd_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def dsd_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def dsd_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def dsd_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def dsd_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def dsd_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def dsd_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def dsd_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def dsd_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def dsd_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dsd_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def dsd_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def dsd_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def dsd_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def dsd_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def dsd_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def dsd_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def dsd_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def dsd_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def dsd_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def dsd_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def dsd_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def dsd_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def dsd_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def dsd_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dsd_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def dsd_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def dsd_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def dsd_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def dsd_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def dsd_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def dsd_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def dsd_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def dsd_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def dsd_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def dsd_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def dsd_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def dsd_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def dsd_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def dsd_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dsd_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def dsd_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def dsd_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def dsd_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def dsd_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def dsd_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def dsd_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

DOWNSIDE_DEVIATION_REGISTRY_076_150 = {
    "dsd_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_076_capitulation_signal},
    "dsd_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_077_capitulation_signal},
    "dsd_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_078_capitulation_signal},
    "dsd_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_079_capitulation_signal},
    "dsd_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_080_capitulation_signal},
    "dsd_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_081_capitulation_signal},
    "dsd_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_082_capitulation_signal},
    "dsd_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_083_capitulation_signal},
    "dsd_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_084_capitulation_signal},
    "dsd_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_085_capitulation_signal},
    "dsd_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_086_capitulation_signal},
    "dsd_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_087_capitulation_signal},
    "dsd_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_088_capitulation_signal},
    "dsd_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_089_capitulation_signal},
    "dsd_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_090_capitulation_signal},
    "dsd_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_091_capitulation_signal},
    "dsd_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_092_capitulation_signal},
    "dsd_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_093_capitulation_signal},
    "dsd_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_094_capitulation_signal},
    "dsd_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_095_capitulation_signal},
    "dsd_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_096_capitulation_signal},
    "dsd_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_097_capitulation_signal},
    "dsd_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_098_capitulation_signal},
    "dsd_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_099_capitulation_signal},
    "dsd_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_100_capitulation_signal},
    "dsd_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_101_capitulation_signal},
    "dsd_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_102_capitulation_signal},
    "dsd_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_103_capitulation_signal},
    "dsd_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_104_capitulation_signal},
    "dsd_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_105_capitulation_signal},
    "dsd_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_106_capitulation_signal},
    "dsd_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_107_capitulation_signal},
    "dsd_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_108_capitulation_signal},
    "dsd_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_109_capitulation_signal},
    "dsd_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_110_capitulation_signal},
    "dsd_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_111_capitulation_signal},
    "dsd_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_112_capitulation_signal},
    "dsd_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_113_capitulation_signal},
    "dsd_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_114_capitulation_signal},
    "dsd_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_115_capitulation_signal},
    "dsd_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_116_capitulation_signal},
    "dsd_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_117_capitulation_signal},
    "dsd_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_118_capitulation_signal},
    "dsd_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_119_capitulation_signal},
    "dsd_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_120_capitulation_signal},
    "dsd_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_121_capitulation_signal},
    "dsd_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_122_capitulation_signal},
    "dsd_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_123_capitulation_signal},
    "dsd_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_124_capitulation_signal},
    "dsd_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_125_capitulation_signal},
    "dsd_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_126_capitulation_signal},
    "dsd_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_127_capitulation_signal},
    "dsd_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_128_capitulation_signal},
    "dsd_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_129_capitulation_signal},
    "dsd_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_130_capitulation_signal},
    "dsd_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_131_capitulation_signal},
    "dsd_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_132_capitulation_signal},
    "dsd_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_133_capitulation_signal},
    "dsd_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_134_capitulation_signal},
    "dsd_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_135_capitulation_signal},
    "dsd_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_136_capitulation_signal},
    "dsd_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_137_capitulation_signal},
    "dsd_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_138_capitulation_signal},
    "dsd_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_139_capitulation_signal},
    "dsd_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_140_capitulation_signal},
    "dsd_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_141_capitulation_signal},
    "dsd_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_142_capitulation_signal},
    "dsd_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_143_capitulation_signal},
    "dsd_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_144_capitulation_signal},
    "dsd_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_145_capitulation_signal},
    "dsd_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_146_capitulation_signal},
    "dsd_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_147_capitulation_signal},
    "dsd_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_148_capitulation_signal},
    "dsd_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_149_capitulation_signal},
    "dsd_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_150_capitulation_signal},
}
