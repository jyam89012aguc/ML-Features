"""Generated capitulation features for 12_high_water_distance: distance/time from prior all-time high.
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

def hwd_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def hwd_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def hwd_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def hwd_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def hwd_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def hwd_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def hwd_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def hwd_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def hwd_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def hwd_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def hwd_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def hwd_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def hwd_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def hwd_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def hwd_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def hwd_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def hwd_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def hwd_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def hwd_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def hwd_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def hwd_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def hwd_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def hwd_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def hwd_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def hwd_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def hwd_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def hwd_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def hwd_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def hwd_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def hwd_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def hwd_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def hwd_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def hwd_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def hwd_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def hwd_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def hwd_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def hwd_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def hwd_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def hwd_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def hwd_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def hwd_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def hwd_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def hwd_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def hwd_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def hwd_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def hwd_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def hwd_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def hwd_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def hwd_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def hwd_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def hwd_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def hwd_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def hwd_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def hwd_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def hwd_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def hwd_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def hwd_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def hwd_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def hwd_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def hwd_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def hwd_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def hwd_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def hwd_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

HIGH_WATER_DISTANCE_REGISTRY_076_150 = {
    "hwd_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_076_capitulation_signal},
    "hwd_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_077_capitulation_signal},
    "hwd_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_078_capitulation_signal},
    "hwd_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_079_capitulation_signal},
    "hwd_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_080_capitulation_signal},
    "hwd_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_081_capitulation_signal},
    "hwd_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_082_capitulation_signal},
    "hwd_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_083_capitulation_signal},
    "hwd_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_084_capitulation_signal},
    "hwd_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_085_capitulation_signal},
    "hwd_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_086_capitulation_signal},
    "hwd_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_087_capitulation_signal},
    "hwd_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_088_capitulation_signal},
    "hwd_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_089_capitulation_signal},
    "hwd_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_090_capitulation_signal},
    "hwd_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_091_capitulation_signal},
    "hwd_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_092_capitulation_signal},
    "hwd_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_093_capitulation_signal},
    "hwd_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_094_capitulation_signal},
    "hwd_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_095_capitulation_signal},
    "hwd_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_096_capitulation_signal},
    "hwd_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_097_capitulation_signal},
    "hwd_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_098_capitulation_signal},
    "hwd_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_099_capitulation_signal},
    "hwd_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_100_capitulation_signal},
    "hwd_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_101_capitulation_signal},
    "hwd_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_102_capitulation_signal},
    "hwd_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_103_capitulation_signal},
    "hwd_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_104_capitulation_signal},
    "hwd_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_105_capitulation_signal},
    "hwd_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_106_capitulation_signal},
    "hwd_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_107_capitulation_signal},
    "hwd_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_108_capitulation_signal},
    "hwd_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_109_capitulation_signal},
    "hwd_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_110_capitulation_signal},
    "hwd_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_111_capitulation_signal},
    "hwd_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_112_capitulation_signal},
    "hwd_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_113_capitulation_signal},
    "hwd_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_114_capitulation_signal},
    "hwd_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_115_capitulation_signal},
    "hwd_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_116_capitulation_signal},
    "hwd_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_117_capitulation_signal},
    "hwd_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_118_capitulation_signal},
    "hwd_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_119_capitulation_signal},
    "hwd_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_120_capitulation_signal},
    "hwd_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_121_capitulation_signal},
    "hwd_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_122_capitulation_signal},
    "hwd_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_123_capitulation_signal},
    "hwd_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_124_capitulation_signal},
    "hwd_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_125_capitulation_signal},
    "hwd_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_126_capitulation_signal},
    "hwd_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_127_capitulation_signal},
    "hwd_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_128_capitulation_signal},
    "hwd_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_129_capitulation_signal},
    "hwd_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_130_capitulation_signal},
    "hwd_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_131_capitulation_signal},
    "hwd_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_132_capitulation_signal},
    "hwd_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_133_capitulation_signal},
    "hwd_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_134_capitulation_signal},
    "hwd_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_135_capitulation_signal},
    "hwd_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_136_capitulation_signal},
    "hwd_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_137_capitulation_signal},
    "hwd_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_138_capitulation_signal},
    "hwd_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_139_capitulation_signal},
    "hwd_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_140_capitulation_signal},
    "hwd_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_141_capitulation_signal},
    "hwd_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_142_capitulation_signal},
    "hwd_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_143_capitulation_signal},
    "hwd_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_144_capitulation_signal},
    "hwd_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_145_capitulation_signal},
    "hwd_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_146_capitulation_signal},
    "hwd_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_147_capitulation_signal},
    "hwd_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_148_capitulation_signal},
    "hwd_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_149_capitulation_signal},
    "hwd_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_150_capitulation_signal},
}
