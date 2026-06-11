"""Generated capitulation features for 19_volume_trend: directional drift in volume.
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

def vtr_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def vtr_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def vtr_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def vtr_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def vtr_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def vtr_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def vtr_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def vtr_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def vtr_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def vtr_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def vtr_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vtr_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def vtr_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def vtr_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def vtr_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def vtr_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def vtr_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vtr_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def vtr_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def vtr_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def vtr_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def vtr_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def vtr_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def vtr_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def vtr_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def vtr_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vtr_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def vtr_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def vtr_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def vtr_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def vtr_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def vtr_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vtr_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def vtr_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def vtr_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def vtr_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def vtr_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def vtr_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def vtr_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def vtr_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def vtr_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vtr_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def vtr_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def vtr_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def vtr_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def vtr_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def vtr_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vtr_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def vtr_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def vtr_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def vtr_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def vtr_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def vtr_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def vtr_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def vtr_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def vtr_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vtr_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def vtr_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def vtr_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def vtr_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def vtr_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def vtr_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vtr_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

VOLUME_TREND_REGISTRY_076_150 = {
    "vtr_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_076_capitulation_signal},
    "vtr_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_077_capitulation_signal},
    "vtr_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_078_capitulation_signal},
    "vtr_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_079_capitulation_signal},
    "vtr_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_080_capitulation_signal},
    "vtr_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_081_capitulation_signal},
    "vtr_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_082_capitulation_signal},
    "vtr_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_083_capitulation_signal},
    "vtr_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_084_capitulation_signal},
    "vtr_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_085_capitulation_signal},
    "vtr_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_086_capitulation_signal},
    "vtr_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_087_capitulation_signal},
    "vtr_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_088_capitulation_signal},
    "vtr_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_089_capitulation_signal},
    "vtr_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_090_capitulation_signal},
    "vtr_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_091_capitulation_signal},
    "vtr_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_092_capitulation_signal},
    "vtr_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_093_capitulation_signal},
    "vtr_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_094_capitulation_signal},
    "vtr_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_095_capitulation_signal},
    "vtr_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_096_capitulation_signal},
    "vtr_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_097_capitulation_signal},
    "vtr_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_098_capitulation_signal},
    "vtr_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_099_capitulation_signal},
    "vtr_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_100_capitulation_signal},
    "vtr_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_101_capitulation_signal},
    "vtr_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_102_capitulation_signal},
    "vtr_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_103_capitulation_signal},
    "vtr_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_104_capitulation_signal},
    "vtr_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_105_capitulation_signal},
    "vtr_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_106_capitulation_signal},
    "vtr_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_107_capitulation_signal},
    "vtr_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_108_capitulation_signal},
    "vtr_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_109_capitulation_signal},
    "vtr_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_110_capitulation_signal},
    "vtr_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_111_capitulation_signal},
    "vtr_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_112_capitulation_signal},
    "vtr_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_113_capitulation_signal},
    "vtr_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_114_capitulation_signal},
    "vtr_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_115_capitulation_signal},
    "vtr_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_116_capitulation_signal},
    "vtr_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_117_capitulation_signal},
    "vtr_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_118_capitulation_signal},
    "vtr_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_119_capitulation_signal},
    "vtr_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_120_capitulation_signal},
    "vtr_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_121_capitulation_signal},
    "vtr_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_122_capitulation_signal},
    "vtr_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_123_capitulation_signal},
    "vtr_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_124_capitulation_signal},
    "vtr_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_125_capitulation_signal},
    "vtr_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_126_capitulation_signal},
    "vtr_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_127_capitulation_signal},
    "vtr_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_128_capitulation_signal},
    "vtr_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_129_capitulation_signal},
    "vtr_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_130_capitulation_signal},
    "vtr_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_131_capitulation_signal},
    "vtr_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_132_capitulation_signal},
    "vtr_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_133_capitulation_signal},
    "vtr_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_134_capitulation_signal},
    "vtr_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_135_capitulation_signal},
    "vtr_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_136_capitulation_signal},
    "vtr_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_137_capitulation_signal},
    "vtr_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_138_capitulation_signal},
    "vtr_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_139_capitulation_signal},
    "vtr_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_140_capitulation_signal},
    "vtr_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_141_capitulation_signal},
    "vtr_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_142_capitulation_signal},
    "vtr_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_143_capitulation_signal},
    "vtr_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_144_capitulation_signal},
    "vtr_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_145_capitulation_signal},
    "vtr_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_146_capitulation_signal},
    "vtr_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_147_capitulation_signal},
    "vtr_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_148_capitulation_signal},
    "vtr_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_149_capitulation_signal},
    "vtr_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_150_capitulation_signal},
}
