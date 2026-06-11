"""Generated capitulation features for 18_volume_dryup: volume collapse/exhaustion.
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

def vdry_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def vdry_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def vdry_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def vdry_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def vdry_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def vdry_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def vdry_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def vdry_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def vdry_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def vdry_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def vdry_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vdry_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def vdry_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def vdry_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def vdry_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def vdry_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def vdry_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vdry_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def vdry_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def vdry_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def vdry_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def vdry_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def vdry_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def vdry_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def vdry_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def vdry_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vdry_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def vdry_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def vdry_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def vdry_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def vdry_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def vdry_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vdry_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def vdry_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def vdry_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def vdry_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def vdry_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def vdry_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def vdry_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def vdry_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def vdry_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vdry_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def vdry_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def vdry_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def vdry_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def vdry_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def vdry_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vdry_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def vdry_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def vdry_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def vdry_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def vdry_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def vdry_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def vdry_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def vdry_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def vdry_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vdry_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def vdry_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def vdry_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def vdry_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def vdry_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def vdry_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vdry_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

VOLUME_DRYUP_REGISTRY_076_150 = {
    "vdry_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_076_capitulation_signal},
    "vdry_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_077_capitulation_signal},
    "vdry_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_078_capitulation_signal},
    "vdry_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_079_capitulation_signal},
    "vdry_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_080_capitulation_signal},
    "vdry_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_081_capitulation_signal},
    "vdry_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_082_capitulation_signal},
    "vdry_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_083_capitulation_signal},
    "vdry_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_084_capitulation_signal},
    "vdry_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_085_capitulation_signal},
    "vdry_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_086_capitulation_signal},
    "vdry_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_087_capitulation_signal},
    "vdry_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_088_capitulation_signal},
    "vdry_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_089_capitulation_signal},
    "vdry_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_090_capitulation_signal},
    "vdry_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_091_capitulation_signal},
    "vdry_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_092_capitulation_signal},
    "vdry_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_093_capitulation_signal},
    "vdry_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_094_capitulation_signal},
    "vdry_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_095_capitulation_signal},
    "vdry_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_096_capitulation_signal},
    "vdry_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_097_capitulation_signal},
    "vdry_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_098_capitulation_signal},
    "vdry_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_099_capitulation_signal},
    "vdry_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_100_capitulation_signal},
    "vdry_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_101_capitulation_signal},
    "vdry_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_102_capitulation_signal},
    "vdry_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_103_capitulation_signal},
    "vdry_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_104_capitulation_signal},
    "vdry_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_105_capitulation_signal},
    "vdry_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_106_capitulation_signal},
    "vdry_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_107_capitulation_signal},
    "vdry_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_108_capitulation_signal},
    "vdry_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_109_capitulation_signal},
    "vdry_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_110_capitulation_signal},
    "vdry_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_111_capitulation_signal},
    "vdry_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_112_capitulation_signal},
    "vdry_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_113_capitulation_signal},
    "vdry_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_114_capitulation_signal},
    "vdry_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_115_capitulation_signal},
    "vdry_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_116_capitulation_signal},
    "vdry_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_117_capitulation_signal},
    "vdry_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_118_capitulation_signal},
    "vdry_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_119_capitulation_signal},
    "vdry_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_120_capitulation_signal},
    "vdry_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_121_capitulation_signal},
    "vdry_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_122_capitulation_signal},
    "vdry_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_123_capitulation_signal},
    "vdry_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_124_capitulation_signal},
    "vdry_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_125_capitulation_signal},
    "vdry_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_126_capitulation_signal},
    "vdry_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_127_capitulation_signal},
    "vdry_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_128_capitulation_signal},
    "vdry_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_129_capitulation_signal},
    "vdry_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_130_capitulation_signal},
    "vdry_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_131_capitulation_signal},
    "vdry_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_132_capitulation_signal},
    "vdry_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_133_capitulation_signal},
    "vdry_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_134_capitulation_signal},
    "vdry_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_135_capitulation_signal},
    "vdry_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_136_capitulation_signal},
    "vdry_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_137_capitulation_signal},
    "vdry_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_138_capitulation_signal},
    "vdry_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_139_capitulation_signal},
    "vdry_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_140_capitulation_signal},
    "vdry_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_141_capitulation_signal},
    "vdry_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_142_capitulation_signal},
    "vdry_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_143_capitulation_signal},
    "vdry_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_144_capitulation_signal},
    "vdry_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_145_capitulation_signal},
    "vdry_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_146_capitulation_signal},
    "vdry_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_147_capitulation_signal},
    "vdry_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_148_capitulation_signal},
    "vdry_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_149_capitulation_signal},
    "vdry_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_150_capitulation_signal},
}
