"""Generated capitulation features for 24_volume_distribution: volume distribution shape.
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

def vds_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def vds_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def vds_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vds_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def vds_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def vds_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def vds_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def vds_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def vds_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def vds_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def vds_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vds_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vds_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def vds_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vds_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def vds_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def vds_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def vds_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def vds_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def vds_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vds_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vds_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def vds_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def vds_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def vds_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def vds_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def vds_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def vds_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def vds_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vds_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vds_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def vds_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vds_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def vds_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def vds_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def vds_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def vds_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def vds_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vds_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vds_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def vds_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def vds_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def vds_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def vds_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def vds_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def vds_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def vds_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vds_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vds_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def vds_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vds_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def vds_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def vds_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def vds_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def vds_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def vds_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vds_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vds_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def vds_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def vds_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def vds_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def vds_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def vds_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def vds_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def vds_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vds_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vds_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def vds_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vds_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def vds_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def vds_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def vds_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def vds_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def vds_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vds_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

VOLUME_DISTRIBUTION_REGISTRY_076_150 = {
    "vds_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_076_capitulation_signal},
    "vds_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_077_capitulation_signal},
    "vds_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_078_capitulation_signal},
    "vds_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_079_capitulation_signal},
    "vds_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_080_capitulation_signal},
    "vds_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_081_capitulation_signal},
    "vds_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_082_capitulation_signal},
    "vds_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_083_capitulation_signal},
    "vds_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_084_capitulation_signal},
    "vds_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_085_capitulation_signal},
    "vds_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_086_capitulation_signal},
    "vds_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_087_capitulation_signal},
    "vds_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_088_capitulation_signal},
    "vds_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_089_capitulation_signal},
    "vds_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_090_capitulation_signal},
    "vds_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_091_capitulation_signal},
    "vds_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_092_capitulation_signal},
    "vds_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_093_capitulation_signal},
    "vds_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_094_capitulation_signal},
    "vds_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_095_capitulation_signal},
    "vds_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_096_capitulation_signal},
    "vds_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_097_capitulation_signal},
    "vds_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_098_capitulation_signal},
    "vds_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_099_capitulation_signal},
    "vds_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_100_capitulation_signal},
    "vds_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_101_capitulation_signal},
    "vds_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_102_capitulation_signal},
    "vds_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_103_capitulation_signal},
    "vds_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_104_capitulation_signal},
    "vds_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_105_capitulation_signal},
    "vds_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_106_capitulation_signal},
    "vds_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_107_capitulation_signal},
    "vds_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_108_capitulation_signal},
    "vds_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_109_capitulation_signal},
    "vds_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_110_capitulation_signal},
    "vds_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_111_capitulation_signal},
    "vds_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_112_capitulation_signal},
    "vds_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_113_capitulation_signal},
    "vds_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_114_capitulation_signal},
    "vds_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_115_capitulation_signal},
    "vds_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_116_capitulation_signal},
    "vds_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_117_capitulation_signal},
    "vds_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_118_capitulation_signal},
    "vds_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_119_capitulation_signal},
    "vds_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_120_capitulation_signal},
    "vds_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_121_capitulation_signal},
    "vds_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_122_capitulation_signal},
    "vds_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_123_capitulation_signal},
    "vds_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_124_capitulation_signal},
    "vds_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_125_capitulation_signal},
    "vds_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_126_capitulation_signal},
    "vds_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_127_capitulation_signal},
    "vds_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_128_capitulation_signal},
    "vds_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_129_capitulation_signal},
    "vds_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_130_capitulation_signal},
    "vds_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_131_capitulation_signal},
    "vds_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_132_capitulation_signal},
    "vds_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_133_capitulation_signal},
    "vds_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_134_capitulation_signal},
    "vds_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_135_capitulation_signal},
    "vds_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_136_capitulation_signal},
    "vds_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_137_capitulation_signal},
    "vds_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_138_capitulation_signal},
    "vds_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_139_capitulation_signal},
    "vds_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_140_capitulation_signal},
    "vds_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_141_capitulation_signal},
    "vds_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_142_capitulation_signal},
    "vds_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_143_capitulation_signal},
    "vds_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_144_capitulation_signal},
    "vds_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_145_capitulation_signal},
    "vds_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_146_capitulation_signal},
    "vds_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_147_capitulation_signal},
    "vds_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_148_capitulation_signal},
    "vds_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_149_capitulation_signal},
    "vds_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_150_capitulation_signal},
}
